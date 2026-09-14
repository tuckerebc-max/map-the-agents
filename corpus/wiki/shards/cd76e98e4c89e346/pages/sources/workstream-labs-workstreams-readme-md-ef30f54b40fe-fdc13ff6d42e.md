---
access: public
aliases: []
claim_ids:
- clm_040a80a5f2e20aa741c539c25213ff0864db55762df1eb1ccafe8aa6ef50c08b
- clm_048a6eae2350834a948877ff5b4f0f3431d66b73e6785d9f53c969172ec35d99
- clm_089206d0451d8d43c51a4557030254f40a5b5be51271b4cd43615de5fb537a71
- clm_1b3c529982c492b4553b00a69c106edd15de05b871a3d8136191bd39d4be1141
- clm_213b19c0d2513292ea35d7c73c15da5f706ba1c68b51a702a9b2388535d65e09
- clm_225a7453cc4fbe74be088ceb941184b33e133b7ff7b58a2eb391c9834e2579c6
- clm_3cb340164dbe4116e1235090f0b1e66fd8c273bdffb2247313f8b9b509bda963
- clm_453f7343d96facf90ca6b6c523e32536b7d398b751f12370e6c3132c71bf03fc
- clm_7864cacbe35ca983fa3a01bd85fffa5ed6fd9bfd90f0e05c31a252523173821f
- clm_db28710bcf2c03063fa5a081cde8afa3aeecff4c3aceac7498c2b175be4809c3
maturity: draft
page_id: pg_738babfd31bb511e8ae8fdc13ff6d42e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_21d1c00d94d959448df32227df7f91f9
title: workstream-labs/workstreams/README.md @ ef30f54b40fe
updated_at: '2026-09-14T03:23:41Z'
---

# workstream-labs/workstreams/README.md @ ef30f54b40fe

<!-- rcw:begin owner=source:src_21d1c00d94d959448df32227df7f91f9 block=evidence -->
- The app is not yet signed with an Apple certificate, so users must strip the macOS quarantine flag with xattr to avoid a misleading 'damaged app' error. [@claim:clm_040a80a5f2e20aa741c539c25213ff0864db55762df1eb1ccafe8aa6ef50c08b]
- The project ships as a macOS desktop app distributed via DMG installers for Apple Silicon (arm64) and Intel (x64), with built-in auto-update. [@claim:clm_048a6eae2350834a948877ff5b4f0f3431d66b73e6785d9f53c969172ec35d99]
- Claude Code lifecycle events (idle, working, awaiting permission, ready for review) are tracked per worktree via hooks and shown as animated sidebar status indicators. [@claim:clm_089206d0451d8d43c51a4557030254f40a5b5be51271b4cd43615de5fb537a71]
- The product is agent-agnostic and reportedly works with Claude, Codex, Aider, and other agents. [@claim:clm_1b3c529982c492b4553b00a69c106edd15de05b871a3d8136191bd39d4be1141]
- Each workstream is defined with a natural-language prompt and an agent choice, and gets its own isolated git worktree. [@claim:clm_213b19c0d2513292ea35d7c73c15da5f706ba1c68b51a702a9b2388535d65e09]
- Workstreams is described as an IDE for orchestrating parallel AI coding agents, each running in an isolated git worktree. [@claim:clm_225a7453cc4fbe74be088ceb941184b33e133b7ff7b58a2eb391c9834e2579c6]
- Users can leave inline comments on split-side diffs and send them to Claude as structured prompts containing file path, line number, and diff context. [@claim:clm_3cb340164dbe4116e1235090f0b1e66fd8c273bdffb2247313f8b9b509bda963]
- An orchestrator sidebar manages multiple git worktrees per repository, showing real-time addition/deletion counts and preserving per-worktree terminals, editors, and state. [@claim:clm_453f7343d96facf90ca6b6c523e32536b7d398b751f12370e6c3132c71bf03fc]
- A CLI named `ws` (in apps/cli) supports commands such as init, create, run, and dashboard for terminal-driven workstream management. [@claim:clm_7864cacbe35ca983fa3a01bd85fffa5ed6fd9bfd90f0e05c31a252523173821f]
- Running the project requires macOS, Node.js 22, Git, and Bun for CLI installation. [@claim:clm_db28710bcf2c03063fa5a081cde8afa3aeecff4c3aceac7498c2b175be4809c3]
<!-- rcw:end owner=source:src_21d1c00d94d959448df32227df7f91f9 block=evidence -->

## Researcher notes

