# standardagents/dmux -- full detail

[Back to orientation](dmux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/standardagents/dmux/8cb3d926631a9349ab67f7ece41d218427ac7e24/68485dfe5f603c6d.json](../../../wiki/dossiers/standardagents/dmux/8cb3d926631a9349ab67f7ece41d218427ac7e24/68485dfe5f603c6d.json)

## specifications (1 claim(s))

- [observation/documented] dmux manages multiple AI coding agents in parallel, giving each task a tmux pane backed by its own isolated git worktree and branch, with merge or GitHub PR actions to bring work back. -- evidence: [README.md#L7-L10](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L7-L10), [README.md#L47-L47](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L47-L47) (`clm_1fd614cc3c0aa6da097b4ddff74c6cdfdf6c90e08d40e958ebd47715400d9b9a`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Each pane is a full working copy in its own worktree so agents do not conflict; merging auto-commits, merges, and cleans up in one step. -- evidence: [README.md#L49-L60](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L49-L60), [README.md#L47-L47](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L47-L47) (`clm_30ebe052a252f4f3d418e66abc46856e4df763a60814ec8cd706a230d16b190c`)
- [observation/documented] Branch handling defaults to automatic worktree/branch naming, but users can optionally pick a different base branch per pane or supply an explicit name, with agent-specific suffixes for multi-agent launches. -- evidence: [README.md#L66-L69](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L66-L69), [README.md#L64-L64](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L64-L64) (`clm_ad52f889b36563b378c4d8e21d39598c8fbd65f030586f6ad710404c5dedba7f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: maintainers use a 'dmux-on-dmux' loop via pnpm dev, and the recommended PR workflow runs pnpm run typecheck and pnpm run test before submitting. -- evidence: [AGENTS.md#L169-L172](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/AGENTS.md#L169-L172), [AGENTS.md#L109-L109](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/AGENTS.md#L109-L109), [AGENTS.md#L174-L177](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/AGENTS.md#L174-L177) (`clm_03d1cda9d0f4667c59638b15cdc530df60a442a727fac112811de53219a744d8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The TUI exposes single-key shortcuts: n for a new worktree pane, t for a terminal pane, m for the pane menu, f for file browsing, s for settings, and q to quit, among others. -- evidence: [README.md#L73-L86](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L73-L86) (`clm_31fa6019a9afaeb2a140f3728cfda459cc486dbe77acef77d1f279fe087c33fe`)
- [observation/documented] dmux supports launching many agent CLIs, including Claude Code, Codex, OpenCode, Cline, Gemini, Qwen, Amp, pi, Cursor, Copilot, and Crush, with multi-select of several agents per prompt. -- evidence: [README.md#L49-L60](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L49-L60) (`clm_25f1318024e3c5f39e490b50c2837f71d733d0fc13fae68b439dfd79956b8413`)
- [observation/documented] First-run setup can configure a primary inference provider and optional backup, discovering models from the provider and supporting API keys, custom OpenAI-compatible endpoints, or Codex/Grok Build logins; reopened via the settings key. -- evidence: [README.md#L43-L43](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L43-L43) (`clm_0ca2535e9cd3aefa16624b70b766816eb9d102ca625e13b0048fdbce44f7a110`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime requirements are tmux 3.0+, Node.js 18+, Git 2.20+, at least one supported agent CLI, and optionally an inference provider key or Codex/Grok Build login for AI naming and analysis. -- evidence: [README.md#L90-L94](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L90-L94) (`clm_de5e65aff50500448b78c8245d5fd64dad7ecafc4096a7681d7e636491bca986`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

