---
access: public
aliases: []
claim_ids:
- clm_30069f15275d452ed3adeef6ab067285c2c290ebdf32ff136a404f2153bab3b5
- clm_44d2ebc2ec9121517ca04b2c3495f1b3a668c5cdf0a4c1098865e8d6e0e7b62a
- clm_4b5ebea99320ed718e66d8f900d41efa354c0574b40e587630488f157593c4fc
- clm_4bd3d2626c543b4d832986c940672ceafcb84cf531591ab66600be1de30d2890
- clm_5a97c930329a34a01bf7a27ab18273bc4361840f9a66e0d1b3d119d9bcfc7763
- clm_60ab6a9b3954be0be934d350a18f67118469a553e7673c08d5f8e233f6cb3f8f
- clm_748c5d52147da8c644d03b84bf835b940dc7c0ef05a3f991661d82c2213c5e04
- clm_87d9a52f336a0ea000f24aae8c24b78cce48bd0b19a6d5e3a29bda873a1fde1c
- clm_8c83d89a469af673baa1ef432d34bca764201e076df54f16c19633d969dc0edb
- clm_8d4c9acef5f939d6a6a664d9a038df0af9e30ea159ce3c01c315a1e02a8f7508
- clm_bfc1e9a3eeb768e83b78b3d782ee10fb82ce983ac61bf14b7881d94adba72995
- clm_cfd2231eaf340e692b62500ab7b3fdfd026e46bc7d121ceefe8590be1a667b87
maturity: draft
page_id: pg_2d68babe4e7250e295ebad7067edc9e3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a41d22b99daf5718afc756589744069d
title: LangLang03/LineCodePro/README.md @ 247903d320ec
updated_at: '2026-09-14T02:12:17Z'
---

# LangLang03/LineCodePro/README.md @ 247903d320ec

<!-- rcw:begin owner=source:src_a41d22b99daf5718afc756589744069d block=evidence -->
- Tools implement a BaseTool contract exposing name, description, category, a JSON argument schema, and an execute(JSONObject, ToolContext) returning a ToolResult. [@claim:clm_30069f15275d452ed3adeef6ab067285c2c290ebdf32ff136a404f2153bab3b5]
- Repository development practice: contributors must keep app code pure Java (Kotlin stdlib excluded from the runtime classpath), place code in the lowest-level fitting module, and run testDebugUnitTest, lintDebug, assembleDebug, and assembleRelease gates before sending a PR. [@claim:clm_44d2ebc2ec9121517ca04b2c3495f1b3a668c5cdf0a4c1098865e8d6e0e7b62a]
- LineCode Pro targets Android 8.0+ (API 26), is at version 1.2.8-max, is written in Java 11, and is licensed GPL-3.0-or-later. [@claim:clm_4b5ebea99320ed718e66d8f900d41efa354c0574b40e587630488f157593c4fc]
- The app is intentionally Java-only with no Kotlin runtime and no XML layouts, built entirely in Java 11 for transparency and reviewability. [@claim:clm_4bd3d2626c543b4d832986c940672ceafcb84cf531591ab66600be1de30d2890]
- Sub-agent tools (agent, agent_pipeline, agent_output) delegate work to another LLM loop, rendered with live progress cards. [@claim:clm_5a97c930329a34a01bf7a27ab18273bc4361840f9a66e0d1b3d119d9bcfc7763]
- Every file-touching tool routes paths through FileToolPathPolicy so the model acts only inside the opened workspace; shell commands run via Termux or an IPC provider, never in the app process. [@claim:clm_60ab6a9b3954be0be934d350a18f67118469a553e7673c08d5f8e233f6cb3f8f]
- Architecture: a single MainActivity hosts MainCoordinator (presenter) delegating to per-concern MVP controllers, with UI state flowing through ChatUiStateAssembler to ChatUiState to the view. [@claim:clm_748c5d52147da8c644d03b84bf835b940dc7c0ef05a3f991661d82c2213c5e04]
- The app id is cn.lineai and the project is a multi-module Gradle build with 14 modules plus :build-logic as a composite build. [@claim:clm_87d9a52f336a0ea000f24aae8c24b78cce48bd0b19a6d5e3a29bda873a1fde1c]
- ModelProtocolFactory dispatches on four protocol types: OPENAI_COMPATIBLE, CODEX_RESPONSES, ANTHROPIC_MESSAGES, and LOCAL_GGUF, each declaring capabilities like native tools and image support. [@claim:clm_8c83d89a469af673baa1ef432d34bca764201e076df54f16c19633d969dc0edb]
- Tool calls pass through PermissionModeController with automatic, confirmation, and read-only modes; confirmation supports one-time or persistent exact-match permissions scoped by mode, tool, command, and working directory. [@claim:clm_8d4c9acef5f939d6a6a664d9a038df0af9e30ea159ce3c01c315a1e02a8f7508]
- ContextCompactionService performs dynamic compaction at 50% (summarizing oldest 70%, keeping recent 30%) and 80% hard triggers, and durable knowledge saved via memory_update is reinjected next session. [@claim:clm_bfc1e9a3eeb768e83b78b3d782ee10fb82ce983ac61bf14b7881d94adba72995]
- Third-party libraries include jsch for SSH, commonmark (BSD-2) for Markdown rendering, and org.json (JSON License); tests use JUnit 4 and Robolectric 4.16. [@claim:clm_cfd2231eaf340e692b62500ab7b3fdfd026e46bc7d121ceefe8590be1a667b87]
<!-- rcw:end owner=source:src_a41d22b99daf5718afc756589744069d block=evidence -->

## Researcher notes

