---
access: public
aliases: []
claim_ids:
- clm_114825a60fc34c1d8d312ca1f7f56dce379c14b0e1f7b1c7460e98bae80d9baa
- clm_40dc4f5aef9806c88552096ddcb9375b567853316f3303e9b0a1ef977b11fcd0
- clm_4c019ef5a773046599f77e39a45913620653c5c44c0177de1818ae771b0fea28
- clm_72f5babcd14862814804547e09713d8b4dd2fab801551c1bcc46938470d0bbc5
- clm_dca464b68ac577dbf8fb71231ce1326e3f24725f39a523ad159ca7bb687f524c
maturity: draft
page_id: pg_7e9a6ecffd095237b499dd8f5fb90502
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1df7d36e31f75ccb8cb7b51e102d35c9
title: LiuMengxuan04/MiniCode/ARCHITECTURE.md @ 40413758cc12
updated_at: '2026-09-14T04:48:35Z'
---

# LiuMengxuan04/MiniCode/ARCHITECTURE.md @ 40413758cc12

<!-- rcw:begin owner=source:src_1df7d36e31f75ccb8cb7b51e102d35c9 block=evidence -->
- Documentation lists planned-but-not-built items including full Ink/React rendering, bridge/IDE two-way communication, remote sessions, LSP support, and a skill marketplace, while noting a minimal sub-agent runtime and basic layered memory loading are already implemented. [@claim:clm_114825a60fc34c1d8d312ca1f7f56dce379c14b0e1f7b1c7460e98bae80d9baa]
- Documentation states very large tool outputs are moved out of the prompt context and stored on disk, leaving the model a preview and a path to the full output. [@claim:clm_40dc4f5aef9806c88552096ddcb9375b567853316f3303e9b0a1ef977b11fcd0]
- Documented runtime state keeps conversation messages in memory during a turn, appends them to a per-project session log after each successful turn, and treats fresh provider-reported usage as the source of truth for context accounting, with local token estimation only as a fallback or a tail estimate. [@claim:clm_4c019ef5a773046599f77e39a45913620653c5c44c0177de1818ae771b0fea28]
- Documentation describes a root agent that can spawn up to three concurrent read-only sub-agents restricted to file search/read, skill loading, and web research tools; sub-agents cannot edit files, run commands, ask the user, or spawn further agents, and the root owns every code change. [@claim:clm_72f5babcd14862814804547e09713d8b4dd2fab801551c1bcc46938470d0bbc5]
- Documentation states this multi-agent MVP does not persist workers, load .claude/agents, support nesting, isolate worktrees, or allow live user steering, framing itself as a minimal teaching implementation. [@claim:clm_dca464b68ac577dbf8fb71231ce1326e3f24725f39a523ad159ca7bb687f524c]
<!-- rcw:end owner=source:src_1df7d36e31f75ccb8cb7b51e102d35c9 block=evidence -->

## Researcher notes

