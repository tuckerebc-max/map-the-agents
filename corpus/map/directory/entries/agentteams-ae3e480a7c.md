# AgentTeams (`agentteams`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: agentscope-ai
- License: Apache-2.0
- Language: Multi-runtime (Node.js, Python)
- Interface: install=docker
- Model providers: OpenAI, DeepSeek, Qwen
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [agentscope-ai/agentteams](../../repos/agentscope-ai/agentteams.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Collaborative multi-agent runtime (by Alibaba/AgentScope) using a Manager-Workers architecture over self-hosted Matrix IM rooms. Zero-credential security model — Workers never see real API keys, only consumer tokens via Higress AI Gateway. Human-in-the-loop by default, Kubernetes-native CRD management, multi-runtime Workers (OpenClaw/Node, QwenPaw/Python, Hermes), 80,000+ community skills.

(captured site page body (agents/agentteams.md), not a verified repo-code finding)
Multi-agent setups usually hide agent-to-agent traffic in black-box calls, and leaked API keys from a compromised worker are the standard failure mode. AgentTeams, from the AgentScope team, instead places a Manager agent and its Workers in self-hosted Matrix rooms alongside the human, with declarative Worker/Team/Human definitions and runtime swaps (OpenClaw, QwenPaw, Hermes) via commands like agt update worker --runtime hermes. Security rests on the Higress AI gateway holding every real credential — workers receive consumer tokens only, so a compromised worker exposes no LLM, GitHub, or MCP keys. A MinIO-backed shared filesystem reduces token spend between agents. Deployment is a one-command install script or a Helm chart bundling Higress, Tuwunel, MinIO, and the controller, with the project backed by Alibaba/Aliyun.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentteams.md)
