# Speech-To-Code (`speech-to-code`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: dharllc
- License: MIT
- Language: JavaScript (frontend), Python (backend, FastAPI/uvicorn)
- Interface: install=git clone; chmod +x build.sh; ./build.sh (sets up Python venv, installs deps, creates .env files); start frontend (npm start) and backend (uvicorn main:app --reload) separately
- Model providers: OpenAI, Anthropic, Google (Generative AI)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [dharllc/speech-to-code](../../repos/dharllc/speech-to-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Web app that converts spoken language into executable code using LLMs; combines speech input, repository files, and manual text into a unified prompt composer. Uses LLM APIs directly to bypass rate limits/outages; includes cost tracking, system prompt management with versioning, and persistent chat sessions. Archived (read-only as of Jun 26, 2026).

(captured site page body (agents/speech-to-code.md), not a verified repo-code finding)
Speech-To-Code was built for developers who think faster than they type at a keyboard: a browser composer combines real-time speech-to-text, selectable repository files, and manual text into one prompt, then sends it straight to OpenAI, Anthropic, or Google APIs. Generated code is displayed for review and clipboard transfer rather than written back to disk, so the tool sits at the prompt-composition stage of development rather than acting on the repository. The FastAPI backend tracks spend per session, and system prompts are managed with versioning for reuse. The repository was archived read-only in June 2026 after 321 commits, so it remains available as a reference implementation of voice-driven LLM interaction rather than a maintained tool.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/speech-to-code.md)
