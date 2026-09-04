#!/usr/bin/env python3
"""Generate reports/MILESTONE_1_SUMMARY.md and reports/STORY_INDEX_REVIEW.md
from the final index + canonical event DB."""
import os, json
from collections import Counter

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
IDX = json.load(open(os.path.join(BASE, 'data/story_index.json')))
CANON = json.load(open(os.path.join(BASE, 'data/canonical_events.json')))
ARCS = json.load(open(os.path.join(BASE, 'data/story_arcs.json')))
stories = IDX['stories']
arc_name = {a['slug']: a['name'] for a in ARCS['arcs']}
arc_order = {a['slug']: a['order'] for a in ARCS['arcs']}

src_dist = Counter(s['primary_source']['work'] for s in stories)
stage_dist = Counter(s['life_stage'] for s in stories)
arc_dist = Counter(s['story_arc'] for s in stories)
conf_dist = Counter(s['source_confidence'] for s in stories)
multi = sum(1 for s in stories if s['additional_sources'])
variants = sum(1 for s in stories if s['variant_notes'])
sens = Counter(s['age_sensitivity'] for s in stories)
fest = Counter(t for s in stories for t in s['festival_tags'])
att = Counter()
for s in stories:
    att[s['primary_source']['work']] += 1
    for a in s['additional_sources']:
        att[a['work']] += 1

def pct(n, d): return f'{100.0*n/d:.1f}%' if d else '0%'
def emit(parts):
    return '\n'.join(p.rstrip('\n') for p in parts)

L = []
L.append('# Milestone 1 Summary — Daily Krishna Stories')
L.append('')
L.append('Generated: 2026-09-01 | Schema: story_index v1.0')
L.append('')
L.append('## Corpus')
L.append('- Sources downloaded: **7** (Tier A) + 2 Sanskrit reference layers; see `SOURCE_MANIFEST.md`')
L.append('- Raw files: Harivamsha (Gutenberg #61937), Mahabharata 18 parvas (Ganguli), Vishnu Purana (Wilson 1840 epub), Bhagavata Purana Sanskrit (GRETIL, 335 ch / 14,061 verses) + Dutt-OCR artifact (reference only)')
L.append(f'- Normalized corpus: {len(json.load(open(os.path.join(BASE,"sources/normalized/registry.json"))))} structural units in `sources/normalized/`')
L.append('')
L.append('## Index')
L.append(f'- **Stories indexed: {len(stories)}** (target 500+)')
L.append(f'- Raw events mined: {CANON.get("raw_count", "n/a")} -> canonical events after cross-source dedup: {CANON["count"]} -> index entries: {len(stories)}')
L.append(f'- Multi-source events: {multi} | Variant traditions flagged: {variants}')
L.append('')
L.append('### Stories by primary source')
for w, c in src_dist.most_common():
    L.append(f'- {w}: **{c}** ({pct(c, len(stories))})')
L.append('')
L.append('### Source attestations (primary + additional; one story may cite several sources)')
for w, c in att.most_common():
    L.append(f'- {w}: {c}')
L.append('')
L.append('### Stories by life stage')
for st in ['birth', 'gokul', 'vrindavan', 'mathura', 'dwaraka', 'pandava_period', 'kurukshetra', 'later_life', 'other']:
    c = stage_dist.get(st, 0)
    L.append(f'- {st}: **{c}** ({pct(c, len(stories))})')
L.append('')
L.append('### Stories by arc')
for slug, c in sorted(arc_dist.items(), key=lambda kv: arc_order.get(kv[0], 900)):
    L.append(f'- {arc_name.get(slug, slug)} (`{slug}`): **{c}**')
L.append('')
L.append('### Source-confidence distribution')
for v in sorted(conf_dist):
    L.append(f'- confidence {v}: {conf_dist[v]} ({pct(conf_dist[v], len(stories))})')
L.append('')
L.append('### Age sensitivity')
for v in sorted(sens):
    L.append(f'- {v}: {sens[v]}')
L.append('')
L.append('### Festival tags (top 10)')
for t, c in fest.most_common(10):
    L.append(f'- {t}: {c}')
L.append('')
L.append('## Corpus gaps & notes')
L.append('- Bhagavata Purana English: no clean public-domain English translation exists digitally. Canonical BP text is the GRETIL Sanskrit (verse-numbered); excerpts for BP-primary stories are freshly rendered from Sanskrit (own-translation policy, same as Daily Gita). The M.N. Dutt 1895-96 OCR (archive.org) is degraded/incomplete (Canto 10 missing Kaliya/Govardhan material) — kept as a reference artifact with confidence 1.')
L.append('- Bhagavata Cantos 3-6: no usable English edition; negligible Krishna narrative content (Kapila/Daksha/Dhruva/cosmology/Ajamila).')
L.append('- Mahabharata books 8-11 and 16-18 came from the KMGanguli compilation (same proofed sacred-texts text); books 1-7 and 12-15 from Gutenberg. Section numbering follows the edition; a handful of section headings are embedded in adjacent files (noted in individual records).')
L.append('- Harivamsha (Gutenberg #61937) is missing some chapter headings (e.g. LV, LXVIII, LXIX, LXXI); affected citations were re-anchored to the containing chapter with an explicit note and confidence 3.')
L.append('- Tier B (Garga Samhita, Brahma Vaivarta, Brahma Purana, Padma Purana): assessed; no clean public-domain English edition exists (Garga Samhita: none; Brahma Vaivarta: only a murky 1955 printing; Brahma Purana: only copyrighted Motilal translation; Padma Purana: none). Per the PD-only policy they were not acquired. Tier A produced 554 stories, so no Tier B expansion was required.')
L.append('- VP Book V contributed 85 mined events, most of which merged into BP/HV-led clusters (only 9 remain VP-primary) — its attestations are counted in the attestation table.')
L.append('')

open(os.path.join(BASE, 'reports/MILESTONE_1_SUMMARY.md'), 'w').write(emit(L))

# ---------------- STORY_INDEX_REVIEW.md ----------------
R = []
R.append('# Story Index Review — full list by arc (chronological)')
R.append('')
R.append(f'{len(stories)} stories - grouped by arc - for human review before story writing')
W = {'Srimad Bhagavata Purana (Sanskrit, GRETIL)': 'Bhagavata Purana',
     'Vishnu Purana (Wilson 1840)': 'Vishnu Purana',
     'Harivamsha (Dutt, Gutenberg #61937)': 'Harivamsha',
     'Mahabharata (Ganguli translation)': 'Mahabharata'}
cur = None
for s in stories:
    arc = s['story_arc']
    if arc != cur:
        cur = arc
        R.append('')
        R.append(f'## {arc_name.get(arc, arc)} ({arc})')
        R.append('')
    ps = s['primary_source']
    ref = f'{W.get(ps["work"], ps["work"])} {ps["book_or_canto"]}.{ps["chapter_or_section"]}'
    if ps.get('verse_range'):
        ref += f'.{ps["verse_range"]}'
    extra = f' +{len(s["additional_sources"])} more' if s['additional_sources'] else ''
    vn = f' - variant: {s["variant_notes"][:70]}' if s['variant_notes'] else ''
    R.append(f'{s["id"]} - {s["working_title"]}')
    R.append(f'{ref}{extra}{vn}')
    R.append(f'Arc: {arc_name.get(arc, arc)} | Strength: {s["estimated_story_strength"]}/5 | Visual: {s["visual_potential"]}/5')
    R.append('')
open(os.path.join(BASE, 'reports/STORY_INDEX_REVIEW.md'), 'w').write(emit(R))

print('reports written | summary', len(L), 'lines | review', len(R), 'lines')
