# zclllyybb/opengiraffe -- full detail

[Back to orientation](opengiraffe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zclllyybb/opengiraffe/40180a705d315c6d54aca045fe80646dd9ceb443/b25edc3f887cf4c8.json](../../../wiki/dossiers/zclllyybb/opengiraffe/40180a705d315c6d54aca045fe80646dd9ceb443/b25edc3f887cf4c8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The system is described as a persistent daemon-based multi-agent system using opencode to explore, plan, implement, and review code changes, with tasks running in parallel git worktrees. -- evidence: [README.md#L7-L7](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L7-L7) (`clm_6edc40b15353de5bafd9bec25b3e10c88544ec4a9d6a8271f19b97618d5c73d9`)
- [observation/documented] A free-running Project Explorer agent continuously crawls the codebase to map structure and dependencies, surfacing refactors, bugs, and missing tests, and its proposals become prioritized tasks. -- evidence: [README.md#L23-L31](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L23-L31), [README.md#L37-L37](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L37-L37), [README.md#L43-L43](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L43-L43) (`clm_0b4d7766ba7179e12bc118a871de7686f386d98cca80becf85f9bfdf4a2ca773`)
- [observation/documented] The system scans repositories for TODO/FIXME comments and uses an AI analyzer to score each item's feasibility and difficulty, producing a backlog that can be selectively dispatched as tasks. -- evidence: [README.md#L23-L31](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L23-L31), [README.md#L53-L53](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L53-L53) (`clm_0347ac01d4688494556d6e84c979ec96a47c8389b044e2be299147c5e2248eb4`)

## design-choices (1 claim(s))

- [observation/documented] Each task runs in its own git worktree and branch (agent/task-<id>-<slug>) so parallel tasks do not conflict; completed branches can be published with a push, revised with human feedback, or cleaned. -- evidence: [README.md#L120-L120](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L120-L120), [README.md#L92-L118](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L92-L118), [README.md#L13-L17](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L13-L17) (`clm_f38f25403ace2d37a9dbdcc163905ade68f939104a3d78f3f364840c4dcc9a07`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the project uses pytest with tests in tests/ where all model I/O is mocked, run via python -m pytest tests/ -v; setup involves cloning, pip installing requirements, and copying config.yaml.template. -- evidence: [README.md#L138-L138](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L138-L138), [README.md#L203-L203](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L203-L203), [README.md#L141-L141](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L141-L141), [README.md#L207-L207](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L207-L207), [README.md#L134-L135](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L134-L135) (`clm_43a5a9c1c4c513e0fdf209e8c3e37569af8cb98d85ac855d123422fb271e549e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A CLI exposes daemon control (start/stop/status), task submission and dispatch, TODO scanning/analysis/dispatch, and a synchronous run-one command for testing a single task. -- evidence: [README.md#L160-L164](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L160-L164), [README.md#L174-L175](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L174-L175), [README.md#L167-L171](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L167-L171), [README.md#L155-L157](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L155-L157) (`clm_9be778ad228b262eb0492c6354e4d6a2613dccc99ee29c3599597b79883e2b0d`)
- [observation/documented] A web dashboard (FastAPI with single-file HTML/JS) served by default on port 8778 provides tabs for the Explorer loop, task management, scanned TODOs, and live model configuration that persists to config.yaml. -- evidence: [README.md#L59-L88](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L59-L88), [README.md#L179-L179](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L179-L179), [README.md#L181-L186](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L181-L186) (`clm_3ca2d173bb5943d6815c3e23a298acb5285f41bbb0d61d78c0911c14d4835c6a`)

## memory-state (1 claim(s))

- [observation/documented] Tasks, agent runs, and review history are stored in SQLite, so the daemon can be stopped and resumed after a reboot. -- evidence: [README.md#L13-L17](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L13-L17) (`clm_2321c170e48e377e07980ae065f13978f2f930720148a3264dde720c5e0e5702`)

## orchestration (2 claim(s))

- [observation/documented] Tasks follow a Planner → Coder → Reviewer pipeline: the planner assesses complexity and may split work into sub-tasks dispatched independently, and rejected code re-enters a retry loop up to a max_retries limit before failing. -- evidence: [README.md#L92-L118](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L92-L118) (`clm_da028f348fa1bfe15b76d22784ab9b0a62a323a5f44263081739a473e00cde1e`)
- [observation/documented] Multiple reviewer models vote on each change, and all reviewers must approve for a task to pass; any REQUEST_CHANGES feeds reviewer feedback back to the coder. -- evidence: [README.md#L23-L31](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L23-L31), [README.md#L92-L118](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L92-L118) (`clm_493879dd99ecb73f373d99ab813d0eb1eddea01255e1b0e8c2aef5b4671cdd83`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt lists fastapi, uvicorn, pyyaml, aiosqlite, jinja2, python-multipart, and pytest as dependencies. -- evidence: [requirements.txt#L1-L7](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/requirements.txt#L1-L7) (`clm_ef6c888076b2cef2229a43b350446cf9afd96d5506eef909ea5df492f519b9ee`)
- [observation/documented] Running the product requires Python 3.11+, the opencode CLI configured with at least one model provider, and a git repository to operate on. -- evidence: [README.md#L126-L128](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L126-L128) (`clm_7aaaa7164e3519847225bd89432390c4d4e3576511b27e2460c4769fa9b33db7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

