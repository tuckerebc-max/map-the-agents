---
access: public
aliases: []
claim_ids:
- clm_131cd95d9d134e1b1e97d6bd9c8aeb2c830ab0e47a0cc3ccc559898bd4d7b640
- clm_248591bf787bab6dc15a69b9a85af9424882dd2be7082d8373294f63c82b64ac
- clm_2c1e08104efef08e123dc6fc8b1a5de6a51dc0b7e82378a74c2eeaf7ccdb9be7
- clm_3da0cf710bdde2e717099a99528eba652e255eacd4160b45906f28b446c9a425
- clm_491df4c10f126c1cfa3360c0be04c5abfc858402352dba55c6d063f4074662c7
- clm_5bbc5740814bf82a6a60cd5e79c898b5a8688e0d8a167d28833434d668ad2a08
- clm_628f9618cdb35d65b3cc14477071e4c6685a51e7d5698b0b1d3f4f5f9b00d1e2
- clm_6994c231848fbb2172c80b1b97675faa5b4744d94f07b9c6a18d837b373e2c4d
- clm_7a21a5b8c0ef86590ecf95b955ac66edf2bb090350e831aad85c9c7b07972d6c
- clm_8d3cd70a1aeb1242fb4a2e6c075ee6e75e2360abb434dfd3ab8290d05fdeda0b
- clm_d9c1ffe5730cfb319cc817276f49b7d99868ce5c39606346564fd9a0cebd46ff
- clm_e95694869f32c094078cc21b9091527e30a0c87e51c7772c1949a4f8ccdcffa0
- clm_f19010cac70964705307ec512e8aab62db38517b8fab2015ec4a6f3d6cd311f3
maturity: draft
page_id: pg_24368101ba435a11b450022ba3135247
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f0c135cdb4e05b528158bf607a79fe53
title: 777genius/agent-teams-ai/README.md @ 43764e1df31f
updated_at: '2026-09-14T01:28:18Z'
---

# 777genius/agent-teams-ai/README.md @ 43764e1df31f

<!-- rcw:begin owner=source:src_f0c135cdb4e05b528158bf607a79fe53 block=evidence -->
- Token analytics track input, output, cache, and reasoning usage across teams, agents, tasks, projects, models, runtimes, sessions, and runs, with monthly token or cost budgets and alerts at 80% and 100%. [@claim:clm_131cd95d9d134e1b1e97d6bd9c8aeb2c830ab0e47a0cc3ccc559898bd4d7b640]
- At team launch, each teammate can run on the main checkout or in its own git worktree to avoid conflicts when running multiple teams, with branch rules configurable via the provisioning prompt. [@claim:clm_248591bf787bab6dc15a69b9a85af9424882dd2be7082d8373294f63c82b64ac]
- The product is described as an orchestration layer for AI agent teams spanning Claude Code, Codex, OpenCode, Cursor, SuperGrok, GitHub Copilot, Z.AI, MiniMax, and Kiro. [@claim:clm_2c1e08104efef08e123dc6fc8b1a5de6a51dc0b7e82378a74c2eeaf7ccdb9be7]
- The app is an Electron desktop application distributed as macOS dmg (Apple Silicon and Intel), Windows exe, Linux AppImage and deb builds via GitHub releases. [@claim:clm_3da0cf710bdde2e717099a99528eba652e255eacd4160b45906f28b446c9a425]
- The desktop app is the main product; a web version exists but is described as still in active development. [@claim:clm_491df4c10f126c1cfa3360c0be04c5abfc858402352dba55c6d063f4074662c7]
- The README's comparison scores for live collaboration are explicitly labeled qualitative editorial assessments of documented capabilities, not benchmark results. [@claim:clm_5bbc5740814bf82a6a60cd5e79c898b5a8688e0d8a167d28833434d668ad2a08]
- Tasks with detected code changes offer a diff view where users can accept, reject, or comment on individual code hunks, similar to Cursor's review flow. [@claim:clm_628f9618cdb35d65b3cc14477071e4c6685a51e7d5698b0b1d3f4f5f9b00d1e2]
- No prerequisites are required: the app can detect installed Claude Code, Codex, and OpenCode runtimes, and other providers like Cursor, SuperGrok, GitHub Copilot, Z.AI, MiniMax, and Kiro can be connected from the UI. [@claim:clm_6994c231848fbb2172c80b1b97675faa5b4744d94f07b9c6a18d837b373e2c4d]
- The app works through locally installed Claude/Codex/OpenCode CLIs rather than app-level API keys, and the FAQ states it does not upload project code to Agent Teams servers; there is no cloud backend for code storage. [@claim:clm_7a21a5b8c0ef86590ecf95b955ac66edf2bb090350e831aad85c9c7b07972d6c]
- Agents in a team message each other, create and manage shared tasks on a kanban board, review each other's work, and can communicate across different teams; multiple teams can run simultaneously and coordinate. [@claim:clm_8d3cd70a1aeb1242fb4a2e6c075ee6e75e2360abb434dfd3ab8290d05fdeda0b]
- Onboarding starts with a free model requiring no auth (no signup, API key, or card), with paid or account providers connected later; the app is free and open source. [@claim:clm_d9c1ffe5730cfb319cc817276f49b7d99868ce5c39606346564fd9a0cebd46ff]
- A guarded, rate-limited nudge system sends short control messages to wake stalled agents, e.g. after a known rate-limit cooldown or when a teammate has not synced with its task or review. [@claim:clm_e95694869f32c094078cc21b9091527e30a0c87e51c7772c1949a4f8ccdcffa0]
- Some RDP sessions expose virtual GPU drivers that can break Electron rendering; the documented workaround is launching with AGENT_TEAMS_DISABLE_GPU=1 to disable hardware acceleration. [@claim:clm_f19010cac70964705307ec512e8aab62db38517b8fab2015ec4a6f3d6cd311f3]
<!-- rcw:end owner=source:src_f0c135cdb4e05b528158bf607a79fe53 block=evidence -->

## Researcher notes

