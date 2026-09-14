# open-spdd (`open-spdd`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: gszhangwei
- License: MIT
- Language: Go
- Interface: install=brew
- Model providers: none (generates commands/skills consumed by Cursor, Claude Code, GitHub Copilot, Antigravity, OpenCode, Codex)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [gszhangwei/open-spdd](../../repos/gszhangwei/open-spdd.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Methodology and cross-platform CLI that transforms AI coding prompts into executable design contracts using the REASONS Canvas framework (7 dimensions: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards). Supports bidirectional sync between design and code (/spdd-sync reverse-syncs code changes back to design). Works across Cursor, Claude Code, GitHub Copilot, Antigravity, OpenCode, Codex via generated command templates. Install also via go install ...

(captured site page body (agents/open-spdd.md), not a verified repo-code finding)
AI coding sessions tend to skip design discipline: requirements stay implicit in chat, and the resulting code drifts from what was actually asked for. OpenSPDD packages a methodology called Structured Prompt-Driven Development with a cross-platform Go CLI that turns a prompt into an 'executable design contract' organized along the REASONS Canvas — Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards. Running openspdd init detects the installed AI tool (Cursor, Claude Code, Copilot, Antigravity, OpenCode, Codex) and generates native slash commands or skills for it; the workflow then runs /spdd-analysis, /spdd-reasons-canvas, /spdd-generate, and /spdd-sync, the last of which reverse-syncs code changes back into the design document. A single Go binary with embedded templates installs via Homebrew, go install, or release binaries. It targets enterprise feature work and team collaboration where the design document needs to outlive the chat session.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-spdd.md)
