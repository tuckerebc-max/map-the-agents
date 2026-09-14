---
access: public
aliases: []
claim_ids:
- clm_158884c1c06613fbae3b1ea498ac501ce1122204075e3ceafef6cb79b45577d5
- clm_3242efdd939c21cc39092d49baed1aa494578b6fcb95023d79531923b623a84e
- clm_4466f295dd87052bbb8e2612d5e6539d4107514e336d52c9fb64ccd51145bb7e
- clm_588e39db7c286b8c93bb7da4fa10d054f0796c34c399e4070238090e7e917fca
- clm_696ada2127727a365c79c22631e5bfa307de7a143e6ae6eb0aa5e0e4aff4e957
- clm_74e177d8ffb796d82c7a26823ea64e1acb904ef33835517ff19c10900941513a
- clm_88ab7ddbabbfd84bd3c844bcbf6949ce082fd9147a997987816ddb136a6c5a6b
- clm_bc672e8177971df89a04bba9462ece25460b908b1047b3f2dade6df745b7ae96
- clm_bfd22f57d63d5e22c703f937550a37f9a51d53257b9196c648c8eec54f58ba07
- clm_f6c319071be93e39acc6028b2c95c01675ea56733979472c08e65d3d5d8891fc
maturity: draft
page_id: pg_df20454b93c75e44ab2a183ce1ded570
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7c798626c2b65109885d832c1564a228
title: LucasDuys/forge/README.md @ 642c60b104f0
updated_at: '2026-09-14T04:08:35Z'
---

# LucasDuys/forge/README.md @ 642c60b104f0

<!-- rcw:begin owner=source:src_7c798626c2b65109885d832c1564a228 block=evidence -->
- Forge requires Claude Code v1.0.33+; the solo path needs no npm install, and Ably is an optional dependency only for multiplayer collaboration. [@claim:clm_158884c1c06613fbae3b1ea498ac501ce1122204075e3ceafef6cb79b45577d5]
- The docs report measured token-savings results for the product's optimization filters, including a real A/B run where filtering a git diff cut Claude token use from 59,600 to 42,402 (28.9% fewer), and caveman compression benchmarks of 26.8% prose reduction. [@claim:clm_3242efdd939c21cc39092d49baed1aa494578b6fcb95023d79531923b623a84e]
- In gated (default) mode Forge pauses before installing new dependencies or calling paid APIs; full mode assumes prior consent for those, but both modes require explicit approval to push to a remote and refuse destructive git ops unless the spec requests them. [@claim:clm_4466f295dd87052bbb8e2612d5e6539d4107514e336d52c9fb64ccd51145bb7e]
- The pipeline is strictly sequential (brainstorm → plan → execute), enforced programmatically via an approval gate, frontier validation, and validateWorkflowPrerequisites(); users cannot skip phases or bypass the approval gate. [@claim:clm_588e39db7c286b8c93bb7da4fa10d054f0796c34c399e4070238090e7e917fca]
- Tasks execute in their own git worktrees with TDD, and passing tasks are squash-merged atomically; a streaming topological scheduler dispatches tasks as soon as their dependencies complete. [@claim:clm_696ada2127727a365c79c22631e5bfa307de7a143e6ae6eb0aa5e0e4aff4e957]
- The docs acknowledge that FORGE_COMPLETE only means tasks done, tests green, reviewer and verifier satisfied; a feature passing all four can still look broken in a browser because unit tests don't render pixels. [@claim:clm_74e177d8ffb796d82c7a26823ea64e1acb904ef33835517ff19c10900941513a]
- Loop state lives on disk in a .forge directory rather than in the conversation, so crashes, context resets, and OOMs can recover by restarting the state machine from disk. [@claim:clm_88ab7ddbabbfd84bd3c844bcbf6949ce082fd9147a997987816ddb136a6c5a6b]
- Users drive Forge through slash commands such as /forge brainstorm, /forge plan, /forge execute --autonomy full, plus read-only /forge watch and /forge status --json, and /forge resume for recovery. [@claim:clm_bc672e8177971df89a04bba9462ece25460b908b1047b3f2dade6df745b7ae96]
- Repository development practice: contributors fork, create a feature branch, make changes, run tests via node scripts/run-tests.cjs, and open a pull request, with details in CONTRIBUTING.md. [@claim:clm_bfd22f57d63d5e22c703f937550a37f9a51d53257b9196c648c8eec54f58ba07]
- The brainstorm phase turns a one-line idea into an R-numbered spec with testable acceptance criteria, and every task must map to at least one R-number. [@claim:clm_f6c319071be93e39acc6028b2c95c01675ea56733979472c08e65d3d5d8891fc]
<!-- rcw:end owner=source:src_7c798626c2b65109885d832c1564a228 block=evidence -->

## Researcher notes

