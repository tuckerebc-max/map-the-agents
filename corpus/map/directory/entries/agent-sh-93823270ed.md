# agent-sh (`agent-sh`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: guanyilun
- License: MIT
- Language: TypeScript
- Interface: install=npm install -g agent-sh (requires Node.js 18+; supports bash, zsh, fish; not native Windows, use WSL)
- Model providers: OpenRouter, OpenAI, DeepSeek, Ollama
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [guanyilun/agent-sh](../../repos/guanyilun/agent-sh.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Composable agent runtime pairing any frontend (shell, TUI, GUI) with any agent backend over one shared extension layer. A pure kernel (typed event bus + handler registry + extension loader) sits at the center, knowing nothing about terminals, LLMs, shells, or rendering. The bundled frontend is a shell where typing \> invokes an agent that already sees your cwd, last ...

(captured site page body (agents/agent-sh.md), not a verified repo-code finding)
Most terminal AI tools weld one frontend to one backend, so switching providers means switching tools; agent-sh instead separates the shell from the agent entirely. Its kernel is a typed event bus with a handler registry and extension loader that knows nothing about terminals, LLMs, or rendering, and the default frontend is a working bash/zsh/fish shell where a \> prompt prefix hands the conversation to an agent that sees your current directory, last command, and its output. Built-in bridges let the same setup drive pi, claude-code, or opencode backends, and extensions add tools, slash commands, and themes over the event bus. It is MIT-licensed, installable via npm, and aimed at terminal-first developers who want their agent choice decoupled from their shell.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agent-sh.md)
