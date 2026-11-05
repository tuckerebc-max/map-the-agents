# Sprout (`sprout`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: prime-radiant-inc
- License: Proprietary
- Language: TypeScript
- Interface: platforms=CLI, Web; install=git clone https://github.com/prime-radiant-inc/sprout && cd sprout && bun install
- Model providers: Anthropic, OpenAI, OpenAI Codex, Google
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [prime-radiant-inc/sprout](../../repos/prime-radiant-inc/sprout.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A recursive coding agent whose root never calls a tool itself: every action is a delegation to a specialist subagent, and repeated failures trigger an async learning pass that mutates a git-backed agent genome.

(captured site page body (agents/sprout.md), not a verified repo-code finding)
Sprout is an experiment in pushing delegation to its limit. A root agent takes a goal, breaks it into subgoals, and hands each to a specialist; specialists can delegate further, so only leaf agents ever touch the eight immutable kernel primitives (read_file, write_file, edit_file, apply_patch, exec, grep, glob, fetch). A verifier and a debugger check work before it lands, and a quartermaster meta-agent can answer what exists, plan how to do something, or fabricate a new specialist at runtime, which is how the roster grows. Stumbles, timeouts, and retries are detected automatically: three repeats of the same mistake or two unresolved errors trigger an asynchronous learning pass that mutates the agent genome, a git-backed store of agent definitions, memories, and routing rules where every change is committed for audit and rollback. Agents talk over a WebSocket pub/sub bus and can run as separate processes; the whole thing runs as an Ink terminal UI or a browser UI on port 7777, maps abstract model tiers onto Anthropic, OpenAI, OpenAI Codex, and Google, and reaches MCP servers through a bundled client. The README reports a 3.7% average stumble rate across 2,201 tracked sessions, and is honest that this is early-stage work aimed at developers curious about recursive multi-agent architectures rather than anyone wanting a finished product.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/sprout.md)
