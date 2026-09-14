---
access: public
aliases: []
claim_ids:
- clm_0d7af5696e1878f6320d23b43e71ca65b68188f0133fc0c29a4fd814f376db1e
- clm_1dbd4240dc80b3a0a6aa6e904133b0e955db5c6089daa929c757e7dbd330a88d
- clm_84c5b043adbefafe74cbf15c3d4bbabbccdcf7a65fc3dd9b75a6bc288229f880
- clm_ba98f3373e76dd23fe728d862baefb742ca82f9c1af9c30ed803aebd562fadee
maturity: draft
page_id: pg_4a2ce5edf7435c678a841bdd057bcefe
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ff3e539475275bbe9d6306193d4f36dc
title: vercel-labs/fx/CHANGELOG.md @ e3ad6d8d645d
updated_at: '2026-09-14T04:40:43Z'
---

# vercel-labs/fx/CHANGELOG.md @ e3ad6d8d645d

<!-- rcw:begin owner=source:src_ff3e539475275bbe9d6306193d4f36dc block=evidence -->
- Recent releases reduced the shell tool to three actions (down from twelve) and cut the subagent command surface to two commands, with Enter steering the active turn rather than queuing follow-ups. [@claim:clm_0d7af5696e1878f6320d23b43e71ca65b68188f0133fc0c29a4fd814f376db1e]
- The libfx npm package is stated to have no runtime dependencies, though host-supplied tools and MCP clients may bring their own. [@claim:clm_1dbd4240dc80b3a0a6aa6e904133b0e955db5c6089daa929c757e7dbd330a88d]
- The product has an auto mode that reviews each pending action, blocks cautioned or untrusted-output-derived actions, and supports full-access mode via `--full-access` or `/permissions full-access`. [@claim:clm_84c5b043adbefafe74cbf15c3d4bbabbccdcf7a65fc3dd9b75a6bc288229f880]
- Subagents can run with their own model and reasoning effort, keep running while the user steers, and accept mid-task feedback without interrupting their current tool. [@claim:clm_ba98f3373e76dd23fe728d862baefb742ca82f9c1af9c30ed803aebd562fadee]
<!-- rcw:end owner=source:src_ff3e539475275bbe9d6306193d4f36dc block=evidence -->

## Researcher notes

