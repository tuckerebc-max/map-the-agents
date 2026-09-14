# 书籍大纲：驾驭工程 — 从 Claude Code 源码到 AI 编码最佳实践

## 背景

基于对 Claude Code v2.1.88 的 1,902 个 TypeScript 源文件的逆向工程，我们提取了一整套驾驭工程（Harness Engineering）模式、上下文管理策略和 AI 编码最佳实践。本书将这些发现组织成一本面向 AI Agent 构建者的实战指南。

目标读者：希望理解顶级 AI 编码产品底层运作机制的 AI 工程师和 Agent 开发者。

---

## 第一篇：架构 — Claude Code 如何运作

### 第1章：AI 编码 Agent 的完整技术栈

- 技术栈概览：TypeScript + React Ink + Bun
- 入口点分析（`main.tsx`）：并行预取、延迟导入、Feature Flag
- 三层架构：应用层（TS）→ 运行时（Bun/Zig）→ 外部依赖（npm/JSC）
- 为什么 "on distribution" 很重要：模型编写自己的工具
- 通过 `bun:bundle` 的 `feature()` 实现构建时死代码消除
- 89 个 Feature Flag 全景：从 `ABLATION_BASELINE` 到 `WORKFLOW_SCRIPTS`

### 第2章：工具系统 — 40+ 个工具作为模型的双手

- `Tool.ts` 接口契约：name、description、prompt、inputSchema、call、checkPermissions、validateInput
- `buildTool()` 工厂函数和失败关闭默认值（`isConcurrencySafe: false`、`isReadOnly: false`）
- 工具注册管线（`tools.ts`）：基于 Feature Flag 的条件加载
- 三阶段渲染：renderToolUseMessage → renderToolUseProgressMessage → renderToolResultMessage
- 工具结果大小预算：单工具 `maxResultSizeChars`、单消息 `MAX_TOOL_RESULTS_PER_MESSAGE_CHARS = 200K`

### 第3章：Agent Loop — 从用户输入到模型响应的完整生命周期

- `queryLoop()` 状态机：`State` 类型的 7 个可变字段（messages、toolUseContext、autoCompactTracking、maxOutputTokensRecoveryCount...）
- 循环转换类型（`Continue`）：工具调用继续、max_output_tokens 恢复（最多 3 次）、token budget 继续、reactive compact
- 单次迭代的完整流程：context collapse → autocompact → API 调用 → 流式响应 → 工具执行 → stop hooks → 继续判定
- 消息标准化管线：`normalizeMessagesForAPI` → `ensureToolResultPairing` → `stripAdvisorBlocks` → `stripExcessMediaItems`
- `prependUserContext` vs `appendSystemContext`：上下文注入的位置和时序
- 中止/重试/降级：`FallbackTriggeredError`、对话中途切换模型、`attemptWithFallback` 循环

### 第4章：工具执行编排 — 权限、并发、流式与中断

- `toolOrchestration.ts` 的 `runTools()`：`partitionToolCalls` 将工具调用分为并发安全批次和串行批次
- `isConcurrencySafe` 判定逻辑：只读工具可并发，写入工具必须串行
- `toolExecution.ts` 单工具生命周期：validateInput → checkPermissions → autoClassifier → call → postToolUse hooks
- `StreamingToolExecutor`：流式工具执行器，边生成边处理
- 权限决策链：工具自身 checkPermissions → 通用权限规则 → YOLO 分类器 → 用户提示
- 工具结果处理：`applyToolResultBudget` → `persistLargeToolResult` → preview 生成
- Stop hooks：工具执行后的中断点，允许用户或系统在工具间插入控制

---

## 第二篇：提示工程 — 系统提示词作为控制面

### 第5章：系统提示词架构

- 分段式组合：`systemPromptSection()` 的记忆化和缓存感知
- 静态与动态边界：`SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 标记
- 缓存优化契约：边界前 = `scope: 'global'`（跨组织可缓存），边界后 = 每会话
- `splitSysPromptPrefix()` 的三条代码路径（MCP 存在时、全局缓存+边界、默认）
- `DANGEROUS_uncachedSystemPromptSection()` 及其使用时机（MCP 连接/断开）

### 第6章：通过提示词引导行为

- **极简主义指令**："三行重复代码优于过早抽象"、"不要添加超出要求的功能"
- **渐进式升级**："切换策略前先诊断原因，不要盲目重试，也不要一次失败就放弃"
- **可逆性意识**："三思而后行" — 高风险操作确认框架
- **工具偏好引导**："使用 Grep（而非 grep 或 rg）" — 通过工具描述重定向
- **Agent 委托指引**：fork vs. 全新 agent、"不要偷看 fork 输出"、"不要竞争"
- **输出效率**：内部员工的散文式沟通风格 vs. 外部用户的精简要点
- **数值锚定**："工具调用间的文字保持在 ≤25 词" — 1.2% 输出 token 削减

### 第7章：模型特定调优与 A/B 测试

- `@[MODEL LAUNCH]` 注解模式：标记模型敏感代码以便发布时扫描
- Capybara v8 的缓解措施：过度注释、虚假声明（29-30% 虚假声明率）、主动性、彻底性
- `USER_TYPE === 'ant'` 门控作为 A/B 测试暂存："在外部用户上验证后解除门控"
- 卧底模式（Undercover）：在系统提示词中压制模型名称、ID 和战略信息
- GrowthBook 集成：`tengu_*` Feature Flag、`_CACHED_MAY_BE_STALE` vs `_CACHED_WITH_REFRESH`
- 知识截止日期映射：按模型注入日期字符串到环境上下文

### 第8章：工具提示词作为微型驾驭器

- **BashTool 提示词**：Git 安全协议（绝不跳过 hooks、绝不 amend、优先指定文件 `git add`）、沙箱配置以 JSON 内联、工具偏好区域、后台任务说明
- **FileEditTool 提示词**："编辑前必须先读取"通过工具报错强制执行、最小唯一 `old_string` 提示（仅内部）、replace_all 用于重命名
- **FileReadTool 提示词**：默认 2000 行、offset/limit 渐进式读取、PDF 页码范围
- **GrepTool 提示词**："始终使用 Grep，绝不在 Bash 中调用 grep"、ripgrep 语法说明、多行匹配可选
- **AgentTool 提示词**：动态 agent 列表（内联 vs. 附件以保持缓存稳定性）、fork 指引、隔离模式
- **SkillTool 提示词**：预算约束的技能列表（上下文窗口的 1%）、三级截断级联、内置技能优先

---

## 第三篇：上下文管理 — 200K Token 竞技场

### 第9章：自动压缩 — 上下文何时以及如何被压缩

- 阈值计算：`contextWindow - MAX_OUTPUT_TOKENS_FOR_SUMMARY(20K) - AUTOCOMPACT_BUFFER(13K)`
- 环境变量覆盖：`CLAUDE_CODE_AUTO_COMPACT_WINDOW`、`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`
- 熔断器：`MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3`（数据：1,279 个会话出现 50+ 次连续失败，每天浪费约 250K 次 API 调用）
- 压缩提示词剖析：9 段模板、`<analysis>` 草稿块（压缩后移除）、时间顺序强调
- 三种提示词变体：BASE（全对话）、PARTIAL（尾部）、PARTIAL_UP_TO（前缀保留）
- Prompt-too-long 重试：丢弃最旧的 API 轮次组、回退丢弃 20%、`PTL_RETRY_MARKER`

### 第10章：压缩后的文件状态保留

- 压缩前快照：`cacheToObject(context.readFileState)` 然后清空
- 压缩后恢复：`POST_COMPACT_MAX_FILES_TO_RESTORE = 5`、单文件上限 5K token、总预算 50K token
- 技能重注入：单技能 5K token 上限、总计 25K 预算、"技能文件顶部的指令通常是关键部分"
- 不重注入的内容：`sentSkillNames`（节省 4K token，模型仍持有 SkillTool schema）
- Delta 附件：延迟工具、agent 列表、MCP 指令在压缩后重新宣告

### 第11章：微压缩 — 精准上下文修剪

- 基于时间的微压缩：间隔阈值触发旧工具结果清理，保留最近 N 个
- 缓存微压缩（API 原生）：`cache_edits` 块删除工具结果但不使缓存前缀失效
- `consumePendingCacheEdits()` / `getPinnedCacheEdits()`：编辑生命周期管理
- 可压缩工具集：FileRead、Bash、Grep、Glob、WebSearch、WebFetch、FileEdit、FileWrite
- `notifyCacheDeletion()` / `notifyCompaction()`：防止缓存中断误报

### 第12章：Token 预算策略

- 工具结果持久化：`DEFAULT_MAX_RESULT_SIZE_CHARS = 50K` → 磁盘 + 预览消息
- 单消息预算：`MAX_TOOL_RESULTS_PER_MESSAGE_CHARS = 200K`（防止 N 个并行工具洪泛）
- Token 计数：规范方式（来自 API usage）vs. 粗略估算（4 字节/token，JSON 为 2）
- 并行工具调用 token 计数：向后遍历以捕获所有交错的 tool_results
- 图片/文档估算：保守 2000 token（真实公式：width*height/750）
- 文件类型感知估算：JSON 按 2 字节/token 防止对密集格式的低估

---

## 第四篇：提示词缓存 — 隐藏的成本优化器

### 第13章：缓存架构与断点设计

- Anthropic API 提示词缓存：前缀匹配、`cache_control: { type: 'ephemeral' }` 标记
- 三级缓存范围：`global`（跨组织）、`org`（单组织）、`null`（不缓存）
- 缓存 TTL 层级：默认 5 分钟、符合条件的用户 1 小时
- `should1hCacheTTL()`：锁存的会话稳定资格检查
- Beta Header 锁存：`afkModeHeaderLatched`、`fastModeHeaderLatched`、`cacheEditingHeaderLatched` — "一旦发送就持续发送，避免浪费约 50-70K token 的缓存"

### 第14章：缓存中断检测系统

- 两阶段检测：`recordPromptState()`（调用前）→ `checkResponseForCacheBreak()`（调用后）
- `PreviousState` 追踪：15+ 字段，包括 systemHash、toolsHash、cacheControlHash、perToolHashes、betas、effortValue
- 中断解释引擎：识别哪个字段变化，生成人类可读原因
- TTL 过期检测：时间间隔 > 5分钟 或 > 1小时 → "可能是 TTL 过期"
- 服务端归因："当所有客户端标志为 false 且间隔在 TTL 内时，约 90% 的中断是服务端原因"
- Diff 文件生成：`createPatch()` 生成前后提示词状态对比

### 第15章：缓存优化模式

- 日期记忆化：`getSessionStartDate()` 只捕获一次，避免午夜缓存失效
- 月度粒度：工具提示词中的 `getLocalMonthYear()` 最小化缓存失效
- Agent 列表改为附件：从内联提示词（占全球 `cache_creation` token 的 10.2%）移至 `system-reminder` 消息
- 技能列表预算：上下文窗口的 1%，级联截断防止无限增长
- `$TMPDIR` 占位符：标准化每用户临时路径以实现跨用户缓存共享
- 条件性段落省略：功能禁用时 → 段落从提示词中消失（而非"功能 X 已禁用"）
- 工具 Schema 缓存：`getToolSchemaCache()` 每会话计算一次，防止 GrowthBook Flag 切换导致序列化 schema 变动

---

## 第五篇：安全与权限 — 纵深防御

### 第16章：权限系统

- 权限模式：`default` → `acceptEdits` → `plan` → `bypassPermissions` → `auto` → `dontAsk`
- 权限规则匹配：精确匹配、前缀匹配（`npm:*`）、通配符（`git add *`）
- 验证 → 权限 → 分类 管线：失败关闭的执行顺序
- 危险模式检测：`isDangerousBashPermission()` 阻止对解释器的工具级别放行
- UNC 路径 NTLM 泄漏防护：对 `\\` 路径跳过 `fs.existsSync()`

### 第17章：YOLO 分类器

- 二次 Claude API 调用用于自动批准决策
- 安全白名单：只读工具完全跳过分类器
- 分类器输出：`{ thinking, shouldBlock, reason }`，结构化输出 Schema
- 拒绝追踪：连续 3 次或总计 20 次拒绝 → 回退到用户提示
- 模板系统：外部用户与 Anthropic 内部用户使用不同提示词
- 调试基础设施：`CLAUDE_CODE_DUMP_AUTO_MODE=1` 导出分类器请求/响应

### 第18章：Hooks — 用户自定义拦截点

- Hook 事件类型：PreToolUse、PostToolUse、PermissionRequest、SessionStart/End、FileChanged 等
- 执行模型：异步生成器、超时处理（默认 10 分钟、SessionEnd 为 1.5 秒）
- 信任门控：交互模式下所有 Hook 都需要信任对话框确认
- 退出码语义：0 = 允许、2 = 阻塞错误 → 入队为任务通知
- 配置快照追踪：检测并响应 settings.json 变更

### 第19章：CLAUDE.md — 用户指令作为覆盖层

- 加载顺序：托管 → 用户 → 项目 → 本地（优先级递增）
- `@include` 指令：传递性文件包含，防止循环引用
- 前置元数据 `paths:` 范围限定：将指令限制在匹配的文件模式
- HTML 注释剥离：`<!-- -->` 中的作者注释在注入前移除
- 注入提示词："这些指令覆盖任何默认行为，你必须严格遵守"
- 大小预算：建议每文件 40K 字符

---

## 第六篇：高级子系统

### 第20章：Agent 集群与多 Agent 编排

- `AgentTool`：通过独立的 `AsyncLocalStorage` 上下文生成子 agent
- Fork 模式：后台执行、共享提示词缓存、"不要偷看输出"
- 协调者模式（`COORDINATOR_MODE`）：多 Worker 编排，任务分配与验证
- 队友 Agent：进程内集群协作、`TeammateAgentContext`、`TeamCreateTool`/`TeamDeleteTool`
- 验证 Agent：`PASS/FAIL/PARTIAL` 判定附带证据（仅内部 A/B 测试）
- Agent 间通信：`SendMessageTool`、`UDS_INBOX` Unix Domain Socket 消息传递

### 第21章：Effort、Fast Mode 与 Thinking

- Effort 级别：low/medium/high/max、优先级链（环境变量 → 应用状态 → 模型默认 → 兜底）
- Fast Mode：Opus 4.6 加速输出、组织状态缓存、冷却管理（限速/过载）
- Thinking 配置：adaptive vs. enabled（预算）vs. disabled
- Ultrathink：关键词触发检测、模型支持门控
- 按模型默认值：Opus + Pro → medium effort，Max/Team Premium 可配置

### 第22章：技能系统 — 从内置到用户自定义

- 技能的本质：可调用的提示词模板，通过 `SkillTool` 注入对话
- 内置技能清单：`skills/bundled/` 下的 batch、loop、scheduleRemoteAgents 等
- 用户自定义技能：`loadSkillsDir.ts` 的发现和加载机制、`.claude/skills/` 目录结构
- MCP 技能桥接：`mcpSkillBuilders.ts` 将 MCP server 能力转化为可调用技能
- 技能搜索系统：`EXPERIMENTAL_SKILL_SEARCH`、本地索引构建、关键词匹配与评分
- 技能生命周期：`RUN_SKILL_GENERATOR`（生成）、`SKILL_IMPROVEMENT`（改进）、`skillChangeDetector`（变更检测）
- 预算约束的技能列表：上下文窗口的 1%、三级截断级联、内置技能优先保留描述
- 技能与 Hook 的交互：技能作为 Hook 触发源、技能内的 slash command 执行

### 第23章：未发布功能管线 — 89 个 Feature Flag 背后的路线图

- KAIROS 助手模式：后台自主 agent、`<tick>` 唤醒机制、autoDream 记忆整理、push notification
- PROACTIVE 模式：自主工作、terminal focus 感知、sleep/wake 循环
- VOICE_MODE：流式语音转文字、push-to-talk 键绑定
- WEB_BROWSER_TOOL：Bun WebView 集成（非 Playwright）
- BRIDGE_MODE + DAEMON：远程控制服务器、CCR 镜像
- COORDINATOR_MODE 的完整编排：worker 分配、验证、汇报
- 从 feature flag 看产品路线图：哪些接近发布、哪些仍在实验

---

## 第七篇：AI Agent 构建者的经验教训

### 第24章：跨会话记忆 — 从遗忘到持久学习

- Memdir 架构：MEMORY.md 索引 + 主题文件，200 行 / 25KB 截断策略
- Extract Memories：fork agent 在查询结束时自动提取，权限隔离
- Session Memory：滚动会话摘要（10K 初始化 / 5K 更新间隔 / 3+ 工具调用）
- Transcript Persistence：JSONL 增量追加，会话恢复重建
- Agent Memory：user/project/local 三作用域，VCS 快照同步
- Auto-Dream：四层门控（Master/Time/Session/Lock），PID 锁，四阶段整合提示词
- 模式：多层记忆架构、后台 fork agent 提取、文件 mtime 即状态、预算约束注入、互补频率设计

### 第25章：驾驭工程原则

1. **提示词即控制面**：通过系统提示词段落引导行为，而非代码限制
2. **缓存感知设计是刚需**：每次提示词变更都有以 cache_creation token 计量的成本
3. **失败关闭，显式开放**：工具默认为不安全/不可并发，必须显式声明安全
4. **A/B 测试一切**：ant-only 门控作为暂存，GrowthBook 用于运行时实验
5. **先观察再修复**：`promptCacheBreakDetection.ts` 作为仪表盘驱动调试的典范
6. **锁存以求稳定**：一旦进入某状态就不再摇摆（beta header、缓存 TTL 资格）

### 第26章：上下文管理作为核心能力

1. **为一切设定预算**：工具结果、文件读取、技能列表、agent 描述都有 token 预算
2. **保留重要内容**：压缩后最多 5 个最近文件、50K 总预算
3. **告知而非隐藏**：截断通过输出元数据报告，模型可分页
4. **熔断失控循环**：连续 3 次失败 → 停止尝试
5. **保守估算**：JSON 按 2 字节/token、图片按 2K token

### 第27章：生产级 AI 编码模式

1. **编辑前先读取**：通过工具报错强制执行，而非仅靠提示词指令
2. **渐进式自主**：从手动到全自动的权限模式，带分类器回退
3. **防御性 Git**：绝不跳过 hooks、绝不 amend（创建新提交）、绝不 force-push
4. **结构化验证**：运行测试 → 检查输出 → 如实报告（不伪造绿色结果）
5. **范围匹配响应**：对 X 的授权不延伸到 Y
6. **工具级提示词优于通用指令**：每个工具携带自己的行为驾驭器

### 第28章：Claude Code 的不足之处（以及你能修复什么）

1. **缓存脆弱性**：分散的注入点制造缓存中断风险 — 应集中构建
2. **压缩信息丢失**：9 段摘要模板无法保留所有推理链
3. **Grep 不是 AST**：文本搜索遗漏动态导入、re-export、字符串引用
4. **静默截断**：50K 工具结果阈值 → 写入磁盘 + 预览，但模型可能不会重新读取
5. **Feature Flag 复杂性**：89 个 flag、锁存状态和构建时门控产生涌现行为
6. **Agent Loop 无法自省**：模型不知道自己处于恢复循环的第几次重试

### 第29章：可观测性工程 — 从 logEvent 到生产级遥测

- 5 层遥测架构：事件入口 → 路由分发 → PII 安全 → 投递韧性 → 远程控制
- 队列-附着模式：`logEvent()` 零依赖设计，事件先入队后异步排空
- PII 安全：`never` 类型标记强制显式验证，`_PROTO_*` 双路路由
- 1P Exporter（807 行）：OTel BatchLogRecordProcessor + 自定义韧性层
  - 批次分片 + 短路逻辑 + 二次退避 + 401 降级 + 磁盘持久化
- Datadog：策展式允许列表（30+ 事件）、用户分桶、15 秒批刷新
- API 三事件模型：query/success/error + TTFT/TTLT 性能指标
- 调试三通道：debug（可能含 PII）/ diagLogs（PII-free）/ errorLogSink（ant-only）
- 分布式追踪：OTel 三级 span（interaction/llm/tool）+ Perfetto 可视化
- 优雅关闭：级联超时（终端→清理→hooks→analytics→forceExit），5 秒失败保险
- 成本追踪：USD/token/行变更，会话间持久化

---

## 附录

### 附录 A：关键文件索引

| 文件 | 职责 |
|------|------|
| `main.tsx` | CLI 入口点，并行预取 |
| `Tool.ts` | 工具接口契约 |
| `tools.ts` | 工具注册，Feature Flag 条件加载 |
| `query.ts` | Agent Loop 主循环，queryLoop 状态机 |
| `services/tools/toolOrchestration.ts` | 工具执行编排，并发分区 |
| `services/tools/toolExecution.ts` | 单工具执行生命周期 |
| `services/tools/StreamingToolExecutor.ts` | 流式工具执行器 |
| `constants/prompts.ts` | 系统提示词构建 |
| `constants/systemPromptSections.ts` | 段落注册表，带缓存控制 |
| `services/api/claude.ts` | API 调用构建，缓存断点放置 |
| `services/api/promptCacheBreakDetection.ts` | 缓存中断检测系统 |
| `services/compact/compact.ts` | 压缩编排 |
| `services/compact/autoCompact.ts` | 自动压缩阈值与触发器 |
| `services/compact/microCompact.ts` | 精准上下文修剪 |
| `utils/api.ts` | `splitSysPromptPrefix()`、工具 Schema 构建 |
| `utils/toolResultStorage.ts` | 大结果持久化 |
| `utils/claudemd.ts` | CLAUDE.md 加载与注入 |
| `utils/permissions/yoloClassifier.ts` | 自动模式分类器 |
| `skills/bundled/` | 内置技能目录 |
| `tools/SkillTool/` | 技能工具实现 |
| `skills/loadSkillsDir.ts` | 用户自定义技能发现 |
| `skills/mcpSkillBuilders.ts` | MCP 到技能桥接 |

### 附录 B：环境变量参考

| 变量 | 效果 |
|------|------|
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | 覆盖上下文窗口大小 |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 以百分比覆盖自动压缩阈值 |
| `CLAUDE_CODE_EFFORT_LEVEL` | 覆盖 effort 级别（low/medium/high/max/auto/unset） |
| `CLAUDE_CODE_DISABLE_FAST_MODE` | 禁用 fast mode |
| `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` | 覆盖文件读取 token 限制 |
| `CLAUDE_CODE_SIMPLE` | 最小系统提示词模式 |
| `CLAUDE_CODE_DUMP_AUTO_MODE` | 导出 YOLO 分类器请求/响应 |
| `DISABLE_AUTO_COMPACT` | 禁用自动压缩 |
| `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY` | 覆盖工具并发上限（默认 10） |
| `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE` | 覆盖上下文硬限制 |

### 附录 C：术语表

| 术语 | 定义 |
|------|------|
| 驾驭工程（Harness Engineering） | 通过提示词、工具和配置（而非代码逻辑）引导 AI 模型行为的实践 |
| Agent Loop | AI agent 的核心执行循环：接收输入 → 调用模型 → 执行工具 → 判断是否继续 |
| 提示词缓存（Prompt Cache） | Anthropic API 特性，缓存消息前缀以减少重复 token 处理 |
| 压缩（Compaction） | 总结对话历史以释放上下文窗口空间 |
| 微压缩（Microcompact） | 精准移除特定工具结果，而非完整压缩 |
| 锁存（Latch） | 一旦进入即保持稳定的会话级状态，防止缓存振荡 |
| Feature Flag（tengu_*） | 通过 GrowthBook 运行时配置的实验门控 |
| DCE（死代码消除） | Bun 的 `feature()` 实现编译时移除门控代码 |
| 技能（Skill） | 可调用的提示词模板，通过 SkillTool 注入对话上下文 |
| 并发分区（Partition） | 将工具调用分为可并行和必须串行的批次 |

### 附录 D：89 个 Feature Flag 完整清单

（按字母顺序列出所有 feature flag 及其功能分类：基础设施/用户功能/实验/遥测）
