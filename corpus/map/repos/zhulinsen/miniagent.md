# zhulinsen/miniagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 657909f0237b @ a1b4aca7057c5eab

## Summary (orientation draft, not independently verified)

Evidence consists of bilingual READMEs plus contributor guides (AGENTS.md, CONTRIBUTING.md) and requirements.txt for MiniAgent, a minimalist CLI agent framework with a single-file core, dual tool-calling modes, skills, MCP support, and orchestration. Product claims are documentation-based; contributor instructions are recorded only as development practice.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] MiniAgent is documented as a minimalist, transparent CLI agent framework whose core engine is a single agent.py file, positioned as an educational 'AI Agent textbook'. -- evidence: [README.md#L17-L17](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L17-L17), [README_EN.md#L17-L17](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L17-L17), [README.md#L42-L42](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L42-L42), [README_EN.md#L42-L42](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L42-L42)
- components (2 claim(s)):
  - [observation/documented] The documented project layout includes agent.py (LLM loop, tool calling, context management), cli.py (Rich streaming CLI), tools/ (code_tools.py, basic_tools.py), extensions/ (mcp_client.py, orchestrator.py), skills.py, config.py, memory.py, and utils/. -- evidence: [README_EN.md#L182-L200](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L182-L200), [README.md#L184-L202](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L184-L202)
  - [observation/documented] Documented built-in tools include code tools (read, write, edit, grep, glob, bash with timeout), OS tools (open_browser, open_app, create_docx, clipboard), system tools (system_info, process_list, env_get/set), and misc tools (calculator with AST-safe evaluation, web_search, http_request). -- evidence: [README_EN.md#L155-L178](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L155-L178), [README.md#L157-L180](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L157-L180)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors must not push directly to main; changes go through pull requests requiring at least one maintainer review, with Conventional Commits message format and tests required for core-logic changes. -- evidence: [AGENTS.md#L140-L143](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L140-L143)
  - [observation/documented] Repository development practice: tests are run with pytest (e.g. 'uv run pytest tests/ -v'), the suite reportedly covers 100+ cases, and code should follow PEP 8 with type annotations and docstrings. -- evidence: [AGENTS.md#L136-L136](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L136-L136), [CONTRIBUTING.md#L107-L108](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L107-L108), [CONTRIBUTING.md#L54-L57](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L54-L57), [AGENTS.md#L132-L134](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L132-L134), [CONTRIBUTING.md#L112-L112](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/CONTRIBUTING.md#L112-L112)
- skills-patterns (1 claim(s)):
  - [observation/documented] A Skill system provides reusable agent configurations combining prompt, tool whitelist, and parameters, with four built-in roles (coder, researcher, reviewer, tester) and a register_skill API for custom skills. -- evidence: [README_EN.md#L246-L246](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L246-L246), [README.md#L259-L265](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L259-L265), [README_EN.md#L257-L263](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L257-L263), [README.md#L19-L29](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L19-L29), [README.md#L248-L248](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L248-L248)
- interfaces (3 claim(s)):
  - [observation/documented] The product supports two tool-calling modes: a default text-parsing mode where the LLM emits structured text like 'TOOL: bash / ARGS: {...}', and a native OpenAI function-calling mode enabled via mode="native" that supports parallel tool calls. -- evidence: [AGENTS.md#L107-L108](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L107-L108), [README.md#L209-L212](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L209-L212), [AGENTS.md#L100-L104](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/AGENTS.md#L100-L104), [README_EN.md#L213-L216](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L213-L216), [README_EN.md#L207-L210](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README_EN.md#L207-L210), [README.md#L215-L218](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L215-L218)
  - [observation/documented] The CLI is launched via 'miniagent' or 'python -m miniagent', and configuration is done through a .env file with variables such as LLM_API_KEY, LLM_MODEL, and LLM_API_BASE; Gemini is supported via Google's OpenAI-compatible endpoint. -- evidence: [README.md#L105-L107](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L105-L107), [README.md#L95-L95](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L95-L95), [README.md#L97-L101](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L97-L101), [README.md#L111-L113](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L111-L113), [README.md#L89-L93](https://github.com/ZhuLinsen/MiniAgent/blob/657909f0237b66293fd7194934c800c6922157d0/README.md#L89-L93)
- memory-state (1 claim(s)):
More evidence: [full detail](miniagent.detail.md)

Metadata and full claim list: [full detail](miniagent.detail.md)
Human notes ([notes](miniagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
