---
access: public
aliases: []
claim_ids:
- clm_054a20b9fae8aa6dca9431d7e2c1499f2ddacf7fdde596d6d5b2a05e175c2cb9
- clm_08c05f9aefc19b0a16d694bd18d549b4d8b18ba13c9f2e94b7ef8a793b9cb6b2
- clm_2319d1fd14b66c34b9302001f52bd1219aca64a72dab7c1de387525e70aff314
- clm_326ba75f4c2d650f9a14d12528e329ebce22fa888ab615c3620973be70b65865
- clm_459fd66c6b6d68da4d6da66260951581967416309e290eed2f332ff22dd2ae5a
- clm_48effc2c8a4463ef70dcc655590b4f900fb3261611a31cdade4d7f5200e7a632
- clm_5b285c118842e0e5d9a944e0eab137eeaa0afa0a749fba2d3677612a7b0f38cb
- clm_646c84e53ea0cc71b888694967a45d4ee94d005c1f70994ec3e9bce7e4bbfca7
- clm_94fbaace38e9b56875c326a0c28726c91bad28ac414916526974738d6bd9713f
- clm_aa3198ae43dba18a4e413364f4a0e03a1e495964c944969222645a855107332b
- clm_ea1da9db7df52b73e3471fb01086e11a94514a76feafd9d105e5f9bfeccfb100
maturity: draft
page_id: pg_5c94d0b9aaca5034814fd14ac543e0d5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4e1ba02ac2e052f58d387463c1046df0
title: Doriandarko/claude-engineer/readme.md @ 0a9e4b309bf6
updated_at: '2026-09-14T01:46:27Z'
---

# Doriandarko/claude-engineer/readme.md @ 0a9e4b309bf6

<!-- rcw:begin owner=source:src_4e1ba02ac2e052f58d387463c1046df0 block=evidence -->
- Repository development practice: contributions are welcome via pull request, and major changes should be preceded by opening an issue for discussion. [@claim:clm_054a20b9fae8aa6dca9431d7e2c1499f2ddacf7fdde596d6d5b2a05e175c2cb9]
- The product requires an Anthropic API key for Claude 3.5 access and an E2B API key for Python code execution, both to be added to a .env file. [@claim:clm_08c05f9aefc19b0a16d694bd18d549b4d8b18ba13c9f2e94b7ef8a793b9cb6b2]
- Configuration options include MODEL (Claude 3.5 Sonnet), MAX_TOKENS, MAX_CONVERSATION_TOKENS, TOOLS_DIR, SHOW_TOOL_USAGE, ENABLE_THINKING, and DEFAULT_TEMPERATURE. [@claim:clm_2319d1fd14b66c34b9302001f52bd1219aca64a72dab7c1de387525e70aff314]
- Built-in tools include a Tool Creator, UV package manager interface, E2B sandboxed Python code executor, Ruff linting tool, and screenshot capture. [@claim:clm_326ba75f4c2d650f9a14d12528e329ebce22fa888ab615c3620973be70b65865]
- The CLI provides rich text formatting, an ASCII token usage bar, live progress indicators, direct tool interaction, and detailed debugging output. [@claim:clm_459fd66c6b6d68da4d6da66260951581967416309e290eed2f332ff22dd2ae5a]
- The web UI offers image upload and analysis with Claude Vision, token usage visualization, markdown rendering with syntax highlighting, and Ctrl/Cmd+Enter to send. [@claim:clm_48effc2c8a4463ef70dcc655590b4f900fb3261611a31cdade4d7f5200e7a632]
- The assistant is designed to autonomously identify, create, and load new tools during conversations, expanding its capabilities over time. [@claim:clm_5b285c118842e0e5d9a944e0eab137eeaa0afa0a749fba2d3677612a7b0f38cb]
- Web tools include DuckDuckGo search, a readable-content web scraper, and a browser tool that opens URLs in the system default browser. [@claim:clm_646c84e53ea0cc71b888694967a45d4ee94d005c1f70994ec3e9bce7e4bbfca7]
- The product ships as both a CLI (ce3.py) and a web interface (app.py), with the web UI served at localhost:5000. [@claim:clm_94fbaace38e9b56875c326a0c28726c91bad28ac414916526974738d6bd9713f]
- File-system tools cover creating folders and files, reading multiple files with binary filtering, full and partial file editing, and exact-substring diff edits. [@claim:clm_aa3198ae43dba18a4e413364f4a0e03a1e495964c944969222645a855107332b]
- The project structure includes app.py (web server), ce3.py (CLI), config.py, static assets, templates, a tools directory with base.py, and prompts/system_prompts.py. [@claim:clm_ea1da9db7df52b73e3471fb01086e11a94514a76feafd9d105e5f9bfeccfb100]
<!-- rcw:end owner=source:src_4e1ba02ac2e052f58d387463c1046df0 block=evidence -->

## Researcher notes

