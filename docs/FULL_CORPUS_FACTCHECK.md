# Full-corpus fact-check instructions (489 stories)

You are the FACT-CHECK pass. Generation and validation are deliberately
SEPARATE — you did not write these stories and must verify them independently
against the source evidence.

For EACH story id in your group:

1. Read the story at `data/stories/<id>.json`
2. Read its evidence pack at `data/evidence_full/<id>.txt`
   (index entry + canonical event + verbatim source excerpts + source passages)
3. Read the full story prose. Evaluate every potentially factual statement
   (events, named characters, places, numbers, cause-effect, dialogue claims,
   outcomes). For each notable claim assign EXACTLY one verdict:
   - **SUPPORTED**: the pack's sources support it
   - **REASONABLE_CONNECTIVE_NARRATION**: minor connective tissue (atmosphere,
     non-factual framing, generic description) that does not assert a
     sourceable fact
   - **UNSUPPORTED**: a factual claim with no support in the pack
   - **CONTRADICTED**: the pack says something different
   Do NOT nitpick style. Do NOT require citations for obvious atmosphere.
   Where the pack's own summary and its passage disagree, note it but treat the
   passage as authoritative unless the summary is clearly the intended reading.

Output: append ONE JSON line per story to
`data/mining/factcheck_full/group_<NN>.jsonl` (create the dir) via execute_code:

```json
{"story_id": "DKS_XXXX",
 "statements": [{"claim": "...", "verdict": "...", "evidence": "..."}],
 "corrections": [{"original_sentence": "exact sentence from the story (UNSUPPORTED/CONTRADICTED only)", "suggested": "corrected sentence grounded in the pack"}],
 "source_fidelity_score": N,
 "notes": ""}
```

`source_fidelity_score`: 5 = no UNSUPPORTED/CONTRADICTED; 4 = only
connective-narration questions; <=3 = any UNSUPPORTED/CONTRADICTED.
Corrections must quote the story's exact sentence so a script can find/replace.

Reply briefly: per story, score + count of UNSUPPORTED/CONTRADICTED.
