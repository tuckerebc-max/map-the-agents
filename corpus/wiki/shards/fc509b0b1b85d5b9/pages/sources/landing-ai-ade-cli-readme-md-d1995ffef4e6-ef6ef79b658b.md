---
access: public
aliases: []
claim_ids:
- clm_172b2232aaf1c05b69117947200624e8f308a25de161a126c272a41243cd21ba
- clm_1c9504e4df7ee748d62834926d41faae01b558e39c78f64d63e49622654727b5
- clm_295c7162c41987eadce87d9d37e4c8cf98785fbca8d21de07b638159c45ea1cb
- clm_59b84b039b3425646bd9bfbf69137d9695c3af666107526577976707728c760e
- clm_91e29bae244e085a3d68414ab86dae6d4fa56bd3b5be90702c7034eb78410391
- clm_9288622aac4c5615bd57cd8e6ff04ac6997c128dfc77749c6847b3a9b797c4d6
- clm_b21d3bb051b65f565213c7f2b0811d867dc5103f5d61e89c852a0c5c58a054d5
- clm_c09ed1d13078a561bee077f2af2df710337580509fcfd4907a82249dadd6081e
- clm_c2e31087356a2932e37d1ebc9c7b8083d0a4b44e83d4364ee7e4c812a6b5d7a5
- clm_fcf9822ea88a5abd24909640e137840d381bf64b809dacb21239fbe0c7f39009
maturity: draft
page_id: pg_1b8feb715d4c5c9188e3ef6ef79b658b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7ab78917db035beda157729c7f80573c
title: landing-ai/ade-cli/README.md @ d1995ffef4e6
updated_at: '2026-09-14T04:04:38Z'
---

# landing-ai/ade-cli/README.md @ d1995ffef4e6

<!-- rcw:begin owner=source:src_7ab78917db035beda157729c7f80573c block=evidence -->
- `ade help --json` returns the entire shipped surface in one call — commands, flags, result shapes, topics, exit states, and store layout — aimed at agent bootstrap, and SKILL.md ships the agent contract. [@claim:clm_172b2232aaf1c05b69117947200624e8f308a25de161a126c272a41243cd21ba]
- Every command accepts `--json` to emit one stable JSON object on stdout, and `ade help COMMAND` documents flags and result shapes. [@claim:clm_1c9504e4df7ee748d62834926d41faae01b558e39c78f64d63e49622654727b5]
- The CLI offers `ade parse` to convert documents into grounded Markdown and elements, and `ade extract` to pull schema-shaped fields with page-and-box evidence, saving results to a local store at ~/.ade. [@claim:clm_295c7162c41987eadce87d9d37e4c8cf98785fbca8d21de07b638159c45ea1cb]
- The command surface includes parse, extract, find, crop, view, history list/clear, login/auth subcommands, version, update, and help, per the README command table. [@claim:clm_59b84b039b3425646bd9bfbf69137d9695c3af666107526577976707728c760e]
- For non-PATH environments like CI or agent harnesses, the CLI can be invoked by absolute path (~/.ade/bin/ade, or %USERPROFILE%\.ade\bin\ade.exe on Windows) with credentials via the ADE_API_KEY environment variable. [@claim:clm_91e29bae244e085a3d68414ab86dae6d4fa56bd3b5be90702c7034eb78410391]
- The repository was formerly `agentic-doc`, the original ADE SDK, preserved unchanged on the legacy branch; since 2026-07-31 it ships the ADE CLI, licensed Apache-2.0. [@claim:clm_9288622aac4c5615bd57cd8e6ff04ac6997c128dfc77749c6847b3a9b797c4d6]
- The store lives at ~/.ade (app at ~/.ade/bin/ade), with ADE_HOME relocating it, ADE_CLI_VERSION pinning a version, and ADE_CLI_INSTALL_DIR changing the destination. [@claim:clm_b21d3bb051b65f565213c7f2b0811d867dc5103f5d61e89c852a0c5c58a054d5]
- Releases ship self-contained binaries for macOS, Linux, and Windows on arm64 and x86_64, requiring no Python or uv. [@claim:clm_c09ed1d13078a561bee077f2af2df710337580509fcfd4907a82249dadd6081e]
- Re-running an identical command consumes no credits because results persist in the local store; parse dedup serves stored results with an explicit notice and only `--force` re-bills. [@claim:clm_c2e31087356a2932e37d1ebc9c7b8083d0a4b44e83d4364ee7e4c812a6b5d7a5]
- The CLI mentions new releases on stderr at most once a day, and ADE_NO_UPDATE_CHECK=1 disables that check; `ade update` self-updates, or points at uv tool upgrade for uv/pipx installs. [@claim:clm_fcf9822ea88a5abd24909640e137840d381bf64b809dacb21239fbe0c7f39009]
<!-- rcw:end owner=source:src_7ab78917db035beda157729c7f80573c block=evidence -->

## Researcher notes

