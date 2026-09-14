# gptme/gptme -- full detail

[Back to orientation](gptme.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gptme/gptme/7c8570587edca8a819777ba660f67ef2f3878cb5/5a6e65dab4305226.json](../../../wiki/dossiers/gptme/gptme/7c8570587edca8a819777ba660f67ef2f3878cb5/5a6e65dab4305226.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Built-in tools documented include shell, ipython, read, save/append, patch/morph, browser (Playwright), vision, screenshot, rag, gh, tmux, computer, subagent, and chats. -- evidence: [README.md#L275-L290](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L275-L290) (`clm_a23780e490e14f19c4cd358ac9c8329ace54adb27cfbf6ed0a7868dc6b7960bc`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README says contributions are welcome and points contributors to the contributing guide at gptme.org/docs/contributing.html; it also notes the codebase is checked and formatted with mypy, ruff, and pyupgrade. -- evidence: [README.md#L422-L433](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L422-L433), [README.md#L657-L657](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L657-L657) (`clm_d7b610b520ad8c3848d15aee992984caf97f1aec4ef57a24ac802c8804bf716f`)

## skills-patterns (1 claim(s))

- [observation/documented] Extensibility layers include Python-package plugins configured in gptme.toml, Anthropic-format skills that auto-load when named, keyword/pattern-matched lessons injected into conversations, and lifecycle hooks. -- evidence: [README.md#L302-L305](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L302-L305), [README.md#L311-L311](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L311-L311), [README.md#L307-L307](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L307-L307), [README.md#L298-L298](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L298-L298), [README.md#L309-L309](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L309-L309) (`clm_ef24c26595d1e9f762dcaed6f6ef7c80db6f5706db7108847f51a1d98291f34f`)

## interfaces (5 claim(s))

- [observation/documented] gptme is a chat-CLI for LLMs; prompts can be passed as arguments and chained with a '-' separator, and the interface exposes user commands like /undo, /log, /model, /tools, and /export. -- evidence: [README.md#L547-L549](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L547-L549), [README.md#L554-L555](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L554-L555), [README.md#L560-L580](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L560-L580), [README.md#L551-L552](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L551-L552) (`clm_06f85b571f71704697f3057e8dac076f4b59693cc73d3df97f8db4caacaa5c90`)
- [observation/documented] CLI options include --model, --workspace, --resume, --no-confirm (-y), --non-interactive (-n), --output-format text|json, --system, and a --tools flag restricting tools to a comma-separated allowlist. -- evidence: [README.md#L588-L615](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L588-L615) (`clm_afb8418de9a18c821434eaf870a492d72a40b26c8cac29d0672ce82d6932f70e`)
- [observation/documented] Non-interactive mode with --output-format json emits one JSON object per line on stdout for machine-readable use in CI or supervising processes. -- evidence: [README.md#L518-L519](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L518-L519), [README.md#L617-L620](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L617-L620) (`clm_2ecdabf1d064bf9953fdf56791803544703e140d44cabc354e947f160fdba08a`)
- [observation/documented] gptme works bidirectionally with MCP: as a client it discovers and loads external MCP servers as tools, and as a server (gptme-mcp-server) it exposes shell, Python, and file tools to MCP clients with state preserved across calls. -- evidence: [README.md#L339-L340](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L339-L340), [README.md#L336-L337](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L336-L337), [README.md#L328-L330](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L328-L330), [README.md#L804-L808](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L804-L808) (`clm_fe7cec872a5cce12f964460b261da8bf6d4e6b4b06e58e9f43571c237f6b1a32`)
- [observation/documented] Via the Agent Client Protocol (ACP) extra, gptme can act as a drop-in coding agent in Zed and JetBrains IDEs, executing with its full toolset and streaming results back to the editor. -- evidence: [README.md#L348-L348](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L348-L348), [README.md#L342-L342](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L342-L342) (`clm_27100d8782b57502b925fb39d87f11290a850997efae4497b8c69b7c37f4e1c1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] gptme service init scaffolds a self-contained headless agent: a systemd service unit, optional timer (hourly/daily/weekly/on-demand), a startup script running one non-interactive session per trigger, prompt.md, and config skeletons. -- evidence: [README.md#L391-L391](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L391-L391), [README.md#L384-L389](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L384-L389), [README.md#L374-L374](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L374-L374) (`clm_64da5b32418af0b58c78f7f95169943cec19833ca4f846b15b17c3b070f086d2`)
- [observation/documented] The gptme-agent-template supports persistent autonomous agents with a git-tracked workspace, run loops, task queues, multi-agent coordination via file leases and a message bus, and external integrations like GitHub and Discord. -- evidence: [README.md#L352-L352](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L352-L352), [README.md#L354-L359](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L354-L359) (`clm_38265c4f86bd3e9f20fdc60698b51710cd369ec0b7da529e0dd6fe60c6e283e1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README advertises an evaluation suite for testing capabilities of different models, with advanced frontier-capability evals listed as in progress. -- evidence: [README.md#L437-L441](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L437-L441), [README.md#L422-L433](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L422-L433) (`clm_a4bb7762d27e5b264998c3d7b05c5625fa5cd8eaf94234f68d94d053ec5ff626`)

## dependencies (2 claim(s))

- [observation/documented] Requires Python 3.10 or newer and credentials for at least one LLM provider; local llama.cpp models need no API key, and OpenRouter offers a no-credit-card free-model path. -- evidence: [README.md#L447-L461](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L447-L461) (`clm_adb3136b27261a0d2c5076a7883bf727d0db5d721cd41d918b33ba520eda3096`)
- [observation/documented] Documented provider support covers Anthropic, OpenAI, Google, xAI, DeepSeek, OpenRouter, and local llama.cpp servers, configured via per-provider API keys or an OpenAI-compatible base URL. -- evidence: [README.md#L761-L769](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L761-L769), [README.md#L780-L784](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L780-L784) (`clm_80ef585ff87afec9811fb4467069eb6be1c0d9ce71033f5509d5370f0831efea`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

