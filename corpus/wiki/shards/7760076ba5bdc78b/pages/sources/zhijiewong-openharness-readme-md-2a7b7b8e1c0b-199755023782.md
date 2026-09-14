---
access: public
aliases: []
claim_ids:
- clm_1bfab95d3d0ae3a1f1660d5025f44dfbf513c8689493388a6334c6aeb265e6b2
- clm_24f75da01a2dca101067440596d7fa2c02b632cbc8ad12d1bc5d63c964d60ec8
- clm_4b026966063c841be8563b142340db25332ab4b85315e84fc42eb292d442f824
- clm_582d0f9430f74999e36290f847ab6e98cae2be8e35736deafd34ffd873e13cb5
- clm_6901a3eeeba93fd5f22256c8845e45193126359ecd6ee76efa0b8428af294142
- clm_a2788287c7c4f8d571ba203bee6463cddffc0a05c8fb5ee286ad94ca1e07f265
- clm_a4d8a6570f50e75501ab73af4c19f553aedc80216a843e8f7e13b1461b8cd1b7
- clm_c66d7969cfda218bf332c0482949fe05d97d87fc3114075bdb964b6f51e37037
- clm_ce4f6f84b207bf3f11471a53fdd220d2bd43b4c52a6090d36d0d9561f6e9ac32
- clm_df1e08f77300fa311a4c22cddae4357184c8557b375fcdcd4659444080ee71ea
maturity: draft
page_id: pg_85309ba8442f560daa5a199755023782
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_85932450c2dd523b82094e1cb8146f07
title: zhijiewong/openharness/README.md @ 2a7b7b8e1c0b
updated_at: '2026-09-14T03:27:27Z'
---

# zhijiewong/openharness/README.md @ 2a7b7b8e1c0b

<!-- rcw:begin owner=source:src_85932450c2dd523b82094e1cb8146f07 block=evidence -->
- The product ships 44 built-in tools across core file/shell operations (Bash, Read, Write, Edit, MultiEdit, Glob, Grep), web tools (WebFetch, WebSearch, ExaSearch), task tools, and agent tools (Agent, ParallelAgent, SendMessage), each labeled with a risk level. [@claim:clm_1bfab95d3d0ae3a1f1660d5025f44dfbf513c8689493388a6334c6aeb265e6b2]
- Scheduled cron tasks are created via /cron commands with schedules like 'every 5m'; a background executor checks every 60 seconds for due tasks, runs them via sub-queries, and stores results in ~/.oh/crons/history/. [@claim:clm_24f75da01a2dca101067440596d7fa2c02b632cbc8ad12d1bc5d63c964d60ec8]
- OpenHarness is a terminal AI coding agent installed via npm as @zhijiewang/openharness and launched with the `oh` command, with headless modes like `oh -p` and `oh run` for single-prompt CI/scripting use. [@claim:clm_4b026966063c841be8563b142340db25332ab4b85315e84fc42eb292d442f824]
- On session exit, memories not accessed in 30+ days lose 0.1 relevance per 30-day period, memories below 0.1 relevance are deleted, and consolidation is on by default (memory.consolidateOnExit). [@claim:clm_582d0f9430f74999e36290f847ab6e98cae2be8e35736deafd34ffd873e13cb5]
- Official Python (openharness-sdk via pip) and TypeScript (@zhijiewang/openharness-sdk) SDKs let programs drive `oh` with streaming events, stateful sessions, custom tools, permission callbacks, and session resume. [@claim:clm_6901a3eeeba93fd5f22256c8845e45193126359ecd6ee76efa0b8428af294142]
- The project targets Node.js 18+ with strict TypeScript, and the ACP integration depends on @agentclientprotocol/sdk as an optionalDependency that exits with an install hint if absent. [@claim:clm_a2788287c7c4f8d571ba203bee6463cddffc0a05c8fb5ee286ad94ca1e07f265]
- Sub-agent permission isolation: an Agent call's permission_mode override can only narrow the parent's mode, and less-restrictive requests are silently clamped; read-only roles like code-reviewer and security-auditor default to plan mode. [@claim:clm_a4d8a6570f50e75501ab73af4c19f553aedc80216a843e8f7e13b1461b8cd1b7]
- Agent roles (code-reviewer, test-writer, debugger, architect, editor, etc.) restrict sub-agents to role-specific tool sets, and an architect→editor two-pass workflow routes to powerful/fast model tiers when modelRouter is configured. [@claim:clm_c66d7969cfda218bf332c0482949fe05d97d87fc3114075bdb964b6f51e37037]
- An `oh acp` command speaks the Agent Client Protocol over stdin/stdout so ACP-capable editors (Zed, JetBrains via plugin, Cline, OpenCode) can drive the agent; permission prompts currently use OpenHarness's own flow rather than ACP's requestPermission path. [@claim:clm_ce4f6f84b207bf3f11471a53fdd220d2bd43b4c52a6090d36d0d9561f6e9ac32]
- Permission modes include ask (default), trust, deny, acceptEdits, plan, auto, and bypassPermissions; low-risk read-only tools auto-approve while medium/high-risk tools require confirmation in ask mode, and Bash commands undergo AST-based destructive-pattern analysis. [@claim:clm_df1e08f77300fa311a4c22cddae4357184c8557b375fcdcd4659444080ee71ea]
<!-- rcw:end owner=source:src_85932450c2dd523b82094e1cb8146f07 block=evidence -->

## Researcher notes

