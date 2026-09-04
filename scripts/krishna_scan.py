#!/usr/bin/env python3
"""Krishna-relevance scan: per-chapter density of Krishna-specific names across the
normalized corpus → selects narrative chapters for LLM mining. Output:
sources/normalized/krishna_chapters.json  [{work, book, chapter, section, title, krishna_hits, chars, select, reason}]
"""
import os, re, json, glob

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
NORM = os.path.join(BASE, 'sources/normalized')

# Strong Krishna-specific markers (avoid generic hari/vishnu/narayana which flood invocations)
MARKERS = re.compile(
    r'\b(krishna|kṛṣṇa|krsna|vasudeva|vāsudeva|janardana|janārdana|govinda|kesava|keśava|keshava|'
    r'madhava|mādhava|madhusudana|madhusūdana|hrisikesa|hṛṣīkeśa|hrishikesha|achyuta|acyuta|'
    r'gopala|gopāla|damodara|dāmodara|kamsa|kaṃsa|kansa|gokula|gokula|vrindavana|vṛndāvana|'
    r'vrindavan|mathura|mathurā|dwaraka|dvārakā|dwarka|devaki|devakī|yasoda|yaśodā|yashoda|'
    r'balarama|balarāma|baladeva|rukmini|rukmiṇī|syamantaka|syamanta|naraka|narakāsura|'
    r'putana|pūtanā|trinavarta|trṇāvarta|kaliya|kāliya|kāliyadaman|dhenuka|dhenukāsura|'
    r'gopi|gopīs?|gopis|gokul|nandagopa|akrura|akrūra|ugrasena|jarasandha|jarāsandha|'
    r'sisupala|śiśupāla|shishupala|satyabhama|satyabhāmā|samba|sāmba|aniruddha|pradyumna|'
    r'uddhava|sudama|sudāmā|kucela|draupadi|draupadī|pandavas|pāṇḍavas|gandhari|gāndhārī)\b',
    re.I)

def scan_file(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    hits = len(MARKERS.findall(txt))
    return hits, len(txt)

out = []

# ---- Bhagavata Sanskrit: curated — Canto 10 all, Canto 1 all, Canto 11 all, Canto 3 ch 2-4
for c in range(1, 13):
    for ch in range(1, 200):
        p = os.path.join(NORM, 'bhagavata_sanskrit', f'canto_{c:02d}', f'chapter_{ch:03d}.txt')
        if not os.path.exists(p):
            continue
        hits, chars = scan_file(p)
        curated = (c == 10) or (c == 1) or (c == 11) or (c == 3 and 2 <= ch <= 4)
        if curated or hits >= 8:
            out.append({'work': 'bhagavata_sanskrit', 'book': c, 'chapter': ch, 'section': None,
                        'krishna_hits': hits, 'chars': chars, 'select': True,
                        'reason': 'curated' if curated else 'density'})

# ---- Vishnu Purana: curated Book V all + density scan others
for b in range(1, 7):
    for ch in range(1, 100):
        p = os.path.join(NORM, 'vishnu_purana', f'book_{b:02d}', f'chapter_{ch:03d}.txt')
        if not os.path.exists(p):
            continue
        hits, chars = scan_file(p)
        curated = (b == 5)
        if curated or hits >= 10:
            out.append({'work': 'vishnu_purana', 'book': b, 'chapter': ch, 'section': None,
                        'krishna_hits': hits, 'chars': chars, 'select': True,
                        'reason': 'curated' if curated else 'density'})

# ---- Harivamsa
import glob as g
for part in [1, 2]:
    for p in sorted(g.glob(os.path.join(NORM, 'harivamsa', f'part_{part:02d}', 'chapter_*.txt'))):
        m = re.search(r'chapter_(\d+)', p)
        ch = int(m.group(1))
        txt = open(p, encoding='utf-8', errors='replace').read()
        title = re.search(r'TITLE: (.+)', txt)
        title = title.group(1) if title else ''
        hits, chars = scan_file(p)
        curated = re.search(r'(KANSA|KRISHNA|VASUDEVA|DEVAKI|NANDA|GOKULA|PUTANA|BALADEVA|RUKSHMIN|RUKMINI|ANIRUDDHA|YADAVA|VRINDAVANA|DWARAKA|JARASHANDHA|AKRURA|KALYA|KALIYA|PARIJATA|SALWA|SALVA|NARAKA|KAMSA|UGrasena)', title, re.I) and part == 1
        if curated or (part == 1 and hits >= 15):
            out.append({'work': 'harivamsa', 'book': part, 'chapter': ch, 'section': None,
                        'krishna_hits': hits, 'chars': chars, 'select': True,
                        'reason': 'curated-title' if curated else 'density', 'title': title})

# ---- Mahabharata: density scan all sections + curated ranges
CURATED_MB = {
    1: [ (173, 193), (200, 206), (214, 225) ],          # svayamvara/pandava meeting; khandava
    2: [ (18, 22), (29, 42), (60, 68) ],                # jarasandha; rajasuya/sisupala; draupadi
    3: [ (12, 13), (21, 23), (48, 50) ],                # krishna visits pandavas
    5: [ (81, 100), (120, 141) ],                       # peace mission; krishna-karna
    6: [ (23, 46) ],                                    # gita + vishvarupa
    7: [ (33, 35), (146, 147), (165, 194) ],            # abhimanyu; jayadratha; drona-vadha
    8: [ (60, 67), (88, 90) ],                          # karna death; krishna urging
    11: [ (11, 16), (25, 27) ],                         # gandhari curse
    14: [ (16, 20) ],                                   # anugita frame
    15: [ (16, 25) ],                                   # krishna visits hastinapura
    16: [(1, 8)],                                      # mausala (all)
}
for p in sorted(g.glob(os.path.join(NORM, 'mahabharata', 'parva_*', 'section_*.txt'))):
    m = re.search(r'parva_(\d+)/section_(\d+)', p)
    pv, sec = int(m.group(1)), int(m.group(2))
    hits, chars = scan_file(p)
    curated = False
    for lo, hi in CURATED_MB.get(pv, []):
        if lo <= sec <= hi:
            curated = True
            break
    if curated or hits >= 12:
        out.append({'work': 'mahabharata', 'book': pv, 'chapter': None, 'section': sec,
                    'krishna_hits': hits, 'chars': chars, 'select': True,
                    'reason': 'curated' if curated else 'density'})

with open(os.path.join(NORM, 'krishna_chapters.json'), 'w') as f:
    json.dump(out, f, indent=1)

from collections import Counter
print('total selected:', len(out))
print(Counter((x['work'], x['reason']) for x in out))
for w in ['bhagavata_sanskrit', 'vishnu_purana', 'harivamsa', 'mahabharata']:
    sel = [x for x in out if x['work'] == w]
    print(w, '->', len(sel))
