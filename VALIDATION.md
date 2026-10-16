# 验证记录 · Validation

## 1.1.0 候选状态（2026-10-16）

应用源码已冻结，Linux CI 镜像已选定，构建与主机检查已通过。**本候选尚未烧录或完成新版设备验收，固件尚未正式发布。** 许可材料及与所选镜像匹配的重链材料已备齐，相关重链检查已通过。

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

## 新版设备待验收

仍需在所选候选镜像上确认 LCD 字形和分页、设置页与卦意页的 T 键行为、完整六爻流程、旧历史和设置保留、新历史仅增加一条，以及 USB／电池分别冷启动。长时间运行与连续进退也尚未形成新版验收记录。

主机预览不能替代 LCD、实体按键和供电场景检查。下述旧版 b3 记录仅作为历史基线。

## English status

The application is frozen at `4d412daab3e4f18339637392813d51ea159af610`. The selected Linux CI image is **1,202,112 bytes**, SHA-256 `6a694cd5e1bec230d249fa4298cd9568841b52689c28484f853b38075b2b06f3`. Native checks (**149,362**), host layout checks (**9,800**), the **62-page** preview audit and two CI rounds for the frozen application passed. Latest private runs `38952526657` (PR CI) and `38952513232` (fixed-source relink-input capture) also passed.

The workflow-only PR head `bb3cd84` does not change the frozen application. Subsequent relink checks using those captured inputs have passed. The macOS local Release image is different and is not the selected candidate. **The new candidate has not been flashed or accepted on hardware and remains unpublished.** Licensing and relink materials are prepared; relink checks have passed; previous hardware acceptance applies only to the b3 image below.

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
