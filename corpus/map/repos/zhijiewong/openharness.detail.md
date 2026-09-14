# zhijiewong/openharness -- full detail

[Back to orientation](openharness.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhijiewong/openharness/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/6e6c76904ecf371f.json](../../../wiki/dossiers/zhijiewong/openharness/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/6e6c76904ecf371f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product ships 44 built-in tools across core file/shell operations (Bash, Read, Write, Edit, MultiEdit, Glob, Grep), web tools (WebFetch, WebSearch, ExaSearch), task tools, and agent tools (Agent, ParallelAgent, SendMessage), each labeled with a risk level. -- evidence: [README.md#L24-L24](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L24-L24), [README.md#L155-L212](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L155-L212) (`clm_1bfab95d3d0ae3a1f1660d5025f44dfbf513c8689493388a6334c6aeb265e6b2`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] OpenHarness is a terminal AI coding agent installed via npm as @zhijiewang/openharness and launched with the `oh` command, with headless modes like `oh -p` and `oh run` for single-prompt CI/scripting use. -- evidence: [README.md#L69-L78](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L69-L78), [README.md#L582-L582](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L582-L582), [README.md#L18-L18](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L18-L18), [README.md#L58-L61](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L58-L61) (`clm_4b026966063c841be8563b142340db25332ab4b85315e84fc42eb292d442f824`)
- [observation/documented] Official Python (openharness-sdk via pip) and TypeScript (@zhijiewang/openharness-sdk) SDKs let programs drive `oh` with streaming events, stateful sessions, custom tools, permission callbacks, and session resume. -- evidence: [README.md#L65-L65](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L65-L65), [README.md#L67-L67](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L67-L67) (`clm_6901a3eeeba93fd5f22256c8845e45193126359ecd6ee76efa0b8428af294142`)
- [observation/documented] An `oh acp` command speaks the Agent Client Protocol over stdin/stdout so ACP-capable editors (Zed, JetBrains via plugin, Cline, OpenCode) can drive the agent; permission prompts currently use OpenHarness's own flow rather than ACP's requestPermission path. -- evidence: [README.md#L721-L721](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L721-L721), [README.md#L714-L714](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L714-L714) (`clm_ce4f6f84b207bf3f11471a53fdd220d2bd43b4c52a6090d36d0d9561f6e9ac32`)

## memory-state (1 claim(s))

- [observation/documented] On session exit, memories not accessed in 30+ days lose 0.1 relevance per 30-day period, memories below 0.1 relevance are deleted, and consolidation is on by default (memory.consolidateOnExit). -- evidence: [README.md#L500-L500](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L500-L500), [README.md#L508-L511](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L508-L511), [README.md#L502-L504](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L502-L504) (`clm_582d0f9430f74999e36290f847ab6e98cae2be8e35736deafd34ffd873e13cb5`)

## orchestration (2 claim(s))

- [observation/documented] Agent roles (code-reviewer, test-writer, debugger, architect, editor, etc.) restrict sub-agents to role-specific tool sets, and an architect→editor two-pass workflow routes to powerful/fast model tiers when modelRouter is configured. -- evidence: [README.md#L550-L550](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L550-L550), [README.md#L559-L559](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L559-L559), [README.md#L536-L548](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L536-L548) (`clm_c66d7969cfda218bf332c0482949fe05d97d87fc3114075bdb964b6f51e37037`)
- [observation/documented] Scheduled cron tasks are created via /cron commands with schedules like 'every 5m'; a background executor checks every 60 seconds for due tasks, runs them via sub-queries, and stores results in ~/.oh/crons/history/. -- evidence: [README.md#L524-L524](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L524-L524), [README.md#L519-L522](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L519-L522), [README.md#L526-L526](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L526-L526) (`clm_24f75da01a2dca101067440596d7fa2c02b632cbc8ad12d1bc5d63c964d60ec8`)

## tools-permissions (2 claim(s))

- [observation/documented] Permission modes include ask (default), trust, deny, acceptEdits, plan, auto, and bypassPermissions; low-risk read-only tools auto-approve while medium/high-risk tools require confirmation in ask mode, and Bash commands undergo AST-based destructive-pattern analysis. -- evidence: [README.md#L290-L290](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L290-L290), [README.md#L280-L288](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L280-L288), [README.md#L214-L214](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L214-L214) (`clm_df1e08f77300fa311a4c22cddae4357184c8557b375fcdcd4659444080ee71ea`)
- [observation/documented] Sub-agent permission isolation: an Agent call's permission_mode override can only narrow the parent's mode, and less-restrictive requests are silently clamped; read-only roles like code-reviewer and security-auditor default to plan mode. -- evidence: [README.md#L578-L578](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L578-L578), [README.md#L569-L569](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L569-L569), [README.md#L576-L576](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L576-L576) (`clm_a4d8a6570f50e75501ab73af4c19f553aedc80216a843e8f7e13b1461b8cd1b7`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project targets Node.js 18+ with strict TypeScript, and the ACP integration depends on @agentclientprotocol/sdk as an optionalDependency that exits with an install hint if absent. -- evidence: [README.md#L721-L721](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L721-L721), [README.md#L24-L24](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L24-L24) (`clm_a2788287c7c4f8d571ba203bee6463cddffc0a05c8fb5ee286ad94ca1e07f265`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

