# kadeai/kade -- full detail

[Back to orientation](kade.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kadeai/kade/616148222f7482e9a8f714e7827619cb673d2214/d84e039d68ba41fa.json](../../../wiki/dossiers/kadeai/kade/616148222f7482e9a8f714e7827619cb673d2214/d84e039d68ba41fa.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Documentation describes an MCP Store with 25,000+ MCPs via LobeHub API integration, offering one-click installation, marketplace search, and enterprise features like security scanning and team sharing. -- evidence: [readme.md#L215-L218](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L215-L218), [readme.md#L213-L213](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L213-L213) (`clm_95b3dd02a6f8be5421abc15e4d7907be85c12384d058f21e1588531efabb979c`)
- [observation/documented] The README lists OAuth support for several platforms (Antigravity, Kilo Code, Gemini CLI, Claude Code, OpenAI Codex) with token storage, auto-refresh, and local callback servers with CSRF protection. -- evidence: [readme.md#L226-L229](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L226-L229), [readme.md#L224-L224](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L224-L224) (`clm_6f64295e21d7967cc5bfbca74034fbcdb22bcba9c1270dabab8ffc09cc0ee8ef`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The changelog records added skills support, including installing and enabling skills and installing skills from skills.sh via a marketplace tab. -- evidence: [CHANGELOG.md#L26-L28](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L26-L28) (`clm_ef8bd9ef9c188d8e2b5829286fe2fef9bf5df1ae50b58225bad927a1ba859ab0`)

## interfaces (2 claim(s))

- [observation/documented] The README describes text-based tool-calling protocols named Unified (CLI-like syntax such as <<read --path ...>>) and Markdown (code blocks), alongside supported legacy JSON and XML formats. -- evidence: [readme.md#L142-L144](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L142-L144), [readme.md#L114-L114](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L114-L114), [readme.md#L116-L119](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L116-L119), [readme.md#L139-L139](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L139-L139) (`clm_e07ceb54b40ec26d19cc296440d9b421fd57a1f739da18cdf7b51cf9cfbd2bde`)
- [observation/documented] The changelog states Markdown, XML, and CLI tool schemas were removed in favor of an overhauled native JSON system and a new 'Aero' schema allowing single-letter tool calls, which conflicts with the README's four-protocol claim. -- evidence: [readme.md#L121-L121](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L121-L121), [CHANGELOG.md#L35-L48](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L35-L48) (`clm_8b8e10eb1b1dca668dc9d9561f0c793eb70a15b39ed1a435f57dbe0adfa57706`)

## memory-state (2 claim(s))

- [observation/documented] Documentation claims each chat remembers its selected AI model across sessions and automatically restores it, allowing multiple models to run concurrently in different chat windows. -- evidence: [readme.md#L93-L96](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L93-L96), [CHANGELOG.md#L127-L131](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L127-L131), [readme.md#L90-L90](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L90-L90) (`clm_71f1e7e75d47a1ed76d68098a6acdb1a9c5186a9c3d658e97acb7f3f875af6a8`)
- [observation/documented] The changelog says task history was moved from VS Code globalState (SQLite) to disk-based JSON storage at globalStorageUri/task_history.json, using an in-memory cache with debounced writes to reduce I/O. -- evidence: [CHANGELOG.md#L119-L121](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L119-L121), [CHANGELOG.md#L101-L106](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L101-L106) (`clm_b60fff4795f6952f6cdf6237a7b7e5638e5acc0ce5f36ad5be13cfcd59ec11fe`)

## orchestration (2 claim(s))

- [observation/documented] Documentation describes a sub-agent system where a main agent can spawn sub-agents recursively, each with its own chat tab, isolated context and memory, with results flowing back to the main agent. -- evidence: [readme.md#L54-L60](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L54-L60), [readme.md#L51-L51](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L51-L51) (`clm_97286a0fc0c149e615f362737c251768b319fdbabd953dd404529f37fc98200b`)
- [observation/documented] The README claims each sub-agent can use a different model from 50+ providers, enabling task-specific agents such as testing, security, and documentation agents. -- evidence: [readme.md#L63-L68](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L63-L68), [readme.md#L54-L60](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L54-L60) (`clm_f0dfeac32df9a0ae9b3108cd0cd9447f8bea0ad02f75ce57030eb56a9e350f05`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README advertises support for 50+ AI providers including OpenAI, Anthropic, Google, and local models, usable in any combination across chats and sub-agents. -- evidence: [readme.md#L63-L68](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/readme.md#L63-L68) (`clm_c6b42adf1c0b650b28672c9e2f93ea1891e172789647c7db971d0ab18d081dd8`)

## limitations (2 claim(s))

- [observation/documented] Known issues in the changelog include the native-protocol edit tool not live-streaming in the GUI, LobeHub MCP search being broken, and rare cases of dropped streams, tool output leaking into chat, and duplicating edit/write GUI blocks. -- evidence: [CHANGELOG.md#L18-L18](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L18-L18), [CHANGELOG.md#L52-L56](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L52-L56) (`clm_0627396f53bb732fab4aa7cb2251eba29ac476cbcc12c43e518279ab4038d148`)
- [observation/documented] The changelog notes the Kiro provider currently supports only the Sonnet 4.5 model, working with both Trial and Pro accounts. -- evidence: [CHANGELOG.md#L35-L48](https://github.com/KADEAI/Kade/blob/616148222f7482e9a8f714e7827619cb673d2214/CHANGELOG.md#L35-L48) (`clm_500e495548e065dc6510f5fc5d00ec13ee191168b77eb30c5b6e2580e54102c5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

