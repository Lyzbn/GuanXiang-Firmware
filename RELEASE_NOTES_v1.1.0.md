# 观象 1.1.0（候选发行草稿）

新增三档阅读：64 卦的本卦和之卦均可查看完整古文卦辞、现代短意和现代精意；默认短意，每卦两行四字。

- 设置页 T 循环切换并保存默认模式；卦意页 T 临时切换，并回到第一页，不改默认设置。
- 长文完整分页；短意和精意可继续进入古文，古文末页直接进入后续。
- 历史按已保存的默认模式阅读，不生成新历史；动爻保留完整爻辞和小象，符合条件时可读用九、用六及其小象。
- 阅读模式使用独立存储键；现有历史与设置格式保持不变，保存失败时保持原内存状态。
- 现代短意与精意由项目依据古典注疏整理，并非现成学者译文。古文范围为 64 条完整卦辞、384 条爻辞、384 条小象和上述特殊用辞，并非全本《易传》。参见[文本来源](TEXT_SOURCES.md)。

## 已冻结的候选与验证

应用源码提交：`4d412daab3e4f18339637392813d51ea159af610`。

选定 Linux CI 应用镜像：**1,202,112 字节**，SHA-256：

```text
6a694cd5e1bec230d249fa4298cd9568841b52689c28484f853b38075b2b06f3
```

原生检查 **149,362 项**、主机布局检查 **9,800 项**和 **62 页**预览审计均通过；固定应用的两轮 CI 检查通过。最新 PR CI `38952526657` 和固定源码重链输入采集 `38952513232` 也已成功。PR #5 的工作流 HEAD `bb3cd84` 仅增加私有采集流程，不改应用代码。详见[验证记录](VALIDATION.md)。

## 发行前剩余工作

**本候选尚未烧录或完成新版设备验收，固件尚未正式发布或提供下载。** 许可与匹配所选镜像的重链材料已备齐，重链和修改库后的重建检查已通过。

仍须确认新版的完整起卦、T 键切换、历史与设置保留、LCD 分页及 USB／电池冷启动。旧 b3 应用的验收结论仅适用于旧镜像；macOS 本地构建也不能替代这里选定的 Linux CI 镜像。正式安装包及其摘要将在发行材料确认后提供。

## English

Candidate 1.1.0 adds Summary, Insight and complete Classical judgment modes for all 64 primary and changed hexagrams. Summary is the default, with two four-character lines. T saves the default in settings and changes only the current session on reading pages, returning to page one. Opening history uses the saved default and does not create a new entry. Reading-mode storage is independent of existing settings and history formats.

Modern readings are project interpretations based on classical commentaries, not an existing scholarly translation. The classical collection includes 64 complete judgments, 384 line texts and their 384 Small Image commentaries, plus the applicable special texts and commentaries for Qian and Kun; it is not the complete Yi Zhuan.

Application source is frozen at `4d412daab3e4f18339637392813d51ea159af610`. The selected Linux CI application is **1,202,112 bytes**, with the SHA-256 shown above. **149,362 native checks**, **9,800 layout checks**, the **62-page** preview audit and two CI rounds passed; latest private CI and relink-input capture also succeeded. The workflow-only PR head does not change the application.

Licensing and matching relink materials are prepared and relink checks have passed. **The candidate remains unpublished and has not been flashed or accepted on hardware.** Previous hardware acceptance applies only to the earlier b3 image. See [VALIDATION.md](VALIDATION.md) for the selected artifact, completed checks and remaining device work.
