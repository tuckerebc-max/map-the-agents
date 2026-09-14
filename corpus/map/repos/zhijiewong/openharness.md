# zhijiewong/openharness

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2a7b7b8e1c0b @ 6e6c76904ecf371f

## Summary (orientation draft, not independently verified)

Selected evidence records: OpenHarness is a terminal AI coding agent installed via npm as @zhijiewang/openharness and launched with the `oh` command, with headless modes like `oh -p` and `oh run` for single-prompt CI/scripting use. Official Python (openharness-sdk via pip) and TypeScript (@zhijiewang/openharness-sdk) SDKs let programs drive `oh` with streaming events, stateful sessions, custom tools, permission callbacks, and session resume.

## Source coverage

Source coverage (partial): 6 of 52 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product ships 44 built-in tools across core file/shell operations (Bash, Read, Write, Edit, MultiEdit, Glob, Grep), web tools (WebFetch, WebSearch, ExaSearch), task tools, and agent tools (Agent, ParallelAgent, SendMessage), each labeled with a risk level. -- evidence: [README.md#L24-L24](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L24-L24), [README.md#L155-L212](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L155-L212)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] OpenHarness is a terminal AI coding agent installed via npm as @zhijiewang/openharness and launched with the `oh` command, with headless modes like `oh -p` and `oh run` for single-prompt CI/scripting use. -- evidence: [README.md#L69-L78](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L69-L78), [README.md#L582-L582](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L582-L582), [README.md#L18-L18](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L18-L18), [README.md#L58-L61](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L58-L61)
  - [observation/documented] Official Python (openharness-sdk via pip) and TypeScript (@zhijiewang/openharness-sdk) SDKs let programs drive `oh` with streaming events, stateful sessions, custom tools, permission callbacks, and session resume. -- evidence: [README.md#L65-L65](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L65-L65), [README.md#L67-L67](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L67-L67)
- memory-state (1 claim(s)):
  - [observation/documented] On session exit, memories not accessed in 30+ days lose 0.1 relevance per 30-day period, memories below 0.1 relevance are deleted, and consolidation is on by default (memory.consolidateOnExit). -- evidence: [README.md#L500-L500](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L500-L500), [README.md#L508-L511](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L508-L511), [README.md#L502-L504](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L502-L504)
- orchestration (2 claim(s)):
  - [observation/documented] Agent roles (code-reviewer, test-writer, debugger, architect, editor, etc.) restrict sub-agents to role-specific tool sets, and an architect→editor two-pass workflow routes to powerful/fast model tiers when modelRouter is configured. -- evidence: [README.md#L550-L550](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L550-L550), [README.md#L559-L559](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L559-L559), [README.md#L536-L548](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L536-L548)
  - [observation/documented] Scheduled cron tasks are created via /cron commands with schedules like 'every 5m'; a background executor checks every 60 seconds for due tasks, runs them via sub-queries, and stores results in ~/.oh/crons/history/. -- evidence: [README.md#L524-L524](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L524-L524), [README.md#L519-L522](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L519-L522), [README.md#L526-L526](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L526-L526)
- tools-permissions (2 claim(s)):
  - [observation/documented] Permission modes include ask (default), trust, deny, acceptEdits, plan, auto, and bypassPermissions; low-risk read-only tools auto-approve while medium/high-risk tools require confirmation in ask mode, and Bash commands undergo AST-based destructive-pattern analysis. -- evidence: [README.md#L290-L290](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L290-L290), [README.md#L280-L288](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L280-L288), [README.md#L214-L214](https://github.com/zhijiewong/openharness/blob/2a7b7b8e1c0b132241d0eebb906dc86863ca19d8/README.md#L214-L214)
More evidence: [full detail](openharness.detail.md)

Metadata and full claim list: [full detail](openharness.detail.md)
Human notes ([notes](openharness.notes.md), never overwritten by build)

[Back to map index](../../index.md)
