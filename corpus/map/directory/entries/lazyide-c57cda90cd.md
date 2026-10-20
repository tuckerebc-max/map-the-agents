# lazyide (`lazyide`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: TysonLabs
- License: MIT
- Language: Rust
- Interface: platforms=CLI, IDE; install=curl -fsSL https://tysonlabs.dev/lazyide/install.sh | sh | brew tap TysonLabs/tap && brew install lazyide | cargo install --git | prebuilt binaries from GitHub Releases
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [tysonlabs/lazyide](../../repos/tysonlabs/lazyide.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight terminal IDE built with Rust and ratatui, distributed as a single binary; full IDE experience in any terminal (ideal for SSH/remote environments); LSP integration (rust-analyzer completions, diagnostics, go-to-definition), syntax highlighting for many languages, code folding, bracket pair colorization, find & replace (regex + ripgrep); 32 themes with live preview, customizable keybindings, tabbed editing, file tree, command palette, autosave & ...

(captured site page body (agents/lazyide.md), not a verified repo-code finding)
Developers working over SSH on remote servers lose their local IDE, and terminal editors with AI agent integration assume more machine context than a remote box offers. lazyide fills that gap as a deliberately agent-free editor: LSP completion and diagnostics via rust-analyzer, syntax highlighting for other languages, git gutter markers, crash-recovering autosave, and a command palette, all in a single ratatui binary that runs anywhere a terminal does. Its own positioning is to pair with an agentic coding tool running alongside it in the terminal. It installs via curl script, Homebrew, Scoop, or cargo, and is MIT-licensed.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/lazyide.md)
