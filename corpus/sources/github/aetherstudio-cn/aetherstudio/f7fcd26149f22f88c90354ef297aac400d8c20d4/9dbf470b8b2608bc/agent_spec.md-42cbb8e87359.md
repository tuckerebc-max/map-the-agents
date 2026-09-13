# Aether Editor — Agent Coordination Spec

## User Goal

将 Aether 打造为真正生产级的 Rust 驱动编辑器：
- **Git 支持**：完整的仓库管理、分支、提交、状态显示
- **SSH 远程连接**：远程文件系统浏览、编辑、终端
- **常用文件类型**：文本、代码、图片等已有 lexer 支持
- **极致 UX/UI**：苹果级毛玻璃透明感（Acrylic/Glass），视觉层次清晰
- **零阻尼交互**：60fps 渲染，输入延迟 < 16ms，无掉帧
- **AI 配置**：设置面板可配置大模型 API 密钥（OpenAI、Claude、Kimi 等）

## Non-Goals
- 不添加 LSP/DAP 新功能（已有基础，但本次不扩展）
- 不添加插件系统新功能（已有基础，但本次不扩展）
- 不添加多语言本地化（保持中文/英文混合）
- 不添加云同步或协作编辑

## Current Repo Facts

- **Stack**: Rust workspace, Windows Win32 API + Direct2D 渲染
- **Package Manager**: Cargo
- **Workspace**: 8 crates declared in root Cargo.toml
  - `aether-core` — buffer, lexer, workspace (已有)
  - `aether-render` — Direct2D 渲染, theme (已有)
  - `aether-win32` — Win32 窗口, UI, 输入处理 (已有)
  - `aether-remote` — Git, SSH, 容器远程 (已有)
  - `aether-lsp` — LSP client (已有)
  - `aether-dap` — DAP client (已有)
  - `aether-tree-sitter` — 语法高亮 (已有)
  - `aether-plugin` — 插件系统 (已有)
- **Missing crates**: `aether-ai`, `aether-shared`, `aether-terminal` (目录存在但无代码)
- **Entry point**: `aether-win32/src/main.rs` → `run()`
- **Render**: `aether-win32/src/render.rs` — Direct2D 1.1, 无 GPU 后处理
- **Current UI**: 深色主题，纯不透明背景，类似 VS Code 的 dark+
- **Build**: 环境无 Rust 工具链，无法编译验证；需保证代码逻辑正确

## Architecture Decisions

1. **毛玻璃效果**: 使用 Windows 10/11 `SetWindowCompositionAttribute` + `DWMWA_USE_IMMERSIVE_DARK_MODE` 实现 Acrylic/Blur Behind，同时在 Direct2D 渲染层使用半透明画刷和模糊背景。
2. **AI 配置**: 新建 `aether-ai` crate 负责 AI 配置存储和 API 调用；`aether-shared` 提供跨 crate 的 settings 序列化；设置 UI 在 `aether-win32` 中实现。
3. **Git/SSH**: `aether-remote` 已提供底层能力；`aether-win32` 需要完善 UI 集成（Git 面板、SSH 连接对话框、远程文件树）。
4. **零阻尼**: 确保 render loop 无阻塞，输入事件直接修改状态并请求重绘，避免额外分配。

## Shared Interfaces

### Settings 序列化（aether-shared）
```rust
// aether-shared/src/settings.rs
pub struct AppSettings {
    pub ai: AiSettings,
    pub ui: UiSettings,
    pub remote: RemoteSettings,
}

pub struct AiSettings {
    pub provider: String, // "openai", "claude", "kimi"
    pub api_key: String,
    pub base_url: Option<String>,
    pub model: String,
}
```

### AI API（aether-ai）
```rust
// aether-ai/src/lib.rs
pub struct AiClient { ... }
impl AiClient {
    pub fn new(config: &AiSettings) -> Self;
    pub async fn complete(&self, prompt: &str) -> Result<String, AiError>;
}
```

### Git 面板数据（aether-win32）
- `GitIntegration` 结构体已存在，需要扩展为显示 staged/unstaged 文件列表
- 需要 `render_source_control_sidebar` 完整实现

## Task Slices

| Worker | Scope | Allowed Paths | Forbidden Paths |
|--------|-------|---------------|-----------------|
| UI-Glass | 毛玻璃效果 + 主题优化 | `aether-render/src/`, `aether-win32/src/render.rs`, `aether-win32/src/window.rs`, `aether-win32/src/theme.rs` (新建) | `aether-core/`, `aether-remote/` |
| AI-Config | AI crate + 设置系统 + 设置 UI | `aether-ai/src/`, `aether-shared/src/`, `aether-win32/src/settings.rs` (新建), `Cargo.toml` (workspace) | `aether-core/`, `aether-remote/`, `aether-render/` |
| Git-SSH | Git 面板 + SSH 连接 UI + 远程文件树 | `aether-win32/src/git.rs`, `aether-win32/src/ssh.rs` (新建), `aether-win32/src/render.rs` (sidebar 部分), `aether-remote/src/` (修复编译) | `aether-core/`, `aether-render/` |

## Merge Order

1. UI-Glass → mainline (渲染层变更最基础)
2. AI-Config → mainline (新建 crate，不冲突)
3. Git-SSH → mainline (UI 层变更，依赖 render 结构)

## Final Verification

- 代码逻辑检查：所有新增文件需有完整实现，无 `todo!()` 或 `unimplemented!()`
- 接口一致性：检查跨 crate 引用路径正确
- Cargo.toml 完整性：新 crate 需正确添加到 workspace
