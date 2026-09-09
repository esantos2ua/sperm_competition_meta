#set document(
  title: "Benchmark Set for Literature Search Validation (Relative Recall)",
  author: ("Eduardo S. A. Santos", "Lygia A. Del Matto"),
)

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, left: 1.5cm, right: 1.5cm),
  header: align(right)[#text(size: 8.5pt, fill: rgb("#64748b"))[Benchmark Set -- Search String Validation (Relative Recall)]],
  footer: context [
    #align(center)[#text(size: 8.5pt, fill: rgb("#64748b"))[Page #counter(page).display("1")]]
  ]
)

#set text(
  font: "Libertinus Serif",
  size: 9.5pt,
  fill: rgb("#0f172a"),
  spacing: 120%,
  lang: "en",
)

#set par(justify: true, leading: 0.65em)

// Document Header
#align(center)[
  #text(size: 16pt, weight: "bold", fill: rgb("#1a4f8a"))[Benchmark Set for Literature Search Validation]
  #v(0.3em)
  #text(size: 11pt, weight: "medium", fill: rgb("#334155"))[Evaluating Search Sensitivity via Relative Recall in Sperm Competition Meta-Analysis]
  #v(0.5em)
  #text(size: 9pt, fill: rgb("#64748b"))[
    *Eduardo S. A. Santos* & *Lygia A. Del Matto* \
    *Date:* September 2026 | *Status:* Registered _A Priori_ | *Protocol Reference:* `protocol/02_update_protocol.typ`
  ]
]

#v(0.8em)
#line(length: 100%, stroke: 1pt + rgb("#1a4f8a"))
#v(0.5em)

== Purpose and Scope

This benchmark set is used to evaluate the *sensitivity* of our literature search strings via the benchmarking / relative-recall approach (Lagisz et al. 2025): a sensitive, comprehensive search string must retrieve a high proportion of known, topically relevant empirical studies. Following established best practices in systematic reviews and evidence synthesis, *this benchmark set was assembled and registered a priori before executing the final production database searches.*

Rather than testing an unwieldy collection, this benchmark set comprises an agile, stratified representative sample of *15 empirical teleost studies* drawn from the 50 baseline studies synthesized in Del Matto (2018). This sample represents 30% of the foundational evidence base and provides a focused audit standard.

== Stratification Principles

The 15 studies were selected to ensure balanced representation across all critical theoretical and taxonomic dimensions:

1. *100% Coverage of Sperm Allocation Studies:* All four empirical studies in the baseline synthesis that measure behavioral sperm allocation per mating act (_in vivo_ ejaculate expenditure) are retained:
   - _Poecilia reticulata_ (Pilastro & Bisazza 1999; internal fertilizer)
   - _Zosterisessor ophiocephalus_ / _Gobius niger_ (Pilastro et al. 2002; external fertilizer)
   - _Rhodeus amarus_ / _sericeus_ (Reichard et al. 2004; external bitterling)
   - _Thalassoma bifasciatum_ (Warner et al. 1995; external reef fish)
2. *Balanced Trait Representation:*
   - *Gonad investment / GSI / Production (10 studies):* Capturing relative testes investment and allometry contrasts.
   - *Sperm Quality & Kinetics (10 studies):* Curvilinear velocity ($V_(C L)$), percent motility, sperm longevity, ATP concentration, and sperm counts.
3. *Taxonomic Diversity (10 Distinct Teleost Families):* Centrarchidae, Gasterosteidae, Cichlidae, Batrachoididae, Salmonidae, Blenniidae, Poeciliidae, Gobiidae, Cyprinidae, and Labridae.
4. *Fertilization Modes:* External fertilization (13 studies) and internal fertilization (2 studies: _Poecilia reticulata_ and _Xiphophorus nigrensis_).

== Relative Recall Evaluation Protocol

For each bibliographic database (Web of Science Core Collection, Scopus, ASFA, OpenAlex, SciELO, BASE):
1. The formal search string is executed, recording query date and total records retrieved.
2. The retrieved records are cross-referenced against the benchmark set using DOI matching and normalized author-year-title matching.
3. *Relative Recall* is computed as:
   $ "Relative Recall (%)" = frac("Number of benchmark studies retrieved", "Total benchmark studies indexed in target database") times 100 $
4. *Acceptance threshold:*
   - $>= 90%$ overall relative recall across all databases.
   - *Strictly 100% recall* (15 / 15 studies) for Web of Science Core Collection and Scopus.
5. If any benchmark study is missed by a search string, the record's title, abstract, and indexed keywords are inspected to identify missing synonyms, and the query is re-piloted until the 100% threshold is met.

#pagebreak()
== Complete Benchmark Study Register (15 Stratified Studies)

#align(center)[
  #set text(size: 6.8pt)
  #set par(leading: 0.5em)
  #table(
    columns: (0.4fr, 2.5fr, 1.3fr, 0.9fr, 1.1fr, 1.4fr, 1.3fr),
    align: (center, left, left, left, left, left, left),
    stroke: 0.35pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1a4f8a") } else if calc.odd(row) { rgb("#f8fafc") } else { white },
    inset: (x: 3.5pt, y: 2.2pt),
    table.header(
      text(fill: white, weight: "bold")[No.],
      text(fill: white, weight: "bold")[Study & Citation],
      text(fill: white, weight: "bold")[Species & Family],
      text(fill: white, weight: "bold")[Fert. Mode],
      text(fill: white, weight: "bold")[Category],
      text(fill: white, weight: "bold")[Key Outcomes],
      text(fill: white, weight: "bold")[DOI],
    ),
    [1],
    [Burness, G., Moyes, C. D., & Montgomerie, R. (2005). Motility, ATP levels and metabolic enzyme activity of sperm from alternative male mating tactics in bluegill sunfish. _Journal of Fish Biology_, 67(4), 1087–1097.],
    [_Lepomis macrochirus_ \ (Centrarchidae)],
    [External],
    [Production, Quality],
    [Sperm quantity, motility, ATP],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1111/j.0022-1112.2005.00812.x")[10.1111/j.0022-1112.2005.00812.x]]],
    [2],
    [Côte, J., Blier, P. U., Caron, A., & Dufresne, F. (2009). Do territorial and sneaker male threespine sticklebacks have different sperm energetics and motility? _Canadian Journal of Zoology_, 87(11), 1061–1068.],
    [_Gasterosteus aculeatus_ \ (Gasterosteidae)],
    [External],
    [Production, Quality],
    [Testes mass, sperm quantity, sperm velocity],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1139/Z09-098")[10.1139/Z09-098]]],
    [3],
    [Fitzpatrick, J. L., Desjardins, J. K., Milligan, N., Montgomerie, R., & Balshine, S. (2007). Behavioral tactics and sperm competition in a cooperatively breeding cichlid. _Behavioral Ecology_, 18(1), 102–109.],
    [_Telmatochromis vittatus_ \ (Cichlidae)],
    [External],
    [Quality],
    [Sperm velocity, sperm longevity],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1093/beheco/arl055")[10.1093/beheco/arl055]]],
    [4],
    [Fitzpatrick, J. L., Earn, D. J., Bucking, C., Craig, P. M., Nadella, S., Wood, C. M., & Balshine, S. (2016). Ejaculate expenditure and sperm performance in alternative reproductive tactics of the plainfin midshipman. _Biological Journal of the Linnean Society_, 108(1), 99–108.],
    [_Porichthys notatus_ \ (Batrachoididae)],
    [External],
    [Production, Quality],
    [Testes mass, sperm count, sperm motility],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1111/bij.12781")[10.1111/bij.12781]]],
    [5],
    [Gage, M. J. G., Stockley, P., & Parker, G. A. (1995). Effects of alternative male mating strategies on characteristics of sperm production in the Atlantic salmon (_Salmo salar_). _Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences_, 350(1334), 391–399.],
    [_Salmo salar_ \ (Salmonidae)],
    [External],
    [Production, Quality],
    [GSI, sperm count, sperm length, motility],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1098/rstb.1995.0173")[10.1098/rstb.1995.0173]]],
    [6],
    [Neff, B. D., Fu, P., & Gross, M. R. (2003). Sperm investment and alternative mating tactics in bluegill sunfish (_Lepomis macrochirus_). _Behavioral Ecology_, 14(5), 634–641.],
    [_Lepomis macrochirus_ \ (Centrarchidae)],
    [External],
    [Production, Quality],
    [GSI, testes mass, sperm count, velocity],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1093/beheco/arg032")[10.1093/beheco/arg032]]],
    [7],
    [Oliveira, R. F., Canario, A. V. M., Grober, M. S., & Santos, R. S. (2001). Male alternative reproductive tactics and secondary sex characters in _Salaria pavo_. _Hormones and Behavior_, 40(3), 415–425.],
    [_Parablennius parvicornis_ \ (Blenniidae)],
    [External],
    [Production, Quality],
    [GSI, testicular gland proportion],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1006/hbeh.2001.1714")[10.1006/hbeh.2001.1714]]],
    [8],
    [Pilastro, A., & Bisazza, A. (1999). Insemination efficiency of sneak tactics in guppies. _Proceedings of the Royal Society of London. Series B: Biological Sciences_, 266(1431), 1887–1891.],
    [_Poecilia reticulata_ \ (Poeciliidae)],
    [Internal],
    [Allocation, Production],
    [Sperm number transferred, allocation],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1098/rspb.1999.0862")[10.1098/rspb.1999.0862]]],
    [9],
    [Pilastro, A., Scaggiante, M., & Rasotto, M. B. (2002). Individual adjustment of sperm expenditure in relation to presence of alternative males. _Proceedings of the National Academy of Sciences_, 99(20), 12927–12931.],
    [_Zosterisessor ophiocephalus_ \ (Gobiidae)],
    [External],
    [Allocation],
    [Sperm allocation per spawn, adjustment],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1073/pnas.152133499")[10.1073/pnas.152133499]]],
    [10],
    [Rasotto, M. B., & Mazzoldi, C. (2002). Male alternative reproductive tactics in the black goby: testicular traits, sperm traits and seminal vesicle function. _Marine Biology_, 141(4), 779–786.],
    [_Gobius niger_ \ (Gobiidae)],
    [External],
    [Production, Quality],
    [Testes mass, sperm count, mucin gland],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1007/s00227-002-0868-8")[10.1007/s00227-002-0868-8]]],
    [11],
    [Reichard, M., Smith, C., & Jordan, W. C. (2004). Genetic evidence reveals a high frequency of alternative mating tactics in the European bitterling (_Rhodeus sericeus_). _Molecular Ecology_, 13(8), 2211–2224.],
    [_Rhodeus amarus_ \ (Cyprinidae)],
    [External],
    [Allocation],
    [Sperm allocation, paternity share],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1111/j.1365-294X.2004.02157.x")[10.1111/j.1365-294X.2004.02157.x]]],
    [12],
    [Sato, T., Hirose, M., Taborsky, M., & Kimura, S. (2004). Size-dependent reproductive tactics in a shell-brooding cichlid, _Lamprologus callipterus_. _Ethology_, 110(1), 49–62.],
    [_Lamprologus callipterus_ \ (Cichlidae)],
    [External],
    [Production],
    [GSI, testes mass, dwarf adaptation],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1046/j.1439-0310.2003.00947.x")[10.1046/j.1439-0310.2003.00947.x]]],
    [13],
    [Smith, C. C., & Ryan, M. J. (2010). Evolution of sperm quality but not quantity in the alternative mating tactics of _Xiphophorus nigrensis_. _Journal of Evolutionary Biology_, 23(8), 1705–1714.],
    [_Xiphophorus nigrensis_ \ (Poeciliidae)],
    [Internal],
    [Production, Quality],
    [Sperm count, velocity, viability],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1111/j.1420-9101.2010.02043.x")[10.1111/j.1420-9101.2010.02043.x]]],
    [14],
    [Vladić, T., & Järvi, T. (2001). Sperm quality in the alternative reproductive tactics of Atlantic salmon: the importance of the loaded raffle mechanism. _Proceedings of the Royal Society of London. Series B: Biological Sciences_, 268(1483), 2375–2381.],
    [_Salmo salar_ \ (Salmonidae)],
    [External],
    [Production, Quality],
    [Sperm velocity, longevity, loaded raffle],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1098/rspb.2001.1768")[10.1098/rspb.2001.1768]]],
    [15],
    [Warner, R. R., Shapiro, D. Y., Marcanato, A., & Petersen, C. W. (1995). Sexual conflict: male corporate vs. individual interest in alternative mating tactics of the bluehead wrasse. _Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences_, 347(1321), 189–197.],
    [_Thalassoma bifasciatum_ \ (Labridae)],
    [External],
    [Allocation],
    [Sperm allocation, fertilization rates],
    [#text(size: 6.2pt)[#link("https://doi.org/10.1098/rspb.1995.0187")[10.1098/rspb.1995.0187]]],
  )
]

#v(0.4em)
== Summary of Benchmark Composition

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    - *Total benchmark records:* 15 studies (~30% sample).
    - *Sperm allocation coverage:* 4 / 4 studies (100%).
    - *Production / GSI coverage:* 10 studies.
  ],
  [
    - *Sperm quality / kinetics:* 10 studies.
    - *Taxonomic breadth:* 10 teleost families.
    - *Target relative recall:* 100% in WoS & Scopus.
  ]
)

#v(0.4em)
#line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
#v(0.2em)

#text(size: 7.5pt, fill: rgb("#64748b"))[
  *References:* \
  - Del Matto, L. A. (2018). _Sperm competition games between alternative reproductive tactics in teleost fishes: a meta-analysis_. MSc thesis, Universidade de São Paulo. \
  - Lagisz, M., et al. (2025). A practical guide to evaluating search string sensitivity in ecology and evolution. _Methods in Ecology and Evolution_.
]
