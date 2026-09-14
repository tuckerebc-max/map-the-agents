---
access: public
aliases: []
claim_ids:
- clm_1192ffa2a0b37a5f49036b982808435da98179b1ba564a4060a730681bc54fd9
- clm_151fecd3080948373995600bdc6cb29b510fa7a749b800a779195f456ede6f6d
- clm_1dcdc63e0b306bc32504e6487a26dff5b33cb09c14ff7288268066fa044792ef
- clm_25dedae062db33f48b086cf033d401372ff7b4b961011193e3ff2d92757f434b
- clm_3bd926cec47597347e1d73170fc26ff710f62d56582fc9e0d1bdee8f8c075a1c
- clm_45fcb1e2be6be76bde1a434255bf5684a9000faa50e24bd3d425e63561ac18d0
- clm_6955a29490e77e71088d227e93fe5d0786620084183b10016f28d4c783a84cc6
- clm_d8727f401d90c41b4239a85badb49140e61e0990e207e57a8f1b920e14dc0719
- clm_da09fcdeff3423c53e946475022543cc61c9be01abc1ef595ad4091e7dc83b33
- clm_e507b5c7998c2f0f364ad1da2f9472da73c332808025439167c2af55d341a5ed
maturity: draft
page_id: pg_5e8899380b405e5d8459ce1b6a5447c1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a0e4a178f84d5963bfe2fae9ef3271ff
title: ZYKJShadow/Async/README.md @ 2c18a43c0711
updated_at: '2026-09-14T03:28:21Z'
---

# ZYKJShadow/Async/README.md @ 2c18a43c0711

<!-- rcw:begin owner=source:src_a0e4a178f84d5963bfe2fae9ef3271ff block=evidence -->
- The Composer offers four modes: Agent (full auto), Plan (review before run), Ask (read-only Q&A), and Debug (systematic troubleshooting). [@claim:clm_1192ffa2a0b37a5f49036b982808435da98179b1ba564a4060a730681bc54fd9]
- Repository development practice: the repo can be run with npm install then npm run desktop, with dev, dev:debug, and icons scripts; the macOS test guide documents building unsigned packages via npm run release:mac:unsigned. [@claim:clm_151fecd3080948373995600bdc6cb29b510fa7a749b800a779195f456ede6f6d]
- The app bridges to Telegram, Slack, Discord, and Feishu bots; inbound messages run through botRuntime, reusing the same agentLoop and teamOrchestrator paths as the desktop Composer, with per-integration model, workspace, and allowlist config. [@claim:clm_1dcdc63e0b306bc32504e6487a26dff5b33cb09c14ff7288268066fa044792ef]
- The main process contains agentLoop.ts (multi-round tool calls, partial JSON streaming, tool repair, aborts), toolExecutor, LLM adapters, gitService, threadStore, settingsStore, LSP session, and PTY terminal. [@claim:clm_25dedae062db33f48b086cf033d401372ff7b4b961011193e3ff2d92757f434b]
- The app is built from scratch on Electron + React + Monaco and is explicitly not a VS Code fork, with a deliberately lean two-process architecture and clear IPC boundaries. [@claim:clm_3bd926cec47597347e1d73170fc26ff710f62d56582fc9e0d1bdee8f8c075a1c]
- Team mode provides multi-agent collaboration with a Lead planning, specialist execution, reviewer verification, and plan-approval workflows; nested and background sub-agents are supported. [@claim:clm_45fcb1e2be6be76bde1a434255bf5684a9000faa50e24bd3d425e63561ac18d0]
- Threads, settings, and plans persist locally as JSON/Markdown under Electron userData (threads.json, settings.json, .async/plans/); threads.json is the authoritative conversation source. [@claim:clm_6955a29490e77e71088d227e93fe5d0786620084183b10016f28d4c783a84cc6]
- Async IDE is an open-source, agent-first desktop workspace combining Agent, editor, Git, and terminal, licensed Apache 2.0, local-first with BYOK model access. [@claim:clm_d8727f401d90c41b4239a85badb49140e61e0990e207e57a8f1b920e14dc0719]
- Sensitive operations such as shell commands and file writes pass through approval gates, and the renderer's access to main-process capabilities is bounded by a preload whitelist. [@claim:clm_da09fcdeff3423c53e946475022543cc61c9be01abc1ef595ad4091e7dc83b33]
- The tech stack includes Electron 41, React 19, TypeScript 5.9, Monaco 0.52, xterm.js, OpenAI/Anthropic/Gemini SDKs, MCP SDK, and node-pty. [@claim:clm_e507b5c7998c2f0f364ad1da2f9472da73c332808025439167c2af55d341a5ed]
<!-- rcw:end owner=source:src_a0e4a178f84d5963bfe2fae9ef3271ff block=evidence -->

## Researcher notes

