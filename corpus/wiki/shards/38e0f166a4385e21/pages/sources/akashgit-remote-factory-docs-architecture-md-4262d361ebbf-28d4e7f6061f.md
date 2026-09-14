---
access: public
aliases: []
claim_ids:
- clm_564419e94a8ee8d48902fe6a4f50b05b0c12f52b2c4116c10130e8e60cad44a8
- clm_962c453b48dd39bec12c357cb717f7fc64d1457675cb62a7fd44ea1f520f002d
- clm_ae0d9a1d3064d01b27b07a13172c1d11ebc92edf5705486ef7c0032f64f43a8d
maturity: draft
page_id: pg_2e37bcfd9727591b9ec428d4e7f6061f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d5fbd197ca925c9898f5edc039e499bb
title: akashgit/remote-factory/docs/architecture.md @ 4262d361ebbf
updated_at: '2026-09-14T01:32:34Z'
---

# akashgit/remote-factory/docs/architecture.md @ 4262d361ebbf

<!-- rcw:begin owner=source:src_d5fbd197ca925c9898f5edc039e499bb block=evidence -->
- The CEO agent detects project state, reads SKILL.md playbooks, spawns specialist agents via `factory agent <role>`, and makes keep/revert decisions based on eval scores. [@claim:clm_564419e94a8ee8d48902fe6a4f50b05b0c12f52b2c4116c10130e8e60cad44a8]
- Agent prompts resolve through a three-tier lookup — project-specific override, user-global override, then the factory default — and a plugin system via the `factory.plugins` entry-point group can extend modes, commands, and agent roles with builtins winning collisions. [@claim:clm_962c453b48dd39bec12c357cb717f7fc64d1457675cb62a7fd44ea1f520f002d]
- Specialist agents include Researcher, Strategist, Builder, Reviewer, Evaluator, Archivist, Refiner, and Failure Analyst, each invoked as `factory agent <role> --task "..."` with a narrow responsibility. [@claim:clm_ae0d9a1d3064d01b27b07a13172c1d11ebc92edf5705486ef7c0032f64f43a8d]
<!-- rcw:end owner=source:src_d5fbd197ca925c9898f5edc039e499bb block=evidence -->

## Researcher notes

