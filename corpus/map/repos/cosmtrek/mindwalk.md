# cosmtrek/mindwalk

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 77cd79596a1b @ 979a5969183bf46b

## Summary (orientation draft, not independently verified)

mindwalk is a visualization tool that replays coding-agent sessions as light moving through a night-style map of the codebase, showing where the agent searched, read, and edited. The CLI offers serve, open, map, build, trace, and analyze subcommands, with flags such as --port, --no-open, per-agent session dirs, --judge, --model, and --no-rubric.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] mindwalk is a visualization tool that replays coding-agent sessions as light moving through a night-style map of the codebase, showing where the agent searched, read, and edited. -- evidence: [README.md#L16-L24](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L16-L24), [README.md#L3-L3](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The system separates three artifacts: a normalized trace (internal/adapter, one adapter per agent format), a deterministic citymap (internal/citymap), and an LLM-judge report (internal/judge), joined by a local Go server serving a React/Three.js frontend. -- evidence: [README.md#L137-L147](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L137-L147), [README.md#L149-L150](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L149-L150)
- design-choices (1 claim(s)):
  - [observation/documented] The UI encodes touch state as light on a dark ink-blue map (seen green, read blue, edited amber), with tree and terrain views, a playback histogram where observation stays cool and mutation glows warm, and glow treated strictly as data. -- evidence: [.impeccable.md#L44-L54](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/.impeccable.md#L44-L54), [.impeccable.md#L22-L34](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/.impeccable.md#L22-L34), [README.md#L58-L83](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L58-L83)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run make setup, make serve (dev server on :8765), make test before sending a PR, and make build to regenerate embedded assets; Go code must stay gofmt-ed and internal/server/static must never be hand-edited. -- evidence: [README.md#L165-L171](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L165-L171), [README.md#L156-L161](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L156-L161), [AGENTS.md#L43-L43](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/AGENTS.md#L43-L43), [AGENTS.md#L38-L41](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/AGENTS.md#L38-L41)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI offers serve, open, map, build, trace, and analyze subcommands, with flags such as --port, --no-open, per-agent session dirs, --judge, --model, and --no-rubric. -- evidence: [README.md#L46-L54](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L46-L54)
- memory-state (1 claim(s)):
  - [observation/documented] Evaluation reports are cached one per session in ~/.mindwalk/reports, go stale without auto-rerun when session content changes, and reuse the drafted rubric when task wording is unchanged. -- evidence: [docs/dynamic-rubric-evaluation.md#L79-L83](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L79-L83), [README.md#L128-L131](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L128-L131), [docs/dynamic-rubric-evaluation.md#L85-L86](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L85-L86)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The judge subprocess runs sealed: it gets no tools, no MCP servers, no user or project settings, and no session persistence, and it only receives the evaluated session's summary. -- evidence: [docs/dynamic-rubric-evaluation.md#L101-L103](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L101-L103), [README.md#L120-L126](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L120-L126)
- evaluation (2 claim(s)):
More evidence: [full detail](mindwalk.detail.md)

Metadata and full claim list: [full detail](mindwalk.detail.md)
Human notes ([notes](mindwalk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
