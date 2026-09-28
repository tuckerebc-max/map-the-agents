# Blinky (`blinky`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: seahyinghang8
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=Install Blinky VSCode extension from the VSCode marketplace
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [seahyinghang8/blinky](../../repos/seahyinghang8/blinky.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI debugging agent for VSCode inspired by SWE-agent; embeds a debugging loop directly inside VSCode for real-time developer feedback mid-run; LSP-based navigation tools (GoToDefinition, GetAllReferences, GetFilesRelevantToEndpoint); match-and-replace file editing technique (generating original text with line numbers) to reduce LLM hallucination and indentation errors; Verify tool runs user-specified repro steps and uses execution feedback to iteratively debug until tests pass; ...

(captured site page body (agents/blinky.md), not a verified repo-code finding)
Blinky brings the SWE-agent debugging loop into the editor rather than the terminal, targeting backend developers who want an agent that fixes bugs in place. A user describes a bug plus optional reproduction steps; the agent iterates — reading code through LSP-derived tools like GoToDefinition and GetAllReferences, editing via a match-and-replace scheme that forces the model to re-emit the original text to catch hallucinations — until a user-specified Verify step passes. Because it runs in VS Code, feedback can arrive mid-run, and the developer watches the loop rather than waiting for a batch result. The project is small and early-stage: seven commits, an MIT-licensed TypeScript extension on the marketplace, OpenAI as the only provider, and a roadmap (more models, broader codebase support) that has not progressed since mid-2024. It remains a reference implementation of editor-embedded debugging loops more than a daily-driver tool.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/blinky.md)
