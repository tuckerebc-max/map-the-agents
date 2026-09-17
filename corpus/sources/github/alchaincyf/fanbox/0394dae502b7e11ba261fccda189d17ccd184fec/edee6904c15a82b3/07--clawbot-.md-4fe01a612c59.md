# 07 · 微信 ClawBot 集成规划

> 目标:在 FanBox 顶栏增加一个微信入口,用户点击弹窗扫码,把「微信 ClawBot」接到本机终端里的 Claude Code / Codex,并为后续接入 OpenClaw、Hermes、Kimi Code 等留好扩展位。
> 路线决策:走微信官方插件 + OpenClaw 中转(安全合规优先,不走非官方逆向桥)。
> 本期交付:规划文档(不写代码)。

---

## 一、调研结论:微信 ClawBot 是什么

微信官方在 2026 年 3 月上线的正规插件能力,走官方插件通道,不是第三方逆向,基本不担心封号。

**核心机制**

- 官方 npm 包 `@tencent-weixin/openclaw-weixin`,配套 CLI `@tencent-weixin/openclaw-weixin-cli`。
- 安装一条命令:`npx -y @tencent-weixin/openclaw-weixin-cli install`,或在 OpenClaw 里 `openclaw plugins install "@tencent-weixin/openclaw-weixin"`。
- 登录靠扫码:终端运行登录命令后打印一个二维码,用微信扫,手机弹出「将 OpenClaw 连接到微信」,点绿色「连接」,几秒后微信通讯录里多出一个叫「微信 ClawBot」的联系人。之后在微信里跟它对话,就等于驱动本机的 agent。
- token 存本地,手机端微信登出即断连。

**能力边界**

| 能力 | 状态 |
|------|------|
| 个人微信、私聊 | 支持 |
| 收发图片 / 语音 / 文件 | 支持 |
| 群聊 | 当前插件不支持 |
| 连接对象 | 官方插件默认只认 OpenClaw,硬绑定到 `main` agent |

**最关键的一条事实**:微信官方插件本身**不能直接连 Claude Code / Codex**,它只跟 OpenClaw 对话。所以「让微信驱动终端里的 claude code」这件事,必须有一个 OpenClaw 在中间。这正是本规划选定路线的由来。

---

## 二、为什么这条路线反而扩展性更好

OpenClaw 不是一个聊天机器人,它是一个 agent runtime(网关守护进程),原生就把各家终端 CLI 当作「后端」来驱动:

- **Claude Code 作为 CLI 后端**:`openclaw config set agents.defaults.model.primary 'claude-cli/claude-opus-4-8'`,OpenClaw 直接调本机 Claude Code 进程,复用本地会话、不用单独管 API key。
- **Codex 走 ACP**(Agent Client Protocol):OpenClaw 以子进程 + JSON-RPC over stdio 的方式驱动 Codex。
- 现成的统一编排器 `claw-orchestrator`(GitHub: Enderfga/claw-orchestrator)把 Claude Code / Codex / Gemini / Cursor 包成一个统一 runtime,并且号称 first-class OpenClaw 插件支持。可作为「多 agent 编排」的加速选项。

这意味着我们想要的那层「可扩展抽象」OpenClaw 已经替我们做好了:

```
微信 ClawBot ──(官方插件)──> OpenClaw 网关 ──(agent runtime / CLI backend)──> Claude Code
                                          ├──> Codex (ACP)
                                          ├──> OpenClaw 原生 agent
                                          ├──> Kimi Code   ← 加一条 runtime 配置即可
                                          └──> Hermes …    ← 加一条 runtime 配置即可
```

**加一个新 agent = 在 OpenClaw 里多一个 agent runtime 条目 + 在 FanBox 注册表里多一行**。这天然满足「轻松扩展到 openclaw / hermes / kimi code」的诉求,我们自己不用碰微信协议。

OpenClaw 关键事实备查:

- 配置文件 `~/.openclaw/openclaw.json`,严格 JSON Schema,多一个逗号或未知 key 会导致网关起不来。
- 网关守护进程默认端口 18789,命令:`openclaw gateway start / stop / restart / status`,`--install-daemon` 可开机自启。
- 支持定义多个 agent,可把某个微信账号绑定到指定 `agentId`(改 `accounts.json` 的 binding 段)。这是「微信选择连哪个 agent」的底层支点。

---

## 三、整体架构

### 3.1 三个进程层

```
┌─────────────────────────────────────────────┐
│ FanBox (Electron 渲染进程)                     │
│  顶栏微信图标 → 连接弹窗(状态机 + 二维码 + 选agent) │
└───────────────┬─────────────────────────────┘
                │ IPC: wechat:*
┌───────────────▼─────────────────────────────┐
│ FanBox 主进程 (electron/main.js)               │
│  · 检测/安装/拉起 OpenClaw 网关                  │
│  · 跑微信插件登录命令,捕获二维码与连接状态        │
│  · 维护「可连接 agent 注册表」                    │
└───────────────┬─────────────────────────────┘
                │ spawn / openclaw CLI / 读 stdout
┌───────────────▼─────────────────────────────┐
│ OpenClaw 网关 (常驻守护进程, :18789)            │
│  · 官方微信插件 (@tencent-weixin/openclaw-weixin)│
│  · agent runtime: claude-cli / codex-acp / …    │
└─────────────────────────────────────────────┘
```

### 3.2 FanBox 侧的扩展抽象:可连接 agent 注册表

为了让前端 UI 和后端解耦,在 FanBox 里定义一个静态注册表(不是过度抽象,就是一份配置数据,直接对应用户需求里点名的几个 agent):

```js
// 可连接 agent 注册表(FanBox 侧)
const CONNECTABLE_AGENTS = [
  {
    id: 'claude-code',
    label: 'Claude Code',
    icon: 'claude.svg',
    openclawAgentId: 'fanbox-claude',     // OpenClaw 里对应的 agent id
    runtime: { kind: 'cli', model: 'claude-cli/claude-opus-4-8' },
    enabled: true,
  },
  {
    id: 'codex',
    label: 'Codex',
    icon: 'codex.svg',
    openclawAgentId: 'fanbox-codex',
    runtime: { kind: 'acp', command: 'codex', args: ['acp'] },
    enabled: true,
  },
  // 扩展位:下面这些先 enabled:false,确认可用后开
  // { id:'openclaw', label:'OpenClaw 原生', runtime:{kind:'native'} },
  // { id:'kimi',     label:'Kimi Code',    runtime:{kind:'cli', command:'kimi'} },
  // { id:'hermes',   label:'Hermes',       runtime:{kind:'acp', command:'hermes'} },
];
```

新增一个 agent 的成本被压到两步:注册表加一行 + OpenClaw 配置加一段 runtime。UI、IPC、弹窗逻辑全部不动。

> 第二维度扩展(可选,先记下不做):OpenClaw 本身还支持 Telegram / WhatsApp 等 channel。哪天想把「微信入口」泛化成「IM 入口」,可以把注册表再加一层 channel 维度。本期不碰,但抽象上给它留了位置。

---

## 四、FanBox 端 UI / UX 方案

### 4.1 顶栏图标

位置:`public/index.html` 的 `<div class="topbar-actions">` 容器内,与现有 `#btn-changes` `#btn-recent` `#btn-terminal` 并列。沿用 `.ghost-btn` 样式,无需新增 CSS。

```html
<button id="btn-wechat" class="ghost-btn" title="连接微信 ClawBot">
  <!-- 微信 SVG icon -->
</button>
```

事件绑定放在 `app.js` 的 `bindEvents()`(约 4056 行)附近,点击调用 `wechatPanel()`。

### 4.2 连接弹窗(复用现有 modal 模式)

复用项目已有的 `.input-overlay` + `.input-dialog` 弹窗模式(参考 `app.js` 的 `memoryPanel()` ~1500 行、`releasePanel()` ~1560 行),Escape 关闭、毛玻璃背景、跟主题走色。

弹窗内部是一个**状态机**,这是整个交互的核心:

```
[环境检测]
   ├─ 未装 OpenClaw      → 状态 A:引导安装
   ├─ 装了但网关没起      → 状态 B:一键启动网关
   └─ 网关在线           → 状态 C:选择要连接的 agent
                              │
                              ▼
                         [选 Claude Code / Codex / …]
                              │
                              ▼
                         状态 D:生成二维码(loading)
                              │
                              ▼
                         状态 E:展示二维码,提示「用微信扫一扫」
                              │
                  ┌───────────┼───────────┐
                  ▼           ▼           ▼
              扫码成功      二维码过期     用户取消
                  │           │
                  ▼           ▼
              状态 F:已连接   回到状态 E(刷新二维码)
              展示:连的是哪个 agent + 断开按钮
```

每个状态的文案要克制、给明确下一步,不堆术语。状态 A/B 是首次使用体验的关键,决定用户会不会卡在第一步。

### 4.3 二维码怎么拿到(技术难点 1)

微信插件登录命令把二维码打印成终端字符画。直接把字符画塞进弹窗,清晰度和可扫描性都差。正确做法:

1. 主进程 spawn 登录命令,**捕获 stdout**。
2. 从输出里**解析出二维码背后的登录字符串 / URL**(终端二维码本质是把一段 URL 编码成图,我们要拿到那段 URL)。
3. 用前端 QR 库(在 `public/vendor/` 里 vendor 一个 `qrcode` 库,跟项目现有 vendor 习惯一致)**重新渲染成清晰二维码**显示在弹窗。

兜底:万一拿不到原始 URL,只能拿到字符画,就用等宽字体原样渲染字符画(能扫但体验次一档),作为降级方案。

> 待验证:登录命令是否在 stdout 里附带可读的登录 URL/token。这点需要在装好插件后实跑一次确认。它直接决定 4.3 用主方案还是降级方案。

### 4.4 连接后展示对话内容(核心功能,花叔点名要)

连上之后,点微信图标不能只显示「已连接」,要能**看到微信里跟 agent 的全部对话内容**。点图标 → 弹窗分两态:未连接显示扫码;已连接显示对话流(像个迷你聊天记录面板)。

**数据来源(已实测确认):**

- `openclaw sessions list` 列出所有会话。微信来的会话,其 session key 形如 `agent:main:...:openclaw-weixin:<accountId>:direct:<peer>@im.wechat`,据此筛出「微信对话」。每条带 session id、模型、token 用量、最近活跃时间。
- 对话正文以 **JSONL transcript** 本地落盘:`~/.openclaw/agents/main/sessions/<sessionId>.jsonl`(每行一条消息事件,含用户消息与 agent 回复)。FanBox 解析这个文件渲染成对话气泡。
- 实测:微信测试对话生成了 `2e17641b-….jsonl`,内容完整可读。

**已探明的坑:**

- `openclaw message read` 的 channel 枚举里**不含 weixin**(只有 telegram/whatsapp/discord 等)。所以读微信对话**不能走 `message read`**,要走「`sessions list` 定位 + 读 transcript JSONL」这条路。
- 网关 file log 对微信消息**遮蔽明文**(隐私边界),正文只在 session transcript 里。读 transcript 是正道,别去 parse 日志。
- transcript 是 JSONL(逐行 JSON 事件),含 system / user / assistant / tool 等多种事件类型,渲染时要过滤出 user + assistant 的可读文本,跳过 system prompt 和 tool 调用噪声。

**FanBox 侧实现:**

- 新增 IPC `wechat:sessions`(列微信会话)、`wechat:transcript`(传 sessionId 读对话,主进程解析 JSONL 返回结构化消息数组)。
- 弹窗已连接态:上方一行连接信息(连的哪个 agent / 哪个微信号)+ 下方对话流。可加轮询或 `fs.watch` transcript 文件实现准实时刷新(项目已有 `fs:watch-set` 机制可复用)。

### 4.5 连接成功的检测(技术难点 2)

持续读登录命令的 stdout,匹配成功标志(如 token saved / login success 之类),命中后主进程通过 `wechat:connected` 事件推给前端,弹窗切到状态 F。同时把「当前连的是哪个 agent」持久化到 `localStorage`,下次打开弹窗直接显示已连接态。

---

## 五、IPC 与进程管理设计

沿用项目现有的 `domain:action` IPC 命名约定(如 `pty:spawn`),新增一组 `wechat:*`:

**主进程 `electron/main.js` 新增:**

```js
ipcMain.handle('wechat:env',     () => detectEnv());          // 返回 OpenClaw 是否安装/网关状态
ipcMain.handle('wechat:install', () => installOpenclaw());    // 引导/执行安装
ipcMain.handle('wechat:gateway', (e, action) => gateway(action)); // start/stop/status
ipcMain.handle('wechat:agents',  () => listConnectableAgents()); // 读注册表
ipcMain.handle('wechat:login',   (e, agentId) => startLogin(agentId)); // 跑登录,流式回二维码
ipcMain.handle('wechat:status',  () => connectionStatus());
ipcMain.handle('wechat:disconnect', () => disconnect());
ipcMain.handle('wechat:sessions', () => listWeixinSessions());   // 列微信会话(sessions list 筛 weixin)
ipcMain.handle('wechat:transcript', (e, sid) => readTranscript(sid)); // 读 transcript JSONL → 消息数组
// 主进程 → 渲染进程 推送:
//   wechat:qrcode    (二维码数据/URL)
//   wechat:connected (连接成功)
//   wechat:log       (安装/登录过程日志,给状态 A/B 用)
```

进程管理可复用 main.js 里已有的 `child_process`(`execFile` / `exec` 已在用,如 line 269 `osascript`、line 616 `lsof`)。OpenClaw 网关建议用 `openclaw gateway start --install-daemon` 交给系统守护,FanBox 只负责检测和拉起,不自己长期持有那个进程,避免 FanBox 退出把网关带走。

**preload `electron/preload.js` 新增:**

```js
contextBridge.exposeInMainWorld('fanboxWechat', {
  env:        () => ipcRenderer.invoke('wechat:env'),
  install:    () => ipcRenderer.invoke('wechat:install'),
  gateway:    (a) => ipcRenderer.invoke('wechat:gateway', a),
  agents:     () => ipcRenderer.invoke('wechat:agents'),
  login:      (id) => ipcRenderer.invoke('wechat:login', id),
  status:     () => ipcRenderer.invoke('wechat:status'),
  disconnect: () => ipcRenderer.invoke('wechat:disconnect'),
  onQrcode:    (cb) => ipcRenderer.on('wechat:qrcode', cb),
  onConnected: (cb) => ipcRenderer.on('wechat:connected', cb),
  onLog:       (cb) => ipcRenderer.on('wechat:log', cb),
});
```

命名风格与现有 `window.fanboxPty` / `fanboxRec` / `fanboxFs` 等保持一致。

---

## 六、关键难点与风险

| # | 风险 / 难点 | 影响 | 对策 |
|---|------------|------|------|
| 1 | 二维码原始 URL 能否从 stdout 解析 | 决定弹窗二维码清晰度 | 实跑验证;拿不到则降级渲染字符画 |
| 2 | OpenClaw 首次安装重 | 拖累首次体验 | 状态 A 做清晰引导;考虑检测 npx 一键装;明确告诉用户这是一次性成本 |
| 3 | OpenClaw 配置文件脆(JSON Schema 严格) | 改坏了网关起不来 | FanBox 改配置前先备份;改完 `gateway status` 校验,失败回滚 |
| 4 | 手机端微信登出即断连 | 用户困惑「为什么断了」 | 状态 F 写明这条;断连时弹窗给出原因而非空白 |
| 5 | 微信账号与某 agent 的绑定关系 | 多 agent 时路由到谁 | 用 OpenClaw 的 per-account binding;一个微信号绑一个 agentId,切换 = 重新 login |
| 6 | Codex / Kimi / Hermes 的 runtime 实测可用性 | 扩展位是否真能用 | 注册表里先 `enabled:false`,逐个实测通过再开 |
| 7 | 官方插件协议演进 | 版本不兼容 | 锁插件版本(2.x 需 OpenClaw ≥2026.3.22),升级前验证 |

---

## 七、分期路线图

**P0 · 可行性钉死(动手前必做)**

本机实测现状(2026-06-15):

- 网关在线:`openclaw gateway status` = running (pid 723, active, 连通 ok)。监听 127.0.0.1:18789。有几个非阻塞告警(代理环境变量、PATH、dingtalk 插件重复 id),建议跑一次 `openclaw doctor --repair`,不影响功能。
- 默认 agent `main`,模型 `openai-codex/gpt-5.4` —— 即「OpenClaw → Codex」这条已经通了。
- 微信插件 `@tencent-weixin/openclaw-weixin` v2.4.3:**已装但 disabled**,`accounts.json` 空(未绑账号)。
- 当前活跃 channel 只有钉钉。`kimi-claw` v0.24.11 连接器已 enabled(扩展位里的 Kimi 已在场)。

所以本机 P0 = 只差「启用微信插件 + 扫码登录」一步,精确步骤:

```bash
# 1. 启用微信官方插件
openclaw config set plugins.entries.openclaw-weixin.enabled true
# 2. 重启网关使其生效(会短暂打断钉钉)
openclaw gateway restart
# 3. 扫码登录(终端打印二维码;用微信扫 → 手机点「连接」)
openclaw channels login --channel openclaw-weixin
# 4. 微信里给「微信ClawBot」联系人发一句话,确认能驱动 main agent(codex)
# 5.(可选)把 main 或新建 agent 的模型切到 claude code,验证驱动 Claude Code:
#    openclaw config set agents.defaults.model.primary 'claude-cli/claude-opus-4-8'
```

P0 同时要钉死**难点 1**:第 3 步执行时**捕获其 stdout**,确认终端二维码旁边是否附带可读的登录 URL / token 字符串。拿得到 → FanBox 弹窗用「解析 URL 再用 JS 重渲染清晰二维码」主方案;拿不到 → 用降级方案(等宽字体原样渲染字符画)。这是全规划里唯一无法靠查资料拍死、必须实跑的点。

### P0 实测结果(2026-06-15,已通过)

**难点 1 解决,走主方案。** `openclaw channels login --channel openclaw-weixin` 的 stdout 同时给出:
1. unicode 半块字符画二维码(可作降级方案);
2. 一条明确标注的可读登录 URL:`https://liteapp.weixin.qq.com/q/<id>?qrcode=<token>&bot_type=3`。

→ FanBox 弹窗主方案成立:捕获 stdout,正则提取这条 `liteapp.weixin.qq.com` URL,用 JS QR 库重渲染清晰二维码。

**端到端链路打通。** 实测流程:`config set ...enabled true` → 重启网关 → login 打印二维码 → 微信扫码 → 日志输出「已将此 OpenClaw 连接到微信」→ `accounts.json` 写入账号 id → 微信通讯录出现「微信ClawBot」。后端 main agent 当前模型即 `openai-codex/gpt-5.4`,即微信消息驱动 Codex 已通。

**实测踩到的坑(写进 FanBox 实现):**

- **登录后必须重启网关**:login 存好凭证后,正在运行的网关不会热加载新 channel(日志报 `did not restart it: invalid channels.start channel`)。必须 `gateway stop && gateway start` 后,channel 才变 `running`。FanBox 的 `wechat:login` 成功回调里要接一步网关重启。
- **`gateway restart` 在本机用 launchctl bootstrap 会报 I/O error**(服务已 bootstrap)。可靠做法是 `gateway stop` 然后 `gateway start`(stop 会清理 stale 进程,start 重新 bootstrap)。FanBox 封装重启时用 stop→start,不要用 restart。
- **二维码有时效**,FanBox 弹窗要做过期刷新(重新跑 login 取新 URL)。
- 本机已有 `kimi-claw` 连接器 enabled、codex 作 main 模型,扩展位里的 Kimi/Codex 实际已具备,P3 接入成本极低。

**P1 · MVP(最小可用)**
- 顶栏微信图标 + 弹窗骨架(复用现有 modal)。
- 只支持 Claude Code 一个 agent(注册表里就一条)。
- 状态机做通 C→D→E→F(假设环境已就绪,先不做状态 A/B 的安装引导,文档里告诉用户先手动装好 OpenClaw)。
- 二维码渲染 + 连接成功检测。
- **已连接态展示对话内容**(4.4):点图标读 transcript JSONL,渲染微信对话流。这是花叔点名的核心功能,P1 就要有(至少静态加载一次,刷新可放 P2)。

**P2 · 完整体验**
- 加 Codex,弹窗里支持选 agent(注册表两条)。
- 补状态 A/B:OpenClaw 未安装/未启动的检测与一键引导。
- 连接状态持久化、断开重连、错误态文案。

**P3 · 扩展开放**
- 打通注册表机制,接入 OpenClaw 原生 / Kimi Code / Hermes(逐个实测后 `enabled:true`)。
- 文档化「如何加一个新 agent」,让以后扩展只改注册表 + OpenClaw 配置。

---

## 八、已定决策(2026-06-15)

1. **首次安装**:FanBox 只做检测 + 给一键复制的安装命令,由用户自己跑。FanBox 不替用户自动装 OpenClaw。
2. **微信图标视觉**:用微信官方绿色气泡 icon(不做单色线性版)。
3. **P0 验证环境**:在花叔本机做。

> 本机环境实况(已检测):node v26 / claude 2.1.170 / codex 0.139.0 / **openclaw 2026.5.18 已装**,且 `~/.openclaw/openclaw-weixin/` 微信官方插件**早已安装**(2026-03-22)。即本机 P0 不需要任何重型安装,直接进入「核实现有链路能否驱动 Claude Code」。「首次安装偏重」这个风险只对未来分发给其他用户时成立。

---

## 附:信息来源

- 微信官方插件 npm:`@tencent-weixin/openclaw-weixin`
- OpenClaw 微信 channel 文档:https://docs.openclaw.ai/channels/wechat
- OpenClaw CLI 后端(claude-cli/codex):https://docs.openclaw.ai/gateway/cli-backends
- OpenClaw agent runtimes:https://docs.openclaw.ai/concepts/agent-runtimes
- OpenClaw 配置/网关:https://docs.openclaw.ai/gateway/configuration
- 统一编排器 claw-orchestrator:https://github.com/Enderfga/claw-orchestrator
- 自定义 agent 绑定(改 accounts.json binding):腾讯云/V2EX 社区教程
- 非官方任意-agent 桥 WeClaw(本路线未采用,留作对照):https://github.com/fastclaw-ai/weclaw
