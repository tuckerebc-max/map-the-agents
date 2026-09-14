# fw-ai/fireconnect

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cc1d84179115 @ fd64e0c6a586cbaf

## Summary (orientation draft, not independently verified)

FireConnect is a CLI that routes AI coding harnesses (Claude Code, Codex, OpenCode, Pi, Cursor, VS Code Chat, DeepSeek Harness) through Fireworks by rewriting each tool's own config, with on/off/status commands, model mapping, usage metering, and Azure/Foundry support. Evidence coverage: 131 of 140 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Supported harnesses and config targets: Claude Code (settings.json), Codex (config.toml), OpenCode (opencode.json), Pi (three JSON files), Cursor (state.vscdb SQLite), VS Code Chat (chatLanguageModels.json + state.vscdb), DeepSeek Harness (settings.yaml + .credentials.yaml). -- evidence: [README.md#L96-L104](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L96-L104)
- design-choices (4 claim(s)):
  - [observation/documented] Rather than running a proxy, `on` rewrites each tool's own config, and `off` restores file-based harnesses byte-for-byte from a snapshot under ~/.fireconnect/ while removing only what FireConnect registered in IDEs. -- evidence: [README.md#L106-L108](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L106-L108), [README.md#L7-L8](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L7-L8)
  - [observation/documented] For Claude Code, auth is a static X-Fireworks-Api-Key custom header rather than apiKeyHelper, chosen so a leftover Anthropic key cannot silently break routing; the trade-off is a plaintext key in settings.json at mode 0600. -- evidence: [README.md#L196-L199](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L196-L199), [README.md#L231-L237](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L231-L237)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI is harness-first: `fireconnect <harness> <command>` with per-harness on/off/status/help plus global commands including login, logout, status, model list, configure, upgrade, uninstall, and --version. -- evidence: [README.md#L679-L690](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L679-L690), [README.md#L667-L673](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L667-L673), [README.md#L665-L665](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L665-L665), [README.md#L663-L663](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L663-L663)
  - [observation/documented] Claude Code subcommands include usage (interactive meter or --plain/--json snapshots), live (tmux split with a live usage meter), and demo (racing two models on a prompt). -- evidence: [README.md#L144-L148](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L144-L148), [README.md#L129-L140](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L129-L140), [README.md#L675-L675](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L675-L675)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Installation requires bash and Node.js 18+, clones the CLI to ~/.fireconnect/cli, and installs a launcher into ~/.local/bin; on Windows it must be run from Git Bash. -- evidence: [README.md#L85-L86](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L85-L86), [README.md#L77-L83](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L77-L83)
- limitations (2 claim(s)):
  - [observation/documented] MiniMax is not supported on Codex because Codex may insert assistant messages between tool_calls and tool_results, which MiniMax chat templates reject; FireConnect fails that model choice with an explanation. -- evidence: [README.md#L362-L365](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L362-L365)
More evidence: [full detail](fireconnect.detail.md)

Metadata and full claim list: [full detail](fireconnect.detail.md)
Human notes ([notes](fireconnect.notes.md), never overwritten by build)

[Back to map index](../../index.md)
