# agent.md (`agentmd`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: agentmd
- License: MIT
- Language: Markdown
- Interface: install=Place an AGENT.md file at the repository root; optionally symlink existing CLAUDE.md/.cursorrules-style files to it for backward compatibility
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [agentmd/agent.md](../../repos/agentmd/agent.md.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A specification defining AGENT.md, a standardized vendor-neutral Markdown configuration file that lets codebases communicate project conventions to any agentic coding tool; replaces fragmented config files (.cursorrules, .windsurfrules, CLAUDE.md, etc.) with one universal file any AI coding agent can parse; supports hierarchical files and @-mentions for file references; backward-compatible migration via symlinks so existing tools keep working. Authored by Geoffrey Huntley ...

(captured site page body (agents/agentmd.md), not a verified repo-code finding)
Every agentic coding tool grew its own instruction-file convention, so a repository supporting several agents accumulates near-duplicate configuration. The AGENT.md specification proposes one vendor-neutral Markdown file with RFC 2119 semantics, hierarchical resolution (root, subdirectory, and user-global files), @-mentions for composing other files, and documented symlink migrations from .cursorrules, CLAUDE.md, .clinerules, and similar files. It was authored by Geoffrey Huntley of Sourcegraph and published as an informational proposal in July 2025 rather than through a formal standards body. Adoption has been modest, with the competing AGENTS.md convention seeing wider industry uptake, so the document mostly matters as one position in the instruction-file standardization contest.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentmd.md)
