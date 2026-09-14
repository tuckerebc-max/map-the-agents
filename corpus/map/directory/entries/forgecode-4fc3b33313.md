# ForgeCode (`forgecode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: tailcallhq
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://forgecode.dev/cli | sh
- Model providers: OpenAI, Anthropic, Google Vertex AI, Groq, OpenRouter, Requesty, x-ai, z.ai, Cerebras, Neuralwatt, OrcaRouter, Meta, IO Intelligence, Amazon Bedrock, ForgeCode Services, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [tailcallhq/forgecode](../../repos/tailcallhq/forgecode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): ZSH plugin with colon prefix system (use AI without leaving shell), three-mode architecture (TUI/CLI one-shot/ZSH plugin), semantic code search, conversation management with branching/cloning, sandbox mode via git worktrees, custom agents/skills/commands system, 300+ models.

(captured site page body (agents/forgecode.md), not a verified repo-code finding)
ForgeCode, built by Tailcall HQ, offers three surfaces over one Rust core: an interactive TUI, a one-shot CLI (\`forge -p\` for prompts, \`forge commit\` for AI commit messages, \`forge suggest\` for natural-language shell commands), and a ZSH plugin where colon-prefixed commands invoke agents without leaving the shell. Three built-in agents divide labor — forge implements code, sage researches read-only, muse writes plans — drawing on 300+ models across OpenAI, Anthropic, Google Vertex AI, Bedrock, OpenRouter, Groq, and OpenAI-compatible endpoints. Conversations persist with resume, clone, and compact operations, semantic workspace indexing speeds context assembly, and forge.yaml plus AGENTS.md configure rules and tool limits. A sandboxed git-worktree mode and restricted shell give teams a safety story for daily-driver adoption.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/forgecode.md)
