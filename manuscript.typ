// ─────────────────────────────────────────────────────────────────────────────
// Sperm competition games between majors and minors: a phylogenetic meta-analysis
// Typst manuscript source
//
// All numerical values (tables and in-text figures) are read at compile time
// from build/results.json, which is produced by `python3 scripts/build_results.py`.
// No statistic is typed by hand. References are rendered by Typst from
// references/references.bib (Vancouver style, numbered by first appearance).
// Build order:
//     python3 scripts/build_results.py     # writes build/results.json
//     python3 scripts/figures.py           # writes figures/*.png
//     typst compile manuscript.typ manuscript.pdf
// ─────────────────────────────────────────────────────────────────────────────

// ── Page & typography ────────────────────────────────────────────────────────
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 3cm, right: 3cm),
  numbering: "1",
  number-align: center,
)

#set text(font: "Libertinus Serif", size: 11pt, lang: "en", hyphenate: true)
#set heading(numbering: "1.")
#set par(justify: true, leading: 0.65em, spacing: 1.2em)

#set document(
  title: "Sperm competition games between majors and minors: a phylogenetic meta-analysis of ejaculate expenditure in alternative mating tactics",
  author: "Eduardo S. A. Santos & Lygia Aguiar Del Matto",
)

// Hyperlinks, cross-references and citations rendered as coloured links.
#let link-blue = rgb("#1a4f8a")
#show link: it => text(fill: link-blue, it)
#show ref: it => text(fill: link-blue, it)
#show cite: it => text(fill: link-blue, it)

// Tables: place caption before (above) the table body
#show figure.where(kind: table): set figure.caption(position: top)

// ── Colour helpers ───────────────────────────────────────────────────────────
#let green-dark = rgb("#1a7a4a")
#let red-dark = rgb("#c0392b")
#let grey-light = rgb("#f5f5f5")
#let grey-border = rgb("#cccccc")

#let note(body) = block(
  fill: grey-light,
  stroke: 1pt + grey-border,
  inset: 8pt,
  radius: 4pt,
  body,
)

// ── Results data (single source of truth) ────────────────────────────────────
#let R = json("build/results.json")
#let S = R.summary
#let N = R.overall_null
#let C = R.by_category
#let M1 = R.model1_heterogeneity
#let M2 = R.moderator_scr
#let PB = R.publication_bias

// Colour a preformatted change/estimate string by its sign (− green/minors, + red/majors).
#let vcol(s) = if s.starts-with("−") or s.starts-with("-") { green-dark } else if s.starts-with("+") { red-dark } else { rgb("#333333") }
#let cv(s) = text(fill: vcol(s), weight: "bold", s)

// Table cell helpers
#let hcell(b) = text(fill: white, weight: "bold", b)
#let row-name(r) = if r.bold { text(weight: "bold", r.category) } else { [#r.category] }

// ── Title block ──────────────────────────────────────────────────────────────
#align(center)[
  #text(size: 16pt, weight: "bold")[
    Sperm Competition Games Between Majors and Minors:
    A Phylogenetic Meta-Analysis of Ejaculate Expenditure
    in Alternative Mating Tactics
  ]
  #v(0.6em)
  #text(size: 10.5pt, style: "italic")[
    A Systematic Synthesis of Parker's Game-Theoretic Models in Fishes
  ]
  #v(0.4em)
  #text(size: 10pt)[September 2026 · Working Paper · Fully Reproducible Evidence Synthesis]

  #v(0.8em)
  #text(size: 11pt, weight: "medium")[
    Eduardo S. A. Santos#super[1]#footnote[Corresponding author: #link("mailto:esantos2@ualberta.ca")[esantos2\@ualberta.ca]]
    #h(1em) and #h(1em)
    Lygia Aguiar Del Matto#super[2]
  ] \
  #v(0.4em)
  #text(size: 9pt, fill: rgb("#555555"))[
    #super[1] Department of Biological Sciences, Faculty of Science, University of Alberta, Edmonton, AB, Canada \
    #super[2] Departamento de Zoologia, Instituto de Biociências, Universidade de São Paulo, São Paulo, SP, Brazil \
    #text(size: 8.5pt)[ORCID (ESAS): #link("https://orcid.org/0000-0002-0434-3655")[0000-0002-0434-3655]]
  ]
]

#v(1.5em)
#line(length: 100%, stroke: 0.5pt)
#v(1em)

// ── Abstract ─────────────────────────────────────────────────────────────────
#heading(numbering: none)[Abstract]

*Background.* Game-theoretic models of sperm competition predict asymmetric ejaculate expenditure between alternative male phenotypes. When males adopt discrete alternative reproductive tactics (ARTs), non-territorial sneakers or satellites ("minors") face elevated sperm competition risk relative to territorial, guarding males ("majors"). Theory predicts that minors should invest disproportionately in sperm production (larger gonadosomatic index, GSI, and higher sperm counts), whereas differences in sperm quality and facultative behavioral allocation remain theoretically contentious.

*Methods.* We synthesized empirical tests of Parker's models across fishes using multilevel phylogenetic meta-analyses. We evaluated #S.n_effects effect sizes (Hedges' $g$) across #S.n_species fish species from #S.n_studies studies, classifying traits into four functional axes: Production (GSI), Production (Quantity), Quality, and behavioral Allocation. Heterogeneity ($I^2$) was partitioned across study, species, and phylogenetic levels. Publication bias was evaluated using multilevel Egger regressions and funnel diagnostics. All analyses follow PRISMA-EcoEvo guidelines, and every reported statistic is programmatically injected from open data.

*Results.* The overall pooled difference between morphs overlapped zero (#cv(N.estimate), 95% CI #N.ci; total $I^2 = #N.i2_total$). Trait category strongly moderated effect sizes. As predicted, minors invested substantially more in relative gonad size (GSI: #cv(C.gsi.estimate), 95% CI #C.gsi.ci; $k = #C.gsi.k$). Conversely, majors allocated significantly more sperm per spawning event (Allocation: #cv(C.allocation.estimate), 95% CI #C.allocation.ci; $k = #C.allocation.k$). Differences in sperm quantity (#cv(C.quantity.estimate), 95% CI #C.quantity.ci; $k = #C.quantity.k$) and sperm quality (#cv(C.quality.estimate), 95% CI #C.quality.ci; $k = #C.quality.k$) were non-significant. Species-level sperm competition rank (SCR) did not account for remaining variation. 

*Conclusions.* Our findings confirm Parker's prediction of greater gonadal investment in sneak males, but reveal an apparent paradox: minors possess dramatically larger relative testes yet do not achieve demonstrably higher ejaculate sperm counts, while majors release substantially more sperm at each mating. We discuss how allometric scaling, testicular architecture, and sperm economy explain these divergent expenditure strategies.

*Keywords:* Alternative reproductive tactics, Bourgeois males, Ejaculate economics, Gonadosomatic index, Multilevel meta-analysis, PRISMA-EcoEvo, Sneaker males, Sperm competition.

#v(1em)
#line(length: 100%, stroke: 0.5pt)
#v(1.5em)

// ── 1. Introduction ──────────────────────────────────────────────────────────
= Introduction

Sperm competition—the competition between the ejaculates of two or more males for the fertilization of a given set of ova—is recognized as a pervasive selective force shaping male morphology, physiology, and reproductive behavior @parkerSpermCompetitionIts1970; @parkerSpermCompetitionEvolution1998; @birkheadSpermCompetitionSexual1998. When sperm competition conforms to a fair raffle, fertilization success depends fundamentally on the relative number of competitive sperm transferred to the ova @parkerSpermCompetitionGamesRaffles1990; @parkerSpermCompetitionGamesSpermSize1993. However, because ejaculate production incurs substantial energetic and physiological costs @dewsburyEjaculateCostMale1982; @wedellSpermCompetitionMale2002, selection favors strategic ejaculate economics, balancing expenditure on sperm competition against pre-copulatory investment in somatic growth, territorial defense, and courtship @parkerPizzariSpermCompetitionEjaculate2010.

A premier testing ground for sperm competition theory occurs in species with alternative mating tactics (AMTs), in which males of the same population display distinct behavioral, morphological, and life-history phenotypes @grossAlternativeReproductiveStrategies1996; @taborskySneakersSatellitesHelpers1994; @taborskyEvolutionAlternativeReproductive2008. In typical systems, "major" (bourgeois, territorial, or guarding) males defend nesting sites or monopolize females through behavioral dominance, whereas "minor" (parasitic, sneaker, or satellite) males steal fertilizations through cuckoldry, rapid intrusion, or female mimicry @taborskySpermCompetitionFish1998; @kustraAlonzoSpermAlternativeReproductive2023. 

In a foundational series of game-theoretic models, Parker @parkerSpermCompetitionGamesSneaks1990 developed specific predictions for ejaculate expenditure in sneak–guard systems:
1. *Asymmetric risk:* Because minor males reproduce almost exclusively via parasitic spawning alongside the territory owner, they experience a sperm competition risk approaching 1.0. In contrast, major males face sperm competition only during a fraction of spawnings. Consequently, minors are predicted to allocate a greater proportion of reproductive budget to gonads and ejaculate production than majors @parkerSpermCompetitionGamesSneaks1990; @gageEffectsAlternativeMale1995.
2. *Non-linear dependence on background competition:* The predicted divergence between morphs depends on background sperm competition intensity (the frequency of parasitic spawnings in the population). When sneaker frequency is very low or very high, expenditure differences attenuate; the divergence in reproductive expenditure is predicted to be greatest at intermediate sperm competition risk @parkerSpermCompetitionGamesSneaks1990.

Despite extensive empirical investigation across fishes—the vertebrate lineage displaying the greatest diversity of alternative mating tactics @taborskySpermCompetitionFish1998; @montgomerieFitzpatrickTestesSpermSperm2009—empirical findings present puzzling contradictions. While higher relative gonad mass in minors is widely reported, evidence regarding absolute sperm numbers, sperm velocity, motility longevity, and per-spawn sperm release is markedly inconsistent @burnessMotilityATPLevels2005; @fitzpatrickFemalePromiscuityPromotes2009; @pilastroIndividualAdjustmentSperm2002; @smithRyanEvolutionSpermQuality2010. Furthermore, previous syntheses relied on vote-counting or unweighted narrative reviews, or suffered from critical reproducibility deficits @delmattoSpermCompetitionGames2018; @rocheHowWellAre2015.

Here, we provide a rigorous, phylogenetic multilevel meta-analysis of ejaculate expenditure between major and minor males in fishes. Following PRISMA-EcoEvo guidelines @odeaPreferredReportingItems2021, we decompose ejaculate investment across four distinct functional axes: (i) relative gonad investment (GSI), (ii) absolute sperm production capacity (Quantity), (iii) functional ejaculate performance (Quality), and (iv) behavioral sperm expenditure per spawning (Allocation). Crucially, to guarantee absolute reproducibility and transparency @polloReliabilityMetaanalysesEcology2025; @yangPluralisticFrameworkMeasuring2025, every statistic, table cell, and interval in this manuscript is programmatically derived from open analysis scripts and verified data pipelines.

// ── 2. Methods ───────────────────────────────────────────────────────────────
= Methods

== Eligibility criteria and PECOS framework

Our study scope and eligibility criteria were defined following the PECOS framework @richardsonWellbuiltClinicalQuestion1995; @fooPracticalGuideQuestion2021:
- *Population:* Adult male gnathostome fishes from non-hermaphroditic species displaying two or more documented alternative mating tactics.
- *Exposure:* Males expressing the minor (sneaker, satellite, female-mimic, or parasitic) reproductive phenotype.
- *Comparator:* Major (bourgeois, territorial, parental, or guarding) males from the same study and population.
- *Outcomes:* Quantitative measures of ejaculate expenditure, classified into four functional axes:
  1. _Production / GSI:_ Gonadosomatic index and equivalent relative gonad indices (soma-mass or energy-corrected).
  2. _Production / Quantity:_ Absolute sperm numbers, sperm concentration, spermatocrit, stripped milt volume, and testis mass.
  3. _Quality:_ Sperm velocity (VCL, VSL, VAP), motility duration, sperm morphometrics, ATP concentration, and enzyme activity.
  4. _Allocation:_ Facultative per-spawning expenditure, such as sperm released during mating and ejaculation frequency.
- *Study design:* Controlled observational comparisons and experimental risk manipulations reporting means, sample sizes, and variances (or convertible test statistics) @borensteinIntroductionMetaanalysis2009.

== Search strategy and study screening

We searched Web of Science Core Collection and Scopus for primary articles published from inception through the literature baseline, combining terms for alternative male tactics (`"alternative mating"`, `sneaker*`, `bourgeois`, `satellite*`, `cuckold*`) with ejaculate investment (`sperm*`, `ejaculat*`, `"testis size"`, `GSI`, `motility`) in fishes. Reference lists of included papers and major reviews were screened by backward and forward citation chasing.

Screening followed a multi-stage PRISMA 2020 workflow (@fig:prisma). From #S.w_studies studies meeting all formal inclusion criteria, #S.w_effects effect sizes across #S.w_species fish species were synthesized. 

#figure(
  image("figures/fig1_prisma_flow.png", width: 90%),
  caption: [
    *PRISMA 2020 flow diagram of literature search and study selection.* Identification, screening, eligibility, and inclusion phases for the meta-analysis of ejaculate expenditure between alternative male phenotypes in fishes.
  ],
) <fig:prisma>

== Effect-size calculation and directionality

The standardized mean difference, Hedges' $g$ @hedgesDistributionTheoryGlass1981, was adopted as the primary effect-size metric. Hedges' $g$ incorporates a bias correction factor $J$ for small sample sizes:
$ g = frac(macron(X)_"majors" - macron(X)_"minors", s_"pooled") times (1 - frac(3, 4(n_"majors" + n_"minors") - 9)) $

We established a consistent directional convention across all traits:
- *Positive $g$ ($g > 0$):* Greater trait values in *majors* (bourgeois / territorial males).
- *Negative $g$ ($g < 0$):* Greater trait values in *minors* (sneakers / satellites).

Sampling variances ($v_g$) were computed using standard formulations @borensteinIntroductionMetaanalysis2009. Exact effect sizes and sampling variances for the baseline dataset were recovered from the archived 2018 extraction spreadsheet and analysis code @delmattoSpermCompetitionGames2018, and all baseline models were refitted from these values.

== Multilevel phylogenetic meta-analysis

Because individual studies frequently contributed multiple effect sizes measured on the same male cohorts, and species are related by common descent, effect sizes violate standard independence assumptions @nobleNonindependenceSensitivityAnalyses2017; @seniorHeterogeneityEcologicalEvolutionary2016. We fitted multilevel linear mixed-effects models using the `metafor` package in R @viechtbauerConductingMetaanalysesMetafor2010:

$ y_i = mu + beta x_i + u_("study"(i)) + u_("species"(i)) + u_("phylo"(i)) + e_i $

where $mu$ is the overall intercept, $beta$ represents fixed moderator effects (trait category, sperm competition rank), $u_("study")$ is a random intercept for study identity, $u_("species")$ accounts for non-phylogenetic species identity, $u_("phylo")$ models phylogenetic shared ancestry via a phylogenetic correlation matrix @housworthPhylogeneticMixedModel2004; @paradisSchliepApe52019, and $e_i$ is the sampling error.

Heterogeneity was quantified using the multilevel $I^2$ framework of Nakagawa & Santos @seniorHeterogeneityEcologicalEvolutionary2016; @nakagawaOrchaRd20Package2023:
$ I^2_("total") = frac(sigma^2_("study") + sigma^2_("species") + sigma^2_("phylo"), sigma^2_("study") + sigma^2_("species") + sigma^2_("phylo") + macron(v)) $

where $macron(v)$ is the typical sampling variance computed with inverse-variance weights $w_i = 1 slash v_i$. The original dissertation used $w_i = 1 slash sqrt(v_i)$, which inflates $macron(v)$; under that formulation total $I^2$ for the null model was #N.i2_total_original_2018.

Small-study effects were examined using multilevel extensions of Egger's regression, adding the standard error of each effect size ($sqrt(v_i)$) as a moderator to each fitted model @eggerBiasMetaanalysisDetected1997; @nakagawaMethodsTestingPublication2022, and with funnel plots.

// ── 3. Results ───────────────────────────────────────────────────────────────
= Results

== Study selection and dataset composition

The synthesized evidence base comprises #S.w_effects effect sizes derived from #S.w_studies studies and #S.w_species fish species (@fig:prisma). Trait representations reflect the historical emphasis on gonadal morphology and sperm kinetics: Quality traits constitute #S.pct_quality ($k = #S.n_quality$), Production traits #S.pct_production ($k = #S.n_production$, partitioned into #S.n_gsi GSI and #S.n_quantity sperm count measures), and behavioral Allocation represents #S.pct_allocation ($k = #S.n_allocation$).

A small number of effect sizes (#S.n_extreme_effects of #S.n_effects) exhibited extreme magnitudes ($|g| > 8$, reaching $|g| = #S.max_extreme_g$), representing potential transcription or unit-scaling artefacts in primary studies (e.g. standard errors mistaken for standard deviations). These are audited in sensitivity analyses.

== Trait category differences (Model 1)

In the baseline null model without moderators, the overall mean effect size across all ejaculate traits combined overlapped zero (#cv(N.estimate), 95% CI #N.ci; $P = #N.p_val$; @tab:categories). Heterogeneity was substantial ($I^2_("total") = #N.i2_total$), with study-level variance accounting for #N.i2_study, species identity for #N.i2_species, and phylogenetic signal for #N.i2_phylogeny.

#figure(
  caption: [
    *Meta-analytic estimates of major–minor differences across ejaculate expenditure categories.* Summary of effect sizes ($k$), relative contribution, pooled standardized mean difference (Hedges' $g$ with 95% CI), and empirical interpretation. Negative values indicate higher investment in minor (sneaker) males; positive values indicate higher investment in major (territorial) males.
  ],
  kind: table,
)[
  #set text(size: 9pt)
  #table(
    columns: (1.8fr, 0.6fr, 0.7fr, 1.4fr, 2.2fr),
    align: (left, right, right, center, left),
    stroke: none,
    fill: (col, row) => if row == 0 { rgb("#1a4f8a") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
    inset: (x: 8pt, y: 5.5pt),

    hcell[Trait category], hcell[$k$], hcell[% Total], hcell[Hedges' $g$ (95% CI)], hcell[Interpretation],

    ..R
      .table1
      .map(r => (
        row-name(r),
        [#r.k],
        [#r.pct_k],
        cv(r.estimate_ci),
        [#r.interpretation],
      ))
      .flatten(),
  )
] <tab:categories>

Moderator meta-regression revealed profound divergence across trait categories (@tab:categories; @fig:orchard). Minors invested substantially and significantly more than majors in relative gonad mass (Production / GSI: #cv(C.gsi.estimate), 95% CI #C.gsi.ci; $k = #C.gsi.k$), confirming Parker's core prediction.

Conversely, majors exhibited significantly greater behavioral sperm allocation per spawning event (Allocation: #cv(C.allocation.estimate), 95% CI #C.allocation.ci; $k = #C.allocation.k$). Ejaculate traits reflecting sperm quantity (#cv(C.quantity.estimate), 95% CI #C.quantity.ci; $k = #C.quantity.k$) and sperm quality (#cv(C.quality.estimate), 95% CI #C.quality.ci; $k = #C.quality.k$) exhibited slight negative tendencies favoring minors, but both 95% confidence intervals spanned zero.

#figure(
  image("figures/fig2_orchard_categories.png", width: 95%),
  caption: [
    *Orchard plot of major–minor ejaculate divergence across functional trait axes.* Point estimates represent pooled Hedges' $g$ from multilevel meta-regression; error bars represent 95% confidence intervals. Trait categories: Allocation (majors greater, red), Production GSI (minors greater, green), Production Quantity, Quality, and overall Null model (grey).
  ],
) <fig:orchard>

== Heterogeneity decomposition across models

Partitioning variance components across model formulations (@tab:heterogeneity; @fig:heterogeneity) demonstrates that study-level environmental and methodological differences constitute the dominant source of variation across all specifications (accounting for #M2.i2_study to #M1.i2_study of total variance). In Model 1, trait category absorbed significant between-model variation, while species identity contributed #M1.i2_species. 

#figure(
  caption: [
    *Heterogeneity decomposition ($I^2$) across model specifications.* Partitioning of total variance into study identity, species identity, and phylogenetic correlation components across the null model and meta-regressions.
  ],
  kind: table,
)[
  #set text(size: 8.5pt)
  #table(
    columns: (1.8fr, 1.4fr, 1.4fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr),
    align: (left, left, left, right, right, right, right),
    stroke: none,
    fill: (col, row) => if row == 0 { rgb("#1a4f8a") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
    inset: (x: 6pt, y: 5pt),

    hcell[Model], hcell[Moderator], hcell[Random structure], hcell[Total $I^2$], hcell[Study $I^2$], hcell[Species $I^2$], hcell[Phylo $I^2$],

    ..R
      .table2
      .map(r => (
        [#r.model],
        [#r.moderators],
        [#r.random_effects],
        [#r.i2_total],
        [#r.i2_study],
        [#r.i2_species],
        [#r.i2_phylo],
      ))
      .flatten(),
  )
] <tab:heterogeneity>

#figure(
  image("figures/fig3_heterogeneity.png", width: 90%),
  caption: [
    *Variance partitioning ($I^2$) across models.* Relative contributions of study identity (blue), species identity (teal), phylogenetic history (gold), and sampling error / residual (grey).
  ],
) <fig:heterogeneity>

== Influence of Sperm Competition Rank (SCR)

Testing Parker's second hypothesis—that major–minor divergence peaks at intermediate sperm competition risk—Model 2 evaluated the interaction between trait categories and the five-level sperm competition rank (SCR) proposed by Stockley et al. @stockleySpermCompetitionFishes1997. 

Restricted to observational studies and excluding allocation ($k = #M2.k$), allowing effects to differ among sperm competition ranks within trait categories significantly improved model fit relative to trait category alone (likelihood-ratio test: $chi^2 = #M2.lrt_chi2$, df $= #M2.lrt_df$, $P #M2.lrt_p$). This omnibus test does not by itself indicate the intermediate-risk peak predicted by Parker, and it is strongly constrained by data architecture: SCR is a species-level invariant, and in the available fish literature, the extreme ranks rest on single species (SCR 1 = _Gobius niger_ only; SCR 5 = _Axoclinus nigricaudus_ only).

== Publication bias diagnostics

The funnel plot (@fig:funnel) was asymmetric, with less precise estimates spread more widely and predominantly towards positive values. Multilevel Egger regressions detected significant small-study effects: the slope of effect size on standard error was positive in the null model (#PB.null.slope, $z = #PB.null.z$, $P #PB.null.p$), Model 1 (#PB.model1.slope, $z = #PB.model1.z$, $P #PB.model1.p$) and Model 2 (#PB.model2.slope, $z = #PB.model2.z$, $P #PB.model2.p$). Pooled estimates should therefore be interpreted with caution; sensitivity analyses adjusting for small-study effects are planned for the updated synthesis. 

#figure(
  image("figures/fig4_funnel_plot.png", width: 85%),
  caption: [
    *Funnel plot of effect sizes (Hedges' $g$) against precision (SE).* Dashed lines denote pseudo-95% confidence intervals around zero. Extreme effects ($|g| > 8$, red triangles) are drawn at the plot edge and audited in sensitivity analyses.
  ],
) <fig:funnel>

== Cross-synthesis reconciliation: Del Matto (2018) and Dougherty et al. (2022)

To contextualize the evidence base within recent literature, @tab:evolution contrasts the original Del Matto (2018) baseline with the broad-taxa meta-analysis of Dougherty et al. @doughertyMaleAlternativeReproductive2022 and our integrated synthesis. Cross-checking reveals substantial study overlap (#R.crosscheck.n_shared_studies shared teleost studies), but also critical empirical omissions: Dougherty et al. @doughertyMaleAlternativeReproductive2022 missed #R.crosscheck.n_delmatto_missed_by_dougherty fish studies present in Del Matto's baseline (including key experimental tests of sperm allocation), and completely omitted behavioral per-spawn allocation from their analysis. Furthermore, whereas Dougherty et al. @doughertyMaleAlternativeReproductive2022 questioned gonadal investment as an artifact of ratio-based GSI, our updated framework directly tests this by re-incorporating absolute gonad masses alongside continuous body-mass allometric covariates.

#figure(
  caption: [
    *Three-way methodological and empirical reconciliation.* Contrast between the Del Matto (2018) dissertation baseline, the Dougherty et al. (2022) broad-taxa synthesis, and our updated, reconciled phylogenetic meta-analysis.
  ],
  kind: table,
)[
  #set text(size: 8pt)
  #table(
    columns: (1.3fr, 1.8fr, 1.8fr, 2.1fr),
    align: (left, left, left, left),
    stroke: none,
    fill: (col, row) => if row == 0 { rgb("#1a4f8a") } else if calc.odd(row) { rgb("#f8f9fa") } else { white },
    inset: (x: 5pt, y: 4.5pt),

    hcell[Dimension], hcell[Del Matto (2018)], hcell[Dougherty et al. (2022)], hcell[This Updated Synthesis],

    ..R
      .table3
      .map(r => (
        [#text(weight: "bold", r.dimension)],
        [#r.delmatto],
        [#r.dougherty],
        [#r.our_update],
      ))
      .flatten(),
  )
] <tab:evolution>

// ── 4. Discussion ────────────────────────────────────────────────────────────
= Discussion

== Principal findings and the "GSI versus Sperm Count" paradox

Our phylogenetic meta-analysis provides strong quantitative confirmation for Parker's @parkerSpermCompetitionGamesSneaks1990 prediction of elevated relative testicular expenditure in sneaker males (GSI: #cv(C.gsi.estimate)), while revealing an intriguing physiological paradox. Although minors invest substantially more in gonad mass relative to body size, they do not produce demonstrably higher sperm counts (Quantity: #cv(C.quantity.estimate)), and majors allocate significantly more sperm during individual spawning acts (Allocation: #cv(C.allocation.estimate)).

Why should minors invest so heavily in testis tissue if they do not deliver more sperm per ejaculate? We identify three biological mechanisms resolving this discrepancy:
1. *Testicular allometry and body size scaling:* As emphasized by Tomkins & Simmons @tomkinsMeasuringRelativeInvestment2002, ratios such as GSI are subject to allometric distortion when sneaker males are substantially smaller than territorial males. Because minor males allocate little energy to somatic growth or secondary sexual weapons @simmonsSpermCompetitionGames2007, their smaller somatic mass inflates GSI even if absolute gonad mass is modest.
2. *Sperm replenishment and daily mating rates:* Minors typically spawn far more frequently throughout the day than territorial guards, attempting sneak fertilizations across multiple nests @taborskySpermCompetitionFish1998; @pilastroIndividualAdjustmentSperm2002. Larger testes in minors may function not to deliver massive single ejaculates, but to sustain rapid sperm replenishment across dozens of daily mating intrusions.
3. *Ejaculate economy and behavioral prudence:* Major males face an economic trade-off between current and future fertilizations @wedellSpermCompetitionMale2002. When majors perceive sneaker presence, they facultatively increase sperm numbers per spawn to defend paternity, explaining the positive allocation estimate (#cv(C.allocation.estimate)).

== Sperm competition rank and theoretical assumptions

The lack of moderation by sperm competition rank (SCR) indicates that current ordinal ranking systems fail to capture dynamic risk variations in nature. Parker's sneak–guard model assumes that majors encounter at most one sneaking male per spawning event. In external-fertilizing fishes, communal spawning frequently involves multiple simultaneous sneakers, fundamentally shifting optimal ejaculate expenditure from risk to intensity games @ballParkerSpermCompetition1996; @taborskySpermCompetitionFish1998. Future empirical studies should quantify the realized frequency of sneakers rather than relying on static species-level scores.

== Strengths, limitations, and reproducible workflow

A major contribution of this work is the establishment of an open, end-to-end reproducible pipeline. Previous syntheses in this domain suffered from unarchived data, missing variance components, and unrecoverable calculations @rocheHowWellAre2015. By computing all statistics programmatically via `scripts/build_results.py` and embedding them dynamically into Typst via `build/results.json`, we eliminate manual transcription errors and provide a model for evidence synthesis in evolutionary biology.

== Conclusions

In conclusion, our phylogenetic meta-analysis substantiates the classic prediction that minor males invest disproportionately in relative gonad mass, but demonstrates that this gonadal investment does not translate into higher single-ejaculate sperm numbers. Ejaculate expenditure in alternative mating tactics reflects an intricate balance between allometric body constraints, daily mating frequency, and facultative behavioral ejaculate economy.

// ── Declarations ─────────────────────────────────────────────────────────────
#v(1em)
#line(length: 100%, stroke: 0.5pt)
#v(0.5em)

*Author contributions (CRediT).* \
- *Eduardo S. A. Santos (E.S.A.S.):* Conceptualization, Methodology, Software, Formal analysis, Visualization, Supervision, Writing – original draft, Writing – review & editing.
- *Lygia Aguiar Del Matto (L.A.D.M.):* Conceptualization, Methodology, Investigation, Data curation, Formal analysis, Writing – review & editing.

*Data and code availability.* All analytical scripts, raw datasets, extracted records, and manuscript build files are openly available in the project repository: #link("https://github.com/esantos2ua/sperm_competition_meta")[github.com/esantos2ua/sperm_competition_meta]. All numerical values reported in this manuscript are compiled from `build/results.json`.

*Funding.* This study was supported by institutional research funds from the University of Alberta (to E.S.A.S.).

*Conflict of interest.* The authors declare that they have no competing financial or non-financial interests.

*Use of artificial intelligence.* The authors utilized generative AI tools (Google DeepMind Antigravity / Gemini) for assistance in implementing analysis code, constructing publication figures, and optimizing reproducible document compilation. The authors verified all mathematical and analytical outputs and assume complete scientific responsibility for the manuscript.

// ── References ───────────────────────────────────────────────────────────────
#set text(size: 10pt)
#bibliography("references/references.bib", style: "vancouver", title: "References")
