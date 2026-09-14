---
access: public
aliases: []
claim_ids:
- clm_210b97eed9bce74aee8ec375093c95733656c3f3c9c2f432a2b158b009b08808
- clm_df431e42e62aac8deb9f94d13c79c402be1d86440ba1988de47b346e9fbf261d
maturity: draft
page_id: pg_029ffe41633b581a8304ad5d0d8fe2de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d458a280775e594ba83a4f6f86c1081d
title: traycerai/traycer/AGENTS.md @ b12949767727
updated_at: '2026-09-14T03:19:55Z'
---

# traycerai/traycer/AGENTS.md @ b12949767727

<!-- rcw:begin owner=source:src_d458a280775e594ba83a4f6f86c1081d block=evidence -->
- Repository development practice: commits must not manually run compile/build/lint/format beforehand because pre-commit runs affected workspace checks, and make dev-desktop targets the production cloud with no local backends. [@claim:clm_210b97eed9bce74aee8ec375093c95733656c3f3c9c2f432a2b158b009b08808]
- Repository development practice: contributors use Bun 1.3.12 workspaces with Nx, run build/compile/lint/format via bun scripts, and commits require DCO sign-off; tests run in CI, not pre-commit hooks. [@claim:clm_df431e42e62aac8deb9f94d13c79c402be1d86440ba1988de47b346e9fbf261d]
<!-- rcw:end owner=source:src_d458a280775e594ba83a4f6f86c1081d block=evidence -->

## Researcher notes

