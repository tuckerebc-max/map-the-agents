# littlebearapps/untether

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4285dad5a12e @ 0436e3cf05c6d927

## Summary (orientation draft, not independently verified)

Untether is a Python Telegram bridge that lets users control AI coding agent CLIs (Claude Code, Codex, OpenCode, Pi, Gemini CLI, Amp) running on their own machine, with progress streaming, interactive approvals, voice input, and cost budgets. The repository also documents a contributor workflow with a gated three-phase release process. Evidence coverage: 114 of 140 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 116 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Configuration lives in ~/.untether/untether.toml with sections for default engine, Telegram transport, projects, and cost budgets (per-run and daily limits). -- evidence: [README.md#L214-L218](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L214-L218), [README.md#L210-L212](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L210-L212), [README.md#L205-L208](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L205-L208), [README.md#L200-L200](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L200-L200)
- design-choices (1 claim(s)):
  - [observation/documented] The setup wizard offers three workflow modes: Assistant (ongoing chat with auto-resume), Workspace (forum topics bound to project/branch), and Handoff (reply-to-continue). -- evidence: [README.md#L73-L77](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L73-L77)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors use Python 3.12+, anyio, msgspec, structlog, Ruff linting, pytest with an 80% coverage threshold, Australian English in user-facing text, and conventional commits on feature/*, fix/*, docs/* branches. -- evidence: [AGENTS.md#L21-L25](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/AGENTS.md#L21-L25)
  - [observation/documented] Repository development practice: every runner must emit exactly one StartedEvent, zero or more ActionEvents, and exactly one final CompletedEvent, constructed via EventFactory rather than directly. -- evidence: [AGENTS.md#L29-L32](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/AGENTS.md#L29-L32), [AGENTS.md#L34-L34](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/AGENTS.md#L34-L34)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Users interact via Telegram bot commands including /cancel, /agent, /model, /planmode, /usage, /export, /browse, /config, /continue, /file put/get, /topic, /restart, /stats, and /auth. -- evidence: [README.md#L167-L190](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L167-L190)
  - [observation/documented] Messages can be prefixed with /<engine> to pick an engine for that task, or /<project> to target a specific repository. -- evidence: [README.md#L192-L192](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L192-L192)
- memory-state (1 claim(s)):
  - [observation/documented] Untether stores chat preferences, session state, and usage stats as JSON files under ~/.untether/, plus an optional per-project .untether-outbox/ directory for agent-delivered files. -- evidence: [README.md#L307-L320](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L307-L320)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Interactive permission buttons let users approve plan transitions and answer clarifying questions; tools auto-execute, and a 'Pause & Outline Plan' option holds the session open for plan review. -- evidence: [README.md#L89-L110](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L89-L110)
  - [observation/documented] Interactive permissions, plan mode, ask mode, diff preview, and auto-approve of safe tools are Claude Code-only; other engines use pre-run approval policies or none. -- evidence: [README.md#L154-L159](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L154-L159), [README.md#L129-L152](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L129-L152)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](untether.detail.md)

Metadata and full claim list: [full detail](untether.detail.md)
Human notes ([notes](untether.notes.md), never overwritten by build)

[Back to map index](../../index.md)
