# ocode (`ocode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: haasonsaas
- License: AGPL-3.0
- Language: Python
- Interface: platforms=Autonomous, CLI, IDE; install=curl -fsSL https://raw.githubusercontent.com/haasonsaas/ocode/main/scripts/install.sh | bash; or pip install -e .; or pipx install git+https://github.com/haasonsaas/ocode.git
- Model providers: Ollama
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [haasonsaas/ocode](../../repos/haasonsaas/ocode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native AI coding assistant powered by local Ollama models; 19+ specialized tools; full MCP server support (resources, tools, prompts); agent tool delegates complex tasks to specialized agents; fully offline and self-hosted

(captured site page body (agents/ocode.md), not a verified repo-code finding)
ocode is a terminal-native coding assistant that streams from a local Ollama instance, requiring no API keys or cloud proxies. It ships nineteen specialized tools covering file operations, grep and diff, git, shell execution, Jupyter notebooks, and architecture analysis, with a smart tool-selection layer that detects multi-action requests. An agent tool delegates complex tasks to specialized subagents for multi-step work. Full MCP support lets it expose resources, tools, and prompts as a server as well as consume them. The permission system is whitelist-first with sandboxed shell execution and blocked paths by default, reflecting a security-first posture rare in solo hobby agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ocode.md)
