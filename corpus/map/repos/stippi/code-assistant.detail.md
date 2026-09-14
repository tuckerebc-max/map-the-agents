# stippi/code-assistant -- full detail

[Back to orientation](code-assistant.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stippi/code-assistant/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/114d3c2ae22361f3.json](../../../wiki/dossiers/stippi/code-assistant/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/114d3c2ae22361f3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The GUI is built on Zed's GPUI framework; the codebase is organized into crates including llm, code_assistant, and web, with the web crate already owning chromiumoxide for browser automation. -- evidence: [docs/context-compaction.md#L41-L44](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/context-compaction.md#L41-L44), [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/browser-agency-plan.md#L67-L70](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/browser-agency-plan.md#L67-L70) (`clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46`)

## design-choices (3 claim(s))

- [observation/documented] Tool-invocation syntax is adaptive per session: native function calling, XML tags, or triple-caret blocks, selectable via --tool-syntax native|xml|caret. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/configuration.md#L187-L190](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L187-L190) (`clm_69ccefc9b543fd9ad05673960e50d3124e920fd39a1306278275642cd46c9991`)
- [observation/documented] Format-on-save runs project formatters after the assistant modifies matching files and updates tool parameters to reflect formatted content, keeping the model's view in sync without re-reading files; mappings pair glob patterns with shell commands. -- evidence: [docs/configuration.md#L144-L150](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L144-L150), [README.md#L60-L75](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L60-L75) (`clm_d2749f1e3e19ac4df142a4651e444d318f2bb4f3e27339876e84b5c61ed59442`)
- [observation/documented] File handling preserves each file's stored encoding, BOM, and CRLF/LF line endings, giving the model clean text while writing the file back in its original form. -- evidence: [README.md#L60-L75](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L60-L75) (`clm_572249c81f94a4a534489e23ea2c816840df19ec8c406752f051eb060cd4571d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source requires the Rust toolchain via rustup, specific Linux system libraries for gpui, the Metal toolchain on macOS, and 'cargo build --release'; browser-agency work followed a TDD/checkpoint style where each step compiles, is tested, and is committable on its own. -- evidence: [README.md#L36-L39](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L36-L39), [README.md#L33-L33](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L33-L33), [README.md#L42-L42](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L42-L42), [README.md#L45-L48](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L45-L48), [docs/browser-agency-plan.md#L192-L193](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/browser-agency-plan.md#L192-L193) (`clm_00653a1b3c00132caeae35cfac4b7d5792c44044eaf116ea5a6bf552424bea7d`)

## skills-patterns (1 claim(s))

- [observation/documented] The agent supports reusable, task-specific skills (playbooks) loadable on demand, and auto-loads AGENTS.md or CLAUDE.md from the project root as repo-specific guidance. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98) (`clm_02aa47e3613ad22b1d6ca8cd72f6363cf9367bc16c6e8d8138488fc19c1b1295`)

## interfaces (4 claim(s))

- [observation/documented] The binary offers four interface modes: a native GUI by default, a terminal mode via --tui, an ACP agent via 'acp' for editors like Zed, and a headless MCP server via 'server'. -- evidence: [README.md#L102-L107](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L102-L107) (`clm_8b8f808790a1442b03d1aa98d38db6147fa7a3d048eb6a0dcf78f1c43571b8c3`)
- [observation/documented] Any mode can accept an initial task via a --task flag, e.g. asking it to explain the codebase. -- evidence: [README.md#L109-L109](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L109-L109) (`clm_208fd78d53f2f3422bb3381a68eb5b1d88de69c2fbe91b5e417310d9f64f1c27`)
- [observation/documented] Zed integration registers the binary as an agent_servers entry with 'acp' args and an API key env var; Claude Desktop integration uses the 'server' subcommand in an mcpServers entry. -- evidence: [README.md#L137-L147](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L137-L147), [README.md#L116-L126](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L116-L126) (`clm_6ede4fe863ae2deef43e9d0cced88c516de3ff4596a9508056c12ea6876dc19d`)
- [observation/documented] CLI flags include --list-models/--list-providers, --model, --task, --continue-task, --use-diff-format, --record/--playback session recording, and --verbose logging. -- evidence: [docs/configuration.md#L207-L216](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L207-L216), [docs/configuration.md#L91-L94](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L91-L94), [docs/configuration.md#L197-L200](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L197-L200) (`clm_dc9a3463ac96a3c82fa1e35d26f3a8082d6c96c50f732c7aeeb15d9478b72224`)

## memory-state (2 claim(s))

- [observation/documented] Sessions are per project with branching and persistent state; each chat session is permanently tied to its initial project/folder and tool syntax, which cannot be changed later. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/configuration.md#L133-L140](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L133-L140) (`clm_5d938e80747f10f9652a61c96c58e43f2202b09ef821f23d4e3110cd61509d20`)
- [observation/documented] Automatic context compaction was implemented: when prior assistant usage crosses the configured context-window threshold, a summary request is injected and the result is persisted as a user message tagged is_compaction_summary, with a collapsible UI banner. -- evidence: [docs/context-compaction.md#L41-L44](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/context-compaction.md#L41-L44) (`clm_5a63018ea5d561f99872f9d0ecac565cb1ee7447b76cffaf69283288a55d7e55`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The product includes permission tiers and a command sandbox; --sandbox-mode offers danger-full-access (the default), read-only, and workspace-write, with --sandbox-network allowing outbound network access in workspace-write mode. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/configuration.md#L207-L216](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L207-L216) (`clm_0acfa49b0bd88396a9b621ab725f2943a7a55a2d83685f76f7d0c3ffd52204b3`)
- [observation/documented] Browser actions are tagged by capability: navigation, screenshots, and reads are read_only, while submit-style actions with external effect are outward and gated by the existing permission tiers with no new mechanism. -- evidence: [docs/browser-agency-plan.md#L47-L61](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/browser-agency-plan.md#L47-L61) (`clm_84dacb23bfbc06e56b2a43af5f7f2e0ed13302b9deb50f50d711173ce4ef5e68`)

## evaluation (1 claim(s))

- [inference/documented] No agent-performance benchmark or eval harness appears in the provided slices; the only test-related evidence is unit/integration test coverage for features, which is development practice rather than agent evaluation. -- evidence: [docs/context-compaction.md#L46-L46](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/context-compaction.md#L46-L46) (`clm_20c179e47db9836b54d2dc79d876bf1609cc2d97865a0bdb461879958c018297`)

## dependencies (1 claim(s))

- [observation/documented] Multiple LLM providers are supported, including Anthropic, OpenAI, Google Vertex AI, Ollama, OpenRouter, SAP AI Core, Groq, Cerebras, and Mistral, configured via providers.json and models.json with example files for each. -- evidence: [README.md#L79-L98](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L79-L98), [docs/configuration.md#L84-L87](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/configuration.md#L84-L87) (`clm_2f014212af75a9cadb059ebea58098da837e3b697fff680b27c768d436886288`)

## limitations (1 claim(s))

- [observation/documented] browser_act ships as a normal write tool because capability tags are static per tool; in the default bypass-all tier it runs freely, and embedders wanting gated consequential actions add the outward tag via the extra-capabilities hook. browser_login always prompts regardless of tier. -- evidence: [docs/browser-agency-plan.md#L229-L236](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/docs/browser-agency-plan.md#L229-L236) (`clm_5623a75280fb7e9f4933641565fa609999381d70ea48def4c9b29226ebae3abd`)

## relevance (1 claim(s))

- [observation/documented] The project is an open-source Rust AI coding agent that runs an autonomous agent loop over a codebase — reading, searching, editing files, and running commands — while keeping the user informed of what it is doing. -- evidence: [README.md#L7-L10](https://github.com/stippi/code-assistant/blob/ba818a46c472bdd6e9b03fa3a5ca608fdc141e9b/README.md#L7-L10) (`clm_2f0e78da1fc0bfc41ed1620976549fe283a7d788ec79775052d263b8140456a4`)

