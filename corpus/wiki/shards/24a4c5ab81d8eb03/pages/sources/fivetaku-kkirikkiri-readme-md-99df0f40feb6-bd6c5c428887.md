---
access: public
aliases: []
claim_ids:
- clm_3f4af1bb55fb0e07df543d85bc12db5227e537ef3aa6ec865720210834dcb08d
- clm_44b3ffddb82b45d500b26d1a11689fd4d67a34338ed0d2089e69bdfea443be95
- clm_4eb4f4f0e76508af22b9aaa7e34e3254c8c9eb3aae69a2f908f27aa336195e19
- clm_5eda18cb33add8db489a45a606ee3f61c21e647f33145cfd45b4449e0678fe65
- clm_69210465d4e48c55c184d3b0ee9154dca80b249543ef129e81d26fe77bdbce7e
- clm_8584bbe79eddc0ddec2ae35ed860cfa49f3d136d8cd9e6bedbd54cb2d0bed7bd
- clm_95a653ba569c170b4303dfea9742f8f672457d1cd8fe96567894ebf7a9ad2632
- clm_9a6af3e7ea044000ddd3793fdb33078ae900a109006e3725494cf3f174b4383b
- clm_a5186fdfe2d8d001b2c69f34b2d7fa52e1100420ca65e28d92d5c9fcc0bcf6be
- clm_ed8461dbe64fcabfaa6586e88ce08e6a69d0f87226846da8050a5f0d430ad37e
maturity: draft
page_id: pg_2bb54ca9d8d1518d998bbd6c5c428887
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_89f38b532cf45eef933013187117090c
title: fivetaku/kkirikkiri/README.md @ 99df0f40feb6
updated_at: '2026-09-14T01:49:09Z'
---

# fivetaku/kkirikkiri/README.md @ 99df0f40feb6

<!-- rcw:begin owner=source:src_89f38b532cf45eef933013187117090c block=evidence -->
- Teams write session-scoped files under .kkirikkiri/teams/{team_name}/ (TEAM_PLAN.md, TEAM_PROGRESS.md, TEAM_FINDINGS.md, report.md), while saved teams persist cross-session under .kkirikkiri/shared/saved-teams/. [@claim:clm_3f4af1bb55fb0e07df543d85bc12db5227e537ef3aa6ec865720210834dcb08d]
- The validation loop runs at most two rounds by default: round 1 is the original team, round 2 an auto-judge choosing keep, full replacement, or partial swap; further rounds need explicit approval. [@claim:clm_44b3ffddb82b45d500b26d1a11689fd4d67a34338ed0d2089e69bdfea443be95]
- Multi-model support appears to work by shelling out to installed external CLIs (Codex, agy, grok, gjc) with per-provider flags and model-override env vars like KKIRIKKIRI_GROK_MODEL. [@claim:clm_4eb4f4f0e76508af22b9aaa7e34e3254c8c9eb3aae69a2f908f27aa336195e19]
- The product is invoked via a /kkirikkiri slash command (e.g. '/kkirikkiri build me a research team') after installing from a plugin marketplace. [@claim:clm_5eda18cb33add8db489a45a606ee3f61c21e647f33145cfd45b4449e0678fe65]
- The opt-in preparation pilot generates cards and Agent requests from one approved plan but is explicitly not a runtime permission sandbox, and no OS sandbox or write serialization for concurrent sessions is newly guaranteed. [@claim:clm_69210465d4e48c55c184d3b0ee9154dca80b249543ef129e81d26fe77bdbce7e]
- Execution follows an eight-step pipeline: intent/preset matching, parallel environment scan, interview, team composition, user confirmation, shared-memory init, quality validation, and report collection. [@claim:clm_8584bbe79eddc0ddec2ae35ed860cfa49f3d136d8cd9e6bedbd54cb2d0bed7bd]
- kkirikkiri is a Claude Code plugin that takes a plain-language goal, asks only for missing decisions, scans the environment, and runs an approved agent team or Workflow. [@claim:clm_95a653ba569c170b4303dfea9742f8f672457d1cd8fe96567894ebf7a9ad2632]
- Two execution substrates are offered: a live collaborating Agent Teams mode or a deterministic Workflow pipeline for high-volume fan-out work; the user picks between them. [@claim:clm_9a6af3e7ea044000ddd3793fdb33078ae900a109006e3725494cf3f174b4383b]
- Requires Claude Code with the CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 env flag and Node.js; tmux is optional, and external CLIs (Codex, Antigravity agy, Grok) are optional since Claude alone can run the full team. [@claim:clm_a5186fdfe2d8d001b2c69f34b2d7fa52e1100420ca65e28d92d5c9fcc0bcf6be]
- Five built-in presets (Research, Development, Analysis, Content, Product/PM) are matched by natural-language trigger words and serve only as starting points for the final team. [@claim:clm_ed8461dbe64fcabfaa6586e88ce08e6a69d0f87226846da8050a5f0d430ad37e]
<!-- rcw:end owner=source:src_89f38b532cf45eef933013187117090c block=evidence -->

## Researcher notes

