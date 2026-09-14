# Super Dev

<div align="center">

<img src="docs/assets/super-dev-logo.png" alt="Super Dev - AI PIPELINE ORCHESTRATOR" width="600">

### 面向商业级交付的宿主教练系统 · 知识驱动治理

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Type Checks](https://img.shields.io/badge/type%20checks-mypy-success)](https://mypy-lang.org/)
[![Lint](https://img.shields.io/badge/lint-ruff-success)](https://docs.astral.sh/ruff/)

[English](README_EN.md) | 简体中文

</div>

---

## 版本

当前版本：`2.4.0`

- 发布说明：[v2.4.0 更新内容](docs/releases/2.4.0.md)
- 官网更新历史：[superdev.goder.ai/changelog](https://superdev.goder.ai/changelog)

## 安装

首页安装口径默认使用 uv：

```bash
uv tool install super-dev
```

安装完成后执行：

```bash
super-dev
```

源码安装、指定版本回滚等次级安装方式保留在 [docs/INSTALL_OPTIONS.md](docs/INSTALL_OPTIONS.md)。

跨平台说明：

- Windows、macOS、Linux 都先安装包，再直接运行 `super-dev`
- 仓库内的 `install.sh` 只是 macOS/Linux 便捷入口，不是 Windows 唯一入口

---

## 演示视频

<video controls playsinline preload="metadata" src="https://shangyankeji.github.io/super-dev/demo.mp4" width="100%"></video>

- 在线播放：[观看演示视频](https://shangyankeji.github.io/super-dev/demo.mp4)
- 仓库文件：[demo.mp4](super-dev-website/public/demo.mp4)

---

## 联系开发者

<div align="center">

微信号：**Excellent_We**

<img src="super-dev-website/public/wx.png" alt="开发者微信" width="200">

扫码或搜索微信号联系开发者

</div>

---

## 项目介绍

`Super Dev` 不是再给宿主叠一层命令集合或脚手架壳。它更像一个宿主教练系统，用来把宿主里的模型能力训练成一套稳定、清晰、可审计、能做商业项目的交付流程。

产品定位：

- 宿主负责模型调用、联网搜索、代码产出、终端执行与文件修改
- `Super Dev` 负责图纸生成、流程治理、设计约束、质量门禁、审计产物与交付标准

换句话说：

- 宿主是执行者
- `Super Dev` 是产品总监、架构师、设计总监、技术教练和 QA 负责人组成的指导系统

它解决的是“宿主会写代码，但不一定会稳定交付”的问题：

- 将需求沉淀为可落地工件：PRD、架构、UI/UX、Spec、任务清单与交付清单
- 将开发过程组织为标准化流水线：可追踪、可恢复、可审计、可复盘
- 将质量控制前置到每个阶段：策略治理、红队审查、质量门禁、发布演练
- 将多宿主协作统一到同一套工程规范：12 个 CLI、9 个 IDE、5 个桌面助手按项目优先注入，共享同一交付标准
- 将知识库与验证规则自动推送到每个阶段：知识驱动治理，而非依赖人工检查
- 将宿主训练成“能稳定做出精品商业项目”的团队，而不是让用户自己拼流程、拼审美、拼质量门

---

## 5 分钟上手

普通用户先记住 1 条安装命令和 3 个终端命令：

```bash
uv tool install super-dev
```

```bash
# 进入宿主接入引导
super-dev

# 更新到最新版，并迁移已接入宿主
super-dev update

# 清理已注入的宿主接入面
super-dev uninstall
```

### 5 分钟路径

1. 在项目目录运行 `super-dev`
2. 让安装器自动检测宿主并写入项目级接入面；只有明确需要跨项目复用时才补用户/全局接入面
3. 打开 `output/maintenance/host-onboard-smoke-*.md`
4. 先看 `标准流第一句` / `比赛流第一句`
5. 再看 `接入后先验`、`框架焦点`、`官方工作流检查`
6. 回到宿主里触发第一句，观察它是否按 `research -> 三文档 -> 等待确认` 进入流程

如果这 6 步成立，你拿到的不是“装好了一个工具”，而是“把当前宿主训练成了这个项目的交付教练”。

### 终端只做 3 件事
- 接入
- 升级
- 卸载 / 预演清理

接入完成后，正常使用都回到宿主里。普通用户第一眼只需要记住：

```text
/super-dev 你的需求
super-dev: 你的需求
/super-dev-seeai 比赛需求
```

更细的入口差异不要靠记忆硬背，直接看安装后生成的 `host-onboard-smoke`，复制里面的 `标准流第一句` 或 `比赛流第一句` 即可。

正确心智：

- 终端只负责接入、升级与卸载
- 宿主才负责 baseline、research、三文档、确认门、Spec、实现、质量门禁与交付
- 普通开发不要离开宿主主路径；如果不是在做接入、诊断、治理收尾或兼容修复，就不要先回终端找阶段命令
- 自动判断会在接入/升级阶段发生，但不会在普通开发流程里越层改宿主配置
- `已接入` 与 `已验证` 是两回事：文件落盘不代表宿主已经真实跑通
- 已有项目不是直接开干：`evolve / variant / patch` 必须先做 `baseline -> baseline confirmation`，再进入差量 research 和三文档
- 恢复是默认场景：关窗口、关电脑、第二天继续，都优先按 `.super-dev/` 与 `output/` 工件恢复当前流程

工作模式：

- `new`：从 0 到 1 的新项目
- `evolve`：已有项目增量迭代
- `variant`：基于现有项目派生 1-N+1 版本
- `patch`：已有项目缺陷修复
- `resume`：中断后的恢复继续

记住一个原则：安装完成后，终端基本就该退场。真正开发回到宿主里，先复制 `标准流第一句` 或 `比赛流第一句`，再按 smoke guide 做首轮验收。

SEEAI 赛事极速版：

- 入口：`/super-dev-seeai` 或 `super-dev-seeai:`
- 仍然保留 `research -> 三文档 -> docs confirm -> spec`
- 但 `spec` 之后直接进入前后端一体化快速开发，不再拆预览确认门
- 适合 30 分钟左右的官网、小游戏、展示型工具、单页 demo

只有在接入、诊断、兼容修复或治理收尾时，才需要回终端。普通用户只需要记住：

```bash
super-dev
super-dev update
super-dev uninstall
```

维护者补充：

- 安装/接入后烟测指南会落到 `output/maintenance/host-onboard-smoke-*.md`
- 如果当前项目已经冻结了 `framework playbook`，安装后烟测指南会直接显示 `框架焦点（Framework Coaching Focus）`、必验场景和交付证据
- 卸载预演或正式清理会落到 `output/maintenance/host-cleanup-*.json/.md`
- 如果只是想先看会删什么，用 `super-dev uninstall --dry-run`
- 升级完成后先重开终端并执行 `super-dev --version`；如果宿主没有进入 `research -> 三文档 -> 等待确认`，再回终端跑 `doctor`
- 如果第一轮 UI 看起来过平、过空、模板味太重，不要指望“最后再补美化”；截图级 UI gate 会在 UI review、quality gate、proof-pack 和 release readiness 里继续拦截
- 正式发版文档 `docs/PUBLISHING.md` 与 `docs/RELEASE_RUNBOOK.md` 只属于维护者，不是普通用户上手路径。

其余 `detect / doctor / review / quality / release / spec / task` 都属于维护面，只在报告明确要求时由维护者进入。

说明：
- `skill / integrate` 只用于宿主接入、兼容性审计和真人验收，不属于日常开发主路径
- `config / enforce / generate` 属于内部维护能力，不是普通用户入口
- `onboard / detect / doctor / run / review / release` 允许保留，但应视为维护面而不是普通用户心智
- 真正的项目开发仍应回到宿主里，优先使用 `/super-dev` 或 `super-dev:` 开题，并直接说“继续当前流程”“现在下一步是什么”
- 如果你在已有项目里做增量开发，不要先在终端里手工跳阶段，先让宿主完成 `baseline -> baseline confirmation`，再进入差量文档和实现
- 如果只是回来继续昨天的活，不要先回终端找 `run` / `jump` / `confirm`，优先在宿主里直接说“继续当前流程”

交付与卡点处理仍然存在治理入口，但它们属于维护面，不应当成普通用户命令目录：

- `product-audit`：范围缺口与实施覆盖率体检
- `release readiness / proof-pack`：发布证据与交付闭环
- `review *`：维护者同步 gate 状态或修订状态

普通用户仍应优先回宿主里说“继续当前流程”“现在下一步是什么”。

---

## 核心功能

### 1. 11 专家 Agent 架构

当前内置 11 个领域专家 Agent，每个专家在对应阶段自动注入到 AI 提示词中，约束宿主按专业标准执行：

| 专家 | 角色 | 注入阶段 |
|------|------|----------|
| PRODUCT | 产品负责人 | research, prd, quality, delivery |
| PM | 产品经理 | research, prd |
| ARCHITECT | 系统架构师 | architecture |
| UI | 界面设计师 | uiux, frontend |
| UX | 交互设计师 | uiux, frontend |
| SECURITY | 安全工程师 | architecture, backend, quality |
| CODE | 开发工程师 | frontend, backend |
| DBA | 数据库工程师 | architecture, backend |
| QA | 质量工程师 | quality |
| DEVOPS | 运维工程师 | delivery |
| RCA | 根因分析师 | quality, delivery |

每个专家具备四层武装：Profile（目标定义、背景故事、思维框架、质量标准）+ Knowledge（阶段知识自动推送）+ Rules（验证规则绑定）+ Protocol（交叉审查协议）。每位专家配备 350+ 行深度 Playbook 操作手册，生成的 AI 提示词超过 600 行，确保每个阶段的输出符合该领域的专业基线。

### 2. UI 智能设计系统

内置完整的设计智能引擎，直接约束前端实现阶段的视觉质量：

- **119 套配色方案**：84 套产品配色 + 35 套美学配色，全部自动生成暗色模式
- **39 个组件库**：覆盖 11 个前端技术栈（React 15 / Vue 9 / Angular 4 / Svelte 2 / 其他）
- **17 套字体预设**：基于 Google Fonts 中国镜像，按产品调性分类
- **完整 Design Token 体系**：色阶、阴影、动效、排版、间距
- **12 项交付前检查清单**：A11y、响应式、暗色模式、加载态、空态、错误态等
- **10 个行业定制**：教育、医疗、电商、金融科技、SaaS、社交、内容、企业、工具、游戏

UI/UX 文档不再只是建议，而是会冻结成一份真正的 UI 契约：

- `output/*-uiux.md`
- `output/*-ui-contract.json`
- `output/frontend/design-tokens.css`
- `output/*-ui-contract-alignment.md`
- `output/*-ui-contract-alignment.json`

宿主提示词、实现约束、UI review、frontend runtime、quality gate、proof-pack、release readiness 都会围绕这份 UI 契约继续执行。

关键治理证据：

- UI review 与 UI contract alignment
- frontend runtime 运行证据
- proof-pack 与 release readiness 摘要

它们共同用于持续检查 UI 契约有没有真的落到源码和交付结果中。

### 3. 流水线编排引擎

- **新项目主链**：research -> docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery
- **已有项目主链**：baseline -> baseline_confirm -> delta research -> docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery
- **检查点与中断续传**：流水线中断后可从断点恢复，不丢失进度
- **阶段超时保护**：每个阶段设有超时机制，防止无限等待
- **确认门控制**：三文档完成后必须等待用户确认，前端预览完成后必须等待用户确认
- **阶段恢复**：宿主可以通过自然语言恢复到目标阶段，高级阶段跳转只保留给维护场景
- **UI 改版回路**：UI 不满意时可在宿主里发起正式改版回路，先更新 UIUX 文档再重做前端
- **适配 0-1 与 1-N+1**：新建项目走完整流水线，已有项目先 baseline 再走增量分析路径
- **继续当前流程路由**：内部恢复与状态命令共享同一套 workflow state 与 action card
- **恢复状态卡**：`.super-dev/SESSION_BRIEF.md` 和 `.super-dev/workflow-state.json` 会沉淀“当前动作 / 宿主第一句 / 机器侧动作 / 连续性规则”
- **关键时间线**：流程快照、语义事件、Hook 事件会汇总成统一的 recent timeline，进入 `SESSION_BRIEF`、Workflow Harness、proof-pack 与 release readiness
- **返工优先级**：文档确认门、预览确认门、UI 改版、架构返工、质量整改都进入统一状态机，不再靠用户记命令

### 4. 文档生成引擎

Super Dev 为每个阶段生成初始文档框架，宿主大模型在此基础上结合用户需求、联网研究和专家知识进行深度完善：

| 文档 | 内容 |
|------|------|
| PRD | 用户画像、功能矩阵、验收标准、竞品对标、商业规则 |
| Architecture | 系统架构、数据模型、接口契约、安全策略、部署方案 |
| UIUX | 设计 Token、页面骨架、组件清单、交互状态、响应式策略 |

宿主根据需求深度生成文档内容，最终产出的文档规模取决于项目复杂度和需求范围。支持 10 个行业领域定制：教育、医疗、电商、金融科技、SaaS、社交、内容、企业、工具、游戏。

补充说明：

- 新功能开发默认走完整流水线：`research -> 三文档 -> 用户确认 -> Spec / tasks -> 前端运行验证 -> 后端 / 测试 / 交付`
- 缺陷修复同样不会直接跳过文档；会走轻量补丁路径，先整理问题现象、复现条件、影响范围和回归风险，再更新补丁文档与验证结果
- 分析阶段默认排除 `.venv`、`site-packages`、`node_modules` 等非项目源码目录

### 5. 质量门禁体系

- **验证规则引擎**：25 条 YAML 声明式规则（14 默认 + 11 红队），支持项目级自定义覆盖
- **质量顾问**：不只说"不达标"，还给出具体修复建议（Quick Wins 优先排序）
- **Spec-Code 一致性检测**：自动比对 Spec 描述与实际代码实现，防止偏离
- **A11y 无障碍检查**：自动验证页面的无障碍标准合规性
- **性能预算校验**：检查资源大小、加载时间等性能指标
- **红队审查**：从安全、性能、架构三个维度对系统进行攻防审查
- **修复命令建议**：检测到问题后直接给出可执行的修复指令
- **策略治理**：default / balanced / enterprise 三级预设
- **Spec 质量评分**：对任务规格进行结构化评分
- **发布就绪面板**：统一展示发布前所有门禁检查结果
- **UI 契约执行检查**：质量门禁会检查 `ui-contract.json`、`design-tokens.css`、frontend runtime 与 UI 对齐报告是否一致

### 6. 宿主接入治理

- 支持 26 个主流宿主统一接入（12 CLI + 9 IDE + 5 桌面助手）
- 新增 `Droid CLI` 官方 `.factory` 宿主接入：`AGENTS.md + .factory/rules + .factory/skills`，`.factory/commands` 仅作为兼容增强面
- 自动生成宿主规则文件、`/super-dev` 映射、Skill 目录
- `detect / onboard / doctor / setup / install / start` 形成接入闭环
- 通过宿主能力边界建模，明确哪些宿主是 `Certified / Compatible / Experimental`
- `--dry-run` 预览模式与 `--stable-only` 稳定模式
- `--save-profile` 写入 `super-dev.yaml` 并用于质量门禁
- `doctor`、`detect`、`start` 默认会输出决策卡：推荐宿主、推荐理由、第一步动作、候选宿主、路径覆盖修复提示
- 决策卡、安装向导与 runtime 报告会直接给出 `标准流第一句 / 比赛流第一句 / 接入后先验 / 官方工作流检查 / 修复剧本`
- 宿主准备度会明确区分 `标准流可直接开工` 和 `SEEAI 比赛模式可直接开工`
- 支持 Windows 注册信息、shim 目录、常见路径和 `SUPER_DEV_HOST_PATH_<HOST>` 自定义路径覆盖
- 显式指定宿主时，系统会围绕你指定的宿主给建议，不再被自动检测结果带偏

### 7. 产品审计与范围缺口

- **product-audit**：从产品、交互、闭环和代码结构角度生成总审查报告
- 区分“流水线已经走完”和“范围是否真的做完”
- 为 `proof-pack`、`release readiness`、质量整改提供范围缺口输入

### 8. 可审计交付

- `proof-pack`：交付证据汇总与 executive summary
- `release readiness`：发布就绪度检查
- `frontend runtime / UI Contract Alignment / quality gate`：前端、设计契约与质量门禁闭环
- `delivery manifest/report/archive`：交付包与归档产物
- `pipeline metrics / knowledge tracking / validation report`：作为内部证据进入交付闭环，不属于普通用户主入口

### 9. 知识库系统

Super Dev 内置结构化知识库（`knowledge/` 目录），270+ 个知识文件、15 万行深度内容，覆盖 23 个技术领域：

- **架构**：微服务、API 网关、分布式事务、配置管理、服务治理
- **安全**：DevSecOps、SAST/DAST/SCA、容器安全、合规自动化、密钥管理
- **运维**：可观测性、AIOps 异常检测、容量规划、混沌工程、SLO/SLI
- **云原生**：容器编排、服务网格、无服务器架构
- **数据工程**：数据管线、流处理、数据治理
- **设计**：UI 全生命周期跨平台手册
- **移动端**：跨平台开发、原生性能优化
- **更多领域**：CI/CD、测试、产品、低代码、边缘/IoT、区块链、量子计算

知识推送引擎：

- **阶段精准映射**：306 个知识文件建立索引，7 个 pipeline 阶段精准推送相关约束
- **渐进式加载**：L1 索引（目录级快速匹配）/ L2 详情（文件级内容推送）/ L3 深度引用（段落级精准引用），token 预算控制
- **知识自演化**：SQLite 追踪每条知识的使用效果（采纳率、命中率），数据驱动权重优化
- 宿主进入流水线后，Super Dev 会自动检索 `knowledge/` 下与当前需求相关的知识文件
- 匹配到的本地标准、场景包和检查清单作为硬约束注入到三文档、Spec 和实现阶段
- 如果已生成 `output/knowledge-cache/*-knowledge-bundle.json`，宿主会继承其中的本地知识命中结果
- 同时支持联网研究增强，将 Web 搜索结果与本地知识合并输出

### 10. 内部治理能力

这部分属于内部维护与交付保障，不是普通用户日常命令面：

- YAML 验证规则与质量门禁
- 宿主兼容度探测与接入审计
- Pipeline 指标、知识跟踪、治理快照
- Prompt / 文档模板 / 规则版本化

---

## 安装方式

### 1. uv 安装（推荐）

```bash
uv tool install super-dev
```

升级：

```bash
super-dev update
```

### 2. 指定版本安装

```bash
uv tool install super-dev==2.4.0
```

升级：

```bash
uv tool upgrade super-dev
super-dev update
```

安装完成后，直接运行：

```bash
super-dev
```

默认会进入宿主安装引导：

- 顶部显示 `Super Dev` 安装入口
- `↑ / ↓` 选择宿主
- `Space` 勾选宿主
- `Enter` 开始安装
- `A` 全选
- `C` 仅选择 CLI 宿主
- `I` 仅选择 IDE 宿主
- `R` 清空选择
- `U` 升级已安装宿主

安装完成后，终端会直接给出该宿主的最终触发方式：

- slash 宿主：`/super-dev 你的需求`
- 非 slash 宿主：`super-dev: 你的需求`
- 比赛极速版：`/super-dev-seeai 比赛需求` 或 `super-dev-seeai: 比赛需求`
- 需要继续验收或恢复时，优先回到宿主里说“继续当前流程”或“现在下一步是什么”

### 3. GitHub 指定标签安装

```bash
uv tool install --from git+https://github.com/shangyankeji/super-dev.git@v2.4.0 super-dev
```

### 4. 源码开发安装

```bash
git clone https://github.com/shangyankeji/super-dev.git
cd super-dev
uv sync
uv run super-dev --version
```

---

## 依赖安装说明

当用户执行：

```bash
uv tool install super-dev
```

或：

```bash
uv tool install super-dev
```

安装器会自动安装 `pyproject.toml` 中声明的 Python 依赖，例如：

- `rich`
- `pyyaml`
- `ddgs`
- `requests`
- `beautifulsoup4`
- `fastapi`
- `uvicorn`

不会自动安装的内容：

- Claude Code / Codex CLI / Gemini CLI / Cursor / Trae / Windsurf / 桌面助手等宿主软件本身
- Node.js、npm、pnpm、Docker、数据库服务这类系统级运行环境
- 宿主账号登录状态、联网权限、浏览器能力
- 项目业务依赖以外的前后端运行时

一句话：

- `pip` / `uv` 会自动安装 **Super Dev 自己的 Python 依赖**
- 不会替用户安装 **宿主工具和系统环境**

如果你希望先显式初始化项目契约，再开始接入宿主：

```bash
super-dev bootstrap --name my-project --platform web --frontend next --backend node
```

这会显式生成：

- `.super-dev/WORKFLOW.md`

用来固定初始化规范、触发方式和阶段顺序。

---

## 当前保留的核心增强

围绕“宿主接入 + 主流水线 + 交付闭环”，当前重点保留这些增强：

- 宿主接入治理：`detect / onboard / doctor / setup / install / start`
- 三文档、Spec、前端优先、预览确认、后端、质量门禁、交付证据
- 专家按阶段注入，知识库在 research / docs / spec / implementation 阶段持续生效
- Plan-Execute / Overseer / Claude-Codex hybrid mode 仍保留在编排内核
- Design inspiration workflow 仍保留在 UI/UX 增强链里
- UI 契约、frontend runtime、UI review、quality gate、proof-pack、release readiness 同一轮证据闭环
- 交付证据、知识跟踪、Pipeline 指标作为内部治理面持续产出

## 历史能力沉淀

下面这些能力仍然是系统底座的一部分，但不再作为单独公开产品面强调：

- 知识驱动治理、渐进式知识加载、知识自演化
- YAML 验证规则、质量顾问、Spec-Code 一致性检测
- 11 专家 Playbook、交叉审查、Prompt/模板版本化
- Pipeline 指标、ADR、治理快照等内部证据
- 宿主深度适配矩阵与多宿主接入治理

---

## 整个系统如何工作

`Super Dev` 的运行方式可以概括为一条固定链路：

1. 用户在项目目录执行 `super-dev`
2. 安装引导把 Super Dev 接入到目标宿主
3. 用户在宿主里输入 `/super-dev 需求` 或 `super-dev: 需求`
4. 宿主进入 Super Dev 流水线，11 个专家 Agent 按阶段注入，知识推送引擎自动推送相关约束
5. 宿主负责联网、推理、编码、运行与修改文件
6. Super Dev 负责流程、文档、知识推送、验证规则、门禁、审计和交付标准

标准流水线：`research -> docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery`

补充说明：

- 新功能开发默认走完整流水线：`research -> 三文档 -> 用户确认 -> Spec / tasks -> 前端运行验证 -> 后端 / 测试 / 交付`
- 缺陷修复同样不会直接跳过文档；会走轻量补丁路径，先整理问题现象、复现条件、影响范围和回归风险，再更新补丁文档与验证结果
- 分析阶段默认排除 `.venv`、`site-packages`、`node_modules` 等非项目源码目录

宿主如何理解 Super Dev：

- `Super Dev` 是当前项目里的本地 Python CLI 工具，加上宿主里的规则文件 / Skill / slash 映射
- 宿主负责模型推理、联网搜索、编码、运行终端与修改文件
- `Super Dev` 负责把宿主拉进固定流水线：research、三文档、确认门、Spec、前端优先、后端联调、质量门禁、交付审计，并在每个阶段自动推送相关知识约束与验证规则
- 当用户输入 `/super-dev 需求` 或 `super-dev: 需求` 时，宿主要切换到 Super Dev 流水线执行模式
- 需要生成或刷新文档、Spec、质量报告、交付产物时，宿主应优先调用本地 `super-dev` CLI
- 如果项目根目录存在 `knowledge/`，宿主必须优先读取与当前需求相关的知识文件
- 如果已生成 `output/knowledge-cache/*-knowledge-bundle.json`，宿主必须把其中命中的本地知识、研究摘要和场景约束继承到三文档、Spec 和实现阶段

---

## 架构概览

Super Dev 2.4.0 架构由四层组成：**宿主接入层**（统一宿主矩阵，按 CLI / IDE / 桌面助手分组）、**知识治理层**（306 索引 / 渐进式加载 / 自演化）、**编排引擎层**（9 阶段流水线 / 11 专家 + Overseer / 验证规则引擎）、**交付审计层**（DORA 度量 / ADR / 一致性检测 / proof-pack）。

### 一、系统高阶流转架构

展示用户、宿主端工具、Super Dev 编排引擎与最终产物之间的流转关系。

![系统高阶流转架构](docs/assets/architecture/system-overview.png)

### 二、9 阶段核心工作流

详细描绘每次对话触发后，引擎在底层的流转经过。

![9 阶段核心工作流](docs/assets/architecture/pipeline-12-phase.png)

### 三、核心模块调用拓扑

展示 `super_dev` 下核心源码目录的职责边界和调用关系。

![核心模块调用拓扑](docs/assets/architecture/module-topology.png)

---

## 统一接入宿主矩阵

正式产品口径：

- 当前矩阵按 `CLI / IDE / 桌面助手` 分组
- `Codex` 和 `Codex CLI` 是两个不同宿主，`Claude` 和 `Claude Code` 也是两个不同宿主
- 默认采用项目优先注入：先写项目级接入面，再按需补齐用户 / 全局接入面

### CLI 宿主（12 个）

| 宿主 | 触发方式 | 终端入口 |
|------|----------|----------|
| Claude Code | `/super-dev 需求` | `super-dev` |
| Codex CLI | `$super-dev`；回退 `super-dev: 需求` | `super-dev` |
| OpenCode | `/super-dev 需求` | `super-dev` |
| Droid CLI | `/super-dev 需求`；比赛模式 `/super-dev-seeai`；回退 `super-dev: 需求` | `super-dev` |
| Gemini CLI | `/super-dev 需求` | `super-dev` |
| Kiro CLI | `/super-dev 需求` | `super-dev` |
| Cursor CLI | `super-dev: 需求` | `super-dev` |
| Copilot CLI | `super-dev: 需求` | `super-dev` |
| Qoder CLI | `/super-dev 需求` | `super-dev` |
| CodeBuddy CLI | `/super-dev 需求` | `super-dev` |
| Kimi Code | `super-dev: 需求`；显式入口 `/skill:super-dev 需求` | `super-dev` |
| Qwen Code | `/super-dev 需求` | `super-dev` |

### IDE 宿主（9 个）

| 宿主 | 触发方式 | 终端入口 |
|------|----------|----------|
| Antigravity | `/super-dev 需求` | `super-dev` |
| Cursor | `/super-dev 需求` | `super-dev` |
| Windsurf | `/super-dev 需求` | `super-dev` |
| Kiro | `/super-dev 需求` | `super-dev` |
| Trae IDE | `super-dev: 需求` | `super-dev` |
| TraeCN | `super-dev: 需求` | `super-dev` |
| CodeBuddy | `/super-dev 需求` | `super-dev` |
| CodeBuddyCN | `/super-dev 需求` | `super-dev` |
| Qoder | `/super-dev 需求` | `super-dev` |

### 桌面助手（5 个）

| 宿主 | 触发方式 | 终端入口 |
|------|----------|----------|
| Claude | `super-dev: 需求` | `super-dev` |
| Codex | App/Desktop: 在 `/` 列表里选择 `super-dev` | `super-dev` |
| WorkBuddy | `super-dev: 需求` | `super-dev` |
| Trae SOLO | `/super-dev 需求` | `super-dev` |
| Trae SOLOCN | `super-dev: 需求` | `super-dev` |

---

### 每个宿主如何使用

#### 1. Claude Code

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 Claude Code 当前会话后，直接在同一会话里触发。

触发命令：
```text
/super-dev 你的需求
```
比赛模式：
```text
/super-dev-seeai 比赛需求
```

自然语言回退：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 推荐作为首选 CLI 宿主。
2. 维护者如需核对接入面，可执行 `super-dev doctor --host claude-code`，确认项目根 `CLAUDE.md`、项目级 `.claude/CLAUDE.md`、可选 `.claude/settings*.json`、项目/用户级 skills 与 agents 一起生效。
3. Claude Code 当前按官方 `CLAUDE.md + settings + project/user skills + subagents` 模型对齐；`.claude/commands/` 仅作为兼容增强面保留，不再当主协议面。
4. 如需增强层，Super Dev 还会补齐 `.claude-plugin/marketplace.json` 与 `plugins/super-dev-claude/.claude-plugin/plugin.json`。

#### 2. Codex

安装：
```bash
super-dev
```

触发位置：
在项目目录完成接入后，重启 `codex`，然后在新的 Codex 会话里触发。

触发命令：
```text
Codex App/Desktop: 在 `/` 列表里选择 super-dev
Codex CLI: $super-dev
回退入口: super-dev: 你的需求
```

接入后是否需要重启：是

补充说明：
1. Codex App/Desktop 优先从 `/` 列表里直接选择 `super-dev`；这是已启用 Skill 的官方入口，不是项目级自定义 slash 文件。
2. Codex CLI 优先显式输入 `$super-dev`。
3. 如果当前已经在自然语言上下文里继续流程，也可以直接输入 `super-dev: 你的需求`。
4. 默认基础接入面是项目根 `AGENTS.md` 与项目级 `.agents/skills/super-dev/SKILL.md`；官方用户级 Skill `~/.agents/skills/super-dev/SKILL.md` 仍会安装，`CODEX_HOME/AGENTS.md`（默认 `~/.codex/AGENTS.md`）改为显式 `--with-user-surfaces` 时才写入。
5. 同时会额外生成可选的 repo plugin 增强层：`.agents/plugins/marketplace.json` + `plugins/super-dev-codex/.codex-plugin/plugin.json`，让 Codex App/Desktop 在 AGENTS + Skills 之外还能看到更完整的本地 plugin 面。
6. 历史安装会在升级时自动迁移到统一的 `super-dev` 命名。
7. 如果旧会话没加载新 Skill，重启 `codex` 再试。
8. 无论使用 `/super-dev`、`$super-dev` 还是 `super-dev:`，都必须进入同一条 Super Dev 流程；长流程里继续修改、补充、确认或恢复时，优先沿用当前入口面。

#### 3. Gemini CLI

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 Gemini CLI 会话后触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. 官方主面已经收口到 `GEMINI.md + settings + custom commands`；项目内优先检查 `GEMINI.md`、可选 `.gemini/settings.json` 和 `.gemini/commands/*.toml`。
2. `/super-dev` 是 Super Dev 注入后的自定义命令面，不是 Gemini CLI 自带内建命令；若命令未刷新，优先重开当前 Gemini CLI 会话。
3. `~/.gemini/skills/` 只作为兼容增强面保留，不再当默认主协议面。
4. 优先在同一会话中完成 research -> 三文档 -> 用户确认 -> Spec -> 前端运行验证 -> 后端/交付；若宿主支持联网，先让它完成同类产品研究。

#### 4. OpenCode

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 OpenCode 会话后触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. 按 CLI slash 模式使用。
2. 若你使用全局命令目录，也建议保留项目级接入文件。

#### 5. Kiro CLI

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 Kiro CLI 会话后触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：是

补充说明：
1. Kiro CLI 当前优先使用宿主已暴露的 `/super-dev` 入口；如果当前会话只接受自然语言，再回退到 `super-dev: 需求`。
2. 官方接入面是 `AGENTS.md` + `.kiro/steering/super-dev.md` + `.kiro/skills/super-dev/SKILL.md`；全局增强面是 `~/.kiro/steering/super-dev.md` 与 `~/.kiro/skills/super-dev/SKILL.md`。
3. 完成接入后建议重开 Kiro CLI，让 steering 上下文与 skills 在新会话里一起生效。

#### 6. Cursor CLI

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 Cursor CLI 当前会话后触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 适合终端内连续执行研究、文档和编码。
2. 官方项目上下文面是项目根 `AGENTS.md` 与 `.cursor/rules/`；根 `CLAUDE.md` 只继续作为兼容上下文，不再当默认主协议面。
3. 若项目上下文或规则面未刷新，可重开一次 Cursor CLI 会话；恢复已有流程时优先使用 Cursor CLI 自身的会话连续性。

#### 7. Qoder CLI

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 Qoder CLI 会话后触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. 适合命令行流水线开发。
2. 若 slash 未生效，先确认 `AGENTS.md`、`.qoder/commands/super-dev.md` 已生成，并检查 `.qoder/rules/` 目录是否存在。
3. 官方接入面已切到 `AGENTS.md` + `.qoder/rules/super-dev.md` + `.qoder/commands/super-dev.md` + `.qoder/skills/` / `~/.qoder/AGENTS.md` + `~/.qoder/commands/` + `~/.qoder/skills/`；`.qoder/agents/` 继续只作为增强面。

#### 8. Copilot CLI

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 Copilot CLI 会话后触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 官方主面是 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/skills/` 与 `.github/agents/`；显式启用用户级 surface 时，再确认 `~/.copilot/skills/`、`~/.copilot/agents/` 与 `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` 也已被会话读取。
2. 当前使用 `super-dev: 你的需求` 作为主触发方式，不走项目级 `/super-dev` 自定义 slash。
3. 若维护者需要排障或补齐接入面，再用 `super-dev doctor --host copilot-cli` 做确认。

#### 9. CodeBuddy CLI

安装：
```bash
super-dev
```

触发位置：
在项目目录启动 CodeBuddy CLI 会话后触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. 在当前 CLI 会话中直接输入即可。
2. 官方主面是 `CODEBUDDY.md` + `.codebuddy/rules/` + `.codebuddy/commands/` + `.codebuddy/skills/` + `.codebuddy/agents/`，并补充 `~/.codebuddy/CODEBUDDY.md`。
3. 如果会话已提前打开，建议重新加载项目规则后再试。
4. 黑客松/比赛场景优先使用 `/super-dev-seeai`，让宿主按半小时节奏压缩 research、三文档、Spec 和一体化开发。

#### 10. Antigravity

安装：
```bash
super-dev
```

触发位置：
打开 Antigravity 的 Agent Chat / Prompt 面板，并确保当前工作区就是目标项目。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：是

补充说明：
1. Antigravity 当前按 `GEMINI.md + custom commands` 模式接入，`.agent/workflows` 继续作为推荐增强面。
2. 接入会写入项目级 `GEMINI.md`、`.gemini/commands/super-dev.toml`、`.agent/workflows/super-dev.md`。
3. 默认只写项目级 `GEMINI.md` 与项目内命令面；用户级 `~/.gemini/GEMINI.md` 与 `~/.gemini/commands/` 仅在显式 `--with-user-surfaces` 时写入，`~/.gemini/skills/` 继续只作为兼容增强层。
4. 完成接入后请重开 Antigravity 或至少新开一个 Agent Chat，再输入 `/super-dev 你的需求`。

#### 11. Cursor

安装：
```bash
super-dev
```

触发位置：
打开 Cursor 的 Agent Chat，并确保当前工作区就是目标项目。

触发命令：
```text
/super-dev 你的需求
```
比赛模式：
```text
/super-dev-seeai 比赛需求
```

接入后是否需要重启：否

补充说明：
1. 建议固定在同一个 Agent Chat 会话里完成整条流水线。
2. 如果项目规则没加载，先重新打开工作区或重新发起聊天。

#### 12. Windsurf

安装：
```bash
super-dev
```

触发位置：
打开 Windsurf 的 Agent Chat / Workflow 入口，在项目上下文内触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. 当前按 `AGENTS.md + rules + workflow + skills` 模式适配。
2. 更适合在同一个 Workflow 里连续完成研究、文档、Spec 和编码。
3. 官方文档公开 `AGENTS.md`、`.windsurf/workflows/` 与 `.windsurf/skills/`；仓库继续把 `.windsurf/rules/` 保留为项目约束面。

#### 13. Kiro

安装：
```bash
super-dev
```

触发位置：
打开 Kiro IDE 的 Agent Chat / AI 面板，在项目上下文内触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：是

补充说明：
1. Kiro IDE 当前优先使用宿主已暴露的 `/super-dev` 入口；如果当前会话只接受自然语言，再回退到 `super-dev: 你的需求`。
2. 接入会写入项目级 `AGENTS.md`、`.kiro/steering/super-dev.md`、`.kiro/skills/super-dev/SKILL.md`，并补充全局 `~/.kiro/steering/super-dev.md` 与 `~/.kiro/skills/super-dev/SKILL.md`；旧 `~/.kiro/steering/AGENTS.md` 仍作为兼容面保留。
3. 如果 steering 或 skills 未加载，先重开项目窗口或新开一个 Agent Chat。

#### 14. Qoder

安装：
```bash
super-dev
```

触发位置：
打开 Qoder IDE 的 Agent Chat，在当前项目内触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. Qoder IDE 当前优先使用项目级 `AGENTS.md + commands + rules + skills` 模式，直接在 Agent Chat 输入 `/super-dev 你的需求`。
2. 若新增命令未出现，先确认 `AGENTS.md`、`.qoder/commands/super-dev.md` 已生成，并检查 `.qoder/rules/super-dev.md` 是否存在，再重新打开项目或新开一个 Agent Chat。
3. 官方接入面已切到 `AGENTS.md` + `.qoder/rules/super-dev.md` + `.qoder/commands/super-dev.md` + `.qoder/skills/` / `~/.qoder/AGENTS.md` + `~/.qoder/commands/` + `~/.qoder/skills/`；`.qoder/agents/` 继续只作为增强面。

#### 15. Trae IDE

安装：
```bash
super-dev
```

触发位置：
打开 Trae IDE 的 Agent Chat，在当前项目上下文内直接触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. Trae 当前使用 `super-dev: 你的需求` 作为主触发方式。
2. 默认只写项目级 `.trae/project_rules.md`、`.trae/rules.md`；用户级 `~/.trae/user_rules.md`、`~/.trae/rules.md` 改成显式 `--with-user-surfaces` 才写入；如果检测到兼容技能目录，也会增强安装 `~/.trae/skills/super-dev/SKILL.md`。
3. 完成接入后建议重开 Trae 或至少新开一个 Agent Chat，使规则生效；如果兼容 Skill 已安装，也会一起生效。
4. 随后按 `output/*` 与 `.super-dev/changes/*/tasks.md` 推进开发。

#### 16. CodeBuddy

安装：
```bash
super-dev
```

触发位置：
打开 CodeBuddy 的 Agent Chat，在项目上下文内触发。

触发命令：
```text
/super-dev 你的需求
```

接入后是否需要重启：否

补充说明：
1. 建议在项目级 Agent Chat 中使用，不要脱离项目上下文。
2. 先让宿主完成 research，再继续文档和编码。
3. 当前按 `CODEBUDDY.md` + `.codebuddy/rules/super-dev/RULE.mdc` + `.codebuddy/commands/` + `.codebuddy/agents/` + `.codebuddy/skills/` 接入。
4. 比赛场景建议固定在同一个 Agent Chat，会比频繁切换子会话更稳。

#### 17. Copilot (VS Code)

安装：
```bash
super-dev
```

触发位置：
打开 VS Code 的 Copilot Chat 面板，在项目上下文内触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 当前使用 `super-dev: 你的需求` 作为主触发方式，通过项目规则文件驱动流程。
2. 若维护者需要排障或核对接入面，再用 `super-dev doctor --host vscode-copilot` 做确认。
3. 在同一个 Copilot Chat 会话里完成整条流水线效果最佳。

#### 18. Roo Code

安装：
```bash
super-dev
```

触发位置：
打开 Roo Code 的 Agent Chat / AI 面板，在项目上下文内触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 当前使用 `super-dev: 你的需求` 作为主触发方式。
2. 默认写入项目级规则文件；若宿主提供官方用户级 Skill 目录，会同步增强安装 Skill，如需用户级协议/命令面再显式启用 `--with-user-surfaces`。
3. 若维护者需要排障或核对接入面，再用 `super-dev doctor --host roo-code` 做确认。

#### 19. Kilo Code

安装：
```bash
super-dev
```

触发位置：
打开 Kilo Code 的 Agent Chat / AI 面板，在项目上下文内触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 当前使用 `super-dev: 你的需求` 作为主触发方式。
2. 默认写入项目级规则文件；若宿主提供官方用户级 Skill 目录，会同步增强安装 Skill，如需用户级协议/命令面再显式启用 `--with-user-surfaces`。
3. 如果规则未加载，先重开项目窗口或新开一个 Agent Chat。

#### 20. Cline

安装：
```bash
super-dev
```

触发位置：
打开 Cline 的 Agent Chat 面板，在项目上下文内触发。

触发命令：
```text
super-dev: 你的需求
```

接入后是否需要重启：否

补充说明：
1. 当前使用 `super-dev: 你的需求` 作为主触发方式。
2. 接入会写入项目级 `.clinerules/` 目录下的规则文件。
3. 若维护者需要排障或核对接入面，再用 `super-dev doctor --host cline` 做确认。
4. 在同一个 Agent Chat 会话里完成整条流水线效果最佳。

#### 21. Droid CLI

Droid CLI 走 Factory 官方宿主模型，无需额外插件包。核心接入面是：

- 项目根 `AGENTS.md`
- `.factory/rules/super-dev.md`
- `.factory/skills/super-dev/SKILL.md`
- `.factory/skills/super-dev-seeai/SKILL.md`
- 兼容增强面：`.factory/commands/super-dev.md`、`.factory/commands/super-dev-seeai.md`
- 用户级 `~/.factory/AGENTS.md` / `~/.factory/commands/` / `~/.factory/skills/`（默认不写；仅在显式 `--with-user-surfaces` 时补齐）

安装：
```bash
super-dev
```

在安装器里选择 `Droid CLI` 后，回到当前项目的 Droid 会话触发。

触发命令：
```text
/super-dev 你的需求
```
回退入口：
```text
super-dev: 你的需求
```
比赛模式：
```text
/super-dev-seeai 比赛需求
```
需要 headless 续跑时：
```bash
droid exec --session-id <id> "continue with next steps"
```

补充说明：
1. Droid CLI 需要在目标项目目录里启动，让当前 session 先读取项目根 `AGENTS.md`。
2. `.factory/rules/` 与 `.factory/skills/` 是主协议面；`.factory/commands/` 继续作为兼容增强面承担 slash 触发补充，不再需要额外插件。
3. 比赛场景优先使用 `/super-dev-seeai`；如果 slash 面板刷新慢，再回退到 `super-dev-seeai:`。
4. 恢复已有流程时优先保持同一 Droid session，不要重新开题。

---

## 关键文档

- [文档总览](docs/README.md)
- [快速开始](docs/QUICKSTART.md)
- [安装方式](docs/INSTALL_OPTIONS.md)
- [宿主使用指南](docs/HOST_USAGE_GUIDE.md)
- [宿主能力审计](docs/HOST_CAPABILITY_AUDIT.md)
- [宿主运行时验收矩阵](docs/HOST_RUNTIME_VALIDATION.md)
- [宿主接入面说明](docs/HOST_INSTALL_SURFACES.md)
- [工作流指南](docs/WORKFLOW_GUIDE.md)
- [集成指南](docs/INTEGRATION_GUIDE.md)
- [产品审查](docs/PRODUCT_AUDIT.md)

执行原则：

- 宿主负责"写代码"
- `Super Dev` 负责"把开发过程做对、做全、可审计"

---

## 关注我们

<div align="center">

<img src="super-dev-website/public/logo.png" alt="微信公众号" width="100%">

</div>

---

## License

[MIT](LICENSE)
