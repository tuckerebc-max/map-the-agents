# shoyann/thrush-swe-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit daef0a6d6a6d @ ad148bedd351dcd1

## Summary (orientation draft, not independently verified)

Thrush is a local dual-mode SWE agent workbench (Next.js/TypeScript/SQLite) with an Assist mode that stages edits for approval and an Auto mode that runs bundled mini-swe-agent in an isolated worktree/Docker, producing reviewable artifacts. Evidence is documentation-based (README, ADRs, CONTEXT.md); no runtime code is in the snapshot.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Auto Mode is backed by a bundled mini-swe-agent checkout in vendor/mini-swe-agent with a non-interactive runner at scripts/mini-auto-run.py; an ADR states the bundled copy should be managed as a Git submodule or clearly tracked vendored dependency. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [docs/adr/0003-bundle-mini-swe-agent.md#L3-L3](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/docs/adr/0003-bundle-mini-swe-agent.md#L3-L3)
  - [observation/documented] Auto runs collect diff, diff stat, changed files, logs, and trajectory, and generate a human-readable Auto Report shown with these artifacts in a side drawer. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L133-L138](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L133-L138)
- design-choices (1 claim(s)):
  - [observation/documented] Thrush offers two modes in one UI: Assist, where the agent drafts edits and the user approves before files are written, and Auto, where the agent attempts a full task in isolation and returns a report and diff. -- evidence: [README.md#L28-L31](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L28-L31), [README.md#L7-L11](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L7-L11)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm run test, npx tsc --noEmit, and npm run lint; the repo includes tests for Auto data flow, readiness checks, recommended environments, the mini resolver, and runner behavior with fake mini results. -- evidence: [README.md#L215-L215](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L215-L215), [README.md#L209-L213](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L209-L213)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Before Auto starts, an Environment Doctor checks Git clean state, Docker availability, mini runtime readiness, model API key configuration, and GitHub readiness. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L125-L129](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L125-L129)
  - [observation/documented] Model providers are configurable via environment variables: MODEL_PROVIDER supports deepseek (default), openai, or anthropic, with per-provider API key, base URL, and model variables, plus an AGENT_API_SECRET bearer token for /api/agent. -- evidence: [README.md#L82-L87](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L82-L87), [README.md#L162-L179](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L162-L179)
- memory-state (1 claim(s)):
  - [observation/documented] Local state lives under data/: a SQLite database (thrush.db) with separate tables for Auto runs, events, artifacts, and presets, plus workspace, auto-runs, mini-venv, and pip/uv cache directories. -- evidence: [README.md#L37-L43](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L37-L43), [README.md#L185-L191](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L185-L191)
- orchestration (2 claim(s)):
  - [observation/documented] Auto Mode runs mini-swe-agent in a separate Git worktree under data/auto-runs/<autoRunId>/worktree on a branch auto/<autoRunId>, leaving the main workspace unchanged; Draft PR creation is a user action, not automatic. -- evidence: [README.md#L197-L197](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L197-L197), [README.md#L33-L33](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L33-L33), [README.md#L133-L138](https://github.com/shoyann/thrush-swe-agent/blob/daef0a6d6a6d8c59cb53aa9b01b220f32a617a35/README.md#L133-L138)
More evidence: [full detail](thrush-swe-agent.detail.md)

Metadata and full claim list: [full detail](thrush-swe-agent.detail.md)
Human notes ([notes](thrush-swe-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
