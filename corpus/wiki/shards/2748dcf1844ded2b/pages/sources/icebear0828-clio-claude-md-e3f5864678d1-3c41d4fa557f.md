---
access: public
aliases: []
claim_ids:
- clm_40269df1a87035cb15ce359a2152659fe937197ff90cb229dfbcb93506620f2e
- clm_6b52e39c7a437d1c026f0486fe732f30933c74b9d27a8085c26ac857e4962295
- clm_f14ae4102753168e6be3ecb5af255f53bc439c3851cfa706783c60d7b1ee159b
maturity: draft
page_id: pg_7981db2fa3165a988cf53c41d4fa557f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_abda8853b81056c6b63a75a5670a8d7f
title: icebear0828/clio/CLAUDE.md @ e3f5864678d1
updated_at: '2026-09-14T02:04:27Z'
---

# icebear0828/clio/CLAUDE.md @ e3f5864678d1

<!-- rcw:begin owner=source:src_abda8853b81056c6b63a75a5670a8d7f block=evidence -->
- Repository development practice: autonomous git workflow requires feature branches and PRs (never pushing directly to master), conventional commits, and a self-review sub-agent that approves or requests changes via gh. [@claim:clm_40269df1a87035cb15ce359a2152659fe937197ff90cb229dfbcb93506620f2e]
- Repository development practice: the project is intended for self-modification by Clio (dogfooding), with .clio/settings.json hooks running tsc and test gates after edits and writes, and a 3-strike rollback rule. [@claim:clm_6b52e39c7a437d1c026f0486fe732f30933c74b9d27a8085c26ac857e4962295]
- Repository development practice: CLAUDE.md instructs contributors to run npm run dev/build/test (vitest), keep TypeScript strict with no any, use ESM .js import extensions, and add tests per module. [@claim:clm_f14ae4102753168e6be3ecb5af255f53bc439c3851cfa706783c60d7b1ee159b]
<!-- rcw:end owner=source:src_abda8853b81056c6b63a75a5670a8d7f block=evidence -->

## Researcher notes

