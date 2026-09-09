# Benchmark Set for Literature Search Validation (Relative Recall)

**Protocol Document:** `protocol/03_benchmark_set.md`  
**Authors:** Eduardo S. A. Santos, Lygia A. Del Matto  
**Status:** Registered *A Priori*  
**Date:** September 2026  
**Related Protocol:** `protocol/02_update_protocol.md` (and compiled `protocol/02_update_protocol.pdf`)  
**Target Sample:** Stratified representative sample of **15 studies** (~30%) drawn from the 50 baseline empirical fish studies in Del Matto (2018).

---

## Purpose and Scope

This benchmark set is used to evaluate the **sensitivity** of our literature search strings via the
benchmarking / relative-recall approach [@lagiszPracticalGuideEvaluating2025]: a sensitive, comprehensive
search string must retrieve a high proportion of known, topically relevant empirical studies. Following
established best practices in systematic reviews and evidence synthesis, **this benchmark set was
assembled and registered *before* executing the final production database searches.**

Rather than testing an excessively broad collection, this set comprises a focused, stratified sample
of **15 representative empirical teleost studies** drawn from the 50 baseline studies synthesized in Del Matto (2018).
This sample represents 30% of the foundational evidence base and provides an agile, robust audit standard.

## Stratification Principles

The 15 studies were selected to ensure balanced coverage across all critical dimensions of sperm competition theory:

1. **100% Coverage of Sperm Allocation Studies:**
   All four empirical studies in the baseline synthesis that measure behavioral sperm allocation per mating act
   (*in vivo* ejaculate expenditure) are retained:
   - *Poecilia reticulata* (Pilastro & Bisazza 1999; internal fertilizer)
   - *Zosterisessor ophiocephalus* / *Gobius niger* (Pilastro et al. 2002; external fertilizer)
   - *Rhodeus amarus* / *sericeus* (Reichard et al. 2004; external bitterling)
   - *Thalassoma bifasciatum* (Warner et al. 1995; external reef fish)
2. **Balanced Trait Representation:**
   - **Gonad investment / GSI / Production (10 studies):** Capturing relative testes investment and allometry contrasts.
   - **Sperm Quality & Kinetics (10 studies):** Curvilinear velocity ($V_{CL}$), percent motility, sperm longevity, ATP concentration, and sperm counts.
3. **Taxonomic Diversity (10 Distinct Teleost Families):**
   - Centrarchidae (sunfishes)
   - Gasterosteidae (sticklebacks)
   - Cichlidae (shell-brooders and cooperative breeders)
   - Batrachoididae (toadfishes / midshipman)
   - Salmonidae (salmon and trout)
   - Blenniidae (combtooth blennies)
   - Poeciliidae (livebearers)
   - Gobiidae (gobies)
   - Cyprinidae (carps and bitterlings)
   - Labridae (wrasses)
4. **Fertilization Modes:**
   - External fertilization (13 studies)
   - Internal fertilization (2 studies: *Poecilia reticulata* and *Xiphophorus nigrensis*)

---

## Relative Recall Evaluation Protocol

For each bibliographic database (Web of Science Core Collection, Scopus, ASFA, OpenAlex, SciELO, BASE):
1. The formal search string is executed, recording query date and total records retrieved.
2. The retrieved records are cross-referenced against the benchmark set using DOI matching and normalized author-year-title matching.
3. **Relative Recall** is computed as:
   $$\text{Relative Recall (\%)} = \frac{\text{Number of benchmark studies retrieved}}{\text{Total benchmark studies indexed in target database}} \times 100$$
4. **Acceptance threshold:**
   - $\ge 90\%$ overall relative recall across all databases.
   - **Strictly 100% recall** (15 / 15 studies) for Web of Science Core Collection and Scopus.
5. If any benchmark study is missed by a search string:
   - The record's title, abstract, and indexed keywords are inspected.
   - Missing terminology, alternative synonyms, or truncated wildcards are identified.
   - The Boolean search string is refined and re-piloted until the 100% threshold is met.

---

## Complete Benchmark Study Register (15 Stratified Studies)

| # | Study & Citation | Year | Species | Family | Fert. Mode | Category | Key Outcomes | DOI |
|---|------------------|------|---------|--------|------------|----------|--------------|-----|
| 1 | Burness, G., Moyes, C. D., & Montgomerie, R. (2005). Motility, ATP levels and metabolic enzyme activity of sperm from alternative male mating tactics in bluegill sunfish. *Journal of Fish Biology*, 67(4), 1087–1097. | 2005 | *Lepomis macrochirus* | Centrarchidae | External | Production, Quality | Sperm quantity, motility, ATP | [10.1111/j.0022-1112.2005.00812.x](https://doi.org/10.1111/j.0022-1112.2005.00812.x) |
| 2 | Côte, J., Blier, P. U., Caron, A., & Dufresne, F. (2009). Do territorial and sneaker male threespine sticklebacks have different sperm energetics and motility? *Canadian Journal of Zoology*, 87(11), 1061–1068. | 2009 | *Gasterosteus aculeatus* | Gasterosteidae | External | Production, Quality | Testes mass, sperm quantity, sperm velocity | [10.1139/Z09-098](https://doi.org/10.1139/Z09-098) |
| 3 | Fitzpatrick, J. L., Desjardins, J. K., Milligan, N., Montgomerie, R., & Balshine, S. (2007). Behavioral tactics and sperm competition in a cooperatively breeding cichlid. *Behavioral Ecology*, 18(1), 102–109. | 2007 | *Telmatochromis vittatus* | Cichlidae | External | Quality | Sperm velocity, sperm longevity | [10.1093/beheco/arl055](https://doi.org/10.1093/beheco/arl055) |
| 4 | Fitzpatrick, J. L., Earn, D. J., Bucking, C., Craig, P. M., Nadella, S., Wood, C. M., & Balshine, S. (2016). Ejaculate expenditure and sperm performance in alternative reproductive tactics of the plainfin midshipman. *Biological Journal of the Linnean Society*, 108(1), 99–108. | 2016 | *Porichthys notatus* | Batrachoididae | External | Production, Quality | Testes mass, sperm count, sperm motility | [10.1111/bij.12781](https://doi.org/10.1111/bij.12781) |
| 5 | Gage, M. J. G., Stockley, P., & Parker, G. A. (1995). Effects of alternative male mating strategies on characteristics of sperm production in the Atlantic salmon (*Salmo salar*). *Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences*, 350(1334), 391–399. | 1995 | *Salmo salar* | Salmonidae | External | Production, Quality | GSI, sperm count, sperm length, motility | [10.1098/rstb.1995.0173](https://doi.org/10.1098/rstb.1995.0173) |
| 6 | Neff, B. D., Fu, P., & Gross, M. R. (2003). Sperm investment and alternative mating tactics in bluegill sunfish (*Lepomis macrochirus*). *Behavioral Ecology*, 14(5), 634–641. | 2003 | *Lepomis macrochirus* | Centrarchidae | External | Production, Quality | GSI, testes mass, sperm count, velocity | [10.1093/beheco/arg032](https://doi.org/10.1093/beheco/arg032) |
| 7 | Oliveira, R. F., Canario, A. V. M., Grober, M. S., & Santos, R. S. (2001). Male alternative reproductive tactics and secondary sex characters in *Salaria pavo*. *Hormones and Behavior*, 40(3), 415–425. | 2001 | *Parablennius parvicornis* | Blenniidae | External | Production, Quality | GSI, testicular gland proportion | [10.1006/hbeh.2001.1714](https://doi.org/10.1006/hbeh.2001.1714) |
| 8 | Pilastro, A., & Bisazza, A. (1999). Insemination efficiency of sneak tactics in guppies. *Proceedings of the Royal Society of London. Series B: Biological Sciences*, 266(1431), 1887–1891. | 1999 | *Poecilia reticulata* | Poeciliidae | Internal | Allocation, Production | Sperm number transferred, allocation | [10.1098/rspb.1999.0862](https://doi.org/10.1098/rspb.1999.0862) |
| 9 | Pilastro, A., Scaggiante, M., & Rasotto, M. B. (2002). Individual adjustment of sperm expenditure in relation to presence of alternative males. *Proceedings of the National Academy of Sciences*, 99(20), 12927–12931. | 2002 | *Zosterisessor ophiocephalus* | Gobiidae | External | Allocation | Sperm allocation per spawn, adjustment | [10.1073/pnas.152133499](https://doi.org/10.1073/pnas.152133499) |
| 10 | Rasotto, M. B., & Mazzoldi, C. (2002). Male alternative reproductive tactics in the black goby: testicular traits, sperm traits and seminal vesicle function. *Marine Biology*, 141(4), 779–786. | 2002 | *Gobius niger* | Gobiidae | External | Production, Quality | Testes mass, sperm count, mucin gland | [10.1007/s00227-002-0868-8](https://doi.org/10.1007/s00227-002-0868-8) |
| 11 | Reichard, M., Smith, C., & Jordan, W. C. (2004). Genetic evidence reveals a high frequency of alternative mating tactics in the European bitterling (*Rhodeus sericeus*). *Molecular Ecology*, 13(8), 2211–2224. | 2004 | *Rhodeus amarus* | Cyprinidae | External | Allocation | Sperm allocation, paternity share | [10.1111/j.1365-294X.2004.02157.x](https://doi.org/10.1111/j.1365-294X.2004.02157.x) |
| 12 | Sato, T., Hirose, M., Taborsky, M., & Kimura, S. (2004). Size-dependent reproductive tactics in a shell-brooding cichlid, *Lamprologus callipterus*. *Ethology*, 110(1), 49–62. | 2004 | *Lamprologus callipterus* | Cichlidae | External | Production | GSI, testes mass, dwarf adaptation | [10.1046/j.1439-0310.2003.00947.x](https://doi.org/10.1046/j.1439-0310.2003.00947.x) |
| 13 | Smith, C. C., & Ryan, M. J. (2010). Evolution of sperm quality but not quantity in the alternative mating tactics of *Xiphophorus nigrensis*. *Journal of Evolutionary Biology*, 23(8), 1705–1714. | 2010 | *Xiphophorus nigrensis* | Poeciliidae | Internal | Production, Quality | Sperm count, velocity, viability | [10.1111/j.1420-9101.2010.02043.x](https://doi.org/10.1111/j.1420-9101.2010.02043.x) |
| 14 | Vladić, T., & Järvi, T. (2001). Sperm quality in the alternative reproductive tactics of Atlantic salmon: the importance of the loaded raffle mechanism. *Proceedings of the Royal Society of London. Series B: Biological Sciences*, 268(1483), 2375–2381. | 2001 | *Salmo salar* | Salmonidae | External | Production, Quality | Sperm velocity, longevity, loaded raffle | [10.1098/rspb.2001.1768](https://doi.org/10.1098/rspb.2001.1768) |
| 15 | Warner, R. R., Shapiro, D. Y., Marcanato, A., & Petersen, C. W. (1995). Sexual conflict: male corporate vs. individual interest in alternative mating tactics of the bluehead wrasse. *Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences*, 347(1321), 189–197. | 1995 | *Thalassoma bifasciatum* | Labridae | External | Allocation | Sperm allocation, fertilization rates | [10.1098/rspb.1995.0187](https://doi.org/10.1098/rspb.1995.0187) |

---

## Summary of Benchmark Composition

- **Total benchmark records:** 15 studies (stratified sample from Del Matto 2018).
- **Sperm allocation coverage:** 4 of 4 studies (100% of available allocation literature).
- **Production / GSI coverage:** 10 studies.
- **Sperm quality / kinetics coverage:** 10 studies.
- **Taxonomic breadth:** 10 teleost families, spanning external and internal fertilizers.
- **Target relative recall:** 100% in Web of Science and Scopus; $\ge 90\%$ across all combined sources.
