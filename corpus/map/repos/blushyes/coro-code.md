# blushyes/coro-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 679c57af5376 @ d60a9546779f7cea

## Summary (orientation draft, not independently verified)

Coro Code is a Rust-based AI coding agent with a terminal UI, installable via cargo, configurable through environment variables or a JSON file, with OpenAI support ready and Anthropic/Google pending; it ships context persistence APIs and documents contributor pre-commit hooks.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Coro Code is described as a high-performance AI coding agent written in Rust with a rich terminal UI, formerly named Trae Agent Rust and kept compatible with the original tool spec. -- evidence: [README.md#L18-L18](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L18-L18)
- components (1 claim(s)):
  - [observation/documented] The Chinese README lists built-in tools including bash, edit, json_edit, thinking, task_done, ckg, and mcp, plus Git-aware file search using @path syntax. -- evidence: [README_zh.md#L22-L26](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README_zh.md#L22-L26)
- design-choices (1 claim(s)):
  - [observation/documented] Config loading follows a unified priority of CLI arguments over environment variables over JSON file, marked completed in the roadmap; token compression (intelligent context compression with adaptive context windows) is also marked completed. -- evidence: [README.md#L159-L164](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L159-L164), [README.md#L136-L140](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L136-L140)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are strongly recommended to install pre-commit hooks via platform-specific scripts; the hooks run cargo fmt --check, cargo clippy, and cargo test before each commit, and the contribution flow is fork, branch, change, test, PR. -- evidence: [README.md#L246-L251](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L246-L251), [README.md#L221-L221](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L221-L221), [README.md#L238-L240](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L238-L240), [README.md#L227-L227](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L227-L227)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI binary is named `coro`; it can run in interactive mode or accept a single task as a direct argument, and supports a `--config` flag pointing to a custom JSON config file. -- evidence: [README.md#L98-L99](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L98-L99), [README.md#L49-L50](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L49-L50), [README.md#L46-L46](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L46-L46)
  - [observation/documented] Configuration can be supplied via environment variables (OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL, and generic CORO_BASE_URL/CORO_MODEL overrides) or a `coro.json` file specifying protocol, base_url, api_key, model, and sampling params such as max_tokens, temperature, and top_p. -- evidence: [README.md#L58-L59](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L58-L59), [README.md#L74-L86](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L74-L86), [README.md#L72-L72](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L72-L72), [README.md#L66-L68](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L66-L68), [README.md#L62-L63](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L62-L63)
- memory-state (2 claim(s)):
  - [observation/documented] The core library supports exporting conversation and execution context to JSON (as a string, a file such as .coro/context.json, or a structured snapshot) and restoring it later via agent APIs like export_context_json and restore_context_from_file, exposed through coro_core::agent. -- evidence: [README.md#L206-L211](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L206-L211), [README.md#L198-L200](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L198-L200), [README.md#L195-L196](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L195-L196), [README.md#L193-L193](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L193-L193), [README.md#L202-L204](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L202-L204)
  - [observation/documented] The persistence snapshot contains conversation_history, AgentExecutionContext, and optional AgentConfig; on restore the saved config is applied, unpaired tool results are handled automatically, and system prompts are re-injected by the agent as needed. -- evidence: [README.md#L215-L217](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L215-L217)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](coro-code.detail.md)

Metadata and full claim list: [full detail](coro-code.detail.md)
Human notes ([notes](coro-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
