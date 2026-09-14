# LocoOperator (`locooperator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: LocoreMind
- License: MIT
- Language: Python
- Interface: install=git clone + uv sync; requires Claude Code (npm install -g @anthropic-ai/claude-code), llama.cpp, and an OpenRouter API key
- Model providers: OpenRouter (cloud fallback); local llama.cpp (GGUF)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: yes (yes)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [locoremind/locooperator](../../repos/locoremind/locooperator.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): 4B-parameter code-exploration agent distilled from Qwen3-Coder-Next, designed as a local sub-agent for Claude Code-style agent loops; 100% JSON-valid tool calls (outperforming the teacher model's 87.6%); runs locally via GGUF/llama.cpp at zero API cost; hybrid routing proxy falls back to OpenRouter on context overflow.

(captured site page body (agents/locooperator.md), not a verified repo-code finding)
The project targets the cost profile of Claude Code sessions, where every cheap exploration subagent still bills API tokens. A local proxy intercepts Claude Code's subagent dispatches (which would otherwise default to Haiku) and routes them to LocoOperator-4B served by llama.cpp, translating between the Anthropic Messages API and the model's JSON tool-call format. Training prioritized tool-call validity over general capability, which is why the distilled model beats its teacher on JSON validity. When a subagent's context overflows, the proxy falls back to OpenRouter so sessions do not die mid-exploration. Claude Code users with local GPU capacity use it to cut per-session cost while keeping the main agent on a frontier model.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/locooperator.md)
