# doriandarko/deepseek-engineer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9aa7a2d3611b @ 2653c09f24d1c2cb

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is an interactive terminal coding assistant integrating DeepSeek reasoning models, offering file operations, code analysis, and assistance via natural conversation and function calling. An /add command lets users preload a single file or an entire directory (with smart filtering) into conversation context, complementing the AI's automatic file reading.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [inference/documented] The rich and prompt_toolkit dependencies suggest the color-coded, streaming terminal UI described in the README is likely built on those libraries. -- evidence: [README.md#L67-L70](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L67-L70), [requirements.txt#L1-L5](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/requirements.txt#L1-L5)
- design-choices (2 claim(s)):
  - [observation/documented] Version 2.0 replaced structured JSON output with native function calling, citing natural conversation, automatic file operations, visible chain-of-thought reasoning, and better error handling. -- evidence: [README.md#L9-L13](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L9-L13)
  - [observation/documented] The architecture streams three channels (reasoning, content, tool_calls), executes tools in real time during streaming, and automatically follows up after tool completion. -- evidence: [README.md#L181-L184](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L181-L184)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup is via git clone, uv venv/uv sync (or pip install -r requirements.txt), and running deepseek-eng.py with uv run or python3. -- evidence: [README.md#L258-L263](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L258-L263), [README.md#L248-L253](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L248-L253), [README.md#L106-L110](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L106-L110), [README.md#L100-L104](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L100-L104), [README.md#L86-L90](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L86-L90)
  - [observation/documented] Repository development practice: the project is described as experimental, showcasing DeepSeek reasoning model capabilities, with contributions welcome. -- evidence: [README.md#L269-L269](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L269-L269), [README.md#L245-L245](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L245-L245)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is an interactive terminal coding assistant integrating DeepSeek reasoning models, offering file operations, code analysis, and assistance via natural conversation and function calling. -- evidence: [README.md#L5-L5](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L5-L5)
  - [observation/documented] An /add command lets users preload a single file or an entire directory (with smart filtering) into conversation context, complementing the AI's automatic file reading. -- evidence: [README.md#L64-L64](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L64-L64), [README.md#L60-L62](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L60-L62)
- memory-state (1 claim(s)):
  - [observation/documented] Context management includes automatic file detection from user messages, conversation cleanup to prevent token overflow, and file content preservation across history. -- evidence: [README.md#L189-L192](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L189-L192)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] requirements.txt lists openai, pydantic, python-dotenv, rich, and prompt_toolkit; the README states Python 3.11+ is required for optimal performance. -- evidence: [requirements.txt#L1-L5](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/requirements.txt#L1-L5), [README.md#L81-L82](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L81-L82)
  - [observation/documented] The tool requires a DeepSeek API key, configured via a DEEPSEEK_API_KEY entry in a .env file. -- evidence: [README.md#L230-L231](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L230-L231), [README.md#L81-L82](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L81-L82), [README.md#L92-L96](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L92-L96)
- limitations (1 claim(s)):
More evidence: [full detail](deepseek-engineer.detail.md)

Metadata and full claim list: [full detail](deepseek-engineer.detail.md)
Human notes ([notes](deepseek-engineer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
