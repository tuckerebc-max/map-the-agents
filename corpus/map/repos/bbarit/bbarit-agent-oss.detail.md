# bbarit/bbarit-agent-oss -- full detail

[Back to orientation](bbarit-agent-oss.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bbarit/bbarit-agent-oss/2cb8b723f2787aa587ef063d366b7cb408ead4aa/193ffd7e172b4267.json](../../../wiki/dossiers/bbarit/bbarit-agent-oss/2cb8b723f2787aa587ef063d366b7cb408ead4aa/193ffd7e172b4267.json)

## specifications (1 claim(s))

- [observation/documented] bbarit-oss is a terminal-native AI coding agent CLI that reads, writes, and edits code, runs shell commands, and ships as a single static Rust binary with no runtime to install. -- evidence: [README.md#L120-L125](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L120-L125) (`clm_cc1b26950ae3976bd5ce0545393c5a1df4c917f8dd1ccf912e10f6bdc6901884`)

## components (1 claim(s))

- [observation/documented] Built-in tools called autonomously in the agent loop include read/write/edit, bash, grep/find/ls/tree, hybrid BM25+semantic code_search, web_search/web_fetch, a task sub-agent spawner, and an opt-in computer tool. -- evidence: [README.md#L312-L320](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L312-L320) (`clm_40f14afbb5963c5b28f4e7f166b8f9262af9cb5302881db6a464ffda24591dcb`)

## design-choices (1 claim(s))

- [observation/documented] The project is a from-scratch Rust rewrite of Pi (MIT), keeping Pi's small agent-loop philosophy and provider-agnostic registry while adding an orchestrator, wiki, personas, and semantic code search; it reports near-zero source overlap with Pi. -- evidence: [README.md#L612-L612](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L612-L612), [README.md#L24-L81](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L24-L81) (`clm_eeab7c0cdc6bce37b079f2d2836d6c821cd287ada12a72134fd4d2a6a22694ac`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run cargo fmt --all, cargo build, and cargo test; CI runs fmt, build, and tests on Linux and macOS with clippy advisory, and fmt is treated as a hard gate. -- evidence: [README.md#L640-L641](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L640-L641), [README.md#L634-L638](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L634-L638), [ARCHITECTURE.md#L40-L47](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/ARCHITECTURE.md#L40-L47) (`clm_39129cf851bec6feea686110a067281614344a4fc4498b6affae232c4134aaca`)

## skills-patterns (1 claim(s))

- [observation/documented] The agent ships 295 curated personas across 30 domains, each a markdown brief at personas/<division>/<id>.md; user-added .md files join the library without code changes, and personas are injected into the system prompt. -- evidence: [README.md#L345-L349](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L345-L349), [README.md#L392-L397](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L392-L397), [README.md#L409-L412](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L409-L412) (`clm_863dd1715948e36c66c02042ae25f0c66b9459d7802f9066feb311d32ee6f979`)

## interfaces (2 claim(s))

- [observation/documented] Non-interactive modes include --print, where stdout carries only the final answer while narration goes to stderr, and --mode json, which streams newline-delimited JSON events for programmatic consumers. -- evidence: [README.md#L253-L254](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L253-L254), [README.md#L258-L259](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L258-L259) (`clm_daf19df9497a7f4e192d7217bffd7111d70db9189c524157b402c9168e3ec635`)
- [observation/documented] An /interop toggle (off by default) lets the agent read Claude Code and Codex MCP-server and skill configs as-is, read-only, using only stdio servers and skipping disabled entries. -- evidence: [README.md#L505-L510](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L505-L510), [README.md#L516-L516](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L516-L516), [README.md#L512-L514](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L512-L514), [README.md#L518-L522](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L518-L522) (`clm_ad9a0ff6b6e1ab57eb7b022bb83aa89f269b48140885f637d9bc6d884ffa98f8`)

## memory-state (3 claim(s))

- [observation/documented] Auto-memory recalls stored facts at turn start via keyword-overlap scoring without an LLM call, and a background sub-agent extracts durable facts typed as user, feedback, project, or reference after each turn. -- evidence: [README.md#L426-L430](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L426-L430), [README.md#L432-L434](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L432-L434), [README.md#L436-L441](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L436-L441) (`clm_0d2659750fde538df5d7143adc5b3aed6bfb7122f0f496fc1fbb508b9e641166`)
- [observation/documented] Memories are stored as plain markdown files with a MEMORY.md index that users can edit, and the agent treats user edits as truth; sub-agents never extract memories to avoid recursion. -- evidence: [README.md#L443-L447](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L443-L447), [README.md#L449-L452](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L449-L452) (`clm_886300953789434820012f23e9ebf531b7a208f80f526dafa7d086ccded84ce1`)
- [observation/documented] A per-project wiki stores markdown pages in a shared vault scoped per project, with get/set/list/search/delete actions, and mutating wiki actions are blocked in plan mode and under read-only personas. -- evidence: [README.md#L464-L468](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L464-L468), [README.md#L484-L488](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L484-L488), [README.md#L470-L474](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L470-L474) (`clm_c2a95d8cbae6aa5f551d5fa3228eb60c7c096beeb8b9a552d592b06dce5bdb26`)

## orchestration (1 claim(s))

- [observation/documented] The --orchestrate flag runs each given task as an independent sub-agent process in parallel and collects the results. -- evidence: [README.md#L263-L265](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L263-L265), [README.md#L267-L268](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L267-L268) (`clm_545317dd3eaa1072c408e37c1a38a844c81a14519918735d036f7a7fceef88fc`)

## tools-permissions (1 claim(s))

- [observation/documented] Tool access can be restricted with --tools/--exclude-tools/--no-tools, mutations can be gated behind project trust via --approve, and read-only personas refuse mutating tools. -- evidence: [README.md#L322-L323](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L322-L323), [README.md#L414-L418](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L414-L418) (`clm_fe30cc7c849992853597789d7326ad6dbab30f982ee605925992e62db11ffe63`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The agent supports many LLM providers from one registry — Anthropic, OpenAI/Codex, Google Gemini/Vertex, OpenRouter, Groq, Mistral, Together, Fireworks, DeepSeek, Cerebras, Bedrock, GitHub Copilot, plus local models via Ollama. -- evidence: [README.md#L293-L304](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L293-L304), [README.md#L655-L658](https://github.com/bbarit/bbarit-agent-oss/blob/2cb8b723f2787aa587ef063d366b7cb408ead4aa/README.md#L655-L658) (`clm_2216021a569e5d05ee9360ead06317cddca241b8f08b657b52b1573d8af78ed1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

