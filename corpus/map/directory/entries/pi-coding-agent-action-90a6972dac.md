# pi-coding-agent-action (`pi-coding-agent-action`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: shaftoe
- License: MIT
- Language: TypeScript
- Interface: install=GitHub Action: uses: shaftoe/pi-coding-agent-action@v2 in workflow YAML; requires Node.js 22+
- Model providers: openai, google, anthropic, amazon-bedrock, google-vertex, custom (OpenAI-compatible)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [shaftoe/pi-coding-agent-action](../../repos/shaftoe/pi-coding-agent-action.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): CI/CD GitHub Action integrating the Pi coding agent with git hosting platform workflows (GitHub, Codeberg, Forgejo); enables interactive (/pi in comments) and non-interactive agent runs for issue assistance, PR reviews, automated code reviews; extensible via npm packages, git repos, and local .ts files

(captured site page body (agents/pi-coding-agent-action.md), not a verified repo-code finding)
pi-coding-agent-action puts the pi coding agent inside continuous-integration workflows so repositories get an agent that responds to /pi-prefixed comments on issues and pull requests, reviews PRs, and executes scheduled maintenance such as dependency audits or documentation syncs. The action wraps the pi SDK with built-in tools for GitHub APIs — commenting, reviewing, opening PRs — and loads the same skills, extensions, and AGENTS.md files a local pi session would, so behavior matches between terminal and CI. It also targets Codeberg and self-hosted Forgejo or Gitea instances, covering the GitHub-API-compatible forge ecosystem rather than GitHub alone. Sessions can be exported as HTML or JSONL artifacts or shared as gist links for postmortems. Released under MIT with semantic-release automation, it serves maintainers who want agent-powered automation on infrastructure they control.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-coding-agent-action.md)
