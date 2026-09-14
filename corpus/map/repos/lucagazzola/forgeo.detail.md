# lucagazzola/forgeo -- full detail

[Back to orientation](forgeo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lucagazzola/forgeo/6e709a374a66b964c97e7e6a9c6665ad89fcac08/12163ac21a1508c3.json](../../../wiki/dossiers/lucagazzola/forgeo/6e709a374a66b964c97e7e6a9c6665ad89fcac08/12163ac21a1508c3.json)

## specifications (1 claim(s))

- [observation/documented] Forgeo is described as a software factory for a coding agent: given a backlog and an agent CLI, it picks the next runnable task, runs the agent, commits the result, and tracks progress in plain files plus a web dashboard. -- evidence: [README.md#L16-L16](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L16-L16), [README.md#L18-L18](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L18-L18) (`clm_594d2b0a06fb928745b63a6ab93dd90e231f50b1395cd9b99e74f52bd2a50d5a`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Optional review_mode: branch commits successful agent work to a forgeo/review/<TASK_ID> branch, marks the task REVIEW, and waits for a human merge/Complete or Request-changes action instead of committing directly to main. -- evidence: [README.md#L20-L24](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L20-L24), [CHANGELOG.md#L43-L49](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L43-L49) (`clm_033db32ad36c6264814c50f9fbd2b4c45cc2c89f0b92d9a7cf898db5bb4ee497`)
- [observation/documented] A silent no-change success (exit 0 with unchanged tree) marks the task BLOCKED for human review rather than FAILED, unless the agent opts in via no_changes_exit_code. -- evidence: [CHANGELOG.md#L141-L145](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L141-L145) (`clm_7dbff1382a95bee2b761e38d4b87fc5af4618dcdd69efb81870625934e13d092`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors must run pytest, ruff check, and mypy src/forgeo before opening a PR, and CI enforces the same quality gates on pull requests. -- evidence: [CONTRIBUTING.md#L69-L77](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L69-L77), [CONTRIBUTING.md#L19-L19](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L19-L19), [CONTRIBUTING.md#L21-L25](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L21-L25) (`clm_09bdd8288a200c68a853e249deb1c2ec784dd7964a94fb7410d6d4b1d57f1eb5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The agent contract is agent-agnostic: any CLI that reads the FORGEO_TASK environment variable can be used, and the backlog task's acceptance criteria are rendered into that instruction. -- evidence: [README.md#L20-L24](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L20-L24), [CONTRIBUTING.md#L36-L43](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L36-L43) (`clm_eba71376f94ccc43fdcd8122179470d2c36a8d98dcb3d0f5e06f1aef70882334`)
- [observation/documented] CLI surface includes forgeo init, validate, start, once, run --task, status, stop, restart, instance add/list, and web, with the daemon running one cycle per interval_minutes. -- evidence: [README.md#L65-L68](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L65-L68), [README.md#L44-L46](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L44-L46), [README.md#L74-L81](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L74-L81), [README.md#L102-L107](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L102-L107) (`clm_87f5d225a4b747829d7c08e2d54ccc6932fcb867e8463f7afb3e43076b2cd91d`)
- [observation/documented] The central dashboard (forgeo web) defaults to 0.0.0.0:8790, aggregates all registered instances, and exposes a per-instance HTTP API under /api/instances/<name>/ including task create/edit/delete, reopen, config PUT, and daemon start/stop/restart endpoints. -- evidence: [CHANGELOG.md#L330-L347](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L330-L347), [CHANGELOG.md#L360-L374](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L360-L374), [README.md#L58-L59](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L58-L59), [README.md#L83-L83](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L83-L83) (`clm_d3ab0ad618a850d3121b80de9a49700266442b0db7cb0a8a8abf0bea23f9c2fb`)
- [observation/documented] The dashboard supports optional bearer-token auth via forgeo web --token (or a token in ~/.config/forgeo/web.toml), returning 401 on /api/* routes without it; without a flag or token file it stays open by default. -- evidence: [CHANGELOG.md#L248-L256](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L248-L256), [README.md#L83-L83](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L83-L83) (`clm_2befd9e1af1a0fbed374262864d41fbd66b8f4f415c96a2a4bea2f547bc336f4`)

## memory-state (1 claim(s))

- [observation/documented] Forgeo persists runtime state in .forgeo/ (backlog, logs, blockers) plus runs.jsonl run history, daemon.state.json, and rotating backlog.json.bak snapshots restored when the backlog is found corrupt. -- evidence: [README.md#L48-L48](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L48-L48), [CHANGELOG.md#L266-L270](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L266-L270), [CHANGELOG.md#L206-L210](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L206-L210), [CHANGELOG.md#L279-L284](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L279-L284), [CHANGELOG.md#L378-L388](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L378-L388) (`clm_45865eca87b7c24ad6b3cc32463f495ffb164e7a68286a6d013da838481257a5`)

## orchestration (1 claim(s))

- [observation/documented] Task selection picks the oldest OPEN task whose dependencies are all COMPLETED (or whose run_at schedule is due); REVIEW blocks dependants while independent tasks keep running. -- evidence: [CHANGELOG.md#L286-L293](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L286-L293), [README.md#L20-L24](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L20-L24) (`clm_05a85f0e27f653315e7806b989bdfaced92fc2efab2ed2f7c78e6c6fdb6093bb`)

## tools-permissions (1 claim(s))

- [observation/documented] An optional Docker sandbox runs the agent isolated, with a configurable image, network (default none), read-only mounts, and the repo bind-mounted at the same path. -- evidence: [README.md#L89-L94](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L89-L94), [README.md#L96-L96](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L96-L96) (`clm_4c4fb2e9da456b43d8ae4916c3f92400c07fdf7f2979e1c4a543b41f743e8a29`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Backlog providers are file, HTTP, GitHub, GitLab, and Jira; file/HTTP exchange the full document while Jira/GitHub/GitLab sync issues individually, with engine state stored in a hidden forgeo block or issue properties. -- evidence: [README.md#L48-L48](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L48-L48), [CHANGELOG.md#L83-L106](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L83-L106), [README.md#L120-L120](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L120-L120) (`clm_502eb40bb2bfa12d35a0c2bbb8886fb3c50303cdab94f239c9b2271ea829dbef`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

