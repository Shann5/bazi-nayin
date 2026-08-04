# The Thirty Nayin (纳音) — English Translations & Dataset

The **nayin** (纳音, *nà yīn*, "received tones") are thirty poetic sound-images from
Chinese metaphysics. Each one covers two adjacent pairs of the sixty Jiazi (六十甲子)
stem-branch cycle and attaches an elemental image to them — not just *Metal*, but
*Gold in the Sea*; not just *Fire*, but *Thunderbolt Fire*.

English resources for BaZi (八字, Four Pillars of Destiny) are inconsistent about these
names — the same nayin gets rendered three or four different ways across sites, which
makes cross-referencing painful. This repo is a small, carefully considered set of
English translations, published as open data.

**Translation principles**

1. **Keep the image, not the word order.** 海中金 is "Gold in the Sea", not "Sea Middle Gold".
2. **Say *Gold* when the image is refined treasure, *Metal* when it is raw or forged** — 海中金 / 沙中金 are gold; 剑锋金 (sword-edge) stays metal.
3. **Use the established English term where one exists** (e.g. Milky Way for 天河), and plain concrete English elsewhere.

Full explanations of each image — what "Gold in the Sea" actually implies in a reading —
are on the reference page this dataset comes from:
**[The 30 Nayin, explained →](https://auspiceoracle.com/en/content/nayin)**

## The table

| Ganzhi pairs | 纳音 | Pinyin | English | Element |
|---|---|---|---|---|
| 甲子·乙丑 | 海中金 | *hǎi zhōng jīn* | Gold in the Sea | Metal |
| 丙寅·丁卯 | 炉中火 | *lú zhōng huǒ* | Fire in the Furnace | Fire |
| 戊辰·己巳 | 大林木 | *dà lín mù* | Great Forest Wood | Wood |
| 庚午·辛未 | 路旁土 | *lù páng tǔ* | Roadside Earth | Earth |
| 壬申·癸酉 | 剑锋金 | *jiàn fēng jīn* | Sword-Edge Metal | Metal |
| 甲戌·乙亥 | 山头火 | *shān tóu huǒ* | Hilltop Fire | Fire |
| 丙子·丁丑 | 涧下水 | *jiàn xià shuǐ* | Water in the Ravine | Water |
| 戊寅·己卯 | 城头土 | *chéng tóu tǔ* | City Wall Earth | Earth |
| 庚辰·辛巳 | 白蜡金 | *bái là jīn* | White Wax Metal | Metal |
| 壬午·癸未 | 杨柳木 | *yáng liǔ mù* | Willow Wood | Wood |
| 甲申·乙酉 | 泉中水 | *quán zhōng shuǐ* | Water in the Spring | Water |
| 丙戌·丁亥 | 屋上土 | *wū shàng tǔ* | Rooftop Earth | Earth |
| 戊子·己丑 | 霹雳火 | *pī lì huǒ* | Thunderbolt Fire | Fire |
| 庚寅·辛卯 | 松柏木 | *sōng bǎi mù* | Pine and Cypress Wood | Wood |
| 壬辰·癸巳 | 长流水 | *cháng liú shuǐ* | Long-Flowing Water | Water |
| 甲午·乙未 | 沙中金 | *shā zhōng jīn* | Gold in the Sand | Metal |
| 丙申·丁酉 | 山下火 | *shān xià huǒ* | Fire at the Foothill | Fire |
| 戊戌·己亥 | 平地木 | *píng dì mù* | Wood on Level Ground | Wood |
| 庚子·辛丑 | 壁上土 | *bì shàng tǔ* | Earth on the Wall | Earth |
| 壬寅·癸卯 | 金箔金 | *jīn bó jīn* | Gold Foil Metal | Metal |
| 甲辰·乙巳 | 覆灯火 | *fù dēng huǒ* | Sheltered Lamp Fire | Fire |
| 丙午·丁未 | 天河水 | *tiān hé shuǐ* | Water of the Milky Way | Water |
| 戊申·己酉 | 大驿土 | *dà yì tǔ* | Post-Road Earth | Earth |
| 庚戌·辛亥 | 钗钏金 | *chāi chuàn jīn* | Hairpin Metal | Metal |
| 壬子·癸丑 | 桑柘木 | *sāng zhè mù* | Mulberry Wood | Wood |
| 甲寅·乙卯 | 大溪水 | *dà xī shuǐ* | Water of the Great Stream | Water |
| 丙辰·丁巳 | 沙中土 | *shā zhōng tǔ* | Earth in the Sand | Earth |
| 戊午·己未 | 天上火 | *tiān shàng huǒ* | Fire in the Sky | Fire |
| 庚申·辛酉 | 石榴木 | *shí liú mù* | Pomegranate Wood | Wood |
| 壬戌·癸亥 | 大海水 | *dà hǎi shuǐ* | Water of the Great Sea | Water |

## Data

Machine-readable copies live in [`data/`](data/):

- [`nayin.json`](data/nayin.json) — array of 30 entries: `hanzi`, `pinyin`, `english`, `element`, `element_en`, `ganzhi` (the two stem-branch pairs), `ganzhi_pinyin`
- [`nayin.csv`](data/nayin.csv) — same data, one row per nayin

The ganzhi→nayin pairing follows the traditional sixty Jiazi order (甲子乙丑海中金 …
壬戌癸亥大海水), cross-checked against [lunar-typescript](https://github.com/6tail/lunar-typescript).

## Usage note: your input time is probably wrong

A nayin lookup keys off the stem-branch (ganzhi) pillars, and the pillars key off
the birth *time* — in solar time, not clock time. Clock time can be off by well
over an hour once you stack historical DST rules, longitude offset from the zone's
standard meridian (4 min/degree; Ürümqi runs ~2 h ahead of the sun), and the
equation of time (±16 min). Near a two-hour branch boundary that's the difference
between two different pillars, i.e. two different nayin.

The calculator this dataset comes from corrects for all three. How the correction
works, with a city-by-city table:
**[True solar time, explained →](https://auspiceoracle.com/en/content/true-solar-time)**

## License & attribution

Data and translations are **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**.
Use them freely — in apps, articles, datasets — with attribution to
[Auspice Oracle](https://auspiceoracle.com) (a link is enough).
