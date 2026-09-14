---
access: public
aliases: []
claim_ids:
- clm_53473b5b32ecde3693f71fc4f99e30615539c8a09a07293262019812d3388cf3
- clm_53ee003035769becae444bfa5519e811aba7b091d1cb010c9cb260b07ad4c143
- clm_9e3182c806a2916c50ad987eb55d1f67bd414369b86b4c9f8996a27b56319119
- clm_b4824d3371b0a5a9f8119543917b38277dde04a38a24275cf5a80c2f7cfbec0d
- clm_df259c60ecd967f0eea829a1dba3dbbfb93f4efea3f6b63673891ea4cec168a7
maturity: draft
page_id: pg_61a1c98e47e051078b46369240e3c9ea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ba6993633dfc5ff99365a813b2e568fa
title: danshapiro/freshell/AGENTS.md @ e68ae40a2b3e
updated_at: '2026-09-14T03:06:36Z'
---

# danshapiro/freshell/AGENTS.md @ e68ae40a2b3e

<!-- rcw:begin owner=source:src_ba6993633dfc5ff99365a813b2e568fa block=evidence -->
- Repository development practice: contributors must work in .worktrees worktrees, branch from origin/main, and land all behavior changes via PRs to main; direct pushes to main are forbidden. [@claim:clm_53473b5b32ecde3693f71fc4f99e30615539c8a09a07293262019812d3388cf3]
- The stack includes React 18, Redux Toolkit, xterm.js, Monaco, Express, node-pty, WebSocket, Vite, TypeScript, and Vitest-based testing tools. [@claim:clm_53ee003035769becae444bfa5519e811aba7b091d1cb010c9cb260b07ad4c143]
- Repository development practice: destructive process-kill, config-corruption, and restart-storm test suites must run inside a disposable Docker sandbox via scripts/sandbox-test.sh, never on the host. [@claim:clm_9e3182c806a2916c50ad987eb55d1f67bd414369b86b4c9f8996a27b56319119]
- Repository development practice: the project mandates Red-Green-Refactor TDD for all but trivial changes, with both unit and e2e coverage required. [@claim:clm_b4824d3371b0a5a9f8119543917b38277dde04a38a24275cf5a80c2f7cfbec0d]
- Repository development practice: broad test runs go through a shared coordinator gate, with scripts/base-gate.sh validating origin/main from a clean scratch worktree and npm run test:status showing holder info. [@claim:clm_df259c60ecd967f0eea829a1dba3dbbfb93f4efea3f6b63673891ea4cec168a7]
<!-- rcw:end owner=source:src_ba6993633dfc5ff99365a813b2e568fa block=evidence -->

## Researcher notes

