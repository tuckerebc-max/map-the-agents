# nicobailon/pi-boomerang -- full detail

[Back to orientation](pi-boomerang.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nicobailon/pi-boomerang/1a5985b2d92cfa84ce1f470d100d02b368711a91/f61ed095535cf80d.json](../../../wiki/dossiers/nicobailon/pi-boomerang/1a5985b2d92cfa84ce1f470d100d02b368711a91/f61ed095535cf80d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] After completion, raw turn history is replaced in future context by an expanded handoff summary containing outcome, changed files, relevant reads, validation commands, failures, and config metadata. -- evidence: [CHANGELOG.md#L62-L63](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/CHANGELOG.md#L62-L63), [README.md#L71-L71](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L71-L71), [README.md#L13-L13](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L13-L13) (`clm_25056fa832859cc129439995d0be008c159b1e980889b73c122d8f4409dac22f`)
- [observation/documented] The session tree preserves full history for `/tree` navigation, so only future context is collapsed while the underlying history remains accessible. -- evidence: [README.md#L39-L39](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L39-L39), [README.md#L41-L41](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L41-L41) (`clm_599228afc967fef35c60dc291c2276814232ad73d8fbc79d8e49e699d6d39bd5`)
- [observation/documented] Boomerang summarizes only context/tokens and never touches file state; all file changes made during a task are preserved on disk. -- evidence: [README.md#L238-L238](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L238-L238) (`clm_1fdcd62eda1cd35372613ac2217abf4c758c41078eafa3d30fd7808a3ea190fa`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The extension exposes a `/boomerang <task>` command that executes a task autonomously and summarizes context afterward, plus `/boomerang-cancel` to abort without summarizing. -- evidence: [README.md#L68-L69](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L68-L69), [README.md#L211-L226](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L211-L226), [README.md#L9-L11](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L9-L11), [README.md#L13-L13](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L13-L13) (`clm_cc3fadac1a039620f9a1c7f171aa4de77e909eb14d2d484e590fc96b610f3a5a`)
- [observation/documented] Chained templates can be run in sequence (e.g. `/boomerang /scout -> /planner -> /impl`) with per-step inline args, global fallback args after `--`, and a single summary return at the end. -- evidence: [README.md#L81-L81](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L81-L81), [README.md#L75-L75](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L75-L75), [README.md#L83-L85](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L83-L85), [README.md#L77-L79](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L77-L79), [README.md#L61-L61](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L61-L61) (`clm_7c4f251abe90fc57ca931b6a42d1457405259c7ab85deada8f915eeaca8e44cf`)
- [observation/documented] Template frontmatter fields `model`, `skill`, and `thinking` control each chain step's configuration, and boomerang restores the original config after the summary return. -- evidence: [README.md#L87-L87](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L87-L87), [README.md#L143-L150](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L143-L150), [README.md#L152-L155](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L152-L155) (`clm_919899d9296e1b3b05f46285e769ee6489f9c48b201dd96bbcb061116870b5bd`)
- [observation/documented] `--rethrow N` (N required, 1-999) reruns the full task N times, summarizing between passes; file changes persist on disk and each pass sees accumulated summaries rather than raw history. -- evidence: [README.md#L103-L107](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L103-L107), [README.md#L93-L93](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L93-L93) (`clm_c5dd72a4b88d678e304d363f3e66c996a75b77e8221c0d2e3892ca622e243e28`)
- [observation/documented] `--loop N` is treated as an alias for `--rethrow N`; if both flags are present `--rethrow` wins, loop metadata is stripped from rendered tasks, and bare `--loop` is invalid. -- evidence: [CHANGELOG.md#L112-L116](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/CHANGELOG.md#L112-L116), [README.md#L113-L116](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L113-L116), [README.md#L125-L126](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L125-L126) (`clm_e0c6d478fe2aa23774b8688700c92310cceb9ed99265b213a2e13436287fb8ad`)
- [observation/documented] Tasks starting with `/` are treated as prompt templates loaded from `<cwd>/.pi/prompts/` then `~/.pi/agent/prompts/`, with subdirectories mapping to path segments; `$@` and `$1`/`$2` expand args. -- evidence: [README.md#L139-L139](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L139-L139), [README.md#L152-L155](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L152-L155), [README.md#L132-L132](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L132-L132) (`clm_f9d977542e326a78296791841676d7ddb29eb2d09f6f9524ebef378f6558c443`)

## memory-state (1 claim(s))

- [observation/documented] Tool state and guidance persist to `~/.pi/agent/boomerang.json` across restarts, while anchor state is in-memory only and clears on session start or switch. -- evidence: [README.md#L205-L205](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L205-L205), [README.md#L244-L247](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L244-L247) (`clm_68a38b2ae4350b2100afd876044ff55e730f624b7828240125278b2fd51ae4fe`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] An optional agent-callable `boomerang` tool supports task mode (queued autonomous execution) and anchor mode (toggle a summary point); it is disabled by default and enabled via `/boomerang tool on`. -- evidence: [README.md#L188-L188](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L188-L188), [README.md#L190-L190](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L190-L190), [README.md#L192-L192](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L192-L192), [README.md#L180-L180](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L180-L180), [README.md#L178-L178](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L178-L178), [README.md#L194-L196](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L194-L196) (`clm_17019c432e9f8bc809006ca9fff6249fe47476d21ea0c28eac488000a7949651`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Documented limitations: summaries are heuristic and may miss semantic details, the agent may still ask questions, anchor state is in-memory only, and tool-initiated summaries may lag in the UI until `/reload`. -- evidence: [README.md#L207-L207](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L207-L207), [README.md#L244-L247](https://github.com/nicobailon/pi-boomerang/blob/1a5985b2d92cfa84ce1f470d100d02b368711a91/README.md#L244-L247) (`clm_c9a8639ad875020b5e4a7caaace4436eda1afefcb8f7853c2ca752d6d82f4026`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

