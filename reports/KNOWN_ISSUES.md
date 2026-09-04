# Known corpus-level issues — surfaced by the style pass, intentionally NOT fixed

The style-normalization pass (2026-09-03) only edited prose. These are
pre-existing cross-story inconsistencies in the verified narrative data that
editors flagged as out of scope. They are candidates for a future
continuity-consistency pass (facts/chronology level, not prose). Each is
internally consistent within its own story and fact-check record.

## Character / plot continuity

1. **Dhenuka's diet** — DKS_0053 (BP 10.15.23: the demon "who had made men his
   food") vs DKS_0054 (VP 5.8: "feeding on the flesh of deer"). Source-variant
   tension across two adjacent stories.
2. **Rukmi alive vs dead** — Rukmi is killed at the dice game in DKS_0207
   (BP 10.61.39), yet appears alive in later-set stories (e.g. DKS_0305 and
   the Rukmini-era HV retellings). Parallel-telling artifact.
3. **Vajranabha** — killed in DKS_0306's backstory yet alive in DKS_0307
   (parallel HV/BP tellings).
4. **Bhishmaka vs Kaishika as Rukmini's father / Krishna's host** — DKS_0191
   has Bhishmaka host Krishna; DKS_0192 has Krishna say Kaishika hosted him.
   Corpus treats the names as alternate for the same person in places.
5. **Nanda's location** — DKS_0119 ends with Nanda departing for Vrindavan in
   tears; DKS_0120 (HV arena) places Nanda in Mathura. Sequencing tension.
6. **The chariot in Karna's snake-arrow episode** — DKS_0483 ends with the
   chariot rising again; DKS_0484 (same MBh 8.90 source) keeps it sunk until
   Krishna raises it.
7. **Balarama's end** — DKS_0523 (yogic departure/death) vs DKS_0525 (he is
   later found alive). MB 16.x variant issue.
8. **DKS_0507 chain fields** (`previous: DKS_0498`, `next: DKS_0511`)
   contradict the evidence pack (0506 → 0508). Metadata chain anomaly.
9. **Pilot-vs-corpus chain divergence** — a few pilot files (e.g. DKS_0024's
   next-link) still point along the 48-story pilot chain rather than the
   full-corpus chain. The full-corpus chain is the production one.
10. **Parallel HV/BP retellings** — the corpus deliberately keeps both
    traditions; where their chronologies conflict (e.g. Mathura flight before
    vs after Jarasandha's death; the Bana-war order in HV vs BP), each story
    follows its own source. This is by design but worth a reader-facing note
    if the app ever surfaces timeline contradictions.
11. **DKS_0537 chain fields** (`previous_story_id: DKS_0530`) contradict its
    evidence pack (DKS_0536). Same class as #8 — metadata anomaly, style pass
    left it untouched.

## Misc data hygiene

11. `source_event_id` mismatches vs evidence packs on a small number of files
    (e.g. DKS_0047: metadata evt_0058 vs pack evt_0059) — noted, not changed.
12. A handful of stories carry `estimated_read/audio_minutes` keys in a
    different order than the schema example (cosmetic; parsers are order-
    agnostic).

## Recommendation

Run a **continuity pass** (LLM, evidence-grounded) over items 1-10 that decides
per conflict whether to (a) harmonize, (b) keep-as-variant with a
`tradition_note`, or (c) adjust chronology metadata — before the stories ship
to users who may read them out of order or back-to-back.
