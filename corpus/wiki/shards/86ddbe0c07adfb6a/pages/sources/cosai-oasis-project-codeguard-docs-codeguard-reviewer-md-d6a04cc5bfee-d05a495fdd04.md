---
access: public
aliases: []
claim_ids:
- clm_36553331b809a8cfe81c88d6ab9a19f9074d60272b6b1c75c48498fb368e43ba
- clm_8a55c901cda20b01b387509e0a7e1c2597ebadfa19ff5dd2391105469ed9967d
- clm_901b85e56a13136c81532b0aaaf29a859c412a6c3ec3ad3809dd58891965f497
- clm_bdfa070413e1c4c0946c7b098f942851d8983384d5360707d9c764b0c0bf1a81
- clm_d4367bed3d54835f86da39fe312e5d9f78c93bd3e12d3fbd3a17241e88a952ec
- clm_e06599c6414020a13ab2ec67eda6ebc502b08b9f99a0c51ec8637e367dc05765
maturity: draft
page_id: pg_6ed35f21598753f4823dd05a495fdd04
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a4c33231c3aa556c87fced2ff025be46
title: cosai-oasis/project-codeguard/docs/codeguard-reviewer.md @ d6a04cc5bfee
updated_at: '2026-09-14T03:43:13Z'
---

# cosai-oasis/project-codeguard/docs/codeguard-reviewer.md @ d6a04cc5bfee

<!-- rcw:begin owner=source:src_a4c33231c3aa556c87fced2ff025be46 block=evidence -->
- The reviewer emits SARIF 2.1.0 with tool.driver.name 'CodeGuard Security Reviewer', results only for confirmed or needs-human findings, and levels error/warning/note by rule class. [@claim:clm_36553331b809a8cfe81c88d6ab9a19f9074d60272b6b1c75c48498fb368e43ba]
- The reviewer subagent is emitted for Claude Code, Cursor, OpenCode, GitHub Copilot/VS Code, and OpenAI Codex, each with a host-specific agent file location. [@claim:clm_8a55c901cda20b01b387509e0a7e1c2597ebadfa19ff5dd2391105469ed9967d]
- The reviewer classifies candidates as confirmed, needs-human, or false-positive; false positives are excluded from SARIF with a one-line justification in the summary. [@claim:clm_901b85e56a13136c81532b0aaaf29a859c412a6c3ec3ad3809dd58891965f497]
- The reviewer treats repository content as untrusted data, ignores embedded instructions, never executes discovered code, and redacts suspected credential values from SARIF and summary output. [@claim:clm_bdfa070413e1c4c0946c7b098f942851d8983384d5360707d9c764b0c0bf1a81]
- The CodeGuard Reviewer is designed for on-demand security scans only and does not activate for general code writing or editing. [@claim:clm_d4367bed3d54835f86da39fe312e5d9f78c93bd3e12d3fbd3a17241e88a952ec]
- A CodeGuard Reviewer subagent performs full-repository security scans against all CodeGuard rules and emits findings as a SARIF 2.1.0 file, writing only that output file. [@claim:clm_e06599c6414020a13ab2ec67eda6ebc502b08b9f99a0c51ec8637e367dc05765]
<!-- rcw:end owner=source:src_a4c33231c3aa556c87fced2ff025be46 block=evidence -->

## Researcher notes

