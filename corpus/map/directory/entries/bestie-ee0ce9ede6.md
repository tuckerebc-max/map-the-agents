# Bestie (`bestie`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: jolexxa
- License: MPL-2.0
- Language: Dart
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/jolexxa/bestie/main/install.sh | bash (downloads the latest release for your platform to ~/.local/bin); Windows needs Developer Mode plus a one-time elevation prompt for sandbox provisioning
- Model providers: Fireworks AI, OpenRouter, any OpenAI-compatible server
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: False (reported)

Repository map entry: [jolexxa/bestie](../../repos/jolexxa/bestie.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A native terminal coding agent in Dart whose selling point is total visibility — a details pane showing inputs and outputs for every action — with a cross-platform sandbox (wide reads, limited writes, configurable network levels), subagents, background jobs, compaction, and pull-based handling of long outputs.

(captured site page body (agents/bestie.md), not a verified repo-code finding)
Bestie is a native terminal coding-agent harness by Joanna May, written in Dart and built as a Flutter-style layered package set (domain, data, infra, use cases, view). Its stated purpose is visibility: a details pane shows the inputs and outputs of every action the agent takes, so, in the author's words, Bestie can't sneak anything past you — the product is for people who want total power over robots. The agent loop invokes its own tools through isolate-backed worker pools with parallel execution: filesystem create/edit tools for text, a sandboxable bash environment for everything else, web search and fetch (using curl-impersonate to dodge captchas), plus calculator, date-time, Wikipedia, and arXiv utilities. Sandboxing is cross-platform — wide read access with writes limited to the working directory and configurable network access levels — with a Windows 10-compatible approach that trades a one-time elevation prompt for simplicity. Subagents are focused workers spawned to finish one self-contained task and report back (they cannot spawn further subagents), and long-running work uses a pull-based paradigm where jobs notify the agent and it pulls the report. Sessions save and load, compaction happens automatically or on demand, and a built-in terminal emulator/multiplexer, command palette, themes, and mascot characters round out the TUI. Providers are Fireworks AI, OpenRouter, and any OpenAI-compatible server, configured through a JSON-schema'd config file or a visual options menu. The project is explicitly alpha ('brand new and should ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/bestie.md)
