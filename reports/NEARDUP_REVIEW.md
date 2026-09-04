# Near-Duplicate Review — Corpus V1

Date: 2026-09-01
Scope: the 17 suspicious pairs flagged by audit round 1 (`data/mining/neardup/result_a/b.jsonl`),
plus additional pairs found by a mechanical title/summary overlap sweep and a
manual keyword-targeted review of every audit reason.

**Critical finding about audit round 1:** the round-1 audit agents produced
*reliable reasons but unreliable id pairings* — in 17/17 cases the listed DKS
ids did not correspond to the stated reason (e.g. it paired two MB Karna-dialogue
events with a reason about the Prabhasa fratricide). Every reason was therefore
re-verified against the actual corpus, and the true duplicate pairs were located
by content. Decisions below are based on the actual events, not the audit's ids.

## Summary of decisions

| # | Audit reason (paraphrased) | Decision | Merged events (post-merge DKS id) |
|---|---|---|---|
| 1 | Balarama's embryo transfer (HV vs BP) | KEEP_SEPARATE_DISTINCT | — |
| 2 | Kalayavana burned by Muchukunda (HV vs BP) | MERGE | DKS_0173 (3 sources) |
| 3 | Rajasuya slaying-plan: Krishna vs Uddhava attribution | KEEP_SEPARATE_VARIANT | — (cross-notes added) |
| 4 | Disguised journey to Magadha/Girivraja (MB vs BP) | MERGE | DKS_0181 (2 sources) |
| 5 | Reveal + challenge Jarasandha (MB vs BP) | MERGE | DKS_0182 (2 sources) |
| 6 | Yadavas resolve to abandon Mathura (HV, two locators) | MERGE | DKS_0301 (2 sources) |
| 7 | Founding of Dwaraka (BP vs HV Viswakarma) | MERGE | DKS_0189 (3 sources) |
| 8 | Yadava fratricide at Prabhasa (VP / BP / MB) | MERGE | DKS_0524 (5 sources) |
| 9 | Sages curse Samba/Samva (BP vs MB) | MERGE | DKS_0520 (4 sources) |
| 10 | Sesha departs from Balarama (VP vs MB) | MERGE | DKS_0522 (2 sources) |
| 11 | Balarama drags the Yamuna (HV vs BP) | MERGE | DKS_0354 (3 sources) |
| 12 | Balarama revisits Vraja/Gokula (HV vs BP) | MERGE | DKS_0353 (3 sources) |
| 13 | Krishna sports with the 16,000 wives (BP vs HV) | MERGE | DKS_0496 (2 sources) |
| 14 | Krishna sends Uddhava to Badarikashrama (VP vs BP) | MERGE | DKS_0518 (4 sources) |
| 15 | Shishupala's outburst at the Rajasuya (BP vs MB) | MERGE | DKS_0398 (3 sources) |
| 16 | Krishna's vow to weeping Draupadi (MB 3.12 vs 5.82) | KEEP_SEPARATE_DISTINCT | — |
| 17 | Krishna names the Pandavas to Balarama (MB 1.189 vs 1.191) | MERGE | DKS_0364 (2 sources) |
| +1 | Shishupala's slaying (BP vs MB) — found during verification of #15 | MERGE | DKS_0399 (2 sources) |

15 merge clusters applied (14 from the audit reasons + 1 extra); 1 variant pair;
2 audit claims rejected as distinct events.

---

## Detailed decisions

### 1. Balarama's embryo transfer — KEEP_SEPARATE_DISTINCT

- Story A: `Devaki's Seventh Embryo Is Transferred to Rohini` — Harivamsha 1.59
- Story B: `The Conception of Devaki and the Six Demon Embryos` — Bhagavata Purana 10.2.15–23
- Decision: KEEP_SEPARATE_DISTINCT
- Reason: two different beats. The HV entry narrates the *transfer* of the seventh
  embryo (Sankarshana/Balarama) to Rohini; the BP entry narrates the *conception*
  (Vishnu entering Vasudeva's mind, Devaki glowing, Kamsa restraining himself).
  The BP chapter does also contain the transfer, but the indexed BP beat is the
  conception, not the transfer — no true duplicate exists in the index.
- Primary-source evidence: HV 1.59 ("I have extracted the embryo out of Devaki's
  womb and placed it in yours... Sangkarshana"); BP 10.2.15–23 (conception; Kamsa
  "refrains from harming her").
- ID changes: none.

### 2. Kalayavana burned by Muchukunda — MERGE

- Story A: `Kalayavana Is Burned by Muchukunda's Gaze` — Harivamsha 1.114
- Story B: `Kalayavana Is Burned by Muchukunda's Glance` — Bhagavata Purana 10.51
- Decision: MERGE → **DKS_0173** `Kalayavana Is Burned by Muchukunda's Glance` (3 sources: BP 10.51, HV 1.114, VP 5.24)
- Reason: identical narrative event (Krishna lures Kalayavana into the cave; the
  sleeping Muchukunda burns him with his gaze) in two/three traditions with the
  same actors, action and outcome.
- Primary-source evidence: BP 10.51; HV 1.114; VP 5.24 (host seized / cave).

### 3. Rajasuya slaying-plan — KEEP_SEPARATE_VARIANT

- Story A: `Krishna Proposes Slaying Jarasandha as Prelude to the Rajasuya` — Mahabharata 2.20
- Story B: `Uddhava's Counsel to Slay Jarasandha` — Bhagavata Purana 10.71
- Decision: KEEP_SEPARATE_VARIANT
- Reason: same strategic plan (slay Jarasandha before the Rajasuya) but a
  *materially different attribution*: the Mahabharata presents Krishna himself
  proposing it; the Bhagavata presents it as Uddhava's counsel to Krishna. Both
  versions are worth telling; each is a different dramatic scene. Cross-references
  added to both events' variant_notes (raw events `mb_a2_002`, `bp10d_004`).
- ID changes: none.

### 4. Disguised journey to Girivraja — MERGE

- Story A: `Krishna, Bhima and Arjuna Set Out for Magadha in Disguise` — Mahabharata 2.20
- Story B: `Approaching Jarasandha in Disguise` — Bhagavata Purana 10.72.14–26
- Decision: MERGE → **DKS_0181** `Krishna, Bhima and Arjuna Approach Jarasandha in Disguise` (2 sources)
- Reason: same journey beat (three heroes travel disguised as brahmanas to
  Girivraja and ask alms of Jarasandha).
- Primary-source evidence: MB 2.20; BP 10.72.14–26.

### 5. Reveal + challenge — MERGE

- Story A: `Krishna Reveals Their Identities and Challenges Jarasandha` — Mahabharata 2.22
- Story B: `Jarasandha Taunts Krishna` (reveal + taunt + single combat set) — Bhagavata Purana 10.72.27–32
- Decision: MERGE → **DKS_0182** `Krishna Reveals Their Identities and Challenges Jarasandha` (2 sources)
- Reason: same confrontation beat.
- Primary-source evidence: MB 2.22; BP 10.72.27–32.

### 6. Resolve to abandon Mathura — MERGE

- Story A: `The Vrishnis Resolve to Abandon Mathura for Dwarka` — Harivamsha, cited 1.35 (citation repair: content is the Kalayavana-era flight, ch ~113)
- Story B: `Krishna Proposes Leaving Mathura for the West` — Harivamsha 1.113
- Decision: MERGE → **DKS_0301** `The Yadavas Resolve to Abandon Mathura for Dwaraka` (2 sources)
- Reason: the same decision moment (Kalayavana's messenger; the Vrishnis resolve
  to leave Mathura for Kushasthali), duplicated across two HV locators. One
  member's printed locator (1.35, "Vasudeva's Family") does not contain this
  passage — re-anchored to ch 113 by content match, confidence lowered to 3,
  repair noted in the record.
- Primary-source evidence: HV ~1.113; the mis-cited 1.35 record flagged.
- ID changes: merged; mis-citation repaired.

### 7. Founding of Dwaraka — MERGE

- Story A: `Krishna Founds Dvaraka` — Bhagavata Purana 10.50
- Story B: `Viswakarma Builds Dwaraka` — Harivamsha 1.115
- Decision: MERGE → **DKS_0189** `Viswakarma Builds Dwaraka for Krishna` (3 sources: BP 10.50, HV 1.115, VP 5.24)
- Reason: same event (Krishna selects the sea-site; the divine architect raises
  the city). Site-selection, Garuda's report, enrichment and later adornment
  remain separate beats.
- Primary-source evidence: BP 10.50; HV 1.115.

### 8. Yadava fratricide at Prabhasa — MERGE

- Story A: `The Yadavas Destroy One Another` — Vishnu Purana 5.37
- Story B: `The Yadava Fratricide at Prabhasa` — Bhagavata Purana 11.30.11–25
- Story C: `The Drunken Quarrel at Prabhasa` — Mahabharata 16.3
- Decision: MERGE → **DKS_0524** `The Yadava Fratricide at Prabhasa` (5 sources: BP 11.30 ×2 beats, MB 16.3, VP 5.37)
- Reason: the same catastrophe (the kinsmen's mutual slaughter with reed-weapons
  after the drunken quarrel) in three traditions. The separate "journey to
  Prabhasa" beat is kept.
- Primary-source evidence: BP 11.30.11–25; VP 5.37; MB 16.3.

### 9. Sages curse Samba — MERGE

- Story A: `The Sages Curse Samba and the Yadavas` — Bhagavata Purana 11.1.13–23
- Story B: `The Sages Curse the Vrishnis Through Samva` — Mahabharata 16.1
- Decision: MERGE → **DKS_0520** `The Sages Curse Samba and the Yadavas` (4 sources: BP 11.1, BP 1.x recall, MB 16.1, VP 5.37)
- Reason: same curse episode (youths disguise Samba as a pregnant woman; the
  sages curse him to bear the iron bolt that destroys the dynasty).
- Primary-source evidence: BP 11.1.13–23; MB 16.1.

### 10. Sesha departs — MERGE

- Story A: `Sesha Departs from Balarama` — Vishnu Purana 5.37
- Story B: `Balarama Departs as the White Serpent` — Mahabharata 16.4
- Decision: MERGE → **DKS_0522** `Sesha Departs from Balarama` (2 sources)
- Reason: same departure scene (the serpent issues from Balarama and enters the ocean).
- Primary-source evidence: VP 5.37; MB 16.4.

### 11. Balarama drags the Yamuna — MERGE

- Story A: `Balarama Drags the Yamuna` — Harivamsha 1.102
- Story B: `Balarama Drags the Yamuna with His Plough` — Bhagavata Purana 10.65
- Decision: MERGE → **DKS_0354** `Balarama Drags the Yamuna` (3 sources: BP 10.65, HV 1.102, VP 5.25)
- Reason: same feat during Balarama's Dwaraka-era return visit to Vraja
  (inebriated, he drags the river with his plough until she begs pardon).
- Primary-source evidence: BP 10.65; HV 1.102.

### 12. Balarama revisits Vraja — MERGE

- Story A: `Balarama Revisits Vraja` — Harivamsha 1.102
- Story B: `Balarama Visits the Gopis of Gokula` — Bhagavata Purana 10.65.1–17
- Decision: MERGE → **DKS_0353** `Balarama Revisits Vraja` (3 sources: BP 10.65, HV 1.102, VP 5.24)
- Reason: same visit (Balarama returns to Nanda's village and stays with the
  cowherds and gopis). Distinct from the Yamuna-drag beat (separate merge #11).
- Primary-source evidence: BP 10.65.1–17; HV 1.102.

### 13. Krishna sports with the 16,000 wives — MERGE

- Story A: `Krishna Sports with His Sixteen Thousand Wives in the Ocean` — Harivamsha 1.235
- Story B: `Krishna's Water-Sports with His Queens` — Bhagavata Purana 10.90.1–24
- Decision: MERGE → **DKS_0496** `Krishna Sports with His Sixteen Thousand Wives` (2 sources)
- Reason: same scene (simultaneous water-sports; each queen believes she alone
  is favoured). The *marriage* to the princesses (BP 10.59) is a different event.
- Primary-source evidence: HV 1.235; BP 10.90.1–24.

### 14. Uddhava sent to Badarikashrama — MERGE

- Story A: `Krishna Sends Uddhava to Badarikashrama` — Vishnu Purana 5.37
- Story B: `Uddhava Departs for Badarikashrama` — Bhagavata Purana 11.29.40–47
- Decision: MERGE → **DKS_0518** `Krishna Sends Uddhava to Badarikashrama` (4 sources: BP 11.29, BP 1.x, MB 16.x, VP 5.37)
- Reason: same final instruction/departure of Uddhava.
- Primary-source evidence: VP 5.37; BP 11.29.40–47.

### 15. Shishupala's outburst — MERGE

- Story A: `Shishupala's Outburst Against Krishna's Honor` — Bhagavata Purana 10.74.29–41
- Story B: `Shishupala Derides Krishna's Deeds and Bhima's Wrath` — Mahabharata 2.41
- Decision: MERGE → **DKS_0398** `Shishupala's Outburst Against Krishna` (3 sources: BP 10.74, MB 2.41, + recall)
- Reason: same assembly scene (the insults at the Rajasuya). Surrounding beats
  (Bhishma's foretelling MB 2.40, the kings incited MB 2.39, the mother's boon
  MB 2.42) are kept separate.
- Primary-source evidence: BP 10.74.29–41; MB 2.41.

### +1. Shishupala's slaying — MERGE (extra)

- Story A: `Krishna Slays Shishupala` — Bhagavata Purana 10.74.42–45
- Story B: `Krishna Fulfils the Prophecy over Infant Shishupala` — Mahabharata 2.42
- Decision: MERGE → **DKS_0399** `Krishna Slays Shishupala` (2 sources)
- Reason: same event (the discus ends Shishupala at the hundredth offence;
  the MB entry frames it as the prophecy's fulfilment). Found while verifying #15.
- Primary-source evidence: BP 10.74.42–45; MB 2.42.

### 16. Krishna's vow to weeping Draupadi — KEEP_SEPARATE_DISTINCT

- Story A: `Krishna Promises Draupadi She Will Be Queen Again` — Mahabharata 3.12 (Vana Parva visit)
- Story B: `Krishna Vows the Kuru Women Will Weep` — Mahabharata 5.82 (Udyoga Parva appeal)
- Decision: KEEP_SEPARATE_DISTINCT
- Reason: two different visits at two different times with different content.
  In Vana (3.12) Krishna consoles Draupadi in the Kamyaka forest and promises the
  restoration of queenship; in Udyoga (5.82) she appeals before the peace mission
  and he vows the Kuru women will weep. Superficially similar "consolation + vow"
  shape, but distinct narrative moments. The audit's "same vow" reading is a
  false positive.
- Primary-source evidence: MB 3.12; MB 5.82.
- ID changes: none.

### 17. Krishna names the Pandavas to Balarama — MERGE

- Story A: `Krishna Recognizes the Disguised Pandavas at Draupadi's Svayamvara` — Mahabharata 1.189
- Story B: `Krishna Names Each Pandava to Balarama` — Mahabharata 1.191
- Decision: MERGE → **DKS_0364** `Krishna Names the Pandavas to Balarama` (2 sources: MB 1.189, 1.191)
- Reason: the same identification scene (Krishna tells Balarama who each
  disguised brother is), split into two beats by the miner; 1.191 merely
  continues the same moment after Bhima's feat. Both locators retained.
- Primary-source evidence: MB 1.189; 1.191.

---

## Additional pairs reviewed (mechanical sweep, all KEEP_SEPARATE_DISTINCT)

- `Krishna Lifts Govardhana Hill` vs `Seven Days Beneath Govardhana` (BP 10.25) — distinct beats of one episode (adjacent verse ranges; validator-approved).
- `Krishna Notices the Twin Arjuna Trees` (BP 10.9) vs `Narada Curses Nalakuvara and Manigriva` (BP 10.10) — the act vs the embedded backstory; both tellable separately.
- `Uddhava Arrives Bearing Krishna's Message` (BP 10.47) vs `Krishna Sends Uddhava to Vrindavan` (BP 10.46) — send vs arrive beats.
- `Krishna Destroys the Flying City Saubha` (BP 10.77) vs `Krishna Slays Dantavakra and Viduratha` (BP 10.78) — distinct events of the same war.
- `Krishna Marches on Sonitpura in Divine Form` (HV 1.264) vs `Krishna Summons Garuda and Marches to Rescue Aniruddha` (HV 1.268) — distinct phases of the Bana campaign.
- `Jvara Consumes Baladeva` (HV 1.270) vs `Jvara Possesses Krishna` (HV 1.271) — sequential beats of the fever episode.
- `Jarasandha Hurls His Mace toward Mathura` (MB 2.19) vs `The Yadavas Rout Jarasandha's Army and Spare Him` (BP 10.50) — different beats of the siege (attack vs rout), different narrative framings.
- `Krishna Marries the Sixteen Thousand Princesses` (BP 10.59) vs the merged water-sports (BP 10.90/HV 1.235) — wedding vs sports, distinct.
- `Muchukunda's Story` (BP 10.51) vs `Kalayavana Is Burned by Muchukunda's Glance` — embedded backstory vs the death event.

## Verification

- All merges applied through the pipeline (`data/mining/clusters/neardup_merges.jsonl`), not by direct mutation: `merge_events.py` → `build_index.py` → `validate_index.py` (PASS, 0 failures).
- Arc overrides re-applied via rule file `data/mining/arc_overrides.json` (pipeline-reproducible).
- Semantic near-duplicate audit re-run on the merged corpus (round 2) — see `data/mining/neardup2/result_a/b.jsonl`; corpus frozen only if clean.


---

## Round-2 audit (post-merge) — 2026-09-01

Re-run of the semantic near-duplicate audit on the merged corpus
(`data/mining/neardup2/result_a/b.jsonl`). Three pairs found; all resolved:

1. **DKS_0322 ~ DKS_0330** (Harivamsha 1.264 vs 1.268 — "march on Sonitpura" /
   "summons Garuda"): MERGE. Both narrate the same departure beat of the Bana-war
   rescue (Krishna, Balarama and Pradyumna flying on Garuda to free Aniruddha);
   the miner split one departure into two beats. Merged as **DKS_0322**
   `Krishna, Balarama and Pradyumna Fly to Sonitpura on Garuda` (2 sources).
2. **DKS_0520 ~ DKS_0525** (Sages-curse event vs "Samva Brings Forth the Iron
   Bolt"): KEEP_SEPARATE_DISTINCT. The curse, the bolt's birth/disposal, and the
   Prabhasa catastrophe are a causal sequence of three distinct events; the audit
   reason conflated the disposal with the curse.
3. **DKS_0126 ~ DKS_0187** (Sudharman hall): KEEP_SEPARATE_VARIANT. Vishnu Purana
   5.21 fetches the celestial hall for Ugrasena at Mathura; Harivamsha 1.115
   folds the hall into Dwaraka's enrichment. Same motif, materially different
   placement — cross-referenced in both events' variant_notes.

No high-confidence duplicates remain. **Corpus V1 frozen.**
