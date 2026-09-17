# 10 · 跨平台移植评估：Windows / Intel Mac

> 写于 2026-06-18，供以后决策。当前 fanbox 只在 Apple Silicon macOS 上验证过。
> 本文把代码里所有 POSIX / macOS 硬假设逐条列出，附 file:line，估算移植工作面。

## 结论先行

| 目标平台 | 难度 | 一句话 |
|---------|------|--------|
| **Intel Mac (x64 darwin)** | 低 | 基本只是构建目标问题：出 x64 / universal 包 + 重编 node-pty。代码逻辑无需改。 |
| **Windows** | 中高 | 主体工作量是把 env/shell/quoting 这一整层从 POSIX 解耦（广而浅，易漏），外加一个不可控变量——codex CLI 在 Windows 的稳定性。 |

建议：Intel Mac 顺手做，零架构风险。Windows 当独立项目评估，先做下面这张清单的解耦。

---

## 一、Intel Mac（x64 darwin）

Electron / Node 跨架构，macOS 系统 API 完全一致（`pmset`/`scutil`/`osascript`/路径都通用），所以**逻辑零改动**。唯一要处理的：

- **原生模块 node-pty 要为 x64 重编**。`electron/main.js:18-21` 已经是「编译失败就降级、app 仍可用」的容错写法，不会崩，但终端能力会缺。配 universal build 或 x64 build 矩阵即可，node-pty 两个架构都有 prebuild。
- ffmpeg 路径 `electron/main.js:626` 已枚举 `/opt/homebrew` 和 `/usr/local`，Intel 机器装在 `/usr/local` 也能命中。无需改。

工作量：构建配置层面，半天内。

---

## 二、Windows —— 真正有「不可控」成分的地方

### A. 可控但很碎、容易漏（自己的工作量）

**1. 联网环境重建整层是 POSIX 的（最核心）**
- `electron/wechat/env.js:11,14,21` —— 靠 `$SHELL -ilc 'env'`（zsh/bash 登录 shell）抓 PATH/代理/中转站变量。`env.js:17` 对 win32 直接 `return {}`，意味着 **Windows 上完全没有这套环境重建**，claude/codex 子进程大概率找不到命令、或代理变量全丢。需用 PowerShell（`$SHELL -ilc` → `powershell -Command "Get-ChildItem Env:"`）重写一套。
- `electron/wechat/env.js:38` —— `scutil --proxy` 读系统代理是 macOS 专属。Windows 要改读注册表 / WinHTTP 代理。

**2. 起 CLI 走的是 POSIX 登录 shell + POSIX 引号转义**
- `electron/wechat/driver.js`（`loginShell` + `zsh -lc`）+ `driver.js:148` 的 `shq()` 是 POSIX 单引号转义。**Windows cmd/PowerShell 引号规则完全不同**，而 `driver.js:74` 要用它转义那段超长多行的人格 system prompt（`--append-system-prompt`）——这是 Windows 移植最磨人、最易出 bug 的一块。
- `server.js:514` 硬编码 `/bin/zsh -lc command -v`；`electron/wechat/driver.js:65` 用 `command -v`。Windows 要换 `where` / `Get-Command`。

**3. 散落的 POSIX / mac 专属命令**
- `electron/main.js:263,276,286,288` —— 「离开不待机」功能（见下）用 `sudo pmset disablesleep` + `visudo` + `osascript` 提权，整套是 macOS 专属。
- `electron/main.js:119,273` —— 截图监听（shot watcher）是 darwin-only（`main.js:119` 已 `platform !== 'darwin' return`）。Windows 要另写。
- `server.js` 的 `du -sk`（磁盘占用）等 POSIX 命令需换 Windows 等价物。

**4. node-pty 在 Windows 走 ConPTY**
- `electron/main.js:468-481` 的终端 spawn 能跑，但 ConPTY 行为与 mac 有差异，`<term>` 控制终端那套（roster/send）多半要分平台调，测试成本不低。

**5. 凭据位置 / 官方限额窗口**
- claude 在 Windows 的凭据存法与 mac Keychain 不同；`server.js` 里读官方 usage 接口那段（5h/周配额）依赖 mac 凭据路径，需分平台。

### B. 真正不可控（看上游脸色）

- **codex CLI 在 Windows 的原生稳定性**不在我们手里。claude code 有 Windows 原生支持，尚可；codex 的 Windows 支持更不成熟，如果它行为飘，改我们的代码也救不了。
- node-pty / ConPTY 的边角行为差异，部分取决于 Electron + 上游库版本。

---

## 三、和「合盖不待机」use case 的关系（重要）

fanbox 的核心场景是「人离开、合盖，仍能用手机微信遥控本机 agent」。代码里 `electron/main.js:88,261-288` 的 `trySetDisableSleep`（`sudo pmset -a disablesleep 1`）就是为此——**让 MacBook 合盖也不睡**（macOS 上这是唯一能阻止 lid-close sleep 的手段）。

跨平台时这条要重做：
- **Intel Mac**：`pmset` 通用，不用改。
- **Windows**：等价物是 `SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)` 或 `powercfg`，且 Windows 笔记本合盖默认动作可在电源计划里设为「不操作」，比 macOS 更好处理。

> 深层产品判断：如果目标是「7×24 合盖也能遥控」，最稳的方案根本不是和笔记本的电源管理较劲，而是把「大脑」跑在一台不睡的常驻机器上（Mac mini / 小主机 / 云）。跨平台移植前值得先想清楚这个定位——见 docs/09。

---

## 四、移植清单（Windows，按依赖顺序）

1. `env.js`：PowerShell 版环境抓取 + 注册表代理读取
2. `driver.js`：CLI 启动改 Windows shell + 重写 system prompt 的传参方式（优先走 stdin / 临时文件，绕开命令行引号地狱）
3. `server.js` / `driver.js`：`command -v`→`where`、`du`→等价、`/bin/zsh` 去硬编码
4. `main.js`：`pmset` 防睡眠 → `SetThreadExecutionState`；提权逻辑（visudo/osascript）替换或去掉
5. node-pty ConPTY 适配 + `<term>` 控制终端分平台测试
6. 凭据 / 官方 usage 窗口分平台
7. 实测 codex 在 Windows 能否稳定续话（不可控项，先验证再决定是否支持）
