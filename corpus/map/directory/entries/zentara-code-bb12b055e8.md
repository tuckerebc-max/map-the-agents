# Zentara-Code (`zentara-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Zentar-Ai
- License: Apache-2.0
- Language: TypeScript
- Interface: install=VS Code Marketplace (search 'Zentara Code'); from source: pnpm install && pnpm vsix
- Model providers: Claude (Anthropic)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [zentar-ai/zentara-code](../../repos/zentar-ai/zentara-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): VS Code extension AI coding assistant and debugger, a mod/fork of Roo-Code (which derives from Cline). Features parallel subagents with isolated contexts, 25+ LSP semantic tools, runtime debugging with 35+ operations (launch, step, breakpoints, state inspection), plan/approve/execute/verify workflow, tool integration for custom extensions, and /init project analysis command. Optimized for speed, safety, and correctness via parallel execution and LSP semantics.

(captured site page body (agents/zentara-code.md), not a verified repo-code finding)
Zentara-Code addresses a gap in chat-driven coding assistants: they can write code but cannot observe it executing, so verification rests on assumptions. Built as a fork of Roo-Code (which descends from Cline), the extension exposes the debugger to the agent — launch and restart sessions, conditional and temporary breakpoints, stepping, stack and variable inspection, and expression evaluation, roughly 35 operations in total. Code intelligence rides the Language Server Protocol rather than text matching, giving the agent semantic usages, call hierarchies, safe renames, and workspace symbol search across 25+ tools. Work follows an explicit pipeline: the agent decomposes a request into steps and proposes an execution order, the user approves impactful actions, parallel subagents with isolated contexts and opt-in write permissions handle independent pieces, and a verification pass exercises the result in the debugger. Custom agent definitions and modes are configurable through project files, and an /init command analyzes a codebase to generate AI-friendly documentation. The extension is free under Apache-2.0, installed from the VS Code Marketplace, with a Claude Max subscription recommended for model access; teams adopting it tend to be those debugging behavior where static chat suggestions repeatedly miss.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zentara-code.md)
