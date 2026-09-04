# SOURCE_MANIFEST — Daily Krishna Stories, Milestone 1

Downloaded **2026-09-01** (all files; see per-source metadata JSON in
`sources/metadata/` for sha256, exact URLs, and license notes).

## Tier A sources (acquired)

| # | Work | Edition / translator | Source location | Format | Status |
|---|------|---------------------|-----------------|--------|--------|
| 1 | **Srimad Bhagavata Purana (Sanskrit)** | GRETIL e-text (data entry U. Stiehl, 2020 conversion); Vulgate recension | `gretil.sub.uni-goettingen.de` `sa_bhAgavatapurANa.txt` | plain text (IAST), verse-marked `bhp_canto.chapter.verse` | ✅ **CANONICAL** — 12 cantos, 335 chapters, 14,061 verses (Canto 10: 90 chapters, 3,936 verses) |
| 2 | **Srimadbhagabatam (M.N. Dutt, English)** | Calcutta: Elysium Press, 1895–96 | archive.org OCR scans (Books 1–2: `proseenglishtran12dutt`; Books 7–12: `india.history.resource.40625`) | djvu.txt (OCR) | ⚠️ **REFERENCE ONLY** — OCR degraded (~85–90% body legibility) and *incomplete/scrambled*: Canto 10 is missing major episodes (Kaliya, Govardhan absent); kept as raw artifact, **not** used for citations |
| 3 | **Harivamsha (M.N. Dutt, English)** | Project Gutenberg **#61937** | `gutenberg.org/cache/epub/61937/pg61937.txt` | UTF-8 text | ✅ **CANONICAL** — Part 1 (Harivamsa+Vishnu Parva, continuous ch. I–CCLXXXIII; 179 chapters parsed) + Part 2 (Bhavishya Parva, 47 ch.) |
| 4 | **Harivamsha (Sanskrit)** | GRETIL `sa_harivaMza.txt` | `gretil.sub.uni-goettingen.de` | plain text (IAST) | ✅ Sanskrit reference layer |
| 5 | **Vishnu Purana (H.H. Wilson, English)** | London: John Murray, **1840** | archive.org item `thevishnupuranacomplete6bookssethoracehaymanwilson` (clean epub digitization + djvu backup) | EPUB (XHTML) + txt | ✅ **CANONICAL** — 6 books, 126 chapters (Book V = Krishna's life, 38 chapters) |
| 6 | **Vishnu Purana (Sanskrit, critical ed.)** | GRETIL `sa_viSNupurANa-crit.txt` | `gretil.sub.uni-goettingen.de` | plain text (IAST) | ✅ Sanskrit reference layer |
| 7 | **Mahabharata (K.M. Ganguli, English, all 18 parvas)** | 1883–96 translation; Project Gutenberg ebooks 15474–15477 (Books 1–7, 12–15) + KMGanguli text files (Books 8–11, 16–18) — both derived from the proofed sacred-texts.com scans | `gutenberg.org` + `github.com/rahulnyk/mahabharata` (`text/KMGanguli`) | UTF-8 text, 2,545 sections across 18 parvas | ✅ **CANONICAL** — full 18-parva coverage |
| 8 | **Mahabharata (duplicate uploads)** | Gutenberg ebooks 7864, 7965, 11894, 12058, 12333 | gutenberg.org | UTF-8 text | ℹ️ kept as raw artifacts; identical translation, earlier uploads (Adi/Sabha/Vana/Virata) |

## What was NOT acquired, and why

- **A clean public-domain *English* Bhagavata Purana could not be located.**
  - M.N. Dutt's translation exists only as degraded/incomplete archive.org OCR
    (see #2) — the user's preference for Dutt is conditional on a *reliable*
    text, which does not exist digitally.
  - wisdomlib.org hosts the G.V. Tagare (Motilal, 1950) translation — **excluded
    as a modern copyrighted translation** (project policy: PD only).
  - English Wikisource has no Bhagavata Purana translation; sacred-texts.com
    serves none (and blocks programmatic access, HTTP 403).
  - **Resolution:** the GRETIL Sanskrit text (verse-numbered, clean) is the
    canonical Bhagavata; English excerpts for Bhagavata-primary stories are
    freshly rendered from the Sanskrit by the pipeline (own translation — PD,
    same policy as the Daily Gita project's own-translations rule).
- **Bhagavata Cantos 3–6 (English):** covered by no usable text; they contain
  almost no Krishna narrative (Kapila/Daksha/Dhruva/cosmology/Ajamila), so this
  gap does not affect the Krishna index. Noted in the milestone summary.
- **Tier B sources** (Garga Samhita, Brahma Vaivarta, Brahma Purana, Padma
  Purana): deferred until Tier A processing completes (per spec). See
  `reports/MILESTONE_1_SUMMARY.md` for the Tier B assessment.

## Provenance notes

- All canonical English translations are public domain (translators: Dutt
  d.1905, Wilson d.1860, Ganguli d.1908).
- The KMGanguli repo (rahulnyk/mahabharata) declares no license, but its book
  files reproduce the PD Ganguli translation as proofed on sacred-texts.com
  (notice of attribution retained in the files); the underlying text is PD.
- Raw downloads are never modified (`sources/raw/` is read-only by convention);
  all cleaning happens in `sources/normalized/`.
- Verse-level citations for the Bhagavata use GRETIL's `bhp_CANTO.CHAPTER.VERSE`
  numbering, which follows the standard Vulgate verse numbering.
