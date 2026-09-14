# olasunkanmi-se/codebuddy -- full detail

[Back to orientation](codebuddy.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/olasunkanmi-se/codebuddy/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/345f3ad884e40c16.json](../../../wiki/dossiers/olasunkanmi-se/codebuddy/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/345f3ad884e40c16.json)

## specifications (1 claim(s))

- [observation/documented] CodeBuddy is described as a multi-agent AI software engineer running inside VS Code that plans, writes, debugs, tests, documents, and deploys features autonomously. -- evidence: [README.md#L11-L11](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L11-L11) (`clm_915cf4d72fd0dba7452980091ace43030d68c6bddd6cf3989cbc0dd12db213f4`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] AgentSafetyGuard enforces configurable hard limits per session (e.g. 2,000 stream events, 400 tool calls, 10-minute runtime) plus per-tool caps and loop detection on repeated file edits. -- evidence: [README.md#L136-L136](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L136-L136), [README.md#L138-L142](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L138-L142) (`clm_a4fe66aa2a992cec69f0d78c45fd6869572074445eca66487beb8cafa2134084`)
- [observation/documented] ProviderFailoverService switches to backup LLM providers on failure, classifying HTTP errors with per-reason cooldowns and probing providers before cooldown expiry. -- evidence: [README.md#L202-L202](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L202-L202), [README.md#L204-L209](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L204-L209) (`clm_f8e2a0b876676177b5cc444475070c21e7e68000badcbc3b0c3e75fe51e22dd1`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] 16 skills ship bundled, each defined by a SKILL.md with optional install scripts; workspace (.codebuddy/skills/) and global (~/.codebuddy/skills/) skills are also discovered, with workspace precedence on name collisions. -- evidence: [README.md#L425-L428](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L425-L428), [README.md#L402-L402](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L402-L402) (`clm_74ad62c5506398a697f3ff5b80afd0e00cfb55282828c71fcdeadea1db2397aa`)

## interfaces (2 claim(s))

- [observation/documented] The extension host and React webview communicate over a bidirectional postMessage protocol with structured commands and typed events. -- evidence: [README.md#L84-L84](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L84-L84) (`clm_b9c81077b11d97935120bb367b0baf96cb8be242227cfbde8ee9ce1fbdd25bcf`)
- [observation/documented] Agent-proposed file changes pass through a diff review pipeline with a Pending Changes panel, per-change apply/reject, composer sessions, and an optional auto-approve setting. -- evidence: [README.md#L342-L349](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L342-L349), [README.md#L340-L340](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L340-L340) (`clm_2fde6cc599dd170e0c39de0f685c68ac0d965ff93f926fbf0809a7d241d56883`)

## memory-state (2 claim(s))

- [observation/documented] Persistence spans a TTL in-memory cache, .codebuddy/ file storage, SQLite with FTS4, a SQLite-backed LangGraph checkpointer, VS Code SecretStorage, and a vector store for embeddings. -- evidence: [README.md#L88-L96](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L88-L96) (`clm_ed621fd4ef75803a7fe5de5ad2f28dc6c530b8a586de339b3656dc66e5d6526d`)
- [observation/documented] Persistent memory is file-backed at .codebuddy/memory.json with Knowledge/Rule/Experience categories, user and project scopes, and automatic injection into the agent's system prompt. -- evidence: [README.md#L473-L473](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L473-L473), [README.md#L475-L478](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L475-L478) (`clm_6209d64466e58355ba3196c61a993ba71567490ba1bf5ac3201b03a720a83e39`)

## orchestration (2 claim(s))

- [observation/documented] A singleton Orchestrator event bus mediates all subsystem communication via typed publish/subscribe events, decoupling agent, webview, and service layers. -- evidence: [README.md#L61-L61](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L61-L61) (`clm_5612c0bdea9947bef044d23c28c76bcf668e05fbf6ed814592f05647e55af131`)
- [observation/documented] A Developer Agent coordinates seven specialized subagents (analyzer, doc writer, debugger, file organizer, architect, reviewer, tester) built on the LangGraph DeepAgents framework, each with role-filtered tools. -- evidence: [README.md#L120-L128](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L120-L128), [README.md#L118-L118](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L118-L118) (`clm_42d1081ddaf28911ca0103ba773726bb3cb53c9f80b8a26b6d291d6b6fec21e9`)

## tools-permissions (2 claim(s))

- [observation/documented] PermissionScopeService offers restricted/standard/trusted profiles configured per workspace via .codebuddy/permissions.json, with a catastrophic deny floor (e.g. rm -rf /) enforced even in trusted mode. -- evidence: [README.md#L534-L534](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L534-L534), [README.md#L526-L526](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L526-L526), [README.md#L528-L532](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L528-L532) (`clm_c5cc43eb134092c3215d188cbc8ce458020947fd0380b1c58b3b1236d553d573`)
- [observation/documented] Destructive operations like file deletion trigger a human-in-the-loop interrupt requiring explicit approval before the agent continues. -- evidence: [README.md#L148-L148](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L148-L148) (`clm_09a7e8a6877a9cee27cfe9969017311dcaf6b765eb86dd70a5c418b5bfe14816`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The agent layer is built on LangGraph/LangChain-compatible chat models, with Tree-sitter WASM parsers for 7 languages and sql.js (WASM) SQLite with FTS4 for persistence. -- evidence: [README.md#L118-L118](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L118-L118), [README.md#L88-L96](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L88-L96), [README.md#L100-L100](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L100-L100) (`clm_634f05b733df1f74405901084fe4734d87bf6691d41d33be668a13289c6ac4c5`)
- [observation/documented] The README lists 10 supported AI providers including cloud options (Gemini, Claude, OpenAI, DeepSeek, Qwen, Groq, GLM, Grok) and local options (Ollama, Docker Model Runner). -- evidence: [README.md#L183-L194](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L183-L194) (`clm_38abd3a860bd2a4117e14a42de553be90d4faef0cb5c0d900fcc54a1db5f2773`)

## limitations (1 claim(s))

- [observation/documented] The public repository is archived: active development moved to a private repo and the public repo no longer accepts features, fixes, issues, or PRs. -- evidence: [README.md#L1-L4](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L1-L4) (`clm_a4e229bc6615e89d8ac3ea2f25bf76556897e641d568c18b9f803c01e579920e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

