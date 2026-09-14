# Awel (`awel`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: MarsZ42
- License: MIT (README) / Apache-2.0 (repo metadata - conflicting)
- Language: TypeScript, JavaScript (Node.js)
- Interface: platforms=IDE; install=Set at least one AI provider env var, then: npx awel create (new project) or cd existing-next-app && npx awel dev
- Model providers: Claude Code (Claude CLI), Anthropic API, OpenAI, Google AI, MiniMax, Zhipu AI, Vercel Gateway, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [marsz42/awel](../../repos/marsz42/awel.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI dev overlay/proxy that lives inside your running Next.js app rather than a separate IDE or CLI; runs a proxy on :3001 in front of the dev server on :3000 and injects an isolated Shadow-DOM chat button; element inspector attaches clicked DOM elements as context; screenshot annotator with shapes/arrows/text; one-click undo of all file changes from a session; pauses HMR/WebSocket ...

(captured site page body (agents/awel.md), not a verified repo-code finding)
Awel puts an AI dev agent inside the running Next.js app rather than beside it: a proxy on port 3001 fronts the dev server on 3000, intercepts HTML responses, and injects a Shadow-DOM script that mounts a floating chat button. Opening it reveals a full-page chat dashboard (in an iframe) where an agent reads, writes, and edits project files, with HMR traffic paused during edits to avoid reload interference. Tools cover file ops, bash, code search, web search/fetch, plan proposals, and dev-server restarts, backed by the Vercel AI SDK across Anthropic, OpenAI, Google, MiniMax, Zhipu, OpenRouter, and Claude CLI (YOLO mode). Element inspection and screenshot annotation attach DOM context directly. It is MIT/Apache-2.0 licensed (the two disagree in-repo), installed via npx awel create|dev, and suits Next.js developers who want in-app agent assistance without leaving the browser tab.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/awel.md)
