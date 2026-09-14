# Dippin (`dippin-lang`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent-sdk
- Provider/maker: 2389-research
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=go install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (VS Code extension, LSP server) (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (human gate node type) (yes)
  - plan_mode: yes (branching logic, manager_loop node type) (yes)

Repository map entry: [2389-research/dippin-lang](../../repos/2389-research/dippin-lang.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): DSL and toolchain for authoring AI pipeline workflows with first-class syntax for prompts, shell scripts, model config, branching logic, and node types (agent, tool, human, parallel, subgraph, manager_loop). Ships a full toolchain: parser, validator/linter, formatter, DOT exporter, simulator, cost/coverage analyzers, LSP server, VS Code extension, .dipx packaging, and WASM playground.

(captured site page body (agents/dippin-lang.md), not a verified repo-code finding)
Dippin is a DSL and toolchain for authoring AI pipeline workflows, intended to replace hand-edited Graphviz DOT as the format people actually write and review. Its first-class syntax covers prompts, shell scripts, model config, and branching logic, and its node types — agent, tool, human, parallel, subgraph, and manager_loop — map directly onto the constructs a multi-agent pipeline needs, including human gates and manager loops. A full toolchain ships around the language: parser, validator and linter, formatter, DOT exporter, simulator, cost and coverage analyzers, an LSP server, a VS Code extension, .dipx packaging, and a WASM playground. Dippin describes pipelines; a separate runtime, such as Tracker, executes them. The audience is anyone designing reviewable, version-controlled AI workflows who wants a real language for the job instead of YAML or DOT.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/dippin-lang.md)
