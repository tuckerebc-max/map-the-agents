# mininglamp-oss/octo-web

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 03b64e2cc53b @ 434c171c2ec4ceb4

## Summary (orientation draft, not independently verified)

Selected evidence records: octo-web is a TypeScript/React front-end that communicates with octo-server over REST and WebSocket, and ships as both a browser build and an Electron-packaged desktop client. The repository layout includes route-level pages (chat, channels, org, settings), a shared UI kit, client state, a REST/WebSocket API client, i18n resources, and an Electron bootstrap directory.

## Source coverage

Source coverage (partial): 3 of 39 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] octo-web is a TypeScript/React front-end that communicates with octo-server over REST and WebSocket, and ships as both a browser build and an Electron-packaged desktop client. -- evidence: [README.md#L31-L34](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L31-L34)
- components (1 claim(s)):
  - [observation/documented] The repository layout includes route-level pages (chat, channels, org, settings), a shared UI kit, client state, a REST/WebSocket API client, i18n resources, and an Electron bootstrap directory. -- evidence: [README.md#L59-L67](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L59-L67)
- design-choices (2 claim(s)):
  - [observation/documented] The Electron PC shell is intentionally thin: it hosts the same React app and forwards IPC for native capabilities such as tray, notifications, file drop, and auto-update, while the browser build runs without any Electron dependency. -- evidence: [README.md#L78-L80](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L78-L80)
  - [observation/documented] The UI provides first-class surfaces for AI agent conversations, including streaming replies, typing indicators, inline tool-call previews, read receipts, and agent-vs-human identity chips. -- evidence: [README.md#L38-L40](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L38-L40)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to work in an assigned worktree rather than the main repository directory, and to consult DEVELOPMENT.md's quick-reference sections before starting tasks. -- evidence: [AGENTS.md#L13-L13](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/AGENTS.md#L13-L13), [AGENTS.md#L11-L11](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/AGENTS.md#L11-L11)
  - [observation/documented] Repository development practice: CLAUDE.md documents a pnpm monorepo with Turborepo, Vite, and Vitest, with apps for the main web application and a browser extension plus shared dmwork packages. -- evidence: [CLAUDE.md#L38-L51](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L38-L51), [CLAUDE.md#L9-L12](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L9-L12), [CLAUDE.md#L7-L7](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L7-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] By default the web build expects an octo-server instance at http://localhost:8080, configurable via VITE_API_* values in a .env.local file copied from .env.example. -- evidence: [README.md#L51-L53](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L51-L53)
  - [observation/documented] The client is part of an ecosystem where octo-web, Android, iOS, and admin clients connect to octo-server, which in turn links to task, AI-summary, and adapter services built on a shared Go library. -- evidence: [README.md#L94-L99](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L94-L99), [README.md#L106-L116](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L106-L116), [README.md#L101-L104](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L101-L104), [README.md#L86-L92](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L86-L92)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](octo-web.detail.md)

Metadata and full claim list: [full detail](octo-web.detail.md)
Human notes ([notes](octo-web.notes.md), never overwritten by build)

[Back to map index](../../index.md)
