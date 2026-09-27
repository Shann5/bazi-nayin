"""纳音 × 纳音矩阵：核对引文、展开五行泛指、输出 30×30。"""
import json, csv
from curated_matrix import M
import en

d = json.load(open('nayin-v2.raw.json', encoding='utf-8'))
CH = d['nayin_chapters']
NAMES = list(CH)                      # 原典章序：金六、火六、木六、土六、水六
EL = {n: n[-1] for n in NAMES}
errs, grid = [], {s: {} for s in NAMES}

for s, entries in M.items():
    if s not in CH: errs.append(('bad subject', s)); continue
    text = CH[s]['quote']
    for others, v, q in entries:
        if q not in text: errs.append(('quote not in chapter', s, q))
        if v not in '+-~0': errs.append(('bad verdict', s, v))
        for o in others.split():
            if len(o) == 1:
                continue
            if o not in CH: errs.append(('bad name', s, o)); continue
            cell = grid[s].setdefault(o, {'verdict': v, 'quotes': [], 'scope': 'named'})
            if cell['scope'] == 'named' and cell['quotes'] and cell['verdict'] != v:
                cell['verdict'] = '~'          # 同章两说不一，记为有条件
            cell['quotes'].append(q)
    # 五行泛指：只填原文没点名的格子
    for others, v, q in entries:
        for o in others.split():
            if len(o) == 1:
                for n in NAMES:
                    if EL[n] == o and n not in grid[s]:
                        grid[s][n] = {'verdict': v, 'quotes': [q], 'scope': 'element'}

print('errors:', errs or 'none')
print('subjects:', len([s for s in NAMES if grid[s]]), '/ 30')
filled = sum(len(r) for r in grid.values())
named = sum(1 for r in grid.values() for c in r.values() if c['scope'] == 'named')
print(f'cells: {filled} / 900 filled ({named} named, {filled - named} by element)')
from collections import Counter
print('verdicts:', Counter(c['verdict'] for r in grid.values() for c in r.values()))

# 不对称：A 喜 B 而 B 忌 A
asym = [(a, b) for a in NAMES for b in NAMES if a < b
        and {grid[a].get(b, {}).get('verdict'), grid[b].get(a, {}).get('verdict')} == {'+', '-'}]
print('asymmetric (+/-):', len(asym)); [print('  ', a, grid[a][b]['verdict'], b, '|', b, grid[b][a]['verdict'], a) for a, b in asym]

for s_ in NAMES:
    for o_, c_ in grid[s_].items():
        c_['verdict_en'] = en.VERDICT_EN[c_['verdict']]
json.dump({'source': d['source'], 'section': '卷一 三十章納音專論', 'order': NAMES,
           'names_en': {n: en.name_en(n) for n in NAMES}, 'verdicts_en': en.VERDICT_EN, 'matrix': grid},
          open('nayin-matrix.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open('nayin-matrix.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['主\\客'] + NAMES)
    for s in NAMES:
        w.writerow([s] + [(grid[s][o]['verdict'] + ('' if grid[s][o]['scope'] == 'named' else '*')) if o in grid[s] else '' for o in NAMES])

with open('nayin-matrix.en.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['subject \\ meets'] + [en.name_en(n) for n in NAMES])
    for s in NAMES:
        w.writerow([en.name_en(s)] + [(grid[s][o]['verdict'] + ('' if grid[s][o]['scope'] == 'named' else '*')) if o in grid[s] else '' for o in NAMES])
