# Milestone 1 Summary — Daily Krishna Stories

Generated: 2026-09-01 | Schema: story_index v1.0

## Corpus
- Sources downloaded: **7** (Tier A) + 2 Sanskrit reference layers; see `SOURCE_MANIFEST.md`
- Raw files: Harivamsha (Gutenberg #61937), Mahabharata 18 parvas (Ganguli), Vishnu Purana (Wilson 1840 epub), Bhagavata Purana Sanskrit (GRETIL, 335 ch / 14,061 verses) + Dutt-OCR artifact (reference only)
- Normalized corpus: 2788 structural units in `sources/normalized/`

## Index
- **Stories indexed: 537** (target 500+)
- Raw events mined: 721 -> canonical events after cross-source dedup: 537 -> index entries: 537
- Multi-source events: 116 | Variant traditions flagged: 166

### Stories by primary source
- Srimad Bhagavata Purana (Sanskrit, GRETIL): **302** (56.2%)
- Mahabharata (Ganguli translation): **115** (21.4%)
- Harivamsha (Dutt, Gutenberg #61937): **113** (21.0%)
- Vishnu Purana (Wilson 1840): **7** (1.3%)

### Source attestations (primary + additional; one story may cite several sources)
- Srimad Bhagavata Purana (Sanskrit, GRETIL): 315
- Harivamsha (Dutt, Gutenberg #61937): 183
- Mahabharata (Ganguli translation): 138
- Vishnu Purana (Wilson 1840): 85

### Stories by life stage
- birth: **17** (3.2%)
- gokul: **22** (4.1%)
- vrindavan: **80** (14.9%)
- mathura: **59** (11.0%)
- dwaraka: **180** (33.5%)
- pandava_period: **45** (8.4%)
- kurukshetra: **80** (14.9%)
- later_life: **35** (6.5%)
- other: **19** (3.5%)

### Stories by arc
- The prophecy of Kamsa (`prophecy_of_kamsa`): **7**
- Birth of Krishna (`birth_of_krishna`): **8**
- Krishna reaches Gokul (`krishna_reaches_gokul`): **7**
- Early Gokul childhood (`early_gokul_childhood`): **16**
- Vrindavan childhood (`vrindavan_childhood`): **31**
- Kaliya and the Yamuna (`kaliya_and_yamuna`): **9**
- Govardhan and Indra (`govardhan_and_indra`): **11**
- Rasa and the gopis (`rasa_and_gopis`): **22**
- Akrura's arrival and departure (`akrura_and_departure`): **8**
- Mathura and Kamsa (`mathura_and_kamsa`): **31**
- Jarasandha and the kings (`jarasandha_and_kings`): **35**
- Dwaraka founded (`dwaraka_founded`): **4**
- Rukmini and the marriages (`rukmini_and_marriages`): **19**
- Syamantaka jewel (`syamantaka_jewel`): **11**
- Narakasura and the gods (`narakasura_and_gods`): **47**
- Dwaraka court and royal life (`dwaraka_royal_life`): **33**
- Pradyumna and Aniruddha (`pradyumna_and_aniruddha`): **50**
- Balarama's stories (`balarama_stories`): **11**
- The Pandavas: friendship (`pandava_friendship`): **28**
- Rajasuya and Shishupala (`rajasuya_and_sisupala`): **18**
- Draupadi's honour (`draupadi_honour`): **4**
- The peace mission (`peace_mission`): **35**
- Kurukshetra war (`kurukshetra_war`): **41**
- Post-war Krishna (`post_war_krishna`): **14**
- Uddhava and the teachings (`uddhava_and_teachings`): **17**
- The end of the Yadavas (`end_of_yadavas`): **8**
- Krishna's departure (`krishna_departure`): **9**
- Other / frame stories (`other`): **3**

### Source-confidence distribution
- confidence 3: 1 (0.2%)
- confidence 4: 234 (43.6%)
- confidence 5: 302 (56.2%)

### Age sensitivity
- all: 418
- mature: 1
- mild_violence: 118

### Festival tags (top 10)
- Naga Panchami: 7
- Janmashtami: 6
- Govardhan Puja: 4
- Diwali: 1
- Naraka Chaturdashi: 1

## Corpus gaps & notes
- Bhagavata Purana English: no clean public-domain English translation exists digitally. Canonical BP text is the GRETIL Sanskrit (verse-numbered); excerpts for BP-primary stories are freshly rendered from Sanskrit (own-translation policy, same as Daily Gita). The M.N. Dutt 1895-96 OCR (archive.org) is degraded/incomplete (Canto 10 missing Kaliya/Govardhan material) — kept as a reference artifact with confidence 1.
- Bhagavata Cantos 3-6: no usable English edition; negligible Krishna narrative content (Kapila/Daksha/Dhruva/cosmology/Ajamila).
- Mahabharata books 8-11 and 16-18 came from the KMGanguli compilation (same proofed sacred-texts text); books 1-7 and 12-15 from Gutenberg. Section numbering follows the edition; a handful of section headings are embedded in adjacent files (noted in individual records).
- Harivamsha (Gutenberg #61937) is missing some chapter headings (e.g. LV, LXVIII, LXIX, LXXI); affected citations were re-anchored to the containing chapter with an explicit note and confidence 3.
- Tier B (Garga Samhita, Brahma Vaivarta, Brahma Purana, Padma Purana): assessed; no clean public-domain English edition exists (Garga Samhita: none; Brahma Vaivarta: only a murky 1955 printing; Brahma Purana: only copyrighted Motilal translation; Padma Purana: none). Per the PD-only policy they were not acquired. Tier A produced 554 stories, so no Tier B expansion was required.
- VP Book V contributed 85 mined events, most of which merged into BP/HV-led clusters (only 9 remain VP-primary) — its attestations are counted in the attestation table.
