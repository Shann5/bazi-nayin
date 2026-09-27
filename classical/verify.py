"""核对公开数据里的每句引文都逐字出自《三命通會》卷一（四庫本，維基文庫錄文）。

python3 verify.py   # 在 classical/ 目录下运行；数据在 ../data/v2/
归一：尅→克；干位上的「巳/已」→己、「已」→巳（四庫本常見混寫）。
"""
import json, re

STEMS = '甲乙丙丁戊己庚辛壬癸'


def norm(s):
    s = re.sub(r'[巳已](?=[丑卯巳未酉亥])', '己', s)
    s = re.sub(rf'(?<=[{STEMS}])已', '巳', s)
    return s.replace('尅', '克')


src = norm(open('sanming-tonghui-juan01.txt', encoding='utf-8').read())
p = json.load(open('../data/v2/pillars.json', encoding='utf-8'))
m = json.load(open('../data/v2/matrix.json', encoding='utf-8'))
chapters = p['nayin_chapters']
bad, n = [], 0
for r in p['ganzhi']:
    for q in r['relations']['quotes']:
        n += 1
        if q not in src: bad.append((r['ganzhi'], q))
for s, row in m['matrix'].items():
    for o, c in row.items():
        for q in c['quotes']:
            n += 1
            if q not in chapters[s]['quote'] or q not in src: bad.append((s, o, q))
print(f'checked {n} quotes; not found: {len(bad)}')
for b in bad: print('  ', b)
assert not bad
