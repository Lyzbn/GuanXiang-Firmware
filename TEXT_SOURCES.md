# 观象文本来源 · Text sources

核对于 2026-10-16。本说明对应深化精意与六十四卦自学候选，应用源码 `ae85426`（文字数据与旧 `38f2db6` 完全一致）；设备验收及安装资产状态另见 [VALIDATION.md](VALIDATION.md)。

**观象今释是本项目依据古典原文和注疏、借助 AI 辅助编写并复核的现代阅读文字，不是王弼、孔颖达、朱熹或现代学者的现成白话译文。** 经传原文、古注节选、项目今释和延伸阅读书目分别标明，不将来源引用或书目推荐作为作者、出版社或机构对本产品的背书。

## 可核验的数据

- [readings.json](readings.json)：64 卦各两行四字短意；每卦按「卦势、义理、处事、辨误」组织的精意；384 爻与用九、用六共 386 份「释义、精意」；所据古注节选及逐条来源。
- [study-content.json](study-content.json)：12 张基础课程的正文、卦画参数与出处，另含 64 卦的完整卦辞、大象和逐条来源。图形 `bit0` 为底爻，阳为 1、阴为 0，`line_count` 区分一画、三画与六画。

上述是公开阅读文字和来源记录，不含应用源码、构建对象、原始网页全文缓存或设备数据。数据中的 `\f` 是分节换页标记，不属于古文。

`readings.json` 的 `sources` 与 `short_basis_notes` 保留短意的来源及取义说明；新版精意另以 `deep_sources`、`deep_sections`、`annotation_excerpt`、逐爻 `anchor` 和 `special` 记录。`insight` 是用于分页显示的组合文字，古注节选和今释在其中分别标识。不要把短意引用朱熹的记录当成新版精意也采用同一解释的证据。

每条来源提供标题、URL、revision ID 和原始 wikitext 的 SHA-256。该摘要标识当时取得的源转录，不是网页 HTML 或项目今释。450 处核验锚点在固定版本来源中命中；这证明所引原句存在，不等于项目每一句现代引申都是古注的主张，也不等于全部转录已据古籍扫描本逐字校勘。

## 经传原文与古注

- **经传原文**：中文维基文库[《周易》](https://zh.wikisource.org/wiki/周易)逐卦转录。设备保留 64 条完整卦辞、64 条大象、384 条爻辞与 384 条小象，另有用九、用六及对应小象；「全句」指这些所收内容不作截短，不表示收入全部《易传》。展示使用简体转录，整理空白和版面注记；履、否、同人、坎保留完整开头，剥卦据《正义》校为「不利有攸往」。
- **深化精意的古注主轴**：王弼注、孔颖达疏[《周易正义》](https://zh.wikisource.org/w/index.php?title=周易正義&oldid=1645137)。设备将古注节选单列；若节选属于经文或传文，则以「经传·节选」区别。逐卦版本以 `deep_sources` 为准。此书整部书目包括王弼、韩康伯注与孔颖达等疏，本次卦爻解释所引为王弼、孔颖达相关段落。网上转录不称「国家图书馆校定本」。
- **短意的补充取义**：朱熹《原本周易本义（四库全书本）》[卷一，revision 736571](https://zh.wikisource.org/w/index.php?title=原本周易本義_(四庫全書本)/卷01&oldid=736571)、[卷二，revision 736575](https://zh.wikisource.org/w/index.php?title=原本周易本義_(四庫全書本)/卷02&oldid=736575)、[卷五，revision 527365](https://zh.wikisource.org/w/index.php?title=原本周易本義_(四庫全書本)/卷05&oldid=527365)。谦、蛊、贲、复、无妄、革的具体取义及注家差异见相应短意记录。深化精意独立遵从所列王孔解释，不把不同注家拼成一种说法。

## 八卦课程与口诀

课程按「识阴阳与八卦 → 上下卦叠六爻 → 读六十四卦」展开。传统口诀的古典见证为[《日讲易经解义》卷首，revision 2092864](https://zh.wikisource.org/w/index.php?title=日講易經解義_(四庫全書本)&oldid=2092864)，清本「盌」规范为「碗」。口诀教学采用乾坤、震艮、离坎、兑巽四组，不将该顺序说成先天或后天方位。

清华大学出版社[《毓老师讲易经①：乾坤卦》书样](https://www.tup.tsinghua.edu.cn/upload/books/yz/073777-01.pdf)印刷第 1 页提供通行作者归属的旁证；本项目未独立确认最早版本的著作归属，界面仅称「传统八卦取象歌」，不称其为《说卦》原文。卦德、自然象取自《说卦》，叠卦及爻位参考《周易本义》；固定版本详见课程数据。

## 延伸阅读与许可边界

国家新闻出版署[首批向全国推荐经典古籍及其整理版本名单](https://www.nppa.gov.cn/xxfb/tzgs/202103/P020221129375889315470.pdf)列有黄寿祺、张善文《周易译注》及王弼撰、楼宇烈校释《周易注校释》。傅佩荣《周易哲学》有[台大开放课程入口](https://ocw.aca.ntu.edu.tw/courses/103S201)。这些是延伸阅读建议，不是内置今释的作者署名、译文转载许可或产品认可；本项目没有整套复制这些现代译注或课程讲义。

古典作品本身属于公有领域；维基文库贡献者的转录与现代编辑层应另按其适用条款处理，页面载有 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)。本项目保留古典作者、转录来源、版本和变更说明，不把古籍公版状态扩大为现代译注可任意转载。本轮未确认一套可明确再分发、覆盖 64 卦的现成现代权威译文，因此采用明确署为项目整理的今释。公开这两份阅读数据不改变私有应用源码的访问或许可状态。

## English

This candidate distinguishes **canonical text**, **classical commentary excerpts**, **GuanXiang’s modern interpretations**, and **further-reading recommendations**. Modern text was prepared by the project with AI assistance and checked against the cited classical material. It is not an existing translation by Wang Bi, Kong Yingda, Zhu Xi or a modern scholar, nor an endorsement by the cited authors or institutions.

[readings.json](readings.json) provides 64 short summaries and four-part expanded hexagram readings, plus 386 individual readings for the 384 lines and the two special Use texts. Each individual reading separates explanation of the commentary from present-day reflections. The new expanded readings primarily follow Wang Bi and Kong Yingda’s *Zhouyi Zhengyi*. Earlier short-note sources, including specified passages from Zhu Xi, remain separately recorded.

[study-content.json](study-content.json) provides twelve foundation lessons, diagram parameters, source records, and the 64 complete judgments and Great Images. The firmware additionally retains the 384 complete line texts and Small Images and the special texts for Qian and Kun. This is not the complete Ten Wings. The traditional trigram mnemonic is attested in the cited *Rijiang Yijing Jieyi*; earliest authorship has not been independently established. The four mnemonic pairs are a teaching order, not a spatial trigram arrangement.

Revision IDs and source-wikitext hashes identify the cited transcriptions; the 450 matching anchors establish that the quotations exist in those versions. They do not make modern applications statements by the classical authors, or certify a full collation against manuscript scans. Ancient works are public domain; modern transcription/editorial rights and Wikisource terms remain distinct. Recommended modern books and the NTU course are not copied wholesale or treated as licensed translations for redistribution. The public files contain reading content and provenance, not private application source, complete source-page caches or device data.

## 数据校验 · Dataset verification

The following SHA-256 values identify the public data files originally exported from `38f2db6040246967c6b827f2c809dde6f2cad725` and verified byte-identical to current application source `ae85426a6943abf851704dd74d2dc820eb4ae4c6`. They are data digests, not firmware or release-archive digests.

| File | SHA-256 |
| --- | --- |
| `readings.json` | `a496696aa9718e163455f63bdb0f6f5dc722a18b72fd5cf0029c91ca11538c07` |
| `study-content.json` | `65aba460f7c70c073b5593b474acc9f9738892a15faf1d1af3be345ecd9bed76` |
