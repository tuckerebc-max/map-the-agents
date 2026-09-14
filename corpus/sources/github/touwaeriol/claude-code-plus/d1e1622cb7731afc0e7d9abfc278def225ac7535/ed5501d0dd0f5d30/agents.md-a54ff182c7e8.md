1=特别提醒：请使用简体中文进行交流
特别提醒：git commit、changelog 不使用中文，而是使用英文

# Claude Code Plus - 架构说明



## 📋 项目概述

Claude Code Plus 是一个 IntelliJ IDEA 插件，集成了 Claude AI 助手，提供智能代码编辑、文件操作、终端执行等功能。

## 🏗️ 整体架构

## 🔌 三种通信方式


### 2️⃣ IDEA 集成通信 (纯 HTTP)

**用途**: 打开文件、显示 Diff、搜索文件等 IDEA 原生功能

**前端**:
```typescript
// frontend/src/services/ideaBridge.ts
import { ideService } from '@/services/ideaBridge'

// 打开文件
await ideService.openFile('/path/to/file.ts', { line: 10 })

// 显示 Diff
await ideService.showDiff({
    filePath: '/path/to/file.ts',
    oldContent: '...',
    newContent: '...'
})
```

**后端**:
```kotlin
// claude-code-server/src/main/kotlin/com/claudecodeplus/server/HttpApiServer.kt
post("/api/") {
    when (action) {
        "ide.openFile" -> ideActionBridge.openFile(request)
        "ide.showDiff" -> ideActionBridge.showDiff(request)
        "ide.searchFiles" -> ideActionBridge.searchFiles(query, maxResults)
        "ide.getFileContent" -> // 读取文件内容
    }
}
```

**协议**: HTTP POST
- 请求-响应模式
- 同步调用
- 简单可靠

---

### 3️⃣ 通用 Web 功能 (纯 HTTP)

**用途**: 其他不需要流式响应的功能

**协议**: HTTP GET/POST
- RESTful API
- 标准 HTTP 请求

---

## 🔧 关键技术细节

### 随机端口机制

**问题**: 多个 IDEA 项目同时打开时，端口冲突

**解决方案**:
```kotlin
// claude-code-server/src/main/kotlin/com/claudecodeplus/server/HttpApiServer.kt
fun start(port: Int = 8765): String {
    val actualPort = try {
        embeddedServer(Netty, port = port) { ... }.start()
        port
    } catch (e: BindException) {
        val availablePort = findAvailablePort()
        embeddedServer(Netty, port = availablePort) { ... }.start()
        availablePort
    }
    return "http://localhost:$actualPort"
}
```

### 前端获取后端地址 & 环境检测

**IDEA 插件模式**: 通过 URL 参数 `?ide=true` 触发后端注入

```kotlin
// jetbrains-plugin/.../VueToolWindowFactory.kt
val ideUrl = "$serverUrl?ide=true"  // 带上 ide=true 参数
browser.loadURL(ideUrl)
```

```kotlin
// claude-code-server/.../HttpApiServer.kt
get("/") {
    val isIdeMode = call.request.queryParameters["ide"] == "true"

    if (isIdeMode) {
        // IDEA 插件模式：注入 window.__serverUrl
        val injection = """
            <script>
                window.__serverUrl = 'http://localhost:$serverPort';
                console.log('✅ Environment: IDEA Plugin Mode');
            </script>
        """.trimIndent()
        html = html.replace("</head>", "$injection\n</head>")
    }
}
```

**浏览器模式**: 通过统一解析器获取地址
```typescript
// frontend/src/services/ideaBridge.ts
import { resolveServerHttpUrl } from '@/utils/serverUrl'

private getBaseUrl(): string {
    return resolveServerHttpUrl()
}

// 环境检测
getMode(): 'ide' | 'browser' {
    return (window as any).__serverUrl ? 'ide' : 'browser'
}
```

`resolveServerHttpUrl()` 的优先级：
1. `window.__serverUrl`（IDEA 注入或提前设置）
2. `VITE_SERVER_URL`
3. `VITE_BACKEND_PORT`（默认 `http://localhost:<port>`）
4. 回退到 `http://localhost:8765`

**优势**:
- ✅ **时序可靠**: HTML 加载时就已注入，Vue 初始化前就能读取
- ✅ **无需额外请求**: 不需要前端主动检测
- ✅ **简单明确**: 通过 `window.__serverUrl` 的存在判断环境

---

## 📁 核心文件说明

### 前端核心文件

#### `frontend/src/services/ideaBridge.ts`
**职责**: 前端与后端的 HTTP 通信桥接

**导出**:
- `ideaBridge`: 单例服务，提供 `query()` 方法
- `ideService`: 便捷 API，封装常用 IDEA 集成功能
    - `openFile()`: 打开文件
    - `showDiff()`: 显示 Diff
    - `searchFiles()`: 搜索文件
    - `getFileContent()`: 获取文件内容
    - `getTheme()`: 获取主题
- `claudeService`: Claude 会话相关 API（通过 HTTP，非 WebSocket）

**示例**:
```typescript
import { ideService } from '@/services/ideaBridge'

// 打开文件并跳转到指定行
await ideService.openFile('/src/App.vue', { line: 42, column: 10 })

// 显示 Diff（支持多处修改）
await ideService.showDiff({
    filePath: '/src/utils/helper.ts',
    oldContent: 'old code',
    newContent: 'new code',
    rebuildFromFile: true,  // 从文件重建完整 Diff
    edits: [
        { oldString: 'foo', newString: 'bar', replaceAll: false }
    ]
})
```

#### `frontend/src/services/ClaudeSession.ts`
**职责**: Claude 会话管理（WebSocket RPC）

**功能**:
- 建立 WebSocket 连接
- 发送消息并接收流式响应
- 中断正在进行的会话
- 管理会话状态

#### `frontend/src/components/tools/`
**职责**: 工具调用显示组件

**组件列表**:
- `ReadToolDisplay.vue`: 读取文件工具
- `WriteToolDisplay.vue`: 写入文件工具
- `EditToolDisplay.vue`: 编辑文件工具
- `BashToolDisplay.vue`: 终端命令工具
- `MultiEditToolDisplay.vue`: 多处编辑工具
- `CompactToolCard.vue`: 可复用的工具卡片组件

**设计原则**:
- 折叠模式：显示关键参数（文件名、路径、命令）
- 展开模式：显示完整细节
- 状态指示：彩色圆点（绿色=成功，红色=失败，灰色=进行中）
- IDEA 集成：点击文件路径打开文件，点击卡片显示 Diff

---

### 后端核心文件

#### `claude-code-server/src/main/kotlin/com/claudecodeplus/server/HttpApiServer.kt`
**职责**: HTTP 服务器主入口

**功能**:
- 启动 Ktor 服务器（随机端口）
- 配置 WebSocket 端点 (`/ws`)
- 配置 HTTP API 端点 (`/api/`)
- 提供静态文件服务（前端资源）

**关键代码**:
```kotlin
// WebSocket RPC 端点
webSocket("/ws") {
    val rpcHandler = WebSocketRpcHandler(this, claudeRpcService)
    rpcHandler.handle()
}

// HTTP API 端点
post("/api/") {
    val requestBody = call.receiveText()
    val json = Json { ignoreUnknownKeys = true }
    val request = json.decodeFromString<FrontendRequest>(requestBody)
    val action = request.action

    when (action) {
        "ide.openFile" -> {
            val response = ideActionBridge.openFile(request)
            call.respondText(json.encodeToString(response), ContentType.Application.Json)
        }
        "ide.showDiff" -> {
            val response = ideActionBridge.showDiff(request)
            call.respondText(json.encodeToString(response), ContentType.Application.Json)
        }
        // ... 其他 API
    }
}
```

#### `jetbrains-plugin/src/main/kotlin/com/claudecodeplus/plugin/bridge/IdeActionBridgeImpl.kt`
**职责**: IDEA 平台 API 调用实现

**功能**:
- `openFile()`: 使用 `FileEditorManager` 打开文件
- `showDiff()`: 使用 `DiffManager` 显示 Diff
- `searchFiles()`: 使用 `FilenameIndex` 搜索文件
- `getFileContent()`: 读取文件内容

**关键代码**:
```kotlin
override fun openFile(request: FrontendRequest): FrontendResponse {
    val filePath = request.data?.jsonObject?.get("filePath")?.jsonPrimitive?.contentOrNull
    val line = request.data?.jsonObject?.get("line")?.jsonPrimitive?.intOrNull

    ApplicationManager.getApplication().invokeLater {
        val file = LocalFileSystem.getInstance().findFileByIoFile(File(filePath))
        if (file != null) {
            val descriptor = OpenFileDescriptor(project, file, line - 1, column - 1)
            FileEditorManager.getInstance(project).openTextEditor(descriptor, true)
        }
    }

    return FrontendResponse(success = true)
}
```

---

## 🎨 设计决策

### 为什么后端使用随机端口？

**原因**:
1. **多项目支持**: 用户可能同时打开多个 IDEA 项目
2. **避免冲突**: 固定端口可能被其他应用占用
3. **灵活性**: 自动选择可用端口，无需用户配置

---

## 🚀 启动流程

### IDEA 插件模式

1. **用户打开 IDEA 项目**
2. **插件初始化** (`HttpServerProjectService`)
    - 启动后端 HTTP 服务器（随机端口）
    - 记录服务器 URL
3. **打开聊天工具窗口** (`ChatToolWindowFactory`)
    - 加载前端资源（Vue 应用）
    - 注入 `window.__serverUrl`
4. **前端初始化**
    - `ideaBridge` 读取 `window.__serverUrl`
    - 建立 HTTP 连接
5. **用户开始对话**
    - 前端通过 WebSocket RPC 发送消息
    - 后端调用 Claude SDK
    - 流式返回响应

### 浏览器模式

1. **启动后端服务器** (手动或脚本)
2. **启动前端开发服务器** (`npm run dev`)
3. **打开浏览器** (`http://localhost:5173`)
4. **前端通过解析器解析 URL**（若无注入，则回退 `http://localhost:8765`）
5. **功能受限**: IDEA 集成功能不可用（打开文件、显示 Diff）

**很重要**
开发时如果需要调试界面：
通过启动 com.asakii.server.StandaloneServerKt 来得到一个 运行在 8765 端口的后端
运行 前端的 dev 任务，可以得到一个运行在端口 5174 的前端
使用mcp 访问 5174 即可测试相关功能
如果 相关端口被占用，停止占用端口的进程，而不是使用新端口


---

## 📝 开发指南

### 添加新的 IDEA 集成功能

1. **定义接口** (`IdeActionBridge.kt`)
```kotlin
interface IdeActionBridge {
    fun myNewFeature(request: FrontendRequest): FrontendResponse
}
```

2. **实现接口** (`IdeActionBridgeImpl.kt`)
```kotlin
override fun myNewFeature(request: FrontendRequest): FrontendResponse {
    // 调用 IDEA Platform API
    return FrontendResponse(success = true)
}
```

3. **添加 HTTP 端点** (`HttpApiServer.kt`)
```kotlin
when (action) {
    "ide.myNewFeature" -> {
        val response = ideActionBridge.myNewFeature(request)
        call.respondText(json.encodeToString(response), ContentType.Application.Json)
    }
}
```

4. **添加前端 API** (`ideaBridge.ts`)
```typescript
export const ideService = {
    async myNewFeature(params: any) {
        return ideaBridge.query('ide.myNewFeature', params)
    }
}
```

5. **在组件中使用**
```typescript
import { ideService } from '@/services/ideaBridge'

await ideService.myNewFeature({ foo: 'bar' })
```

---

## 🔍 调试技巧

### 查看 HTTP 请求

### 常见问题

**问题**: 前端无法连接后端
- 检查 `window.__serverUrl` 是否正确注入
- 检查后端服务器是否启动
- 检查端口是否被占用

**问题**: IDEA 集成功能不工作
- 确认在 IDEA 插件模式下运行（不是浏览器）
- 检查 `IdeActionBridgeImpl` 是否正确注入
- 查看 IDEA 日志中的错误信息




---

## 📚 相关文档

- [HTTP API 架构](docs/HTTP_API_ARCHITECTURE.md)
- [前端重构设计](docs/frontend-refactoring-design.md)
- [工具显示规范](docs/tool-display-specification.md)
- [主题系统](docs/THEME_SYSTEM.md)

---

## 📦 外部子模块

- `external/openai-codex`
    - 来源仓库：`org-14957082@github.com:openai/codex.git`
    - 管理方式：作为 git submodule 引入，位于 `external/` 目录，后续可通过 `git submodule update --init --recursive` 同步。


