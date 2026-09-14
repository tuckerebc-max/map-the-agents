---
access: public
aliases: []
claim_ids:
- clm_5b3b5433c2b48c40bfd491696a0965a9ad702eab4ddace943cb84072138d513e
- clm_6abd789d7c4143b4e0caaa939e5f35d6046a9126e0cd0ef2f815090bdba1d4df
maturity: draft
page_id: pg_65061560c2cc5eb38017563f1ed5d70b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_085696af2bef502ca171cf04604f091b
title: leox255/loopsy/AGENTS.md @ 73c165476279
updated_at: '2026-09-14T03:10:02Z'
---

# leox255/loopsy/AGENTS.md @ 73c165476279

<!-- rcw:begin owner=source:src_085696af2bef502ca171cf04604f091b block=evidence -->
- State lives under ~/.loopsy/ in config.yaml, context.json (key-value store), peers.json, logs/audit.jsonl, and relay.json; the messaging protocol stores inbox, outbox, and ack entries as context keys with TTLs. [@claim:clm_5b3b5433c2b48c40bfd491696a0965a9ad702eab4ddace943cb84072138d513e]
- Repository development practice: contributors build with pnpm install and pnpm build, and releases are tag-driven — pushing a v* tag publishes loopsy and @loopsy/deploy-relay to npm via OIDC Trusted Publisher with provenance attestations. [@claim:clm_6abd789d7c4143b4e0caaa939e5f35d6046a9126e0cd0ef2f815090bdba1d4df]
<!-- rcw:end owner=source:src_085696af2bef502ca171cf04604f091b block=evidence -->

## Researcher notes

