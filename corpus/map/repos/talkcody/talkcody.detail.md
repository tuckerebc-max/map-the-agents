# talkcody/talkcody -- full detail

[Back to orientation](talkcody.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/talkcody/talkcody/5543bf9264366daa2f26880095fc34e016ffb304/1104f8fbbb441e08.json](../../../wiki/dossiers/talkcody/talkcody/5543bf9264366daa2f26880095fc34e016ffb304/1104f8fbbb441e08.json)

## specifications (1 claim(s))

- [observation/documented] TalkCody is described as a free, open-source AI coding agent licensed under the MIT License, with releases on GitHub. -- evidence: [README.md#L8-L10](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L8-L10), [README.md#L6-L6](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L6-L6), [README.md#L112-L112](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L112-L112) (`clm_fdcce1ded6504887e309cd161cb2910261f55d6131549abb7400b0bb129ec0c3`)

## components (2 claim(s))

- [observation/documented] Frontend stack includes React 19, TypeScript, Vite 7, Tailwind CSS 4, Shadcn UI, Zustand state management, Monaco Editor, and the Vercel AI SDK. -- evidence: [docs/content/docs/en/open-source/architecture.mdx#L45-L48](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L45-L48), [docs/content/docs/en/open-source/architecture.mdx#L61-L62](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L61-L62), [docs/content/docs/en/open-source/architecture.mdx#L58-L59](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L58-L59), [docs/content/docs/en/open-source/architecture.mdx#L55-L56](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L55-L56), [docs/content/docs/en/open-source/architecture.mdx#L50-L53](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L50-L53) (`clm_c99f30edad33a5e047615804d49935c65015a832f75453d7a4720d5fdb099983`)
- [observation/documented] The Rust backend uses libSQL (SQLite-compatible embedded database with full-text and vector search) and tree-sitter for code navigation. -- evidence: [docs/content/docs/en/open-source/architecture.mdx#L74-L77](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L74-L77), [docs/content/docs/en/open-source/architecture.mdx#L72-L72](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L72-L72), [docs/content/docs/en/open-source/architecture.mdx#L79-L79](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L79-L79) (`clm_7881da5e2f26dfc648da0646b2f493c4f4bc5da1bf1ba971b44471413bb62c92`)

## design-choices (1 claim(s))

- [observation/documented] The product uses a two-tier architecture: a React 19 + TypeScript frontend and a Tauri 2 + Rust backend communicating over IPC. -- evidence: [README.md#L86-L86](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L86-L86), [docs/content/docs/en/open-source/architecture.mdx#L11-L39](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L11-L39), [docs/content/docs/en/open-source/architecture.mdx#L66-L68](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L66-L68) (`clm_f6b260120d0436848f1391d12ae14479baba2505bb47822879f2ee0512719db4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to a Development Setup Guide and CONTRIBUTING.md for building from source and contribution details. -- evidence: [README.md#L101-L101](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L101-L101), [README.md#L80-L80](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L80-L80), [README.md#L78-L78](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L78-L78) (`clm_901c136f5acb1139632087c32c7ba4a777c75a35be2261a418451bd385310642`)

## skills-patterns (4 claim(s))

- [observation/documented] Skills are pre-configured packages containing system prompt snippets, workflow rules, reference docs, and executable scripts, following the Agent Skills Specification standard. -- evidence: [docs/content/docs/en/features/skills.mdx#L14-L18](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L14-L18), [docs/content/docs/en/features/skills.mdx#L22-L24](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L22-L24), [docs/content/docs/en/features/skills.mdx#L28-L28](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L28-L28) (`clm_62d6e6c10118a8cc439316a8267ac53cdab9a7be61dbaa8a24f11e34f3d34534`)
- [observation/documented] Skills use a standard directory layout with a required SKILL.md plus optional scripts, references, and assets directories. -- evidence: [docs/content/docs/en/features/skills.mdx#L32-L44](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L32-L44) (`clm_30f6187e5394d2fb01df7c4a3d76a1f82d22548e1a79ff13cb8212c285372d5f`)
- [observation/documented] Skills can be installed from a marketplace, imported from GitHub (single or batch, with automatic directory-type detection), created, edited, and exported for use in other tools. -- evidence: [docs/content/docs/en/features/skills.mdx#L125-L127](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L125-L127), [docs/content/docs/en/features/skills.mdx#L101-L105](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L101-L105), [docs/content/docs/en/features/skills.mdx#L72-L74](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L72-L74), [docs/content/docs/en/features/skills.mdx#L82-L88](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L82-L88), [docs/content/docs/en/features/skills.mdx#L92-L99](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L92-L99), [docs/content/docs/en/features/skills.mdx#L113-L118](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L113-L118) (`clm_407fcea2b7b03e37d4f28bb2ffea510ee204cddd4842f4447469bee4954236dc`)
- [observation/documented] Unlike agents (one at a time, full system prompt), multiple skills can be activated simultaneously to add domain knowledge to a conversation. -- evidence: [docs/content/docs/en/features/skills.mdx#L140-L142](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L140-L142), [docs/content/docs/en/features/skills.mdx#L133-L138](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/skills.mdx#L133-L138) (`clm_cd976b5fb2443d0eea7337408c445f8481272b77314590ec153ff2ac784e18ed`)

## interfaces (3 claim(s))

- [observation/documented] The agent ships built-in tools for file read/write/edit, code search, glob matching, Bash command execution, web fetch/search, calling other agents, todo lists, and asking the user questions. -- evidence: [docs/content/docs/en/features/tools.mdx#L50-L54](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L50-L54), [docs/content/docs/en/features/tools.mdx#L25-L29](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L25-L29), [docs/content/docs/en/features/tools.mdx#L45-L46](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L45-L46), [docs/content/docs/en/features/tools.mdx#L40-L42](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L40-L42), [docs/content/docs/en/features/tools.mdx#L33-L36](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L33-L36) (`clm_db7aa50e12351c6b55da8bb6afe7fd5a793d9bf8b612837e5f2e3ec2da4ff1b3`)
- [observation/documented] The app supports multimodal input (text, voice, images, files), MCP server support, a built-in terminal, and an agents & skills marketplace. -- evidence: [README.md#L45-L50](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L45-L50) (`clm_55d716d6f6b0203c6ad5e217257fe91eea8c6a828f4d6769d4946ed6602830fa`)
- [observation/documented] Installers are offered for macOS (Apple Silicon/Intel), Windows x64, and Linux x86_64 AppImage. -- evidence: [README.md#L58-L60](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L58-L60) (`clm_022e01b588d3ddcf2aef247a3afbd34bed294d295aa8237a5a07715c79947d36`)

## memory-state (1 claim(s))

- [observation/documented] All data, conversations, and code are stored locally on the user's machine, with local SQLite storage shown in the architecture diagram. -- evidence: [README.md#L40-L42](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L40-L42), [docs/content/docs/en/open-source/architecture.mdx#L11-L39](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/open-source/architecture.mdx#L11-L39) (`clm_456f413ca04a82c286606f0a4a47eceb2f130ae154f7da8f35e9a36f9e4b22a2`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Users can temporarily enable or disable tools per conversation via a tools panel; changes apply only to the current session and reset to defaults after app restart. -- evidence: [docs/content/docs/en/features/tools.mdx#L73-L75](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L73-L75), [docs/content/docs/en/features/tools.mdx#L68-L71](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L68-L71), [docs/content/docs/en/features/tools.mdx#L66-L66](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L66-L66) (`clm_5407cd6fa0835215d5da787539e5d13591109dac8599e3d2285b76e371048beb`)
- [observation/documented] The docs recommend a least-privilege approach when configuring agent tools, e.g. a code reviewer agent gets read/search but not write or Bash. -- evidence: [docs/content/docs/en/features/tools.mdx#L81-L81](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L81-L81), [docs/content/docs/en/features/tools.mdx#L83-L89](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/docs/content/docs/en/features/tools.mdx#L83-L89) (`clm_303c6d5d71097686d0b82ff9581679379bf3d922f62ebbb64af9dda1974b5cd5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project acknowledges dependencies on Tauri, Bun, Monaco Editor, libSQL, Shadcn UI, and Fumadocs, among others. -- evidence: [README.md#L117-L124](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L117-L124) (`clm_d8b09a045891925e66f5bc3e186fc2ee26c379d0ce61174d48c829f77fe13005`)
- [observation/documented] The product supports multiple AI providers including OpenAI, Anthropic, Google, and local models via Ollama or LM Studio, and can leverage ChatGPT Plus or GitHub Copilot subscriptions. -- evidence: [README.md#L40-L42](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L40-L42), [README.md#L21-L25](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L21-L25), [README.md#L35-L37](https://github.com/talkcody/talkcody/blob/5543bf9264366daa2f26880095fc34e016ffb304/README.md#L35-L37) (`clm_6d9bad68aa14a3ee593d5ea6c001c53c1788c044187adcaf8966b40655a8e804`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

