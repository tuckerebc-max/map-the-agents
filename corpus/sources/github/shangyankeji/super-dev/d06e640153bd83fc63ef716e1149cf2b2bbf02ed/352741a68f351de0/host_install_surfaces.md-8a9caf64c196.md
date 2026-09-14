# Host Install Surfaces

> 维护者文档。普通用户不需要先读这份安装面差异说明，先运行 `super-dev` 并按 `host-onboard-smoke-*.md` 验收即可。

这份文档只描述宿主触发面与安装差异，不再把内部维护命令当成普通用户入口。

## Core Rule

不同宿主的安装方式和触发词不同，但公开合同应收敛成：

- 终端：`super-dev` / `super-dev update` / `super-dev uninstall`
- 支持 slash 的宿主：`/super-dev` / `/super-dev-work` / `/super-dev-run` / `/super-dev-review` / `/super-dev-seeai`
- 不支持 slash 的宿主：`super-dev:` / `super-dev-work:` / `super-dev-run:` / `super-dev-review:` / `super-dev-seeai:`

## Common Hosts

### Codex CLI

- 触发词：`super-dev:`
- 继续开发时优先直接说：`super-dev: 继续当前流程`

### Claude Code

- 触发词：`/super-dev`
- 继续开发时优先直接说：`/super-dev 继续当前流程`

### Trae / Kiro / Copilot Chat

- 触发词：`super-dev:`
- 继续开发时优先直接说：`super-dev: 继续当前流程`

## 建议顺序

1. 先用 `super-dev` 完成宿主接入
2. 再确认当前宿主对应的触发词
3. 正式开发直接回宿主，用 `/super-dev` 或 `super-dev:` 继续主流水线
4. 只有接入异常时，才回终端使用 `onboard` / `detect` / `doctor` 这类维护命令

## 自定义安装路径

如果宿主没有装在默认目录，自动检测除了命令名和常见安装路径，还支持显式路径覆盖。

- `SUPER_DEV_HOST_PATH_CODEX_CLI=<安装路径>`
- `SUPER_DEV_HOST_PATH_OPENCODE=<安装路径>`
- `SUPER_DEV_HOST_PATH_CURSOR=<安装路径>`

设置后重新执行 `super-dev` 即可；只有维护者在报告明确要求时，才进入 `doctor` 等维护命令。

## 为什么需要这份文档

如果只告诉用户“输入 super-dev”，但不说明当前宿主到底该用 `/super-dev` 还是 `super-dev:`，安装成功也会在第一步就卡住；所以安装面文档必须服务宿主触发，而不是继续扩张终端命令面。
