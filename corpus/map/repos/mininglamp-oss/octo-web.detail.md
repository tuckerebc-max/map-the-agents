# mininglamp-oss/octo-web -- full detail

[Back to orientation](octo-web.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mininglamp-oss/octo-web/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/434c171c2ec4ceb4.json](../../../wiki/dossiers/mininglamp-oss/octo-web/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/434c171c2ec4ceb4.json)

## specifications (1 claim(s))

- [observation/documented] octo-web is a TypeScript/React front-end that communicates with octo-server over REST and WebSocket, and ships as both a browser build and an Electron-packaged desktop client. -- evidence: [README.md#L31-L34](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L31-L34) (`clm_7114e9ab302d865e3d3fc593d3cb0dc52b3770f51f2755dc827798921162e77d`)

## components (1 claim(s))

- [observation/documented] The repository layout includes route-level pages (chat, channels, org, settings), a shared UI kit, client state, a REST/WebSocket API client, i18n resources, and an Electron bootstrap directory. -- evidence: [README.md#L59-L67](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L59-L67) (`clm_06ac04a20d191b2643cec1d3105cf59fd4c93b0f93ac305d66dc3a4747478b5f`)

## design-choices (2 claim(s))

- [observation/documented] The Electron PC shell is intentionally thin: it hosts the same React app and forwards IPC for native capabilities such as tray, notifications, file drop, and auto-update, while the browser build runs without any Electron dependency. -- evidence: [README.md#L78-L80](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L78-L80) (`clm_6d8dcf0fffa51a55c83dca8c94ec91aba69f050ddd03015af9de60aa95d59a9d`)
- [observation/documented] The UI provides first-class surfaces for AI agent conversations, including streaming replies, typing indicators, inline tool-call previews, read receipts, and agent-vs-human identity chips. -- evidence: [README.md#L38-L40](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L38-L40) (`clm_ec08e473455bfef0440bdf4ed256e442fab74e2e2dfc445123ae4f610c1bdcb8`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to work in an assigned worktree rather than the main repository directory, and to consult DEVELOPMENT.md's quick-reference sections before starting tasks. -- evidence: [AGENTS.md#L13-L13](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/AGENTS.md#L13-L13), [AGENTS.md#L11-L11](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/AGENTS.md#L11-L11) (`clm_c7cee3a7ea22493fa8a16b0754c10eb015e5d3e090325ba9435102108b59193d`)
- [observation/documented] Repository development practice: CLAUDE.md documents a pnpm monorepo with Turborepo, Vite, and Vitest, with apps for the main web application and a browser extension plus shared dmwork packages. -- evidence: [CLAUDE.md#L38-L51](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L38-L51), [CLAUDE.md#L9-L12](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L9-L12), [CLAUDE.md#L7-L7](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L7-L7) (`clm_ef563e2e9aa80d0f2de18c5ba0374143c18fb5e9a5c3727c7edf5eb1110cbd2c`)
- [observation/documented] Repository development practice: CLAUDE.md prescribes coding conventions including Conventional Commits, PascalCase component directories, ProviderListener-based ViewModels instead of Redux/Zustand, and routing API calls through WKApp.apiClient. -- evidence: [CLAUDE.md#L63-L63](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L63-L63), [CLAUDE.md#L93-L102](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L93-L102), [CLAUDE.md#L55-L55](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/CLAUDE.md#L55-L55) (`clm_ee45d5d48d2d7ffcd371df0fd6c5c79c2b27cc2504e2d53ec8e1c9fea3a3a4ef`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] By default the web build expects an octo-server instance at http://localhost:8080, configurable via VITE_API_* values in a .env.local file copied from .env.example. -- evidence: [README.md#L51-L53](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L51-L53) (`clm_b608a62d7b8f4005a0c4ad085dfd42eed12afa73e2e5b71b78befd618d2d4ab0`)
- [observation/documented] The client is part of an ecosystem where octo-web, Android, iOS, and admin clients connect to octo-server, which in turn links to task, AI-summary, and adapter services built on a shared Go library. -- evidence: [README.md#L94-L99](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L94-L99), [README.md#L106-L116](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L106-L116), [README.md#L101-L104](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L101-L104), [README.md#L86-L92](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L86-L92) (`clm_093c4f407480827a2441f70b02b22315356aed11eea9310237d0dd7ee2b12132`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project's original scaffolding derives from TangSengDaoDaoWeb, and octo-server is described as driving a WuKongIM real-time messaging core behind this client. -- evidence: [README.md#L155-L156](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L155-L156) (`clm_0d20650047d91a77b346ebcd94f87f7ff1a5b3a6f922e37706cd6829271e040f`)
- [observation/documented] The project is licensed under Apache License 2.0, with third-party attributions listed in a NOTICE file. -- evidence: [README.md#L149-L149](https://github.com/Mininglamp-OSS/octo-web/blob/03b64e2cc53b69e6c1e7e24e315f3a329dba0bfe/README.md#L149-L149) (`clm_563666c1db14778b2324b9af50140a2acbd6344b892630441de5e430ac7e06db`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

