# prorise-cool/claude-code-multi-agent -- full detail

[Back to orientation](claude-code-multi-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/prorise-cool/claude-code-multi-agent/0dc13057c17fb4591fdd5f02deb170ffacf981d2/f6186454c59968b4.json](../../../wiki/dossiers/prorise-cool/claude-code-multi-agent/0dc13057c17fb4591fdd5f02deb170ffacf981d2/f6186454c59968b4.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The framework runs a Python hooks system that executes intelligent actions automatically across the Claude Code session lifecycle, using Ollama for smart decisions. -- evidence: [README.md#L358-L358](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L358-L358), [README.md#L23-L23](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L23-L23) (`clm_1047981bf7a5ace77373b236635df1c3c2a48a2fd9893bb6424620a34f2b94dc`)
- [observation/documented] The layout includes .claude/hooks (core modules base_hook.py, ollama_client.py, document_manager.py, config.py, logger.py plus handler entry scripts), .claude/commands, .claude/skills, and settings.json for hooks configuration. -- evidence: [README.md#L879-L919](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L879-L919) (`clm_5c7c8f3ec6818cbc6b89ce396933848b7eb757f9c44c255c328a970671f7edda`)

## design-choices (2 claim(s))

- [observation/documented] The design is document-driven: three core documents (DEVELOPMENT.md, KNOWLEDGE.md, CHANGELOG.md) are read and injected at session start, replacing Memory MCP to avoid context explosion. -- evidence: [README.md#L360-L363](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L360-L363), [README.md#L93-L93](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L93-L93) (`clm_af7447bcd959616a0fdba4f03abfe178a0702ef43fb3060d576314d3826d94fa`)
- [observation/documented] All prompt templates are stored in .claude/hooks/prompts.json with variable placeholders, grouped by hook type, for tuning and version control; edits load on the next hook run without restart. -- evidence: [README.md#L1031-L1031](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L1031-L1031), [README.md#L496-L501](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L496-L501) (`clm_6cf669def3ea9f68db4d73af4a2031b9795c595e0b1d114ae5e71d65c0f8d327`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are told to fork the repo, create a feature branch, commit, push, and open a pull request, and to set up the dev environment with uv sync. -- evidence: [README.md#L1071-L1071](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L1071-L1071), [README.md#L1041-L1054](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L1041-L1054) (`clm_95bbd9ec01b6a844d1355c63697db5c3f7a9a37f0e83eb5c137fb0cb66fecac1`)

## skills-patterns (1 claim(s))

- [observation/documented] Each skill requires a SKILL.md with YAML frontmatter (shown fields: name, description, version, author) and may include a references/ directory; example skills include code-review, test-generator, api-designer, database-optimizer, and doc-writer. -- evidence: [README.md#L700-L701](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L700-L701), [README.md#L558-L564](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L558-L564), [README.md#L532-L550](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L532-L550), [README.md#L556-L556](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L556-L556), [README.md#L820-L821](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L820-L821), [README.md#L766-L767](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L766-L767), [README.md#L594-L595](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L594-L595), [README.md#L645-L646](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L645-L646) (`clm_2b58ec41a536d6ae823ab3633701c9b82fadb7a415f35f8f2c64f5b0897afc72`)

## interfaces (2 claim(s))

- [observation/documented] Hooks return JSON with an exit_code where 0 allows the operation to continue and 2 blocks it, e.g. when a dangerous command is detected. -- evidence: [README.md#L409-L410](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L409-L410), [README.md#L382-L382](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L382-L382) (`clm_2bf68fff7ca5965dad9e5d0ebf45d22e9c413814bd08eafd34441d4c8139ed1e`)
- [observation/documented] Skills are invoked via slash commands like /backend-specialist; the flow reads the skill's SKILL.md, parses YAML frontmatter, and uses Ollama to optimize the prompt before executing as an expert persona. -- evidence: [README.md#L288-L290](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L288-L290), [README.md#L520-L528](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L520-L528) (`clm_00509537fda793b930838d331b1929656cd53e2f7b3e4879744599c38fb1a65f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] On session start, the SessionStart hook detects the project type via Ollama, scans and loads skills, initializes the document system, and checks Git configuration such as .gitignore and branch strategy. -- evidence: [README.md#L445-L445](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L445-L445), [README.md#L441-L441](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L441-L441), [README.md#L455-L455](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L455-L455), [README.md#L258-L262](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L258-L262), [README.md#L437-L437](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L437-L437), [README.md#L449-L451](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L449-L451) (`clm_ffdc16a1fd3c0be5de5fe38ff24a516ef21d0223596f12d7634f9472af0b2d38`)

## tools-permissions (1 claim(s))

- [observation/documented] The shipped settings.json grants permissions for Bash(mkdir:*), Bash(uv:*), Bash(chmod:*), Write, and Edit, and wires SessionStart, UserPromptSubmit, and PostToolUse hooks to uv-run Python scripts. -- evidence: [README.md#L965-L997](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L965-L997) (`clm_724dcb027f0f353fe8e8236012ec42498193e55d23408d7882dde2b60af9a8dc`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project depends on Ollama (recommended, with gemma3:1b as the suggested lightweight model and llama3.2:3b optional) and uv for Python dependency management, with optional TTS via pyttsx3 configured through environment variables. -- evidence: [README.md#L955-L955](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L955-L955), [README.md#L232-L235](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L232-L235), [README.md#L254-L256](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L254-L256), [README.md#L132-L132](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L132-L132), [README.md#L251-L251](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L251-L251), [README.md#L109-L111](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L109-L111), [README.md#L135-L136](https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/0dc13057c17fb4591fdd5f02deb170ffacf981d2/README.md#L135-L136) (`clm_6599a10518aad93da85dea7b59e11afc926d2a4370309761667d8205d2cbb09f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

