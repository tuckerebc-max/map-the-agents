# AgentsMesh 全栈数据架构审计 (R2 Phase 1)

> 5 个并行 Explore agent 对仓库进行系统性扫描后产出。审计覆盖 9 个数据层
> （L1 server DB → L8 iOS Swift + L4' 客户端持久化）、所有跨层转换边界、
> 13 个核心 domain 的形状差异。目标：为 R2 实施提供决策依据。

## 1. 摘要

- **9 个数据层**：L1 DB / L2 GORM / L3 Wire / L4 Rust cache / L4' 客户端持久化 / L5 wasm bridge / L6 Web TS / L7 UniFFI / L8 iOS
- **每个 domain 平均 5-7 个类型副本**，最长链路 7 层
- **类型副本规模**：258 个 Rust legacy struct + 131 个 ffi UniFFI Record + 15 个 web 手写 TS interface + 同数量 proto generated TS（命名冲突 snake vs camel）
- **手写转换样板**：backend ~1612 行（49 函数）+ Rust core proto_convert ~300 行 + ffi/dto 30+ From impl ≈ **2200 行纯样板**
- **每次 list_pods**：4-5 次 serde_json 转换跨 wasm/JS 边界
- **类型源真相**：proto schema 在 L3 是 SSOT，但 L4/L4'/L7 各自再镜像一遍 → DRY 违反

## 2. 9 层数据形状盘点

### L1 DB (PostgreSQL)
20+ 表，13 个核心 domain。snake_case 列名。JSONB 字段用于 `runners.host_info` / `loops.config_overrides` / `pods.config_overrides` 等灵活字段。

| Domain | 表 | 列数 | JSONB |
|---|---|---|---|
| pod | pods | 19 | (无) |
| channel | channels | 12 | (无) |
| runner | runners | 14 | host_info |
| ticket | tickets | 18 | (无) |
| loop | loops | 36 | prompt_variables, autopilot_config, config_overrides |

### L2 Backend GORM (Go)
`backend/internal/domain/*/`。PascalCase 字段名 + `json:` snake_case tag。`*string` / `*int64` nullable。158 个 struct 总数。**计算字段**：`Pod.IsMember` / `Pod.AliasDisplay` 用 `gorm:"-"` 不入库。

### L3 Wire (Connect-RPC proto)
**实际 39 个 service**（β agent 误报为 1 个）+ ~150 个 message。snake_case 字段。已稳定，是真正的 SSOT。

代表 message 字段数：proto.pod.v1.Pod (28) / proto.channel.v1.Channel (16) / proto.runner_api.v1.Runner (18) / proto.ticket.v1.Ticket (~20)。

### L4 Rust core in-memory cache
- **types crate**（待删）：17 个 legacy serde 文件，258 个 pub struct/enum，134 KB
- **state crate**：13 个 *_state.rs，cache 类型 = legacy types::Pod / Channel / Runner
- **services crate**：17 个 service，提供 `xxx_json() -> String` / `set_xxx(json)` / `xxx_connect(bytes)` 三套接口
- **api-client crate**：32 个 module，**已基本 100% Connect-RPC**（β 误报 — 仅 runner.rs 残留 3 个 REST 方法）
- **events / persistence / auth**：全部用 legacy types

### L4' 客户端持久化（agent ε 补充审计）
- **Rust persistence crate** (`clients/core/crates/persistence/`)：
  - 后端：InMemoryBackend（wasm/web）+ SqliteBackend（iOS/desktop native）
  - schema：`kv_store(tbl, key, data BLOB)` + `kv_index(tbl, key, field, value)`
  - 6 个 Repo（Pod/Channel/Runner/Ticket/Loop/Message），全部 serde_json 序列化 **legacy types::Xxx**
  - 同步策略：state cache 修改时**同步**写 Repo（无事务、错误被吞）
- **iOS Keychain**：仅 auth tokens，App cache 重启丢失（无持久化）
- **Web localStorage**：仅 tokens + blockstore pending ops + workspace 偏好；wasm 用 InMemoryBackend
- **Desktop Electron**：localStorage 同步到磁盘

### L5 wasm bridge (Rust ↔ JS)
- 30 个 service wrapper + 13 个 state wrapper + node-bridge 26 个 command 文件（共 ~331 napi methods）
- **474 个 #[wasm_bindgen] method**：~92 JSON-in + ~118 JSON-out + ~136 connect-bytes + ~128 typed
- **155 个 JSON 接口完全无 TS 调用方**（dead），仅 ~10 个仍在被使用

### L6 Web TS
- 22 个 `*Connect.ts` adapter（约 176 个导出函数）
- **15 个手写 TS interface**（`PodData` 等 snake_case）
- 同时存在 proto 生成的 TS 类型（`@proto/pod/v1/pod_pb.ts`，camelCase）
- 52 个 zustand store（核心 12 个），共 ~190 次 JSON.stringify/parse 调用
- UI components 接收手写 interface 形状

### L7 UniFFI bridge (Rust ↔ Swift)
- 13 个 service struct，约 60 个 `#[uniffi::export]` method
- **131 个 #[uniffi::Record/Enum]** 跨 12 个 dto 模块
- 完全镜像 legacy types crate（手写 `From<types::Pod> for PodDto`）
- 字段保留 snake_case（违反 Swift 命名约定但保持链路一致）

### L8 iOS Swift (TCA)
- 10 个 Feature 模块 + DesignSystem
- TCA State **直接持有 UniFFI Record**（`pods: [PodDto]`），无中间 Swift struct
- SwiftUI View 直通 UniFFI Record 字段（`pod.agent_slug` snake_case）

## 3. 转换边界详解

### 主路径（Pod list 为例）

```
L1 pods 表 (PostgreSQL)
  ↓ GORM ORM (auto, json:"pod_key" tag)
L2 domain.Pod struct (Go)
  ↓ backend/api/connect/pod/convert.go::toProtoPod() [142 行]
L3 proto.pod.v1.Pod (proto binary wire)
  ↓ Connect-RPC binary OR JSON
  ↓ api-client/modules/pod.rs::list_pods_connect()
  ↓ prost decode
L4 proto_pod_v1::Pod (Rust prost type)
  ↓ services/proto_convert.rs::pod::from_proto() [~40 行/domain]
L4 types::Pod (Rust legacy serde)
  ↓ services/pod.rs 写入 cache
L4 state::PodState.pods (Vec<types::Pod>)
  ↓ persistence/repos/pod_repo.rs::save_pod() [if SqliteBackend]
L4' kv_store BLOB (SqliteBackend JSON) ← iOS/desktop only

读路径分叉到 L5-L6 (Web) 和 L7-L8 (iOS)：

[Web 路径]
  ↓ wasm/service_pod.rs::pods_json() = serde_json::to_string(state.pods())
L5 String (Rust → JS)
  ↓ wasm-bindgen 跨 boundary
L5 JS String
  ↓ stores/pod.ts: JSON.parse(svc.pods_json())
L6 PodData[] (TS plain object, snake_case)
  ↓ zustand store state
L6 React useStore hook
  ↓ component render
DOM

[iOS 路径]
  ↓ ffi/services/pod.rs::list_pods()
  ↓ ffi/dto/pod.rs::From<types::Pod> for PodDto [手写 30+ 字段]
L7 PodDto (Rust #[uniffi::Record])
  ↓ UniFFI auto-generated Swift binding
L8 PodDto (Swift struct, snake_case 保留)
  ↓ TCA PodListFeature.State.pods: [PodDto]
  ↓ SwiftUI View 接收 PodDto
UIKit/SwiftUI render
```

### 边界统计

| 边界 | 位置 | 行数 | 是否手写 | 是否 JSON 中介 |
|---|---|---|---|---|
| L1↔L2 | GORM tag | 0 | 自动 | 否 |
| L2↔L3 | backend/api/connect/*/convert.go | **1612** | 手写 | 否 (binary or JSON wire) |
| L3↔L4(proto) | api-client/modules/*.rs | ~0 | prost auto | 否 |
| L4(proto)↔L4(legacy) | services/proto_convert.rs | **~300** | 手写 | 否 |
| L4(cache)↔L4' | persistence/repos/*.rs | ~150 | 手写 | 是 (serde_json blob) |
| L4↔L5 (wasm out) | wasm/service_*.rs::pods_json() | ~50 | 手写 | 是 (String) |
| L5↔L6 (JS receive) | stores/*.ts: JSON.parse | ~100 | 手写 | 是 |
| L4↔L7 (UniFFI) | ffi/dto/*.rs From impl | **~600** | 手写 | 否 (typed Record) |
| L7↔L8 | UniFFI generated | 0 | auto | 否 |

**总手写转换样板 ≈ 2900 行**。

### 字段语义不一致点

| 字段类型 | L1 (DB) | L2 (GORM) | L3 (proto3) | L4 (legacy) | L6 (TS) | L8 (Swift) |
|---|---|---|---|---|---|---|
| nullable string | NULL | `*string` | `string=""` | `Option<String>` | `string \| undefined` | `String?` |
| nullable int | NULL | `*int64` | `int64=0` | `Option<i64>` | `number \| undefined` | `Int64?` |
| timestamp | TIMESTAMPTZ | `time.Time` | `string` ISO8601 | `Option<String>` | `string` | `String` |
| enum status | `varchar` | `string` | `enum` | `enum PodStatus` | `string` literal union | `enum PodStatusDto` |
| JSONB | `jsonb` | `json.RawMessage` | `string` | `Option<serde_json::Value>` | `unknown` | `String` |

**关键风险**：proto3 默认值（`""`、`0`、`false`）vs legacy `Option<T>=None`。
往返时无法区分"字段未设置"和"字段为零值"。

## 4. 13 Domain 横切表

| Domain | L1 DB cols | L2 GORM fields | L3 proto fields | L4 legacy fields | L4' persisted | L6 TS手写 | L7 ffi Record |
|---|---|---|---|---|---|---|---|
| pod | 19 | 41 | 28 | 33 | ✅ PodRepo | PodData (22) | PodDto (30+) |
| channel | 12 | 16 | 16 | 14 | ✅ ChannelRepo | ChannelData | ChannelDto |
| runner | 14 | 20 | 18 | 8 | ✅ RunnerRepo | RunnerData | RunnerDto |
| ticket | 18 | 23 | ~20 | 15 | ✅ TicketRepo | TicketData | TicketDto |
| loop | 36 | 39 | ~30 | LoopData/LoopRunData | ✅ LoopRepo | LoopData | LoopDataDto |
| message | N | N | N | ChannelMessage (14) | ✅ MessageRepo | (映射 ChannelMessage) | ChannelMessageDto |
| mesh | (聚合) | (聚合) | MeshTopology+Node+Edge | 5 struct | ❌ | MeshTopology | MeshTopologyDto |
| autopilot | (子表) | ~10 | AutopilotController | 4 struct | ❌ | AutopilotData | AutopilotDto |
| blockstore | 5+ | 8+ | Block/Op | 11 struct | ❌ | Block | BlockDto |
| repository | 1 | 1 | Repository | 9 struct | ❌ | Repository | RepositoryDto |
| billing | 2+ | 2+ | Subscription/Plan | 8 struct (R1c 后) | ❌ | (无手写) | BillingOverviewDto |
| user | 2+ | 3+ | User | User+UserIdentity (auth.rs) | ❌ | User | UserDto |
| organization | 1 | 1 | Organization | Organization+OrgMemberView | ❌ | Organization | OrganizationDto |

**注**：L4' 持久化仅 6 个 domain（pod/channel/runner/ticket/loop/message），其它 domain 不持久化客户端。

## 5. 痛点定位 (量化)

1. **类型副本**：13 domain × 平均 6 副本 = ~78 个独立类型定义，~5000 字段定义重复
2. **手写转换样板**：~2900 行（backend convert + Rust proto_convert + ffi/dto From impl）
3. **JSON 边界开销**：每次 list_pods = 4-5 次 serde_json 跨边界
4. **字段语义不一致**：5 处（nullable / timestamp / enum / JSONB / repeated）
5. **命名冲突**：L6 手写 snake_case ↔ proto-generated TS camelCase 共存
6. **L4' 持久化耦合**：state cache 修改同步写 Repo，无事务/批处理/异步
7. **iOS/Web 实际无离线**：除 token 外 cache 全部 in-memory
8. **类型版本管理缺失**：legacy struct 改字段时旧 SQLite 数据反序列化无 migration

## 6. 5 个候选方案对比

每个方案回答 Q1-Q6（详见 plan 文件）。

### 方案 A：proto 作为单一类型源（最激进）

- L4 cache = proto types（加 serde derive，state crate 存 `Vec<proto::Pod>`）
- L5 = wasm `pods_json()` 用 serde 输出 proto 类型 JSON
- L6 = web 收到 snake_case JSON（与现有 TS interface 一致）→ 解码到 proto generated TS type 或 plain object
- L7 = ffi DTO 仅做 UniFFI Record 适配（仍手写，但字段与 proto 一致）
- L8 = TCA 直接持 ffi Record
- L4' = persistence 存 proto types（prost encode 或 serde_json）

**消除**：types crate legacy 文件（17 个，~4000 行）+ proto_convert.rs（~300 行）
**保留**：ffi/dto mirror（UniFFI 限制）+ backend convert.go（L2↔L3 仍需）
**改动估计**：~5000 行 / 80 文件
**风险**：proto3 默认值语义入侵 cache 层（Option<i64> vs i64=0）

### 方案 B：state crate 自有 view types

- L4 cache = state crate 定义 `PodView` 等（保 Option 语义）
- L4 转换 = `From<proto::Pod> for PodView` 在 state crate
- 其它层都用 view types
- types crate 删空，view types 在 state crate

**消除**：types crate legacy（4000 行）
**保留**：转换层（位置变到 state crate）+ proto_convert（或合并）
**改动估计**：~3500 行 / 60 文件
**风险**：仍有转换层，DRY 改善有限

### 方案 C：Rust core 不缓存

- L4 = 不存在
- 各前端自管 state（zustand / TCA）
- ffi/wasm 仅做 service 调用包装

**消除**：state crate 全部 + 大部分 ffi/dto + wasm cache 接口
**新增**：web/iOS 自管 cache 的代码量增加
**改动估计**：~8000 行（包括前端 cache 新代码）
**风险**：业务逻辑下沉 Rust SSOT 设计被推翻

### 方案 D：Connect-RPC JSON wire + 端到端 JSON 对象

- 全程使用 Connect JSON wire（`Content-Type: application/json`）
- Web 直接 fetch JSON，无 wasm 中介
- iOS 用 URLSession + Codable
- Rust core 退化为可选层（仅 desktop/auth）

**消除**：proto_convert.rs + types crate + ffi/dto + wasm wire 路径
**新增**：Web/iOS 直接调 backend
**改动估计**：~7000 行（且影响 backend 路由）
**风险**：原 SSOT 大改；性能（JSON 字符串 vs binary）

### 方案 E：混合（按层选最优）

- L4-L5：proto types + binary 接口（性能）
- L6：TS 用 proto generated 类型（camelCase）
- L7-L8：ffi DTO 镜像 + UniFFI Record
- L4'：proto encode binary blob

**改动估计**：~4500 行 / 70 文件
**风险**：层间命名不一致（snake/camel mix），DRY 改善有限

## 7. 推荐方案

**推荐方案 A（proto 作为单一类型源）+ 局部 view types**：

1. **proto 加 serde derive** → 让 prost 类型直接 JSON-friendly
2. **state crate cache = proto types**（不再有 legacy）
3. **ffi/dto 保留但精简**：每个 DTO 字段与 proto 一致，From impl 仅做命名/类型映射
4. **wasm `*_json()` 接口保留**：内部改用 serde 序列化 proto 类型
5. **删除 proto_convert.rs + types crate legacy 文件**
6. **persistence Repo 改存 proto bytes**（用 prost encode；比 JSON 更紧凑）
7. **L4' iOS Keychain / Web localStorage 保持现状**（设计 OK）
8. **接受 proto3 默认值语义**：cache 层 helper 函数处理（`if v == 0 { None }`）

**论证**：
- proto schema 已经是 SSOT（L3 稳定）；L4 也用它可实现真正单源
- 现有 fmt: snake_case 全链路保持
- 工作量适中（~5000 行）
- ffi 仅做适配（UniFFI 自动 binding 不变）
- L4' persistence 用 prost binary 比 JSON 性能更好

**风险缓解**：
- proto3 默认值：cache 层 helper 函数 `pod.alias.is_empty() => None`
- web 端兼容：TS interface 命名保持 snake_case（与 proto 一致）

## 决策点

请在以下做选择：

- **架构方案**：A / B / C / D / E 或要求设计 F
- **L4' persistence 是否同时升级**：proto bytes vs 保持 JSON
- **iOS/Web 离线能力**：是否在本次重构中扩展持久化范围

进入 R2 Phase 2 实施需要明确以上 3 个决策。
