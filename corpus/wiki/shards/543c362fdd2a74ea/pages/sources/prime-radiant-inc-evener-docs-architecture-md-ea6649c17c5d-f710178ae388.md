---
access: public
aliases: []
claim_ids:
- clm_05d6bdc3e5773285652d03c4ba217cb812ec8c5aba095d360f82cbead36ea600
- clm_654a61ee0e3f88d56d50d7683e80dfb08c545707cc4f5461c1f617566d80b523
- clm_d45761b153f2cb18e5ce95b0921689ea546962d172285ce75e3bf1e4b11ece37
- clm_e39ec22e5226f349325ada2f2245bd79363453b103fb8cfbca64dc15b890d8ad
- clm_eab9a401a6711dd8f35704d5ba0b01c788c8aec110fa38cab10f7127fa452d14
- clm_fd113fa0049fb22d4d7566d7b5ddd91056bc950ef0eb8e3c0dd08c6b0731c9cc
maturity: draft
page_id: pg_bd6505c44b7859b8bb18f710178ae388
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_34c1c53002675694bec3f841a8e20ef7
title: prime-radiant-inc/evener/docs/architecture.md @ ea6649c17c5d
updated_at: '2026-09-14T02:32:56Z'
---

# prime-radiant-inc/evener/docs/architecture.md @ ea6649c17c5d

<!-- rcw:begin owner=source:src_34c1c53002675694bec3f841a8e20ef7 block=evidence -->
- A session's file, process, and network access can be confined with the `--sandbox` flag; sandbox denials can escalate to a human approval card, though breaker-parked calls carry no typed error and do not trigger that escalation. [@claim:clm_05d6bdc3e5773285652d03c4ba217cb812ec8c5aba095d360f82cbead36ea600]
- The repo is a multi-module Go monorepo (llm, agent, auth libraries plus the app) where binaries couple only via the appwire and hubapi wire contracts, never by importing each other's code; libraries may never import app code. [@claim:clm_654a61ee0e3f88d56d50d7683e80dfb08c545707cc4f5461c1f617566d80b523]
- A repeated-call breaker keys a per-session ledger on tool name plus a hash of raw argument bytes: the third consecutive same-class failure is refused before dispatch, and a repetition trigger nudges on byte-identical result bodies without refusing, so communicate is never blocked. [@claim:clm_d45761b153f2cb18e5ce95b0921689ea546962d172285ce75e3bf1e4b11ece37]
- The product ships three binaries: `evener` (non-interactive CLI engine), `evener hub` (browser-based orchestrator for many concurrent sessions), and `evener tui` (terminal dashboard), plus a one-shot `llmcall` client. [@claim:clm_e39ec22e5226f349325ada2f2245bd79363453b103fb8cfbca64dc15b890d8ad]
- The hub spawns `evener` serve daemons as subprocesses and serves clients over AppWire; sessions can be forked at any user message or to a side thread via /aside, and subagents appear indented under their spawning session in the sidebar. [@claim:clm_eab9a401a6711dd8f35704d5ba0b01c788c8aec110fa38cab10f7127fa452d14]
- Repository development practice: build and install from source with make build / build-hub / build-llmcall / make install, run `make help` for targets, and note that vet/test-race/lint gates iterate over every module since a root-only `go test ./...` skips the library suites in a workspace. [@claim:clm_fd113fa0049fb22d4d7566d7b5ddd91056bc950ef0eb8e3c0dd08c6b0731c9cc]
<!-- rcw:end owner=source:src_34c1c53002675694bec3f841a8e20ef7 block=evidence -->

## Researcher notes

