# fw-ai/fireconnect -- full detail

[Back to orientation](fireconnect.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fw-ai/fireconnect/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/fd64e0c6a586cbaf.json](../../../wiki/dossiers/fw-ai/fireconnect/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/fd64e0c6a586cbaf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Supported harnesses and config targets: Claude Code (settings.json), Codex (config.toml), OpenCode (opencode.json), Pi (three JSON files), Cursor (state.vscdb SQLite), VS Code Chat (chatLanguageModels.json + state.vscdb), DeepSeek Harness (settings.yaml + .credentials.yaml). -- evidence: [README.md#L96-L104](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L96-L104) (`clm_7fd2dbc90513889ad66bc4434fec5c18104dcf3fbb04a79fddbab7b2d16b79be`)

## design-choices (4 claim(s))

- [observation/documented] Rather than running a proxy, `on` rewrites each tool's own config, and `off` restores file-based harnesses byte-for-byte from a snapshot under ~/.fireconnect/ while removing only what FireConnect registered in IDEs. -- evidence: [README.md#L106-L108](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L106-L108), [README.md#L7-L8](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L7-L8) (`clm_667a582ca1410fc6655ba2867f62edb7530f5942d9cd2e5a673bd95663ddf27f`)
- [observation/documented] For Claude Code, auth is a static X-Fireworks-Api-Key custom header rather than apiKeyHelper, chosen so a leftover Anthropic key cannot silently break routing; the trade-off is a plaintext key in settings.json at mode 0600. -- evidence: [README.md#L196-L199](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L196-L199), [README.md#L231-L237](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L231-L237) (`clm_360543b1558aa281bd507f88b21e604793c469d1261dc738c6d72fd48dcf6e5b`)
- [observation/documented] Model IDs get a [1m] suffix when the resolved context window is at least 1M tokens, so Claude Code sizes the window correctly and strips the tag before requests; the tag applies to Claude Code only. -- evidence: [README.md#L253-L265](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L253-L265) (`clm_066eac8f9d884f6d06f1234a7fb82aba444944e039669f1f233d082518f6ebd3`)
- [observation/documented] The installed statusLine recomputes session cost from the transcript at Fireworks rates (Claude Code's own estimate uses Anthropic list prices), showing a bar sized by each model's share of spend plus per-model cost and cache-hit rate; NO_COLOR strips it to plain text. -- evidence: [README.md#L297-L305](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L297-L305), [README.md#L321-L326](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L321-L326), [README.md#L328-L335](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L328-L335) (`clm_c848619cdc525f0429c873093694a68f279b55dc89d96e79c565b5aa3e9a3be7`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI is harness-first: `fireconnect <harness> <command>` with per-harness on/off/status/help plus global commands including login, logout, status, model list, configure, upgrade, uninstall, and --version. -- evidence: [README.md#L679-L690](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L679-L690), [README.md#L667-L673](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L667-L673), [README.md#L665-L665](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L665-L665), [README.md#L663-L663](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L663-L663) (`clm_0f41e9c95530b0786ac2c41507687213c516e53166cb018bbf687ed31c1c40cf`)
- [observation/documented] Claude Code subcommands include usage (interactive meter or --plain/--json snapshots), live (tmux split with a live usage meter), and demo (racing two models on a prompt). -- evidence: [README.md#L144-L148](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L144-L148), [README.md#L129-L140](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L129-L140), [README.md#L675-L675](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L675-L675) (`clm_5b315f9ccf939448d2a0043b9db8cfab133ef4e5ce9557e3473415ab28ea9c5d`)
- [observation/documented] Claude Code model mapping is configured via an interactive wizard (--interactive), per-slot flags (--model, --opus, --sonnet, --haiku, --fable, --subagent), or --non-interactive saved prefs for CI and scripts. -- evidence: [README.md#L174-L178](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L174-L178), [README.md#L160-L160](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L160-L160), [README.md#L163-L165](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L163-L165), [README.md#L168-L169](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L168-L169) (`clm_91ca06e224f79165e53ab9e6dd4f8d961d12a2119fbcdd6d31cb0a321da78de3`)
- [observation/documented] Azure/Microsoft Foundry mode routes OpenCode, Codex, Pi, Cursor, and VS Code through an OpenAI-compatible Foundry endpoint using deployment names as model IDs; Claude Code is excluded because Foundry does not expose the Anthropic Messages API. -- evidence: [README.md#L636-L645](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L636-L645), [README.md#L610-L614](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L610-L614), [README.md#L657-L659](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L657-L659) (`clm_5ff796ae2b21e3ed17ab0dfe6c404821903d201b3b301ea1a0a0e55053299ff6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation requires bash and Node.js 18+, clones the CLI to ~/.fireconnect/cli, and installs a launcher into ~/.local/bin; on Windows it must be run from Git Bash. -- evidence: [README.md#L85-L86](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L85-L86), [README.md#L77-L83](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L77-L83) (`clm_c5b8a74b015fadefb3601c744a37cb67b55b44df81b0ee2fde1fe0d7c2e27f19`)

## limitations (2 claim(s))

- [observation/documented] MiniMax is not supported on Codex because Codex may insert assistant messages between tool_calls and tool_results, which MiniMax chat templates reject; FireConnect fails that model choice with an explanation. -- evidence: [README.md#L362-L365](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L362-L365) (`clm_512e0bfc93b8097ecb3f14dfc0bc1581a9445a65a1381b0b85c5c503f3864b21`)
- [observation/documented] Claude Code cannot mark a model as non-vision, so attaching an image while a text-only slot is active can break the session; activation prints a warning and recovery is via /rewind. -- evidence: [README.md#L269-L271](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L269-L271), [README.md#L273-L275](https://github.com/fw-ai/fireconnect/blob/cc1d8417911517d1507a6c5c0b857aafe51c4bb0/README.md#L273-L275) (`clm_e61e8664cfbf9866726d89722d592a9268284c36d515a9910cb8fd8385f3da5f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

