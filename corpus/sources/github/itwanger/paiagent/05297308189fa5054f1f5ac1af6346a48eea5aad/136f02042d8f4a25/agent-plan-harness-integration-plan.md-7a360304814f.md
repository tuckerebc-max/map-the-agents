# PaiAgent-one 接入火山方舟 Agent Plan + Harness 执行计划

## Summary

目标：把火山方舟 Agent Plan 接成 PaiAgent-one 的统一 Agent 能力配置。用户配置一次 Agent Plan 后，工作流可复用语言模型、联网搜索、记忆召回、图片生成、视频生成、向量/RAG，并让 ReAct Agent 按需调用这些能力。

关键说明需要在产品和文档中明确体现：

- 联网搜索：Agent Plan 免费赠送与豆包同源的联网搜索额度，开箱即可获取实时、权威信息。
- 记忆能力：Agent Plan 内置 `Doubao-embedding-vision` 模型，帮助 Agent 在信息量大、对话长、资料分散的场景下更准确召回相关内容，提升跨轮次上下文追踪能力与整体效果。

设计原则：Agent Plan 是「供应商/套餐配置」，不是单个业务节点；联网搜索、记忆、图片生成、视频生成、RAG 都落成可编排节点，同时注册为 ReAct Agent 可选工具。

参考入口：

- Agent Plan 套餐概览：https://www.volcengine.com/docs/82379/2366394?lang=zh
- 接入向量化模型：https://www.volcengine.com/docs/82379/2375464?lang=zh
- 接入视觉模型：https://www.volcengine.com/docs/82379/2375486?lang=zh

## Key Changes

- 全局配置新增 provider：`volcengine_agent_plan`，前端展示为「火山方舟 Agent Plan」。
- 全局配置扩展模型字段：`embeddingModel`、`imageModel`、`videoModel`；现有 `model` 继续作为默认语言模型，`ttsModel` 继续服务 TTS。
- 全局配置扩展 Harness 能力开关：`webSearchEnabled`、`memoryEnabled`，并在 UI 中展示联网搜索与记忆能力说明。
- 新增联网节点：`web_search`、`web_fetch`。
- 新增记忆节点：`memory_write`、`memory_retrieve`。
- 新增多模态节点：`image_generate`、`video_generate`、`vision_analyze`。
- 新增知识库节点：`knowledge_upsert`、`knowledge_retrieve`。
- ReAct Agent 工具扩展：联网搜索、网页读取、记忆读写、知识检索、图片生成、视频生成都可作为工具启用。

## Implementation Changes

### 1. Agent Plan 配置层

后端扩展 `llm_global_config`：

- `model`：默认语言模型。
- `embedding_model`：默认记忆/RAG 向量模型，默认建议 `doubao-embedding-vision`。
- `image_model`：默认图片生成模型。
- `video_model`：默认视频生成模型。
- `tts_model`：默认 TTS 模型。
- `web_search_enabled`：是否启用 Agent Plan 联网搜索。
- `memory_enabled`：是否启用 Agent Plan 记忆能力。

`LLMGlobalConfigService` 增加 provider 归一化：

- `volcengine`、`ark`、`agent_plan`、`agent plan`、`火山方舟` -> `volcengine_agent_plan`。

前端 `LLMConfigModal` 新增 Agent Plan 专属配置区：

- API URL、API Key、语言模型、向量模型、图片模型、视频模型、TTS 模型。
- 联网搜索说明：免费赠送与豆包同源的联网搜索额度，开箱获取实时、权威信息。
- 记忆能力说明：内置 `Doubao-embedding-vision`，用于长对话、资料分散、多轮上下文召回。

LLM 和 ReAct Agent 节点选择 Agent Plan 配置时，继续复用现有 OpenAI-compatible 语言模型链路。

### 2. 联网搜索能力

新增 `web_search` 节点：

- 输入：`query`、`limit`、`freshness`、`siteFilter`、`language`。
- 输出：`results`、`summary`、`citations`、`query`。
- 用于实时信息获取、市场调研、新闻聚合、文章资料收集。

新增 `web_fetch` 节点：

- 输入：`urls`、`extractMode`。
- 输出：`pages`、`content`、`citations`。
- 用于读取指定网页、PDF、文档链接后交给 LLM 总结。

后端封装 `HarnessWebSearchClient`，节点执行器不直接绑定厂商接口细节。

ReAct Agent 注册工具：

- `web_search(query, limit)`。
- `web_fetch(urls)`。

DebugDrawer 展示搜索结果、摘要和引用链接。

### 3. 记忆能力

记忆能力底层使用 Agent Plan 的 `Doubao-embedding-vision` 向量模型，不先假设有独立外部 Memory API。

新增本地记忆表：

- `agent_memory`：保存记忆内容、类型、scope、tags、source。
- `agent_memory_embedding`：保存 embedding、模型名、维度、索引元信息。

新增 `memory_write` 节点：

- 输入：`content`、`memoryType`、`tags`、`scope`。
- 输出：`memoryId`、`scope`、`stored`。
- 用于保存用户偏好、项目背景、历史结论、素材风格要求。

新增 `memory_retrieve` 节点：

- 输入：`query`、`scope`、`topK`、`tags`。
- 输出：`memories`、`context`、`citations`。
- 用于在工作流开头召回跨轮次上下文。

默认显式写入记忆，不自动把每次对话都沉淀为长期记忆。

默认 scope：

- `workflow`：当前工作流记忆。
- `user`：当前用户长期偏好。
- `global`：团队共享记忆，必须由节点显式选择。

ReAct Agent 注册工具：

- `memory_retrieve(query, scope, topK)`。
- `memory_write(content, memoryType, tags, scope)`。

### 4. 多模态生成能力

新增 `image_generate` 节点：

- 输入：`prompt`、`referenceImageUrl`、`size`、`style`、`count`、`negativePrompt`。
- 输出：`imageUrl`、`imageUrls`、`prompt`、`model`、`metadata`。

新增 `video_generate` 节点：

- 输入：`prompt`、`referenceImageUrl`、`duration`、`resolution`、`ratio`、`cameraMotion`。
- 输出：`taskId`、`status`、`videoUrl`、`coverUrl`、`model`、`metadata`。
- 按异步任务处理，用 SSE 推送提交、生成中、转存中、完成/失败。

新增 `vision_analyze` 节点：

- 输入：`imageUrl` 或 `videoUrl`、`criteria`。
- 输出：`description`、`score`、`issues`、`pass`。
- 可与条件分支联动，用于生成结果质检和自动重试。

图片、视频结果统一转存到 MinIO，避免下游节点依赖厂商临时 URL。

### 5. RAG 与知识库能力

新增 `knowledge_upsert`：

- 输入：`knowledgeBaseId`、`content`、`sourceUrl`、`title`、`tags`。
- 输出：`contentId`、`chunkCount`、`indexed`。

新增 `knowledge_retrieve`：

- 输入：`query`、`knowledgeBaseId`、`topK`、`scoreThreshold`。
- 输出：`chunks`、`citations`、`context`。

RAG 与 Memory 共用 Agent Plan 的 `embeddingModel`，但产品语义分开：

- RAG 面向资料库。
- Memory 面向 Agent 运行历史、用户偏好、跨轮上下文追踪。

## Example Workflows

### 联网内容生产

输入主题 -> `web_search` 搜实时资料 -> `memory_retrieve` 召回写作风格 -> `llm` 生成脚本 -> `image_generate` 生成封面 -> `video_generate` 生成短视频 -> `tts` 生成旁白 -> `output`。

### 长期记忆 Agent

输入任务 -> `memory_retrieve` 召回历史要求 -> `react_agent` 调用搜索/记忆/生成工具 -> `memory_write` 保存最终偏好或结论 -> `output`。

### RAG 学习助手

`knowledge_upsert` 写入课程资料 -> 用户提问 -> `knowledge_retrieve` 召回资料 -> `llm` 回答 -> `image_generate` 配图 -> `tts` 讲解。

### 营销素材闭环

商品资料 + 商品图 -> `web_search` 查竞品 -> `llm` 提炼卖点 -> `image_generate` 海报 -> `video_generate` 短片 -> `vision_analyze` 质检 -> 条件分支通过/重试。

## Test Plan

后端单测：

- Agent Plan 配置保存、更新、默认配置、provider 归一化、联网搜索/记忆开关回显。
- LLM 节点选择 Agent Plan 配置后仍能解析 `model/apiUrl/apiKey`。
- `web_search/web_fetch` mock 成功、空结果、外部错误、引用字段输出。
- `memory_write/memory_retrieve` 使用 `doubao-embedding-vision` 配置、scope 隔离、topK 召回、空记忆。
- 图片/视频节点参数构造、异步轮询、URL 转存、失败透传。
- `vision_analyze.pass` 能被条件分支正确读取。
- ReAct Agent 可按配置启用搜索、记忆、生成工具。

前端验证：

- `npm run build` 通过。
- Agent Plan 配置弹窗能编辑多模型字段，并展示联网搜索和记忆能力说明。
- 节点面板展示联网、记忆、知识库、多模态节点。
- DebugDrawer 可展示搜索引用、记忆召回、图片、视频、音频。

集成验收：

- `./mvnw test` 通过。
- 用 mock Agent Plan/Harness API 跑通「联网内容生产」工作流。
- 有真实 Agent Plan Key 时，手动验证一次联网搜索、一次记忆召回、一次图片生成、一次视频生成。

## Assumptions

- 记忆能力第一版基于 `Doubao-embedding-vision` + 本地记忆表实现，不假设火山方舟提供独立 Memory 存储 API。
- 联网搜索第一版通过后端客户端封装 Agent Plan/Harness 联网能力，前端和节点执行器不绑定厂商接口细节。
- 记忆默认显式写入，不自动保存每轮对话。
- 媒体产物统一转存 MinIO。
- MVP 必须体现 Agent Plan 的三类核心价值：联网搜索、记忆召回、多模态生成。
