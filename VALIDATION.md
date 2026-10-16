# 验证记录 · Validation

## 当前候选：64 卦大字卦象卡（2026-10-16）

源码 `ae85426a6943abf851704dd74d2dc820eb4ae4c6` 仅在 38 候选基础上调整自学卦象卡：所有 64 卦显示 40px 大字卦名、左侧卦图、上方上下卦与底部两句短意。阅读内容、课程和字体数据未改变，已与该固定提交逐字核对。

**固定源码 CI 全部通过。已仅更新 app0，写后核验、NVS 保持与启动烟测通过；本候选用户验收已通过，v1.1.0-rc.1 已公开预发行。** 旧 38 的用户反馈、启动记录及重链结论均留在下方历史区，不能自动归给新镜像。

| 选定应用 | 标识 |
| --- | --- |
| 固定源码 Linux CI | `38967327177`，全部通过 |
| 应用镜像大小 | 1,567,632 字节 |
| 应用 SHA-256 | `57e9dd2d6238164209ce90b4fc03c7b92e6c33df8f383d3b3cbba28dfb087f5e` |
| 准确重链输入采集 | `38967328357`，成功；匹配重链验证通过 |
| 设备结果 | 仅写 app0；独立 verify_flash 通过，NVS 全部 20,480 字节与升级前一致；20 秒启动烟测通过，用户验收已通过 |

| 软件检查 | 结果与范围 |
| --- | --- |
| 本地正式构建 | 通过；RAM 24,556 / 327,680 字节；Flash 1,567,545 / 3,342,336 字节 |
| 原生回归与构建 | 固定源码 CI 通过，238,355 项原生检查通过 |
| 主阅读主机审计 | 13,522 个布局、214,191 个边界，0 错误；68 张预览 |
| 自学主机审计 | 5,362 个布局、34,342 个边界，0 错误；32 张预览 |
| 新布局覆盖 | 全部 64 卦均支持大字卦名与卦图 |
| 安装资产 | 8 项离线升级检查通过；Full 为 1,633,168 字节，应用偏移及 NVS 全 `0xff` 检查通过 |
| Debug | 本轮未重跑；下方 38 的 Debug 成功仅属历史证据 |

Flash 是本地构建统计，不是 Linux CI `.bin` 长度。主阅读与自学采用各自审计口径。本次机器检查和用户验收已通过，具体用户确认范围如下；未据此宣称全部设置组合或长期压力测试通过。

### 本候选匹配重链通过

- 采集运行 `38967328357` 的 3,351 个 framework/source/SDK 文件逐个与所提供材料匹配。
- 18 个原始应用对象重链精确复现所选 CI 应用；删除未使用的 IPA 日文字体成员后仍逐字节相同。
- 18 个去除调试信息的应用对象可重链，产物仍为 1,567,632 字节；仅 ELF 摘要及镜像校验区域的 65 个字节变化，其余字节一致。重链 SHA-256 为 `8f21618ed29e31fac0d6b212650d17aa65a7e39dfbe453e50f56b2ec4cbc3e7d`，不是安装镜像摘要。
- 修改框架后 48 个 core/SPI/Wire 源文件与 3 个库重建和链接通过，测试结束后已恢复原始源文件。

以上在交叉工具环境中使用准确 Linux CI 运行库完成；**公开 Linux wrapper 原生运行仍待单独执行**。完整结果见 [RELINK_VALIDATION.json](RELINK_VALIDATION.json)。该 JSON 是重链包生成时的记录，发布状态以本页为准。它仅描述重链流程，其 `device_flashing_performed: false` 表示此重链流程不烧录设备；本候选的独立设备结果记录在下文。

### 本候选设备机器检查

应用区写入后独立 `verify_flash` 通过；全部 20,480 字节 NVS 与升级前一致。20 秒受控串口启动烟测通过，观察到一次正常应用启动，显示 240×135，loop、IMU 与扬声器就绪，报告 heap 358,076 字节；观察窗口内未见 fatal 或重启循环。

### 本候选用户验收通过

用户明确确认：

- 大字卦卡显示满意，旧历史和设置保留。
- 完整本卦、动爻到之卦阅读正常，新占完成后历史只有一条新增。
- USB 与电池分别冷启动正常，新历史和设置均保留。

以上为本次 `ae85426` 的实际确认范围，不宣称长期压力测试或全部设置组合已验证。[`v1.1.0-rc.1`](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.1) 已公开预发行，源码元数据仍为 `1.1.0-dev`；不称为稳定正式版。

### Current candidate — English

Source `ae85426a6943abf851704dd74d2dc820eb4ae4c6` changes only the study hexagram card relative to the 38 candidate: all 64 cards show a 40px name, a figure on the left, trigram labels above and two summary lines below. Published reading, lesson and font data are byte-identical to this source.

Fixed-source CI `38967327177` passed. The selected application is 1,567,632 bytes, SHA-256 `57e9dd2d6238164209ce90b4fc03c7b92e6c33df8f383d3b3cbba28dfb087f5e`. Exact-input capture `38967328357` and matching relink verification passed: 3,351 framework/source/SDK files matched; original objects and the unused-font removal reproduce the CI image exactly. All 18 stripped objects relink with only 65 digest/checksum bytes changed; rebuilding 48 core source units and three libraries after modification also passed. Native execution of the public Linux wrapper remains pending. Local Release statistics are RAM 24,556 bytes / Flash 1,567,545 bytes. Main-reading audit: 13,522 layouts / 214,191 bounds / 68 previews. Study audit: 5,362 layouts / 34,342 bounds / 32 previews; both report zero errors. The exact-source CI recorded 238,355 passing native checks. Debug was not rerun for this source.

**App-only writing and independent flash verification passed. All 20,480 NVS bytes remain unchanged. The 20-second serial boot smoke test passed, with one normal boot, display/loop/IMU/speaker ready and no fatal error or reboot loop in the observation window. User acceptance passed; v1.1.0-rc.1 is publicly available as a prerelease.** The user confirmed the large-name cards, old data retention, complete reading with exactly one new history entry, and USB/battery cold starts with new data retained. These checks do not establish long-duration stress-test results. The historical 38 evidence below, including its Debug build, remains separate.

## 历史基线：38 深化精意与自学候选（2026-10-16）

本次应用源码为 `38f2db6040246967c6b827f2c809dde6f2cad725`，新增 64 卦四节精意、384 爻及用九／用六共 386 份解读、12 课八卦入门与上下卦组合自学。动爻 Enter 顺读完成爻辞、小象、精意及下一动爻，末项进入之卦。

**本次固定源码 CI 已全部通过，选定应用已仅写入设备 app0；启动烟测通过；用户已确认正常启动、旧数据保留且总体体验良好，之后提出大字卦卡增强，固件当时未正式发布。** 写后应用摘要匹配；NVS 全部 20,480 字节与升级前一致。这些证据不代替功能交互、历史回顾或冷启动验收。配套重链包另经完整来源与重链检查，结果见下文；不沿用旧 `4d412daa` 的结论。

| 选定应用 | 标识 |
| --- | --- |
| 固定源码 Linux CI | `38964682642`，全部通过 |
| 应用镜像大小 | 1,567,440 字节 |
| 应用 SHA-256 | `f58703ade8e478e8950393c071d9625de22d77e389ebff9f8f85504cf5565b6a` |
| 设备写入 | 仅 app0，写后摘要验证通过；NVS 20,480 字节不变 |

该摘要只标识应用镜像，不是合并镜像或发行归档。

本次受控串口启动烟测通过：显示 240×135、IMU 与扬声器就绪，应用进入 loop，报告 heap 358,076 字节。观察到一次正常应用启动，观察窗口内未见 fatal 错误或重启。用户随后确认正常启动、旧数据保留且总体体验良好；该反馈不等于下列全部专项验收项目逐一通过。启动烟测不等于这些交互项目已通过。

| 检查 | 本次结果 |
| --- | --- |
| 本地原生回归 | 238,355 项通过 |
| 内容与出处 | 64 卦／386 条爻级解读；450 处古典来源锚点命中固定版本 |
| 正式构建 | 通过；RAM 24,556 / 327,680 字节；Flash 1,567,345 / 3,342,336 字节 |
| 调试构建 | 通过；Flash 1,614,005 字节 |
| 主阅读主机审计 | 13,522 个布局、214,191 个边界检查，0 错误；68 张预览 |
| 自学主机审计 | 5,359 个布局、34,070 个边界检查，0 错误；29 张预览 |
| 字形 | 2,241 个正文字符覆盖通过；317 个新增正文补字 |

这里的 Flash 数值为本地构建统计，不是 Linux CI 应用 `.bin` 文件长度。主阅读与自学审计采用各自检查口径；主机预览仍不能代替 LCD 字形、实体键、声音、帧率与供电场景验收。来源锚点命中也不等于全部录文已据古籍扫描本逐字校勘。

公开的 [readings.json](readings.json) 与 [study-content.json](study-content.json) 从上述固定提交导出，包含阅读文字、图示参数和出处；其文件摘要见 [TEXT_SOURCES.md](TEXT_SOURCES.md)。不含私有应用源码、完整来源页缓存、构建对象或设备数据。

### 本次匹配重链与升级包

- 完整来源采集运行 `38964686178`；包内 3,351 个 framework/source/SDK 文件均逐个与该次 CI 实际源码核对。
- 18 个应用对象和 6 个库归档取自该次采集。原对象重链及移除未引用 IPA 字库成员后均逐字节等于应用 `f58703ad…5565b6a`。
- 应用对象去除调试信息后可重链；仅 63 个字节在 ELF 摘要和镜像校验区域不同，其余应用字节一致。重链摘要为 `16370bc0d6c23d27221071fa3c2b3fdad991c613598e7f84c4d265955294c670`。
- 修改框架后的 48 个 core/SPI/Wire 源文件及 3 个库重建通过，验证后原始源码已恢复；完整包清单核对通过。
- 新版应用升级脚本的 8 个离线用例通过，测试仅使用包内应用和嵌入的布局样本，不依赖私有构建路径。

重链验证在 macOS 交叉工具环境中使用准确 Linux CI 运行库完成；最终 Linux wrapper 尚待公开只读流程运行。此处保留旧 38 的摘要记录；[RELINK_VALIDATION.json](RELINK_VALIDATION.json) 当前仅对应新 ae 候选。这不替代下列用户硬件验收。

### 38 未逐项确认的验收范围

- 乾、坎、既济等完整卦级及逐爻精意的 LCD 字形、分节分页和页脚提示。
- 首页 L、12 课全部内容、上下卦组合、64 卦目录、返回位置和用九／用六。
- 无动、单动、多动与全动乾坤的 Enter 顺读，包括末项进入之卦。
- 原有起卦、T 模式切换、历史与设置保留、新历史仅增加一条、USB／电池冷启动和长时间运行。

### Historical 38 candidate — English

Updated application source is `38f2db6040246967c6b827f2c809dde6f2cad725`. Local Release/Debug builds and 238,355 native checks passed. Main-reading audit: 13,522 layouts / 214,191 bounds / 68 previews. Study audit: 5,359 layouts / 34,070 bounds / 29 previews. Both audits report zero errors. Content checks cover 64 expanded hexagram readings, 386 line/special-text readings and 450 source anchors.

**Fixed-source CI `38964682642` passed and the selected application was flashed to app0 only. The serial boot smoke test passed; the user subsequently confirmed normal startup, preserved data and a positive overall experience, then requested the large study-card names. This was not acceptance of every individual scenario, and firmware remained unpublished.** The application is 1,567,440 bytes, SHA-256 `f58703ade8e478e8950393c071d9625de22d77e389ebff9f8f85504cf5565b6a`; its written digest matches. All 20,480 NVS bytes remain unchanged. Matching relink and modified-framework rebuild checks passed with the supplied CI inputs; the final Linux wrapper remains to be run in the read-only public workflow. Local program-size statistics are not the CI `.bin` byte length. Older artifact and device records below apply only to their stated versions.

## 以下为历史基线：上一轮三档阅读候选

以下保留 `4d412daa` 的已完成记录，供区分版本。其镜像、重链材料及启动检查均不证明本次 `38f2db6` 的新增内容已在设备上通过。

## 旧 4d 三档阅读候选状态（2026-10-16）

应用源码已冻结，Linux CI 镜像已选定，构建与主机检查已通过。**本候选已烧录并通过启动检查，完整设备验收进行中，固件尚未正式发布。** 许可材料及与所选镜像匹配的重链材料已备齐，相关重链检查已通过。

| 项目 | 选定候选 |
| --- | --- |
| 应用源码提交 | `4d412daab3e4f18339637392813d51ea159af610` |
| 构建来源 | Linux GitHub CI，Cardputer ADV Release |
| 应用镜像大小 | **1,202,112 字节** |
| 应用 SHA-256 | `6a694cd5e1bec230d249fa4298cd9568841b52689c28484f853b38075b2b06f3` |

以上摘要对应应用镜像，不是完整合并镜像或压缩归档。后续安装包和重链材料必须明确对应这一候选，不能借用其他构建的摘要。

## 已完成的检查

- **149,362 项原生检查通过**：覆盖独立阅读模式存储、旧设置及历史保留、保存失败回滚、三档完整分页、禁首标点及历史阅读不新增记录。
- **9,800 项主机布局检查、62 页预览审计通过**；文本与字体覆盖审计通过。
- 五条古文提取回归通过：履、否、同人、习坎及剥的完整卦辞与预期一致。
- Cardputer ADV Release、Debug 本地构建通过；固定应用的两轮 GitHub CI 检查通过，包含原生检查、字体／文本审计、Release 构建、主机视觉审计与完整私有归档校验。
- 应用升级检查 **8 个离线用例通过**，该检查没有写入设备。

最新内部运行记录：

| 运行 | 结果与范围 |
| --- | --- |
| PR #5 CI `38952526657` | 通过；工作流 HEAD `bb3cd84` 仅增加私有重链输入采集工作流，应用代码仍对应冻结的 `4d412daa` |
| 固定 `4d412daa` 重链输入采集 `38952513232` | 通过；采集 Linux 构建对象、工具链和 SDK 输入；后续匹配重链检查已通过，见下文 |

工作流提交与应用源码提交分别记录，避免把打包流程变更误认作应用变更。以上工作流及构建对象保存在私有源码仓库中，当前没有公开固件下载。

## 匹配重链材料

- 使用原始 CI 应用对象和 CI 对应运行库，重链结果与选定应用逐字节一致。
- 删除 M5GFX archive 未使用的 IPA 日文字体成员后，重链结果仍与选定应用逐字节一致。
- 配套包提供 17 个去除调试信息的应用对象。重链后应用仍为 1,202,112 字节，仅构建摘要与镜像校验相关字段变化，其他镜像字节相同。
- 修改 Arduino core 后，48 个 core/SPI/Wire 源文件编译和 3 个 archive 重建、链接均通过，随后恢复原始源码。
- 官方 Linux 工具链归档及 esptool 包已校验摘要，分别 1,737 和 199 个文件与 CI 导出一致。工具链需从官方安装，不作为独立运行库随包分发。
- 许可材料清单 93 项校验通过。上述为构建与重链检查，没有替代新版设备验收。

## 本地构建与选定 CI 镜像的区别

macOS 本地 Release 镜像为 **1,202,368 字节**，Debug 为 **1,247,296 字节**；两种本地构建的 RAM 统计均为 **24,508 字节**。本地镜像与选定的 Linux CI 镜像字节不同，本地镜像及其重链输入不能直接替代上表候选。最终匹配结论应以选定 CI 镜像和对应材料的验证记录为准。

## 新版设备验收进行中

2026-10-16，所选候选已通过应用区升级写入设备，写入摘要匹配。升级前完成 8 MB 备份并与设备摘要校验；升级及首次启动前后 NVS 字节完全一致。20 秒串口检查确认循环、显示、IMU 和扬声器就绪，未见 panic 或重启循环。

仍需在所选候选镜像上确认 LCD 字形和分页、设置页与卦意页的 T 键行为、完整六爻流程、旧历史和设置保留、新历史仅增加一条，以及 USB／电池分别冷启动。长时间运行与连续进退也尚未形成新版验收记录。

主机预览不能替代 LCD、实体按键和供电场景检查。下述旧版 b3 记录仅作为历史基线。

## English status

The application is frozen at `4d412daab3e4f18339637392813d51ea159af610`. The selected Linux CI image is **1,202,112 bytes**, SHA-256 `6a694cd5e1bec230d249fa4298cd9568841b52689c28484f853b38075b2b06f3`. Native checks (**149,362**), host layout checks (**9,800**), the **62-page** preview audit and two CI rounds for the frozen application passed. Latest private runs `38952526657` (PR CI) and `38952513232` (fixed-source relink-input capture) also passed.

The workflow-only PR head `bb3cd84` does not change the frozen application. Subsequent relink checks using those captured inputs have passed. The macOS local Release image is different and is not the selected candidate. **The new candidate has been flashed and passed the serial boot check; full device acceptance is in progress and firmware remains unpublished.** Licensing and relink materials are prepared; relink checks have passed; previous hardware acceptance applies only to the b3 image below.

## 旧版 b3 基线（2026-10-16）

以下结论仅对应此前在 Cardputer ADV 上验收的维护候选应用，不自动延伸到 1.1.0 或任何重新构建的文件。

- 来源提交：`b3a90f7a00e5f037e468d96917f6396db2b4dfeb`
- 应用大小：1,177,584 字节
- 应用 SHA-256：`61215d7fc268f1da0ddd1e3e2dca90543b052027b5800f940189662a3123b32c`

### 旧版真机确认

用户在 M5Stack Cardputer ADV 上确认：

- 应用更新后能正常进入观象，原历史与设置保留。
- 每爻两次 Enter 的六爻流程正常，本卦、动爻、之卦可查看。
- 完成一次起卦后，历史只增加一条。
- USB 供电与电池供电分别冷启动均正常，新历史与设置保留。

串口启动观察未发现 panic、看门狗复位或重启循环。该轮塔罗临时验收结束后，设备恢复了此观象应用及其最新历史和设置。

### 旧版主机与构建检查

- 原生逻辑检查：137,070 项检查通过，包含持久化失败回滚及首次使用行为。
- Release、Debug 固件构建通过，GitHub CI 通过。
- 56 张主机页面预览，9,403 项布局检查、178,585 项边界检查无失败。
- 古文 888 个非 ASCII 字符覆盖检查通过。
- 发行归档校验测试 6 项通过；镜像头、分区、偏移、文件摘要分别检查。

### 旧版范围限制

尚未完成全部设置组合、长时间运行和 50–100 次连续进退的专项验收。主机预览不代替 LCD 字形、色彩和实体手感检查。任何替换资源后的新应用都需重新记录构建与验证结果。
