---
access: public
aliases: []
claim_ids:
- clm_41d50af997e98ff064758c1d6a60c61f9e57430e1958486ce41f324ae5be1272
- clm_778f4e1750fdae2515666f7b486d1a9d220757d9381c0de5b1215371090c2d13
- clm_a91c5b121f0a26645df1e70044ab79cb3985129a5000f086305c76561723c7a3
- clm_cc194878d650776d6da60d5fce0831118544a956d2f908bb164d6f2638b840a8
- clm_da651159fec9ccd2eecf3aef0bf91424bca37ffbfa805c82bc0bc7935797b9b3
maturity: draft
page_id: pg_b40073e190fa5d8d9cf09df8ecc69f62
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7c9d9d6141c75b87bda40a5e4a3c0b46
title: 2389-research/fleet-control/docs/superpowers/plans/2026-03-23-control-plane.md
  @ efe2657f5465
updated_at: '2026-09-14T01:26:04Z'
---

# 2389-research/fleet-control/docs/superpowers/plans/2026-03-23-control-plane.md @ efe2657f5465

<!-- rcw:begin owner=source:src_7c9d9d6141c75b87bda40a5e4a3c0b46 block=evidence -->
- The architecture has three layers in one Go module: a `controld` daemon, a `control` CLI, and an MCP server, with the CLI and MCP as thin clients over the daemon's HTTP API. [@claim:clm_41d50af997e98ff064758c1d6a60c61f9e57430e1958486ce41f324ae5be1272]
- Repository development practice: the plan defines an acyclic import DAG (e.g., api must never import daemon, registry must never import tmux) and a Makefile with build, test, lint (go vet), and clean targets. [@claim:clm_778f4e1750fdae2515666f7b486d1a9d220757d9381c0de5b1215371090c2d13]
- Repository development practice: the implementation plan instructs agentic workers to use superpowers subagent-driven-development or executing-plans skills, with checkbox-tracked tasks and TDD-style test-first steps. [@claim:clm_a91c5b121f0a26645df1e70044ab79cb3985129a5000f086305c76561723c7a3]
- Repository development practice: the plan mandates commit hygiene (staging specific files, not git add -A) and test hygiene including -race for concurrent packages, 30s timeouts, and unique socket paths from t.TempDir(). [@claim:clm_cc194878d650776d6da60d5fce0831118544a956d2f908bb164d6f2638b840a8]
- The tech stack specifies Go, modernc.org/sqlite as the only acceptable SQLite driver (mattn/go-sqlite3 forbidden), bubbletea/lipgloss for the TUI, and net/http over a Unix socket. [@claim:clm_da651159fec9ccd2eecf3aef0bf91424bca37ffbfa805c82bc0bc7935797b9b3]
<!-- rcw:end owner=source:src_7c9d9d6141c75b87bda40a5e4a3c0b46 block=evidence -->

## Researcher notes

