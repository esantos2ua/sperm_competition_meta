# Summary of the meta-analysis to be updated

**Source work:** Del Matto, L. A. (2018). *Sperm competition games between majors and minors: a
meta-regression of fishes with alternative mating tactics.* MSc dissertation ("Dissertação de Mestrado",
Versão original), Instituto de Biociências, **Universidade de São Paulo**, Departamento de Zoologia.
Supervisor: Prof. Dr. Eduardo da Silva Alves dos Santos. São Paulo, **Maio de 2018**; 50 f. + anexo.
Funding acknowledged: **CNPq** and **CAPES**. **Unpublished** — no journal version exists.

This document summarizes the original study. It is the starting point for the protocol of the planned
**update** of this meta-analysis, which is also the route by which the work will be brought to publication.

All numbers below are taken from the high-fidelity markdown conversion of the source PDF,
[`../references/DelMatto2018_dissertation.md`](../references/DelMatto2018_dissertation.md) (physical page
indices in that file run **two ahead** of the printed folios).

---

## 1. Background and rationale

- Sperm competition — competition among the sperm of different males to fertilize a female's ova — is one of
  the processes that shape mating behaviour within and across species (Parker 1970, 1998).
- **Sperm competition game models** (Parker 1990a, 1990b, 1998; Parker et al. 2012) assume that (i) sperm
  production is costly (Dewsbury 1982; Wedell et al. 2002), (ii) males trade off allocation between ejaculate
  expenditure and acquiring matings (Parker 1998; Kvarnemo & Simmons 2013), and (iii) greater ejaculate
  expenditure increases fertilization success (Parker 1998; Martin et al. 1974). A central across-species
  prediction is that males invest more in ejaculates where the degree of sperm competition is higher, with
  supporting evidence in several taxa (Stockley et al. 1997; Byrne et al. 2002; Pitcher et al. 2005; Ramm et
  al. 2005).
- In species with **alternative mating tactics (AMTs)**, males of different phenotypes face *different* sperm
  competition risk purely because of their phenotype (Parker 1990b; Taborsky 1998). **Minors** (sneakers)
  always mate inside another male's territory and should therefore always face sperm competition; **majors**
  defend territories or females, can prevent females from mating with other males, and therefore face lower
  risk.
- **Parker's (1990b) "sneak–guard" model** predicts (i) that **minors invest more in ejaculate traits than
  majors**, and (ii) that as the **proportion of minors in a population increases**, majors should increase
  their expenditure until it approaches that of minors. Consequently the *difference* between majors and
  minors should be **greatest at intermediate levels** of sperm competition and small when sperm competition
  is very low or very high — i.e. a **curvilinear (hump-shaped)** relationship.
- Previous tests were single-taxon and equivocal. A comparative analysis of dimorphic *Onthophagus* dung
  beetles supported the first prediction (minors had proportionally larger testes) but **not** the second
  (Simmons et al. 2007). Studies of testis size and sperm competition in AMT species more broadly have found
  conflicting patterns (Smith & Ryan 2010; Simmons et al. 1999; Byrne 2004; Kelly 2008), and whether sperm
  *quality* traits consistently respond to sperm competition is contested (Snook 2005).
- **Fishes** were chosen because external fertilization is the norm (Montgomerie & Fitzpatrick 2009) and
  group spawning is common, which favours both AMTs and sperm competition (Taborsky 2008). The dissertation
  states that, as far as the author was aware, **no study had tested these predictions in an analysis across
  species with alternative male phenotypes**, and it presents itself as "the first meta-analysis testing
  Parker's (1990b) predictions about sperm competition in species with male alternative phenotypes".

### Terminology / conventions used in the dissertation

- **Majors:** males that usually defend territories or females (Taborsky et al. 2008); sometimes court and are
  more attractive to females.
- **Minors:** males that usually do not defend territories or females (Taborsky et al. 2008); less exuberant,
  use sneak copulations inside a major's territory.
- **Ejaculate expenditure** is not treated as a single trait. Response variables were sorted into three
  **sperm expenditure categories** (full list in the dissertation's Table 1):
  - **Production** — investment in sperm number or sperm volume; **subdivided** into
    - **Production/Quantity** (sperm density, sperm count, sperm volume, …), and
    - **Production/GSI** — "the only variable classified as Production/GSI was the Gonadal Somatic Index
      (GSI; either total body mass based, soma mass based and in one case energy based)".
    - *All variables of absolute gonad mass were **excluded** "because they are not independent from GSI".*
  - **Quality** — traits making sperm more fertile: sperm velocity (average path, straight-line,
    curvilinear), sperm length (total, flagellum, midpiece, head, end piece), ATP concentration, motility,
    longevity, enzyme activity (pyruvate kinase, citrate synthase), seminal vesicle mass and the **Seminal
    Vesicle Somatic Index (SVSI)**, testicular gland index/area, accessory gland mass.
  - **Allocation** — facultative, immediate responses modulated at ejaculation: sperm concentration in the
    water, number of ejaculations per spawning, sperm per spawn, proportion of sperm delivered relative to
    sperm at rest.
- **Repeated measures over time:** where motility/velocity were measured at several times post-activation,
  only the **first measurement after activation** was extracted.
- **Sperm competition rank (SCR)** — the species-level proxy for sperm competition intensity, "proposed by
  Stockley et al. (2007)" [*sic*; only Stockley et al. **1997** appears in the reference list], ranging
  **0 to 5** in discrete categories:
  - **0** — internal fertilization (including mouth-brooding), no polygamy or group spawning.
  - **1** — internal fertilization with low group spawning or polygamy, **or** external fertilization with
    pairing and no group spawning.
  - **2** — internal fertilization with a high degree of group spawning or polygamy, **or** external
    fertilization with pairing and low incidence of group spawning.
  - **3** — external fertilization with pairing and moderate group spawning, **or** no pairing and low group
    spawning.
  - **4** — external fertilization with pairing and a high incidence of group spawning, **or** no pairing and
    low group spawning.
  - **5** — no pairing and a high level of group spawning.
  - Level 5 = highest sperm competition, level 0 = least. Species were ranked from **life-history data
    obtained from the literature**; similar ranks are cited as used by Byrne et al. (2002) and Fitzpatrick et
    al. (2009). The abstract describes the rank as having "five levels, from 1 … to 5".
  - The dissertation states explicitly that the **best** proxy would have been **the proportion of minor males
    in the population** at the time of data collection, but that "most of the studies in the dataset did not
    report the proportion of minors", so SCR was used instead.
- **Sign convention (Hedges' *g*):** **positive *g*** = greater mean value for **majors**; **negative *g*** =
  greater mean value for **minors**. Directionality was corrected accordingly when *g* was computed from
  inferential statistics. Benchmarks of 0.2 / 0.5 / 0.8 for small / medium / large effects (Cohen 1969).

## 2. Objectives

To test, with a phylogenetic meta-regression across fish species with male AMTs, the two predictions of
Parker's sneak–guard model. Stated as predictions in the Methods:

1. There is a **significant difference in investment in sperm-competition traits between minor and major
   males, for all subtypes of investment** (quantity, GSI, quality and allocation), with **minors investing
   more than majors**.
2. The **difference between minors and majors is greatest in species with an intermediate sperm competition
   rank**, and smaller in species with higher and lower ranks, **for all subtypes** of sperm investment.

## 3. Data sources and scope

- **Literature search:** the platforms ***Web of Knowledge*** (basic search, all databases) and ***Scopus***
  (advanced search). Search **last updated 16 May 2017**. A single Boolean string was used in both:

  ```
  ("alternat* sex* behavio*r*" OR "alternat* sex* role*" OR "alternat* sex* phenotype*" OR
   "alternat* sex* tactic*" OR "alternat* sex* strateg*" OR "alternat* reproductive behavio*r*" OR
   "alternat* reproductive role*" OR "alternat* reproductive phenotype*" OR
   "alternat* reproductive tactic*" OR "alternat* reproductive strateg*" OR
   "alternat* mating behavio*r*" OR "alternat* mating role*" OR "alternat* mating phenotype*" OR
   "alternat* mating tactic*" OR "alternat* mating strateg*" OR "reproductive role*" OR
   "reproductive phenotype*" OR "reproductive tactic*" OR "reproductive strateg*" OR
   "mating role*" OR "mating phenotype*" OR "mating tactic*" OR "mating strateg*" OR
   "male* *morph*")
  AND
  ("sperm competition" OR "testis size" OR "ejaculate" OR "sperm allocation" OR "post*copulato*")
  ```

- **Yield:** *Web of Knowledge* **868** results; *Scopus* **682** results; after removing duplicates,
  **1,103 distinct records**. Screening is illustrated by a **PRISMA flow diagram** (Fig. 1; Moher et al.
  2009) — which is a vector figure in the PDF and is **not text-extractable**, so the flow numbers below come
  from the prose.
- **Title/abstract screening → 205 articles.**
- **Full-text screening:** "we read **191 articles** (of the **205** in our dataset; **14 articles were not
  screened because of time constraints**)"; then, two sentences later, "After reading the full text of **192
  articles**, we kept **50 studies** in our dataset." *(The 191 vs. 192 mismatch is unresolved in the text;
  see §7.)*
- **Final dataset (as stated):** **183 effect sizes** from **50 studies** and **29 fish species**
  (Supplementary Table 1). Breakdown given: **65** production (35.5%) = **31 GSI** + **34 Quantity**;
  **107** quality (58.5%); **11** allocation (6%).
- **Effect size:** **Hedges' *g*** (Hedges 1981), the standardized difference between two group means with a
  small-sample correction. Computed from group means and SDs where possible; SD derived from SE or the 95% CI
  when SD was not reported; and computed from **inferential statistics** (*t*, one-way ANOVA *F*,
  Wilcoxon matched-pair signed-rank, Mann–Whitney *U*) using the **Practical Meta-Analysis Effect Size
  Calculator** (Wilson 2018) when no descriptive statistics or plots were available.
- **Figure digitising:** ***GraphClick*** v. 3.0.3 (Arizona Software 2012) or the ***metaDigitise*** R package
  (Pick et al. 2018).
- **Data availability:** the dissertation contains **no data availability statement, no analysis code, and no
  reference to any repository** (no OSF / Dryad / Zenodo / figshare / GitHub). The only machine-recoverable
  artefacts are, in the *Supplementary Material*:
  - **Supplementary Table 1** — one row per effect size with exactly seven columns: *Species*, *Hedges' g*,
    *N*, *SCR*, *Original response variable*, *Variable type* (production / quality / allocation), *Source*.
    **It does not contain per-group means, SDs/SEs, or per-morph sample sizes**; *N* is a **single** value
    described in the caption as "sample sizes (number of males investigated) reported in the original
    articles", and **no sampling variance is reported**. It also does **not** contain the Quantity-vs-GSI
    sub-category, nor the observational-vs-experimental flag used to subset model 2.
  - **Supplementary Figure 1** — a phylogeny of the included species (**29 tips**). Its **branches are vector
    art, so the topology itself is not machine-readable**; the **tip labels do extract as text** in the
    conversion, and a raster of the whole page is available at
    [`../references/figures/p38_img0.png`](../references/figures/p38_img0.png). No tree file, no branch lengths,
    and **no statement of where the topology came from**.
  - This is the key consideration for the reproduction step of the update (see §8).

### Inclusion / selection criteria (abridged)

**First pass (titles and abstracts):**

1. Studied one or more **fish** species/populations.
2. Some indication that males of the species have **at least two distinct mating tactics** (different morphs
   or different specific behaviours).
3. The abstract indicated that **both male phenotypes were compared** with respect to characteristics involved
   in sperm competition and/or body size.

**Second pass (full text):**

1. Confirmation the study was about **fish** species.
2. Species were **not hermaphrodite**.
3. Confirmation that males have **at least two described mating tactics**.
4. Male phenotypes were compared for **characteristics involved in sperm competition** (regardless of body-size
   comparisons).
5. Presence of **"proper statistics"** — the study reports the **mean** of the response variable, the **sample
   size**, and **SD or SE**; or data recoverable from figures; or, failing that, **inferential statistics whose
   direction of effect the authors report** (which phenotype had the larger trait).

### Coded study traits (moderators)

Only two moderators were used, and only one of them varies within a species:

- **Type of investment variable** (sperm expenditure category), fitted with **four levels**: *allocation*,
  *production as sperm quantity*, *production as GSI*, *quality*.
- **Sperm competition rank (SCR)**, fitted as a **categorical variable with five levels** (1–5). SCR is a
  **species-level constant** assigned from literature life-history data.
- Additional fields recorded in Supplementary Table 1 but not used as moderators: species, sample size *N*,
  the original response variable name, and the source study.
- An **observational vs. experimental/laboratory** distinction was used to *subset* the data for model 2
  (experimental/laboratory effect sizes were dropped) but is **not reported per effect size** anywhere in the
  document.

## 4. Statistical methods

- **Software:** the function ***`rma.mv`*** in the ***`metafor`*** package (Viechtbauer 2010) in **R version
  3.4.0** (R Core Team 2017). Effect sizes were "deemed to be statistically significant when 95% confidence
  intervals (CI) did not overlap zero" — no *p*-values or omnibus moderator tests (*Q*_M) are reported for the
  meta-regressions.
- **Null model:** intercept only, with **three random effects** — **study (paper) identity + species identity +
  phylogeny**. *(Inferred: the Methods never describe a null model; it appears only in Tables 2 and 3, where its
  row carries `Moderators = NA`.)*
- **Meta-regression model 1:** moderator = **variable type** (4 levels), **parameterized to return the mean
  meta-analytic estimate for each level** (so each level could be tested against zero) rather than as
  contrasts against a reference level. Random effects: study identity + species identity (**phylogeny removed**
  because it "explained virtually no variation").
- **Meta-regression model 2:** moderator = **variable type : sperm competition rank** interaction, again
  parameterized so that "the interactions were restricted to each level" of variable type. Fitted to a
  **subset**: allocation effect sizes removed (small *n*), and, because most remaining effect sizes came from
  observational studies in natural settings, "the small number of effect sizes from experimental/laboratory
  studies" was **also removed**. Random effects: study identity + species identity (phylogeny again removed).
- **Heterogeneity:** a **modified *I*² metric** following **Nakagawa & Santos (2012)** [cited in the Methods
  but **absent from the reference list**], reported as total *I*² and per-random-effect *I*² with 95% CIs. For
  the phylogeny random effect, *I*² is interpreted as analogous to **phylogenetic signal** (Housworth et al.
  2004).
- **Publication bias / sensitivity analysis:** **Egger's regressions** (Egger et al. 1997) on each of the three
  models, reported as an intercept with a *t*- and *p*-value. No funnel plots, no time-lag analysis, no
  leave-one-out or outlier analyses are reported; the "Sensitivity analysis" section contains only the Egger
  regressions and the *I*² decomposition.
- **Non-independence:** handled only through the study-identity and species-identity random intercepts. No
  variance–covariance matrix for shared controls or shared males, and no explicit effect-size-level
  (observation) random effect is described — the text names exactly "paper identity, species identity and also
  a phylogeny term".

## 5. Key results

**Overall (null) model**

- Mean effect **−0.519 (95% CI −1.317 to 0.278)** — negative (minors > majors) and moderate in magnitude, but
  **the CI overlapped zero**.
- Total heterogeneity ***I*² = 83.21% (81.60 to 85.44)**; partitioned as **study identity 55.46% (53.54 to
  57.38)**, **species identity 9.35% (7.43 to 11.28)**, **phylogeny 18.38% (16.46 to 20.30)**.

**Meta-regression model 1 (variable type)** — the headline result, plotted as Fig. 2:

| Variable type | Hedges' *g* | 95% CI | Interpretation |
|---|---|---|---|
| **Allocation** | **+2.732** | 1.476 to 3.989 | **Majors** allocate significantly more sperm; large effect |
| **Production / GSI** | **−2.638** | −3.105 to −2.177 | **Minors** invest significantly more in gonad mass relative to body size |
| **Production / Quantity** | −0.384 | −0.845 to 0.076 | small, non-significant |
| **Quality** | −0.251 | −0.699 to 0.197 | small, non-significant |

- Total *I*² = **83.52% (81.60 to 85.44)**; study identity **76.02% (74.10 to 77.94)**; species identity
  **7.50% (5.58 to 9.42)** per Table 2 — note the Results **text** instead reports "the species identity
  (9.35%)", which is the *null model's* value (see §7). **Phylogeny removed** from the model.

**Meta-regression model 2 (variable type × SCR)**

- "Within each type of investment variable, we found little evidence that the level of sperm competition
  influenced the difference in investment between minors and majors" — the magnitude of the major–minor
  difference "was similar across the range of sperm competition ranks".
- Total *I*² = **82.57% (80.65 to 84.50)**; study identity **46.24% (44.32 to 48.16)**; species identity
  **36.33% (34.41 to 38.25)**. **Phylogeny removed.**
- **No coefficient table for this model exists in the document.** The text cites "(Table 3; Fig. 3)", but
  Table 3 is the Egger's-regression table; the model-2 estimates appear **only** in Fig. 3, a vector plot that
  is not text-extractable. The Discussion adds only a qualitative statement that "even if we consider the
  tendency of the average effect size coefficients (not considering their 95% CIs) it seems that the sperm
  trait expenditure is behaving contrary to Parker's prediction".

**Egger's regressions (Table 3)** — "little evidence of publication bias":

| Model | Intercept | *t* | *p* |
|---|---|---|---|
| Null model | −0.323 | −0.633 | 0.528 |
| Meta-regression model 1 | −0.338 | −0.664 | 0.507 |
| Meta-regression model 2 | −0.610 | −1.067 | 0.288 |

## 6. Main conclusions

- Presented as **the first meta-analysis testing Parker's (1990b) predictions** about sperm competition in
  species with male alternative phenotypes, using **29 fish species**.
- **Overall, minors invest more than majors** in ejaculate traits, "yet this overall result was not
  statistically significant".
- **Minors invest significantly more in relative gonad size (GSI)**, supporting one of Parker's predictions.
- **Sperm quantity *per se* is similar** between majors and minors. Combined with the GSI result, the author
  infers that (i) both tactics have similar amounts of sperm available per spawning event, so both experience
  similar sperm competition risk per spawning, and (ii) the larger relative gonad investment by minors means
  minors can **replenish sperm stocks faster** than majors, consistent with minors mating more frequently.
- **Sperm quality does not differ** between majors and minors at any sperm competition level, suggesting sperm
  quality "is not under such strong selection as gonad mass"; discussed against Smith & Ryan (2010) and
  Parker's (1993) prediction that quality traits respond most when sperm-number evolution is constrained.
- **Contrary to prediction, majors allocate significantly more sperm than minors** per spawning bout. The
  author flags this as the opposite of game-theory expectations, notes the small sample (**n = 11**), and
  explicitly "encourage[s] researchers to conduct more experiments manipulating the number of sneakers and
  comparing sperm allocation between majors and minors".
- **No support for the second prediction:** SCR had "very little influence" on the magnitude of the major–minor
  difference — mirroring Simmons et al.'s (2007) *Onthophagus* result.
- The proposed explanation is an **assumption violation**: Parker's (1990b) sneak–guard model assumes a major
  faces sperm competition from **one minor at a time**, whereas most species in the dataset are **external
  fertilizers** in which several minors may sneak on the same spawning. Hence "the risk of sperm competition,
  even at low levels (such as a sperm competition rank of 1), should be strong enough to cause the investment
  patterns we observe".
- Overall conclusion: in fishes with AMTs, **both majors and minors are under strong selection from sperm
  competition, even when the risk of polyandry is low**.

## 7. Notable limitations (relevant to the update)

- **The stated number of effect sizes differs from the row count of Supplementary Table 1 — identified and
  resolved.** We counted the actual rows and distinct entries in Supplementary Table 1 as converted:

| Quantity | Stated in the Results text | Counted in Supplementary Table 1 | Agreement |
|---|---|---|---|
| Studies (sources) | **50** | **50** | ✔ agrees |
| Fish species | **29** | **29** | ✔ agrees |
| Effect sizes (total rows) | **183** | **207** | 24 more rows — the excluded absolute gonad masses (resolved below) |
| — Quality | 107 | **107** | ✔ agrees |
| — Allocation | 11 | **11** | ✔ agrees |
| — Production (total) | 65 | **89** | 24 more — same 24 rows (resolved below) |
| — Production / GSI | 31 | **31** | ✔ agrees |
| — Production / Quantity | 34 | **34** (89 − 31 GSI − 24 absolute masses) | ✔ agrees |

  *Counting notes.* 207 is the number of data rows after removing 3 rows that are pure line-wrap artefacts of
  the PDF→markdown conversion (continuation fragments of the *Source* cell for Leach & Montgomerie 2000, Koseki
  & Maekawa 2002 and Hurtado-Gonzales & Uy 2009). The 50 sources require merging the same three split cells
  and nothing more: 53 raw *Source* strings minus those 3 fragments is exactly 50 (one source is printed in the
  parenthetical form "(Serrano et al., 2006)", but that is cosmetic and does not create a duplicate string).
  The 29 species require treating ***Parablennius parvicornis*** and ***Parablennius sanguinolentus
  parvicornis*** as one species (29 species also equals the number of tips in Supplementary Figure 1).
  **GSI = 31 exactly** if the rows labelled `GSI` (22), `GSI (%)` (6), `GSI (energy based)` (2) and
  `adjusted IG` (1) are counted together — which matches the stated 31 and validates the classification.

  **The explanation, and the reconciliation.** Supplementary Table 1 is the **full extraction table**,
  including the variables the Methods say were dropped from the analysis, even though its caption reads "List
  of effect sizes **used in** this meta-analysis". Exactly **24 rows** record an **absolute gonad or testis
  mass or weight** — verbatim from the *Original response variable* column: `gonad mass (g)` ×8,
  `gonad mass (mg)` ×3, `testes mass (g)` ×3, and one row each of `gonad mass`, `gonad weight (mg)`,
  `gonad wet mass (g)`, `gonad wet weight (g)`, `total gonad weight (g)`, `testes mass`, `testes weight (g)`,
  `testis mass (g)`, `mass of testis (mg)` and `absolute mass of testes`. These are precisely the class the
  Methods say was dropped: "we excluded all variables of gonad mass because they are not independent from
  GSI". (The row labelled `testes corrected for body mass` is **not** in this set: it is a body-size-corrected
  index, so the exclusion rule does not reach it.)

  Excluding exactly those 24 rows reconciles the appendix with the Results on **all four** sub-counts:
  207 − 24 = **183** total; 89 − 24 = **65** Production; of which GSI-type = **31** and the remainder
  = **34** Quantity; with Quality **107** and Allocation **11** untouched. The dissertation's own printed
  percentages corroborate 183 as the analysed *N* (65/183 = 35.5%, 107/183 = 58.5%, 11/183 = 6.0%, exactly as
  printed). **The analysed dataset can therefore be reconstructed exactly** from Supplementary Table 1 by
  applying the dissertation's own documented exclusion rule — a positive reproducibility finding rather than an
  outstanding discrepancy. Confirming this reconstruction in code is a named step of the Q0 reproduction (see
  [`02_update_protocol.md`](02_update_protocol.md) §3.1). What remains genuinely unrecoverable is not the row
  set but the **weights**: the table archives no per-morph means, SDs or sample sizes (next bullet).

- **The reported dataset cannot be reweighted as archived.** Supplementary Table 1 gives *g* and a single *N*
  per row but **no per-group means, SDs, or per-morph sample sizes and no sampling variance**. Hedges' *g*'s
  variance requires *n*₁ and *n*₂ separately, so the inverse-variance weights used in the original models
  **cannot be recovered exactly** — only approximated (e.g. assuming *n*₁ = *n*₂ = *N*/2). Two further
  analysis-critical fields are also absent from the table: the **Quantity-vs-GSI sub-category** (must be
  re-derived from the free-text response-variable strings) and the **observational-vs-experimental flag** used
  to subset model 2.
- **Implausibly large effect sizes suggest extraction or computation errors.** Eight rows have |*g*| > 8, up to
  |*g*| = **78.624** (*Sufflogobius bibarbatus*, seminal vesicle mass, Seivåg et al. 2016), **54.723**
  (*Lepomis macrochirus*, sperm density, Burness et al. 2005), **−48.947** and **−23.531** (*Salmo salar*,
  relative sperm volume and number, Gage et al. 1995), **−17.716** (*S. bibarbatus*, testes mass), **14.018**
  and **10.219** (*S. salar*), **−8.088** (*Symphodus melops*, GSI). Twenty-two rows have |*g*| > 3. Values of
  this magnitude are not credible as standardized mean differences on raw data and most plausibly arise from
  SE being treated as SD, from log-scaled or per-kg data, or from digitising error. No outlier or influence
  analysis was performed.
- **The sperm competition rank is confounded with species and is severely unbalanced.** SCR is a species-level
  constant, so with 29 species there are only 29 independent values. In the table, **SCR 1 is represented by a
  single species** (*Gobius niger*, 15 effect sizes) and **SCR 5 by a single species** (*Axoclinus
  nigricaudus*, **3** effect sizes, all from Neat 2001). Row counts by rank are 1: 15, 2: 58, 3: 93, 4: 38,
  5: 3; species counts by rank are 1: 1, 2: 9, 3: 11, 4: 7, 5: 1 (rank 4 is 7, not 8, once the two
  *Parablennius* entries are merged into one species, so the ranks sum to the stated 29). **No effect size has
  rank 0**, despite the
  scale being defined from 0. The variable type × SCR interaction therefore asks a 15-cell question of a
  dataset whose extreme cells are one species deep — i.e. the ranks at which Parker's model makes its sharpest
  predictions are the ones with essentially no replication.
- **The prediction actually tested is not the prediction the model makes.** Parker's (1990b) prediction is a
  **curvilinear** relationship with a maximum at intermediate risk, but SCR was fitted as an **unordered
  five-level factor** interacted with variable type, and **no test of curvature** (e.g. a quadratic term on
  rank), and **no omnibus test of the interaction**, is reported. The conclusion of "little evidence" rests on
  visual inspection of CIs in Fig. 3.
- **Model-2 estimates are not reported numerically anywhere.** The cross-reference points to Table 3, which is
  the Egger's table. There is thus **no numerical target** against which model 2 can be reproduced, other than
  its *I*² values and Egger intercept.
- **An internal inconsistency in the Results text.** The species-identity *I*² for model 1 is reported as
  9.35% in the prose but 7.50% in Table 2 (9.35% is the null model's value). The *I*²_total 95% CI for the
  null model and for model 1 are also printed identically (81.60 to 85.44).
- **Screening was incomplete and asymmetric.** **14 of the 205** title/abstract-eligible articles were "not
  screened because of time constraints", and the prose gives both **191** and **192** as the number of
  full texts read. The dissertation twice flags itself as provisional, calling it "the current version of this
  manuscript" (physical p. 15) and "this version of the manuscript" (physical p. 16), i.e. the dataset was
  explicitly work in progress.
- **Category coding is internally inconsistent for gland/vesicle masses.** Absolute gonad mass was excluded as
  non-independent of GSI, yet **absolute seminal vesicle mass**, **absolute accessory gland mass** and
  **testicular gland area** were retained inside the *Quality* category (one row each), alongside their
  body-size-corrected counterparts (SVSI ×4, `accessory gland corrected for body mass`, TGI). The
  same-study pairing of absolute and relative versions of the same organ is not flagged. Mirroring this, two
  rows filed under *Quality* are in fact **quantity** traits — `sperm density (sperm/mL)` and `spermatocrit`
  (one row each) — so the Quality/Quantity boundary is not applied consistently either.
- **Taxonomic concentration.** Of the 207 rows, **63 (30%)** are salmonids (*Salmo salar* 31, *Oncorhynchus
  tshawytscha* 20, *O. masou* 4, *O. nerka* 3, *Salvelinus alpinus* 5), **32** are gobies, **23** are Lake
  Tanganyika cichlids, and **18** are bluegill (*Lepomis macrochirus*); the five most-represented species
  supply **96/207 (46%)** of all effect sizes. Sample sizes per row range from **N = 9 to N = 182**.
- **The allocation result — the one that contradicts theory — is the thinnest.** All **11** allocation effect
  sizes come from **4 studies and 5 species**; 8 of the 11 are from Pilastro et al. (2002) alone, and the
  single largest value (*g* = **+7.943**, *Poecilia reticulata*, "proportion of sperm delivered", Pilastro &
  Bisazza 1999) comes from an **internally fertilizing** poeciliid, whose "allocation" is insemination
  efficiency rather than sperm release into water. The unweighted mean of the 11 values is ≈ +0.88, versus a
  model estimate of +2.732.
- **Phylogeny was dropped, and its provenance is undocumented.** Phylogeny carried *I*² = 18.38% in the null
  model but was removed from both meta-regressions for explaining "virtually no variation"; the tree in
  Supplementary Figure 1 has no stated source, no branch lengths, and no accompanying file.
- **GSI is a ratio index and majors and minors differ in body size by definition** in many AMT species; the
  dissertation does not address the well-known allometric problems of testing relative-investment differences
  between size-divergent morphs, nor does it retain body mass as a covariate.
- **No open data, no code, no registration.** There is no data availability statement, no analysis script, no
  repository, and no protocol registration. All *R* work was done in R 3.4.0 with `metafor` at an unstated
  version.
- **Search vintage and scope.** The search ended **16 May 2017** — roughly **nine years** (nine years and two
  months, to the 28 Jul 2026 protocol date) of subsequent
  primary literature is missing. Only two platforms were queried, with an English-only Boolean string, no grey
  literature, no reference-list snowballing described, and no attempt to contact authors for missing data.
- **Single-taxon and single-reviewer.** The synthesis is fish-only, so the generality of the major/minor
  pattern to other AMT taxa is untested (the only comparison point is a single beetle genus). Screening and
  extraction appear to have been done by one person; no inter-reviewer reliability is reported. The
  Acknowledgements credit B. Buzatto with contributing to the initial data-collection stages and the
  supervisor with performing the data analysis jointly with the author.

## 8. Opportunities for the update (to be refined in the formal protocol)

The planned update follows a **reproduce-then-update** design with two research questions (see
[`02_update_protocol.md`](02_update_protocol.md)): **Q0** reconstructs the 2018 dataset from Supplementary
Table 1 and re-implements the original models to recover the reported estimates; **Q1** then updates the
synthesis with roughly nine years of new evidence and contemporary methods, with the explicit goal of
**publishing** the synthesis.

- **Reconstruct-then-reproduce first (Q0):** because no dataset or code was archived, digitise Supplementary
  Table 1 (207 rows), rebuild the derived fields the table lacks (GSI-vs-Quantity sub-category;
  observational-vs-experimental flag), reconstruct sampling variances under a stated assumption about group
  sizes, rebuild a species tree, and re-fit the null model and models 1 and 2 to check recovery of the
  published estimates (−0.519; +2.732; −2.638; −0.384; −0.251; the *I*² decompositions; the three Egger
  intercepts).
- **Confirm the 183-vs-207 reconciliation in code as a named deliverable**, publishing the row-level
  classification and the exact rule that reproduces the analysed dataset (exclude the 24 absolute gonad/testis
  masses; retain body-mass-corrected indices), which recovers 183 / 65 / 31 / 34 exactly.
- **Audit the extreme effect sizes.** Re-extract from source the 8 rows with |*g*| > 8 (and, more broadly, a
  random ~10–20% validation sample of all rows) against the original articles, quantify extraction drift, and
  classify each discrepancy by cause.
- **Recover per-group means, SDs and per-morph *N*** for every retained study, so that the update rests on a
  dataset in which variances are computed rather than approximated, and so alternative effect-size metrics
  (lnRR, lnCVR for variance differences) become available.
- **Test the prediction Parker actually makes.** Fit sperm competition risk as an **ordered/continuous**
  moderator with a **quadratic term** to test the hump-shaped prediction directly, report the omnibus test of
  the moderator, and — where the primary literature now reports it — use the **proportion of minors in the
  population**, the quantity the model is written in and the proxy the dissertation wanted but could not use.
- **Fix the gonad-investment analysis rather than discarding data.** Retain absolute gonad/testis mass with
  **body mass as a covariate** (or use an allometrically appropriate index) instead of excluding 24 effect
  sizes, and treat the GSI-vs-absolute-mass distinction as a moderator plus a redundancy flag.
- **Interrogate the anomalous allocation result** with the enlarged evidence base, separating between-morph
  comparisons from within-male experimental manipulations of perceived risk, and separating internal from
  external fertilizers.
- **Add tactic-level moderators** the original could not: fixed/genetic vs. plastic/conditional tactics,
  sequential vs. simultaneous expression, sneaker vs. satellite vs. female-mimic minors, and whether the
  species is an internal or external fertilizer (the assumption violation the Discussion invokes but never
  tests).
- **Keep the primary synthesis fish-focused for comparability with the 2018 baseline**, but add an explicit
  **taxonomic-generality extension** testing whether the major/minor expenditure pattern holds in other taxa
  with alternative reproductive tactics (insects — including the *Onthophagus* literature — and other
  vertebrates), with taxon as a moderator.
- **Extend coverage** beyond 16 May 2017; broaden **information sources** (add Web of Science Core Collection
  and Scopus properly, plus grey literature and non-English records, and finish the **14 unscreened**
  records); use **two independent screeners** with reported agreement.
- **Apply updated analytical methods:** multilevel `rma.mv` with study / effect-size / species random effects
  plus a **properly sourced fish phylogeny**, a variance–covariance matrix for effect sizes sharing males or
  controls, cluster-robust inference, `orchaRd` heterogeneity decomposition and orchard/bubble plots.
- **Modernise bias and robustness diagnostics:** multilevel Egger's regression with a bias-corrected mean,
  funnel plots, time-lag bias, leave-one-out and leave-one-species-out re-fits, and outlier analyses — none of
  which the original reports.
- **Publish with open data and code**, remedying the original's central reproducibility gap.
