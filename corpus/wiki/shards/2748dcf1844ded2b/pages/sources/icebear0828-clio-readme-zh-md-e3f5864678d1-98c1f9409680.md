---
access: public
aliases: []
claim_ids:
- clm_16bec364e7e037352e659ca34bc3aa2e5918d6cd68606fef919f5cb3274a7d7c
- clm_8b6f93f49c114a273f30f2627ebfe11f893c80e1e067b8fc94f1eab70c8754b1
- clm_c4038043727826f38921c5c9d1a95897b36834567bd72e748d4bd32b816ed702
maturity: draft
page_id: pg_5fe80863708b57afb7b898c1f9409680
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f90f79e676015f2499f556bf85fd5945
title: icebear0828/clio/README_zh.md @ e3f5864678d1
updated_at: '2026-09-14T02:04:27Z'
---

# icebear0828/clio/README_zh.md @ e3f5864678d1

<!-- rcw:begin owner=source:src_f90f79e676015f2499f556bf85fd5945 block=evidence -->
- The codebase appears organized into core engine modules (agent loop, streaming client, permissions, sandbox, session, settings) and a tools layer including checkpoint, hooks, MCP, LSP, subagent, tasks, teams, and worktree files. [@claim:clm_16bec364e7e037352e659ca34bc3aa2e5918d6cd68606fef919f5cb3274a7d7c]
- Sub-agents support background execution via run_in_background with completion notifications, and can run in isolated git worktrees; agent teams enable messaging between agents. [@claim:clm_8b6f93f49c114a273f30f2627ebfe11f893c80e1e067b8fc94f1eab70c8754b1]
- The CLI supports OpenAI-compatible endpoints and custom gateways via --api-format openai and --api-url, in addition to the default direct Anthropic API connection. [@claim:clm_c4038043727826f38921c5c9d1a95897b36834567bd72e748d4bd32b816ed702]
<!-- rcw:end owner=source:src_f90f79e676015f2499f556bf85fd5945 block=evidence -->

## Researcher notes

