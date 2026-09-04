# Full-corpus writer instructions (489 stories)

Same editorial contract as the pilot. Read `docs/EDITORIAL_GUIDE.md` fully first
and follow every rule (voice, 600–900 words, ~450 floor for short events, source
fidelity, reflection, titles, hero_scene, schema §20).

Differences from the pilot run:

- **Evidence packs** live at `data/evidence_full/<id>.txt` (same structure as the
  pilot packs; passage excerpts are longer, so you have more source to work with).
- **Output**: write each story to `data/stories/<id>.json` (NOT
  data/pilot_stories/). Create the directory if needed.
- **Schema**: identical to guide §20. `generation_metadata.corpus_version` =
  `"V1"`, `editorial_status` = `"unreviewed"`.
- **Chain**: the pack's `## Corpus chain` section gives `previous_story_id` /
  `next_story_id` across the whole corpus — use them. `next_story_tease`: one
  sentence only when there is a real continuation (the chain's next story);
  `null` otherwise.
- **Pilot overlap**: if a pack contains the note "this story already exists in
  the pilot" — skip it; you will not be assigned those.
- Write one file per story with `write_file`. After all stories: reply with the
  ids and word counts, plus any fidelity doubts (what you had to leave out
  because the pack didn't support it).
