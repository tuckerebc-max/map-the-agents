---
access: public
aliases: []
claim_ids:
- clm_13be2bd5dca4ca4b2a53cc04f88b8a5bb2f50c629f9f146f750d1b03d359389c
- clm_3c125130d14929067f1b29e0a3a8139b8ae2cc7a95f969b3db26c7bde99c7955
- clm_445b71d725136ff071170149f409608a1e9a8249d2949602824188875d27eea9
- clm_5e6f5b67bc5ad37ea6c55e0261fba661529fcabeae8c2039d558481c1ea6b606
- clm_676de505113dc5cf97e52690cb4429cf449013796825a64325754d909d618429
- clm_97e3728d64d8e71b86e80ee6f665c875bb3f1e469962092042b26f1bef08bdb4
maturity: draft
page_id: pg_942ac4a9097b5bed8060d53adfa811b4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_472b7f295443531c80d668db702ff376
title: SWE-agent/SWE-ReX/README.md @ 5c995c365dfb
updated_at: '2026-09-14T04:24:36Z'
---

# SWE-agent/SWE-ReX/README.md @ 5c995c365dfb

<!-- rcw:begin owner=source:src_472b7f295443531c80d668db702ff376 block=evidence -->
- SWE-ReX exposes a runtime interface for interacting with sandboxed shell environments, letting an AI agent run arbitrary commands on arbitrary environments. [@claim:clm_13be2bd5dca4ca4b2a53cc04f88b8a5bb2f50c629f9f146f750d1b03d359389c]
- SWE-ReX detects when shell commands finish, extracts output and exit code for the agent, supports interactive tools like ipython and gdb, and allows multiple parallel shell sessions. [@claim:clm_3c125130d14929067f1b29e0a3a8139b8ae2cc7a95f969b3db26c7bde99c7955]
- The project advertises fast, massively parallel agent runs, citing large-benchmark evaluation and a demo of SWE-agent running on 30 SWE-bench instances in parallel. [@claim:clm_445b71d725136ff071170149f409608a1e9a8249d2949602824188875d27eea9]
- The package installs via pip as swe-rex, with optional extras for modal, fargate, and daytona, plus a dev extra for development setup. [@claim:clm_5e6f5b67bc5ad37ea6c55e0261fba661529fcabeae8c2039d558481c1ea6b606]
- SWE-ReX originated from the SWE-agent and SWE-agent enigma projects and aims to disentangle agent logic from infrastructure concerns. [@claim:clm_676de505113dc5cf97e52690cb4429cf449013796825a64325754d909d618429]
- Agent code stays the same regardless of whether commands run locally, in Docker containers, on AWS remote machines, Modal, or other backends. [@claim:clm_97e3728d64d8e71b86e80ee6f665c875bb3f1e469962092042b26f1bef08bdb4]
<!-- rcw:end owner=source:src_472b7f295443531c80d668db702ff376 block=evidence -->

## Researcher notes

