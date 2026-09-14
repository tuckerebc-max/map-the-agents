# RepoAgent (`repoagent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: OpenBMB
- License: Apache-2.0
- Language: Python
- Interface: install=pip
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [openbmb/repoagent](../../repos/openbmb/repoagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM-powered framework for automatic repository-level code documentation generation using AST-based per-object analysis with bidirectional invocation relationship detection. Multi-threaded concurrent generation, seamless Markdown replacement on code changes, and pre-commit hook for team-wide automated doc maintenance. Prototype Chat With Repo feature for Q&A and code explanation.

(captured site page body (agents/repoagent.md), not a verified repo-code finding)
Repository documentation rots because writing it is unpaid labor and updating it after every refactor is worse; RepoAgent automates the maintenance part. It parses the project into an AST, produces per-object Markdown entries that record callers and callees in both directions, and stores the results as a Gitbook-style book inside the repo. On each commit, a diff-driven pass regenerates only the affected objects, which keeps cost and review surface proportional to the change. Generation is multi-threaded with customizable prompts and output language, and an optional chat-with-repo service answers questions from the generated corpus. Research groups and Python project maintainers use it to keep documentation synchronized with code; Java and C++ support remains future work.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/repoagent.md)
