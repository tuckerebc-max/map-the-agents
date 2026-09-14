# Open Decisions

## 2026-07-14 — 官网重设计的浏览器视觉验收

- **状态：** blocked by current sandbox, not waived.
- **现状：** `next dev` 在 `0.0.0.0:3000` 和 `127.0.0.1:3100` 均因 `listen EPERM` 无法启动；Playwright CLI 无法建立可用会话；Chrome headless 对本地静态导出执行后以 exit 134 退出。
- **已完成证据：** `npm run lint`、普通 `npm run build`、GitHub Pages 静态导出、源码 token 扫描和 WCAG 对比度计算均通过。
- **触发条件：** 在允许 localhost 监听与浏览器进程的正常开发机或 CI preview 环境中运行视觉 QA。
- **验收项：** 1440、1024、768、375 四档无横向滚动；桌面/移动导航可用；中英文切换持久化；复制命令成功/失败反馈可感知；控制台无错误；`prefers-reduced-motion` 生效。

## 2026-07-14 — 受限沙箱中的 Rust PID 生命周期测试

- **状态：** deferred environment validation; unrelated to the website change.
- **现状：** `RUST_TEST_THREADS=1 cargo test --workspace --quiet` 中 `umadev-agent` 有 1504/1506 项通过，以下两项在当前沙箱失败：
  - `run_lock::tests::a_live_local_lock_with_a_foreign_boot_id_is_not_reclaimable`
  - `runtime_proof::tests::reclaim_kills_our_own_tracked_alive_pid`
- **判断依据：** 两项都依赖本机 PID/boot-id/liveness 行为；本次 diff 未修改任何 Rust 文件，串行执行仍以相同进程回收断言失败。
- **触发条件：** 在具备正常进程枚举、signal 和 boot-id 能力的 macOS/Linux CI runner 上重跑 `cargo test --workspace`。
- **边界：** 不为让无关测试在受限沙箱变绿而修改产品进程语义。

## 2026-07-14 — 二级页面迁移到 Delivery Blueprint 视觉系统

- **状态：** parked after homepage sign-off.
- **已决定边界：** 本轮重构官网首页、全局 tokens、字体交付和导航入口；`/docs`、`/gallery`、`/changelog`、`/contributors` 保持原有内容与路由，并通过兼容 token 继续可用。
- **待决定：** 是否把四个内容型二级页面的布局也从旧 HUD 结构迁移为新的 technical editorial 结构。
- **触发条件：** 首页视觉方向确认后，按文档阅读、版本时间线、图片画廊、贡献者名录四种内容模型分别设计，不能用一个通用卡片模板套完。
