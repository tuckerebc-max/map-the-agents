---
access: public
aliases: []
claim_ids:
- clm_2621f57e5e543ed6333145b2ac1421c16846c8bb4a02f5919691ed5acc9397b9
- clm_2e0f53730c6600e81363071e70dcfd9892eceae517417fa72b8b6f97c5ccbb39
- clm_306860977918cce409e21758b1b7a17340a36c7a785fcaf9875ad3835445592b
- clm_37b0a4f25d1aeaebaec119c597b8ef81651b754990e4e8ca0b8d516104bd262b
- clm_3f72a61abe0f3a003d982e22d44f8b8b41ad0b184cd8aabb9ac65a137376ea4f
- clm_4256c5f6432f8b6d742c10ed42857034047becc61bcd039200b6a0db939717d8
- clm_70e6634cb4583ca020b9a5ffbe32929409d6431e540997ec6a1bc8bc483d079b
- clm_7ae34aa3c592b144e7522469a29ee2ccd1ec4888ae939185cf8bff32600a937c
- clm_863568697c6018c7031fe8170fda8ad8cc16ec2284e1235912a0cd1487fce507
- clm_99ae4ebf9a0c929a178f2b2f2ec7bc5c3d90e96c7c94d0b7aedbee71df455c15
- clm_a2b75a0e028c8e9f9f14e85445c1c8bf8269f291b6c5b0bc5a9af8127dd4a72d
- clm_b016ef0a48afc385263a6b721486f701384c7e16606d662d3a5bb7e6acecc293
- clm_b6c32da7e15bddec977fc3a7741224fbfd94c968c01b9526dd2145d39c19ee2f
- clm_f224932fef0a847358ad28ff5b2ab417f26566b29c17c686ca2539a8541e2708
maturity: draft
page_id: pg_97ae7ff4c2bc54af8dccc7d38736a97a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3162a85b456b573aa7491e69cbdb0c41
title: gi-dellav/zerostack/README.md @ efd142b3ac46
updated_at: '2026-09-14T01:51:09Z'
---

# gi-dellav/zerostack/README.md @ efd142b3ac46

<!-- rcw:begin owner=source:src_3162a85b456b573aa7491e69cbdb0c41 block=evidence -->
- zerostack is a minimal coding agent written in Rust, inspired by pi and opencode. [@claim:clm_2621f57e5e543ed6333145b2ac1421c16846c8bb4a02f5919691ed5acc9397b9]
- The README states Windows support is untested, and the loop and git-worktree features are explicitly marked experimental. [@claim:clm_2e0f53730c6600e81363071e70dcfd9892eceae517417fa72b8b6f97c5ccbb39]
- The gated memory feature keeps plain-Markdown notes (global MEMORY.md plus per-project logs) injected into the system prompt each session; it is not in the default build. [@claim:clm_306860977918cce409e21758b1b7a17340a36c7a785fcaf9875ad3835445592b]
- With the acp feature, zerostack acts as an ACP (JSON-RPC) agent server over stdio or TCP so editors like Zed can connect; ACP is not in the default build. [@claim:clm_37b0a4f25d1aeaebaec119c597b8ef81651b754990e4e8ca0b8d516104bd262b]
- Optional --sandbox mode runs bash commands in bubblewrap (or zerobox on macOS), masks credential directories by default, and can require the backend via --sandbox-required; network stays on unless disabled. [@claim:clm_3f72a61abe0f3a003d982e22d44f8b8b41ad0b184cd8aabb9ac65a137376ea4f]
- The project targets users wanting a lightweight terminal coding agent, citing ~30k LoC, a 26MB binary, and roughly 16MB average RAM versus much heavier JS-based agents. [@claim:clm_4256c5f6432f8b6d742c10ed42857034047becc61bcd039200b6a0db939717d8]
- There are five permission modes (restrictive, readonly, guarded, standard, yolo) with per-tool glob patterns, session allowlists, and doom-loop detection for repeated identical tool calls. [@claim:clm_70e6634cb4583ca020b9a5ffbe32929409d6431e540997ec6a1bc8bc483d079b]
- A prompts system lets users switch built-in system prompts (code, plan, review, debug, ask, etc.) at runtime via /prompt, and custom prompts can be added as markdown files under the config prompts directory. [@claim:clm_7ae34aa3c592b144e7522469a29ee2ccd1ec4888ae939185cf8bff32600a937c]
- Git worktree integration offers /worktree, /wt-merge, and /wt-exit slash commands for a branch-per-task workflow, with optional auto-merge on exit; the feature is labeled experimental. [@claim:clm_863568697c6018c7031fe8170fda8ad8cc16ec2284e1235912a0cd1487fce507]
- Sessions are saved as JSON under $XDG_DATA_HOME/zerostack/sessions/ and can be resumed with -c, -r, or --session <id>; auto-compaction summarizes old messages near the context-window limit. [@claim:clm_99ae4ebf9a0c929a178f2b2f2ec7bc5c3d90e96c7c94d0b7aedbee71df455c15]
- An iterative loop system (experimental) repeatedly works through a LOOP_PLAN.md plan with validation commands, usable via /loop in the TUI or headless flags like --loop-prompt and --loop-max. [@claim:clm_a2b75a0e028c8e9f9f14e85445c1c8bf8269f291b6c5b0bc5a9af8127dd4a72d]
- A --dangerously-skip-permissions flag bypasses all permission checks entirely and is not a runtime-toggleable mode. [@claim:clm_b016ef0a48afc385263a6b721486f701384c7e16606d662d3a5bb7e6acecc293]
- The agent automatically loads AGENTS.md or CLAUDE.md from the project root or ancestor directories into the system prompt, and optionally ARCHITECTURE.md under the archmd feature; -n disables context-file loading. [@claim:clm_b6c32da7e15bddec977fc3a7741224fbfd94c968c01b9526dd2145d39c19ee2f]
- The agent supports multiple LLM providers: OpenRouter (default), OpenAI-compatible, Anthropic, Gemini, and Ollama, plus custom providers configured via config.yaml. [@claim:clm_f224932fef0a847358ad28ff5b2ab417f26566b29c17c686ca2539a8541e2708]
<!-- rcw:end owner=source:src_3162a85b456b573aa7491e69cbdb0c41 block=evidence -->

## Researcher notes

