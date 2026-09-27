"""三命通會 卷一 → nayin v2 (60 干支 + 30 纳音) 原文抽取。

只做「切段 + 定位 + 正则抽干支」，不做译解。所有自动抽出的关系都带 quote，供人工复核。
"""
import json, re

STEMS = '甲乙丙丁戊己庚辛壬癸'
BRANCHES = '子丑寅卯辰巳午未申酉戌亥'
SIXTY = [STEMS[i % 10] + BRANCHES[i % 12] for i in range(60)]
GZ = f'[{STEMS}][{BRANCHES}]'
ELEM = '金木水火土'

raw = open('../sanming-tonghui-juan01.txt', encoding='utf-8').read().splitlines()


def norm(s: str) -> str:
    """四库本常以「巳/已」代「己」、以「已」代「巳」：只在干支位置上纠正。"""
    s = re.sub(r'[巳已](?=[丑卯巳未酉亥])', '己', s)  # 己 只配阴支
    s = re.sub(rf'(?<=[{STEMS}])已', '巳', s)
    s = s.replace('尅', '克')
    return s


def strip_wiki(s: str) -> str:
    return re.sub(r'\{\{SK anchor\|[^}]*\}\}', '', s).strip('　 ')


# ---------- 纳音名：从 30 章标题取（原文字形） ----------
NAYIN = {}  # 干支 → 纳音
chapters = {}
for i, line in enumerate(raw):
    m = re.search(r'\{\{SK anchor\|(' + GZ + GZ + r')(..[金木水火土])\}\}', norm(line))
    if m and i > 130:
        pair, name = m.group(1), m.group(2)
        body = norm(raw[i + 1]).strip('　 ')
        chapters[name] = {'ganzhi': [pair[:2], pair[2:]], 'quote': body}
        NAYIN[pair[:2]] = NAYIN[pair[2:]] = name
assert len(chapters) == 30, len(chapters)

# ---------- 层 1：論納音取象 · 六段气象（按地支对） ----------
ARC = [
    ('子丑', '陰陽始孕', '人在胞胎物藏荄根未有涯際'),
    ('寅卯', '陰陽漸闢', '人漸生長物以拆甲羣葩漸剖如人將有立身也'),
    ('辰巳', '陰陽氣盛', '物當華秀如人三十四十而有立身之地始有進取之象'),
    ('午未', '陰陽彰露', '物己成齊人至五十六十富貴貧賤可知凡百興衰可見'),
    ('申酉', '陰陽肅殺', '物已收成人已龜縮各得其靜矣'),
    ('戌亥', '陰陽閉塞', '物氣歸根人當休息各有歸著'),
]
arc_text = norm(raw[30] if '論納音取象' in raw[29] else '')
qu_line = next(l for l in raw if '甲子納音象聖人喩之' in l)
for pair, head, tail in ARC:
    assert head in qu_line and tail[:6] in qu_line, (pair, head)


def arc_for(gz):
    for idx, (pair, head, tail) in enumerate(ARC):
        if gz[1] in pair:
            return {'stage': idx + 1, 'branch_pair': pair, 'quote': head + tail}


# ---------- 层 2a：釋六十甲子性質吉凶 · 小注 ----------
start = next(i for i, l in enumerate(raw) if '釋六十甲子性質吉凶' in l)
end = next(i for i, l in enumerate(raw) if i > start and l.lstrip('　').startswith('右件六十甲子'))
block = norm(''.join(raw[start + 1:end]))
notes = {}
for m in re.finditer(r'(' + GZ + r')[金木水火土](?:\}\})?\{\{SK notes\|([^}]*)\}\}', block):
    notes[m.group(1)] = m.group(2)
missing = [g for g in SIXTY if g not in notes]
assert not missing, missing

# 小注 = 象 + 喜忌 + 神煞/字形标签。标签词表用于截断，保留原文于 note_raw。
TAGS = ['破祿', '正祿', '福星', '華葢', '正印', '天乙', '天徳', '徳合', '官貴', '貴人', '喜神', '福神', '進神', '退神',
        '伏神', '交神', '祿', '伏馬', '建祿', '羊刃', '飛刃', '截路', '棒杖', '杖刑', '相刑', '平頭',
        '聾啞', '懸針', '破字', '闕字', '曲脚', '八専', '八專', '大敗', '妨害', '九醜', '短夭', '短天', '刑']


def split_note(n):
    cut = len(n)
    for t in TAGS:
        k = n.find(t)
        if k > 0:
            cut = min(cut, k)
    core = n[:cut]
    m = re.search(r'[大尤]?喜|忌|夏則|惡', core)
    image = core[:m.start()] if m else core
    likes = core[m.start():] if m else ''
    image = re.sub(r'^為', '', image)
    return image, likes


# ---------- 层 2b：盛大 / 小弱 规则 ----------
rule_line = norm(raw[end]).strip('　 ')
SCALE = {
    'large': ['松柏木', '大林木', '天上火', '劒鋒金', '大海水', '大驛土'],
    'small': ['楊柳木', '石榴木', '覆燈火', '金泊金', '井泉水', '砂中土'],
}
# 原文「柘榴木」「沙中土」与章名「石榴木」「砂中土」异写，核对时按原文字面
for w in ['松柏', '楊柳', '柘榴木', '大林木', '天上火', '劒鋒金', '大海水', '大驛土', '覆燈火', '金泊金', '井泉水', '沙中土']:
    assert w in rule_line, w

# ---------- 层 2c：逐干支段落 ----------
para_lines = []
i = end + 1
while '{{SK anchor|甲子乙丑海中金}}' not in raw[i]:
    para_lines.append(norm(raw[i]).strip('　 '))
    i += 1
paras = '\n'.join(para_lines)
# 段首：干支 + ≤6 字 + 之金/木… 或 干支 + 為…之X
heads = list(re.finditer(r'(' + GZ + r')(?:[^\n之]{0,6})之[金木水火土]', paras))
seg = {}
for k, m in enumerate(heads):
    gz = m.group(1)
    if gz in seg:
        continue
    stop = heads[k + 1].start() if k + 1 < len(heads) else len(paras)
    # 同一段内合写的两柱（丙申…丁酉…）各自截到下一个段首
    text = paras[m.start():stop].split('\n')[0]
    seg[gz] = {'label': m.group(0)[2:], 'quote': text}

# 自动抽关系：忌/嫌/畏/愛/喜/得 + 连续干支
REL = {'avoid': '忌|嫌|畏|惟畏|惟嫌', 'welcome': '愛|喜|貴得|藉|得'}


def rel_from(text):
    out = {'avoid': [], 'welcome': [], 'unharmed_by': []}
    for kind, verbs in REL.items():
        for m in re.finditer(rf'(?:{verbs})((?:{GZ}){{1,6}})', text):
            gzs = re.findall(GZ, m.group(1))
            out[kind] += [g for g in gzs if g in SIXTY]
    for m in re.finditer(r'([金木水火土衆他凡])[金木水火土]?(?:不能克|無傷)|不(?:忌|嫌|畏|怕)衆?([金木水火土])', text):
        e = m.group(1) or m.group(2)
        if e and e in ELEM:
            out['unharmed_by'].append(e)
    return {k: sorted(set(v), key=SIXTY.index) if k != 'unharmed_by' else sorted(set(v)) for k, v in out.items()}


rows = []
for gz in SIXTY:
    image, likes = split_note(notes[gz])
    s = seg.get(gz)
    rows.append({
        'ganzhi': gz,
        'nayin': NAYIN[gz],
        'nayin_element': NAYIN[gz][-1],
        'scale': next((k for k, v in SCALE.items() if NAYIN[gz] in v), None),
        'arc': arc_for(gz),
        'image': image,
        'likes': likes,
        'note_raw': notes[gz],
        'state_label': s['label'] if s else None,
        'paragraph': s['quote'] if s else None,
        'relations_auto': rel_from(s['quote']) if s else None,
    })

out = {
    'source': '三命通會 卷一（四庫全書本，維基文庫）https://zh.wikisource.org/wiki/三命通會_(四庫全書本)/卷01',
    'sections': {
        'arc': '論納音取象', 'notes': '釋六十甲子性質吉凶', 'scale_rule': '釋六十甲子性質吉凶·右件六十甲子',
        'chapters': '甲子乙丑海中金…壬戌癸亥大海水（三十章）',
    },
    'scale_rule_quote': rule_line,
    'ganzhi': rows,
    'nayin_chapters': chapters,
}
json.dump(out, open('nayin-v2.raw.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('rows', len(rows), 'with paragraph', sum(1 for r in rows if r['paragraph']))
print('no paragraph:', [r['ganzhi'] for r in rows if not r['paragraph']])
