---
access: public
aliases: []
claim_ids:
- clm_44a2fcf77239b74a2f11e3ded86372429bb38a3d8196604332da2f10bdba3608
- clm_4eaff013ceb7098aa8ce1901e121ba4af682b7fbedc9ef142f3ed788185ea054
- clm_55667549ff19c7a0476eb1387484a9f91aa9273427d87e6ac1bf61fef7ade92b
- clm_5b839e6628490757b93b6a2352615f2e97932532f3ce9dd0286566deeb78ebd1
- clm_90a58d313ca8dbf01d77aefe432f3a49763619610c7fa359392d60ef7295e5a3
- clm_d92175391619bafe7f38c4633892ad507f2b7ff19e9319c54169ad9419cad65b
maturity: draft
page_id: pg_a4aec5cdea2a54c98d7134076856ac07
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_beba001ea77254e881b5df000113c564
title: aaif-goose/goose/CUSTOM_DISTROS.md @ 50666ae0b9a5
updated_at: '2026-09-14T01:28:50Z'
---

# aaif-goose/goose/CUSTOM_DISTROS.md @ 50666ae0b9a5

<!-- rcw:begin owner=source:src_beba001ea77254e881b5df000113c564 block=evidence -->
- Configuration precedence is documented as environment variables, then config.yaml, then defaults. [@claim:clm_44a2fcf77239b74a2f11e3ded86372429bb38a3d8196604332da2f10bdba3608]
- Custom clients can integrate over ACP using 'goose serve', an HTTP/WebSocket server started with a GOOSE_SERVER__SECRET_KEY environment variable. [@claim:clm_4eaff013ceb7098aa8ce1901e121ba4af682b7fbedc9ef142f3ed788185ea054]
- Telemetry via PostHog is optional and can be disabled by setting GOOSE_DISABLE_TELEMETRY=1, or redirected to a custom PostHog instance by modifying posthog.rs. [@claim:clm_55667549ff19c7a0476eb1387484a9f91aa9273427d87e6ac1bf61fef7ade92b]
- Secrets are stored via a SecretStorage mechanism that uses the system keyring by default with a file-based fallback available, and configuration lives at ~/.config/goose/config.yaml. [@claim:clm_5b839e6628490757b93b6a2352615f2e97932532f3ce9dd0286566deeb78ebd1]
- Recipes are YAML-based task definitions that can bundle extensions and, with sub-recipes and subagents, express multi-step workflows; an example recipe declares extensions with stdio type, command, and args. [@claim:clm_90a58d313ca8dbf01d77aefe432f3a49763619610c7fa359392d60ef7295e5a3]
- The architecture diagram shows user interfaces (CLI, Electron desktop, custom UIs) above a 'goose serve' ACP HTTP/WebSocket server, above a core goose crate containing providers, MCP extensions, and config/recipes. [@claim:clm_d92175391619bafe7f38c4633892ad507f2b7ff19e9319c54169ad9419cad65b]
<!-- rcw:end owner=source:src_beba001ea77254e881b5df000113c564 block=evidence -->

## Researcher notes

