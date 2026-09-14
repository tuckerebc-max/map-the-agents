---
access: public
aliases: []
claim_ids:
- clm_07d3b1438fd274ec16ef003070b0dbae2d0de9a737afed50666127426d2c7a8d
- clm_a3da54a361ea3be8ab1d570c303d765d075c1e3a686c8171f5fdd083ee7dfe9d
maturity: draft
page_id: pg_de1021ef71b8595daef57668bd5757cf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_39ef7683b3db57d39c84f838b10c65b2
title: the-open-agent/openagent/CLAUDE.md @ b98d42165dc0
updated_at: '2026-09-14T03:19:07Z'
---

# the-open-agent/openagent/CLAUDE.md @ b98d42165dc0

<!-- rcw:begin owner=source:src_39ef7683b3db57d39c84f838b10c65b2 block=evidence -->
- Repository development practice: CLAUDE.md documents a Beego MVC backend where each entity follows a three-layer pattern (object structs with xorm tags, controllers wired to routes in routers/router.go, and auto-migration via engine.Sync2 in object/adapter.go), with composite primary keys of (Owner, Name). [@claim:clm_07d3b1438fd274ec16ef003070b0dbae2d0de9a737afed50666127426d2c7a8d]
- Repository development practice: CLAUDE.md instructs contributors to build with go build, run tests via go test ./..., and develop the React frontend with yarn install/start/lint:js; a full production build via build.sh cross-compiles for linux/amd64, arm64, and riscv64. [@claim:clm_a3da54a361ea3be8ab1d570c303d765d075c1e3a686c8171f5fdd083ee7dfe9d]
<!-- rcw:end owner=source:src_39ef7683b3db57d39c84f838b10c65b2 block=evidence -->

## Researcher notes

