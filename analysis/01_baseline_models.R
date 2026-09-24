#!/usr/bin/env Rscript
# 01_baseline_models.R
# --------------------
# Refits the Del Matto (2018) baseline models from the original extraction
# spreadsheet (exact Hedges' g and sampling variances, archived in the 2018
# analysis repository) and writes every model quantity used by the manuscript
# to build/model_results.json. scripts/build_results.py formats these values
# into build/results.json; scripts/figures.py plots them.
#
# Model specifications follow analysis/original_2018/meta-analysis.script.Rmd,
# with two corrections:
#   * Typical sampling variance (Nakagawa & Santos 2012, Eq. 22) uses weights
#     w_i = 1 / v_i. The 2018 script used w_i = 1 / sqrt(v_i), which inflates
#     the typical sampling variance and understates I^2. Both are reported.
#   * Small-study effects are tested with a multilevel Egger regression
#     (sqrt(v_i) as a moderator in the full rma.mv model; Nakagawa et al. 2022).
#     The 2018 script regressed residuals on v_i with lm() and interpreted the
#     intercept rather than the slope.
#
# Usage (from repository root):
#   Rscript analysis/01_baseline_models.R

suppressPackageStartupMessages({
  library(ape)
  library(geiger)
  library(phytools)
  library(metafor)
  library(jsonlite)
})

in_dir <- "data/input/delmatto2018_original"
dir.create("build", showWarnings = FALSE)

# ── Data and phylogeny (as in the 2018 script) ────────────────────────────────
dat_all <- read.csv(file.path(in_dir, "data_for_analysis.csv"), sep = ";",
                    fileEncoding = "UTF-8-BOM", stringsAsFactors = FALSE)
dat_all <- dat_all[, !grepl("^X", names(dat_all))]

tree <- read.tree(file.path(in_dir, "fish_tree.tre"))
phy <- compute.brlen(tree, method = "Grafen")
uniq <- data.frame(spp = sort(unique(dat_all$animal_on_tree)))
rownames(uniq) <- uniq$spp
missing_tips <- name.check(phy, uniq)$data_not_tree
for (s in missing_tips) phy <- add.species.to.genus(phy, s, where = "root")

# 24 absolute gonad-mass effect sizes were excluded in the original Methods
dat <- subset(dat_all, is_abs_gonad_size == 0)
dat$phylo <- dat$animal_on_tree
dat$category <- factor(dat$variable.type1,
                       levels = c("allocation", "production_1", "production_0", "quality"),
                       labels = c("allocation", "gsi", "quantity", "quality"))

phy_ma <- compute.brlen(drop.tip(phy, which(!phy$tip.label %in% dat$animal_on_tree)),
                        method = "Grafen")
cor_ma <- vcv(phy_ma, corr = TRUE)

# ── Helpers ───────────────────────────────────────────────────────────────────
typical_v <- function(v, w) {
  k <- length(w)
  sum(w * (k - 1)) / (sum(w)^2 - sum(w^2))
}

i2 <- function(model, v, labels) {
  s2 <- setNames(model$sigma2, labels)
  out <- function(s2m) as.list(round(100 * c(total = sum(s2), s2) / (sum(s2) + s2m), 2))
  list(corrected = out(typical_v(v, 1 / v)),
       original_2018 = out(typical_v(v, 1 / sqrt(v))))
}

coefs <- function(model) {
  lapply(setNames(seq_along(model$b), rownames(model$b)), function(j)
    list(est = model$b[j], se = model$se[j], ci_low = model$ci.lb[j],
         ci_high = model$ci.ub[j], z = model$zval[j], p = model$pval[j]))
}

egger <- function(model) {
  e <- update(model, mods = as.formula(paste(
    deparse(model$formula.mods %||% ~1), "+ sqrt(es_var)")))
  j <- which(rownames(e$b) == "sqrt(es_var)")
  list(slope = e$b[j], se = e$se[j], z = e$zval[j], p = e$pval[j])
}
`%||%` <- function(a, b) if (is.null(a)) b else a

re_phylo <- list(~1 | paper.number, ~1 | animal_on_tree, ~1 | phylo)
re_nophylo <- list(~1 | paper.number, ~1 | animal_on_tree)

# ── Null model: study + species + phylogeny ───────────────────────────────────
m0 <- rma.mv(es_hedges_g, es_var, random = re_phylo, R = list(phylo = cor_ma),
             method = "REML", data = dat)

# ── Model 1: trait category (phylogeny dropped, as in the 2018 dissertation) ──
m1 <- rma.mv(es_hedges_g, es_var, mods = ~ category - 1, random = re_nophylo,
             method = "REML", data = dat)
m1_phylo <- rma.mv(es_hedges_g, es_var, mods = ~ category - 1, random = re_phylo,
                   R = list(phylo = cor_ma), method = "REML", data = dat)

# ── Model 2: category x SCR, observational studies, no allocation ─────────────
dat_obs <- subset(dat, type.of.study == "obs" & category != "allocation")
dat_obs$category <- droplevels(dat_obs$category)
m2 <- rma.mv(es_hedges_g, es_var, mods = ~ factor(sperm.comp.rank) %in% (category - 1),
             random = re_nophylo, method = "REML", data = dat_obs)
# Does SCR explain variation beyond trait category? (likelihood-ratio test, ML fits)
m2_ml <- update(m2, method = "ML")
m2_base_ml <- rma.mv(es_hedges_g, es_var, mods = ~ category - 1, random = re_nophylo,
                     method = "ML", data = dat_obs)
lrt_scr <- anova(m2_ml, m2_base_ml)

# ── Assemble output ───────────────────────────────────────────────────────────
res <- list(
  source = "data/input/delmatto2018_original/data_for_analysis.csv",
  metafor_version = as.character(packageVersion("metafor")),
  summary = list(
    n_rows_all = nrow(dat_all),
    n_effects = nrow(dat),
    n_abs_gonad_excluded = sum(dat_all$is_abs_gonad_size == 1),
    n_studies = length(unique(dat$paper.number)),
    n_studies_all_rows = length(unique(dat_all$paper.number)),
    n_species = length(unique(dat$animal)),
    n_tips = Ntip(phy_ma),
    n_tips_added_at_genus_root = length(missing_tips),
    n_by_category = as.list(table(dat$category)),
    n_extreme = sum(abs(dat$es_hedges_g) > 8),
    max_abs_g = max(abs(dat$es_hedges_g)),
    k_model2 = nrow(dat_obs)
  ),
  null = list(coef = coefs(m0)[[1]], sigma2 = m0$sigma2,
              i2 = i2(m0, dat$es_var, c("study", "species", "phylo")),
              egger = egger(m0), aic = AIC(m0)),
  model1 = list(coef = coefs(m1),
                i2 = i2(m1, dat$es_var, c("study", "species")),
                egger = egger(m1), aic = AIC(m1), aic_with_phylo = AIC(m1_phylo)),
  model2 = list(i2 = i2(m2, dat_obs$es_var, c("study", "species")),
                egger = egger(m2),
                lrt_scr = list(chi2 = lrt_scr$LRT, df = lrt_scr$parms.f - lrt_scr$parms.r,
                               p = lrt_scr$pval))
)

write_json(res, "build/model_results.json", auto_unbox = TRUE, digits = NA, pretty = TRUE)

# Effect-level data for the funnel plot
write.csv(data.frame(es_id = dat$es_id, study = dat$paper.number, species = dat$animal,
                     category = dat$category, yi = dat$es_hedges_g, vi = dat$es_var,
                     resid = residuals(m1)),
          "build/effect_sizes.csv", row.names = FALSE)

cat("Wrote build/model_results.json and build/effect_sizes.csv\n")
