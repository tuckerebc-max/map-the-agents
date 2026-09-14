# doriandarko/claude-engineer -- full detail

[Back to orientation](claude-engineer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/doriandarko/claude-engineer/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/b3e0ef2d65aadd78.json](../../../wiki/dossiers/doriandarko/claude-engineer/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/b3e0ef2d65aadd78.json)

## specifications (1 claim(s))

- [observation/documented] Configuration options include MODEL (Claude 3.5 Sonnet), MAX_TOKENS, MAX_CONVERSATION_TOKENS, TOOLS_DIR, SHOW_TOOL_USAGE, ENABLE_THINKING, and DEFAULT_TEMPERATURE. -- evidence: [readme.md#L185-L192](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L185-L192) (`clm_2319d1fd14b66c34b9302001f52bd1219aca64a72dab7c1de387525e70aff314`)

## components (4 claim(s))

- [observation/documented] The project structure includes app.py (web server), ce3.py (CLI), config.py, static assets, templates, a tools directory with base.py, and prompts/system_prompts.py. -- evidence: [readme.md#L135-L149](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L135-L149) (`clm_ea1da9db7df52b73e3471fb01086e11a94514a76feafd9d105e5f9bfeccfb100`)
- [observation/documented] Built-in tools include a Tool Creator, UV package manager interface, E2B sandboxed Python code executor, Ruff linting tool, and screenshot capture. -- evidence: [readme.md#L213-L213](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L213-L213), [readme.md#L216-L218](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L216-L218), [readme.md#L233-L233](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L233-L233) (`clm_326ba75f4c2d650f9a14d12528e329ebce22fa888ab615c3620973be70b65865`)
- [observation/documented] File-system tools cover creating folders and files, reading multiple files with binary filtering, full and partial file editing, and exact-substring diff edits. -- evidence: [readme.md#L221-L225](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L221-L225) (`clm_aa3198ae43dba18a4e413364f4a0e03a1e495964c944969222645a855107332b`)
- [observation/documented] Web tools include DuckDuckGo search, a readable-content web scraper, and a browser tool that opens URLs in the system default browser. -- evidence: [readme.md#L228-L230](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L228-L230) (`clm_646c84e53ea0cc71b888694967a45d4ee94d005c1f70994ec3e9bce7e4bbfca7`)

## design-choices (1 claim(s))

- [observation/documented] The assistant is designed to autonomously identify, create, and load new tools during conversations, expanding its capabilities over time. -- evidence: [readme.md#L111-L116](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L111-L116), [readme.md#L16-L16](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L16-L16) (`clm_5b285c118842e0e5d9a944e0eab137eeaa0afa0a749fba2d3677612a7b0f38cb`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcome via pull request, and major changes should be preceded by opening an issue for discussion. -- evidence: [readme.md#L201-L201](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L201-L201) (`clm_054a20b9fae8aa6dca9431d7e2c1499f2ddacf7fdde596d6d5b2a05e175c2cb9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product ships as both a CLI (ce3.py) and a web interface (app.py), with the web UI served at localhost:5000. -- evidence: [readme.md#L37-L37](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L37-L37), [readme.md#L40-L41](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L40-L41), [readme.md#L85-L86](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L85-L86), [readme.md#L3-L3](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L3-L3) (`clm_94fbaace38e9b56875c326a0c28726c91bad28ac414916526974738d6bd9713f`)
- [observation/documented] The web UI offers image upload and analysis with Claude Vision, token usage visualization, markdown rendering with syntax highlighting, and Ctrl/Cmd+Enter to send. -- evidence: [readme.md#L66-L72](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L66-L72), [readme.md#L154-L161](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L154-L161) (`clm_48effc2c8a4463ef70dcc655590b4f900fb3261611a31cdade4d7f5200e7a632`)
- [observation/documented] The CLI provides rich text formatting, an ASCII token usage bar, live progress indicators, direct tool interaction, and detailed debugging output. -- evidence: [readme.md#L164-L169](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L164-L169), [readme.md#L89-L94](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L89-L94) (`clm_459fd66c6b6d68da4d6da66260951581967416309e290eed2f332ff22dd2ae5a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt pins flask 3.0.0 and requires anthropic, rich, beautifulsoup4, pyautogui, pillow, matplotlib, requests, and other packages. -- evidence: [requirements.txt#L1-L15](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/requirements.txt#L1-L15) (`clm_0d38f1b65f7654ba4d8db8bda1921794bf84d18bad23d0039dd4177f04c09de0`)
- [observation/documented] The product requires an Anthropic API key for Claude 3.5 access and an E2B API key for Python code execution, both to be added to a .env file. -- evidence: [readme.md#L248-L248](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L248-L248), [readme.md#L245-L246](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L245-L246), [readme.md#L250-L253](https://github.com/Doriandarko/claude-engineer/blob/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8/readme.md#L250-L253) (`clm_08c05f9aefc19b0a16d694bd18d549b4d8b18ba13c9f2e94b7ef8a793b9cb6b2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

