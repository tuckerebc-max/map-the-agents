# PurrCode (`purrcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Weilin0723
- License: Apache-2.0
- Language: Rust
- Interface: install=curl -fsSL https://raw.githubusercontent.com/Weilin0723/PurrCode/v1.0.0/scripts/install.sh | sh; or npm install --global @minaovo/purrcode; or cargo build --release (Rust 1.88+)
- Model providers: Ollama, LM Studio, NVIDIA NIM, remote providers via /connect
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [weilin0723/purrcode](../../repos/weilin0723/purrcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Judgment-first local-first coding agent runtime where model output is treated as a proposal, never authority; durable authorization + recorded validation for every native action; native pure-Rust desktop IDE (no browser/Electron/VS Code); works in isolated git worktrees; evidence-based model selection with budget enforcement; /mode switches between Ask, Plan, Build, Review.

(captured site page body (agents/purrcode.md), not a verified repo-code finding)
PurrCode starts from the position that model output is a proposal and never authority: repository content, downloaded skills, and generated code are all untrusted until a separate authorization layer approves each action, re-checks that approval immediately before execution, and records the validation afterward. Permission modes are daemon-enforced constraints rather than prompt-level politeness, so a read-only mode genuinely prevents writes, and sandboxing via sandbox-exec or Bubblewrap is reported honestly rather than oversold. Agent work runs in detached Git worktrees so uncommitted user work is never silently stashed or overwritten. A pure-Rust desktop IDE built on egui shares one daemon-owned session with the terminal TUI, letting a task move between interfaces without losing state. Local-first operation connects to Ollama or LM Studio by default with NVIDIA NIM as a first-class cloud option, and credentials stay in the OS keychain, never in model context. Developers who want a security-enforced local agent rather than a prompt-level one use PurrCode.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/purrcode.md)
