# landing-ai/ade-cli -- full detail

[Back to orientation](ade-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/landing-ai/ade-cli/d1995ffef4e63a2a1c2774d9add93368889353c5/c1500fbf08ca7088.json](../../../wiki/dossiers/landing-ai/ade-cli/d1995ffef4e63a2a1c2774d9add93368889353c5/c1500fbf08ca7088.json)

## specifications (4 claim(s))

- [observation/documented] A draft v2 proposal (revised 2026-07-21) re-keys the store on job item ids — a hash of verb, source path, content, and params — replacing content-derived doc ids, with a flat ~/.ade/jobs/<id>/ layout. -- evidence: [docs/ade-cli-v2-proposal.md#L24-L29](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L24-L29), [docs/ade-cli-v2-proposal.md#L31-L32](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L31-L32), [docs/ade-cli-v2-proposal.md#L3-L10](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L3-L10) (`clm_6470e77b6e5cdfa042ff27b3fab27f6b7dad712241e284be818ee5dc57395807`)
- [observation/documented] The proposal defines parse as an idempotent state machine (absent/pending/complete/failed/expired) over the store, blocking by default with --wait, where Ctrl-C stops waiting but never the server-side work. -- evidence: [docs/ade-cli-v2-proposal.md#L197-L197](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L197-L197), [docs/ade-cli-v2-proposal.md#L180-L189](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L180-L189), [docs/ade-cli-v2-proposal.md#L193-L193](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L193-L193) (`clm_16714afb5d316992c28803dd85912914f8cf29f5bcecc07877471a1ddb0228de`)
- [observation/documented] The proposal targets the ADE v2 API: async POST /v2/parse and /v2/extract job contracts, priority/standard service tiers, parse returning markdown plus a structure tree with inline grounding {page, range, box}. -- evidence: [docs/ade-cli-v2-proposal.md#L71-L71](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L71-L71), [docs/ade-cli-v2-proposal.md#L73-L73](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L73-L73), [docs/ade-cli-v2-proposal.md#L75-L75](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L75-L75) (`clm_742dbdd84130d4a4f72e33af5ab890b91e8f6779fa12e8982cc47695739e74c7`)
- [observation/documented] Per the proposal, extract accepts a parse job item id, a document path (reusing the latest completed parse or auto-parsing first), or bring-your-own markdown, and field-to-box evidence is computed as a local join stored as evidence.json. -- evidence: [docs/ade-cli-v2-proposal.md#L280-L280](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L280-L280), [docs/ade-cli-v2-proposal.md#L223-L226](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L223-L226), [docs/ade-cli-v2-proposal.md#L236-L252](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L236-L252) (`clm_f475384775a5a00165b86df217bd062deedd4a007e6fbbfc1b27739f182932b1`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Re-running an identical command consumes no credits because results persist in the local store; parse dedup serves stored results with an explicit notice and only `--force` re-bills. -- evidence: [README.md#L6-L10](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L6-L10), [docs/ade-cli-v2-proposal.md#L45-L47](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L45-L47) (`clm_c2e31087356a2932e37d1ebc9c7b8083d0a4b44e83d4364ee7e4c812a6b5d7a5`)
- [observation/documented] The CLI mentions new releases on stderr at most once a day, and ADE_NO_UPDATE_CHECK=1 disables that check; `ade update` self-updates, or points at uv tool upgrade for uv/pipx installs. -- evidence: [README.md#L114-L117](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L114-L117) (`clm_fcf9822ea88a5abd24909640e137840d381bf64b809dacb21239fbe0c7f39009`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The CLI offers `ade parse` to convert documents into grounded Markdown and elements, and `ade extract` to pull schema-shaped fields with page-and-box evidence, saving results to a local store at ~/.ade. -- evidence: [README.md#L6-L10](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L6-L10) (`clm_295c7162c41987eadce87d9d37e4c8cf98785fbca8d21de07b638159c45ea1cb`)
- [observation/documented] Every command accepts `--json` to emit one stable JSON object on stdout, and `ade help COMMAND` documents flags and result shapes. -- evidence: [README.md#L58-L60](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L58-L60) (`clm_1c9504e4df7ee748d62834926d41faae01b558e39c78f64d63e49622654727b5`)
- [observation/documented] The command surface includes parse, extract, find, crop, view, history list/clear, login/auth subcommands, version, update, and help, per the README command table. -- evidence: [README.md#L62-L77](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L62-L77) (`clm_59b84b039b3425646bd9bfbf69137d9695c3af666107526577976707728c760e`)
- [observation/documented] `ade help --json` returns the entire shipped surface in one call — commands, flags, result shapes, topics, exit states, and store layout — aimed at agent bootstrap, and SKILL.md ships the agent contract. -- evidence: [README.md#L89-L95](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L89-L95) (`clm_172b2232aaf1c05b69117947200624e8f308a25de161a126c272a41243cd21ba`)
- [observation/documented] For non-PATH environments like CI or agent harnesses, the CLI can be invoked by absolute path (~/.ade/bin/ade, or %USERPROFILE%\.ade\bin\ade.exe on Windows) with credentials via the ADE_API_KEY environment variable. -- evidence: [README.md#L97-L101](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L97-L101) (`clm_91e29bae244e085a3d68414ab86dae6d4fa56bd3b5be90702c7034eb78410391`)

## memory-state (1 claim(s))

- [observation/documented] The store lives at ~/.ade (app at ~/.ade/bin/ade), with ADE_HOME relocating it, ADE_CLI_VERSION pinning a version, and ADE_CLI_INSTALL_DIR changing the destination. -- evidence: [README.md#L111-L112](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L111-L112), [README.md#L105-L109](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L105-L109) (`clm_b21d3bb051b65f565213c7f2b0811d867dc5103f5d61e89c852a0c5c58a054d5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Releases ship self-contained binaries for macOS, Linux, and Windows on arm64 and x86_64, requiring no Python or uv. -- evidence: [README.md#L18-L19](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L18-L19) (`clm_c09ed1d13078a561bee077f2af2df710337580509fcfd4907a82249dadd6081e`)

## limitations (1 claim(s))

- [observation/documented] The proposal notes the ADE v2 backend has no job cancel — submitted work always completes and bills — and encrypted PDFs are always rejected with a 422 (encrypted_pdf_unsupported). -- evidence: [docs/ade-cli-v2-proposal.md#L77-L84](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L77-L84), [docs/ade-cli-v2-proposal.md#L73-L73](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/docs/ade-cli-v2-proposal.md#L73-L73) (`clm_e2adc14c99702f12f6f24596de61e3736c145656179f72308feb2603f287cf56`)

## relevance (1 claim(s))

- [observation/documented] The repository was formerly `agentic-doc`, the original ADE SDK, preserved unchanged on the legacy branch; since 2026-07-31 it ships the ADE CLI, licensed Apache-2.0. -- evidence: [README.md#L132-L132](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L132-L132), [README.md#L125-L128](https://github.com/landing-ai/ade-cli/blob/d1995ffef4e63a2a1c2774d9add93368889353c5/README.md#L125-L128) (`clm_9288622aac4c5615bd57cd8e6ff04ac6997c128dfc77749c6847b3a9b797c4d6`)

