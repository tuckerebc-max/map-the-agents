# talkcody/talkcody

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5543bf926436 @ 1104f8fbbb441e08

## Summary (orientation draft, not independently verified)

TalkCody is a free, open-source (MIT) desktop AI coding agent built with React 19/TypeScript and Tauri 2/Rust, documented with local storage, multi-provider model support, a Skills system following the Agent Skills Specification, and built-in agent tools with per-session enable/disable.

## Source coverage

Source coverage (partial): 6 of 88 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] TalkCody is described as a free, open-source AI coding agent licensed under the MIT License, with releases on GitHub. -- evidence: [README.md#L8-L10](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L8-L10), [README.md#L6-L6](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L6-L6), [README.md#L112-L112](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L112-L112)
- components (2 claim(s)):
  - [observation/documented] Frontend stack includes React 19, TypeScript, Vite 7, Tailwind CSS 4, Shadcn UI, Zustand state management, Monaco Editor, and the Vercel AI SDK. -- evidence: [docs/content/docs/en/open-source/architecture.mdx#L45-L48](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L45-L48), [docs/content/docs/en/open-source/architecture.mdx#L61-L62](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L61-L62), [docs/content/docs/en/open-source/architecture.mdx#L58-L59](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L58-L59), [docs/content/docs/en/open-source/architecture.mdx#L55-L56](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L55-L56), [docs/content/docs/en/open-source/architecture.mdx#L50-L53](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L50-L53)
  - [observation/documented] The Rust backend uses libSQL (SQLite-compatible embedded database with full-text and vector search) and tree-sitter for code navigation. -- evidence: [docs/content/docs/en/open-source/architecture.mdx#L74-L77](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L74-L77), [docs/content/docs/en/open-source/architecture.mdx#L72-L72](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L72-L72), [docs/content/docs/en/open-source/architecture.mdx#L79-L79](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L79-L79)
- design-choices (1 claim(s)):
  - [observation/documented] The product uses a two-tier architecture: a React 19 + TypeScript frontend and a Tauri 2 + Rust backend communicating over IPC. -- evidence: [README.md#L86-L86](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L86-L86), [docs/content/docs/en/open-source/architecture.mdx#L11-L39](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L11-L39), [docs/content/docs/en/open-source/architecture.mdx#L66-L68](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L66-L68)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to a Development Setup Guide and CONTRIBUTING.md for building from source and contribution details. -- evidence: [README.md#L101-L101](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L101-L101), [README.md#L80-L80](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L80-L80), [README.md#L78-L78](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L78-L78)
- skills-patterns (4 claim(s)):
  - [observation/documented] Skills are pre-configured packages containing system prompt snippets, workflow rules, reference docs, and executable scripts, following the Agent Skills Specification standard. -- evidence: [docs/content/docs/en/features/skills.mdx#L14-L18](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L14-L18), [docs/content/docs/en/features/skills.mdx#L22-L24](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L22-L24), [docs/content/docs/en/features/skills.mdx#L28-L28](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L28-L28)
  - [observation/documented] Skills use a standard directory layout with a required SKILL.md plus optional scripts, references, and assets directories. -- evidence: [docs/content/docs/en/features/skills.mdx#L32-L44](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L32-L44)
- interfaces (3 claim(s)):
  - [observation/documented] The agent ships built-in tools for file read/write/edit, code search, glob matching, Bash command execution, web fetch/search, calling other agents, todo lists, and asking the user questions. -- evidence: [docs/content/docs/en/features/tools.mdx#L50-L54](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L50-L54), [docs/content/docs/en/features/tools.mdx#L25-L29](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L25-L29), [docs/content/docs/en/features/tools.mdx#L45-L46](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L45-L46), [docs/content/docs/en/features/tools.mdx#L40-L42](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L40-L42), [docs/content/docs/en/features/tools.mdx#L33-L36](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L33-L36)
  - [observation/documented] The app supports multimodal input (text, voice, images, files), MCP server support, a built-in terminal, and an agents & skills marketplace. -- evidence: [README.md#L45-L50](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L45-L50)
- memory-state (1 claim(s)):
  - [observation/documented] All data, conversations, and code are stored locally on the user's machine, with local SQLite storage shown in the architecture diagram. -- evidence: [README.md#L40-L42](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L40-L42), [docs/content/docs/en/open-source/architecture.mdx#L11-L39](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L11-L39)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Users can temporarily enable or disable tools per conversation via a tools panel; changes apply only to the current session and reset to defaults after app restart. -- evidence: [docs/content/docs/en/features/tools.mdx#L73-L75](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L73-L75), [docs/content/docs/en/features/tools.mdx#L68-L71](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L68-L71), [docs/content/docs/en/features/tools.mdx#L66-L66](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L66-L66)
More evidence: [full detail](talkcody.detail.md)

Metadata and full claim list: [full detail](talkcody.detail.md)
Human notes ([notes](talkcody.notes.md), never overwritten by build)

[Back to map index](../../index.md)
