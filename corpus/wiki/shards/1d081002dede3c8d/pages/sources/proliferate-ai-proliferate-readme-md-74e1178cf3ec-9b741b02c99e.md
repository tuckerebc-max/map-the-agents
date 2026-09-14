---
access: public
aliases: []
claim_ids:
- clm_0a5daf5425c05a5d90c20acd36298fc82f5385990338bed296d039f46c0b45f6
- clm_1f00b19537f6de34a749521d8ed2f818035f6f3f3795eb069f4c307a33b4d3aa
- clm_54ee03fd46a4d5c4b24f81c15a7d667ea0f7c2c946c83b136489901f38453b8f
- clm_61f086cb72c79561e1f76cadccefc1f2acf6b6bc323fcf9b3d3571bdd7bf14d9
- clm_71e9505bff09d8c05b54d1647db971f35521595d861603fff6254abb2f10d467
- clm_96a22697aa3f93d1d23d10c2481806e4737e36f6f05a15e0c72863573b48c793
- clm_9fd1c5cbdbfb144a212faa2119164de0f12ac8835137f8fb81df4bd087e07515
- clm_fb5b041378797d93948cb5e82e19cd47ee45e5fea8e6fe1619120bd278ff7c23
maturity: draft
page_id: pg_ea7252f0ea085c818e299b741b02c99e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e7117f6f3c0555659f1e6c35e151a185
title: proliferate-ai/proliferate/README.md @ 74e1178cf3ec
updated_at: '2026-09-14T02:32:29Z'
---

# proliferate-ai/proliferate/README.md @ 74e1178cf3ec

<!-- rcw:begin owner=source:src_e7117f6f3c0555659f1e6c35e151a185 block=evidence -->
- The control plane is self-hostable; the Docker Compose guide runs Caddy, Postgres, and the API with bootstrap and update scripts, and an AWS option uses a CloudFormation wrapper on EC2. [@claim:clm_0a5daf5425c05a5d90c20acd36298fc82f5385990338bed296d039f46c0b45f6]
- Proliferate runs coding agents such as Claude Code, Codex, OpenCode, Cursor, and Grok through each agent's native harness. [@claim:clm_1f00b19537f6de34a749521d8ed2f818035f6f3f3795eb069f4c307a33b4d3aa]
- Repository development practice: local full-stack development additionally needs Python 3.12+, uv, and Docker, using named dev profiles when multiple worktrees run concurrently. [@claim:clm_54ee03fd46a4d5c4b24f81c15a7d667ea0f7c2c946c83b136489901f38453b8f]
- The product advertises recurring and event-driven agent workflows, such as nightly review passes, alert triage, and dependency bumps. [@claim:clm_61f086cb72c79561e1f76cadccefc1f2acf6b6bc323fcf9b3d3571bdd7bf14d9]
- The product supports subagents that delegate scoped work to child agents, plus integrations including MCPs, skills, Computer Use, Browser Use, and custom tools shared across agents. [@claim:clm_71e9505bff09d8c05b54d1647db971f35521595d861603fff6254abb2f10d467]
- Repository development practice: running from source requires Rust stable, Node.js 22+, and pnpm, with 'make install' and 'make dev-local' to launch the desktop app with the bundled local AnyHarness runtime. [@claim:clm_96a22697aa3f93d1d23d10c2481806e4737e36f6f05a15e0c72863573b48c793]
- Multiple coding agents can run in parallel in one workspace, and each task gets an isolated git worktree with its own branch, terminal, conversation, and review state. [@claim:clm_9fd1c5cbdbfb144a212faa2119164de0f12ac8835137f8fb81df4bd087e07515]
- The desktop app can be pointed at a self-hosted control plane via a documented configuration procedure. [@claim:clm_fb5b041378797d93948cb5e82e19cd47ee45e5fea8e6fe1619120bd278ff7c23]
<!-- rcw:end owner=source:src_e7117f6f3c0555659f1e6c35e151a185 block=evidence -->

## Researcher notes

