---
access: public
aliases: []
claim_ids:
- clm_1c670e34e6b9c69d0e2ee32123e7192ff5aec08d3d8dd7d05537f2c5bb8473ca
- clm_253c50f7f0225a6bef01fb1103d26154a5cca98057d9ef0dd5fea2de3111677f
- clm_31ef6244862bc709729aed83ece8c1b746bbd0c7a535af1539b829750d498e84
- clm_4045cbc87953f2c5ec04e42aa6a9f0bd67fc7e1d34d20d43ae44827b13b42a77
- clm_44c3166fc8505eaa9932da57e432394649fb40b2a15c7cb52e50c9d164e5fdfc
- clm_57fb6157afd3c0dbb4d46ad23f796ee4cea74f251cdd76496b2eb5ce90021b00
- clm_75cf532ff4c887ec864560f8036d354d79a206bdcd580e93a910bc65d9d052c9
- clm_9a0121c1ee5328eb5810974e4f291e190d8510fb5559d18b000a65336f0cd78b
- clm_9a08c5d1988fd4fb42657cb85a7ccaceb55dcced7ae2070c3296b9eb07a53d94
- clm_d57c855cabaf32f9c107aaeded378a9909e258a1d3d4bc6ca20ee3e979ebd5c7
- clm_e503dbd2ed75c7658f7ddf87c196fc2e6291cbd052a168000735f39a19ec893b
- clm_f6b04680f526d06708e644c382a79f806d73e6abb428163f83346a458c70e5c6
maturity: draft
page_id: pg_e328d5a7a5485e7fbbd700531397031c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5fec8663ff305b8f89bf793db9b93869
title: timwuhaotian/the-pair/README.md @ 8d678875f777
updated_at: '2026-09-14T03:19:47Z'
---

# timwuhaotian/the-pair/README.md @ 8d678875f777

<!-- rcw:begin owner=source:src_5fec8663ff305b8f89bf793db9b93869 block=evidence -->
- Full automation mode operates with workspace-scoped permissions, and each pair stores its own runtime permissions under .pair/runtime/<pairId>/; global opencode permissions are not modified — permissions are session-specific. [@claim:clm_1c670e34e6b9c69d0e2ee32123e7192ff5aec08d3d8dd7d05537f2c5bb8473ca]
- The Pair is a free, open-source desktop app running two AI coding agents: a read-only Mentor that plans and reviews, and an Executor that writes code and runs commands, cross-checking each other's work. [@claim:clm_253c50f7f0225a6bef01fb1103d26154a5cca98057d9ef0dd5fea2de3111677f]
- The tech stack is Tauri 2.x with a Rust backend, React 19 + TypeScript frontend, Tailwind CSS v4, Zustand state, Framer Motion, and Lucide React icons. [@claim:clm_31ef6244862bc709729aed83ece8c1b746bbd0c7a535af1539b829750d498e84]
- The agent workflow loops through Mentoring, Executing, and Reviewing stages, and runs are capped at a flat 20-iteration default, pausing for human review when the budget is reached. [@claim:clm_4045cbc87953f2c5ec04e42aa6a9f0bd67fc7e1d34d20d43ae44827b13b42a77]
- Session snapshots are saved automatically; on relaunch the app detects interrupted sessions and offers to restore them with full conversation history and turn state. [@claim:clm_44c3166fc8505eaa9932da57e432394649fb40b2a15c7cb52e50c9d164e5fdfc]
- The documented Rust backend includes PairManager (lifecycle), MessageBroker (state machine), ProcessSpawner (multi-provider), ContextBridge, QualityGate, SmartPause, Git Tracker, Worktrees, Session Snapshot, Resource Monitoring, Acceptance, and Report Generator modules. [@claim:clm_57fb6157afd3c0dbb4d46ad23f796ee4cea74f251cdd76496b2eb5ce90021b00]
- Repository development practice: the README's Development section documents npm scripts for building and testing, including npm test for JS and Rust unit tests, typecheck, lint, e2e, and platform-specific build commands. [@claim:clm_75cf532ff4c887ec864560f8036d354d79a206bdcd580e93a910bc65d9d052c9]
- Coordination features include structured handoff prompts, quality gates, smart-pause logic, and a per-turn step-cycle guard that kills runaway agent processes to prevent CPU exhaustion. [@claim:clm_9a0121c1ee5328eb5810974e4f291e190d8510fb5559d18b000a65336f0cd78b]
- The app requires at least one AI provider CLI (opencode, Claude Code, Codex, Antigravity, or Kimi Code); Codex, Claude, Gemini, and Kimi are detected from installed CLIs and sign-in state. [@claim:clm_9a08c5d1988fd4fb42657cb85a7ccaceb55dcced7ae2070c3296b9eb07a53d94]
- Besides the desktop app, a terminal CLI edition called Pair Code is available on npm (installable globally via npm install -g pair-code), sharing the same Mentor + Executor design. [@claim:clm_d57c855cabaf32f9c107aaeded378a9909e258a1d3d4bc6ca20ee3e979ebd5c7]
- The product is model-agnostic: it can pair provider CLIs including opencode, Claude Code, OpenAI Codex, Gemini CLI, and Kimi Code in any combination, plus local models via Ollama. [@claim:clm_e503dbd2ed75c7658f7ddf87c196fc2e6291cbd052a168000735f39a19ec893b]
- No benchmark or agent-performance evaluation harness appears in the provided evidence; the only test-related material is the repository's own unit/e2e test scripts, so agent task performance appears unmeasured in this snapshot. [@claim:clm_f6b04680f526d06708e644c382a79f806d73e6abb428163f83346a458c70e5c6]
<!-- rcw:end owner=source:src_5fec8663ff305b8f89bf793db9b93869 block=evidence -->

## Researcher notes

