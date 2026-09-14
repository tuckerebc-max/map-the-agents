# GitIngest (`gitingest`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: coderamp-labs
- License: MIT
- Language: Python
- Interface: platforms=Desktop; install=pip
- Model providers: none (calls no LLM APIs; uses tiktoken only to estimate token counts)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (browser extensions for Chrome, Firefox, Edge) (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [coderamp-labs/gitingest](../../repos/coderamp-labs/gitingest.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Turns any Git repository into a prompt-friendly text digest optimized for LLMs — simply replace 'hub' with 'ingest' in any GitHub URL. Offers CLI, Python package, browser extensions, and self-hostable web service.

(captured site page body (agents/gitingest.md), not a verified repo-code finding)
Getting a whole repository into an LLM context is awkward, and GitIngest exists to make it a single step. It clones or reads a repo and emits a formatted digest — summary, directory tree, file contents — with token counts computed via tiktoken so users can budget prompts, handling private repos through GitHub PATs and submodules along the way. The same capability ships as gitingest.com, a pip-installed CLI and Python library, Chrome/Firefox/Edge extensions, and a Docker self-host option. It calls no model APIs itself; the digest is consumed in whatever LLM tool the user prefers. At 15k-plus stars it is the best-known alternative to Repomix for prompt-packaging codebases.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gitingest.md)
