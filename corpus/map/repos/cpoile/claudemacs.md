# cpoile/claudemacs

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1f2fe7bbc718 @ 21761bc18dec649d

## Summary (orientation draft, not independently verified)

README-only evidence for claudemacs, an Emacs package that runs AI coding CLIs (Claude Code, Codex, Gemini) in terminal-backed Emacs sessions with workspace-aware session management, notifications, and a transient command menu. No contributor/development-practice or evaluation evidence is present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The package supports multiple terminal backends: Ghostel is selected automatically when available, otherwise it falls back to Eat; the backend can be forced via claudemacs-terminal-backend. -- evidence: [README.md#L154-L155](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L154-L155), [README.md#L150-L152](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L150-L152), [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31), [README.md#L145-L148](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L145-L148)
  - [observation/documented] A configurable tool registry defines which AI CLI tools are available, with defaults Claude, Codex, and Gemini, each with program, switches, and model-types entries; users can add tools like aider. -- evidence: [README.md#L478-L478](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L478-L478), [README.md#L491-L499](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L491-L499), [README.md#L480-L489](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L480-L489)
- design-choices (5 claim(s)):
  - [observation/documented] The project's stated design philosophy is simplicity: let the LLM CLI run in the terminal without agents, MCP, or IDE integration, which the README says would consume context. -- evidence: [README.md#L8-L9](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L8-L9)
  - [observation/documented] Sessions are workspace-aware: the session is keyed to the Doom/Perspective workspace and the tool's cwd defaults to the project's git root, enabling separate sessions per workspace in a monorepo. -- evidence: [README.md#L363-L367](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L363-L367)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] Claudemacs exposes a transient menu (default binding C-c C-e) with core commands for starting, switching, resuming, listing, and killing sessions, plus action commands like fix-error-at-point and implement-comment. -- evidence: [README.md#L420-L427](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L420-L427), [README.md#L443-L450](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L443-L450), [README.md#L418-L418](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L418-L418)
  - [observation/documented] Action commands accept a C-u prefix to broadcast the action to all active sessions. -- evidence: [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31), [README.md#L443-L450](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L443-L450)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions can be resumed using tool-specific resume flags, and the resume submenu supports resuming a Codex session by UUID. -- evidence: [README.md#L437-L441](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L437-L441), [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The start-session submenu offers a -d switch to skip permissions (--dangerously-skip-permissions or equivalent) when launching a tool. -- evidence: [README.md#L437-L441](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L437-L441)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Requirements are Emacs 28.1+, the Eat package or Ghostel with its native module, transient (built-in since Emacs 28), and a supported AI CLI such as Claude Code. -- evidence: [README.md#L734-L737](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L734-L737)
More evidence: [full detail](claudemacs.detail.md)

Metadata and full claim list: [full detail](claudemacs.detail.md)
Human notes ([notes](claudemacs.notes.md), never overwritten by build)

[Back to map index](../../index.md)
