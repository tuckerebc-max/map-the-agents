# mini-coding-agent (`mini-coding-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: rasbt
- License: Apache-2.0
- Language: Python
- Interface: install=binary
- Model providers: Ollama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [rasbt/mini-coding-agent](../../repos/rasbt/mini-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Intentionally minimal and readable coding agent harness designed for educational purposes to explain the six core components of a coding agent (live repo context, prompt cache reuse, structured tools/permissions, context reduction, transcripts/memory/resumption, bounded subagents). No runtime dependencies beyond the Python standard library. Runs locally via Ollama.

(captured site page body (agents/mini-coding-agent.md), not a verified repo-code finding)
Raschka wrote mini-coding-agent as the runnable companion to his essay on the components of a coding agent, with the constraint that the entire harness fit in one readable file with no dependencies beyond the Python standard library. The loop sends prompts to a local Ollama model (qwen3.5:4b by default) that must answer with either a tool call or a final answer; tools cover repo-context gathering, file operations, and shell commands, each validated and gated by an approval mode (ask, auto, never) so risky actions require consent. The implementation demonstrates the standard efficiency patterns directly: a stable prompt prefix for cache reuse, clipped outputs and deduplicated reads for context reduction, durable transcripts with distilled working memory, and subagents scoped to bounded subtasks. Sessions persist under .mini-coding-agent/sessions and resume by ID. Readers use it alongside the essay to understand agent internals rather than to ship code with it — fifteen commits and a default six-step cap signal its educational scope.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mini-coding-agent.md)
