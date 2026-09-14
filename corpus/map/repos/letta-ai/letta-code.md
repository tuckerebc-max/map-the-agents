# letta-ai/letta-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f2bd2392a824 @ 28b1a65f09718697

## Summary (orientation draft, not independently verified)

Evidence covers Letta Code's README (agent harness with memory, skills, subagents, remote computers, CLI/desktop/browser interfaces), example mods and a mod-learning harness, Nix packaging docs, an AI contribution policy, and two internal plan documents. No source code is included, so most claims are documentation-based.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The example memory-citations mod is intentionally conservative: it observes memory paths passed to tools at tool_start (before execution), not successful reads, and marks shell-command matches as medium confidence. -- evidence: [docs/examples/mods/README.md#L12-L16](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L12-L16), [docs/examples/mods/README.md#L18-L20](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L18-L20)
  - [observation/documented] The /mods learn TUI command never auto-installs learned mods; users must review the generated candidate before copying it into their mod directory and running /reload. -- evidence: [docs/examples/mods/README.md#L46-L49](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L46-L49)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the AI policy requires contributors to disclose all AI tool usage in issues and PRs, select an authorship option, include a human-verification phrase, and noncompliant submissions are automatically closed. -- evidence: [AI_POLICY.md#L19-L22](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L19-L22), [AI_POLICY.md#L24-L24](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L24-L24), [AI_POLICY.md#L5-L5](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L5-L5), [AI_POLICY.md#L9-L13](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L9-L13)
  - [observation/documented] Repository development practice: when bun.lock changes, contributors should regenerate the Nix dependency expression with `bunx bun2nix -o bun.nix` before opening a PR. -- evidence: [docs/nix.md#L97-L97](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/nix.md#L97-L97), [docs/nix.md#L99-L101](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/nix.md#L99-L101)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills load from global (~/.letta), project-scoped (.agents/skills), and agent-scoped (MemFS) locations, and can be installed from GitHub, ClawHub, or Hermes Skills Hub with `letta skills install`. -- evidence: [README.md#L103-L107](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L103-L107), [README.md#L101-L101](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L101-L101), [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32)
- interfaces (3 claim(s)):
  - [observation/documented] Letta Code is distributed as the npm package @letta-ai/letta-code, installed globally via npm, and run with the `letta` command in a project directory. -- evidence: [README.md#L40-L42](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L40-L42), [README.md#L38-L38](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L38-L38), [README.md#L3-L3](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L3-L3), [README.md#L44-L47](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L44-L47)
  - [observation/documented] Agents can be interacted with through a local CLI, a desktop app for macOS/Windows/Linux, a browser client at chat.letta.com, and messaging integrations such as Telegram, Slack, and Discord. -- evidence: [README.md#L7-L11](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L7-L11)
- memory-state (2 claim(s)):
  - [observation/documented] Agent context, including memory blocks, is tracked via git under MemFS and can be synced to a user's GitHub repository via /memory-repository set. -- evidence: [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32)
  - [observation/documented] Agents rewrite their own context over time, including system-prompt learning via memory blocks and skill learning, with periodic 'dreaming' configurable via /sleeptime. -- evidence: [README.md#L5-L5](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L5-L5), [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32)
- orchestration (2 claim(s)):
  - [observation/documented] Built-in subagents (general-purpose, forked, recall, history-analyzer) can run in the background, and agents can call any other agent, including themselves, as subagents. -- evidence: [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32)
More evidence: [full detail](letta-code.detail.md)

Metadata and full claim list: [full detail](letta-code.detail.md)
Human notes ([notes](letta-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
