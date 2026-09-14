# luckeyfaraday/athena

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 47ec8132d51d @ 4ac2ac908f6c4b73

## Summary (orientation draft, not independently verified)

Athena is an Electron+React desktop app with a FastAPI backend for orchestrating local AI coding agent sessions (Codex, OpenCode, Claude Code, Athena Code, Hermes, shell), with embedded PTY terminals, native session discovery, project-local recall/handoffs, and an MCP bridge letting Hermes drive the workspace. Evidence is README-only documentation of the 0.1.7 snapshot. Evidence coverage: 156 of 199 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 21 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

21 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Athena is a local desktop workspace for orchestrating AI coding agents, described as version 0.1.7 and targeting Linux, Windows, and macOS. -- evidence: [README.md#L34-L34](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L34-L34), [README.md#L9-L18](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L9-L18), [README.md#L5-L7](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L5-L7)
- components (2 claim(s)):
  - [observation/documented] The app is an Electron + React frontend with a FastAPI Python backend launched by Electron, plus an MCP server under mcp_server/ exposing Athena tools to Hermes. -- evidence: [README.md#L55-L55](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L55-L55), [README.md#L72-L81](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L72-L81), [README.md#L120-L130](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L120-L130)
  - [observation/documented] Embedded terminals are implemented with node-pty in the Electron main process and rendered in the React UI with xterm.js. -- evidence: [README.md#L55-L55](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L55-L55), [README.md#L300-L300](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L300-L300), [README.md#L335-L335](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L335-L335)
- design-choices (3 claim(s)):
  - [observation/documented] Fresh agent panes start without project context by default; memory, recall, and instruction bundles attach only when an explicit immersive context mode is selected, creating an immutable workspace-scoped bundle and a bootstrap prompt pointing at it. -- evidence: [README.md#L302-L304](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L302-L304), [README.md#L306-L309](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L306-L309), [README.md#L595-L597](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L595-L597)
  - [observation/documented] Terminal streaming is bounded and sequence-aware: output goes only to subscribed visible views, is retained until xterm acknowledges, replays from an atomic snapshot after remount, and sends an explicit reset/truncation marker when a consumer falls behind. -- evidence: [README.md#L337-L343](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L337-L343)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run pytest plus scripts/run_regression_checks.py and client test/build suites before PRs; PRs run the same suites in .github/workflows/pr-checks.yml, and changes to terminal streaming, session discovery, or pane layout must add a regression case. -- evidence: [README.md#L291-L293](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L291-L293), [README.md#L270-L273](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L270-L273), [README.md#L277-L283](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L277-L283), [README.md#L680-L684](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L680-L684), [README.md#L267-L268](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L267-L268)
  - [observation/documented] Repository development practice: contributor notes say to keep run artifacts under .context-workspace/runs/<run-id>/, avoid overwriting user-owned AGENTS.md/CLAUDE.md without opt-in, and prefer adapter-specific behavior. -- evidence: [README.md#L680-L684](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L680-L684)
- skills-patterns (2 claim(s)):
  - [observation/documented] On every launch the app installs an agent skill named athena-context-workspace into Codex, Claude, and OpenCode skill directories, tracking installs in ~/.context-workspace/agent-skills.json so user-edited directories are not overwritten. -- evidence: [README.md#L379-L383](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L379-L383), [README.md#L385-L388](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L385-L388), [README.md#L375-L377](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L375-L377)
  - [observation/documented] A bundled Hermes skill (docs/hermes-recall-skill/SKILL.md) defines a required pattern: run session_search, summarize native sessions, write the recall cache, verify by reading it back, and report before continuing. -- evidence: [docs/hermes-recall-skill/SKILL.md#L26-L26](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/docs/hermes-recall-skill/SKILL.md#L26-L26), [docs/hermes-recall-skill/SKILL.md#L1-L4](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/docs/hermes-recall-skill/SKILL.md#L1-L4), [docs/hermes-recall-skill/SKILL.md#L28-L33](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/docs/hermes-recall-skill/SKILL.md#L28-L33)
More evidence: [full detail](athena.detail.md)

Metadata and full claim list: [full detail](athena.detail.md)
Human notes ([notes](athena.notes.md), never overwritten by build)

[Back to map index](../../index.md)
