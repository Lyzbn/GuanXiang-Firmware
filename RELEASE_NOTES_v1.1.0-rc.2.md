# 观象 v1.1.0-rc.2（预发行）

2026-10-25。这一版修复「自学 → 读六十四卦」目录翻页：屏幕每页显示 4 卦，旧版左右键却移动 8 卦，造成隔页跳过。现在左右键与显示统一为 4 卦，可顺序浏览全部 16 页，首尾循环，并在打开一卦后返回原目录位置。

## 保留的功能

三档阅读（古文、短意、精意）、64 卦与 386 份逐爻／用辞解读、动爻顺读、12 课八卦入门、叠六爻及 40px 大字卦象卡均保留。字体、阅读文字、数据格式和设备适配未变；仅面向 M5Stack Cardputer ADV，离线运行，无需 microSD。

## 安装文件

| 文件 | 用途与数据影响 |
| --- | --- |
| `GuanXiang-Cardputer-ADV-v1.1.0-rc.2-Full.bin` | 首次安装或主动重装；写 `0x0`，会清除历史和设置 |
| `GuanXiang-Cardputer-ADV-v1.1.0-rc.2-AppUpgrade.zip` | 兼容布局、app0 启动的既有观象；检查通过后仅写 `0x10000`，不写 NVS |
| `GuanXiang-Cardputer-ADV-v1.1.0-rc.2-Relink.zip` | 对应本次二进制的重链接材料 |
| `INSTALL.md`、`PROVENANCE.json`、`SHA256SUMS` | 安装、来源与外层文件摘要 |

[下载 rc.2](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.2) · [安装说明](INSTALL.md)。新包包含完整 Adafruit TCA8418 BSD 声明和既有字体许可，无需另取 rc.1 的许可补充包。rc.1 原发行附件与摘要保留不变。

公开发行号为 **v1.1.0-rc.2**，已验收二进制原样发布，源码内部版本仍为 `1.1.0-dev`。修复提交 `96057ad`，合并提交 `935194f`，CI 检出 `fd68d201`，三者源码树一致。应用为 **1,567,664 字节**，SHA-256：

`44dd57a8d659d0097c00e48154155ce8d289ef2272c89fbe6df7feaf48239ec5`

完整镜像为 **1,633,200 字节**，SHA-256：

`81f8cea104067171cf768409fd686dd82cb8b3f359d0f95c6aa8ef109e472069`

以上是镜像摘要，不是 ZIP 摘要。

## 本轮验证

固定源码 CI `40195260690` 通过；239,345 项原生回归检查通过，自学主机审计 5,362 个布局／34,342 个边界无错误。8 项离线升级器测试和完整镜像布局校验通过。匹配重链与修改框架重建通过；公开 Linux 工作流对发行资产的核验另行记录。

应用写入、独立 Flash 核验、NVS 保留及 20 秒启动烟测通过。用户实机确认正常启动、旧历史与设置保留；目录反向 `1–4 → 61–64 → 57–60`、正向 `57–60 → 61–64 → 1–4`，以及第 64 卦打开后返回位置均正常。

本轮未重复完整起卦、USB／电池冷启动、长期运行或全部设置组合。rc.1 的相关验收保留为历史记录，不算作这一镜像的新验收。重链接与逐版本边界见 [VALIDATION.md](VALIDATION.md)；此前功能说明见 [rc.1 发行说明](RELEASE_NOTES_v1.1.0.md)。

## English

This prerelease fixes the study catalogue skipping alternate pages. Left/Right now advances four entries, matching the four visible rows, and wraps through all sixteen pages. Opening a hexagram and returning preserves the catalogue position. Reading content, fonts, data formats and the other rc.1 features are unchanged.

Use the Full image at `0x0` for a first installation or reset; it clears history and settings. Eligible existing installations should use AppUpgrade, which checks the partition layout and app0 selection before writing only `0x10000`. The package includes the complete TCA8418 BSD notice; the old rc.1 assets remain unchanged.

The accepted CI binary is distributed unchanged as v1.1.0-rc.2; its internal version remains `1.1.0-dev`. CI, 239,345 native checks, study-layout checks, eight offline upgrader tests and merged-image layout checks passed. Matching relink and modified-framework rebuild checks also passed; native Linux verification of release assets is recorded separately. Device acceptance covered normal startup, retained history/settings, both catalogue wrap directions, and opening hexagram 64 and returning correctly. Full casting and USB/battery cold starts were not repeated for this binary; rc.1 results remain historical evidence. See the validation record for the exact scope.
