---
access: public
aliases: []
claim_ids:
- clm_6b6b55b40f44e087986346716c32c2db3f0c18177671fcd7b6a4d0604de240fe
- clm_912731bd43ea3a6cbb594ccb11937737658aec58ff09f63bfe6e80d2d6bd00ca
- clm_a5c21d1cc098e49905a060f22999d02e6e849325791befe32f71497e8e287b44
maturity: draft
page_id: pg_c0ec13bafba45270a4819dc9ff201f75
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fdb9354a2bce53e4af16325026808e10
title: Arch1eSUN/Arcgentic/CLAUDE-v0.1.0-handoff.md @ 645c345077d7
updated_at: '2026-09-14T03:34:59Z'
---

# Arch1eSUN/Arcgentic/CLAUDE-v0.1.0-handoff.md @ 645c345077d7

<!-- rcw:begin owner=source:src_fdb9354a2bce53e4af16325026808e10 block=evidence -->
- Repository development practice: the CLAUDE handoff file instructs the contributing dev session to follow a 30-task build contract in order, use TDD for Bash scripts, commit once per task with conventional-commit prefixes directly on main, and never add paid-API integrations or force-push. [@claim:clm_6b6b55b40f44e087986346716c32c2db3f0c18177671fcd7b6a4d0604de240fe]
- Repository development practice: the contributing environment requires Bash >= 4, Python 3 >= 3.8 with PyYAML and jsonschema, Claude Code >= 1.0, and the superpowers plugin, with plugin-dev recommended for skill review. [@claim:clm_912731bd43ea3a6cbb594ccb11937737658aec58ff09f63bfe6e80d2d6bd00ca]
- Repository development practice: the handoff defines six mechanical completion checks (commits count, all test files passing, plugin.json version bump, tag creation, dogfood gate files present, and everything pushed to origin) before reporting done. [@claim:clm_a5c21d1cc098e49905a060f22999d02e6e849325791befe32f71497e8e287b44]
<!-- rcw:end owner=source:src_fdb9354a2bce53e4af16325026808e10 block=evidence -->

## Researcher notes

