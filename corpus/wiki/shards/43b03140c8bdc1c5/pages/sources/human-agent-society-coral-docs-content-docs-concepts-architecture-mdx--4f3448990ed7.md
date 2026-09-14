---
access: public
aliases: []
claim_ids:
- clm_15f483d5d0c948bfe8e6127d664719d02a455c1a5824d49471240ada74787872
- clm_3421d849785be4547c29cc55186795a62204c0e2bfb1dc92090f5397ae4c761c
- clm_5afba1023faa04c595dba066a166b0d4ed44a956dd7754ce95cd299cbbb2b54d
- clm_7a0b4ef34bd86f3a0b621bb265dc5cc3d50b84a886b5bbf0c31db9e3a4255943
- clm_cf0e14600569680463a67eec552f7a81f57687185cb935f2b70f9480c3533e14
- clm_ee1fde860d23a596c41016df08bd69a10e3eb29382052903093ce6bd3c5362ba
maturity: draft
page_id: pg_04815e08ed515f1cb0b84f3448990ed7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ddefbdc8cfb15952b64d02647a7d20e0
title: Human-Agent-Society/CORAL/docs/content/docs/concepts/architecture.mdx @ 0123dfb939b3
updated_at: '2026-09-14T03:57:24Z'
---

# Human-Agent-Society/CORAL/docs/content/docs/concepts/architecture.mdx @ 0123dfb939b3

<!-- rcw:begin owner=source:src_ddefbdc8cfb15952b64d02647a7d20e0 block=evidence -->
- coral start creates shared state, per-agent git worktrees, a grader daemon, generated CORAL.md instructions, and agent subprocesses; the manager interrupts agents with heartbeat prompts like reflect, consolidate, and pivot. [@claim:clm_15f483d5d0c948bfe8e6127d664719d02a455c1a5824d49471240ada74787872]
- A grader daemon polls pending attempt JSON files in agent worktrees, runs the grader, writes scores back, and performs cleanup; agents poll the same files until results appear. [@claim:clm_3421d849785be4547c29cc55186795a62204c0e2bfb1dc92090f5397ae4c761c]
- A web dashboard exposes a POST /api/steer endpoint that validates the manager is stopped, then queues a continue_from action or marks an attempt as user-best; coral resume applies queued actions, and coral resume --from creates an in-memory steering action. [@claim:clm_5afba1023faa04c595dba066a166b0d4ed44a956dd7754ce95cd299cbbb2b54d]
- The stack is Python 3.11+ with Hatchling build, uv package manager, PyYAML, and a Starlette backend with React/Vite frontend for the dashboard. [@claim:clm_7a0b4ef34bd86f3a0b621bb265dc5cc3d50b84a886b5bbf0c31db9e3a4255943]
- Agents and the grader daemon communicate entirely through the filesystem, with no RPC, sockets, or message queue. [@claim:clm_cf0e14600569680463a67eec552f7a81f57687185cb935f2b70f9480c3533e14]
- Shared state lives in .coral/public/ (attempts, notes, skills, logs, heartbeat, steering, eval counter) and is symlinked into every agent worktree; grader venvs and answer keys stay hidden in .coral/private/. [@claim:clm_ee1fde860d23a596c41016df08bd69a10e3eb29382052903093ce6bd3c5362ba]
<!-- rcw:end owner=source:src_ddefbdc8cfb15952b64d02647a7d20e0 block=evidence -->

## Researcher notes

