# vercel-doctor (`vercel-doctor`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Aniket-508
- License: MIT
- Language: TypeScript / JavaScript
- Interface: install=npx -y vercel-doctor@latest . (for projects); curl -fsSL https://vercel-doctor.com/install-skill.sh | bash (for coding agents)
- Model providers: None (deterministic rule-based analysis; no LLM at analysis time)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aniket-508/vercel-doctor](../../repos/aniket-508/vercel-doctor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Reduces Vercel bills with one command. Scans Next.js codebases for patterns that inflate Vercel bills (long function duration, uncached routes, unoptimized images) and detects dead code, outputting actionable diagnostics. Supports coding agent skills for Cursor, Claude Code, Amp Code, Codex, Gemini CLI, OpenCode, Windsurf, and Antigravity. Generates AI-ready fix prompts for popular coding agents. Supports Next.js 15/16+.

(captured site page body (agents/vercel-doctor.md), not a verified repo-code finding)
Vercel costs rise quietly: an uncached route, a sequentially-awaited function, or an unoptimized image shows up as invoice line items long after the code shipped. Vercel Doctor addresses that with a deterministic scanner — no LLM involved — that runs two passes over a Next.js codebase: one flags billing-relevant patterns (function duration, caching configuration, image optimization, prefetch behavior, edge functions, cron usage, build caching), the other finds dead code such as unused files, exports, and duplicates, then emits a scored report with file-level detail, version-aware Next.js 15/16 guidance, and JSON/markdown output for CI via a GitHub Action. For remediation it ships an installable skill and --ai-prompts output that feed ready-made fix prompts to Cursor, Claude Code, Codex, and other agents, which perform the actual edits. Next.js teams auditing cloud spend use it; it is MIT-licensed, unaffiliated with Vercel, and actively maintained on npm.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vercel-doctor.md)
