---
access: public
aliases: []
claim_ids:
- clm_158884c1c06613fbae3b1ea498ac501ce1122204075e3ceafef6cb79b45577d5
- clm_4977431eac43653209ff0a689d311348494eb9135cbf0a43ea8e801e6828e2be
- clm_588e39db7c286b8c93bb7da4fa10d054f0796c34c399e4070238090e7e917fca
- clm_696ada2127727a365c79c22631e5bfa307de7a143e6ae6eb0aa5e0e4aff4e957
- clm_fbd0c35540ca633f028dc65e8f032c328568e2fedd1ed77189c18ace4180f505
maturity: draft
page_id: pg_672e40a956525516a9475b5b76f6b655
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_620021a5afdd50f68892029b6179b221
title: LucasDuys/forge/docs/architecture.md @ 642c60b104f0
updated_at: '2026-09-14T04:08:35Z'
---

# LucasDuys/forge/docs/architecture.md @ 642c60b104f0

<!-- rcw:begin owner=source:src_620021a5afdd50f68892029b6179b221 block=evidence -->
- Forge requires Claude Code v1.0.33+; the solo path needs no npm install, and Ably is an optional dependency only for multiplayer collaboration. [@claim:clm_158884c1c06613fbae3b1ea498ac501ce1122204075e3ceafef6cb79b45577d5]
- Three cross-cutting skills run automatically across agents: Karpathy guardrails inlined into executor/reviewer/planner, graphify knowledge-graph integration, and DESIGN.md design-system support — the latter two degrade gracefully when their inputs are absent. [@claim:clm_4977431eac43653209ff0a689d311348494eb9135cbf0a43ea8e801e6828e2be]
- The pipeline is strictly sequential (brainstorm → plan → execute), enforced programmatically via an approval gate, frontier validation, and validateWorkflowPrerequisites(); users cannot skip phases or bypass the approval gate. [@claim:clm_588e39db7c286b8c93bb7da4fa10d054f0796c34c399e4070238090e7e917fca]
- Tasks execute in their own git worktrees with TDD, and passing tasks are squash-merged atomically; a streaming topological scheduler dispatches tasks as soon as their dependencies complete. [@claim:clm_696ada2127727a365c79c22631e5bfa307de7a143e6ae6eb0aa5e0e4aff4e957]
- Collaboration defines a transport interface (read, cas, del, list, publish/subscribe/sendTargeted) with two backends: Ably WebSocket pub/sub (sub-second) and a zero-setup polling backend over a git branch (~2.5s). [@claim:clm_fbd0c35540ca633f028dc65e8f032c328568e2fedd1ed77189c18ace4180f505]
<!-- rcw:end owner=source:src_620021a5afdd50f68892029b6179b221 block=evidence -->

## Researcher notes

