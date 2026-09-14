---
access: public
aliases: []
claim_ids:
- clm_145461293a8a0682dec49ed8a946adac7d19ecaabfeb91af0fd16655d0606c74
- clm_6b2dffd77e83f35f1f06e82c7c3e9cf6ec4c497e09df783c61837689e3158dfe
- clm_9a3dfbcf553a54b832003c640e8a5e9914082da3237982eca3eef7b353bd6d18
- clm_cd567eb22cf8c9a0be118b5cb106817e61fdd1b7759f5f41f428a2e638c7284f
- clm_d5533bd1e3377a071c2ae63ce897ff4fda76d5e6e90aefceb0792a09329194a0
- clm_ff6246f60ec9d3c5b96b948f850e90db0b3088a7259e276144ca8dd64b180793
maturity: draft
page_id: pg_d40f662fa47f5fae9a8b3c42c3904cff
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c78c91182b1e55e7913f161a97d3623e
title: Human-Agent-Society/CORAL/docs/content/docs/getting-started/configuration.mdx
  @ 0123dfb939b3
updated_at: '2026-09-14T03:57:24Z'
---

# Human-Agent-Society/CORAL/docs/content/docs/getting-started/configuration.mdx @ 0123dfb939b3

<!-- rcw:begin owner=source:src_c78c91182b1e55e7913f161a97d3623e block=evidence -->
- GraderConfig requires a setuptools-style entrypoint (module.path:ClassName) resolved in a grader venv, with setup commands, timeout (default 300s), direction, private files, and args; an empty entrypoint is a load-time error. [@claim:clm_145461293a8a0682dec49ed8a946adac7d19ecaabfeb91af0fd16655d0606c74]
- Legacy grader.type and grader.module fields were removed; tasks still setting them fail to load with a migration error pointing at grader.entrypoint. [@claim:clm_6b2dffd77e83f35f1f06e82c7c3e9cf6ec4c497e09df783c61837689e3158dfe]
- Tasks are defined by a task.yaml file with sections for task, grader, agents, islands, sharing, workspace, and run configuration. [@claim:clm_9a3dfbcf553a54b832003c640e8a5e9914082da3237982eca3eef7b353bd6d18]
- A top-level preset field layers reusable defaults between schema defaults and task.yaml, with CLI overrides winning over everything; presets cannot stack, and the resolved config is fully expanded so resume and the grader daemon never need the preset file. [@claim:clm_cd567eb22cf8c9a0be118b5cb106817e61fdd1b7759f5f41f428a2e638c7284f]
- The coral CLI includes commands such as init, start, validate, status, log, notes, skills, wait, checkout, and heartbeat set, with dotlist key=value config overrides supported on start. [@claim:clm_d5533bd1e3377a071c2ae63ce897ff4fda76d5e6e90aefceb0792a09329194a0]
- Multi-island mode partitions agents into isolated groups with scoped state; migration moves selected agents between islands on a score-ranked schedule, carrying role, heartbeat config, attempts, and logs while notes and skills stay on the source island. [@claim:clm_ff6246f60ec9d3c5b96b948f850e90db0b3088a7259e276144ca8dd64b180793]
<!-- rcw:end owner=source:src_c78c91182b1e55e7913f161a97d3623e block=evidence -->

## Researcher notes

