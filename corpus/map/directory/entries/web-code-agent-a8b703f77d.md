# web-code-agent (`web-code-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: oldjs
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=git clone + npm install (Next.js 14 project)
- Model providers: None — generates context Markdown for external LLMs (ChatGPT, Claude)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [oldjs/web-code-agent](../../repos/oldjs/web-code-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runs entirely locally in the browser with absolute privacy—code never leaves the user's machine. Uses a semantic vectorization engine to build a local knowledge index of the codebase, enabling natural language Q&A. Acts as an LLM collaboration accelerator by generating context-aware Markdown to feed AI assistants, reducing token costs and API latency. Also supports smart config generation (e.g., Dockerfile).

(captured site page body (agents/web-code-agent.md), not a verified repo-code finding)
web-code-agent (Folda-Scan) solves codebase Q&A for users who cannot or will not upload code to cloud services: scanning, semantic vectorization, indexing, and question matching all run in the browser using the File System Access API, so project code never leaves the machine. Built on Next.js 14, it builds a local vector index from a selected project folder and answers natural-language questions against it. It also generates context-aware Markdown designed to be pasted into external AI assistants, reducing token costs, and can help produce configuration files such as Dockerfiles. It calls no LLM APIs itself; external assistants like ChatGPT or Claude consume the Markdown it produces. Usage requires a Chromium browser with the File System Access API.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/web-code-agent.md)
