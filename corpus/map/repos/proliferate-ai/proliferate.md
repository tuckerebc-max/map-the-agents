# proliferate-ai/proliferate

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 74e1178cf3ec @ 48727c705a63ed65

## Summary (orientation draft, not independently verified)

The snapshot is mostly README plus contributor-routing docs for Proliferate, an open-source AI IDE that runs multiple coding agents in parallel with per-task git worktrees and a self-hostable control plane. Product claims come from the README; contributor instructions are recorded only under workflows.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product supports subagents that delegate scoped work to child agents, plus integrations including MCPs, skills, Computer Use, Browser Use, and custom tools shared across agents. -- evidence: [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: running from source requires Rust stable, Node.js 22+, and pnpm, with 'make install' and 'make dev-local' to launch the desktop app with the bundled local AnyHarness runtime. -- evidence: [README.md#L121-L124](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L121-L124), [README.md#L119-L119](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L119-L119), [README.md#L115-L117](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L115-L117)
  - [observation/documented] Repository development practice: local full-stack development additionally needs Python 3.12+, uv, and Docker, using named dev profiles when multiple worktrees run concurrently. -- evidence: [README.md#L126-L128](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L126-L128), [README.md#L138-L139](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L138-L139), [README.md#L130-L136](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L130-L136)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Proliferate runs coding agents such as Claude Code, Codex, OpenCode, Cursor, and Grok through each agent's native harness. -- evidence: [README.md#L53-L53](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L53-L53), [README.md#L23-L24](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L23-L24), [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49), [README.md#L55-L87](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L55-L87)
  - [observation/documented] The desktop app can be pointed at a self-hosted control plane via a documented configuration procedure. -- evidence: [README.md#L102-L106](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L102-L106)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Multiple coding agents can run in parallel in one workspace, and each task gets an isolated git worktree with its own branch, terminal, conversation, and review state. -- evidence: [README.md#L23-L24](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L23-L24), [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49)
  - [observation/documented] The product advertises recurring and event-driven agent workflows, such as nightly review passes, alert triage, and dependency bumps. -- evidence: [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The control plane is self-hostable; the Docker Compose guide runs Caddy, Postgres, and the API with bootstrap and update scripts, and an AWS option uses a CloudFormation wrapper on EC2. -- evidence: [README.md#L95-L100](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L95-L100), [README.md#L91-L93](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L91-L93)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](proliferate.detail.md) for every claim.)

Metadata and full claim list: [full detail](proliferate.detail.md)
Human notes ([notes](proliferate.notes.md), never overwritten by build)

[Back to map index](../../index.md)
