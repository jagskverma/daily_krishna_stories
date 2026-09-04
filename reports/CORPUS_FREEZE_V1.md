# Corpus Freeze — V1

- **Freeze date:** 2026-09-01
- **Canonical event count:** 537 (raw events mined: 721)
- **Story index count:** 537
- **Multi-source events:** 116 | **Variant traditions flagged:** 166

## Counts by primary source
- Srimad Bhagavata Purana (Sanskrit, GRETIL): **302**
- Mahabharata (Ganguli translation): **115**
- Harivamsha (Dutt, Gutenberg #61937): **113**
- Vishnu Purana (Wilson 1840): **7**

## Counts by life stage
- birth: 17
- gokul: 22
- vrindavan: 80
- mathura: 59
- dwaraka: 180
- pandava_period: 45
- kurukshetra: 80
- later_life: 35
- other: 19

## Counts by arc
- Akrura's arrival and departure (`akrura_and_departure`): 8
- Balarama's stories (`balarama_stories`): 11
- Birth of Krishna (`birth_of_krishna`): 8
- Draupadi's honour (`draupadi_honour`): 4
- Dwaraka founded (`dwaraka_founded`): 4
- Dwaraka court and royal life (`dwaraka_royal_life`): 33
- Early Gokul childhood (`early_gokul_childhood`): 16
- The end of the Yadavas (`end_of_yadavas`): 8
- Govardhan and Indra (`govardhan_and_indra`): 11
- Jarasandha and the kings (`jarasandha_and_kings`): 35
- Kaliya and the Yamuna (`kaliya_and_yamuna`): 9
- Krishna's departure (`krishna_departure`): 9
- Krishna reaches Gokul (`krishna_reaches_gokul`): 7
- Kurukshetra war (`kurukshetra_war`): 41
- Mathura and Kamsa (`mathura_and_kamsa`): 31
- Narakasura and the gods (`narakasura_and_gods`): 47
- Other / frame stories (`other`): 3
- The Pandavas: friendship (`pandava_friendship`): 28
- The peace mission (`peace_mission`): 35
- Post-war Krishna (`post_war_krishna`): 14
- Pradyumna and Aniruddha (`pradyumna_and_aniruddha`): 50
- The prophecy of Kamsa (`prophecy_of_kamsa`): 7
- Rajasuya and Shishupala (`rajasuya_and_sisupala`): 18
- Rasa and the gopis (`rasa_and_gopis`): 22
- Rukmini and the marriages (`rukmini_and_marriages`): 19
- Syamantaka jewel (`syamantaka_jewel`): 11
- Uddhava and the teachings (`uddhava_and_teachings`): 17
- Vrindavan childhood (`vrindavan_childhood`): 31

## Near-duplicate decisions (all 17 audit pairs + round 2)
See `reports/NEARDUP_REVIEW.md` for the full evidence. Summary:
- MERGE: 15 clusters from audit round 1 (Kalayavana/Muchukunda, Sesha, Balarama Vraja visit, Balarama drags the Yamuna, Uddhava to Badarikashrama, Prabhasa fratricide ×3-way, Samba curse, Shishupala outburst, Shishupala slaying, Magadha journey, Jarasandha reveal, 16,000-wives sports, naming the Pandavas, abandon Mathura, Dwaraka founding) + 1 from round 2 (Sonitpura Garuda flight) = **16 merges applied**
- KEEP_SEPARATE_VARIANT: 2 (Rajasuya plan attribution Krishna-vs-Uddhava; Sudharman hall Mathura-vs-Dwaraka placement)
- KEEP_SEPARATE_DISTINCT: 3 audit claims rejected (embryo transfer beats; Draupadi vow 3.12 vs 5.82; Samba curse vs iron-bolt birth) + 9 mechanical-sweep pairs reviewed as distinct beats

## QA status
- `scripts/validate_index.py`: **PASS, 0 failures** (≥500 stories ✓, unique ids ✓, required fields ✓, valid primary refs ✓, no duplicate titles/summaries ✓, no near-duplicate events ✓, arcs valid ✓, chronological ordering ✓, enums valid ✓)
- Semantic near-duplicate audit round 2: **clean** (3 pairs found, all resolved above)

## Hashes
- `SOURCE_MANIFEST.md` sha256: 12328ad77a0d25b720e07b2e2042754fc828f874ff696375a5e3ee888a068a64
- `data/canonical_events.json` sha256: ba23d4819128a0b4ea34d6951ea1513d3bc0fa3a65d8a516b6ff441062298d70
- `data/story_index.json` sha256: 57a66c9183de34bae405d4bf5994ee8aa99fed4901b2be5710c625c357b7690e
- `data/story_index.csv` sha256: 651741b329a5fbdef1039274cac97d3e2222c7832bf644787961cd75a2e8be2f

## Freeze terms
`data/canonical_events.json` is the authoritative semantic event database; `data/story_index.json` is the authoritative story catalogue. Neither will be silently mutated during Milestone 2; any future change goes through the pipeline (`merge_events.py` → `build_index.py` → `validate_index.py`) and is recorded here.
## Addendum (known ordering quirk — recorded, not changed)
The birth sequence indexes Kamsa's slaying of the newborn girl (BP 10.4, arc
birth_of_krishna) BEFORE the Yamuna crossing (BP 10.3.46-49, arc
krishna_reaches_gokul) because arc order (20 < 30) outranks chapter order. The
crossing chronologically precedes 10.4. The frozen corpus keeps this ordering
(arc taxonomy is authoritative); the 48-story pilot chain was corrected directly
to read 0013 (birth) -> 0018 (crossing) -> 0015 (girl) -> 0024 (Putana).
