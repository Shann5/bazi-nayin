"""英文层。纳音译名以站内 lib/labels.ts NAYIN_EN 为唯一真源（这里是它的只读拷贝，同步时两边一起改）；
十二长生用语沿用 STAGE_EN 的锁定译名：死 = Stillness、墓/庫 = Storage、絶 = Void、敗 = Bath（沐浴），
不出 Death 裸词。原典字形是繁体，这里先映射到站内简体键。
"""

# 原典章名（繁）→ 站内 NAYIN_EN 键（简）
TO_SITE = {
    '海中金': '海中金', '金泊金': '金箔金', '白鑞金': '白蜡金', '砂中金': '沙中金', '劒鋒金': '剑锋金', '釵釧金': '钗钏金',
    '霹靂火': '霹雳火', '爐中火': '炉中火', '覆燈火': '覆灯火', '天上火': '天上火', '山下火': '山下火', '山頭火': '山头火',
    '桑柘木': '桑柘木', '松柏木': '松柏木', '大林木': '大林木', '楊柳木': '杨柳木', '石榴木': '石榴木', '平地木': '平地木',
    '壁上土': '壁上土', '城頭土': '城头土', '砂中土': '沙中土', '路傍土': '路旁土', '大驛土': '大驿土', '屋上土': '屋上土',
    '澗下水': '涧下水', '大溪水': '大溪水', '長流水': '长流水', '天河水': '天河水', '井泉水': '泉中水', '大海水': '大海水',
}

NAYIN_EN = {
    '海中金': 'Gold in the Sea', '炉中火': 'Fire in the Furnace', '大林木': 'Great Forest Wood',
    '路旁土': 'Roadside Earth', '剑锋金': 'Sword-Edge Metal', '山头火': 'Hilltop Fire',
    '涧下水': 'Water in the Ravine', '城头土': 'City Wall Earth', '白蜡金': 'Soft Wax Metal',
    '杨柳木': 'Willow Wood', '泉中水': 'Water in the Spring', '屋上土': 'Rooftop Earth',
    '霹雳火': 'Thunderbolt Fire', '松柏木': 'Pine and Cypress Wood', '长流水': 'Long-Flowing Water',
    '沙中金': 'Gold in the Sand', '山下火': 'Fire at the Foothill', '平地木': 'Tree on Open Ground',
    '壁上土': 'Earth on the Wall', '金箔金': 'Gold Foil Metal', '覆灯火': 'Sheltered Lamp Fire',
    '天河水': 'Water of the Milky Way', '大驿土': 'Great Road Earth', '钗钏金': 'Hairpin and Bracelet Metal',
    '桑柘木': 'Mulberry Wood', '大溪水': 'Water of the Great Stream', '沙中土': 'Earth in the Sand',
    '天上火': 'Fire in the Sky', '石榴木': 'Pomegranate Wood', '大海水': 'Water of the Great Sea',
}

ELEMENT_EN = {'金': 'Metal', '木': 'Wood', '水': 'Water', '火': 'Fire', '土': 'Earth'}


def name_en(trad: str) -> str:
    if len(trad) == 1:
        return 'any ' + ELEMENT_EN[trad]
    return NAYIN_EN[TO_SITE[trad]]


ARC_EN = {
    1: 'Conceived — held in the womb, roots not yet out',
    2: 'Opening — growing, buds splitting, about to stand',
    3: 'Flourishing — in bloom, the age of first standing and advancing',
    4: 'Revealed — fully formed; how a life has gone becomes visible',
    5: 'Gathering in — harvest taken, drawing inward into quiet',
    6: 'Closing — qi returns to the root; time to rest',
}

VERDICT_EN = {'+': 'welcomes', '-': 'avoids', '~': 'conditional', '0': 'no effect'}

IMAGE_EN = {
    '甲子': 'treasure', '乙丑': 'unworked ore', '丙寅': 'furnace coals', '丁卯': 'furnace smoke',
    '戊辰': 'wild mountain timber, not yet fit for use', '己巳': 'flowers and grasses on the hilltop',
    '庚午': 'dry earth by the road', '辛未': 'earth holding its yield, waiting for the autumn harvest',
    '壬申': 'halberds', '癸酉': 'hammers and chisels', '甲戌': 'where fire rests', '乙亥': 'the heat of a fire',
    '丙子': 'rivers and lakes', '丁丑': 'still, clear water that does not flow',
    '戊寅': 'embankments and city walls', '己卯': 'broken embankments, fallen walls',
    '庚辰': 'tin and pewter', '辛巳': 'living ore mixed with sand and stone',
    '壬午': 'willow trunk', '癸未': 'willow roots', '甲申': 'a sweet-water well', '乙酉': 'water in a shaded gully',
    '丙戌': 'mounded earth', '丁亥': 'open plain', '戊子': 'thunder', '己丑': 'lightning',
    '庚寅': 'pine and cypress trunks', '辛卯': 'pine and cypress roots', '壬辰': 'dragon water',
    '癸巳': 'water that never stops, flowing to the sea', '甲午': 'gold refined a hundred times',
    '乙未': 'metal left among furnace ashes', '丙申': 'wildfire through white grass',
    '丁酉': 'the echo of spirits; fire without form', '戊戌': 'withered mugwort', '己亥': 'mugwort shoots',
    '庚子': 'hollow earth: a house', '辛丑': 'a burial mound', '壬寅': 'ornamental metal',
    '癸卯': 'rings, buttons and bells', '甲辰': 'a lamp', '乙巳': "the lamp's light",
    '丙午': 'the disc of the moon', '丁未': 'light (as above)', '戊申': 'fields in autumn', '己酉': 'autumn crops',
    '庚戌': 'what remains of blades', '辛亥': 'bells, cauldrons and treasures',
    '壬子': 'wood harmed by too much water', '癸丑': 'wood harmed by too little water',
    '甲寅': 'rain', '乙卯': 'dew', '丙辰': 'embankment', '丁巳': 'marshy earth',
    '戊午': 'the disc of the sun', '己未': 'sunlight', '庚申': 'pomegranate flower', '辛酉': 'pomegranate seeds',
    '壬戌': 'the sea', '癸亥': 'a hundred rivers',
}

LIKES_EN = {
    '甲子': 'metal and wood in their strong places', '乙丑': 'fire, and southern days and hours',
    '丙寅': 'winter, and wood', '丁卯': 'the southeast, autumn and winter', '戊辰': 'water',
    '己巳': 'spring and autumn', '庚午': 'water, and spring', '辛未': 'autumn, and fire',
    '壬申': 'greatly: 子 午 卯 酉', '癸酉': 'wood, and 寅 卯', '甲戌': 'spring and summer',
    '乙亥': 'earth, and summer', '丙子': 'wood and earth', '丁丑': 'metal, and summer',
    '戊寅': 'wood and fire', '己卯': '申 酉, and fire', '庚辰': 'autumn, and a little wood',
    '辛巳': 'fire, and autumn', '壬午': 'spring and summer', '癸未': 'winter and water; spring also suits',
    '甲申': 'spring and summer', '乙酉': 'the east and south', '丙戌': 'spring, summer, and water',
    '丁亥': 'fire and wood', '戊子': 'water, spring and summer; with earth it becomes spirit',
    '己丑': 'water, spring and summer; with earth it dims', '庚寅': 'autumn and winter',
    '辛卯': 'water and earth; spring suits', '壬辰': 'thunder and lightning, spring and summer',
    '癸巳': '亥 子, where it transforms', '甲午': 'water, wood and earth', '乙未': 'great fire, and earth',
    '丙申': 'autumn, winter, and wood', '丁酉': '辰 戌 丑 未', '戊戌': 'fire, spring and summer',
    '己亥': 'water, spring and summer', '庚子': 'wood, and metal with wood', '辛丑': 'wood, fire and spring',
    '壬寅': 'wood, and a little fire', '癸卯': 'strong fire, and autumn', '甲辰': 'night and water; dislikes day',
    '乙巳': 'above all 申 酉 and autumn', '丙午': 'night and autumn, when water is strong', '丁未': '(as above)',
    '戊申': '申 酉, and fire', '己酉': '申 酉, and winter', '庚戌': 'a little fire, and wood',
    '辛亥': 'wood, fire and earth', '壬子': 'fire, earth and summer', '癸丑': 'metal, water and autumn',
    '甲寅': 'summer, and fire', '乙卯': 'water and fire', '丙辰': 'metal and wood', '丁巳': 'fire, and the northwest',
    '戊午': 'feared in summer, loved in winter; avoids 戊子 己丑 甲寅 乙卯',
    '己未': 'avoids night, and fears the same four', '庚申': 'summer; autumn and winter do not suit',
    '辛酉': 'autumn and summer', '壬戌': 'spring, summer, and wood', '癸亥': 'metal, earth and fire',
}

# 状态语：十二长生位用 STAGE_EN 锁定译名
STATE_EN = {
    '伏明之火': 'fire with its light hidden', '偏庫之火': 'fire in a side Storage', '偏庫之金': 'metal in a side Storage',
    '偏庫／臨官之水': 'water in a side Storage / water at Coming of Age', '兩土下木': 'wood beneath two earths',
    '厚徳之土': 'earth of deep virtue', '受傷之土': 'wounded earth', '土中之木': 'wood buried in earth',
    '堅成之金': 'hardened, finished metal', '天將之火': "the heavenly general's fire", '始生之土': 'newly born earth',
    '專位／偏庫之木': 'wood in its own seat / in a side Storage', '從革之金': 'metal that yields to reshaping',
    '柔和之木': 'soft, pliant wood', '歲寒之木': 'wood that holds through the cold of the year',
    '氣聚之金': 'metal with its qi gathered', '水中之火': 'fire within water', '流衍之水': 'spreading water',
    '福壯祿厚之土': 'earth of strong fortune and ample provision', '福聚之土': 'earth where fortune gathers',
    '福聚之水': 'water where fortune gathers', '臨官之土': 'earth at Coming of Age', '臨官之火': 'fire at Coming of Age',
    '臨官之金': 'metal at Coming of Age', '自庫之土': 'earth in its own Storage', '自庫之木': 'wood in its own Storage',
    '自庫之水': 'water in its own Storage', '自庫之火': 'fire in its own Storage', '自庫之金': 'metal in its own Storage',
    '自敗之土': 'earth at Bath', '自敗之水': 'water at Bath', '自敗之金': 'metal at Bath',
    '自旺／偏庫之火': 'fire at Prime / in a side Storage', '自死之土': 'earth at Stillness', '自生之木': 'wood at Birth',
    '自生之水': 'water at Birth', '自生之金': 'metal at Birth', '自病／自死之水': 'water at Weakening / at Stillness',
    '自病／自死之火': 'fire at Weakening / at Stillness', '自絶之土': 'earth at Void', '自絶之水': 'water at Void',
    '自絶／氣散之金': 'metal at Void / with its qi scattered', '自胎之金': 'metal at Conception',
    '赫曦之火': 'blazing fire', '近火之木': 'wood close to fire', '重阜之土': 'earth heaped in hills',
    '金居木上': 'metal sitting over wood', '銀漢之水': 'water of the Milky Way',
}
