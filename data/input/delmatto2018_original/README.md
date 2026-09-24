# Del Matto (2018) original analysis files

Recovered from the 2018 GitHub repository `meta-analysis-Lygia` (Del Matto & Santos), archived here unchanged except for file names of the trees.

| File | Contents |
|---|---|
| `data_for_analysis.csv` | Original extraction spreadsheet (semicolon-separated, UTF-8 with BOM; some fields contain quoted line breaks). 207 rows, identical in order, *g*, *N* and SCR to Supplementary Table 1 of the dissertation. Adds exact sampling variances (`es_var`), study ID (`paper.number`), trait sub-category (`variable.type1`: `production_1` = GSI, `production_0` = quantity), absolute-gonad-mass flag (`is_abs_gonad_size`; 24 rows excluded from the 183 analysed), study design (`type.of.study`), setting (`condition`), treatment/morph labels, population, quoted methods text, and morph body sizes (mean, SD, n) for 153 rows. `?` marks missing values. |
| `fish_tree.tre` | Betancur-R et al. (2017) bony-fish phylogeny with tip labels reduced to `Genus_species`; the tree used in 2018. |
| `betancur2017_additional_file2.tre` | Same tree as published (BMC Evol. Biol. 17:162, Additional file 2), tip labels `Family_Genus_species_code`. |

`animal_on_tree` maps each species to its tip; species absent from the tree were mapped to a relative or to a placeholder added at the genus root (see `analysis/original_2018/meta-analysis.script.Rmd`).
