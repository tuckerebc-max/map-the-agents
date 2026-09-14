---
access: public
aliases: []
claim_ids:
- clm_15240c53919e0e0e430d8728137c74f3bb4b04d4d00c7b9e6367afeb3b26045a
- clm_2045fffbe584c14a0c4ac8123f674e87a3459fafa70a169f661d9c3dd9d6b935
- clm_34fa756b8b6e3b0863234103e432abd8f028ea360aea448417665ba6410f991a
- clm_50be779ee40350ac4133631be84aa6ba913f0ae16ea3b1330e2c856e01a743e2
- clm_5bb0176e60f170b8b00bd0321b586e5178b37b447c1a16a0a04da0642accec96
- clm_5c2f70f436c9fa63d9e3ae3b9cffd3f99adca62b60755283838e435c8eaa79b1
- clm_6d2f9dc8fdb177e096afa178b202d7954a4ec4e5e3d59326b53dd323c927ec90
- clm_7f428ee8bfe61832784054a38a4c543e48f72ac63446599ec62c647e154d5a4d
- clm_82691afaae0191369c8dd1789400850834a02aa9753aa0437663f423b5adc04e
- clm_9ec3c9d8c154fe705756b3126d4cc1c602d52c637b48deb43ba3b143e9817255
- clm_a6020a5783bf3448215b073d5bff068ebc49ad23fd49d7a4445298d153c5b87b
- clm_ad593f13fd32fd787e180bf3843be20f9fee51c21cd55ba0eda850dadaafbc0a
- clm_aed6f2a21a33d1228adcbb99fc28a99428e395453071a4559c24e6db87d443a4
- clm_b66d64704c64f6d5d8e8a603d2ce2e7ab446afa6ab568bc1001b6e1cd74888d6
- clm_c6e1a3789e00d96753593140255b3969b9fe57f76e0218dc715db158caf2590c
- clm_d75a00647fb28292f69dfaa5a7934867c3dbd213e4b315e192ea0a2a7a8490a1
maturity: draft
page_id: pg_8c942ba77f945125bf63a4d3cf997137
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_90482fc645e750f795208ff2bb5d75a2
title: XiaomiMiMo/MiMo-Code/README.md @ 6fbb1732232c
updated_at: '2026-09-14T03:25:17Z'
---

# XiaomiMiMo/MiMo-Code/README.md @ 6fbb1732232c

<!-- rcw:begin owner=source:src_90482fc645e750f795208ff2bb5d75a2 block=evidence -->
- The README states MiMoCode does not support the built-in macOS Terminal.app, recommending iTerm2 or the VS Code integrated terminal for rendering issues. [@claim:clm_15240c53919e0e0e430d8728137c74f3bb4b04d4d00c7b9e6367afeb3b26045a]
- Workflows are deterministic JavaScript scripts orchestrating multiple agents with fixed phases, bounded retries, and automatic parallelization; four built-ins ship (compose, deep-research, fact-check, research-experiment), and custom ones go in .mimocode/workflows/. [@claim:clm_2045fffbe584c14a0c4ac8123f674e87a3459fafa70a169f661d9c3dd9d6b935]
- Cross-session memory uses SQLite FTS5 with files for project memory (MEMORY.md), session checkpoints, scratch notes, and per-task progress; memory is injected automatically on session resume. [@claim:clm_34fa756b8b6e3b0863234103e432abd8f028ea360aea448417665ba6410f991a]
- Context management includes automatic checkpoints, context reconstruction near the window limit, budgeted injection with importance ranking, and a per-model adjustable compaction point via /context-limit or compaction.max_context. [@claim:clm_50be779ee40350ac4133631be84aa6ba913f0ae16ea3b1330e2c856e01a743e2]
- File access outside the project directory triggers an external_directory permission prompt by default; /tmp can be allowlisted in config, and --dangerously-skip-permissions injects an allow-all base while explicit deny rules still block. [@claim:clm_5bb0176e60f170b8b00bd0321b586e5178b37b447c1a16a0a04da0642accec96]
- Repository development practice: development uses bun (bun ci for frozen-lockfile install, bun run dev, bun turbo typecheck). [@claim:clm_5c2f70f436c9fa63d9e3ae3b9cffd3f99adca62b60755283838e435c8eaa79b1]
- The research-experiment workflow appears to provide an evaluation-style loop (baseline, iterate, audit against metric gaming) for mechanically verifiable metrics, though no benchmark results for the agent itself appear in the evidence. [@claim:clm_6d2f9dc8fdb177e096afa178b202d7954a4ec4e5e3d59326b53dd323c927ec90]
- Environment variables can disable builtin skills entirely, disable only office/media skills, or hide skills from TUI autocomplete while keeping them available to agents. [@claim:clm_7f428ee8bfe61832784054a38a4c543e48f72ac63446599ec62c647e154d5a4d]
- Three primary agents exist: build (full permissions), plan (read-only analysis), and compose (specs-driven orchestration); Tab switches agents, and Compose is isolated once entered. [@claim:clm_82691afaae0191369c8dd1789400850834a02aa9753aa0437663f423b5adc04e]
- MiMoCode is built as a fork of OpenCode, retaining core capabilities (multiple providers, TUI, LSP, MCP, plugins) and adding memory, context management, subagents, goal loops, and dream/distill self-improvement. [@claim:clm_9ec3c9d8c154fe705756b3126d4cc1c602d52c637b48deb43ba3b143e9817255]
- MiMoCode is a terminal-native AI coding assistant that reads/writes code, runs commands, manages Git, and maintains persistent project memory across sessions. [@claim:clm_a6020a5783bf3448215b073d5bff068ebc49ad23fd49d7a4445298d153c5b87b]
- The primary agent can spawn subagents that share session context, run in parallel, and support lifecycle tracking, cancellation, and background execution. [@claim:clm_ad593f13fd32fd787e180bf3843be20f9fee51c21cd55ba0eda850dadaafbc0a]
- Voice input requires the sox dependency and is available to MiMo logged-in users; the ASR model mimo-v2.5-asr is only on MiMo's platform while voice control works via OpenRouter-compatible providers. [@claim:clm_aed6f2a21a33d1228adcbb99fc28a99428e395453071a4559c24e6db87d443a4]
- Install options include a curl one-liner for macOS/Linux, a PowerShell script for Windows, and npm install -g @mimo-ai/cli; the CLI is launched with the `mimo` command. [@claim:clm_b66d64704c64f6d5d8e8a603d2ce2e7ab446afa6ab568bc1001b6e1cd74888d6]
- Builtin skills are matched by exact name, localized alias, or BM25 relevance; high-confidence matches auto-load, and users can override builtins with same-name skills in project or personal skill directories. [@claim:clm_c6e1a3789e00d96753593140255b3969b9fe57f76e0218dc715db158caf2590c]
- First launch offers configuration via Xiaomi MiMo OAuth, Codex/ChatGPT OAuth, one-step import from Claude Code, catalog providers, or any custom OpenAI-compatible API. [@claim:clm_d75a00647fb28292f69dfaa5a7934867c3dbd213e4b315e192ea0a2a7a8490a1]
<!-- rcw:end owner=source:src_90482fc645e750f795208ff2bb5d75a2 block=evidence -->

## Researcher notes

