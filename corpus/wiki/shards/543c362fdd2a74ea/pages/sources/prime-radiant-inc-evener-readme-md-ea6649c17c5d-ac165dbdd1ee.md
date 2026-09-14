---
access: public
aliases: []
claim_ids:
- clm_05d6bdc3e5773285652d03c4ba217cb812ec8c5aba095d360f82cbead36ea600
- clm_3d355114fdce40a8f21bda6bcdc69d4727db0ad03fedca4475e55a14a576a809
- clm_754b04d96a8d39a7ee420c1d88bdff1477f7f20ff5887e454e41608f0171b21b
- clm_c51b98fc026589a199eae4382c2a44cb6fc82d1211e4a120f52915722e8fffca
- clm_e1c8cec03779524b7f3a45eeca9ec9d5e0cb7c932671b71e5f04114074e3e9ef
- clm_e39ec22e5226f349325ada2f2245bd79363453b103fb8cfbca64dc15b890d8ad
- clm_eab9a401a6711dd8f35704d5ba0b01c788c8aec110fa38cab10f7127fa452d14
- clm_ed65f4826fbd15098381a2412f26f5aa61cef47dbefcd72465100213b9177e7c
- clm_fd113fa0049fb22d4d7566d7b5ddd91056bc950ef0eb8e3c0dd08c6b0731c9cc
maturity: draft
page_id: pg_e14ab2bc30595aa68035ac165dbdd1ee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fc78730611355cb395e737454298674c
title: prime-radiant-inc/evener/README.md @ ea6649c17c5d
updated_at: '2026-09-14T02:32:56Z'
---

# prime-radiant-inc/evener/README.md @ ea6649c17c5d

<!-- rcw:begin owner=source:src_fc78730611355cb395e737454298674c block=evidence -->
- A session's file, process, and network access can be confined with the `--sandbox` flag; sandbox denials can escalate to a human approval card, though breaker-parked calls carry no typed error and do not trigger that escalation. [@claim:clm_05d6bdc3e5773285652d03c4ba217cb812ec8c5aba095d360f82cbead36ea600]
- The TUI connects to the hub at 127.0.0.1:9180 by default, auto-starts a missing local hub (unless --no-auto-start-hub), and supports flags like --hub-addr, --hub-bin, --auth-token, --state-dir, and --debug. [@claim:clm_3d355114fdce40a8f21bda6bcdc69d4727db0ad03fedca4475e55a14a576a809]
- The hub listens on 127.0.0.1:9180, prints a one-time auth URL that sets an authorizing browser cookie, and offers a /new session page, /credentials page, fork-from-message, /aside side threads, transparent resume, and Ctrl/⌘K search. [@claim:clm_754b04d96a8d39a7ee420c1d88bdff1477f7f20ff5887e454e41608f0171b21b]
- Evener uses the LLM's native tool-calling and supports many providers out of the box (OpenAI, Anthropic, Google, Ollama, Bedrock, Azure, and others), with additional providers addable via a providers.toml entry. [@claim:clm_c51b98fc026589a199eae4382c2a44cb6fc82d1211e4a120f52915722e8fffca]
- Session state auto-saves under the XDG state directory per project after each assistant turn; project IDs derive from the canonical path so linked worktrees share a bucket while separate clones get distinct ones; sessions resume via --resume, --resume-last, or --resume-with. [@claim:clm_e1c8cec03779524b7f3a45eeca9ec9d5e0cb7c932671b71e5f04114074e3e9ef]
- The product ships three binaries: `evener` (non-interactive CLI engine), `evener hub` (browser-based orchestrator for many concurrent sessions), and `evener tui` (terminal dashboard), plus a one-shot `llmcall` client. [@claim:clm_e39ec22e5226f349325ada2f2245bd79363453b103fb8cfbca64dc15b890d8ad]
- The hub spawns `evener` serve daemons as subprocesses and serves clients over AppWire; sessions can be forked at any user message or to a side thread via /aside, and subagents appear indented under their spawning session in the sidebar. [@claim:clm_eab9a401a6711dd8f35704d5ba0b01c788c8aec110fa38cab10f7127fa452d14]
- Standalone user skills in the config skills directory are discovered automatically, extra skill paths can be added via skills_dirs in launch.toml or CLI flags, and user-global slash commands are read from a commands directory when present. [@claim:clm_ed65f4826fbd15098381a2412f26f5aa61cef47dbefcd72465100213b9177e7c]
- Repository development practice: build and install from source with make build / build-hub / build-llmcall / make install, run `make help` for targets, and note that vet/test-race/lint gates iterate over every module since a root-only `go test ./...` skips the library suites in a workspace. [@claim:clm_fd113fa0049fb22d4d7566d7b5ddd91056bc950ef0eb8e3c0dd08c6b0731c9cc]
<!-- rcw:end owner=source:src_fc78730611355cb395e737454298674c block=evidence -->

## Researcher notes

