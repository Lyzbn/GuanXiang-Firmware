# 观象 v1.1.0-rc.1（公开预发行）

这次候选扩展阅读深度，并加入无需起卦的六十四卦自学。应用源码为 `ae85426a6943abf851704dd74d2dc820eb4ae4c6`。**固定源码 CI 已全部通过，已仅更新 app0，写后核验、NVS 保持与启动烟测通过；用户验收已通过，v1.1.0-rc.1 已公开预发行。**

## 新增与调整

- **64 卦大字卦象卡**：40px 卦名与左侧卦图，上方标明上下卦，底部保留两句短意；复用现有官方字体，全部 64 卦均支持。
- **64 卦深化精意**：按「卦势、义理、处事、辨误」四节展开，讲清古义、处境和行动条件。
- **386 份逐爻与用辞解读**：384 爻及用九、用六分「释义、精意」，古注节选与出处另列。现代反思不冒称古注原话。
- **12 课 → 叠六爻 → 六十四卦自学**：首页 L 进入，从阴阳、读画方向和传统口诀认识八卦，再选择上下卦查找重卦，最后按通行卦序阅读。无需起卦，不新增历史。
- **完整古文**：保留 64 条卦辞、384 条爻辞与小象及特殊用辞；自学另收 64 条完整大象，并非全本《易传》。
- **动爻连续阅读**：Enter 先读完当前卡全部页，再按爻辞、小象、精意、下一动爻前进；末项直接进入之卦。乾坤六爻全动先完整读用九／用六。左右键仍可主动切卡。
- **长文排版**：16px 正文、20px 行距、左对齐、每屏最多四行；章节从新页开始，不用缩字或截断容纳更多内容。
- **三档与历史继续保留**：短意为默认两行四字；设置页 T 保存默认档位，阅读页 T 临时切换。自学不修改默认值，既有历史和设置格式不变。

经传原文、王弼注／孔颖达疏的古注节选、观象今释分别标明。今释为本项目依据古典注疏、借助 AI 辅助编写并核对的现代文字，不是现代学者的现成译文。推荐书目仅供延伸阅读，不表示作者、出版社或机构授权或认可本产品。完整现代文字、课程与出处见 [readings.json](readings.json)、[study-content.json](study-content.json) 和 [文本来源](TEXT_SOURCES.md)。

## 已完成的软件验证

本地 Release 构建与固定源码 CI（含 238,355 项原生检查）通过。主阅读主机审计覆盖 13,522 个布局、214,191 个边界，提供 68 张预览；自学覆盖 5,362 个布局、34,342 个边界，提供 32 张预览，两者均无错误。内容检查覆盖 64 卦、386 份爻级解读与 450 处来源锚点。

固定源码 Linux CI `38967327177` 全部通过；选定应用为 1,567,632 字节，SHA-256 为 `57e9dd2d6238164209ce90b4fc03c7b92e6c33df8f383d3b3cbba28dfb087f5e`。准确输入采集 `38967328357` 成功，匹配重链及修改框架重建验证均通过；公开 Linux 原生重链与框架重建[检查已通过](https://github.com/Lyzbn/GuanXiang-Firmware/actions/runs/38968830479)。仅写 app0 后独立 verify_flash 通过，20,480 字节 NVS 保持一致，20 秒启动烟测通过；用户验收已通过；不能沿用旧 38 的设备或重链结论。逐版本检查及设备边界见 [VALIDATION.md](VALIDATION.md)。

## 用户验收与预发行材料

用户已确认本次 `ae85426`：大字卦卡显示满意，旧历史与设置保留；完整本卦、动爻到之卦阅读正常，完成新占后历史只增加一条；USB 与电池分别冷启动正常，新历史和设置保留。这不是长期压力测试结论。

已公开 [`v1.1.0-rc.1` 预发行](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.1)，源码元数据仍为 `1.1.0-dev`，不称为稳定正式版。安装包、摘要与匹配重链材料随该预发行提供。

## English

The user accepted this exact `ae85426` candidate: large-name study cards, preserved old history/settings, complete primary/moving-line/changed reading with exactly one new history entry, and both USB and battery cold starts with new data retained. This is not a long-duration stress-test result. The public release is [**v1.1.0-rc.1**](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.1), a prerelease with source-version metadata `1.1.0-dev`, not a stable release.

All 64 study cards now show a 40px hexagram name beside the figure, upper/lower trigram labels above, and two short summary lines below. This visual update reuses the existing official fonts.

This 1.1.0 candidate expands all 64 hexagram readings into four sections and adds 386 individual readings: 384 lines plus the special Use of Nine and Use of Six. Each separates explanation of the classical commentary from modern reflections, with commentary excerpts and sources shown separately.

Press L on the home screen for **twelve foundation lessons → upper/lower trigram combinations → all 64 hexagrams**. Study requires no cast and creates no history entry. It adds the 64 complete Great Images alongside the existing judgments, line texts and Small Images; this is not the complete Ten Wings.

Enter finishes each moving-line card before continuing through line text, Small Image, Insight, the next moving line and finally the changed hexagram. All-moving Qian and Kun complete their special Use text first. Long text retains a 16px body, 20px line spacing and a four-line maximum; sections begin on new pages. Summary remains the default; T saves a default in settings or switches temporarily during reading. Existing history and settings formats remain unchanged.

Canonical text, Wang Bi/Kong Yingda commentary excerpts and AI-assisted project interpretations are labelled separately. Recommended modern books are further-reading suggestions, not licensed translations or endorsements.

Application source: `ae85426a6943abf851704dd74d2dc820eb4ae4c6`. The local Release build and fixed-source CI, including 238,355 native regression checks, passed. Main-reading audit: 13,522 layouts / 214,191 bounds / 68 previews. Study audit: 5,362 layouts / 34,342 bounds / 32 previews. Both report zero errors. **Fixed-source CI `38967327177` passed. App-only writing, independent flash verification, NVS preservation and the serial boot smoke test passed; this candidate’s user acceptance passed, and v1.1.0-rc.1 is publicly available as a prerelease.** The application is 1,567,632 bytes; its SHA-256 is shown above. Exact-input capture `38967328357`, matching relink and modified-framework rebuild verification passed. Native Linux relinking and framework rebuilding [passed](https://github.com/Lyzbn/GuanXiang-Firmware/actions/runs/38968830479) using the published release assets. Earlier draft device or relink results do not validate this build. See [VALIDATION.md](VALIDATION.md).
