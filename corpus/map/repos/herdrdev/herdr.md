# herdrdev/herdr

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit aa961df943b8 @ 9d624c3d74eb8c6b

## Summary (orientation draft, not independently verified)

Herdr is described as a single Rust binary with no Electron dependency, running inside the user's existing terminal. The product keeps terminals running in a background server so work continues after the client closes or SSH drops, and restores saved layout after server or machine restart.

## Source coverage

Source coverage (partial): 3 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Herdr is described as a single Rust binary with no Electron dependency, running inside the user's existing terminal. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
  - [observation/documented] The product keeps terminals running in a background server so work continues after the client closes or SSH drops, and restores saved layout after server or machine restart. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
- design-choices (2 claim(s)):
  - [observation/documented] Herdr runs agents like Claude Code, Codex, Cursor, OpenCode, and Grok in their own terminals without wrapping or replacing them. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
  - [observation/documented] Each pane is marked working, blocked, or idle, and Herdr signals when an agent stops and needs input. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors should use just recipes (just test, just check) rather than invoking cargo directly, and run just check before committing. -- evidence: [AGENTS.md#L141-L141](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L141-L141), [AGENTS.md#L136-L139](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L136-L139), [AGENTS.md#L134-L134](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L134-L134)
  - [observation/documented] Repository development practice: Rust production code must avoid unwrap(), use tracing for logging, and gate platform-specific code via cfg attributes in src/platform/. -- evidence: [AGENTS.md#L251-L255](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/AGENTS.md#L251-L255)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Agents can drive Herdr through a CLI and socket API to spawn panes, prompt each other, and wait until another agent is blocked. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
  - [observation/documented] The TUI supports tmux-style prefix keys plus mouse click, drag, and split interactions. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] After a server or machine restart, Herdr restores layout and can resume supported agent sessions, but the original processes do not survive. -- evidence: [README.md#L31-L38](https://github.com/herdrdev/herdr/blob/aa961df943b874730b23f78baf94af7332f7acfa/README.md#L31-L38)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](herdr.detail.md) for every claim.)

Metadata and full claim list: [full detail](herdr.detail.md)
Human notes ([notes](herdr.notes.md), never overwritten by build)

[Back to map index](../../index.md)
