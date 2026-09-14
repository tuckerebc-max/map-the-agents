---
access: public
aliases: []
claim_ids:
- clm_0a74b819a7480753aa876342746598bdfe2258d89b2a31763bae36761d981001
- clm_a6c36e215eeca7d418b2f7a389a2e01d4ac4270965798689bafac833f9cd1aa1
- clm_a8b505c44e482774ae0d8d52ccb9ba7dc1df1cce8f8e2218aaa8d9843e2ba226
- clm_b8d976f0cb09e9301e2c3c30d2d2020e352852401d942c7fddf5445d244a59f1
- clm_dcd9ccd68aa128d21b14400f99a9a2ac6a5d5b69b7bf51efccf25c1ff072240d
- clm_de7a4cdde55ae79390b307a73cf866d76afef04319135effca0e8a31e5185257
maturity: draft
page_id: pg_9378ffd40610545c96e0e551fe89d6ea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3b703eb94fac525a82584ac59b1bdfa7
title: NikitaDmitrieff/auto-co-meta/README.md @ 5e6bb8a8765e
updated_at: '2026-09-14T04:12:54Z'
---

# NikitaDmitrieff/auto-co-meta/README.md @ 5e6bb8a8765e

<!-- rcw:begin owner=source:src_3b703eb94fac525a82584ac59b1bdfa7 block=evidence -->
- The Makefile exposes operational commands such as make start, monitor, status, health, history, export, stop, pause, and resume, plus a Next.js dashboard runnable on port 3000. [@claim:clm_0a74b819a7480753aa876342746598bdfe2258d89b2a31763bae36761d981001]
- Each cycle reads consensus.md, builds a prompt from PROMPT.md, calls 'claude -p', has agents update consensus, appends structured JSONL logs, then sleeps and repeats; each cycle selects 3-5 of the 14 relevant agents. [@claim:clm_a6c36e215eeca7d418b2f7a389a2e01d4ac4270965798689bafac833f9cd1aa1]
- Claude Code installed and working is listed as the prerequisite; the comparison table states the only dependency is Claude Code itself, with no framework or database required. [@claim:clm_a8b505c44e482774ae0d8d52ccb9ba7dc1df1cce8f8e2218aaa8d9843e2ba226]
- auto-co is described as a bash loop that invokes Claude Code every two minutes, letting 14 AI agents debate, decide, build, and deploy software continuously without human supervision. [@claim:clm_b8d976f0cb09e9301e2c3c30d2d2020e352852401d942c7fddf5445d244a59f1]
- Key runtime files include auto-loop.sh (the loop with monitoring, error handling, and adaptive frequency), PROMPT.md (per-cycle system prompt), memories/consensus.md, .claude/agents/*.md personas, and a Makefile of commands. [@claim:clm_dcd9ccd68aa128d21b14400f99a9a2ac6a5d5b69b7bf51efccf25c1ff072240d]
- The design deliberately avoids a database, server, or framework: state persists in markdown files plus git, with Claude Code as the sole dependency. [@claim:clm_de7a4cdde55ae79390b307a73cf866d76afef04319135effca0e8a31e5185257]
<!-- rcw:end owner=source:src_3b703eb94fac525a82584ac59b1bdfa7 block=evidence -->

## Researcher notes

