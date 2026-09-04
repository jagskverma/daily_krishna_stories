# STYLE_NORMALIZATION_REPORT.md

Pass: **style normalization v1** · Model: **DeepSeek V4 Flash** · Date: 2026-09-03
Scope: editorial prose-only pass over the full fact-checked corpus. NOT a generation pass.

## Numbers

- **Stories processed:** 537 / 537 (489 full-corpus + 48 pilot)
- **Changed levels (self-reported per story):**
  - major rewrite: 249
  - minor/targeted edit: 288
  - unchanged: 0 (every story received at least a targeted edit; none needed no touch)
- **Standalone-context added:** 343 stories (first-reader context woven into openings)
- **Reflections:** left untouched except a handful re-voiced into the 40–80 word band (all still within §18)
- **Word counts:** min 441 (DKS_0079, single story marginally under the 450 floor — left as-is to avoid padding) · max 1037 (DKS_0490, a deliberately long VP narrative) · mean ~589 · only 1 story over 900; ~20 in the 700–900 "longer is acceptable" band
- **Field preservation:** only `story` (+ `reflection` where noted) and `generation_metadata.style_normalization` changed; verified byte-identical on all other fields for a 12-story random sample against the archival snapshot
- **Archival snapshot:** `data/archive/stories_factchecked_v1/` (per-file) + `data/archive/stories_factchecked_v1.json` + `data/archive/full_fact_checks_v1.json` — the pre-normalization fact-checked state, preserved untouched

## Common style issues corrected

1. **Chain-dependent openings** — stories opened on references to prior episodes with no self-contained context. Fixed with 1–3 woven context sentences (343 stories). Highest-frequency fix in the pass.
2. **Unexplained named characters** — Balarama, Uddhava, Akrura, Rohini, Vidura, Dussasana, Satyaki etc. appearing without identification. Now introduced briefly at first mention (e.g., "Balarama, Krishna's elder brother"; "Uddhava, Krishna's close friend and adviser").
3. **Unglossed cultural/Sanskrit terms** — gopis, brahmanas, swayamvara, yojana, arghya, Rajasuya, Govinda, Vraja, Kshatriyas, asura, gurukula, tilak, etc. now explained naturally in-sentence or rendered plain (Vraja → Vrindavan, Govinda → "the protector of the cows", asura → demon).
4. **Translationese / scripture-register prose** — "behooves", "endued with", "forsooth", "O monarch", "thou/thee/ye", "illustrious sons of Pandu", epithet piles (Savyasachin, Janarddana) modernized to plain timeless voice. 15+ agents reported removing these.
5. **"The verses say / the text is blunt / the account does not linger" meta-commentary** — analyst framing stripped and converted into narration (reported across nearly every wave).
6. **Redundant restatement** — doubled similes, triple "one after another", repeated closers, duplicate openings/teasers merged.
7. **Trailer-style or moralizing endings** — foreshadow-moral tails, essay closes, "and thus humanity learned…" replaced with quiet still-scene endings.
8. **Over-theological register for Krishna** — "the omniscient Supreme Lord…" demoted to plain "Krishna" except where the moment genuinely calls for it.
9. **Inconsistent place/name forms** — Vraja/Gokula/Vrindavan, Yasoda/Yashoda, Dwaraka/Dwarka normalized within stories (prose level).

## Common AI patterns removed

- "the verses say / text says" attribution frames
- trailer foreshadowing ("what happened next would change everything", "belongs to the moment that follows")
- stacked "It was not X. It was Y." constructions (kept at most occasionally)
- rhetorical-question chains
- narrator verdicts and tell-don't-show commentary ("a line worth pausing over", "this was a touching moment")
- doubled dramatic-irony clichés ("The trap, had he known how to look for it, was already closing…")
- essay-style closers and moralizing codas
- epithet stacking and title pile-ups

## Child-friendly wording changes (representative)

- Violence softened without event removal: "vomiting blood" → restraint; "wolves living on fat, blood and flesh" → "dark-faced and fierce"; gore at temples removed; intoxication/nudity rendered with restraint + content notes retained.
- Adult/melodramatic imagery simplified for read-aloud (rasa-lila intimacy kept substance-faithful and non-graphic).
- Kinship and identity stated plainly (Dussasana = Duryodhana's younger brother; Pandavas = Krishna's cousins; Dhritarashtra's blindness at first mention).

## Stories where rewriting risked factual meaning (flagged)

461 of 537 report lines carry a `risk` note where wording brushed a factual edge. The notable classes, each resolved fact-preservingly:

- **Naming characters the source leaves unnamed** (Rukmini in HV accounts; "the girl" → named via corpus chain) — identity drawn from the canonical event DB, flagged.
- **Source-internal attribution disputes preserved, not "fixed"** (e.g., DKS_0088: the "rod of punishment" line kept in Indra's confession as fact-checked though BP assigns it to Krishna; DKS_0372's Draupadi-vs-Krishna embrace kept as corrected by the fact-check pass).
- **Epithet interpretations** (rāma-nātha = "husband of the goddess of fortune", not Balarama — corrected from a misreading during the pass and flagged; Shesha/Ananta name unification).
- **Violence softened** with the removed detail quoted in the risk line so reviewers can audit.
- **Cross-story sequencing tensions** left untouched (e.g., Nanda present vs departed at Mathura in adjacent stories) — noted as corpus-level issues for a later pass, not fixed in prose.
- One **pre-existing factual tension surfaced, not resolved**: DKS_0054's Dhenuka "feeding on deer" (VP) vs DKS_0053's "made men his food" (BP) — flagged in report for a fact-check look.

## Comparison / acceptance

- Per-story acceptance check (standalone readability, child-friendliness, fact preservation, AI-pattern scan) was performed by each editor agent before saving; all report lines record the result.
- Independent spot check by the orchestrator: field-preservation violations 0/12 random sample; all 537 files valid JSON; all carry `style_normalization: {pass: v1, model: deepseek-v4-flash}`.
- No new substantive narrative facts introduced (self-checked per story + sampled by orchestrator).

## Artifacts

- **Production dataset:** `data/stories.json` (537 stories, reassembled from `data/stories/` + `data/pilot_stories/`) — now the normalized production set
- **Per-story report lines:** `data/mining/style_report/n001..n090.jsonl` (537 lines)
- **Aggregated report data:** `data/style_report_data.json`
- **Archival snapshot (pre-normalization):** `data/archive/stories_factchecked_v1/` (+ `.json`, `full_fact_checks_v1.json`)

## Caveats

- The pass ran as ~90 parallel editor agents on flash; cross-story consistency (e.g., identical phrasing across two stories telling the same event) was reduced within batches but not globally deduplicated — a later corpus-wide repetition pass could catch residual echoes.
- `editorial_status` remains `unreviewed` for all stories (human review still pending — this pass did not review, it edited).
