# deepsec (`deepsec`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: vercel-labs
- License: Apache-2.0
- Language: TypeScript
- Interface: install=npm
- Model providers: Vercel AI Gateway, OpenAI, Anthropic, custom HTTPS provider
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [vercel-labs/deepsec](../../repos/vercel-labs/deepsec.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Agent-powered vulnerability scanner for on-demand review of large-scale repos. Resumable execution (skips already-analyzed files on re-run), fans out work across Vercel Sandbox microVM worker machines in parallel, tunable AI thinking levels, keeps API keys host-side (injected into sandboxes rather than baked in).

(captured site page body (agents/deepsec.md), not a verified repo-code finding)
deepsec is Vercel Labs' agent-powered vulnerability scanner for on-demand, whole-repository security review rather than continuous linting. A free regex pre-pass filters the codebase, then AI models at maximum reasoning effort review what remains, fanning out across worker machines — optionally Vercel Sandbox microVMs — so large codebases parallelize; runs are resumable, skipping files already analyzed when interrupted. Workflows run through npx commands (init, scan, process, revalidate, export), with findings exportable as markdown directories and a SKILL.md exposed so coding agents can operate the scanner. Billing goes through Vercel AI Gateway or the user's own OpenAI/Anthropic keys, and large scans can cost thousands of dollars, which suits security teams auditing big repositories on demand.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepsec.md)
