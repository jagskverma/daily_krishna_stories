#!/usr/bin/env python3
"""Compile the frozen editorial corpus into the compact Flutter asset."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = PROJECT_ROOT / "data"
OUTPUT_PATH = PROJECT_ROOT / "app" / "assets" / "data" / "stories.v1.json"

APP_STAGES = {
    "birth": "birth",
    "gokul": "gokul",
    "vrindavan": "vrindavan",
    "mathura": "mathura",
    "dwaraka": "dwarka",
    "pandava_period": "pandavas",
    "kurukshetra": "kurukshetra",
    "later_life": "laterLife",
}

ARTWORK_BY_STAGE = {
    "birth": "assets/artwork/birth.jpg",
    "gokul": "assets/artwork/butter.jpg",
    "vrindavan": "assets/artwork/kaliya.jpg",
    "mathura": "assets/artwork/govardhan.jpg",
    "dwarka": "assets/artwork/butter.jpg",
    "pandavas": "assets/artwork/kaliya.jpg",
    "kurukshetra": "assets/artwork/govardhan.jpg",
    "laterLife": "assets/artwork/birth.jpg",
}


def read_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalized_stage(raw_stage: str, arc_stage: str) -> str:
    # The corpus has 19 deliberately broad "other" classifications. Sixteen
    # already belong to a chronological arc; the final three frame stories are
    # presented at the end of Later Life so the product keeps its eight-stage
    # journey without losing any catalogue entries.
    source_stage = arc_stage if raw_stage == "other" else raw_stage
    if source_stage == "other":
        source_stage = "later_life"
    try:
        return APP_STAGES[source_stage]
    except KeyError as error:
        raise ValueError(f"Unsupported life stage: {source_stage}") from error


def paragraphs(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", value) if part.strip()]


def compile_corpus() -> dict:
    corpus = read_json(DATA_ROOT / "stories.json")
    index = read_json(DATA_ROOT / "story_index.json")
    arc_data = read_json(DATA_ROOT / "story_arcs.json")

    stories_by_id = {story["id"]: story for story in corpus["stories"]}
    index_by_id = {story["id"]: story for story in index["stories"]}
    arcs_by_id = {arc["slug"]: arc for arc in arc_data["arcs"]}

    expected_count = corpus["story_count"]
    if expected_count != 537 or index["story_count"] != expected_count:
        raise ValueError("Expected the frozen 537-story V1 corpus")
    if len(stories_by_id) != expected_count or len(index_by_id) != expected_count:
        raise ValueError("Story IDs must be unique in both source files")
    if stories_by_id.keys() != index_by_id.keys():
        raise ValueError("stories.json and story_index.json IDs do not match")

    ordered_index = sorted(index["stories"], key=lambda item: item["chronological_order"])
    orders = [item["chronological_order"] for item in ordered_index]
    if orders != list(range(1, expected_count + 1)):
        raise ValueError("Chronological order must be continuous from 1 to 537")

    compiled_stories = []
    for index_story in ordered_index:
        story = stories_by_id[index_story["id"]]
        arc = arcs_by_id.get(story["story_arc"])
        if arc is None:
            raise ValueError(f"Unknown story arc for {story['id']}: {story['story_arc']}")

        body = paragraphs(story["story"])
        sources = [
            {
                "work": source["work"],
                "reference": source["reference"],
                "role": source.get("role", "supporting"),
            }
            for source in story["sources"]
        ]
        if not story["title"].strip() or not body or not story["reflection"].strip():
            raise ValueError(f"Incomplete required content for {story['id']}")
        if not sources:
            raise ValueError(f"Missing source references for {story['id']}")
        if sum(source["role"] == "primary" for source in sources) != 1:
            raise ValueError(f"Expected one primary source for {story['id']}")

        stage = normalized_stage(story["life_stage"], arc["life_stage"])
        compiled_stories.append(
            {
                "id": story["id"],
                "content": {
                    "en": {
                        "title": story["title"].strip(),
                        "subtitle": (story.get("subtitle") or "").strip(),
                        "summary": index_story["one_line_summary"].strip(),
                        "body": body,
                        "reflection": story["reflection"].strip(),
                        "traditionNote": story.get("tradition_note"),
                    }
                },
                "illustration": ARTWORK_BY_STAGE[stage],
                "lifeStage": stage,
                "storyArc": story["story_arc"],
                "storyArcTitle": index_story["story_arc_name"],
                "characters": story["characters"],
                "themes": story["themes"],
                "locations": story["locations"],
                "sources": sources,
                "contentNote": story.get("content_note"),
                "heroScene": story["hero_scene"].strip(),
                "visualElements": story["visual_elements"],
                "nextStoryTease": story.get("next_story_tease"),
                "readTimeMinutes": story["estimated_read_minutes"],
                "estimatedAudioMinutes": story["estimated_audio_minutes"],
                "chronologicalOrder": index_story["chronological_order"],
                "festivalTags": index_story["festival_tags"],
                "ageSensitivity": index_story["age_sensitivity"],
                "editorialStatus": story["editorial_status"],
            }
        )

    compiled_arcs = [
        {
            "id": arc["slug"],
            "title": arc["name"],
            "order": arc["order"],
            "summary": arc["summary"],
        }
        for arc in sorted(arc_data["arcs"], key=lambda item: item["order"])
    ]

    return {
        "schemaVersion": 1,
        "corpusVersion": "V1",
        "storyCount": len(compiled_stories),
        "arcs": compiled_arcs,
        "stories": compiled_stories,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when the checked-in Flutter asset is missing or stale.",
    )
    args = parser.parse_args()

    payload = json.dumps(
        compile_corpus(), ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8") + b"\n"

    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_bytes() != payload:
            raise SystemExit("Flutter corpus asset is stale; run export_app_corpus.py")
        print(f"PASS: {OUTPUT_PATH} is current ({len(payload):,} bytes)")
        return

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(payload)
    print(f"Wrote {OUTPUT_PATH} ({len(payload):,} bytes, 537 stories)")


if __name__ == "__main__":
    main()
