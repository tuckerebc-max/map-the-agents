# kadeai/kade

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 616148222f74 @ d84e039d68ba41fa

## Summary (orientation draft, not independently verified)

Selected evidence records: Documentation describes a sub-agent system where a main agent can spawn sub-agents recursively, each with its own chat tab, isolated context and memory, with results flowing back to the main agent. The README claims each sub-agent can use a different model from 50+ providers, enabling task-specific agents such as testing, security, and documentation agents.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Documentation describes an MCP Store with 25,000+ MCPs via LobeHub API integration, offering one-click installation, marketplace search, and enterprise features like security scanning and team sharing. -- evidence: [readme.md#L215-L218](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L215-L218), [readme.md#L213-L213](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L213-L213)
  - [observation/documented] The README lists OAuth support for several platforms (Antigravity, Kilo Code, Gemini CLI, Claude Code, OpenAI Codex) with token storage, auto-refresh, and local callback servers with CSRF protection. -- evidence: [readme.md#L226-L229](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L226-L229), [readme.md#L224-L224](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L224-L224)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The changelog records added skills support, including installing and enabling skills and installing skills from skills.sh via a marketplace tab. -- evidence: [CHANGELOG.md#L26-L28](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L26-L28)
- interfaces (2 claim(s)):
  - [observation/documented] The README describes text-based tool-calling protocols named Unified (CLI-like syntax such as <<read --path ...>>) and Markdown (code blocks), alongside supported legacy JSON and XML formats. -- evidence: [readme.md#L142-L144](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L142-L144), [readme.md#L114-L114](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L114-L114), [readme.md#L116-L119](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L116-L119), [readme.md#L139-L139](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L139-L139)
  - [observation/documented] The changelog states Markdown, XML, and CLI tool schemas were removed in favor of an overhauled native JSON system and a new 'Aero' schema allowing single-letter tool calls, which conflicts with the README's four-protocol claim. -- evidence: [readme.md#L121-L121](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L121-L121), [CHANGELOG.md#L35-L48](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L35-L48)
- memory-state (2 claim(s)):
  - [observation/documented] Documentation claims each chat remembers its selected AI model across sessions and automatically restores it, allowing multiple models to run concurrently in different chat windows. -- evidence: [readme.md#L93-L96](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L93-L96), [CHANGELOG.md#L127-L131](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L127-L131), [readme.md#L90-L90](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L90-L90)
  - [observation/documented] The changelog says task history was moved from VS Code globalState (SQLite) to disk-based JSON storage at globalStorageUri/task_history.json, using an in-memory cache with debounced writes to reduce I/O. -- evidence: [CHANGELOG.md#L119-L121](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L119-L121), [CHANGELOG.md#L101-L106](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L101-L106)
- orchestration (2 claim(s)):
  - [observation/documented] Documentation describes a sub-agent system where a main agent can spawn sub-agents recursively, each with its own chat tab, isolated context and memory, with results flowing back to the main agent. -- evidence: [readme.md#L54-L60](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L54-L60), [readme.md#L51-L51](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L51-L51)
  - [observation/documented] The README claims each sub-agent can use a different model from 50+ providers, enabling task-specific agents such as testing, security, and documentation agents. -- evidence: [readme.md#L63-L68](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L63-L68), [readme.md#L54-L60](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L54-L60)
More evidence: [full detail](kade.detail.md)

Metadata and full claim list: [full detail](kade.detail.md)
Human notes ([notes](kade.notes.md), never overwritten by build)

[Back to map index](../../index.md)
