# zhulinsen/miniagent -- full detail

[Back to orientation](miniagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhulinsen/miniagent/657909f0237b66293fd7194934c800c6922157d0/a1b4aca7057c5eab.json](../../../wiki/dossiers/zhulinsen/miniagent/657909f0237b66293fd7194934c800c6922157d0/a1b4aca7057c5eab.json)

## specifications (1 claim(s))

- [observation/documented] MiniAgent is documented as a minimalist, transparent CLI agent framework whose core engine is a single agent.py file, positioned as an educational 'AI Agent textbook'. -- evidence: [README.md#L17-L17](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L17-L17), [README_EN.md#L17-L17](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L17-L17), [README.md#L42-L42](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L42-L42), [README_EN.md#L42-L42](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L42-L42) (`clm_ee5d1dae846d121ade6a9953a13457815c6a3846eed3aaefdc1896e624667c57`)

## components (2 claim(s))

- [observation/documented] The documented project layout includes agent.py (LLM loop, tool calling, context management), cli.py (Rich streaming CLI), tools/ (code_tools.py, basic_tools.py), extensions/ (mcp_client.py, orchestrator.py), skills.py, config.py, memory.py, and utils/. -- evidence: [README_EN.md#L182-L200](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L182-L200), [README.md#L184-L202](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L184-L202) (`clm_e66f5f68793b89610129a948533260bc1b98c74d809600f6f1f5286618c4f804`)
- [observation/documented] Documented built-in tools include code tools (read, write, edit, grep, glob, bash with timeout), OS tools (open_browser, open_app, create_docx, clipboard), system tools (system_info, process_list, env_get/set), and misc tools (calculator with AST-safe evaluation, web_search, http_request). -- evidence: [README_EN.md#L155-L178](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L155-L178), [README.md#L157-L180](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L157-L180) (`clm_9c4deee429f5663cb829ff592f10d4f4dfc7b16fbca63e1d292acfba05a4fba9`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors must not push directly to main; changes go through pull requests requiring at least one maintainer review, with Conventional Commits message format and tests required for core-logic changes. -- evidence: [AGENTS.md#L140-L143](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L140-L143) (`clm_a18b21d91126976578eb09bc6196cb0ed5b28be28d29c638830818e8b3ec78c2`)
- [observation/documented] Repository development practice: tests are run with pytest (e.g. 'uv run pytest tests/ -v'), the suite reportedly covers 100+ cases, and code should follow PEP 8 with type annotations and docstrings. -- evidence: [AGENTS.md#L136-L136](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L136-L136), [CONTRIBUTING.md#L107-L108](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L107-L108), [CONTRIBUTING.md#L54-L57](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L54-L57), [AGENTS.md#L132-L134](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L132-L134), [CONTRIBUTING.md#L112-L112](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L112-L112) (`clm_7f6e10f32806a3784ce989681c7a0692bc83c198b2450f466e54d51a34369a72`)
- [observation/documented] Repository development practice: the contribution flow is fork-based — fork the repo, create a feature or fix branch from main, push, and open a PR against main with a detailed description. -- evidence: [CONTRIBUTING.md#L88-L93](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L88-L93), [CONTRIBUTING.md#L82-L84](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L82-L84) (`clm_3c413fa2eaad8794d3aaf5c96013715c218a110dc3440d7a5e7dcaf05eef87c8`)

## skills-patterns (1 claim(s))

- [observation/documented] A Skill system provides reusable agent configurations combining prompt, tool whitelist, and parameters, with four built-in roles (coder, researcher, reviewer, tester) and a register_skill API for custom skills. -- evidence: [README_EN.md#L246-L246](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L246-L246), [README.md#L259-L265](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L259-L265), [README_EN.md#L257-L263](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L257-L263), [README.md#L19-L29](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L19-L29), [README.md#L248-L248](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L248-L248) (`clm_535cc2e71452127661a850cf1d1640dc9e05efa99bff640b950eccdeea584422`)

## interfaces (3 claim(s))

- [observation/documented] The product supports two tool-calling modes: a default text-parsing mode where the LLM emits structured text like 'TOOL: bash / ARGS: {...}', and a native OpenAI function-calling mode enabled via mode="native" that supports parallel tool calls. -- evidence: [AGENTS.md#L107-L108](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L107-L108), [README.md#L209-L212](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L209-L212), [AGENTS.md#L100-L104](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L100-L104), [README_EN.md#L213-L216](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L213-L216), [README_EN.md#L207-L210](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L207-L210), [README.md#L215-L218](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L215-L218) (`clm_956863e8798b597f03be73e3bd7b460f80139047798925c3b9fda64bab6c0558`)
- [observation/documented] The CLI is launched via 'miniagent' or 'python -m miniagent', and configuration is done through a .env file with variables such as LLM_API_KEY, LLM_MODEL, and LLM_API_BASE; Gemini is supported via Google's OpenAI-compatible endpoint. -- evidence: [README.md#L105-L107](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L105-L107), [README.md#L95-L95](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L95-L95), [README.md#L97-L101](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L97-L101), [README.md#L111-L113](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L111-L113), [README.md#L89-L93](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L89-L93) (`clm_2ef94f1e8e2bf38ea4a947bde31bcfcbe57f9bc2e72ecb8ecd9b5f827c177097`)
- [observation/documented] The framework exposes MCP protocol support via load_mcp_tools, allowing tools from any MCP server (e.g. the filesystem server) to be added to an agent with agent.add_tool. -- evidence: [README.md#L230-L232](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L230-L232), [README_EN.md#L228-L230](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L228-L230), [README.md#L222-L222](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L222-L222), [README_EN.md#L220-L220](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L220-L220) (`clm_4ee3552cabf3d003d5cb8de21ac92cd55e1ec9d8e062d648a6fa604c96074a4f`)

## memory-state (1 claim(s))

- [observation/documented] The product includes lightweight session memory stored at ~/.miniagent/memory.json (path configurable via MINIAGENT_HOME) and auto-compresses conversation history beyond a configurable message limit. -- evidence: [README.md#L184-L202](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L184-L202), [AGENTS.md#L149-L166](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L149-L166), [AGENTS.md#L40-L81](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L40-L81) (`clm_b464f1fa2c3cfd05d47aa83b4ef7468398022a3f92de310aaf1fbf6ef944c089`)

## orchestration (1 claim(s))

- [observation/documented] A built-in Orchestrator decomposes complex tasks and assigns them to specialized workers driven by the Skill system, e.g. planning researcher → coder → tester for a research-and-code task. -- evidence: [README_EN.md#L234-L234](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L234-L234), [README.md#L241-L242](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L241-L242), [README.md#L244-L244](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L244-L244), [README.md#L236-L236](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L236-L236), [README_EN.md#L239-L240](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L239-L240) (`clm_5cc5bd7684040e0404a8d624779ad5eab4c72aea4e9ca65dd2152bc8929384e4`)

## tools-permissions (1 claim(s))

- [observation/documented] The runtime includes a safety guard that auto-detects dangerous bash commands and requires confirmation before execution, controlled by a CONFIRM_DANGEROUS setting documented as defaulting to true. -- evidence: [README_EN.md#L19-L29](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L19-L29), [AGENTS.md#L149-L166](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L149-L166), [README.md#L19-L29](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L19-L29) (`clm_b7aab3587b646437cde5f4be0b80fd71e435546d136c3a230d4cc0ce8a00f289`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt lists seven runtime dependencies: openai, requests, python-dotenv, tenacity, psutil, distro, and rich; python-docx is an optional extra for Word document support. -- evidence: [README_EN.md#L117-L118](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L117-L118), [requirements.txt#L1-L7](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/requirements.txt#L1-L7), [README.md#L117-L118](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L117-L118) (`clm_8510a54d07b2349ffc1fe40f3282abf07e56717b6c23fa9d0d8a6ef3d3b5f3e7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

