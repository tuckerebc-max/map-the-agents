# datasciencemonkey/coding-agents-databricks-apps -- full detail

[Back to orientation](coding-agents-databricks-apps.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/22db77d5/2fe2784a/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/d20a4ad5ff34cf66.json](../../../wiki/dossiers/22db77d5/2fe2784a/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/d20a4ad5ff34cf66.json)

## specifications (1 claim(s))

- [observation/documented] The project lets users run Claude Code, Codex, Gemini CLI, Hermes Agent, and OpenCode in a browser, connected to their Databricks workspace with no local setup. -- evidence: [README.md#L11-L11](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L11-L11) (`clm_2c312c020563fec223ea957d5a782674ed3d3526cb81df252e4d71f61e04df94`)

## components (3 claim(s))

- [observation/documented] The repo bundles five agents: Claude Code (with 39 Databricks skills and 2 MCP servers), Codex, Gemini CLI, Hermes Agent, and OpenCode, each installed at boot. -- evidence: [README.md#L35-L35](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L35-L35), [README.md#L33-L33](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L33-L33), [README.md#L27-L27](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L27-L27), [README.md#L25-L25](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L25-L25), [README.md#L29-L29](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L29-L29), [README.md#L31-L31](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L31-L31) (`clm_cd1c2f644b9d0529774dd95ea3a2cc97eb61e9a594bc008150c33f2d0701ebf7`)
- [observation/documented] Two MCP servers are included: DeepWiki for AI-powered questions about GitHub repos, and Exa for web search and code context retrieval. -- evidence: [README.md#L206-L209](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L206-L209) (`clm_21b9b68e5af32cc4aa2f6994ed8fa3ac75f676edddfb61d17888ab1ad785b184`)
- [observation/documented] Claude Code sessions are traced to a Databricks MLflow experiment via a Stop hook calling mlflow.claude_code.hooks.stop_hook_handler(), configured at startup by setup_mlflow.py in ~/.claude/settings.json. -- evidence: [README.md#L124-L130](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L124-L130), [README.md#L122-L122](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L122-L122), [README.md#L102-L102](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L102-L102) (`clm_4becb9b86603a45185f0ea383bf043417b90860561a336fd58ffc2ef621d846f`)

## design-choices (4 claim(s))

- [observation/documented] On first terminal session the user pastes a short-lived PAT that configures all CLIs; tokens auto-rotate every 10 minutes and are not persisted across restarts by design. -- evidence: [README.md#L35-L35](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L35-L35), [README.md#L372-L372](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L372-L372) (`clm_fd10da3b8c603463d3f1abf934c6795e10ddcaeb54fde23d6078484696d9a9f7`)
- [observation/documented] An approved design doc records bundling skills into the image rather than downloading at startup, citing faster startup, no network dependency, and predictability as reasons. -- evidence: [docs/plans/2025-02-03-bundled-skills-design.md#L3-L4](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/plans/2025-02-03-bundled-skills-design.md#L3-L4), [docs/plans/2025-02-03-bundled-skills-design.md#L164-L170](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/plans/2025-02-03-bundled-skills-design.md#L164-L170) (`clm_de688e39c3fa54d88ea86f6d1c5ae6bd85737757609c7b56a8d5993f20c027f9`)
- [observation/documented] A tmux evaluation concluded tmux should be removed in favor of localStorage-based session recovery, because tmux caused visual artifacts, resize conflicts, and keybinding clashes. -- evidence: [docs/2026-03-08-tmux-evaluation.md#L13-L18](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L13-L18), [docs/2026-03-08-tmux-evaluation.md#L3-L5](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L3-L5) (`clm_1a15a7eaff68ece1180dfdc7d7c4e15a165ae65350e42953182e55c1bdfbda95`)
- [observation/documented] Production Gunicorn is configured with workers=1 because PTY state is process-local, threads=16, gthread worker class, and a 60-second timeout for long-lived WebSocket connections. -- evidence: [README.md#L376-L376](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L376-L376) (`clm_42fdf7f9be53988b7c5315ad179c2dc8497052143ecc3345383f8dccf2400da3`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The app bundles 39 skills: 25 Databricks skills from ai-dev-kit (agent-bricks, genie, mlflow-eval, unity-catalog, etc.) and 14 superpowers skills (TDD, debugging, review, git-worktrees, etc.). -- evidence: [README.md#L180-L188](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L180-L188), [README.md#L192-L199](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L192-L199), [README.md#L25-L25](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L25-L25) (`clm_44e94e09a3442196ae3fb4553bef6129319b1792183a705301111c80f374916f`)

## interfaces (3 claim(s))

- [observation/documented] The app exposes HTTP endpoints including /health, /api/session, /api/input, /api/output, /api/output-batch, /api/heartbeat, /api/resize, /api/upload, and /api/session/close. -- evidence: [README.md#L325-L338](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L325-L338) (`clm_3075dd5a053442eb47d1c4b96c0b8558d351ce88fca42cd703b66bbe0190f936`)
- [observation/documented] Socket.IO events include join_session, terminal_input, terminal_resize, heartbeat (client-to-server) and terminal_output, session_exited, session_closed, shutting_down (server-to-client). -- evidence: [README.md#L342-L352](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L342-L352) (`clm_2ddf9a5c5b57d24e74f549a9b9acc9ede7be6eef78cf78525644c0db435dedfd`)
- [observation/documented] An MCP flow lets external clients delegate tasks: coda-bridge.py proxies stdio JSON-RPC over HTTP with an injected OAuth token, returning a task_id immediately with results fetched later via coda_inbox/coda_get_result. -- evidence: [README.md#L244-L311](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L244-L311), [README.md#L313-L313](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L313-L313) (`clm_29708a732ca47d0e42992e8a3aed49d36948690333678c2fef28dbb8f10eec59`)

## memory-state (1 claim(s))

- [observation/documented] A state_sync.py process persists Claude Code auto-memory and bash history to /Workspace/Users/{email}/.state/ every 5 minutes, since only /Workspace files survive container restarts. -- evidence: [docs/2026-03-08-tmux-evaluation.md#L40-L42](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L40-L42), [docs/2026-03-08-tmux-evaluation.md#L22-L25](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L22-L25) (`clm_b8f28c94857f46c7e2971994a347516cb7bd99153d681344402100b29d206d6e`)

## orchestration (1 claim(s))

- [observation/documented] At startup, Gunicorn calls initialize_app(), then a background thread runs 5 sequential setup steps followed by 6 agent setups in parallel via ThreadPoolExecutor, with progress reported through /api/setup-status. -- evidence: [README.md#L317-L321](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L317-L321) (`clm_99c1b2a512335f8e4253e281ce48ef508dc4af23e5435f9f692774d9013a8505`)

## tools-permissions (1 claim(s))

- [observation/documented] The app is single-user: the owner is resolved via the app's service principal and Apps API, and authorization checks X-Forwarded-Email against app.creator. -- evidence: [README.md#L372-L372](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L372-L372) (`clm_8798fd54f57140e4ff9975ea5b6a227b07619d08e02fd8ff006f884b31e45a26`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack uses Flask, Flask-SocketIO, Gunicorn, xterm.js, Python PTY, uv, Databricks SDK, Databricks AI Gateway, and MLflow; requirements.lock is hash-pinned and auto-regenerated by CI. -- evidence: [README.md#L383-L425](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L383-L425), [README.md#L433-L433](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L433-L433) (`clm_d8b6daa8c2835a9d1e94516f0283b069346d9797da3bfcdb88e1482bf90c7738`)

## limitations (2 claim(s))

- [observation/documented] The tmux evaluation acknowledges a remaining gap: if Gunicorn kills a worker, PTY file descriptors are lost and the localStorage recovery approach cannot restore those sessions. -- evidence: [docs/2026-03-08-tmux-evaluation.md#L34-L34](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L34-L34) (`clm_afcdbfa036754c14af752bdb5baa1070b47a29a4f00430823dfe9c92c28df6eb`)
- [observation/documented] An earlier design doc lists limitations including no persistence across redeploys, a 12-hour Databricks session limit, and initially no terminal resize signaling. -- evidence: [docs/plans/2026-02-02-web-terminal-design.md#L275-L281](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/plans/2026-02-02-web-terminal-design.md#L275-L281) (`clm_a98a487c13681b0c3e70d6eaf29cf4d95fbcf919770ef302b9956aa51abed2ca`)

## relevance (1 claim(s))

- [observation/documented] The project has moved from a personal handle to Databricks Labs, where development continues. -- evidence: [README.md#L2-L4](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L2-L4) (`clm_53298ba9a0abf7ec97f7da1d27ca9d6c46c5f247acd4472ec722a4dc67fef2a8`)

