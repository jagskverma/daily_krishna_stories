# Full Corpus Report — Daily Krishna Stories

- **Date:** 2026-09-02
- **Stories:** 537 (all 537 index entries)
- **Word counts:** min 450 / max 1045 / mean 596 (target 600-900, ~450 floor for short events)
- **Generation models:** {'deepseek-v4-pro': 168, 'deepseek-v4-flash': 369} (waves 1-3 + pilot on pro before the flash switch; everything after on flash per instruction)
- **Fact checks:** 537/537 (489 full-corpus + 48 pilot). Fidelity: {5: 505, 4: 32} (all >= 4)
- **Corrections applied:** 31 sentence corrections across 27 stories (all UNSUPPORTED/CONTRADICTED fixed before assembly)

## By life stage
- birth: 17
- gokul: 22
- vrindavan: 80
- mathura: 59
- dwaraka: 180
- pandava_period: 45
- kurukshetra: 80
- later_life: 35
- other: 19

## By primary source
- Bhagavata Purana: 290
- Mahabharata: 115
- Harivamsha: 113
- Srimad Bhagavata Purana: 12
- Vishnu Purana: 7

## Content stats
- tradition_notes: 127 | content_notes: 131 | next_story_teases: 483 | hero_scenes: 537

## Arc distribution (top 12)
- pradyumna_and_aniruddha: 50
- narakasura_and_gods: 47
- kurukshetra_war: 41
- jarasandha_and_kings: 35
- peace_mission: 35
- dwaraka_royal_life: 33
- vrindavan_childhood: 31
- mathura_and_kamsa: 31
- pandava_friendship: 28
- rasa_and_gopis: 22
- rukmini_and_marriages: 19
- rajasuya_and_sisupala: 18

## Artifacts
- `data/stories/` — 537 individual story JSONs
- `data/stories.json` — assembled corpus (schema v2.0)
- `data/full_fact_checks.json` + `data/pilot_fact_checks.json` — per-claim verdicts + fidelity
- `data/pilot_stories.json` — the 48-story pilot (unchanged)
- `data/evidence_full/` — 537 evidence packs (the factual boundary)
- Dashboard: http://localhost:8199 (serves all 537)