# arctic-cli/interface -- full detail

[Back to orientation](interface.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/arctic-cli/interface/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/7cc376ff685e024d.json](../../../wiki/dossiers/arctic-cli/interface/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/7cc376ff685e024d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product tracks real-time usage across coding plans, supports multiple accounts per provider, and allows switching models mid-conversation. -- evidence: [README.md#L11-L14](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L11-L14) (`clm_75fb28875c3b4d5ff1f6b6d49361396a282f997681e36df9c5e5cf1fea0273af`)

## design-choices (1 claim(s))

- [observation/documented] Arctic runs locally and connects directly to the AI provider, storing conversations on the device; it collects anonymous telemetry that can be disabled with `arctic telemetry disable`. -- evidence: [README.md#L64-L64](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L64-L64), [README.md#L66-L68](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L66-L68), [README.md#L50-L50](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L50-L50) (`clm_36aa835eccbeb33de090fd1f65b020c4fd5dcf74b5e29ce602d8ee9541f9a189`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: Arctic is built with Bun 1.3+; contributors fork, clone, run `bun install`, and use `bun dev` to launch the TUI with watch mode on packages/arctic. -- evidence: [CONTRIBUTING.md#L9-L9](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L9-L9), [CONTRIBUTING.md#L22-L27](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L22-L27), [CONTRIBUTING.md#L18-L20](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L18-L20), [CONTRIBUTING.md#L7-L7](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L7-L7) (`clm_68847aafb4bb5a08e5ee058141eab19510ebf429e1ecb2cce38a78183913fdf4`)
- [observation/documented] Repository development practice: the repo is a Turbo-managed monorepo with packages/arctic (SolidJS + OpenTUI CLI/TUI), packages/sdk, and packages/plugin. -- evidence: [CONTRIBUTING.md#L31-L31](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L31-L31), [CONTRIBUTING.md#L33-L35](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L33-L35) (`clm_84fffc88538dd6ebcbbaf5caac2585ee570676bd4865b9a207bf2398d2a9be84`)
- [observation/documented] Repository development practice: contributors run tests with `bun test`, follow a strict style guide (prefer const over let, avoid else/try-catch, use Bun APIs), and submit PRs with clear descriptions. -- evidence: [CONTRIBUTING.md#L52-L54](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L52-L54), [CONTRIBUTING.md#L43-L46](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L43-L46), [STYLE_GUIDE.md#L3-L12](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/STYLE_GUIDE.md#L3-L12), [CONTRIBUTING.md#L50-L50](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L50-L50), [CONTRIBUTING.md#L58-L61](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L58-L61) (`clm_91fbf3db59b66202a7eaa7ea85c8605f12ae2825416f645d8ec8eebb1420dbdd`)
- [observation/documented] Repository development practice: contributions are licensed under the project's MIT License. -- evidence: [CONTRIBUTING.md#L65-L65](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/CONTRIBUTING.md#L65-L65) (`clm_d3687719cd8967fa1b640a25a13dfe8074193568cf41636d95944ec5155d737c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Arctic provides a terminal UI launched with the `arctic` command after a shell-script install and sourcing the shell config. -- evidence: [README.md#L16-L16](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L16-L16), [README.md#L24-L26](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L24-L26), [README.md#L28-L30](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L28-L30), [README.md#L20-L22](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L20-L22) (`clm_98dcd33969fd5bc2764bd01a70073c184fd0439c9fb9a471540fb3e5148a7a76`)
- [observation/documented] Supported coding-plan providers include Claude Code, Codex, Gemini CLI, Antigravity, GitHub Copilot, Z.AI, Kimi, Amp Code, Qwen Code, and MiniMax. -- evidence: [README.md#L34-L34](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L34-L34) (`clm_f45e44376081066ce05d24b04aaad65cf5bc56b68a3725465c607dc7147669e6`)
- [observation/documented] API-key support is documented for OpenAI, Anthropic, Google, Perplexity, Openrouter, Ollama, and more. -- evidence: [README.md#L36-L36](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L36-L36), [README.md#L57-L57](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L57-L57) (`clm_911156b2441482c831399754fd6d9e680fe03f40a9dabb74fcb44d9690b329ca`)
- [observation/documented] A `arctic telemetry status` command reports the current telemetry state. -- evidence: [README.md#L72-L74](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L72-L74), [README.md#L70-L70](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L70-L70) (`clm_9b1c718baee70fd4ae25bdbb3b8dd15815a0ad70b63f7bc3c6b38f58825ecd84`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Arctic can import existing Claude Code and OpenCode configuration, including custom commands, agents from ~/.claude/agents/, and MCP servers. -- evidence: [README.md#L43-L43](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L43-L43), [README.md#L11-L14](https://github.com/arctic-cli/interface/blob/cddbdde2dc9586a35ad311b9e8bd83c0187144ae/README.md#L11-L14) (`clm_5c7feda44509064245b8bfd1c02d82823e959cd96ed24a6b71140f919da096ce`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

