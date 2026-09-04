# Editorial Review Dashboard — Daily Krishna Stories (Pilot)

A local, zero-dependency review tool for the 48 pilot stories.

## Run

```bash
cd ~/Documents/projects/indian_apps/dailyX/daily_krishna_stories/review_dashboard
python3 server.py          # default port 8199
# or: python3 server.py 9000
```

Open **http://localhost:8199** in any browser. (A server is usually already
running on :8199 from the build session.)

## What you can do

- **Progress bar** — live counts of Unreviewed / Approved / Needs Revision /
  Rejected across the 48 stories.
- **Story list** — ID, title, life stage, arc, primary source + reference,
  reading time, source-fidelity score, status. Filter by status / life stage /
  arc / primary source / theme; search by title, ID, or characters.
- **Reading screen** — the story as a reader would see it (title, prose,
  reflection, sources, tradition note, next-story tease), plus:
- **Source Evidence** (collapsible) — why the story was selected, canonical
  event id, exact references, variant notes, per-statement fact-check verdicts,
  and the source-fidelity score.
- **Review controls** — Approve / Needs Revision / Reject / Reset buttons and a
  free-form comment box. Status + comments persist to
  `data/pilot_review_state.json` (survives restarts and is machine-readable).

## Data wiring

| File | Contents |
|---|---|
| `data/pilot_stories.json` | the 48 story objects (schema v2.0) |
| `data/pilot_fact_checks.json` | per-story fact-check statements + fidelity scores |
| `data/pilot_story_selection.json` | why each story was chosen |
| `data/pilot_review_state.json` | your review statuses + comments (created on first save) |

Rebuild the assembled file after any story edit:

```bash
python3 scripts/assemble_pilot.py
```

## Layout / stack

Plain HTML/CSS/JS + Python stdlib `http.server` — no build step, no node_modules.
`server.py` serves the static files and two tiny JSON endpoints
(`GET/POST /api/review`). Replace or extend freely.
