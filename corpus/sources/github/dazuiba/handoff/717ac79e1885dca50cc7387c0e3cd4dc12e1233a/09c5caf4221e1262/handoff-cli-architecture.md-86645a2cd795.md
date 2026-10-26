# handoff CLI 架构文档

## 1. 模块清单与职责

### 顶层模块

| 文件 | 职责 | 核心元素 |
|---|---|---|
| `cli/__init__.py` | 包定义，通过 `importlib.metadata` 暴露 `__version__` | `__version__` |
| `cli/main.py` | **入口点**：解析 `sys.argv`、分派子命令。无参数时若未配置则引导 `handoff init`。 | `main()`, `usage()` |
| `cli/config.py` | **配置层**：加载/合并 `~/.handoff/config.yaml`（数据层）和 `backend_types.yaml`（机制层），提供 `Config` 类。也管理 TUI 主题持久化。 | `Config`, `read_tui_theme()`, `write_tui_theme()`, `write_default_user_config()` |
| `cli/backend.py` | **后端桥接**：将配置转化为 CLI 参数、环境变量。处理 placeholder 替换（`{prompt}`, `{session_id}`, `{model}` 等），区分 claude/codex 两种后端类型。 | `build_args()`, `build_resume_args()`, `set_backend_env()`, `resolve_backend_model()`, `wrap_with_pty()` |
| `cli/core.py` | **持久化层**：SQLite 数据库 (`~/.handoff/runs/handoff.db`)、run_id 分配、seq_code 编解码、遗留数据迁移。 | `get_db()`, `create_run()`, `alloc_seq()`, `counter_to_seq_code()`, `find_run()`, `task_paths()`, `_migrate_legacy_state()` |
| `cli/stream.py` | **流执行引擎**：启动后端子进程、捕获 JSONL 输出、实时进度展示、写入 .out.txt / .result.md。包含两个流解析器。 | `execute_run()`, `ClaudeStreamParser`, `CodexStreamParser`, `make_parser()` |
| `cli/jsonl_parser.py` | **JSONL 共享解析**：逐行解析 claude `stream-json` 格式，提取事件（文本、工具调用、结果等），供 `stream.py` 和 `jsonl_viewer.py` 共用。 | `parse_jsonl_line()`, `ParsedEvent`, `format_event_for_stream()`, `format_event_as_rich()`, `extract_result()` |
| `cli/jsonl_viewer.py` | **JSONL 查看器**：Textual `Screen`，以 4 个 Tab（Stream/Output/Prompt/Result）展示单次运行的完整信息。`handoff list` 中按 Enter 进入的详情页。 | `JsonlViewerScreen`, `make_viewer_screen()` |
| `cli/tui.py` | **TUI 应用**：Textual `App` + `Screen`，渲染运行列表（DataTable），支持自动刷新、杀进程、打开详情、resume。`handoff list` 的交互式界面。 | `RunListApp`, `RunListScreen`, `KillConfirmScreen`, `HandoffTuiApp` |
| `cli/runtime_info.py` | **运行时元数据**：读写 `runs.runtime_info` JSON 字段（PID、token 用量、model、pro 标志）。包含 token 扫描、进程存活检测、进程组杀灭。 | `update_runtime_info()`, `parse_runtime_info()`, `scan_jsonl_usage()`, `kill_process_group()`, `reconcile_running_runs()` |
| `cli/version_check.py` | **版本检查**：非阻塞 daemon 线程，每 24h 查一次 PyPI 最新版本并提示。 | `maybe_check()`, `_check()` |

### commands/ 子模块

| 文件 | 职责 | 核心元素 |
|---|---|---|
| `cli/commands/__init__.py` | 空文件，标记为包。 | - |
| `cli/commands/run.py` | `handoff run` — 派发一次非交互式任务（文件/stdin/--text 作为 prompt），执行后端并等待结果。 | `cmd_run()`, `_execute()` |
| `cli/commands/new.py` | `handoff new` — 预分配 run_id，打印 .prompt.md 路径，可选写入 stdin。 | `cmd_new()` |
| `cli/commands/list.py` | `handoff list` / `ls` — 列出最近运行记录，TUI 模式或纯文本模式。 | `cmd_list()` |
| `cli/commands/resume.py` | `handoff resume` — 向已有 conversation 追加一次非交互式 turn。 | `cmd_resume()` |
| `cli/commands/open.py` | `handoff open` — 以交互模式重新打开某个 conversation（`os.execvp` 替换当前进程）。 | `cmd_open()`, `_open_interactive()` |
| `cli/commands/tail.py` | `handoff tail` — 快捷别名，等价于 `handoff list --follow`。 | `cmd_tail()` |
| `cli/commands/init.py` | `handoff init` — 创建 `~/.handoff/config.yaml`、建立 skill/agent 符号链接。 | `cmd_init()`, `run_init()` |
| `cli/commands/env.py` | `handoff env` — 打印配置/数据路径，不加载 Config（即使配置损坏也能工作）。 | `cmd_env()` |
| `cli/commands/session_target.py` | **共享解析逻辑**：`open` 和 `resume` 共用，将 selector + CLI 参数解析为 `SessionTarget`（backend/session_id/cwd/pro）。 | `resolve_session_target()`, `SessionTarget` |

---

## 2. 模块依赖图

### 2.1 导入关系

```
main.py
  +-- config.py -------------- backend_types.yaml (机制层)
  |                            user_config_template.yaml
  |                            ~/.handoff/config.yaml (数据层)
  |                            ~/.handoff/tui_state.json (TUI 主题)
  +-- core.py ---------------- runtime_info.py
  |                            ~/.handoff/runs/handoff.db (SQLite)
  +-- commands/run.py -------- backend.py
  |   |                         stream.py ---- jsonl_parser.py
  |   |                         runtime_info.py
  |   +------------------------ core.py
  +-- commands/new.py -------- core.py
  +-- commands/list.py ------- core.py, runtime_info.py, tui.py
  +-- commands/open.py ------- backend.py, commands/session_target.py
  +-- commands/resume.py ----- commands/run.py, commands/session_target.py
  +-- commands/tail.py ------- commands/list.py
  +-- commands/init.py ------- config.py
  +-- commands/env.py -------- (仅路径字符串计算, 无后端依赖)
  +-- version_check.py ------- (仅 urllib + threading, 独立运行)
```

### 2.2 核心调用链

```
handoff run:
  main.py -> config.py -> commands/run.py -> backend.py + core.py
                                          -> stream.py + jsonl_parser.py + runtime_info.py

handoff list:
  main.py -> config.py -> core.py + tui.py + jsonl_viewer.py + runtime_info.py

handoff open/resume:
  main.py -> config.py -> session_target.py -> open.py / resume.py -> backend.py

handoff new:
  main.py -> config.py -> core.py

handoff init:
  main.py -> config.py (write_default_user_config) + commands/init.py (创建链接)
```

### 2.3 分层架构

```
+---------------------------------------------+
|  main.py (入口 + 分派)                       |
+--------------+--------------+---------------+
|  commands/   |  config.py   |  backend.py   |
|  各子命令     |  (配置层)     |  (CLI 构建)   |
+--------------+--------------+---------------+
|  stream.py (执行引擎)                        |
|  jsonl_parser.py (JSONL 共享解析)            |
|  tui.py / jsonl_viewer.py (交互展示)          |
+---------------------------------------------+
|  core.py (持久化 + ID 分配)                  |
|  runtime_info.py (运行时元数据)               |
+---------------------------------------------+
|  文件系统: ~/.handoff/                       |
|    config.yaml  runs/handoff.db              |
|    tasks/*.prompt.md, *.out.txt, *.result.md |
|    runs/*.jsonl                              |
+---------------------------------------------+
```

---

## 3. handoff run 命令完整数据流

### 阶段 1：进程启动与参数解析

**入口：`main.py` -> `main()`**

1. 迁移遗留数据: `~/.ds-cli` -> `~/.handoff` (`_migrate_legacy_state`)
2. 非阻塞版本检查 (daemon 线程, 每 24h 一次, `maybe_check()`)
3. 无参数时的特殊处理：
   - 若 `~/.handoff/config.yaml` 不存在 -> 引导 `handoff init`
   - 否则打印 usage 并退出
4. 解析子命令: `subcmd = sys.argv[1]` (例如 "run"), `rest = sys.argv[2:]`
5. 处理 `--help` / `--version` / `init` / `env` 这些不需 Config 的命令
6. 对需要 Config 的命令 (run, list, open, resume, tail, new): `config = Config()` 触发完整的配置加载
7. 分派: `cmd_run(rest, config)`

**参数解析：`commands/run.py` -> `cmd_run()`**

手动遍历 `argv`，支持：
- 位置参数：输入文件路径或 `-`（stdin）
- `--backend <name>` / `--backend=<name>`
- `--cwd <dir>`
- `--slug <slug>` / `--slug=<slug>`
- `--text <prompt...>` / `--text=<prompt>`
- `--pro`（使用 pro_model）
- `--verbose`（打印底层命令到 stderr）
- `--dry-run`（打印命令不执行）
- `--` 分隔符

实现细节：
- `--verbose` 和 `--dry-run` 在遍历前先过滤，位置不影响语义
- `--text` 之后的所有剩余参数都是 prompt（除非遇到 `--`）
- 支持 `=` 分隔的语法 (`--backend=codex`)
- 当输入源是 `TASKS_DIR` 下符合 run_id 格式的 `.prompt.md` 文件时，识别为 "adopted" 模式--使用 `handoff new` 预分配的 run_id

### 阶段 2：配置加载

**`config.py` -> `Config.__init__()`**

1. `_ensure_user_config_exists()`: 如果 `~/.handoff/config.yaml` 不存在 -> `run_init()` 写入模板 + 创建链接

2. 加载机制层: `self._backend_types = _load_yaml("cli/backend_types.yaml")`
   - 包含 `types.claude` / `types.codex`
   - 定义了 `command`, `pty`, `session_flags`, `session_id_flags`, `continue_id_flags`, `resume_flags`
   - `system_prompt` (内置默认，可被用户覆盖)

3. 加载数据层: `self._user = _load_with_includes("~/.handoff/config.yaml")`
   - 递归解析 `include: ` 指令 (支持绝对/相对路径)
   - include 列中的文件先合并，当前文件的键覆盖
   - 循环引用检测 (`_seen` set)

4. `_warn_deprecated()`: 移除废弃的顶层键 (`type_defaults`, `backend_types`, `backend_template`, `fast_backend`, `default_model`, `pro_model`, `default_backend`)

5. `_validate()`: backends 不能为空; 每个 backend 的 type 必须在 backend_types.yaml 中存在; claude 类型的 backend 必须有 model 字段

**后端解析 (`Config.backends` 属性)**：
```
对每个 backend:
  btype = overrides.get("type", "claude")
  base = types.get(btype)        # 机制层: command, pty, flags
  merged = _deep_merge(base, overrides)
    - dict 递归合并
    - list 整体替换（不拼接）
    - 标量覆盖
  merged["type"] = btype
  result[name] = _expand_env_vars(merged)  # ${ENV_VAR} -> os.environ.get()
```

**system_prompt 合并**: `base + "\n\n" + backend 专属指令` (全局在 `backend_types.yaml` 中，用户可通过顶层 `system_prompt` 覆盖)

### 阶段 3：后端进程启动

**`backend.py` -> `build_args()`**

Placeholder 上下文: `{prompt}`, `{session_id}`, `{system_prompt}`, `{model}`, `{pro_model}`, `{model_reasoning_effort}`, `{cwd}`, `{home}`, `{default_model}` (遗留兼容)

**claude 类型参数构建**:
```
args = ["claude"]
+ session_flags: ["-p", "{prompt}", "--dangerously-skip-permissions",
                   "--append-system-prompt", "{system_prompt}",
                   "--output-format", "stream-json", "--verbose",
                   "--include-partial-messages"]
+ [session_id_flags]  如果提供 session_id: "--session-id {id}"
+ [continue_id_flags] 如果 resume: "--resume {id}"
```

**codex 类型参数构建**:
```
args = ["codex"]
+ session_flags: ["exec", "--json", "--skip-git-repo-check",
                   "--sandbox", "workspace-write", "-m", "{model}",
                   "-C", "{cwd}", "{prompt}"]
+ --dangerously-bypass-approvals-and-sandbox (自动注入, 避免 exec 意外中断)
+ [reasoning_effort via -c] 如果配置了 model_reasoning_effort
+ [session_id 通过 continue_id_flags (resume 时): "exec", "resume", "--json", ...]
+ [developer_instructions via -c] 如果有 system_prompt
```

**关键差异**:
- codex 新运行时 session_id 为 None -- 后端通过 `thread.started` 事件报告真实的 thread_id
- codex resume 时使用 `continue_id_flags` **替换** `session_flags` -- 因为 `codex exec resume` 不接受 `--sandbox/-C`
- claude 新运行时 session_id = UUID

**PTY 包装 (`wrap_with_pty`)**:
- claude: `["script", "-q", "/dev/null"]` + args (使 CLI 在 PTY 中运行)
- codex: `pty: []` -- 不包装

**环境变量 (`set_backend_env`)**:
- claude 类型是 "hermetic" 的：先清除 8 个 `ANTHROPIC_*` 变量，防止从宿主 session 继承污染
- 然后从 backend 的 `env` 块设置变量
- 如果未明确设置 `CLAUDE_CONFIG_DIR`，默认为 `~/.claude`

**Token 就绪检查 (`ensure_backend_token_ready`)**:
- 只检查使用 `ANTHROPIC_AUTH_TOKEN` 的 backend (如 deepseek)
- 空值或 `<...>` 占位符 -> `sys.exit(2)` 并给出明确提示

### 阶段 4：JSONL 流处理

**`stream.py` -> `execute_run()`**

```
1. 启动子进程 (Popen)
   - stdin=DEVNULL (prompt 在 argv 中; PTY 不读 stdin)
   - stderr=STDOUT (合并)
   - preexec_fn=os.setsid (新建进程组，方便 kill)

2. 保存 PID 和 start token 到 runtime_info

3. 主循环: 逐行读取 proc.stdout
   - 写入 .jsonl 文件
   - parser.feed(line) -> 解析为 (kind, payload) 事件
   - handle_events(): session 事件更新 DB; progress 事件打印+写 .out.txt

4. parser.finish() 刷新缓冲区

5. 结果判定:
   - 若 parser.result_text 存在且非错误 -> finish_success()
   - 若 claude 类型 -> 回退到 extract_result(jsonl_path) 扫描 JSONL
   - 否则 -> 错误状态
```

**`ClaudeStreamParser`** (claude `--output-format stream-json`):
- `feed(line)`: 调用 `jsonl_parser.parse_jsonl_line()` 解析 JSONL
- 识别事件:
  - `stream_event.content_block_start` (tool_use) -> "tool" 事件
  - `stream_event.message_start` -> model 名
  - `assistant` 中的 text / tool_use -> "text" / "tool" 事件
  - `user` 中的 tool_result -> "info" 事件
  - `system` 中的 status / task_started -> "info" / "task" 事件
  - `result` -> "result" / "error" + result_text
- `_flush()`: 延迟去重 (相同 plan_text 连续出现只输出一次)
- `result_text`: 来自 JSONL `type: "result"` 事件中的 `result` 字段

**`CodexStreamParser`** (`codex exec --json`):
- `feed(line)`: 直接 `json.loads()` 解析
- 识别事件:
  - `thread.started` -> 提取 thread_id 作为 session_id，发出 `("session", tid)` 事件
  - `item.started/item.completed` -> command_execution / reasoning / agent_message 文本
  - `turn.completed` -> 累计 usage，最终结果 = 最后一条 agent_message
  - `turn.failed` -> 提取错误信息
  - `error` -> 暂时性错误 (如重连重试)，打印但不中止

**事件处理 (`handle_events`)**:
- `("session", id)` -> 更新 runs 表的 session_id (只有 Codex 后端产生)
- `("progress", text)` -> 打印到 stderr + 追加到 .out.txt

### 阶段 5：结果落盘

**文件结构 (`core.py` -> `task_paths()`)**:
```
~/.handoff/tasks/
  <run_id>.prompt.md   -- 原始 prompt (Markdown)
  <run_id>.out.txt     -- 完整日志 (进度行 + RESULT= 标记)
  <run_id>.result.md   -- 最终结果 (Markdown)

~/.handoff/runs/
  handoff.db           -- SQLite 数据库
  <run_id>-<uuid>.jsonl -- 原始 JSONL 流
```

**成功路径 (`finish_success`)**:
1. 更新 DB: status="success", 清除 PID, 持久化 usage
2. 写入 result.md
3. 在 out.txt 末尾写入 `RESULT=<result_path>` 标记
4. 打印 result 到 stdout + `sys.exit(0)`

**中断处理 (Ctrl+C)**:
- SIGINT -> 5s 超时 SIGKILL
- status="interrupted", result.md 写入 "INTERRUPTED\n"
- `sys.exit(130)`

**失败路径**:
- status="error", 诊断信息写入 stderr, JSONL 路径写入 .result.md

**SQLite 表结构**:

`runs`:
```sql
CREATE TABLE runs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    seq         INTEGER NOT NULL,
    seq_code    TEXT NOT NULL,
    run_id      TEXT NOT NULL UNIQUE,     -- "0611-ds-03-fix-auth"
    run_day     TEXT NOT NULL,
    uuid        TEXT NOT NULL UNIQUE,
    session_id  TEXT,
    cwd         TEXT NOT NULL,
    prompt      TEXT NOT NULL,
    jsonl_path  TEXT NOT NULL,
    created_at  TEXT DEFAULT (datetime('now','localtime')),
    status      TEXT DEFAULT 'running',
    backend     TEXT DEFAULT '',
    runtime_info TEXT DEFAULT '{}'
);
```

`run_counters`:
```sql
CREATE TABLE run_counters (
    day     TEXT PRIMARY KEY,
    last_n  INTEGER NOT NULL
);
```

**run_id 格式**: `<mmdd>-<backend2>-<SEQ_CODE>-<slug>`
- 例如 `0611-ds-03-fix-auth`
- `SEQ_CODE`: 01-99 -> A0-ZZ (最大 1035 = ZZ)
- `slug`: 用户输入，清洗为最多 3 段 `[a-z0-9-]`

**seq_code 编码**:
- 1-99: 两位数 `n`
- 100+: `first = chr('A' + (n-100) // 36)`, `second = base36(n-100 % 36)`
- 总共 26x36+99 = 1035 个槽位

---

## 4. 关键细节

### 4.1 异常处理

| 环节 | 异常类型 | 处理方式 |
|---|---|---|
| YAML 解析 | `yaml.YAMLError` | 打印错误 + `sys.exit(1)` |
| 配置缺失 | 无 backends / 无 model | 打印诊断 + `sys.exit(1)` |
| Token 缺失 | ENV_VAR 未设置 | `ensure_backend_token_ready` 检查 + `sys.exit(2)` |
| 文件不存在 | `OSError` / `FileNotFoundError` | 打印路径 + `sys.exit(2)` |
| stdin 不可读 | TTY 但无输入 | 提示 + `sys.exit(2)` |
| 重复派发 | adopted run_id 已存在 | 拒绝 + `sys.exit(2)` |
| 子进程中断 | `KeyboardInterrupt` | SIGINT -> 5s 超时 SIGKILL -> status="interrupted" -> `sys.exit(130)` |
| 子进程失败 | `proc.returncode != 0` | 回退到 `extract_result()` 扫描 JSONL -> status="error" -> `sys.exit(1)` |
| PID 不存在 | `ProcessLookupError` | `reconcile_running_runs` 将 running -> error |
| TUI Kill 失败 | `KillRunError` | 通知用户，不崩溃 |
| 日配额超额 | `n > 1035` | ROLLBACK + `sys.exit(2)` |
| 网络请求失败 | PyPI 不可达 | 静默忽略 |

### 4.2 配置优先级和覆盖机制

```
最高: CLI 参数 (--backend, --pro, --cwd, --slug)
  |
用户配置: ~/.handoff/config.yaml
  |-- backends.<name>.*    用户定义的 backend 属性
  |   |-- type             决定使用哪个机制层定义
  |   |-- model/pro_model  模型名
  |   |-- env              环境变量 (支持 ${ENV_VAR} 展开)
  |   +-- system_prompt    backend 专属指令 (可选, 追加到全局后)
  +-- system_prompt        全局 system_prompt (覆盖内置默认)
  |
机制层: cli/backend_types.yaml (不可被用户配置覆盖)
  |-- system_prompt        内置默认 (用户可覆盖)
  +-- types.<type>.*       command, pty, flags 模板
  |
最低: 内置默认值 (type="claude", 默认主题等)
```

**Deep-merge 规则**: dict 递归合并；list 整体替换；标量覆盖。

**include 指令**: config.yaml 可包含 `include: other.yaml` (string 或 list)，先合 include 文件，再合当前文件的键。循环引用由 `_seen` set 检测。

### 4.3 后端类型差异

| 特性 | claude | codex |
|---|---|---|
| 命令 | `claude` | `codex` |
| PTY | `script -q /dev/null` | 无 |
| 输出格式 | `--output-format stream-json` | `--json` |
| 流解析器 | `ClaudeStreamParser` (通过 jsonl_parser) | `CodexStreamParser` (直接 json.loads) |
| session_id 来源 | 调用方提供 UUID | 后端在 thread.started 事件中报告 |
| session_id_flags | `--session-id {id}` | 空 (codex 自行分配) |
| continue (resume) | `--resume {id}` 追加到 session_flags | `exec resume` 替换 session_flags |
| interactive resume | `--resume {id}` | `resume {id}` |
| system_prompt | `--append-system-prompt` 标志 | `-c developer_instructions=...` (JSON 编码) |
| reasoning_effort | 不支持 | `-c model_reasoning_effort="xhigh"` |
| sandbox | 不适用 | `--sandbox workspace-write` |
| bypass | 不适用 | `--dangerously-bypass-approvals-and-sandbox` |
| 环境变量 | hermetic--清除 ANTHROPIC_* 继承 | 不清除 (保留宿主环境) |
| TUI 流 Tab | 显示 | 隐藏 (codex 不产生标准 stream-json) |

### 4.4 任务 ID 分配和存储

**run_id 生成 (`create_run`)**:
1. `BEGIN IMMEDIATE` (防并发)
2. 读 `run_counters` 表获取今日 last_n -> n = last_n + 1
3. `INSERT OR REPLACE run_counters (day, n)`
4. `seq_code = counter_to_seq_code(n)`
5. `backend_abbrev`: deepseek->ds, codex->cx, 其他->前2字符
6. `run_id = f"{mmdd}-{b2}-{seq_code}-{clean_slug}"`
7. 生成 UUID
8. `session_id` = 参数的 session_id 或 UUID (claude 新 session) 或 None (codex)
9. `INSERT INTO runs (...)`

**handoff new + adopt 流程**:
- `handoff new --backend codex --slug my-fix` -> `alloc_seq()` 递增计数器，打印 `.prompt.md` 路径，用户写入 prompt
- `handoff run /path/to/0720-cx-05-my-fix.prompt.md` -> `_is_adopted_path()` 识别为已分配路径，验证 backend2 一致性，`create_run(run_id_override=...)` 不复增计数器，不重写 .prompt.md

**resume 时的 session 关联**:
- `handoff resume <seq>` 在 runs 表中创建新行 (新 run_id / 新 seq / 新 uuid)
- 但 `session_id` 指向父运行的 session_id
- 多个 turn 共享同一个后端 session，但每个 turn 有独立的 run_id 和文件

**reconcile_running_runs** (runtime_info.py):
- 检查所有 status="running" 的行
- 通过 `process_group_alive(pid)` 检测进程是否还在运行
- 通过 `process_start_token` 校验 PID 复用 (同一 PID 但启动时间不同 -> 视为已死)
- 标记为 "error" 状态，记录 `error_reason: "process_missing"`
