# Benzi (`benzi`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Variant Technologies
- License: Proprietary
- Language: Python
- Interface: platforms=Web
- Model providers: DeepSeek, Anthropic
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [oooscoos/benzi](../../repos/oooscoos/benzi.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Compiles the codebase into a resolved, queryable map before answering: tree-sitter grammars resolve imports, class ancestry, and every identifier to its definition, so call-flow and data-flow questions answer in O(1) through tools like get_callers, call_tree, trace_path, and backflow. Every edit passes syntax and semantic checks against the real parser with automatic rollback on broken parses.

(captured site page body (agents/benzi.md), not a verified repo-code finding)
Benzi is a coding agent harness from Variant Technologies built on the observation that Claude Code greps, Cursor embeds, and Aider maps signatures, while Benzi resolves. Before the agent loop runs, it compiles the codebase into a queryable map using per-language tree-sitter grammars — ten languages spanning Python, JavaScript, TypeScript, Java, C#, C++, C, Go, Rust, and Ruby, plus a second engine for HTML, CSS, and DOM-JS — resolving imports, class ancestry, and identifier definitions, and joining call flow and data flow at call sites. The agent then works through 35-plus tools like get_callers, call_tree, trace_path, and backflow, and every write is gated through syntax and semantic checks with blast-radius checks before and after changes and automatic rollback on broken parses. Its self-reported benchmarks include 78.2% on SWE-bench Verified run on DeepSeek v4-flash at $0.095 per resolved instance, and a cross-harness comparison claiming it reads 2.3x fewer lines than Claude Code on the same 24-bug set; the repo is public under a proprietary source-available license, with a web app and a VS Code extension.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/benzi.md)
