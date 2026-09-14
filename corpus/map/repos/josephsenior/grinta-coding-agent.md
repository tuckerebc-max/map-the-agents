# josephsenior/grinta-coding-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 918df240e0a5 @ 3ff10eff6d798156

## Summary (orientation draft, not independently verified)

Grinta is a local-first terminal coding agent (Python 3.12/3.13, MIT, v1.0.0) with a Textual TUI and non-interactive runner, a SessionOrchestrator with safety/retry middleware, durable sessions and ShadowGit-backed checkpoints, and multiple hosted or local inference providers. Evidence is mostly README and architecture documentation; contributor workflow guidance appears in README/COMMUNITY/GOVERNANCE sections.

## Source coverage

Source coverage (partial): 6 of 108 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Grinta is described as a local-first coding agent built to finish long, failure-prone software tasks, released under the MIT license and maintained by Youssef Mejdi. -- evidence: [README.md#L397-L398](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L397-L398), [README.md#L7-L9](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L7-L9)
  - [observation/documented] The runtime targets Python 3.12 or 3.13, supports Linux, Windows, macOS, and WSL2, and the package metadata reports version 1.0.0. -- evidence: [README.md#L43-L52](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L43-L52), [docs/ARCHITECTURE.md#L242-L242](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L242-L242), [README.md#L308-L313](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L308-L313)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture has four layers: interface (launcher, TUI, non-interactive runner), orchestration (planning, retries, finish validation), execution (local commands, files, tools), and durability (event stream and persisted state). -- evidence: [docs/ARCHITECTURE.md#L10-L13](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L10-L13), [README.md#L239-L246](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L239-L246)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo and run a platform setup script (start_here.sh or START_HERE.ps1 on Windows), then run pre-commit on all files and unit tests via PYTHONPATH=. uv run pytest backend/tests/unit before opening a pull request. -- evidence: [README.md#L357-L361](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L357-L361), [README.md#L363-L365](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L363-L365), [README.md#L367-L367](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L367-L367), [README.md#L355-L355](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L355-L355), [README.md#L369-L372](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L369-L372)
  - [observation/documented] Repository development practice: the project follows a maintainer-led governance model with a single lead maintainer holding release and merge authority, and best-effort review targets of 5 business days for bugs and 7 for pull requests. -- evidence: [MAINTAINERS.md#L3-L3](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L3-L3), [MAINTAINERS.md#L12-L14](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L12-L14), [MAINTAINERS.md#L16-L16](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L16-L16), [MAINTAINERS.md#L7-L8](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L7-L8), [GOVERNANCE.md#L5-L5](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/GOVERNANCE.md#L5-L5)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product offers a Textual terminal UI for TTY stdin and a non-interactive runner for piped input where each input line is one turn, plus slash commands like /mode, /model, /checkpoint, and /resume. -- evidence: [README.md#L43-L52](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L43-L52), [README.md#L190-L191](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L190-L191), [README.md#L164-L176](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L164-L176), [docs/ARCHITECTURE.md#L88-L89](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L88-L89)
  - [observation/documented] CLI subcommands include grinta init, grinta doctor, grinta sessions list/show/export/prune, and flags such as --project, --model, --theme, --minimal, --accessible, and --cleanup-storage. -- evidence: [README.md#L103-L106](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L103-L106), [README.md#L180-L188](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L180-L188), [docs/ARCHITECTURE.md#L81-L84](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L81-L84)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions, event history, and checkpoints persist locally; workspace checkpoints use the standalone ShadowGit package writing content-addressed snapshots to a private object store without touching the user's .git. -- evidence: [README.md#L269-L272](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L269-L272), [docs/ARCHITECTURE.md#L217-L225](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L217-L225), [README.md#L259-L267](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L259-L267), [README.md#L19-L22](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L19-L22)
- orchestration (2 claim(s)):
More evidence: [full detail](grinta-coding-agent.detail.md)

Metadata and full claim list: [full detail](grinta-coding-agent.detail.md)
Human notes ([notes](grinta-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
