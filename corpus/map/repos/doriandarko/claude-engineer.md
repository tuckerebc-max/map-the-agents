# doriandarko/claude-engineer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0a9e4b309bf6 @ b3e0ef2d65aadd78

## Summary (orientation draft, not independently verified)

Claude Engineer v3 is a self-improving Claude 3.5 assistant framework shipped as a CLI (ce3.py) and Flask web UI (app.py), with dynamic tool creation, built-in tools, and documented configuration and API-key requirements. All prior claims were supported except the API-key claim, which is corrected with the .env citation.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Configuration options include MODEL (Claude 3.5 Sonnet), MAX_TOKENS, MAX_CONVERSATION_TOKENS, TOOLS_DIR, SHOW_TOOL_USAGE, ENABLE_THINKING, and DEFAULT_TEMPERATURE. -- evidence: [readme.md#L185-L192](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L185-L192)
- components (4 claim(s)):
  - [observation/documented] The project structure includes app.py (web server), ce3.py (CLI), config.py, static assets, templates, a tools directory with base.py, and prompts/system_prompts.py. -- evidence: [readme.md#L135-L149](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L135-L149)
  - [observation/documented] Built-in tools include a Tool Creator, UV package manager interface, E2B sandboxed Python code executor, Ruff linting tool, and screenshot capture. -- evidence: [readme.md#L213-L213](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L213-L213), [readme.md#L216-L218](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L216-L218), [readme.md#L233-L233](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L233-L233)
- design-choices (1 claim(s)):
  - [observation/documented] The assistant is designed to autonomously identify, create, and load new tools during conversations, expanding its capabilities over time. -- evidence: [readme.md#L111-L116](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L111-L116), [readme.md#L16-L16](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L16-L16)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcome via pull request, and major changes should be preceded by opening an issue for discussion. -- evidence: [readme.md#L201-L201](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L201-L201)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product ships as both a CLI (ce3.py) and a web interface (app.py), with the web UI served at localhost:5000. -- evidence: [readme.md#L37-L37](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L37-L37), [readme.md#L40-L41](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L40-L41), [readme.md#L85-L86](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L85-L86), [readme.md#L3-L3](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L3-L3)
  - [observation/documented] The web UI offers image upload and analysis with Claude Vision, token usage visualization, markdown rendering with syntax highlighting, and Ctrl/Cmd+Enter to send. -- evidence: [readme.md#L66-L72](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L66-L72), [readme.md#L154-L161](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L154-L161)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] requirements.txt pins flask 3.0.0 and requires anthropic, rich, beautifulsoup4, pyautogui, pillow, matplotlib, requests, and other packages. -- evidence: [requirements.txt#L1-L15](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/requirements.txt#L1-L15)
  - [observation/documented] The product requires an Anthropic API key for Claude 3.5 access and an E2B API key for Python code execution, both to be added to a .env file. -- evidence: [readme.md#L248-L248](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L248-L248), [readme.md#L245-L246](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L245-L246), [readme.md#L250-L253](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L250-L253)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](claude-engineer.detail.md) for every claim.)

Metadata and full claim list: [full detail](claude-engineer.detail.md)
Human notes ([notes](claude-engineer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
