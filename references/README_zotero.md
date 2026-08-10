# Reference management — Zotero + Better BibTeX

The protocol's bibliography is managed in **Zotero** with the **Better BibTeX (BBT)**
extension and auto-exported to [`sperm_competition_meta.bib`](sperm_competition_meta.bib) in this
folder. The protocol reads that file through its YAML front-matter:

```yaml
bibliography: ../references/sperm_competition_meta.bib
```

`sperm_competition_meta.bib` is a **generated file** — edit references in Zotero, not by hand.
Citation keys (e.g. `@salo2007`, `@doherty2016`) are the contract between the `.bib` and the
protocol prose, so they must stay stable.

## One-time setup

1. **Install Better BibTeX** — in Zotero: *Tools → Add-ons → install from the `.xpi`*
   downloaded from <https://retorque.re/zotero-better-bibtex/installation/>. Restart Zotero.

2. **Bootstrap the collection from this file (keeps the existing keys).**
   - Create a collection, e.g. **`sperm_competition_meta`**.
   - With BBT installed, importing a `.bib` **preserves and pins the imported citation keys**
     (in Zotero 8 keys are always pinned). Confirm this is on: *Settings → Better BibTeX →
     Import → "Keep keys on import"* (or the hidden pref `better-bibtex.importCitationKey`).
   - *File → Import…* → select `sperm_competition_meta.bib` → import **into that collection**.
     The 52 entries arrive with the exact keys used in the protocol.

   *(Alternative: if you already curate these references elsewhere in Zotero, drag them into
   the collection instead, then pin each key to match — right-click → Better BibTeX → set/pin
   citation key — so they equal the keys in the protocol.)*

3. **Set up automatic export back to this file.**
   - Right-click the collection → **Export Collection…**
   - Format **Better BibTeX**; tick **Keep updated**.
   - Save as `sperm_competition_meta.bib` **in this `references/` folder** (overwrite it).
   - From now on, every change in Zotero rewrites this file automatically.

## Day-to-day

- **Add a study:** add it to the `sperm_competition_meta` collection in Zotero. BBT re-exports
  the file; cite it in the protocol with `[@citekey]` (see the key in Zotero's *Citation Key*
  field, or *right-click → Better BibTeX → Copy citation key*).
- **Citation-key style:** to make new keys look like the existing ones
  (`surname` + `year`, lower-case), set *Settings → Better BibTeX → Citation keys →
  formula* to `auth.lower + year` and pin any collisions. Existing pinned keys are untouched.
- **Two works, same author & year** (e.g. Viechtbauer 2010 ×2) are disambiguated by a suffix;
  here they are pinned as `viechtbauer2010` and `viechtbauerCheung2010`.

## Rendering the protocol (resolves `@keys` → formatted list)

The reference list is generated on render into the `::: {#refs}` block; do not maintain it by
hand. Either tool works:

```bash
# Quarto (bundles pandoc; no separate install)
quarto render 02_update_protocol.md

# or pandoc directly
pandoc --citeproc 02_update_protocol.md -o 02_update_protocol.pdf
```

Run from the `protocol/` directory so the relative `../references/…` path resolves. To apply a
journal style, drop a `.csl` file in `references/` and add `csl: ../references/<style>.csl` to
the protocol's YAML (default is Chicago author–date).

## Notes

- The protocol's YAML `nocite:` block lists a few references that are in the library but not
  yet cited in the prose, so they still appear in the list. When you cite one inline with
  `[@key]`, remove it from `nocite`.
- Keep `sperm_competition_meta.bib` tracked in git: it is the fallback that lets the protocol
  render on any machine even before Zotero/BBT is configured there.
