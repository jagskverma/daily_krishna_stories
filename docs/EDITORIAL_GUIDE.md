# Editorial Guide — Daily Krishna Stories (Pilot)

This is the default editorial contract for writing pilot stories. Every rule here
is deliberate; apply them all. We will revise the contract later based on human
review — so the pilot is a *test of the voice*, not just of content.

## 1. Audience

General Indian adults and families who want Krishna's stories in an accessible
form, readable aloud to a 10–12 year old without feeling like a children's book.
Never write *for* children (no baby-talk, no simplification as a goal), never
write academic or dense theological prose. A parent should be able to read the
same page to a child naturally.

## 2. Length

600–900 words (reading 3–5 min). A naturally short event may be ~450 words; a
complex one may reach ~1,100. Never pad. One satisfying narrative episode per story.

## 3. Voice

Warm, elegant, vivid, restrained. Timeless, intimate, clear, visually evocative,
calm, narratively strong. Modern natural English. NOT textbook, NOT Wikipedia,
NOT sermon, NOT motivational, NOT cartoon, NOT TV-serial melodrama, NOT florid
pseudo-scriptural English ("Thereupon the Supreme Personality of Godhead gazed
upon the firmament" is banned). Prefer: "Krishna looked toward the darkening sky."

## 4. Devotional tone

Respectful and devotional without preaching. Krishna is not a mere fictional
character, but do not insert theological claims the source does not support.
Banned repetitions: "Lord Krishna, in his infinite mercy…", "As we all know…",
"This teaches us that…", "The divine Lord then…". Use "Krishna" naturally;
use honorifics only where appropriate. Let the events carry the devotion.

## 5. Source fidelity (CRITICAL)

Write ONLY from the evidence pack (`data/pilot_evidence/<DKS>.txt`): index entry,
canonical event, source excerpts, and the cited source passages. That is the
factual boundary. Do not import details from TV serials, Amar Chitra Katha,
modern retellings, internet folklore, or popular memory — unless independently
in the pack. If the pack's sources differ (see variant_notes), follow the
primary source and note the difference in `tradition_note` (never blend
incompatible versions into one seamless account).

## 6. Dialogue

Do not invent long cinematic dialogue. If the source has dialogue, paraphrase it
faithfully into natural English; use direct quotation sparingly. If the source
only says someone spoke/asked/responded, do not fabricate a dramatic
conversation. Minor connective narration is allowed; invented plot is not.

## 7. Context

Each story must work for someone who never read the previous one. Give only the
minimum context (e.g. "Krishna's uncle Kamsa had spent years trying to prevent
the prophecy that Devaki's child would cause his death"). Never re-explain the
whole biography.

## 8. Opening

First 1–3 sentences create curiosity: an unusual situation, an impending
conflict, a question, a visual moment, a striking decision. Banned openings:
"Once upon a time…", "In Hindu mythology…", "This is the story of…". No clickbait.

## 9. Structure

Opening (hook) → context (only what's needed) → development (choices change
something) → peak (central event/revelation/conflict) → resolution (consequence)
→ reflection (very brief, where appropriate). Never label these sections in the
prose; the story must flow naturally.

## 10. Endings

Do not end every story with a moral. Vary: emotional resolution / image /
consequence / revelation / transition to the next event / short philosophical
reflection / unanswered tension where historically appropriate. The ending
should feel earned.

## 11. reflection (separate field, NOT in prose)

1–3 sentences of thoughtful interpretation, not a command. Example: "Krishna's
question to Nanda is striking because he does not reject tradition casually; he
asks what purpose the ritual serves and whether the community understands why it
performs it." Banned: "Moral: we should always…". `null` is acceptable when the
story needs no reflection.

## 12. Title

3–8 words, concise, intriguing. Examples: "Krishna Questions Indra's Worship",
"The Night Krishna Was Born", "A Message for Rukmini", "When Sudama Came to
Dwaraka". Avoid "The Amazing Story of…", "Lord Krishna Teaches Us…", spoilers.
`subtitle` (optional) adds context when needed.

## 13. Sources

`"sources"` array: primary + additional, e.g. [{"work": "Bhagavata Purana",
"reference": "10.24.1–18", "role": "primary"}, …]. Shown in the dashboard/app,
never inside the prose.

## 14. tradition_note (optional)

A reader-facing note when a source variation matters, e.g. "The Harivamsha gives
a somewhat different emphasis to this episode." Keep it one or two sentences.

## 15. Names

Readable transliteration, no diacritics: Krishna, Arjuna, Yashoda, Dwaraka,
Vrindavan, Kamsa, Balarama, Rukmini, Draupadi. Consistent throughout (no mixing
Kṛṣṇa/Krishna, Dvārakā/Dwaraka). Follow the characters list in the evidence pack.

## 16. Violence

Do not sanitize events away, but describe violence with restraint ("Krishna
struck Kamsa down and ended his reign" — not graphic gore). Set `content_note`
when an episode may warrant parental awareness.

## 17. Audio suitability

Reads well aloud: avoid very long sentences, nested parentheses, excessive
Sanskrit terms, citations in prose; consistent names; punctuation that breathes.
Set `estimated_audio_minutes` (usually 3–5; ~150 words/min).

## 18. hero_scene + visual_elements

`hero_scene`: ONE concrete visual moment for the illustration (e.g. "Seven-year-
old Krishna holding Govardhan Hill effortlessly on one raised hand while
villagers, cattle and children shelter beneath it as rain lashes the landscape
outside."). `visual_elements`: list of characters, objects, location, weather,
action, mood. Do NOT generate images.

## 19. Continuity

`previous_story_id` / `next_story_id` come from the evidence pack's pilot chain.
`next_story_tease`: at most one sentence, only where a real continuation exists
(e.g. "But Indra was not ready to accept the villagers' decision."); `null`
otherwise.

## 20. Output

Write ONE JSON file per story: `data/pilot_stories/<id>.json`, exactly this shape:

```json
{
  "id": "DKS_0003",
  "title": "…",
  "subtitle": null,
  "story": "… (600-900 words, the full prose)",
  "reflection": "… or null",
  "tradition_note": null,
  "content_note": null,
  "estimated_read_minutes": 4,
  "estimated_audio_minutes": 4,
  "life_stage": "birth",
  "story_arc": "prophecy_of_kamsa",
  "characters": ["Kamsa", "Vasudeva", "Devaki"],
  "locations": ["Mathura"],
  "themes": ["prophecy", "fate"],
  "previous_story_id": null,
  "next_story_id": "DKS_0013",
  "next_story_tease": "… or null",
  "hero_scene": "…",
  "visual_elements": ["…"],
  "sources": [{"work": "Bhagavata Purana", "reference": "10.1.28-33", "role": "primary"}],
  "generation_metadata": {
    "corpus_version": "V1",
    "model": "deepseek-v4-flash",
    "generated_at": "<ISO date>",
    "source_event_id": "<canonical event id from the pack>"
  },
  "editorial_status": "unreviewed"
}
```

`sources[].work` uses the friendly work name (Bhagavata Purana / Vishnu Purana /
Harivamsha / Mahabharata); `reference` like "10.24.1-18" or "5.7" or
"1.113" (work-appropriate granularity, matching the pack). `role`: "primary" for
the first, "additional" for the rest.

## Quality bar

Before finishing a story, read it aloud mentally and check: does the opening
hook? Does it feel like one episode? Is every statement traceable to the pack?
Is the devotional weight carried by events, not adjectives? If a sentence could
have been written by Wikipedia, rewrite it.
