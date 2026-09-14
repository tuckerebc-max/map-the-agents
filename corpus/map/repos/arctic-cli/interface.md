# arctic-cli/interface

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cddbdde2dc95 @ 7cc376ff685e024d

## Summary (orientation draft, not independently verified)

README describes Arctic as a terminal UI for AI coding agents with usage tracking, multi-account support, and provider integrations; CONTRIBUTING.md and STYLE_GUIDE.md document Bun-based development practices.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product tracks real-time usage across coding plans, supports multiple accounts per provider, and allows switching models mid-conversation. -- evidence: [README.md#L11-L14](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L11-L14)
- design-choices (1 claim(s)):
  - [observation/documented] Arctic runs locally and connects directly to the AI provider, storing conversations on the device; it collects anonymous telemetry that can be disabled with `arctic telemetry disable`. -- evidence: [README.md#L64-L64](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L64-L64), [README.md#L66-L68](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L66-L68), [README.md#L50-L50](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L50-L50)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: Arctic is built with Bun 1.3+; contributors fork, clone, run `bun install`, and use `bun dev` to launch the TUI with watch mode on packages/arctic. -- evidence: [CONTRIBUTING.md#L9-L9](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L9-L9), [CONTRIBUTING.md#L22-L27](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L22-L27), [CONTRIBUTING.md#L18-L20](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L18-L20), [CONTRIBUTING.md#L7-L7](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L7-L7)
  - [observation/documented] Repository development practice: the repo is a Turbo-managed monorepo with packages/arctic (SolidJS + OpenTUI CLI/TUI), packages/sdk, and packages/plugin. -- evidence: [CONTRIBUTING.md#L31-L31](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L31-L31), [CONTRIBUTING.md#L33-L35](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L33-L35)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Arctic provides a terminal UI launched with the `arctic` command after a shell-script install and sourcing the shell config. -- evidence: [README.md#L16-L16](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L16-L16), [README.md#L24-L26](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L24-L26), [README.md#L28-L30](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L28-L30), [README.md#L20-L22](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L20-L22)
  - [observation/documented] Supported coding-plan providers include Claude Code, Codex, Gemini CLI, Antigravity, GitHub Copilot, Z.AI, Kimi, Amp Code, Qwen Code, and MiniMax. -- evidence: [README.md#L34-L34](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L34-L34)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Arctic can import existing Claude Code and OpenCode configuration, including custom commands, agents from ~/.claude/agents/, and MCP servers. -- evidence: [README.md#L43-L43](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L43-L43), [README.md#L11-L14](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L11-L14)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](interface.detail.md) for every claim.)

Metadata and full claim list: [full detail](interface.detail.md)
Human notes ([notes](interface.notes.md), never overwritten by build)

[Back to map index](../../index.md)
