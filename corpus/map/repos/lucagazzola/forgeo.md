# lucagazzola/forgeo

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6e709a374a66 @ 12163ac21a1508c3

## Summary (orientation draft, not independently verified)

Forgeo is a scheduled, agent-driven software factory: a daemon picks backlog tasks, runs an agent CLI, commits results, and surfaces human decisions via a central web dashboard, with file/HTTP/Jira/GitHub/GitLab backlog providers and an optional Docker sandbox. Contributor quality gates (pytest, ruff, mypy) are documented separately as repository development practice.

## Source coverage

Source coverage (partial): 3 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Forgeo is described as a software factory for a coding agent: given a backlog and an agent CLI, it picks the next runnable task, runs the agent, commits the result, and tracks progress in plain files plus a web dashboard. -- evidence: [README.md#L16-L16](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L16-L16), [README.md#L18-L18](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L18-L18)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Optional review_mode: branch commits successful agent work to a forgeo/review/<TASK_ID> branch, marks the task REVIEW, and waits for a human merge/Complete or Request-changes action instead of committing directly to main. -- evidence: [README.md#L20-L24](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L20-L24), [CHANGELOG.md#L43-L49](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L43-L49)
  - [observation/documented] A silent no-change success (exit 0 with unchanged tree) marks the task BLOCKED for human review rather than FAILED, unless the agent opts in via no_changes_exit_code. -- evidence: [CHANGELOG.md#L141-L145](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L141-L145)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors must run pytest, ruff check, and mypy src/forgeo before opening a PR, and CI enforces the same quality gates on pull requests. -- evidence: [CONTRIBUTING.md#L69-L77](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L69-L77), [CONTRIBUTING.md#L19-L19](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L19-L19), [CONTRIBUTING.md#L21-L25](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L21-L25)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The agent contract is agent-agnostic: any CLI that reads the FORGEO_TASK environment variable can be used, and the backlog task's acceptance criteria are rendered into that instruction. -- evidence: [README.md#L20-L24](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L20-L24), [CONTRIBUTING.md#L36-L43](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CONTRIBUTING.md#L36-L43)
  - [observation/documented] CLI surface includes forgeo init, validate, start, once, run --task, status, stop, restart, instance add/list, and web, with the daemon running one cycle per interval_minutes. -- evidence: [README.md#L65-L68](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L65-L68), [README.md#L44-L46](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L44-L46), [README.md#L74-L81](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L74-L81), [README.md#L102-L107](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L102-L107)
- memory-state (1 claim(s)):
  - [observation/documented] Forgeo persists runtime state in .forgeo/ (backlog, logs, blockers) plus runs.jsonl run history, daemon.state.json, and rotating backlog.json.bak snapshots restored when the backlog is found corrupt. -- evidence: [README.md#L48-L48](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L48-L48), [CHANGELOG.md#L266-L270](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L266-L270), [CHANGELOG.md#L206-L210](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L206-L210), [CHANGELOG.md#L279-L284](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L279-L284), [CHANGELOG.md#L378-L388](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L378-L388)
- orchestration (1 claim(s)):
  - [observation/documented] Task selection picks the oldest OPEN task whose dependencies are all COMPLETED (or whose run_at schedule is due); REVIEW blocks dependants while independent tasks keep running. -- evidence: [CHANGELOG.md#L286-L293](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/CHANGELOG.md#L286-L293), [README.md#L20-L24](https://github.com/lucaGazzola/forgeo/blob/6e709a374a66b964c97e7e6a9c6665ad89fcac08/README.md#L20-L24)
- tools-permissions (1 claim(s)):
More evidence: [full detail](forgeo.detail.md)

Metadata and full claim list: [full detail](forgeo.detail.md)
Human notes ([notes](forgeo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
