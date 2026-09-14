# Gambit (`gambit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: bolt-foundry
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npx @bolt-foundry/gambit (no install); Deno via jsr:@bolt-foundry/gambit
- Model providers: OpenRouter (default), Claude Code CLI, Codex CLI, custom providers
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry (renamed): original lead [bolt-foundry/gambit](https://github.com/bolt-foundry/gambit) (source: backing, field: `source_code_url`) now resolves to [getworkloop/gambit](../../repos/getworkloop/gambit.md) (github id 1101529500, verified [https://github.com/getworkloop/gambit](https://github.com/getworkloop/gambit)).

## Description

Highlight (site page `what_makes_it_special`): Builds the evidence layer for agent systems: generate and quality-validate realistic scenarios, run any agent against them, grade transcripts from JSONL traces, and promote failures into regression suites gated in CI.

(captured site page body (agents/gambit.md), not a verified repo-code finding)
Teams shipping agent features lack a systematic way to prove they work, so Bolt Foundry built Gambit around scenario generation, grading, and regression. Agents under test — whether Mastra, LangGraph, OpenAI Agents SDK, or custom stacks — are exercised through one-shot runs, a REPL, or a browser chat with full traces, while Gambit's own 'deck' agents are defined in Markdown or TypeScript with Zod schemas. Grading turns transcripts into pass/fail evidence, and a GitHub Actions example shows scenario grades acting as PR gates. Agents compose through child actions and ctx.spawnAndWait, OpenRouter is the default provider with Claude Code and Codex CLIs as alternative runtimes, and the repository has moved from bolt-foundry to the coworkerprotocol-org.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gambit.md)
