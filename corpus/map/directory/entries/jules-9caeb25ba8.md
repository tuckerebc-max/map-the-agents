# Jules (`jules`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Google
- License: Proprietary
- Language: unknown
- Interface: platforms=CLI, Web; install=Web app — no local install. Visit jules.google.com, sign in with Google, connect GitHub.
- Model providers: Gemini (Gemini 2.5 Pro / Gemini 3 Pro)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Async coding agent by Google that clones your repo to a Cloud VM, builds a plan using Gemini models, makes code edits, and opens pull requests for approval. GitHub-native workflow (assign via 'jules' label), plan-before-code, scales to massively parallel multi-agent development (up to 60 concurrent tasks on Ultra).

(captured site page body (agents/jules.md), not a verified repo-code finding)
Jules moves coding work off the developer's machine entirely: tasks are assigned through GitHub (a 'jules' label or a repo/branch prompt), and the agent works asynchronously on a cloud VM. The workflow is plan-first — Gemini drafts the approach, the user approves or edits it, then diffs are reviewed before Jules opens a pull request. Concurrency is the product's lever: up to 60 parallel tasks on the Ultra tier, making it suited to batch chores like dependency bumps, test backfill, and small features across many repos. Pricing ties to Google One AI tiers: free at 15 tasks/day, Pro at 100/day, Ultra at 300/day with priority model access.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/jules.md)
