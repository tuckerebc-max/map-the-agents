# byob (`byob`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: Scronkfinkle
- License: MIT OR Apache-2.0
- Language: Rust
- Interface: platforms=CLI, Desktop; install=cargo install byob (browser UI built in); cargo install byob --no-default-features (slim); nix build github:Scronkfinkle/byob; or release archives (.tar.gz/.dmg) from GitHub Releases for Linux, macOS, and Windows
- Model providers: Any OpenAI-compatible endpoint (llama-server, Ollama, LM Studio, vLLM, or a hosted API) plus Claude over Anthropic's Messages API; tool calling falls back to prompt-based calls when the server has none
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [scronkfinkle/byob](../../repos/scronkfinkle/byob.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A native GPU-drawn desktop AI coworker with no Electron and no bundled inference — point it at any model endpoint you run and it reads and writes files, runs commands and sandboxed Python, and builds spreadsheets, charts, documents, and HTML apps beside the chat, where every feature (prompt, core tools, artifacts, subagents, plan, even compaction) is a bundled plugin on ...

(captured site page body (agents/byob.md), not a verified repo-code finding)
byob — Bring Your Own Brain — is a local-first desktop coworker for people who already run a model: no bundled inference and no account, just any OpenAI-compatible URL or Claude over Anthropic's Messages API, with first-run auto-discovery of local servers on their usual ports and per-model settings for context window, temperature, and extra request JSON. It is one native Rust program that draws its own interface on the GPU with no Electron (~60 MB download, 13 MB slim), and the same interface compiled to WebAssembly serves a browser tab or a phone on the live session through byob --serve or tailscale. Around the chat it builds artifacts — spreadsheets that recalculate and report errors back to the model, charts linked to sheets that redraw when data moves, Markdown documents, images, and HTML apps rendered inline by a bundled Servo process — while file tools, run_command, and sandboxed run_python carry an approval-card, diff-per-turn, undo-per-turn workflow, with a YOLO mode that drops the approvals. The defining design choice is that everything is a plugin on one API: the prompt, core tools, artifacts, appearance, and even the appearance-changing ui_look tool ship as ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/byob.md)
