# 观象 1.1.0（深化精意与自学候选草稿）

这次候选扩展阅读深度，并加入无需起卦的六十四卦自学。应用源码为 `38f2db6040246967c6b827f2c809dde6f2cad725`。**固定源码 CI 已全部通过，新应用已仅写入设备 app0；启动烟测通过，用户对新增阅读、自学与顺读的验收进行中，尚未收到验收结果，固件未正式发布。**

## 新增与调整

- **64 卦深化精意**：按「卦势、义理、处事、辨误」四节展开，讲清古义、处境和行动条件。
- **386 份逐爻与用辞解读**：384 爻及用九、用六分「释义、精意」，古注节选与出处另列。现代反思不冒称古注原话。
- **12 课 → 叠六爻 → 六十四卦自学**：首页 L 进入，从阴阳、读画方向和传统口诀认识八卦，再选择上下卦查找重卦，最后按通行卦序阅读。无需起卦，不新增历史。
- **完整古文**：保留 64 条卦辞、384 条爻辞与小象及特殊用辞；自学另收 64 条完整大象，并非全本《易传》。
- **动爻连续阅读**：Enter 先读完当前卡全部页，再按爻辞、小象、精意、下一动爻前进；末项直接进入之卦。乾坤六爻全动先完整读用九／用六。左右键仍可主动切卡。
- **长文排版**：16px 正文、20px 行距、左对齐、每屏最多四行；章节从新页开始，不用缩字或截断容纳更多内容。
- **三档与历史继续保留**：短意为默认两行四字；设置页 T 保存默认档位，阅读页 T 临时切换。自学不修改默认值，既有历史和设置格式不变。

经传原文、王弼注／孔颖达疏的古注节选、观象今释分别标明。今释为本项目依据古典注疏、借助 AI 辅助编写并核对的现代文字，不是现代学者的现成译文。推荐书目仅供延伸阅读，不表示作者、出版社或机构授权或认可本产品。完整现代文字、课程与出处见 [readings.json](readings.json)、[study-content.json](study-content.json) 和 [文本来源](TEXT_SOURCES.md)。

## 已完成的软件验证

本地 Release／Debug 构建通过；238,355 项原生检查通过。主阅读主机审计覆盖 13,522 个布局、214,191 个边界，提供 68 张预览；自学覆盖 5,359 个布局、34,070 个边界，提供 29 张预览，两者均无错误。内容检查覆盖 64 卦、386 份爻级解读与 450 处来源锚点。

固定源码 Linux CI `38964682642` 全部通过；选定应用为 1,567,440 字节，SHA-256 为 `f58703ade8e478e8950393c071d9625de22d77e389ebff9f8f85504cf5565b6a`。仅写 app0 后摘要验证通过，NVS 全部 20,480 字节与升级前一致。启动烟测通过，用户验收进行中，尚无本次用户验收结论；匹配重链和安装材料正在更新。逐版本检查及设备边界见 [VALIDATION.md](VALIDATION.md)。

## 发行前剩余工作

新候选需要验证 LCD 字形与分节分页、首页 L 和课程／组合／目录按键、动爻到之卦的顺读，以及原有起卦、阅读档位、历史和设置保留、USB／电池冷启动。旧候选已完成的启动或交互记录仅适用于旧镜像。安装包与摘要将在匹配材料确认后更新，本文件不提供尚未确认的下载链接。

## English

This 1.1.0 candidate expands all 64 hexagram readings into four sections and adds 386 individual readings: 384 lines plus the special Use of Nine and Use of Six. Each separates explanation of the classical commentary from modern reflections, with commentary excerpts and sources shown separately.

Press L on the home screen for **twelve foundation lessons → upper/lower trigram combinations → all 64 hexagrams**. Study requires no cast and creates no history entry. It adds the 64 complete Great Images alongside the existing judgments, line texts and Small Images; this is not the complete Ten Wings.

Enter finishes each moving-line card before continuing through line text, Small Image, Insight, the next moving line and finally the changed hexagram. All-moving Qian and Kun complete their special Use text first. Long text retains a 16px body, 20px line spacing and a four-line maximum; sections begin on new pages. Summary remains the default; T saves a default in settings or switches temporarily during reading. Existing history and settings formats remain unchanged.

Canonical text, Wang Bi/Kong Yingda commentary excerpts and AI-assisted project interpretations are labelled separately. Recommended modern books are further-reading suggestions, not licensed translations or endorsements.

Application source: `38f2db6040246967c6b827f2c809dde6f2cad725`. Local Release/Debug builds and 238,355 native checks passed. Main-reading audit: 13,522 layouts / 214,191 bounds / 68 previews. Study audit: 5,359 layouts / 34,070 bounds / 29 previews. Both report zero errors. **Fixed-source CI `38964682642` passed and the selected application was flashed to app0 only. The serial boot smoke test passed; user acceptance is in progress, with no user result recorded yet, and firmware remains unpublished.** The application is 1,567,440 bytes; its SHA-256 is shown above and its written digest matches. All 20,480 NVS bytes are unchanged. Matching materials are being updated; earlier draft device or relink results do not validate this build. See [VALIDATION.md](VALIDATION.md).
