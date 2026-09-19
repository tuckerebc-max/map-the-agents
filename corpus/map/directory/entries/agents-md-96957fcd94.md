# agents-md (`agents-md`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: FerroxLabs
- License: MIT
- Language: Markdown
- Interface: platforms=CLI; install=curl
- Model providers: Any (tool-agnostic instructions file, not a model integration)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ferroxlabs/agents-md](../../repos/ferroxlabs/agents-md.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A drop-in AGENTS.md file (~200 lines) that makes every coding agent (Claude Code, Codex, Cursor, Gemini CLI, Aider, Windsurf, Copilot, Devin) behave like a senior engineer — kills sycophancy, stops drive-by refactors, forces verification loops, surfaces ambiguities. Universal single-file approach: one AGENTS.md read natively by most agents; symlink covers Claude Code (CLAUDE.md) and Gemini CLI (GEMINI.md). Self-improving: Section 11 'Project ...

(captured site page body (agents/agents-md.md), not a verified repo-code finding)
Coding agents tend toward agreement instead of pushback, unrelated refactoring, and claiming completion without evidence; existing fixes are scattered across blog posts and tool-specific rules files. This project condenses Karpathy's failure-mode analysis, Boris Cherny's Claude Code workflow, and Anthropic's official guidance into roughly 200 lines that stay short enough for agents to actually follow, following the cross-tool AGENTS.md standard with symlinks for CLAUDE.md and GEMINI.md. Sections 0-9 are fixed behavioral scaffolding; only the project-context section is edited, and a learnings section grows as the user corrects the agent. The file requires no plugin or config for most tools. It targets developers who want baseline senior-engineer behavior from any agent without per-tool setup.
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agents-md.md)
