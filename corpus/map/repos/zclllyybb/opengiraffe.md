# zclllyybb/opengiraffe

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 40180a705d31 @ b25edc3f887cf4c8

## Summary (orientation draft, not independently verified)

The evidence is README-only documentation for Open Giraffe, a daemon-based multi-agent coding orchestrator built on the opencode CLI, describing its pipeline, CLI, dashboard, configuration, and dependencies. No source code is included in the slices, so all claims are documented rather than code-inspected.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The system is described as a persistent daemon-based multi-agent system using opencode to explore, plan, implement, and review code changes, with tasks running in parallel git worktrees. -- evidence: [README.md#L7-L7](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L7-L7)
  - [observation/documented] A free-running Project Explorer agent continuously crawls the codebase to map structure and dependencies, surfacing refactors, bugs, and missing tests, and its proposals become prioritized tasks. -- evidence: [README.md#L23-L31](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L23-L31), [README.md#L37-L37](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L37-L37), [README.md#L43-L43](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L43-L43)
- design-choices (1 claim(s)):
  - [observation/documented] Each task runs in its own git worktree and branch (agent/task-<id>-<slug>) so parallel tasks do not conflict; completed branches can be published with a push, revised with human feedback, or cleaned. -- evidence: [README.md#L120-L120](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L120-L120), [README.md#L92-L118](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L92-L118), [README.md#L13-L17](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L13-L17)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project uses pytest with tests in tests/ where all model I/O is mocked, run via python -m pytest tests/ -v; setup involves cloning, pip installing requirements, and copying config.yaml.template. -- evidence: [README.md#L138-L138](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L138-L138), [README.md#L203-L203](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L203-L203), [README.md#L141-L141](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L141-L141), [README.md#L207-L207](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L207-L207), [README.md#L134-L135](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L134-L135)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A CLI exposes daemon control (start/stop/status), task submission and dispatch, TODO scanning/analysis/dispatch, and a synchronous run-one command for testing a single task. -- evidence: [README.md#L160-L164](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L160-L164), [README.md#L174-L175](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L174-L175), [README.md#L167-L171](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L167-L171), [README.md#L155-L157](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L155-L157)
  - [observation/documented] A web dashboard (FastAPI with single-file HTML/JS) served by default on port 8778 provides tabs for the Explorer loop, task management, scanned TODOs, and live model configuration that persists to config.yaml. -- evidence: [README.md#L59-L88](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L59-L88), [README.md#L179-L179](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L179-L179), [README.md#L181-L186](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L181-L186)
- memory-state (1 claim(s)):
  - [observation/documented] Tasks, agent runs, and review history are stored in SQLite, so the daemon can be stopped and resumed after a reboot. -- evidence: [README.md#L13-L17](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L13-L17)
- orchestration (2 claim(s)):
  - [observation/documented] Tasks follow a Planner → Coder → Reviewer pipeline: the planner assesses complexity and may split work into sub-tasks dispatched independently, and rejected code re-enters a retry loop up to a max_retries limit before failing. -- evidence: [README.md#L92-L118](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L92-L118)
  - [observation/documented] Multiple reviewer models vote on each change, and all reviewers must approve for a task to pass; any REQUEST_CHANGES feeds reviewer feedback back to the coder. -- evidence: [README.md#L23-L31](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L23-L31), [README.md#L92-L118](https://github.com/zclllyybb/OpenGiraffe/blob/40180a705d315c6d54aca045fe80646dd9ceb443/README.md#L92-L118)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](opengiraffe.detail.md)

Metadata and full claim list: [full detail](opengiraffe.detail.md)
Human notes ([notes](opengiraffe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
