---
access: public
aliases: []
claim_ids:
- clm_0347ac01d4688494556d6e84c979ec96a47c8389b044e2be299147c5e2248eb4
- clm_0b4d7766ba7179e12bc118a871de7686f386d98cca80becf85f9bfdf4a2ca773
- clm_2321c170e48e377e07980ae065f13978f2f930720148a3264dde720c5e0e5702
- clm_3ca2d173bb5943d6815c3e23a298acb5285f41bbb0d61d78c0911c14d4835c6a
- clm_43a5a9c1c4c513e0fdf209e8c3e37569af8cb98d85ac855d123422fb271e549e
- clm_493879dd99ecb73f373d99ab813d0eb1eddea01255e1b0e8c2aef5b4671cdd83
- clm_6edc40b15353de5bafd9bec25b3e10c88544ec4a9d6a8271f19b97618d5c73d9
- clm_7aaaa7164e3519847225bd89432390c4d4e3576511b27e2460c4769fa9b33db7
- clm_9be778ad228b262eb0492c6354e4d6a2613dccc99ee29c3599597b79883e2b0d
- clm_da028f348fa1bfe15b76d22784ab9b0a62a323a5f44263081739a473e00cde1e
- clm_f38f25403ace2d37a9dbdcc163905ade68f939104a3d78f3f364840c4dcc9a07
maturity: draft
page_id: pg_9ed06b093339531cb0ef76238ad13674
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e74699f9a19c5b9da9f50f5287ab9b2a
title: zclllyybb/OpenGiraffe/README.md @ 40180a705d31
updated_at: '2026-09-14T03:27:02Z'
---

# zclllyybb/OpenGiraffe/README.md @ 40180a705d31

<!-- rcw:begin owner=source:src_e74699f9a19c5b9da9f50f5287ab9b2a block=evidence -->
- The system scans repositories for TODO/FIXME comments and uses an AI analyzer to score each item's feasibility and difficulty, producing a backlog that can be selectively dispatched as tasks. [@claim:clm_0347ac01d4688494556d6e84c979ec96a47c8389b044e2be299147c5e2248eb4]
- A free-running Project Explorer agent continuously crawls the codebase to map structure and dependencies, surfacing refactors, bugs, and missing tests, and its proposals become prioritized tasks. [@claim:clm_0b4d7766ba7179e12bc118a871de7686f386d98cca80becf85f9bfdf4a2ca773]
- Tasks, agent runs, and review history are stored in SQLite, so the daemon can be stopped and resumed after a reboot. [@claim:clm_2321c170e48e377e07980ae065f13978f2f930720148a3264dde720c5e0e5702]
- A web dashboard (FastAPI with single-file HTML/JS) served by default on port 8778 provides tabs for the Explorer loop, task management, scanned TODOs, and live model configuration that persists to config.yaml. [@claim:clm_3ca2d173bb5943d6815c3e23a298acb5285f41bbb0d61d78c0911c14d4835c6a]
- Repository development practice: the project uses pytest with tests in tests/ where all model I/O is mocked, run via python -m pytest tests/ -v; setup involves cloning, pip installing requirements, and copying config.yaml.template. [@claim:clm_43a5a9c1c4c513e0fdf209e8c3e37569af8cb98d85ac855d123422fb271e549e]
- Multiple reviewer models vote on each change, and all reviewers must approve for a task to pass; any REQUEST_CHANGES feeds reviewer feedback back to the coder. [@claim:clm_493879dd99ecb73f373d99ab813d0eb1eddea01255e1b0e8c2aef5b4671cdd83]
- The system is described as a persistent daemon-based multi-agent system using opencode to explore, plan, implement, and review code changes, with tasks running in parallel git worktrees. [@claim:clm_6edc40b15353de5bafd9bec25b3e10c88544ec4a9d6a8271f19b97618d5c73d9]
- Running the product requires Python 3.11+, the opencode CLI configured with at least one model provider, and a git repository to operate on. [@claim:clm_7aaaa7164e3519847225bd89432390c4d4e3576511b27e2460c4769fa9b33db7]
- A CLI exposes daemon control (start/stop/status), task submission and dispatch, TODO scanning/analysis/dispatch, and a synchronous run-one command for testing a single task. [@claim:clm_9be778ad228b262eb0492c6354e4d6a2613dccc99ee29c3599597b79883e2b0d]
- Tasks follow a Planner → Coder → Reviewer pipeline: the planner assesses complexity and may split work into sub-tasks dispatched independently, and rejected code re-enters a retry loop up to a max_retries limit before failing. [@claim:clm_da028f348fa1bfe15b76d22784ab9b0a62a323a5f44263081739a473e00cde1e]
- Each task runs in its own git worktree and branch (agent/task-<id>-<slug>) so parallel tasks do not conflict; completed branches can be published with a push, revised with human feedback, or cleaned. [@claim:clm_f38f25403ace2d37a9dbdcc163905ade68f939104a3d78f3f364840c4dcc9a07]
<!-- rcw:end owner=source:src_e74699f9a19c5b9da9f50f5287ab9b2a block=evidence -->

## Researcher notes

