# Autolith (`autolith`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: lambda-symbolics
- License: ISC
- Language: Common Lisp
- Interface: platforms=CLI; install=curl -fsSL https://sh.lambda-symbolics.com/autolith | sh (standalone binary for Linux, macOS, BSDs, Windows); nix run github:lambda-symbolics/autolith; or build from a source checkout
- Model providers: ChatGPT, GitHub Copilot, Gemini, Grok, Nous, Anthropic, Fireworks, OpenCode, OpenRouter, Mistral, Vertex Gemini, Vertex Anthropic, local models via OpenAI-compatible endpoints (auth via autolith auth \<provider\>)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [lambda-symbolics/autolith](../../repos/lambda-symbolics/autolith.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A terminal agent living inside a live Common Lisp image that can introspect and rewrite its own running code — including itself — and roll back through self-created image generations when a modification goes wrong, recovering into a rescue image to diagnose the failure.

(captured site page body (agents/autolith.md), not a verified repo-code finding)
Autolith, or AL, is a terminal agent built as a live Common Lisp image rather than a program that talks to an editor: because the agent's own code is loaded in the same image it works in, it can observe its live state, introspect what it is doing, and modify its own source — adapting itself to the task or the user's preferences — where a conventional harness would need a restart. The design leans on image generations: you or AL checkpoint the running image, and a bad self-modification (the docs call it 'a full frontal lobotomy') rolls back to the prior generation or reloads into a recovery image that diagnoses and optionally repairs the damage. Around that core sit practical ergonomics — XDG-conforming configuration, a bounded catalog of Skills loaded on demand via skill.load, child agents in channels up to three levels deep, mission schedules that wake the agent for background work, an independent tool-less reviewer pass over changed snapshots, and MCP clients joined per channel — with a deliberate nod to the Lisp Machine it is 'pretty close' to. Model access is broad: web-flow or API-key auth for ChatGPT, Copilot, Gemini, Grok, Nous, Anthropic, Fireworks, OpenCode, OpenRouter, Mistral and Vertex, all switched with autolith auth. It ships as a standalone binary for Linux, macOS, the BSDs and Windows, ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/autolith.md)
