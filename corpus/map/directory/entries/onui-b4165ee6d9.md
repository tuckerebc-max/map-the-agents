# onUI (`onui`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: onllm-dev
- License: GPL-3.0
- Language: TypeScript
- Interface: platforms=Web; install=Chrome Web Store / Edge Add-ons / installer from GitHub releases (curl or PowerShell)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [onllm-dev/onui](../../repos/onllm-dev/onui.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Annotation-first UI pair programming: a browser extension (Chrome + Edge + Firefox) that lets humans visually mark up UI elements/regions for AI agents via in-page annotation and draw mode; local-only MCP bridge with no cloud backend, privacy-preserving; auto-registers onui-local MCP for Claude Code and Codex; shadow DOM isolation for stable styling; multi-format export (compact to forensic) for varying agent context ...

(captured site page body (agents/onui.md), not a verified repo-code finding)
onUI addresses the gap between what a developer sees in a browser and what a coding agent can understand from a screenshot or text description. The extension adds annotate and draw modes to any web page, letting users tag elements or regions with intent and severity before exporting structured context at several detail levels. A local MCP server hands that context to agents such as Claude Code or Codex, with no cloud service in the path. Because annotations target the rendered page, no instrumentation of the target application is required, and the extension stays off by default per tab. The project ships as a Chrome, Edge, and Firefox extension with a native bridge for the MCP server.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/onui.md)
