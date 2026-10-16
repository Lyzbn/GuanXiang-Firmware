# 观象文本来源 · Text sources

核对于 2026-10-16。三档阅读分别为古文全句、现代短意、现代精意。

**现代短意与精意是本项目据原典整理的现代阅读文字，由 AI 辅助编写并逐条交叉核对；不是孔颖达、朱熹或现代学者的现成白话译文。** 短意每卦两行、每行四字；精意每卦 79–94 个汉字。它们解释卦象与古义，并提出适合现代生活的思考，不是逐字翻译。

全部 64 卦现代文字及逐条依据公开在 [readings.json](readings.json)。每条列出卦序、卦名、短意、精意、来源页面、revision ID、原始 wikitext 的 SHA-256，以及 `basis_notes` 整理说明。SHA-256 对应抓取时的原始页面文本，不是网页 HTML 或改写后的现代文字。

## 古文与注疏

- 古文来自中文维基文库[《周易》](https://zh.wikisource.org/wiki/周易)。固件保存 64 条完整卦辞、384 条爻辞、384 条对应小象，另有乾的用九、坤的用六及各自小象。「全句」表示这些内容不作节选，并不表示包含整部《易传》。展示采用简体转录，整理空白与版面注记；本轮校核保留履、否、同人和坎的完整开头，并据《正义》将剥卦断句校为「不利有攸往」。
- 现代整理逐卦参照[《周易正义》目录（revision 1645137）](https://zh.wikisource.org/w/index.php?title=周易正義&oldid=1645137)：魏王弼、晋韩康伯注，唐孔颖达等疏。实际取义页面及版本分别记在 JSON 中。书目背景可参照[国家图书馆／国家古籍保护中心介绍](https://www.nlc.cn/pcab/gjbhzs/jd/20170816_154623.shtml)；本项目使用网上转录，不称其为国图校定本。
- 谦、蛊、贲、复、无妄、革另参照宋朱熹《原本周易本义（四库全书本）》：[卷一（revision 736571）](https://zh.wikisource.org/w/index.php?title=原本周易本義_(四庫全書本)/卷01&oldid=736571)、[卷二（revision 736575）](https://zh.wikisource.org/w/index.php?title=原本周易本義_(四庫全書本)/卷02&oldid=736575)、[卷五（revision 527365）](https://zh.wikisource.org/w/index.php?title=原本周易本義_(四庫全書本)/卷05&oldid=527365)。具体取义与注家差异见各条 `basis_notes`，未列入的卦不声称已逐条核对《本义》。

上述古典作品本身属于公有领域；转录来自维基文库贡献者，页面另载 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 条款。古籍的公版状态不等于现代译注可任意转载。本轮未确认一套覆盖 64 卦、具有明确再分发许可的现成现代权威译文，因此没有采用或冒称此类译文。公开来源不表示原作者或有关机构认可本产品。

## English

The three reading modes separate **classical text**, **short modern notes**, and **extended modern notes**. The modern notes are this project's own paraphrases of the classical text and commentaries, prepared with AI assistance and cross-checked entry by entry. They are not an existing translation by a classical commentator or modern scholar.

[readings.json](readings.json) contains all 64 modern entries and their source records. Each record includes page links, revision IDs, SHA-256 hashes of the original source wikitext, and an explanation of the interpretation used. The main commentary is *Zhouyi Zhengyi*; six entries also cite Zhu Xi's *Zhouyi Benyi*, as identified above. The hashes identify the retrieved source text, not the resulting paraphrases.

The classical collection contains 64 complete judgments, 384 line texts and their 384 Small Images, plus the special texts for Qian and Kun. It does not contain every part of the Ten Wings. Display text uses simplified Chinese transcription with documented normalization and corrections. The ancient works are public domain; Wikisource transcription credits and applicable site terms remain distinct from the rights in modern translations. No complete modern scholarly translation with confirmed redistribution permission was adopted.

## 数据校验 · Dataset verification

`readings.json` SHA-256:

```text
ad0c68c6150423662601412ef622da11c76adfcc9bd3a2740d8ff2101002769f
```

This digest identifies the frozen modern dataset accompanying this draft. Firmware build and device verification are recorded separately in [VALIDATION.md](VALIDATION.md).
