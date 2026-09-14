---
access: public
aliases: []
claim_ids:
- clm_176f67fd9004173cce1bc12057277e21cb88ea57d94dae65638c3310360400e0
- clm_6a086cd409e0028981f53b19b913e05320e0c0744bad51cd51c77780f2642491
- clm_a4dab8ccca225a306afd16200f6182a7f6991eed0e647fa88149a3ad0adcc8be
maturity: draft
page_id: pg_7b1cdd7ccd68553a8494e9dec94093ee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_66dcc0040d1656edbfe02d932f4a4be9
title: plandex-ai/plandex/docs/docs/core-concepts/configuration.md @ e2d772072efa
updated_at: '2026-09-14T03:11:52Z'
---

# plandex-ai/plandex/docs/docs/core-concepts/configuration.md @ e2d772072efa

<!-- rcw:begin owner=source:src_66dcc0040d1656edbfe02d932f4a4be9 block=evidence -->
- REPL commands include \config, \set-config, and \set-auto, with `default` variants that modify configuration for new plans. [@claim:clm_176f67fd9004173cce1bc12057277e21cb88ea57d94dae65638c3310360400e0]
- A configuration system exposes settings such as auto-mode (none/basic/plus/semi/full, default semi), auto-apply (default false), auto-commit (default true), and can-exec, viewable via `plandex config` and modifiable via `plandex set-config`. [@claim:clm_6a086cd409e0028981f53b19b913e05320e0c0744bad51cd51c77780f2642491]
- Many settings can be overridden per command with CLI flags (e.g. `plandex tell "..." --apply --auto-exec --debug`); these overrides apply only to that execution and don't change saved configuration. [@claim:clm_a4dab8ccca225a306afd16200f6182a7f6991eed0e647fa88149a3ad0adcc8be]
<!-- rcw:end owner=source:src_66dcc0040d1656edbfe02d932f4a4be9 block=evidence -->

## Researcher notes

