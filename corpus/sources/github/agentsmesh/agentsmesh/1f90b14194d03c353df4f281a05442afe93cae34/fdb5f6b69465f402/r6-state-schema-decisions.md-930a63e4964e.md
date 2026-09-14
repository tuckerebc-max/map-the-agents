# R6 — 客户端 state schema 落地决策

承接 R2（proto schema 作为跨域 SSOT）。R6 的问题：客户端 Rust state
crate 是否需要为每个域单独定义 `proto/<svc>_state/v1` schema（带
client-derived 字段），还是继续直用 wire proto？

## 三类划分

按"Rust 是否对 wire 数据加业务逻辑"分三类：

### A 类：透明代理（直用 wire proto）

`*_state.rs` 只是 `Vec<ProtoType>` 容器，没有外部 HashMap，没有客户端衍生字段。
直接用 `proto.<svc>.v1.*` 即可。

| State | 内容 |
|---|---|
| `git_provider_state` | `Vec<RepositoryProvider>` + `Vec<ProviderRepository>` |
| `loop_state` | `Vec<LoopData>` + `Vec<LoopRunData>` |
| `mesh_state` | `Option<MeshTopology>` 单例 |
| `org_state` | `Vec<Organization>` + `Vec<OrgMemberView>` |
| `repo_state` | `Vec<Repository>` + `Vec<Branch>` |
| `user_state` | `User` + `Vec<UserIdentity>` |

**决策**：零代码改动。这些已经符合"proto schema = SSOT"原则。

### B 类：有客户端衍生状态（需要 state schema）

`*_state.rs` 维护一份 wire 之外的衍生数据，UI 依赖它渲染：

| State | 衍生字段 | 决策 |
|---|---|---|
| `channel_state` | `unread_count` / `mention_count` / `last_message` / `last_activity_at` | **已落地**：`proto.channel_state.v1.Channel` 加 4 个 client-derived 字段（tag 100+），HashMap 删除，状态内联到 Channel struct |

### B-候选但保留 HashMap（按访问模式与持久化语义判断）

不是所有衍生状态都该升到 schema。channel 的内联成功因为同时满足三条件：
**批量读取**（sidebar 一次列出所有 channel 的 unread）+ **必须持久化** +
**事件驱动可重建**。下表的衍生字段不全部满足这些条件，故保留 HashMap：

| State | 衍生字段 | 不上 schema 的理由 |
|---|---|---|
| `pod_state.init_progress` | pod 初始化进度 | 单实体查询；ephemeral；运行后丢弃 |
| `autopilot_state.iterations` / `thinking_history` | controller 迭代历史 | 单实体；session-local；bounded（200/100）|
| `blockstore_state.nest_children` / `backlinks` | 衍生索引 | 可从 refs 廉价重建；YAGNI |
| `blockstore_state.last_op_id` | 同步 watermark | 候选未来内联到 `Workspace.last_op_id`；当前 HashMap 工作良好 |
| `ticket_state.pods_by_ticket_slug` | ticket → pods cache | 单实体；optional cache |
| `ticket_state.view_mode` | UI 偏好 | 跨页全局偏好；候选未来移到 user preferences proto |
| `ticket_state.board_columns` | kanban 列分组 | 按需重建；不需独立持久化 |

## 复盘

R6 把 channel 这一**特例**（sidebar 批量场景）正确升到了 schema 字段。
其它 state crate 走 audit 路径而非机械复用 channel pattern：避免 schema 膨胀
和无意义的 proto 字段（默认值序列化也有成本）。

未来如果发现新的批量 + 持久化 + 可重建场景，再单独按 channel 同样路径
新增 `proto/<svc>_state/v1/*.proto`。
