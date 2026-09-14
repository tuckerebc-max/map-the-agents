# zhangliang605/carrycode -- full detail

[Back to orientation](carrycode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhangliang605/carrycode/090431f9651fdf4bec87ee4b7a028364e031b725/53270305d1f756d7.json](../../../wiki/dossiers/zhangliang605/carrycode/090431f9651fdf4bec87ee4b7a028364e031b725/53270305d1f756d7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Configuration lives in ~/.carry/carrycode.json (provider credentials and preferences) and ~/.carry/carrycode-runtime.json (language, default model, theme), with paths overridable via CARRYCODE_CONFIG_DIR or CARRYCODE_CONFIG_FILE. -- evidence: [README.md#L219-L223](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L219-L223), [README.md#L225-L225](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L225-L225) (`clm_7d53701a6d132e62b613ac61019043fd7eaf1e53ba44011f4173e5569a744fa8`)

## design-choices (1 claim(s))

- [observation/documented] The agent has two modes: Build mode for autonomous code generation and editing, and Plan mode for read-only analysis and planning. -- evidence: [README.md#L46-L62](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L46-L62) (`clm_957eff14639612055eec2b7dae5abd8b72536091402abe4710733f72ff4eecdf`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: building from source requires Rust (latest stable), Node.js v18+, Bun, and OS build tools; contributors use bun install, bun run build (or build:rust / build:ts), bun run dev, and bun run clean, producing ./target/index.js and a native Rust .node module. -- evidence: [README.md#L130-L130](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L130-L130), [README.md#L118-L124](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L118-L124), [README.md#L140-L141](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L140-L141), [README.md#L133-L133](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L133-L133), [README.md#L145-L147](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L145-L147), [README.md#L136-L137](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L136-L137), [README.md#L158-L161](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L158-L161) (`clm_efe0243de2a0ea55c4b7ff9c9aebd8c86305fe36996710f3d72af2932780c7e4`)
- [observation/documented] Repository development practice: the recommended install path is a one-line script (curl ... install.sh | sudo sh on macOS/Linux, irm ... install.ps1 | iex on Windows) that auto-detects the platform, downloads the binary, verifies the checksum, and installs to /usr/local/bin. -- evidence: [README.md#L73-L74](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L73-L74), [README.md#L76-L76](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L76-L76), [README.md#L70-L70](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L70-L70) (`clm_a36e2d4be2da291629dc9e81a69ab4acce515a0d11f1d683b314d8557dc53d05`)

## skills-patterns (1 claim(s))

- [observation/documented] A skills system loads predefined or custom skills compatible with Claude Code, managed via /skill, with SkillHub integration to search Tencent SkillHub and install skills directly from results. -- evidence: [README.md#L25-L25](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L25-L25), [README.md#L46-L62](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L46-L62) (`clm_8ae0274b1398e1497749f21cc35f259d15071db1910ee73006f3383bd987a164`)

## interfaces (3 claim(s))

- [observation/documented] The CLI is invoked as 'carry'; it offers an interactive terminal UI mode plus a single-shot mode via 'carry --once "..."' with an optional --timeout-ms flag, suited to scripting and CI. -- evidence: [README.md#L96-L98](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L96-L98), [README.md#L107-L107](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L107-L107), [README.md#L109-L112](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L109-L112) (`clm_ab146d466495b00cc7b6bff0da3a555f3f2a413055f15509f33be8df5d47bc7a`)
- [observation/documented] The interactive UI exposes slash commands including /model, /mcp, /skill, /rule, /theme, /language, /approval, /session, /compact, /update, and /exit. -- evidence: [README.md#L167-L179](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L167-L179) (`clm_ad3595bbb1aef052f181189610b6e247c7eccae39abfab793dbe954a7ee0961c`)
- [observation/documented] API keys can be supplied via environment variables such as OPENAI_API_KEY, ANTHROPIC_API_KEY, and GEMINI_API_KEY, or configured through the first-launch setup wizard or /model add. -- evidence: [README.md#L215-L215](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L215-L215), [README.md#L207-L207](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L207-L207), [README.md#L209-L213](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L209-L213) (`clm_9d14e772aab1a0bd4bd06cc61f1c19cc2e6c19eb09b8fc176821e91d47c08daf`)

## memory-state (1 claim(s))

- [observation/documented] Sessions can be created, switched, and resumed with context persisting across conversations, and /compact compresses the current session context; long conversations are automatically compressed to fit token limits. -- evidence: [README.md#L167-L179](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L167-L179), [README_CN.md#L44-L60](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README_CN.md#L44-L60) (`clm_0c469a46e3e9bc2ad55737e2ab922bfacca204b9b52bb2a920a21a7d9021e6bc`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Approval modes control the agent's permissions at runtime: read-only, agent (read/write plus execution), and agent-full (unrestricted), selectable via /approval. -- evidence: [README.md#L167-L179](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L167-L179), [README_CN.md#L44-L60](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README_CN.md#L44-L60) (`clm_9f6a4043b3f9a946358eb5db34b5ce2a05ccbb67ce076e8534ad90ffc7018ed9`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product advertises support for 17+ LLM providers and 240+ models, including OpenAI, Anthropic, Google Gemini, DeepSeek, Kimi, GLM, MiniMax, Qwen, xAI Grok, Ollama, vLLM, and any OpenAI-compatible endpoint. -- evidence: [README.md#L25-L25](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L25-L25), [README.md#L46-L62](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L46-L62), [README.md#L185-L199](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L185-L199) (`clm_6fad38bfb1e474a106f22458f19c3142180fbc2914d0600ddd5f4f9aceab29fb`)

## limitations (1 claim(s))

- [inference/documented] The usage terms prohibit modifying the project's Logo, Banner, or identifying marks when modifying or commercially using the source, directing such requests to us@carrycode.ai; this appears to be a branding restriction rather than a functional limitation. -- evidence: [README.md#L234-L236](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L234-L236) (`clm_b878108a92c74978bc712e231f592268223156cb3ae949f298dff036209c6709`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

