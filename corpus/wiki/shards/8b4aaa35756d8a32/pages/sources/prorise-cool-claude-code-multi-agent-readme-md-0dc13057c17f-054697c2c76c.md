---
access: public
aliases: []
claim_ids:
- clm_00509537fda793b930838d331b1929656cd53e2f7b3e4879744599c38fb1a65f
- clm_1047981bf7a5ace77373b236635df1c3c2a48a2fd9893bb6424620a34f2b94dc
- clm_2b58ec41a536d6ae823ab3633701c9b82fadb7a415f35f8f2c64f5b0897afc72
- clm_2bf68fff7ca5965dad9e5d0ebf45d22e9c413814bd08eafd34441d4c8139ed1e
- clm_5c7c8f3ec6818cbc6b89ce396933848b7eb757f9c44c255c328a970671f7edda
- clm_6599a10518aad93da85dea7b59e11afc926d2a4370309761667d8205d2cbb09f
- clm_6cf669def3ea9f68db4d73af4a2031b9795c595e0b1d114ae5e71d65c0f8d327
- clm_724dcb027f0f353fe8e8236012ec42498193e55d23408d7882dde2b60af9a8dc
- clm_95bbd9ec01b6a844d1355c63697db5c3f7a9a37f0e83eb5c137fb0cb66fecac1
- clm_af7447bcd959616a0fdba4f03abfe178a0702ef43fb3060d576314d3826d94fa
- clm_ffdc16a1fd3c0be5de5fe38ff24a516ef21d0223596f12d7634f9472af0b2d38
maturity: draft
page_id: pg_9a83928ff4315b508df7054697c2c76c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2eafaa34153e5fe5a252b19dff81cd61
title: Prorise-cool/Claude-Code-Multi-Agent/README.md @ 0dc13057c17f
updated_at: '2026-09-14T04:17:40Z'
---

# Prorise-cool/Claude-Code-Multi-Agent/README.md @ 0dc13057c17f

<!-- rcw:begin owner=source:src_2eafaa34153e5fe5a252b19dff81cd61 block=evidence -->
- Skills are invoked via slash commands like /backend-specialist; the flow reads the skill's SKILL.md, parses YAML frontmatter, and uses Ollama to optimize the prompt before executing as an expert persona. [@claim:clm_00509537fda793b930838d331b1929656cd53e2f7b3e4879744599c38fb1a65f]
- The framework runs a Python hooks system that executes intelligent actions automatically across the Claude Code session lifecycle, using Ollama for smart decisions. [@claim:clm_1047981bf7a5ace77373b236635df1c3c2a48a2fd9893bb6424620a34f2b94dc]
- Each skill requires a SKILL.md with YAML frontmatter (shown fields: name, description, version, author) and may include a references/ directory; example skills include code-review, test-generator, api-designer, database-optimizer, and doc-writer. [@claim:clm_2b58ec41a536d6ae823ab3633701c9b82fadb7a415f35f8f2c64f5b0897afc72]
- Hooks return JSON with an exit_code where 0 allows the operation to continue and 2 blocks it, e.g. when a dangerous command is detected. [@claim:clm_2bf68fff7ca5965dad9e5d0ebf45d22e9c413814bd08eafd34441d4c8139ed1e]
- The layout includes .claude/hooks (core modules base_hook.py, ollama_client.py, document_manager.py, config.py, logger.py plus handler entry scripts), .claude/commands, .claude/skills, and settings.json for hooks configuration. [@claim:clm_5c7c8f3ec6818cbc6b89ce396933848b7eb757f9c44c255c328a970671f7edda]
- The project depends on Ollama (recommended, with gemma3:1b as the suggested lightweight model and llama3.2:3b optional) and uv for Python dependency management, with optional TTS via pyttsx3 configured through environment variables. [@claim:clm_6599a10518aad93da85dea7b59e11afc926d2a4370309761667d8205d2cbb09f]
- All prompt templates are stored in .claude/hooks/prompts.json with variable placeholders, grouped by hook type, for tuning and version control; edits load on the next hook run without restart. [@claim:clm_6cf669def3ea9f68db4d73af4a2031b9795c595e0b1d114ae5e71d65c0f8d327]
- The shipped settings.json grants permissions for Bash(mkdir:*), Bash(uv:*), Bash(chmod:*), Write, and Edit, and wires SessionStart, UserPromptSubmit, and PostToolUse hooks to uv-run Python scripts. [@claim:clm_724dcb027f0f353fe8e8236012ec42498193e55d23408d7882dde2b60af9a8dc]
- Repository development practice: contributors are told to fork the repo, create a feature branch, commit, push, and open a pull request, and to set up the dev environment with uv sync. [@claim:clm_95bbd9ec01b6a844d1355c63697db5c3f7a9a37f0e83eb5c137fb0cb66fecac1]
- The design is document-driven: three core documents (DEVELOPMENT.md, KNOWLEDGE.md, CHANGELOG.md) are read and injected at session start, replacing Memory MCP to avoid context explosion. [@claim:clm_af7447bcd959616a0fdba4f03abfe178a0702ef43fb3060d576314d3826d94fa]
- On session start, the SessionStart hook detects the project type via Ollama, scans and loads skills, initializes the document system, and checks Git configuration such as .gitignore and branch strategy. [@claim:clm_ffdc16a1fd3c0be5de5fe38ff24a516ef21d0223596f12d7634f9472af0b2d38]
<!-- rcw:end owner=source:src_2eafaa34153e5fe5a252b19dff81cd61 block=evidence -->

## Researcher notes

