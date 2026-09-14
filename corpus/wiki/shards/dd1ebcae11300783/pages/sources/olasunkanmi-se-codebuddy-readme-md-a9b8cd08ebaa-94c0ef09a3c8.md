---
access: public
aliases: []
claim_ids:
- clm_09a7e8a6877a9cee27cfe9969017311dcaf6b765eb86dd70a5c418b5bfe14816
- clm_2fde6cc599dd170e0c39de0f685c68ac0d965ff93f926fbf0809a7d241d56883
- clm_38abd3a860bd2a4117e14a42de553be90d4faef0cb5c0d900fcc54a1db5f2773
- clm_42d1081ddaf28911ca0103ba773726bb3cb53c9f80b8a26b6d291d6b6fec21e9
- clm_5612c0bdea9947bef044d23c28c76bcf668e05fbf6ed814592f05647e55af131
- clm_6209d64466e58355ba3196c61a993ba71567490ba1bf5ac3201b03a720a83e39
- clm_634f05b733df1f74405901084fe4734d87bf6691d41d33be668a13289c6ac4c5
- clm_74ad62c5506398a697f3ff5b80afd0e00cfb55282828c71fcdeadea1db2397aa
- clm_915cf4d72fd0dba7452980091ace43030d68c6bddd6cf3989cbc0dd12db213f4
- clm_a4e229bc6615e89d8ac3ea2f25bf76556897e641d568c18b9f803c01e579920e
- clm_a4fe66aa2a992cec69f0d78c45fd6869572074445eca66487beb8cafa2134084
- clm_b9c81077b11d97935120bb367b0baf96cb8be242227cfbde8ee9ce1fbdd25bcf
- clm_c5cc43eb134092c3215d188cbc8ce458020947fd0380b1c58b3b1236d553d573
- clm_ed621fd4ef75803a7fe5de5ad2f28dc6c530b8a586de339b3656dc66e5d6526d
- clm_f8e2a0b876676177b5cc444475070c21e7e68000badcbc3b0c3e75fe51e22dd1
maturity: draft
page_id: pg_bfefa820defa5b81979594c0ef09a3c8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4cc851d8a25e591c9e76844fec6b6f8e
title: olasunkanmi-SE/codebuddy/README.md @ a9b8cd08ebaa
updated_at: '2026-09-14T02:24:32Z'
---

# olasunkanmi-SE/codebuddy/README.md @ a9b8cd08ebaa

<!-- rcw:begin owner=source:src_4cc851d8a25e591c9e76844fec6b6f8e block=evidence -->
- Destructive operations like file deletion trigger a human-in-the-loop interrupt requiring explicit approval before the agent continues. [@claim:clm_09a7e8a6877a9cee27cfe9969017311dcaf6b765eb86dd70a5c418b5bfe14816]
- Agent-proposed file changes pass through a diff review pipeline with a Pending Changes panel, per-change apply/reject, composer sessions, and an optional auto-approve setting. [@claim:clm_2fde6cc599dd170e0c39de0f685c68ac0d965ff93f926fbf0809a7d241d56883]
- The README lists 10 supported AI providers including cloud options (Gemini, Claude, OpenAI, DeepSeek, Qwen, Groq, GLM, Grok) and local options (Ollama, Docker Model Runner). [@claim:clm_38abd3a860bd2a4117e14a42de553be90d4faef0cb5c0d900fcc54a1db5f2773]
- A Developer Agent coordinates seven specialized subagents (analyzer, doc writer, debugger, file organizer, architect, reviewer, tester) built on the LangGraph DeepAgents framework, each with role-filtered tools. [@claim:clm_42d1081ddaf28911ca0103ba773726bb3cb53c9f80b8a26b6d291d6b6fec21e9]
- A singleton Orchestrator event bus mediates all subsystem communication via typed publish/subscribe events, decoupling agent, webview, and service layers. [@claim:clm_5612c0bdea9947bef044d23c28c76bcf668e05fbf6ed814592f05647e55af131]
- Persistent memory is file-backed at .codebuddy/memory.json with Knowledge/Rule/Experience categories, user and project scopes, and automatic injection into the agent's system prompt. [@claim:clm_6209d64466e58355ba3196c61a993ba71567490ba1bf5ac3201b03a720a83e39]
- The agent layer is built on LangGraph/LangChain-compatible chat models, with Tree-sitter WASM parsers for 7 languages and sql.js (WASM) SQLite with FTS4 for persistence. [@claim:clm_634f05b733df1f74405901084fe4734d87bf6691d41d33be668a13289c6ac4c5]
- 16 skills ship bundled, each defined by a SKILL.md with optional install scripts; workspace (.codebuddy/skills/) and global (~/.codebuddy/skills/) skills are also discovered, with workspace precedence on name collisions. [@claim:clm_74ad62c5506398a697f3ff5b80afd0e00cfb55282828c71fcdeadea1db2397aa]
- CodeBuddy is described as a multi-agent AI software engineer running inside VS Code that plans, writes, debugs, tests, documents, and deploys features autonomously. [@claim:clm_915cf4d72fd0dba7452980091ace43030d68c6bddd6cf3989cbc0dd12db213f4]
- The public repository is archived: active development moved to a private repo and the public repo no longer accepts features, fixes, issues, or PRs. [@claim:clm_a4e229bc6615e89d8ac3ea2f25bf76556897e641d568c18b9f803c01e579920e]
- AgentSafetyGuard enforces configurable hard limits per session (e.g. 2,000 stream events, 400 tool calls, 10-minute runtime) plus per-tool caps and loop detection on repeated file edits. [@claim:clm_a4fe66aa2a992cec69f0d78c45fd6869572074445eca66487beb8cafa2134084]
- The extension host and React webview communicate over a bidirectional postMessage protocol with structured commands and typed events. [@claim:clm_b9c81077b11d97935120bb367b0baf96cb8be242227cfbde8ee9ce1fbdd25bcf]
- PermissionScopeService offers restricted/standard/trusted profiles configured per workspace via .codebuddy/permissions.json, with a catastrophic deny floor (e.g. rm -rf /) enforced even in trusted mode. [@claim:clm_c5cc43eb134092c3215d188cbc8ce458020947fd0380b1c58b3b1236d553d573]
- Persistence spans a TTL in-memory cache, .codebuddy/ file storage, SQLite with FTS4, a SQLite-backed LangGraph checkpointer, VS Code SecretStorage, and a vector store for embeddings. [@claim:clm_ed621fd4ef75803a7fe5de5ad2f28dc6c530b8a586de339b3656dc66e5d6526d]
- ProviderFailoverService switches to backup LLM providers on failure, classifying HTTP errors with per-reason cooldowns and probing providers before cooldown expiry. [@claim:clm_f8e2a0b876676177b5cc444475070c21e7e68000badcbc3b0c3e75fe51e22dd1]
<!-- rcw:end owner=source:src_4cc851d8a25e591c9e76844fec6b6f8e block=evidence -->

## Researcher notes

