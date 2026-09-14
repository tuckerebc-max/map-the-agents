# touwaeriol/claude-code-plus -- full detail

[Back to orientation](claude-code-plus.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/touwaeriol/claude-code-plus/d1e1622cb7731afc0e7d9abfc278def225ac7535/ed5501d0dd0f5d30.json](../../../wiki/dossiers/touwaeriol/claude-code-plus/d1e1622cb7731afc0e7d9abfc278def225ac7535/ed5501d0dd0f5d30.json)

## specifications (1 claim(s))

- [observation/documented] The product is an IntelliJ IDEA plugin that integrates Claude AI into the IDE, offering code assistance via natural-language chat. -- evidence: [README.md#L7-L9](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L7-L9), [README.md#L24-L24](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L24-L24) (`clm_d4c6feab9bbac90240a7ceeeb848d8ab280cfe4f4ea47507563e10bc93660a10`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [inference/documented] The architecture appears to use RSocket over WebSocket for streaming chat and plain HTTP for non-streaming IDE actions, per the changelog's RSocket migration notes and AGENTS.md protocol descriptions. -- evidence: [AGENTS.md#L50-L53](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/AGENTS.md#L50-L53), [AGENTS.md#L182-L182](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/AGENTS.md#L182-L182), [CHANGELOG.md#L129-L136](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L129-L136) (`clm_8bef16158fa27fe6fae1d8d332697dd2e19f549bbae0db3e5ba43f768f42733c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to communicate in Simplified Chinese while writing git commits and changelog entries in English. -- evidence: [AGENTS.md#L1-L2](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/AGENTS.md#L1-L2) (`clm_1be0b3e2d18b1cf1c9df5bb6d1b0ae2296c161103170022d30090ac3b486997a`)
- [observation/documented] Repository development practice: the README welcomes contributions via pull requests, and the changelog records CI verification-matrix and caching build practices. -- evidence: [CHANGELOG.md#L14-L17](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L14-L17), [CHANGELOG.md#L345-L353](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L345-L353), [README.md#L134-L134](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L134-L134) (`clm_7a8b51e8999587c202c2231420971e5f1099d98e098a4265986fbfe2bc871502`)

## skills-patterns (1 claim(s))

- [observation/documented] The plugin supports MCP (Model Context Protocol) servers to extend Claude's capabilities, with status monitoring, reconnect, and enable/disable controls. -- evidence: [CHANGELOG.md#L76-L79](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L76-L79), [README.md#L75-L75](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L75-L75) (`clm_953af7d2190798029e07225a1c336389a9d8b953449a8688d3941f6f09fcc24e`)

## interfaces (1 claim(s))

- [observation/documented] A model selector lets users switch between Claude models (Opus 4.5, Sonnet 4.5, Haiku 4.5), including a /model slash command and default model in settings. -- evidence: [README.md#L50-L50](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L50-L50), [CHANGELOG.md#L82-L85](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L82-L85) (`clm_7a0f8de7aa9c6f961325e310fd5977e2052c9b5363c3f4adf1b99d56aee2510f`)

## memory-state (1 claim(s))

- [observation/documented] Sessions support reconnection: the plugin resumes a session using a stored conversation ID and auto-reconnects when the frontend becomes visible again. -- evidence: [CHANGELOG.md#L105-L108](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L105-L108) (`clm_f2ef34ecd3c61427733d85f237a0a463a44bc88a3a4d19f5b65614dcf557b2ae`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] File write operations go through a secure authorization dialog, and the plugin added a dynamic MCP tool allowlist for flexible tool permissions. -- evidence: [CHANGELOG.md#L473-L476](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L473-L476), [README.md#L55-L55](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L55-L55) (`clm_bb863e917286dc6399fdc3a820cac94f124ba96595c1466a9f31aaca752b1154`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The plugin requires a JetBrains IDE (builds 242-253) and Node.js v18 or higher with node on PATH, and bundles a Claude CLI so no separate CLI install is needed. -- evidence: [README.md#L94-L99](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L94-L99), [README.md#L101-L101](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L101-L101) (`clm_c39bcd8acab8b1869e6c7b10c4bc8f883f9dc2cf2ddc54c98e3a7a113223aa79`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

