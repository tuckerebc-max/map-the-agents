# softeria/postmortemthis

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 37f38fea5a62 @ cd1cf2daf51dc0f0

## Summary (orientation draft, not independently verified)

The snapshot contains only README content describing postmortemthis, a shell script that runs one review prompt across multiple coding-agent CLIs in parallel, with setup/auth via OpenRouter. No source code is present in the evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product is described as a single small script that installs, updates, and runs all the agents on Windows, macOS, and Linux, with no server or MCP required. -- evidence: [README.md#L11-L11](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L11-L11)
- design-choices (2 claim(s)):
  - [observation/documented] Grok is run through an OpenAI-compatible harness against the OpenRouter model x-ai/grok-build-0.1, since Grok's own CLI cannot reach OpenRouter. -- evidence: [README.md#L30-L30](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L30-L30)
  - [observation/documented] The design keeps the user inside their own agent, which makes the final call, while the external agents only read the diff; the script is described as the only fixed part of the system. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9), [README.md#L24-L24](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L24-L24)
- workflows (1 claim(s)):
  - [observation/documented] A `setup` command probes each agent, lets the user log in, force OpenRouter, or disable an agent, optionally fires a test prompt, and saves the choices for later runs. -- evidence: [README.md#L32-L32](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L32-L32)
- skills-patterns (1 claim(s)):
  - [observation/documented] Installation is prompt-driven: the user pastes a prompt that makes their coding agent create a /postmortemthis skill, downloading the .cmd script once into the skill folder; the repo's SKILL.md is described as a starting point. -- evidence: [README.md#L24-L24](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L24-L24), [README.md#L17-L20](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L17-L20)
- interfaces (1 claim(s)):
  - [observation/documented] The tool is invoked as a shell script: piping a prompt to `sh postmortemthis.cmd` runs it across all agents, with `setup` and `doctor` subcommands for configuration and availability checks. -- evidence: [README.md#L36-L40](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L36-L40)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] It runs one prompt across several coding-agent CLIs (Claude Code, Codex, Antigravity, Qwen, Vibe, Grok) in parallel, each reading the current diff. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9), [README.md#L17-L20](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L17-L20)
- tools-permissions (1 claim(s)):
  - [observation/documented] Read-only operation is enforced by each agent's own CLI, except Antigravity which lacks such a switch and is instead constrained via its plan mode; the user is notified if the tree changes during a run. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The tool depends on the user's installed coding-agent CLIs and their logins; for agents without access, OpenRouter is used via OAuth login or an OPENROUTER_API_KEY, with usage billed to the user's account. -- evidence: [README.md#L28-L28](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L28-L28)
More evidence: [full detail](postmortemthis.detail.md)

Metadata and full claim list: [full detail](postmortemthis.detail.md)
Human notes ([notes](postmortemthis.notes.md), never overwritten by build)

[Back to map index](../../index.md)
