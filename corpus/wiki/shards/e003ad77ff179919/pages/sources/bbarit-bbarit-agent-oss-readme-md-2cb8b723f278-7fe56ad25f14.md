---
access: public
aliases: []
claim_ids:
- clm_0d2659750fde538df5d7143adc5b3aed6bfb7122f0f496fc1fbb508b9e641166
- clm_2216021a569e5d05ee9360ead06317cddca241b8f08b657b52b1573d8af78ed1
- clm_39129cf851bec6feea686110a067281614344a4fc4498b6affae232c4134aaca
- clm_40f14afbb5963c5b28f4e7f166b8f9262af9cb5302881db6a464ffda24591dcb
- clm_545317dd3eaa1072c408e37c1a38a844c81a14519918735d036f7a7fceef88fc
- clm_863dd1715948e36c66c02042ae25f0c66b9459d7802f9066feb311d32ee6f979
- clm_886300953789434820012f23e9ebf531b7a208f80f526dafa7d086ccded84ce1
- clm_ad9a0ff6b6e1ab57eb7b022bb83aa89f269b48140885f637d9bc6d884ffa98f8
- clm_c2a95d8cbae6aa5f551d5fa3228eb60c7c096beeb8b9a552d592b06dce5bdb26
- clm_cc1b26950ae3976bd5ce0545393c5a1df4c917f8dd1ccf912e10f6bdc6901884
- clm_daf19df9497a7f4e192d7217bffd7111d70db9189c524157b402c9168e3ec635
- clm_eeab7c0cdc6bce37b079f2d2836d6c821cd287ada12a72134fd4d2a6a22694ac
- clm_fe30cc7c849992853597789d7326ad6dbab30f982ee605925992e62db11ffe63
maturity: draft
page_id: pg_1351f31f1edd5e518c227fe56ad25f14
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d3be3296417550ee831e3d75febaf08f
title: bbarit/bbarit-agent-oss/README.md @ 2cb8b723f278
updated_at: '2026-09-14T01:37:39Z'
---

# bbarit/bbarit-agent-oss/README.md @ 2cb8b723f278

<!-- rcw:begin owner=source:src_d3be3296417550ee831e3d75febaf08f block=evidence -->
- Auto-memory recalls stored facts at turn start via keyword-overlap scoring without an LLM call, and a background sub-agent extracts durable facts typed as user, feedback, project, or reference after each turn. [@claim:clm_0d2659750fde538df5d7143adc5b3aed6bfb7122f0f496fc1fbb508b9e641166]
- The agent supports many LLM providers from one registry — Anthropic, OpenAI/Codex, Google Gemini/Vertex, OpenRouter, Groq, Mistral, Together, Fireworks, DeepSeek, Cerebras, Bedrock, GitHub Copilot, plus local models via Ollama. [@claim:clm_2216021a569e5d05ee9360ead06317cddca241b8f08b657b52b1573d8af78ed1]
- Repository development practice: contributors run cargo fmt --all, cargo build, and cargo test; CI runs fmt, build, and tests on Linux and macOS with clippy advisory, and fmt is treated as a hard gate. [@claim:clm_39129cf851bec6feea686110a067281614344a4fc4498b6affae232c4134aaca]
- Built-in tools called autonomously in the agent loop include read/write/edit, bash, grep/find/ls/tree, hybrid BM25+semantic code_search, web_search/web_fetch, a task sub-agent spawner, and an opt-in computer tool. [@claim:clm_40f14afbb5963c5b28f4e7f166b8f9262af9cb5302881db6a464ffda24591dcb]
- The --orchestrate flag runs each given task as an independent sub-agent process in parallel and collects the results. [@claim:clm_545317dd3eaa1072c408e37c1a38a844c81a14519918735d036f7a7fceef88fc]
- The agent ships 295 curated personas across 30 domains, each a markdown brief at personas/<division>/<id>.md; user-added .md files join the library without code changes, and personas are injected into the system prompt. [@claim:clm_863dd1715948e36c66c02042ae25f0c66b9459d7802f9066feb311d32ee6f979]
- Memories are stored as plain markdown files with a MEMORY.md index that users can edit, and the agent treats user edits as truth; sub-agents never extract memories to avoid recursion. [@claim:clm_886300953789434820012f23e9ebf531b7a208f80f526dafa7d086ccded84ce1]
- An /interop toggle (off by default) lets the agent read Claude Code and Codex MCP-server and skill configs as-is, read-only, using only stdio servers and skipping disabled entries. [@claim:clm_ad9a0ff6b6e1ab57eb7b022bb83aa89f269b48140885f637d9bc6d884ffa98f8]
- A per-project wiki stores markdown pages in a shared vault scoped per project, with get/set/list/search/delete actions, and mutating wiki actions are blocked in plan mode and under read-only personas. [@claim:clm_c2a95d8cbae6aa5f551d5fa3228eb60c7c096beeb8b9a552d592b06dce5bdb26]
- bbarit-oss is a terminal-native AI coding agent CLI that reads, writes, and edits code, runs shell commands, and ships as a single static Rust binary with no runtime to install. [@claim:clm_cc1b26950ae3976bd5ce0545393c5a1df4c917f8dd1ccf912e10f6bdc6901884]
- Non-interactive modes include --print, where stdout carries only the final answer while narration goes to stderr, and --mode json, which streams newline-delimited JSON events for programmatic consumers. [@claim:clm_daf19df9497a7f4e192d7217bffd7111d70db9189c524157b402c9168e3ec635]
- The project is a from-scratch Rust rewrite of Pi (MIT), keeping Pi's small agent-loop philosophy and provider-agnostic registry while adding an orchestrator, wiki, personas, and semantic code search; it reports near-zero source overlap with Pi. [@claim:clm_eeab7c0cdc6bce37b079f2d2836d6c821cd287ada12a72134fd4d2a6a22694ac]
- Tool access can be restricted with --tools/--exclude-tools/--no-tools, mutations can be gated behind project trust via --approve, and read-only personas refuse mutating tools. [@claim:clm_fe30cc7c849992853597789d7326ad6dbab30f982ee605925992e62db11ffe63]
<!-- rcw:end owner=source:src_d3be3296417550ee831e3d75febaf08f block=evidence -->

## Researcher notes

