# AgentsMesh 数据架构原则 (R2 决策)

## 核心原则

> **Schema 用 proto；Wire 传输用 JSON；域内按需选择数据结构。**

三层正交关系：

1. **Schema 定义**：proto schema 是单一真理源（SSOT）
2. **Wire 传输**：跨进程 / 跨语言传输用 **JSON**（Connect-RPC JSON encoding `Content-Type: application/json`）
3. **域内表示**：每个语言 / 模块内部按需选用 proto 生成类型 / View Type / 自定义 struct

为什么这样：
- proto schema 提供跨语言形状一致性 + 字段版本管理
- JSON wire 提供调试友好（curl 可读）+ 浏览器原生支持 + 无需 protobuf 运行时
- 域内灵活性允许各端按自己的最优表示组织内存数据

## 三条规则

### 规则 1：跨域用 JSON wire（proto schema 决定形状）

跨任何域边界（network / language / process）传输数据，用 **JSON 字符串**，但形状由 proto schema 决定：

- 跨 L2 backend ↔ L3 wire（Connect-RPC）→ `Content-Type: application/json`（Connect 协议默认支持）
- 跨 L3 wire ↔ L4 Rust core → JSON string，用 serde decode 到 proto crate type
- 跨 L5 wasm ↔ L6 Web → JSON string（`pods_json() -> String`，web `JSON.parse(...)`）
- 跨 L7 ffi ↔ L8 Swift → UniFFI Record（仍然 typed，但字段命名跟随 proto schema）

### 规则 2：域内可自定义

数据进入一个域（语言 / 模块 / 内存层）后，按需选择最合适的内部表示：

| 场景 | 选用数据结构 |
|---|---|
| 域内**未做特殊处理**，纯缓存 wire 数据 | **直接用 proto 类型**（`Vec<proto::Pod>`） |
| 域内有**轻量加工**（cache metadata / derived display） | **View Type**（基于 proto 派生，嵌入或交叉） |
| 域内有**重度业务建模**（聚合 / 投影 / UI state） | **自定义 struct**（与 proto 解耦） |

### 规则 3：跨域时显式转换

任何从"自定义 struct"或"View Type"出域时，必须显式转换回 proto wire shape：

- `impl From<MyCustomView> for proto::Pod`（出域）
- `impl From<proto::Pod> for MyCustomView`（入域）
- 转换函数集中在域边界处，不散落业务代码

## 应用到 9 层数据架构

| 层 | 域 | 数据结构原则 |
|---|---|---|
| L1 | PostgreSQL | 已定 (SQL schema) |
| L2 | Backend domain (Go GORM) | 已定 (GORM struct) |
| L2↔L3 | backend convert.go | **JSON wire** + proto schema 形状（规则 1） |
| L3 | Wire | proto schema 是 SSOT；wire payload 是 JSON |
| L3↔L4 | api-client (Rust) | **JSON wire** + serde decode 到 proto crate type |
| L4 | Rust core cache | **按需**：大多数直接 proto type；需 timestamp 等加工时用 view |
| L4↔L4' | persistence | **JSON blob**（serde_json::to_string proto type；可读可调试可 jq 检查） |
| L4' | Client persistence | JSON-encoded proto |
| L4↔L5 | wasm bridge | **JSON string**（`pods_json() -> String`，内容形状为 proto schema） |
| L5↔L6 | wasm → web | **JSON string**（web `JSON.parse(svc.pods_json())`） |
| L6 | Web TS | **按需**：列表数据用 proto generated TS 类型；UI 状态独立 |
| L4↔L7 | ffi DTO | **proto-mirror Record**（UniFFI 限制：仍 typed Record，字段命名跟随 proto schema） |
| L7↔L8 | UniFFI generated | auto-generated Swift |
| L8 | iOS Swift TCA | **按需**：列表数据用 UniFFI Record；TCA State + UI 加工时用 view |

## 关键决策与影响

### 决策 1：proto 加 serde derive

所有 `rust_prost_library` 生成的 proto 类型自动加 `#[derive(serde::Serialize, serde::Deserialize)]`。

**实现**：`tools/rust_prost_toolchain/BUILD.bazel` 加 `prost_opts = ["type_attribute=.=#[derive(serde::Serialize\\, serde::Deserialize)]"]`。

**影响**：
- proto 类型既能 `prost::Message::encode()`（binary）又能 `serde_json::to_string()`（JSON）
- types crate 不再需要 legacy serde mirror
- L4↔L5 桥可保留 JSON 路径（开发友好）也可用 binary（性能）

### 决策 2：state crate 默认用 proto，按需 view

```rust
// 简单 cache — 直接 proto
pub struct RunnerState {
    runners: Vec<proto::runner_api::v1::Runner>,
}

// 有加工 cache — view type
pub struct PodCacheEntry {
    pub pod: proto::pod::v1::Pod,      // proto base
    pub last_synced_at: i64,           // 加工：去重
    pub local_init_progress: Option<PodInitProgress>,  // 加工：客户端状态
}
pub struct PodState {
    pods: Vec<PodCacheEntry>,
    current_pod_key: Option<String>,
}
```

### 决策 3：删除 proto_convert.rs

`services/src/proto_convert.rs`（~300 行）整个删除。services 拿到 proto 响应后：
- 简单情况：直接存 proto 到 cache
- 有加工：在域内（state crate）做转换，不在 services 层

### 决策 4：删除 types crate 17 个 legacy 文件

`clients/core/crates/types/src/` 最终只剩：
- `lib.rs`（proto re-export）
- `common.rs`（基础类型）
- `enums.rs`（业务枚举，proto 之前的）
- `service_error.rs`（错误类型）

### 决策 5：ffi DTO 保留但精简

UniFFI 不支持直接消费 prost 生成类型（需要 `#[derive(uniffi::Record)]`）。保留 `ffi/dto/` 作为 Rust-Swift 桥的 mirror 层，**但字段与 proto 一一对应**，不引入 legacy 字段命名/语义差异。

### 决策 6：L4' persistence 用 JSON blob

`persistence/repos/*.rs` 把 `save_pod(types::Pod)` 改为 `save_pod(proto::Pod)`，存储 `serde_json::to_string(pod)` JSON 字符串到 SQLite blob。可读可调试，`sqlite3 ... "SELECT data FROM kv_store" | jq` 可直接查看。

代价：JSON 比 prost binary 大 2-3 倍。AgentsMesh 客户端持久化不是性能敏感场景（pod / channel / runner 列表通常 < 100 个），可接受。

### 决策 7：proto3 默认值语义在 cache 层用 helper 处理

```rust
// 在 state crate 提供 helper
pub fn nonzero_i64(v: i64) -> Option<i64> {
    if v == 0 { None } else { Some(v) }
}
pub fn non_empty_string(s: &str) -> Option<&str> {
    if s.is_empty() { None } else { Some(s) }
}
```

cache view 取字段时用 helper：`nonzero_i64(pod.runner_id)`。

## 不做的事

- ❌ 不强制所有内存结构都嵌入 proto base（避免过度抽象）
- ❌ 不要求 web/iOS UI 状态和 proto 强绑定
- ❌ 不引入新的 generic view trait（YAGNI）

## R2 Phase 2 实施清单

按照上述原则，下一步实施：

1. **proto serde derive**（tools/rust_prost_toolchain/BUILD.bazel + MODULE.bazel）
2. **api-client / Connect wire 切到 JSON**（Connect-Web 客户端 + Connect-Go backend 都默认 JSON wire）
3. **删除 proto_convert.rs**（300 行）
4. **改 13 个 state crate cache 类型**（直接 proto 或定义 view entry）
5. **改 services crate** services 把 proto 响应直接写入 cache，删除 dual-track JSON 接口
6. **改 wasm `*_json()` 实现**（serde 输出 proto 类型，签名不变）
7. **persistence 改用 JSON blob**（serde_json 序列化 proto type）
8. **删除 17 个 types crate legacy 文件**
9. **改 ffi/dto/ 字段与 proto 对齐**（如有差异）
10. **L8 iOS TCA State** 检查是否需要 view types（多数情况下直接用 PodDto 即可）
11. **L6 web stores**：检查是否需要 view interface（多数情况下用 proto generated TS 即可）

预计净减少：~5000-6000 行（删除 legacy types + proto_convert + dual-track JSON 接口 + ffi 部分镜像简化）

## Wire 协议选型

- **当前**：Connect-RPC 默认用 `Content-Type: application/proto`（binary）
- **目标**：切到 `Content-Type: application/json`（JSON wire）
  - Backend：Connect-Go 自动支持，无需改 handler
  - Web 客户端：`@connectrpc/connect-web` 可配置 `transport: createConnectTransport({ baseUrl, useBinaryFormat: false })` 或类似 API
  - Rust api-client：当前用 prost binary，需切到 JSON encoding（用 `pbjson` 或 serde direct on proto types）
  - iOS：URLSession + JSON（无 Connect-Swift 时手写）

**好处**：
- curl 直接调试：`curl -X POST -H 'Content-Type: application/json' -d '{"orgSlug":"x"}' http://.../proto.pod.v1.PodService/ListPods`
- 浏览器 DevTools Network 面板可读
- 无 prost runtime 依赖于客户端 wire decode

**代价**：JSON 比 proto binary 大 2-3 倍 → 但 AgentsMesh API 不是 high-throughput 场景

## 风险与缓解

| 风险 | 缓解 |
|---|---|
| proto3 默认值入侵 cache | helper 函数 `nonzero_*` / `non_empty_*` |
| auth crate 依赖 legacy `User/AuthSession` | 用 `proto.auth.v1.User` 替换；AuthSession 若 proto 没有则在 auth crate 内部定义（不在 types crate） |
| ffi/dto 仍手写 | 接受作为 UniFFI 限制；but 字段与 proto 一致，无信息加工 |
| web 端 snake_case ↔ camelCase | proto-gen TS 是 camelCase。要么转 web 全 camelCase，要么 proto JSON 输出 snake_case（serde 默认）让 web 端用 snake_case，与现有 TS interface 一致 |
| iOS Swift snake_case 字段（UniFFI auto-gen）| 接受，与 Rust 链路一致；如需 Swift convention，加 computed property 包装（in iOS feature 层） |
| Connect-RPC JSON wire 性能 | 不在性能敏感路径，可接受；如热路径需要再做 binary 优化 |

## 已确认决策点

- ✅ **架构方案 A**：proto 作为 schema 原型，跨域 wire 用 JSON，域内按需选择数据结构
- ✅ **wire 协议**：Connect-RPC JSON wire（`Content-Type: application/json`）
- ✅ **wasm 出口**：JSON 字符串（`pods_json() -> String`），内容形状由 proto schema 决定
- ✅ **persistence**：JSON blob 存储（serde_json 序列化 proto type）
- ✅ **types crate 全删 legacy**：包括 auth.rs (User/AuthSession/Organization)
- ✅ **大 commit**：R2 Phase 2 作为单一原子提交

