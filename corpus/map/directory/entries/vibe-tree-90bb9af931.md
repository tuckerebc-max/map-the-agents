# vibe-tree (`vibe-tree`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: sahithvibudhi
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Desktop, Web; install=macOS: brew install --cask --no-quarantine sahithvibudhi/tap/vibetree; Windows/Linux: download installer; From source: pnpm install then pnpm dev:desktop
- Model providers: Claude Code, OpenAI Codex CLI, Gemini CLI, Aider, opencode, any terminal-based agent CLI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [sahithvibudhi/vibe-tree](../../repos/sahithvibudhi/vibe-tree.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Every AI coding task gets its own isolated git worktree with its own branch and persistent terminal, enabling true parallel agent execution without agents stomping on each other. Supports any terminal-based agent CLI. Usable as desktop app or browser-accessible server (including phone access via QR pairing). One-click disposal of failed experiments.

(captured site page body (agents/vibe-tree.md), not a verified repo-code finding)
Running several AI agents against one checkout means merge conflicts and clobbered edits, and terminal-based agents die when a window closes. VibeTree gives every task an isolated git worktree with its own branch and a persistent terminal whose scrollback survives reloads and reconnects, so parallel agents never stomp on each other and long-running sessions survive reconnects. A fleet view shows which agents are working, waiting, or done (with a chime when one needs attention), a changes view puts the diff beside the terminal so a comment can be sent back as the agent's next prompt, and dev-server URLs are detected for browser preview. Because it hosts real terminals, it works with claude, codex, gemini, aider, or any shell command, and a standalone server mode adds phone access via QR pairing. Developers running parallel agent tasks use it as a desktop app or self-hosted server; it is MIT-licensed and actively maintained.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/vibe-tree.md)
