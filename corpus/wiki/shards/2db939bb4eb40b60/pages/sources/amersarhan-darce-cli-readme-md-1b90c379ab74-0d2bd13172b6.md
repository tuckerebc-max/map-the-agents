---
access: public
aliases: []
claim_ids:
- clm_3eea4d1e37df684178bd9aa458e9d7bc2153fb9c2495a34faceb35469baa8d35
- clm_7d8bb49228aadd062f9e7a4bf2e4410d450139625f3ca20f51a65ca998436d57
- clm_995cc8bc0a92f10e884a566b4cc04a29fd2f1c0402e50d2f6ac6bcec4a363058
- clm_a28056f839c4244b52d90f7058d57468c1f2bf260097de78c8a9ff9688e0edb0
- clm_a96bb98da3278e45ce7dc196fbcf76992aa1515b25d7f3d03358eba4d1ceb4b8
- clm_d30c239a92aa26218763f43ce2c6da99f3be9f22cb6da7a3158403b6a45455d5
- clm_d58b422f60ea95bb5f62e1384d7570ba327c91945f5dc53cee24002505aa4f11
- clm_d96a9c1a7ad601b41374b93b05b64a7269974ddc2f50181c8fdfd1a426e85222
- clm_ef882d174a7fffcdd62a5fbc18dfa1876acec6fcbc55e006bd10c22a70162e85
- clm_f332c2f32c4cf436c358ceba75d88f3f38b6a20c408c71fc4172ccc67a940194
- clm_f345526639d0995f70da8a862e65e4c7eca172db661bd857947a1a30fdfc0039
maturity: draft
page_id: pg_580e654f6b1f59aaa4980d2bd13172b6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5b993453bf495e249f5f9762f2459fb8
title: AmerSarhan/darce-cli/README.md @ 1b90c379ab74
updated_at: '2026-09-14T01:33:23Z'
---

# AmerSarhan/darce-cli/README.md @ 1b90c379ab74

<!-- rcw:begin owner=source:src_5b993453bf495e249f5f9762f2459fb8 block=evidence -->
- The tool is git-aware, tracking branch, changes, and recent commits, and supports session resume via 'darce --resume' plus context compaction for long conversations. [@claim:clm_3eea4d1e37df684178bd9aa458e9d7bc2153fb9c2495a34faceb35469baa8d35]
- Darce is a terminal AI coding agent that reads, writes, and edits code, runs shell commands, and searches codebases, positioning itself against Claude Code, Cursor, and Copilot CLI. [@claim:clm_7d8bb49228aadd062f9e7a4bf2e4410d450139625f3ca20f51a65ca998436d57]
- Darce includes smart routing that automatically picks a model per task, and users can override routing with rules in a ~/.darcerc config file mapping conditions like large-context or complex-reasoning to specific models. [@claim:clm_995cc8bc0a92f10e884a566b4cc04a29fd2f1c0402e50d2f6ac6bcec4a363058]
- The agent provides seven tools: Read, Write, Edit, Bash, Glob, Grep, and WebFetch, plus keyboard shortcuts like Ctrl+M for model switching and triple-quote multi-line input. [@claim:clm_a28056f839c4244b52d90f7058d57468c1f2bf260097de78c8a9ff9688e0edb0]
- Tool access is tier-gated: the free Starter plan limits users to 3 tools (Read, Grep, Glob) while paid tiers unlock all 7 tools, and resume/history is paid-only. [@claim:clm_a96bb98da3278e45ce7dc196fbcf76992aa1515b25d7f3d03358eba4d1ceb4b8]
- Repository development practice: contributors clone the repo, run npm install, use 'npm run dev' to run from source, run tests with 'npx tsx test.ts' (106 tests), and build with 'npm run build'. [@claim:clm_d30c239a92aa26218763f43ce2c6da99f3be9f22cb6da7a3158403b6a45455d5]
- The product routes to multiple external models, listing qwen3-coder (default), grok-4.1-fast, claude-sonnet-4, gemini-2.5-pro, deepseek-r1, deepseek-chat, and llama-4-maverick. [@claim:clm_d58b422f60ea95bb5f62e1384d7570ba327c91945f5dc53cee24002505aa4f11]
- The CLI exposes slash commands including /help, /model, /clear, /cost, /compact, and /quit, with short aliases such as /m, /c, and /q. [@claim:clm_d96a9c1a7ad601b41374b93b05b64a7269974ddc2f50181c8fdfd1a426e85222]
- No agent performance benchmarks or eval harness appear in the evidence; the only test-related content is the repository's own test suite instructions, so evaluation capability appears undocumented. [@claim:clm_ef882d174a7fffcdd62a5fbc18dfa1876acec6fcbc55e006bd10c22a70162e85]
- The product tracks real-time token count and spend in a status bar and offers an account dashboard for usage stats. [@claim:clm_f332c2f32c4cf436c358ceba75d88f3f38b6a20c408c71fc4172ccc67a940194]
- Installation and startup are via npm global install of darce-cli followed by 'darce login' and 'darce'; the README states no config files, API keys, or Docker are needed to start. [@claim:clm_f345526639d0995f70da8a862e65e4c7eca172db661bd857947a1a30fdfc0039]
<!-- rcw:end owner=source:src_5b993453bf495e249f5f9762f2459fb8 block=evidence -->

## Researcher notes

