# LogWatcher 需求规格说明

## 概述

LogWatcher 是一个用于监控 AI 编码工具（如 Codex）会话日志文件的机制。通过监听 home 目录下的会话文件，可以准确获取用户输入内容，弥补终端状态识别中对输入内容可能存在的误差。

## 目标

- 准确获取用户在 AI 编码工具中发送的消息
- 持续追踪对话记录
- 识别用户下达的最后一个指令

## 技术方案

### 1. 文件路径规则

以 Codex 为例，会话文件路径格式为：
```
~/.codex/sessions/YYYY/MM/DD/rollout-{timestamp}-{uuid}.jsonl
```

示例：
```
C:\Users\test\.codex\sessions\2025\12\01\rollout-2025-12-01T04-14-23-019ad666-f5ab-7501-a616-bbdc79da615b.jsonl
```

### 2. 文件搜索逻辑

1. **触发条件**：检测到 Codex 进程创建后启动搜索
2. **搜索范围**：进程创建时间之后被创建的文件
3. **搜索频率**：每秒搜索一次
4. **最大尝试次数**：20 次
5. **时间精度**：精确到毫秒
6. **跨平台支持**：使用跨平台库获取文件创建时间

### 3. 文件格式解析

会话文件是 JSONL 格式，每行一个 JSON 对象。

#### 3.1 session_meta（第一行）

```json
{
  "timestamp": "2025-11-30T20:14:23.281Z",
  "type": "session_meta",
  "payload": {
    "id": "019ad666-f5ab-7501-a616-bbdc79da615b",
    "timestamp": "2025-11-30T20:14:23.147Z",
    "cwd": "D:\\codes\\2025\\aicode-kanban",
    "originator": "codex_cli_rs",
    "cli_version": "0.63.0",
    ...
  }
}
```

关键字段：
- `payload.id`: 会话 UUID，可用于构造文件名和路径

#### 3.2 用户消息（event_msg + user_message）

```json
{
  "timestamp": "2025-11-30T20:16:39.465Z",
  "type": "event_msg",
  "payload": {
    "type": "user_message",
    "message": "用户发送的消息内容",
    "images": []
  }
}
```

筛选条件：
- `type` = "event_msg"
- `payload.type` = "user_message"

### 4. 状态追踪

需要记录以下状态：
- **codex_session_id**: 会话 UUID
- **file_lines_read**: 已读取的文件行数
- **file_offset**: 已读取的文件偏移量（字节）

### 5. 增量读取机制

1. **轮询频率**：每 500ms 检查一次文件变化
2. **读取策略**：
   - 从上次偏移量位置继续读取
   - 偏移量通常停在 `\n` 位置，继续读到下一个 `\n` 即可获得完整的一行 JSON
3. **容错处理**：
   - 如果读取失败（如 JSON 解析错误），从头重新读取整个文件并重置偏移量

### 6. 消息搜索策略

- 从后往前搜索
- 筛选条件：`type` = "event_msg" 且 `payload.type` = "user_message"
- 可获取：用户发送的所有消息、最后一个用户指令

## 数据结构

### LogWatcherState

```go
type LogWatcherState struct {
    SessionID     string    // Codex 会话 ID
    FilePath      string    // 当前监控的文件路径
    LinesRead     int       // 已读取的行数
    FileOffset    int64     // 文件偏移量
    LastCheckTime time.Time // 上次检查时间
    UserMessages  []UserMessage // 用户消息列表
}
```

### UserMessage

```go
type UserMessage struct {
    Timestamp time.Time // 消息时间戳
    Message   string    // 消息内容
    Images    []string  // 图片（base64）
}
```

## 工作流程

```
1. 检测到 Codex 进程创建
        ↓
2. 启动文件搜索（每秒一次，最多20次）
        ↓
3. 找到对应的 .jsonl 文件
        ↓
4. 读取第一行获取 session_meta
        ↓
5. 验证会话 ID，记录初始状态
        ↓
6. 启动增量读取循环（每 500ms）
        ↓
7. 检测文件变化，增量读取新内容
        ↓
8. 解析 JSON 行，提取用户消息
        ↓
9. 更新状态并通知上层应用
```

## 输出数据

通过 LogWatcher 可以获得：
- 完整的对话记录
- 两次检查间隔之间新增的对话
- 用户下达的最后一个指令
- 会话的工作目录、使用的模型等元信息

## 支持的 AI 工具

目前计划支持：
- Codex CLI (`~/.codex/sessions/...`)

未来可扩展支持其他工具。

## 注意事项

1. 需要处理时区问题（文件名中的时间戳格式）
2. 需要处理跨平台文件路径差异
3. 需要处理并发访问文件的情况
4. 需要在进程退出时清理 watcher 资源
