# 777genius/agent-teams-ai

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 43764e1df31f @ 771d7e3404fa9a61

## Summary (orientation draft, not independently verified)

The evidence describes Agent Teams AI, a free open-source Electron desktop app that orchestrates teams of AI coding agents across Claude Code, Codex, OpenCode and other providers, with kanban task management, diff review, token analytics, and a local no-cloud architecture. It also includes contributor guardrails and an announcements feature plan with an e2e checklist. Evidence coverage: 114 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 12 of 173 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is described as an orchestration layer for AI agent teams spanning Claude Code, Codex, OpenCode, Cursor, SuperGrok, GitHub Copilot, Z.AI, MiniMax, and Kiro. -- evidence: [README.md#L203-L203](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L203-L203)
- components (3 claim(s)):
  - [observation/documented] The app is an Electron desktop application distributed as macOS dmg (Apple Silicon and Intel), Windows exe, Linux AppImage and deb builds via GitHub releases. -- evidence: [README.md#L142-L178](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L142-L178)
  - [observation/documented] Token analytics track input, output, cache, and reasoning usage across teams, agents, tasks, projects, models, runtimes, sessions, and runs, with monthly token or cost budgets and alerts at 80% and 100%. -- evidence: [README.md#L205-L218](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L205-L218)
- design-choices (3 claim(s)):
  - [observation/documented] The app works through locally installed Claude/Codex/OpenCode CLIs rather than app-level API keys, and the FAQ states it does not upload project code to Agent Teams servers; there is no cloud backend for code storage. -- evidence: [docs/articles/agent-teams-opus-4-8.en.md#L42-L42](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/articles/agent-teams-opus-4-8.en.md#L42-L42), [README.md#L320-L324](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L320-L324)
  - [observation/documented] Onboarding starts with a free model requiring no auth (no signup, API key, or card), with paid or account providers connected later; the app is free and open source. -- evidence: [README.md#L332-L336](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L332-L336), [README.md#L14-L16](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L14-L16), [README.md#L239-L239](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L239-L239)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributor guardrails require pnpm (not npm/yarn), desktop Electron dev via pnpm dev, production files capped at 800 lines enforced by a source-file-size ratchet script, and testing only in sandbox/test projects rather than real user projects. -- evidence: [AGENT_CRITICAL_GUARDRAILS.md#L5-L18](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/AGENT_CRITICAL_GUARDRAILS.md#L5-L18)
  - [observation/documented] Repository development practice: an announcements e2e checklist defines a sandboxed fixture harness with isolated user-data roots, a loopback fixture server, CDP-based verification, and rules that evaluation is restricted to DOM inspection and sandbox setup. -- evidence: [docs/announcements-e2e-checklist.md#L7-L11](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-e2e-checklist.md#L7-L11), [docs/announcements-e2e-checklist.md#L3-L3](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-e2e-checklist.md#L3-L3), [docs/announcements-e2e-checklist.md#L13-L13](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-e2e-checklist.md#L13-L13)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The desktop app is the main product; a web version exists but is described as still in active development. -- evidence: [README.md#L314-L314](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L314-L314)
More evidence: [full detail](agent-teams-ai.detail.md)

Metadata and full claim list: [full detail](agent-teams-ai.detail.md)
Human notes ([notes](agent-teams-ai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
