# dazuiba/handoff

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 717ac79e1885 @ 7e70da208eba64cc

## Summary (orientation draft, not independently verified)

Handoff is a CLI proxy that dispatches coding tasks to configurable AI backends (Claude/Anthropic-compatible endpoints and Codex), invoked from Claude Code skills or Codex custom agents, with background execution, a RESULT= file protocol, and TUI history tools.

## Source coverage

Source coverage (partial): 3 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Backends are configured in ~/.handoff/config.yaml; any Anthropic-compatible endpoint can be added, env keys are exported before the CLI launches, {model} substitutes the resolved model, and ${ENV_VAR} expands from the shell. -- evidence: [README.md#L187-L187](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L187-L187), [README.md#L200-L200](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L200-L200), [README.md#L189-L198](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L189-L198)
  - [observation/documented] The opus and codex backends reuse existing Claude Code / Codex logins with zero configuration; only DeepSeek requires a token. -- evidence: [README.md#L54-L54](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L54-L54)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: releases are made by bumping the version in pyproject.toml, committing, tagging vX.Y.Z, and pushing; a v* tag triggers a workflow that builds with uv build and publishes to PyPI. -- evidence: [CLAUDE.md#L48-L48](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L48-L48), [CLAUDE.md#L43-L46](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L43-L46)
  - [observation/documented] Repository development practice: CLAUDE.md provides guidance to Claude Code when working with code in this repository, including a file map of the cli/ package and release steps. -- evidence: [CLAUDE.md#L3-L3](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L3-L3), [CLAUDE.md#L43-L46](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L43-L46), [CLAUDE.md#L11-L39](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L11-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI exposes run, resume, list/ls, tail, env, init, and new commands; list and tail provide interactive TUI views of task history and live output streams. -- evidence: [README.md#L124-L124](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L124-L124), [README.md#L113-L113](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L113-L113), [README.md#L219-L221](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L219-L221), [CLAUDE.md#L11-L39](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L11-L39), [README.md#L119-L119](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L119-L119)
  - [observation/documented] Dispatched tasks return exactly one line, RESULT=<path-to-result-file>, to the calling session; that path serves as a stable handle so every follow-up resumes the same session. -- evidence: [README.md#L209-L213](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L209-L213)
- memory-state (1 claim(s)):
  - [observation/documented] State persists under ~/.handoff, including config.yaml, a SQLite runs database (handoff.db), and tui_state.json storing the user's TUI theme choice. -- evidence: [CLAUDE.md#L11-L39](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L11-L39), [README.md#L56-L56](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L56-L56), [README.md#L151-L151](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L151-L151)
- orchestration (1 claim(s)):
  - [observation/documented] Tasks run in the background so the main session never blocks; handoff launches the backend CLI (claude -p or codex exec) in an isolated context and streams output to disk, and several tasks can be dispatched in one message. -- evidence: [README.md#L209-L213](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L209-L213), [README.md#L160-L160](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L160-L160)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](handoff.detail.md)

Metadata and full claim list: [full detail](handoff.detail.md)
Human notes ([notes](handoff.notes.md), never overwritten by build)

[Back to map index](../../index.md)
