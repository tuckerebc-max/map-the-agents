---
access: public
aliases: []
claim_ids:
- clm_4e82b99eea7f379e5d9b27ddbbea96abd6a3007ce00b429e1f9fb3518851c1fc
- clm_503e285b1c2946cadebdc933aec798870296aca511fa21ad49d1fd537a77bbe9
- clm_5487d2c58aa59d90888259336c8f2d28a0b823d8d2dc14049b98e1503155f97a
- clm_68f82f927b6499f0b63334cf5fb9d06e259ebd2f9fadd0c9a207804df49b0bc9
- clm_76bf15a24d7e2c3d90352a377fd0f0cea1008b57ecc7460d6f62587266ad3307
- clm_ae865c03813fb4c44446b647af734672451ce92b2e72db0cc8bcf004ed8d52ac
- clm_ca60a241d71e0e380f83af37ead67cdb5acd88eb87175b101011a3f1d88c8516
maturity: draft
page_id: pg_3a11a7c766675b10a861fde4f5ea2503
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c66a465232cd5868b16aae0fcc6fbce3
title: zjrosen/perles/docs/CURSOR_AGENT.md @ f97afa7a7c44
updated_at: '2026-09-14T04:34:24Z'
---

# zjrosen/perles/docs/CURSOR_AGENT.md @ f97afa7a7c44

<!-- rcw:begin owner=source:src_c66a465232cd5868b16aae0fcc6fbce3 block=evidence -->
- Repository development practice: optional Cursor integration tests are build-tagged, run via go test -tags=cursor_integration, and are intended for local/dev environments rather than CI. [@claim:clm_4e82b99eea7f379e5d9b27ddbbea96abd6a3007ce00b429e1f9fb3518851c1fc]
- Since Cursor lacks --append-system-prompt, Perles prepends the system prompt to the main prompt with a blank line separator, the same approach used for OpenCode. [@claim:clm_503e285b1c2946cadebdc933aec798870296aca511fa21ad49d1fd537a77bbe9]
- Cursor CLI does not support tool filtering flags, so all agent tools remain enabled and the DisallowedTools config field is silently ignored for that provider. [@claim:clm_5487d2c58aa59d90888259336c8f2d28a0b823d8d2dc14049b98e1503155f97a]
- Orchestration providers include Claude, Amp, Codex, OpenCode, and Cursor Agent CLI; coordinator and worker clients can be mixed, e.g. cursor coordinator with claude workers. [@claim:clm_68f82f927b6499f0b63334cf5fb9d06e259ebd2f9fadd0c9a207804df49b0bc9]
- Using the Cursor provider requires the cursor-agent CLI on PATH; installing from source requires Go 1.27+. [@claim:clm_76bf15a24d7e2c3d90352a377fd0f0cea1008b57ecc7460d6f62587266ad3307]
- With the Cursor provider, token and cost fields show zero because Cursor's stream-json output lacks usage and cost data. [@claim:clm_ae865c03813fb4c44446b647af734672451ce92b2e72db0cc8bcf004ed8d52ac]
- Because Cursor reads MCP config only from .cursor/mcp.json, Perles writes role-specific server entries (orchestrator, per-worker, observer) into that shared file using a read-merge-write pattern. [@claim:clm_ca60a241d71e0e380f83af37ead67cdb5acd88eb87175b101011a3f1d88c8516]
<!-- rcw:end owner=source:src_c66a465232cd5868b16aae0fcc6fbce3 block=evidence -->

## Researcher notes

