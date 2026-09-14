## Lime v1.144.1

### 新功能

- 无。

### 修复

- 修复 Windows CLI npm 构建缺少 `WriteFile` 所需 `windows-sys` `Win32_System_IO` feature 的问题。

### 优化与重构

- 无。

### 测试与质量

- 补跑 TUI Rust 测试、格式检查与版本一致性门禁；跨平台 CLI 产物由 GitHub Actions 验证。

### 文档

- 无。

### 其他

- 修复版不覆盖已发布的 `v1.144.0` tag；CLI npm 发布继续使用 GitHub Actions npm Trusted Publishing。

**完整变更**: `v1.144.0` -> `v1.144.1`
