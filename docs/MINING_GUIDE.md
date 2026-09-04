# Mining guide — Krishna event extraction (Milestone 1)

You are a careful scholarly curator building a **canonical index of Krishna story
units** for a daily-story app. Your job: read the assigned source chapters and
extract every Krishna-related **narrative event** as a structured JSON record.
You do NOT write the final story prose. You only index events with verifiable
source references.

## What counts as a story unit

A unit must contain meaningful narrative movement: **setup → action/conflict/
discovery → outcome or transition**. A prayer or hymn with no narrative frame is
NOT a story by itself. A chapter describing Krishna's glories without events is
NOT a unit.

Major episodes should be decomposed into independently tellable beats. Example
(Govardhan episode): "Nanda prepares Indra worship" / "Krishna questions Nanda" /
"Krishna argues for Govardhan worship" / "villagers celebrate Govardhan" /
"Indra becomes furious" / "the storm attacks Vrindavan" / "Krishna lifts
Govardhan" / "life beneath Govardhan for seven days" / "Indra realizes his
error" / "Indra meets Krishna and asks forgiveness".

Do NOT inflate counts with arbitrary paragraph splits. A beat must be able to
sustain a 2–4 minute daily story on its own. As a rough guide, aim for
**1.5–3 units per narrative chapter**, fewer for discourse/prayer chapters
(some yield 0), more for episode-rich chapters (up to 4–5).

## Citation honesty (MANDATORY)

- **Never invent or guess verse/section numbers.** Cite only what you actually
  see in the text you read.
- If the source shows verse numbers (e.g. the Sanskrit Bhagavata files are
  numbered `1. … 2. …` per chapter), fill `verse_range` with the exact range,
  e.g. `"1-12"` or `"7"`.
- If the source only has chapter/section granularity, leave `verse_range` empty
  (`""`) and set `source_confidence` ≤ 4.
- `source_excerpt`: 1–3 sentences of evidence that the event exists. For English
  sources, quote verbatim (fix obvious OCR typos only, and note `[ocr-fixed]`).
  For the Sanskrit Bhagavata, render the key verse(s) into your own clear
  English and note `(rendered from Sanskrit, verse NN)`. Keep excerpts short.

## Output format

Write a JSONL file (one event per line) to the exact path given in your task.
Each record:

```json
{
  "event_id": "short_source_key_sequence_number, e.g. vp5_003_01",
  "title": "Short working title, e.g. 'Krishna Questions the Worship of Indra'",
  "one_line_summary": "One sentence: what happens, to whom, and the outcome.",
  "life_stage": "birth|gokul|vrindavan|mathura|dwaraka|pandava_period|kurukshetra|later_life|other",
  "story_arc": "One arc name from the canonical list below (choose closest).",
  "characters": ["Krishna", "Nanda", "Indra"],
  "locations": ["Vrindavan", "Govardhana hill"],
  "themes": ["devotion", "humility", "pride"],
  "primary_source": {
    "work": "exact work name, e.g. 'Srimad Bhagavata Purana (Sanskrit)'",
    "book_or_canto": "10",
    "chapter_or_section": "24",
    "verse_range": "1-25"
  },
  "additional_sources": [],
  "source_excerpt": "…",
  "variant_notes": "",
  "festival_tags": ["Govardhan Puja", "Janmashtami"],
  "age_sensitivity": "all|mild_violence|mature",
  "estimated_story_strength": 3,
  "visual_potential": 4,
  "independent_story_score": 3,
  "source_confidence": 5,
  "sequence_hint": 0,
  "notes": ""
}
```

## Field rules

- `life_stage`: birth | gokul | vrindavan | mathura | dwaraka | pandava_period |
  kurukshetra | later_life | other. (gokul = Nanda's village infancy;
  vrindavan = the forest/pasture years; later_life = post-war to departure.)
- `story_arc`: pick from the canonical arc list.
- Scores 1–5: `estimated_story_strength` = how good a daily story this would be
  (narrative arc, emotional resonance); `visual_potential` = how visual the
  scene is (art/daily-image potential); `independent_story_score` = how well it
  stands alone without context; `source_confidence` = citation reliability
  (5 = exact verse refs, 4 = chapter refs in a clean edition, ≤3 = OCR or
  rough refs).
- `sequence_hint`: order of this unit within its source (0,1,2,…) so we can
  rebuild chronology.
- `variant_notes`: only if you find a materially different version WITHIN your
  assigned chapters (different tradition retellings are merged later by another
  pass — do not try to dedupe across sources).
- `festival_tags`: only well-attested festivals (Janmashtami, Govardhan Puja,
  Holi, Diwali, Naga Panchami, Ratha Yatra, etc.) — do not invent.

## Canonical story arcs

prophecy_of_kamsa, birth_of_krishna, krishna_reaches_gokul, early_gokul_childhood,
vrindavan_childhood, kaliya_and_yamuna, govardhan_and_indra, rasa_and_gopis,
akrura_and_departure, mathura_and_kamsa, jarasandha_and_kings, dwaraka_founded,
rukmini_and_marriages, syamantaka_jewel, narakasura_and_gods, pandava_friendship,
rajasuya_and_sisupala, draupadi_honour, peace_mission, kurukshetra_war,
post_war_krishna, uddhava_and_teachings, end_of_yadavas, krishna_departure, other

## Hard rejections

Reject candidates that are: only generic Krishna trivia; an identical repeat of
another unit you already extracted; pure theology/discourse with no narrative;
events with no locatable source reference in your text.
