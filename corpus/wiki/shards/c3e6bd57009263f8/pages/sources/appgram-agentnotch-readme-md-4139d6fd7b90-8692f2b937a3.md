---
access: public
aliases: []
claim_ids:
- clm_817ed53aec442a58714f7809a1982bd928b90ae8b76ae159ec9985a691910376
- clm_858c27e5d26e29cb26e3c4d4e3d6b4447c406d960950758b337e6c5540a1110f
- clm_8a740c83509cc83ddad02d3cc4c7c93bf976ef69764cc9532c1807e8aa04c948
- clm_9204fe28077a4be0046b5a92615e3333a50b4c1a3b2ae648c3efb5b1c9a86113
- clm_93ad087c73b2e4ad0a0cd26fb337fca4c976d96032103c0c18a572db6bb38876
- clm_9c4de1b06419279be53299c021ceabf2edfb1c31eff7aec211a835f19d8969ac
- clm_a513571ac9ce6d547062ef3a2b07ce169155c377278a04ae9f70bc1c4480a311
- clm_ab84cdaf8beb71041bc73008cf0edf9a15af49b68c46d92ce04bdf6ce5db281e
- clm_c83d00eb55f0b673b43970a6c098112d6538d80890a19b311a9a38d7d4cb9b8b
maturity: draft
page_id: pg_965dd63578d05d36a3848692f2b937a3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9d4bfd1c71c051169ab1ed346b13e254
title: AppGram/agentnotch/README.md @ 4139d6fd7b90
updated_at: '2026-09-14T03:35:20Z'
---

# AppGram/agentnotch/README.md @ 4139d6fd7b90

<!-- rcw:begin owner=source:src_9d4bfd1c71c051169ab1ed346b13e254 block=evidence -->
- It tracks input/output token usage and estimated costs in real time, and notifies the user when an assistant finishes a task. [@claim:clm_817ed53aec442a58714f7809a1982bd928b90ae8b76ae159ec9985a691910376]
- Requires macOS 14.0 (Sonoma) or later; on non-notch Macs the app falls back to the menu bar. [@claim:clm_858c27e5d26e29cb26e3c4d4e3d6b4447c406d960950758b337e6c5540a1110f]
- Source-aware color coding distinguishes assistants: orange for Claude Code, blue for Codex, and light blue for unknown sources. [@claim:clm_8a740c83509cc83ddad02d3cc4c7c93bf976ef69764cc9532c1807e8aa04c948]
- The app runs entirely locally, sending no data anywhere; it only receives telemetry from local AI tools. [@claim:clm_9204fe28077a4be0046b5a92615e3333a50b4c1a3b2ae648c3efb5b1c9a86113]
- AgentNotch is a macOS menu bar app that lives in the Mac's notch and shows real-time telemetry from Claude Code and OpenAI Codex sessions. [@claim:clm_93ad087c73b2e4ad0a0cd26fb337fca4c976d96032103c0c18a572db6bb38876]
- Interaction model: the notch indicator expands on hover to show recent tool calls, and clicking opens a full view with token breakdown and settings. [@claim:clm_9c4de1b06419279be53299c021ceabf2edfb1c31eff7aec211a835f19d8969ac]
- The app displays each tool call as it happens, including file reads, code edits, and shell commands. [@claim:clm_a513571ac9ce6d547062ef3a2b07ce169155c377278a04ae9f70bc1c4480a311]
- Display is configurable: token counts, cost estimates, source filtering (Claude/Codex), and the menu bar icon can be toggled. [@claim:clm_ab84cdaf8beb71041bc73008cf0edf9a15af49b68c46d92ce04bdf6ce5db281e]
- AgentNotch listens for OTLP/HTTP on port 4318 by default and decodes OTLP logs (/v1/logs) and metrics (/v1/metrics). [@claim:clm_c83d00eb55f0b673b43970a6c098112d6538d80890a19b311a9a38d7d4cb9b8b]
<!-- rcw:end owner=source:src_9d4bfd1c71c051169ab1ed346b13e254 block=evidence -->

## Researcher notes

