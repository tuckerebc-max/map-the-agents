---
access: public
aliases: []
claim_ids:
- clm_010850df770996483730a7a309904276ebe4ec30a63cf802defa27809149e677
- clm_05d8b3693196e5dbdaf446f6b3c2e5d82116af3dc955d3dce027b23578d3dea9
- clm_36192bb87d43b2124d368c59e36f7fa670d07127cbd0588414ccb0150488786b
- clm_83ef7e99d45bee501f3512b5baaf6fbaa5dd7152c2e0d5c65acbc1eed0f9c84c
- clm_917cb9115361931b246d2da67b667ce4fc4d4d2295e85a44920a0ce2a7664b3b
maturity: draft
page_id: pg_d1f50e40675a56f58ff91dd70231f232
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6b028023847e540a8896aa333212b8e4
title: SWE-agent/SWE-agent/README.md @ 3ea751c087f3
updated_at: '2026-09-14T03:16:49Z'
---

# SWE-agent/SWE-agent/README.md @ 3ea751c087f3

<!-- rcw:begin owner=source:src_6b028023847e540a8896aa333212b8e4 block=evidence -->
- Development effort has largely moved to mini-SWE-agent, which the maintainers say matches SWE-agent's performance while being much simpler, and they recommend it going forward. [@claim:clm_010850df770996483730a7a309904276ebe4ec30a63cf802defa27809149e677]
- Repository development practice: contributors are welcomed via GitHub issues and pull requests, with discussion in issues encouraged before larger code changes; CI badges show pytest, docs builds, codecov, pre-commit, and link checking. [@claim:clm_05d8b3693196e5dbdaf446f6b3c2e5d82116af3dc955d3dce027b23578d3dea9]
- The EnIGMA offensive-security (CTF) mode currently recommends using SWE-agent 0.7 while EnIGMA is being updated for 1.0. [@claim:clm_36192bb87d43b2124d368c59e36f7fa670d07127cbd0588414ccb0150488786b]
- A single YAML configuration governs the agent: it defines tools, prompts shown deterministically or conditionally during a trajectory, demonstrations, model behavior, and the agent-environment input/output interface. [@claim:clm_83ef7e99d45bee501f3512b5baaf6fbaa5dd7152c2e0d5c65acbc1eed0f9c84c]
- SWE-agent enables a user-chosen language model (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to fix issues in real GitHub repositories, find cybersecurity vulnerabilities, or perform custom tasks. [@claim:clm_917cb9115361931b246d2da67b667ce4fc4d4d2295e85a44920a0ce2a7664b3b]
<!-- rcw:end owner=source:src_6b028023847e540a8896aa333212b8e4 block=evidence -->

## Researcher notes

