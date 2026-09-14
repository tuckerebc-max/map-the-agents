# Claude Code v2.1.88 子系统锚点索引

> 用于在新版本的 minified bundle 中定位各子系统。
> 锚点是稳定的字符串常量，在不同版本中通常保持一致。

## 使用方法

```bash
# 在 cli.js 中搜索锚点
grep -c 'tengu_api_query' cli.js        # 确认存在
grep -o 'tengu_api_query' cli.js         # 计数出现次数
grep -b 'tengu_api_query' cli.js         # 获取字节偏移
```

---

## 分析/遥测（Analytics & Telemetry）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_init` | main.tsx | 应用初始化事件 |
| 事件名 | `tengu_exit` | setup.ts | 应用退出事件 |
| 事件名 | `tengu_startup_telemetry` | main.tsx | 启动遥测事件 |
| OTel 作用域 | `com.anthropic.claude_code.events` | services/analytics/firstPartyEventLogger.ts | 1P 事件日志作用域 |
| OTel 计量器 | `com.anthropic.claude_code` | utils/telemetry/instrumentation.ts | 主计量器名 |
| OTel 跟踪器 | `com.anthropic.claude_code.tracing` | utils/telemetry/sessionTracing.ts | Span tracer |
| API 端点 | `/api/event_logging/batch` | services/analytics/firstPartyEventLoggingExporter.ts | 事件批量导出 |
| Datadog 端点 | `https://http-intake.logs.us5.datadoghq.com/api/v2/logs` | services/analytics/datadog.ts | Datadog 日志摄取 |
| Datadog Token | `pubbbf48e6d78dae54bceaa4acf463299bf` | services/analytics/datadog.ts | 客户端 token |
| GrowthBook | `tengu_event_sampling_config` | services/analytics/firstPartyEventLogger.ts | 事件采样配置 |
| GrowthBook | `tengu_1p_event_batch_config` | services/analytics/firstPartyEventLogger.ts | 1P 批量事件配置 |
| 文件路径 | `~/.claude/telemetry/` | services/analytics/firstPartyEventLoggingExporter.ts | 失败事件本地存储 |

## API 客户端（API Client）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_api_query` | services/api/logging.ts | API 查询事件 |
| 事件名 | `tengu_api_success` | services/api/logging.ts | API 成功事件 |
| 事件名 | `tengu_api_error` | services/api/logging.ts | API 错误事件 |
| 事件名 | `tengu_api_retry` | services/api/withRetry.ts | API 重试事件 |
| 事件名 | `tengu_api_529_background_dropped` | services/api/withRetry.ts | 529 过载后台丢弃 |
| 事件名 | `tengu_api_opus_fallback_triggered` | services/api/withRetry.ts | Opus 降级触发 |
| 事件名 | `tengu_api_custom_529_overloaded_error` | services/api/withRetry.ts | 自定义 529 过载错误 |
| 事件名 | `tengu_streaming_idle_timeout` | services/api/claude.ts | 流空闲超时 |
| 事件名 | `tengu_streaming_stall` | services/api/claude.ts | 流停滞 |
| 事件名 | `tengu_streaming_error` | services/api/claude.ts | 流错误 |
| 事件名 | `tengu_max_tokens_reached` | services/api/claude.ts | 达到最大 token |
| 事件名 | `tengu_context_window_exceeded` | services/api/claude.ts | 上下文窗口超限 |
| 错误类 | `CannotRetryError` | services/api/withRetry.ts | 不可重试错误 |
| 错误类 | `FallbackTriggeredError` | services/api/withRetry.ts | 降级触发错误 |
| API 端点 | `/api/oauth/usage` | services/api/usage.ts | 使用量查询 |
| API 端点 | `/api/oauth/profile` | services/oauth/getOauthProfile.ts | OAuth 用户资料 |

## 提示词缓存（Prompt Cache）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_prompt_cache_break` | services/api/promptCacheBreakDetection.ts | 缓存断裂检测 |
| 事件名 | `tengu_api_cache_breakpoints` | services/api/claude.ts | 缓存断点事件 |
| GrowthBook | `tengu_prompt_cache_1h_config` | services/api/claude.ts | 1 小时缓存 TTL 配置 |
| 常量 | `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` | constants/prompts.ts | 系统提示词动态边界标记 |

## 压缩（Compaction）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_auto_compact_succeeded` | query.ts | 自动压缩成功 |
| 事件名 | `tengu_compact` | services/compact/compact.ts | 压缩开始 |
| 事件名 | `tengu_partial_compact` | services/compact/compact.ts | 部分压缩 |
| 事件名 | `tengu_compact_failed` | services/compact/compact.ts | 压缩失败 |
| 事件名 | `tengu_compact_ptl_retry` | services/compact/compact.ts | PTL 重试 |
| GrowthBook | `tengu_sm_compact_config` | services/compact/sessionMemoryCompact.ts | 会话内存压缩配置 |
| 常量 | `MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES` | services/compact/autoCompact.ts | 值=3，熔断阈值 |
| 常量 | `AUTOCOMPACT_BUFFER_TOKENS` | services/compact/autoCompact.ts | 值=13000 |
| 常量 | `WARNING_THRESHOLD_BUFFER_TOKENS` | services/compact/autoCompact.ts | 值=20000 |
| 常量 | `MAX_OUTPUT_TOKENS_FOR_SUMMARY` | services/compact/autoCompact.ts | 值=20000 |

## 权限（Permissions）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_tool_use_can_use_tool_rejected` | services/tools/toolExecution.ts | 工具使用被拒 |
| 事件名 | `tengu_tool_use_can_use_tool_allowed` | services/tools/toolExecution.ts | 工具使用允许 |
| 事件名 | `tengu_tool_use_success` | services/tools/toolExecution.ts | 工具使用成功 |
| 事件名 | `tengu_permission_explainer_generated` | utils/permissions/permissionExplainer.ts | 权限解释生成 |
| GrowthBook | `tengu_auto_mode_config` | utils/permissions/yoloClassifier.ts | YOLO 自动模式配置 |
| 工具名 | `classify_result` | utils/permissions/yoloClassifier.ts | YOLO 分类器工具名 |

## 钩子（Hooks）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_pre_tool_hooks_cancelled` | services/tools/toolHooks.ts | 工具前钩子取消 |
| 事件名 | `tengu_post_tool_hook_error` | services/tools/toolHooks.ts | 工具后钩子错误 |
| 事件名 | `tengu_pre_stop_hooks_cancelled` | query/stopHooks.ts | 停止前钩子取消 |
| 事件名 | `tengu_stop_hook_error` | query/stopHooks.ts | 停止钩子错误 |

## 工具注册（Tool Registration）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 工具名 | `Bash` | tools/BashTool/toolName.ts | Bash 命令执行 |
| 工具名 | `Read` | tools/FileReadTool/prompt.ts | 文件读取 |
| 工具名 | `Write` | tools/FileWriteTool/prompt.ts | 文件写入 |
| 工具名 | `Edit` | tools/FileEditTool/constants.ts | 文件编辑 |
| 工具名 | `Glob` | tools/GlobTool/prompt.ts | 文件匹配 |
| 工具名 | `Grep` | tools/GrepTool/prompt.ts | 文本搜索 |
| 工具名 | `WebFetch` | tools/WebFetchTool/prompt.ts | 网页获取 |
| 工具名 | `WebSearch` | tools/WebSearchTool/prompt.ts | 网页搜索 |
| 工具名 | `Agent` | tools/AgentTool/constants.ts | 子代理生成 |
| 工具名 | `Skill` | tools/SkillTool/constants.ts | 技能加载 |
| 工具名 | `LSP` | tools/LSPTool/prompt.ts | 语言服务 |
| 工具名 | `PowerShell` | tools/PowerShellTool/toolName.ts | PowerShell（Windows） |
| 工具名 | `TaskCreate` | tools/TaskCreateTool/constants.ts | 任务创建 |
| 工具名 | `TaskList` | tools/TaskListTool/constants.ts | 任务列表 |
| 工具名 | `TaskUpdate` | tools/TaskUpdateTool/constants.ts | 任务更新 |
| 工具名 | `SendMessage` | tools/SendMessageTool/constants.ts | 消息发送 |
| 工具名 | `EnterPlanMode` | tools/EnterPlanModeTool/constants.ts | 进入计划模式 |
| 工具名 | `ExitPlanMode` | tools/ExitPlanModeTool/constants.ts | 退出计划模式 |
| 工具名 | `NotebookEdit` | tools/NotebookEditTool/constants.ts | Jupyter 编辑 |

## MCP

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_mcp_start` | cli/handlers/mcp.tsx | MCP 启动 |
| 事件名 | `tengu_mcp_add` | cli/handlers/mcp.tsx | MCP 服务器添加 |
| 事件名 | `tengu_mcp_server_connection_succeeded` | services/mcp/client.ts | 服务器连接成功 |
| 事件名 | `tengu_mcp_server_connection_failed` | services/mcp/client.ts | 服务器连接失败 |
| 事件名 | `tengu_mcp_tools_commands_loaded` | services/mcp/client.ts | 工具命令加载 |
| 事件名 | `tengu_mcp_oauth_flow_start` | services/mcp/auth.ts | OAuth 流程开始 |
| 事件名 | `tengu_mcp_oauth_flow_success` | services/mcp/auth.ts | OAuth 流程成功 |
| 事件名 | `tengu_mcp_elicitation_shown` | services/mcp/elicitationHandler.ts | 引导界面显示 |

## 代理/任务（Agent & Task）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_agent_flag` | main.tsx | 代理标志事件 |
| 事件名 | `tengu_agent_memory_loaded` | main.tsx | 代理内存加载 |
| 事件名 | `tengu_agent_tool_completed` | tools/AgentTool/agentToolUtils.ts | 代理工具完成 |
| 事件名 | `tengu_agent_tool_terminated` | tools/AgentTool/AgentTool.tsx | 代理工具终止 |
| 事件名 | `tengu_forked_agent_default_turns_exceeded` | （v2.1.91 新增） | 分叉代理超限 |

## 技能（Skills）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_skill_tool_invocation` | tools/SkillTool/SkillTool.ts | 技能调用事件 |
| 事件名 | `tengu_skill_loaded` | utils/telemetry/skillLoadedEvent.ts | 技能加载事件 |
| 事件名 | `tengu_dynamic_skills_changed` | skills/loadSkillsDir.ts | 动态技能变更 |

## 会话/成本（Session & Cost）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_session_resumed` | screens/REPL.tsx | 会话恢复 |
| 事件名 | `tengu_cost_threshold_reached` | screens/REPL.tsx | 成本阈值达到 |
| 事件名 | `tengu_session_memory_loaded` | services/SessionMemory/sessionMemoryUtils.ts | 会话内存加载 |
| 事件名 | `tengu_session_memory_extraction` | services/SessionMemory/sessionMemory.ts | 会话内存提取 |
| 持久化键 | `lastSessionId` | cost-tracker.ts | 上次会话 ID |

## 桥接（Bridge）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| GrowthBook | `tengu_bridge_poll_interval_config` | bridge/pollConfig.ts | 桥接轮询间隔 |
| GrowthBook | `tengu_bridge_repl_v2_config` | bridge/envLessBridgeConfig.ts | 桥接 REPL v2 配置 |

## OAuth/认证

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_oauth_token_exchange_success` | services/oauth/client.ts | OAuth token 交换 |
| 事件名 | `tengu_oauth_token_refresh_success` | services/oauth/client.ts | OAuth token 刷新 |
| 事件名 | `tengu_oauth_roles_stored` | services/oauth/client.ts | OAuth 角色存储 |
| 事件名 | `tengu_oauth_api_key` | services/oauth/client.ts | OAuth API 密钥 |

## 文件操作（File Operations）

| 锚点类型 | 锚点值 | 源文件 | 说明 |
|---------|--------|--------|------|
| 事件名 | `tengu_file_upload_failed` | services/api/filesApi.ts | 文件上传失败 |
| 事件名 | `tengu_file_history_track_edit_success` | utils/fileHistory.ts | 文件编辑跟踪 |
| 事件名 | `tengu_file_history_rewind_success` | utils/fileHistory.ts | 文件回溯 |

## 功能标志实验代码名

这些是 GrowthBook 实验的内部代码名，可用于追踪实验变化：

| 锚点值 | 源文件 | 说明 |
|--------|--------|------|
| `tengu_birch_trellis` | tools/BashTool/bashPermissions.ts | Bash 安全实验 |
| `tengu_surreal_dali` | tools/RemoteTriggerTool/ | 远程触发实验 |
| `tengu_hive_evidence` | constants/prompts.ts | 提示词实验 |
| `tengu_glacier_2xr` | tools/ToolSearchTool/prompt.ts | 工具搜索实验 |
| `tengu_quartz_lantern` | tools/FileWriteTool/ | 文件写入实验 |
| `tengu_otk_slot_v1` | services/api/claude.ts | OTK 槽位实验 |
| `tengu_frond_boric` | services/analytics/sinkKillswitch.ts | 遥测远程熔断 |

## GrowthBook 配置汇总

| 配置名 | 用途 |
|--------|------|
| `tengu_event_sampling_config` | 事件采样率控制 |
| `tengu_1p_event_batch_config` | 1P 批量事件配置 |
| `tengu_prompt_cache_1h_config` | 1 小时缓存 TTL |
| `tengu_sm_compact_config` | 会话内存压缩 |
| `tengu_auto_mode_config` | YOLO 自动模式 |
| `tengu_bridge_poll_interval_config` | 桥接轮询间隔 |
| `tengu_bridge_repl_v2_config` | 桥接 REPL v2 |
| `tengu_version_config` | 版本配置 |
| `tengu_max_version_config` | 最大版本控制 |
| `tengu_feedback_survey_config` | 反馈调查 |
| `tengu_bad_survey_transcript_ask_config` | 差评后转录请求 |
| `tengu_good_survey_transcript_ask_config` | 好评后转录请求 |
| `tengu_kairos_brief_config` | Kairos 简报 |
| `tengu_kairos_cron_config` | Kairos 定时 |
| `tengu_startup_manual_model_config` | 启动手动模型 |
| `tengu_sm_config` | 会话内存总配置 |
| `tengu_review_bughunter_config` | Bug 猎人审查 |

---

*基于 Claude Code v2.1.88 源码整理，共 120+ 锚点*
