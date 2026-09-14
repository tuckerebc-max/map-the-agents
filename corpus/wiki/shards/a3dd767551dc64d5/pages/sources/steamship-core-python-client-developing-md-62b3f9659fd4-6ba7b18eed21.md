---
access: public
aliases: []
claim_ids:
- clm_20f595ad8df8899839f8d2da22e3629317b37cfd294fa3a4db9bf856c3e8fc32
- clm_5b289535eb1d0e1431886570e6488df463c22eb5f8fdb4377d3a650226a140e4
- clm_6d00e8456e6b45c4866c383289e08be539c8cccc30bd69cad22523ab10c4798a
- clm_a584d98cea3b80ed3e33d1e59389b401df7328610cf2fc378f293467babd64ae
maturity: draft
page_id: pg_28c0901570585ef78e686ba7b18eed21
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ab7ea1830b0e5ed3a293bcc7c158e886
title: steamship-core/python-client/DEVELOPING.md @ 62b3f9659fd4
updated_at: '2026-09-14T02:43:24Z'
---

# steamship-core/python-client/DEVELOPING.md @ 62b3f9659fd4

<!-- rcw:begin owner=source:src_ab7ea1830b0e5ed3a293bcc7c158e886 block=evidence -->
- Repository development practice: releases are deployed by creating a semver tag (without 'v') targeting main via the GitHub Release feature. [@claim:clm_20f595ad8df8899839f8d2da22e3629317b37cfd294fa3a4db9bf856c3e8fc32]
- Repository development practice: contributors target Python 3.8, format with black and isort, run CI via GitHub Actions, and use pre-commit hooks (flake8, mypy, bandit, etc.) for linting; tests use Pyunit. [@claim:clm_5b289535eb1d0e1431886570e6488df463c22eb5f8fdb4377d3a650226a140e4]
- The codebase is layered: base depends on nothing; data on base; plugin on base and data; client on base, data, plugin; and app on all four. [@claim:clm_6d00e8456e6b45c4866c383289e08be539c8cccc30bd69cad22523ab10c4798a]
- Repository development practice: integration tests run against a live Steamship server using a 'test' profile in ~/.steamship.json, and a client fixture cleans up space-scoped resources, though apps, app versions, plugins, and plugin versions must be destroyed manually. [@claim:clm_a584d98cea3b80ed3e33d1e59389b401df7328610cf2fc378f293467babd64ae]
<!-- rcw:end owner=source:src_ab7ea1830b0e5ed3a293bcc7c158e886 block=evidence -->

## Researcher notes

