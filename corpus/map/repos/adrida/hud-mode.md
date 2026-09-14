# adrida/hud-mode

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 98571ccf7101 @ 278eae6eb4afb581

## Summary (orientation draft, not independently verified)

hud-mode is a zero-dependency terminal HUD that wraps OpenCode, Claude Code, and Codex CLIs, driving them headless via JSON event streams with a lossless full-TUI toggle. Evidence is README-only documentation of install, usage, instruments, and architecture.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Gauges include status flag, model, mode, effort, message count, elapsed time, tokens, live subagents, session cost, context size, and on-disk conversation size, flowing onto a second aligned row when needed. -- evidence: [README.md#L93-L110](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L93-L110)
- design-choices (3 claim(s)):
  - [observation/documented] Instruments and the activity line update in place rather than scrolling; the prompt bar stays writable so messages typed mid-turn queue and fire when the answer lands. -- evidence: [README.md#L14-L17](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L14-L17)
  - [observation/documented] When the agent stops, the full answer is shown with rendered markdown and clickable links; sending a follow-up recompacts the screen back to instruments and prompt bar. -- evidence: [README.md#L19-L21](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L19-L21)
- workflows (1 claim(s)):
  - [observation/documented] `hud install` wires a skills directory, a settings.json hook (backed up), codex prompt and AGENTS.md entries, and an opencode command file; `hud uninstall` removes all of it. -- evidence: [README.md#L122-L125](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L122-L125)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product is a terminal HUD for coding agents, installed globally via npm and launched with the `hud` command, optionally with a prompt argument. -- evidence: [README.md#L42-L46](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L42-L46), [README.md#L3-L8](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L3-L8), [README.md#L29-L31](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L29-L31)
  - [observation/documented] Supports three engines: OpenCode (default), Claude Code, and Codex; `hud default claude` changes the engine used by bare `hud`. -- evidence: [README.md#L42-L46](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L42-L46), [README.md#L48-L51](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L48-L51), [README.md#L3-L8](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L3-L8)
- memory-state (1 claim(s)):
  - [observation/documented] Shared agent links persist in a per-session ledger at ~/.claude/hud/links/ across restarts, and gauge selections persist in ~/.claude/hud/config.json. -- evidence: [README.md#L93-L110](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L93-L110)
- orchestration (2 claim(s)):
  - [observation/documented] hud drives each CLI headless through its JSON event stream (e.g. `opencode run --format json`, `claude -p --output-format stream-json`, `codex exec --json`) and resumes sessions via each engine's own resume mechanism. -- evidence: [README.md#L83-L87](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L83-L87), [README.md#L114-L120](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L114-L120)
  - [observation/documented] The full-TUI handback uses a sentinel file ~/.claude/hud/handoff.json watched by the wrapper, written per-engine via a hook, an AGENTS.md rule, or a command template. -- evidence: [README.md#L114-L120](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L114-L120)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requires Node >= 18 and at least one of opencode, claude, or codex on the PATH. -- evidence: [README.md#L37-L38](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L37-L38)
- limitations (1 claim(s)):
More evidence: [full detail](hud-mode.detail.md)

Metadata and full claim list: [full detail](hud-mode.detail.md)
Human notes ([notes](hud-mode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
