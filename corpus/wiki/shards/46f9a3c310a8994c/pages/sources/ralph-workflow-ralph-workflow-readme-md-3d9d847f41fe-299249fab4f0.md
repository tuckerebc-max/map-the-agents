---
access: public
aliases: []
claim_ids:
- clm_0756b1face0a85e69053abd93b70edd96b56401c1869f8bd6498593eb7621231
- clm_2f4d0597996b6c14f584cf0a60a9697d135fb11371873bfa1b7208c2c6080760
- clm_57fcee6b3aa34ec3c979336ece4ab6430d7a4cadd061ff251fff4c0a303e401d
- clm_6138f051cd67c4496c9d03d8afea6610b0056e37bf62c5624c10fd038c6b5999
- clm_6f8e35ff842d220ab6115e4de8b5768bb5ccbf9218469d423d5dc458e858dc10
- clm_ae06c66c616fb45c77e30dba95a5309912b21c26f2085e4810620ff272c51711
- clm_c0f087015e0f49879d441108235060bca5a30d9a2f3abd16a09c2ddd6e7435d2
maturity: draft
page_id: pg_9c5dc64e640054e6ac9c299249fab4f0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_554234629ff25ee7ab417a0f748d4709
title: Ralph-Workflow/Ralph-Workflow/README.md @ 3d9d847f41fe
updated_at: '2026-09-14T02:35:18Z'
---

# Ralph-Workflow/Ralph-Workflow/README.md @ 3d9d847f41fe

<!-- rcw:begin owner=source:src_554234629ff25ee7ab417a0f748d4709 block=evidence -->
- Ralph Workflow is described as a free, open-source AI agent orchestrator for coding work that takes one well-specified task and runs a Ralph loop with the user's chosen coding agent. [@claim:clm_0756b1face0a85e69053abd93b70edd96b56401c1869f8bd6498593eb7621231]
- The README states the tool is not intended for vague prompts or repositories lacking tests or other guardrails, targeting work too large to babysit but too risky to trust blindly. [@claim:clm_2f4d0597996b6c14f584cf0a60a9697d135fb11371873bfa1b7208c2c6080760]
- The Ralph Loop pattern is attributed to Geoffrey Huntley (ghuntley.com/ralph), with Ralph Workflow positioned as an independent reference implementation of that pattern. [@claim:clm_57fcee6b3aa34ec3c979336ece4ab6430d7a4cadd061ff251fff4c0a303e401d]
- The product ships nine built-in agent backends: Claude Code, Claude Code headless, Codex, OpenCode, Nanocoder, AGY, Pi, Cursor, and Kimi; the user authenticates one locally and the tool uses it. [@claim:clm_6138f051cd67c4496c9d03d8afea6610b0056e37bf62c5624c10fd038c6b5999]
- A checkout install provides an `rdev` launcher whose `--version` ends in -build, deliberately leaving any globally installed `ralph` command in place; native Windows users are directed to install the published package via pipx or pip. [@claim:clm_6f8e35ff842d220ab6115e4de8b5768bb5ccbf9218469d423d5dc458e858dc10]
- The runtime requires Python 3.12 or newer and is described as local-first; the project is licensed AGPL-3.0-or-later and published on PyPI. [@claim:clm_ae06c66c616fb45c77e30dba95a5309912b21c26f2085e4810620ff272c51711]
- The core orchestration is a Ralph loop of plan, build, verify, and fix stages run with the selected coding agent, after which the user returns to inspect the result. [@claim:clm_c0f087015e0f49879d441108235060bca5a30d9a2f3abd16a09c2ddd6e7435d2]
<!-- rcw:end owner=source:src_554234629ff25ee7ab417a0f748d4709 block=evidence -->

## Researcher notes

