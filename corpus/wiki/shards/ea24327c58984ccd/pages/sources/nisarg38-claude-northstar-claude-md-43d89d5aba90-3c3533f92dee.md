---
access: public
aliases: []
claim_ids:
- clm_28b59b57b6991d23b35e89f2e1ac89a29d6282ada921bfa5c2ebccf5281c64e5
- clm_8319bbe8444eed661041f438f4289e3f9c99dca86db0366f4c13462cffe8b824
- clm_94dd46b257a455c049d503af548b56873f660ab78fa5059919e2b0784a4d302d
- clm_d3830b80a00ff9cc1f3082bf3417517cfed6082a6a80ecc059e759c0e9355253
maturity: draft
page_id: pg_cc2bd0027c465d3a9af23c3533f92dee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d0f29a747aca5214ab16d96d7302d625
title: Nisarg38/claude-northstar/CLAUDE.md @ 43d89d5aba90
updated_at: '2026-09-14T04:13:10Z'
---

# Nisarg38/claude-northstar/CLAUDE.md @ 43d89d5aba90

<!-- rcw:begin owner=source:src_d0f29a747aca5214ab16d96d7302d625 block=evidence -->
- Repository development practice: state files have defined update triggers — project-state.json after each session, decisions.md on technical choices, progress-log.md at session end, and north-star.md when the vision changes. [@claim:clm_28b59b57b6991d23b35e89f2e1ac89a29d6282ada921bfa5c2ebccf5281c64e5]
- The framework follows a quality pipeline before merging significant work: developer completes, QA verifies, reviewer approves, then merge. [@claim:clm_8319bbe8444eed661041f438f4289e3f9c99dca86db0366f4c13462cffe8b824]
- Repository development practice: the installed CLAUDE.md instructs the agent to always read north-star.md, project-state.json, and decisions.md at session start, then either capture a new vision or report state and work autonomously. [@claim:clm_94dd46b257a455c049d503af548b56873f660ab78fa5059919e2b0784a4d302d]
- Repository development practice: sub-agents are spawned via the Task tool with subagent_type 'general-purpose', using prompt files from .claude/harness/prompts/ with injected context. [@claim:clm_d3830b80a00ff9cc1f3082bf3417517cfed6082a6a80ecc059e759c0e9355253]
<!-- rcw:end owner=source:src_d0f29a747aca5214ab16d96d7302d625 block=evidence -->

## Researcher notes

