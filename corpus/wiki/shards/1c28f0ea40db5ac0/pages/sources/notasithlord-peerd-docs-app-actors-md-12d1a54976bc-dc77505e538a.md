---
access: public
aliases: []
claim_ids:
- clm_2d5ed33ed3326fa1f189374f1712af495251c40c0e4a91394e3be81d744ba76c
- clm_493a5940a94099b8603b9a0fef44d07ade0064dd0ce5b00f2f566449ab05e48f
maturity: draft
page_id: pg_b805b05bc3955ff08ca0dc77505e538a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_03743a43d00a55f9bfaae00e25cbd01e
title: NotASithLord/peerd/docs/APP-ACTORS.md @ 12d1a54976bc
updated_at: '2026-09-14T02:23:22Z'
---

# NotASithLord/peerd/docs/APP-ACTORS.md @ 12d1a54976bc

<!-- rcw:begin owner=source:src_03743a43d00a55f9bfaae00e25cbd01e block=evidence -->
- App manifests use peerd.json with fields like kind, entry, agent (kind bound-app, profile, surface, name, instructions, runtime), and capabilities; a conforming Git repository places peerd.json and its entry file at the root. [@claim:clm_2d5ed33ed3326fa1f189374f1712af495251c40c0e4a91394e3be81d744ba76c]
- Apps integrate via window.peerd APIs: agent.open() reveals a trusted drawer only during real user activation, agent.expose() declares observe/act semantic adapters, and peerd.data provides bounded JSON persistence (1 MB per write) mapped to data/<key>.json in the App's working tree. [@claim:clm_493a5940a94099b8603b9a0fef44d07ade0064dd0ce5b00f2f566449ab05e48f]
<!-- rcw:end owner=source:src_03743a43d00a55f9bfaae00e25cbd01e block=evidence -->

## Researcher notes

