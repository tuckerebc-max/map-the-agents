# code-review (`code-review`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: gemini-cli-extensions
- License: Apache-2.0
- Language: Markdown / Gemini CLI extension definitions
- Interface: platforms=CLI; install=gemini extensions install https://github.com/gemini-cli-extensions/code-review
- Model providers: Google
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [gemini-cli-extensions/code-review](../../repos/gemini-cli-extensions/code-review.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Gemini CLI extension built by the authors of the Gemini Code Assist GitHub App; integrates AI-powered code review directly into the Gemini CLI for both branch changes and pull requests via /code-review and /pr-code-review commands. PR review requires the GitHub MCP server.

(captured site page body (agents/code-review.md), not a verified repo-code finding)
The extension ports the review behavior of Google's Code Assist GitHub app into a local Gemini CLI session, so developers get review feedback on their working branch before pushing. The /code-review command analyzes changes on the current branch, while /pr-code-review pulls a specified GitHub pull request through the GitHub MCP server and reviews it in place, accepting repository and PR identifiers via arguments or the REPOSITORY and PULL_REQUEST_NUMBER environment variables. It is installed with the Gemini CLI extension command and requires Gemini CLI v0.4.0 or newer, running entirely within the user's existing Gemini CLI setup rather than as a separate product. It targets developers already using Gemini CLI who want review feedback on branch diffs and pull requests without leaving the terminal.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/code-review.md)
