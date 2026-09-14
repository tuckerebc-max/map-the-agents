# thrush-swe-agent (`thrush-swe-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: shoyann
- License: unknown
- Language: TypeScript
- Interface: install=git clone --recurse-submodules, npm install, npm run bootstrap:mini, copy .env.local.example to .env.local, npm run dev
- Model providers: deepseek, openai, anthropic
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [shoyann/thrush-swe-agent](../../repos/shoyann/thrush-swe-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Dual-mode local SWE agent workbench: Assist mode (agent drafts edits, user approves each one) and Auto mode (runs bundled mini-swe-agent in isolated git worktree, returns report, diff, logs, trajectory without touching main workspace)

(captured site page body (agents/thrush-swe-agent.md), not a verified repo-code finding)
Thrush is a local, self-hosted workbench for software-engineering agents built around two deliberately different safety postures. In supervised operation the agent inspects the repo, reasons, drafts edits, and asks for confirmation, with every change staged as a pending revision the developer approves before anything touches disk. Delegating a full task instead routes it to a bundled mini-swe-agent instance running inside an isolated git worktree under data/auto-runs, after an Environment Doctor pre-check verifies clean git state, Docker, the model key, and GitHub readiness; the run produces a report, diff, logs, and full trajectory while the main workspace stays untouched, and opening a draft PR remains a manual step. The implementation is Next.js 15 with SQLite, keyed for DeepSeek, OpenAI, or Anthropic, with Windows users directed to WSL. It fits developers who want one local workbench that can switch between reviewed drafting and autonomous runs on throwaway worktrees.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/thrush-swe-agent.md)
