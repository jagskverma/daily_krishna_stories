# Daily Krishna Stories — content corpus

Public-domain, source-grounded Krishna narrative corpus for the Daily Krishna
Stories app (dailyX family, sibling of Daily Gita). **Corpus V1 frozen:
537 stories**, all fact-checked and style-normalized.

## What's here

| Path | Contents |
|---|---|
| `data/stories.json` | **Production dataset — all 537 stories** (single file) |
| `data/stories/` | Per-story JSON (full-corpus stories, DKS_0001–0536 range) |
| `data/pilot_stories/` | Per-story JSON (48-story editorial pilot subset) |
| `data/story_index.json` / `.csv` | Canonical 537-entry story catalogue |
| `data/canonical_events.json` | Merged, deduplicated event database |
| `data/archive/` | Pre-normalization rollback snapshot (`stories_factchecked_v1/`) |
| `data/evidence_full/`, `data/pilot_evidence/` | Source evidence packs per story |
| `data/full_fact_checks.json`, `data/pilot_fact_checks.json` | Fact-check records (fidelity scores) |
| `data/mining/` | Raw mined events, near-dup audits, style reports |
| `sources/` | Raw downloads + normalized corpus + provenance metadata (see `SOURCE_MANIFEST.md`) |
| `docs/` | Editorial, mining, writing, fact-check, style guides |
| `reports/` | Milestone summaries, near-dup review, style report, known issues |
| `scripts/` | Acquisition → normalize → mine → merge → validate → QA pipeline |
| `review_dashboard/` | Local editorial review dashboard (python server, port 8199) |

## Sources (all public domain)

- **Srimad Bhagavata Purana** — GRETIL Sanskrit (canonical; own translations, per project policy)
- **Harivamsha** — M.N. Dutt, Project Gutenberg #61937
- **Vishnu Purana** — H.H. Wilson, 1840
- **Mahabharata** — K.M. Ganguli, all 18 parvas

Full provenance (editions, URLs, dates, sha256, license notes) in
[`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md) and `sources/metadata/`.

## Corpus numbers

- 537 stories (48 editorial pilot + 489 full corpus)
- All fact-checked: fidelity ≥ 4/5; 31 corrections applied
- All style-normalized to the house voice (pass v1)
- `editorial_status: unreviewed` on every story — human review is the
  shipping gate (see `review_dashboard/`)

## Notes

- Source translations are public domain (Dutt d.1905, Wilson d.1860,
  Ganguli d.1908); English renderings of Bhagavata verses are the project's
  own translations. The story corpus itself is original project content.
- `app/` (Flutter scaffold) and raw large downloads are not in this repo;
  raw sources are re-downloadable per `SOURCE_MANIFEST.md`.
- Known pre-existing cross-story continuity quirks: `reports/KNOWN_ISSUES.md`.
