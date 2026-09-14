---
access: public
aliases: []
claim_ids:
- clm_11c174646ea441616ad37e2461eef5f12563c89163630b1b52428ff0b7761350
- clm_1927dcf64aec32ce21111fbc053ca5a52e260bafec228141bd7986c6f4b089d0
- clm_2c3b28d9db15231e4826b283f7baad112332ab89ab7b004a04998dfb1429c83a
- clm_60f633ba7bb8669426b272cdd46dc41f97f90ed0949912390425759dfd2055df
- clm_6f4552093dfc4819b70703c4e690cfa18a763faf6a7289354f21332e5e96e1eb
- clm_bbfae7a8e419e3065d9568805753f398f9d4ea0b5681ec04bc6b6155913143e7
- clm_c2ac3148178583ac309ce8e6cbbd29842dd95093d9f926c4897e70afe1877f92
maturity: draft
page_id: pg_3e93a6e1df4c59f3a004a5de3c04c6e9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e426ba9267a55086860f5f7eeeb5052c
title: 2389-research/coven-gateway/README.md @ 11425046d196
updated_at: '2026-09-14T04:41:43Z'
---

# 2389-research/coven-gateway/README.md @ 11425046d196

<!-- rcw:begin owner=source:src_e426ba9267a55086860f5f7eeeb5052c block=evidence -->
- The gateway exposes an HTTP API on port 8080 with endpoints for listing agents, sending messages with SSE streaming responses, health/readiness checks, and channel-binding CRUD. [@claim:clm_11c174646ea441616ad37e2461eef5f12563c89163630b1b52428ff0b7761350]
- The repository layout includes an agent manager with connection registry and channel bindings, a gateway orchestrator with gRPC and HTTP API handlers, a config loader, and a SQLite persistence store. [@claim:clm_1927dcf64aec32ce21111fbc053ca5a52e260bafec228141bd7986c6f4b089d0]
- Routing uses channel bindings that map frontend channels (e.g., Slack, Matrix) to specific agents for sticky agent assignment. [@claim:clm_2c3b28d9db15231e4826b283f7baad112332ab89ab7b004a04998dfb1429c83a]
- Repository development practice: contributors build with make (proto plus binaries), run tests via go test ./... (optionally with -race), and can install pre-commit hooks running go fmt, go vet, go test, and go mod tidy. [@claim:clm_60f633ba7bb8669426b272cdd46dc41f97f90ed0949912390425759dfd2055df]
- SQLite persistence for threads and messages is implemented in pure Go without CGO, and the database path is configurable, including an in-memory option for testing. [@claim:clm_6f4552093dfc4819b70703c4e690cfa18a763faf6a7289354f21332e5e96e1eb]
- The README lists Slack frontend integration, Prometheus metrics, and mTLS agent authentication as planned rather than implemented, indicating these capabilities are not yet shipped in Phase 1. [@claim:clm_bbfae7a8e419e3065d9568805753f398f9d4ea0b5681ec04bc6b6155913143e7]
- Building requires Go 1.22+, the protoc compiler, and proto generation expects the coven-agent repository checked out as a sibling directory; the project is MIT licensed. [@claim:clm_c2ac3148178583ac309ce8e6cbbd29842dd95093d9f926c4897e70afe1877f92]
<!-- rcw:end owner=source:src_e426ba9267a55086860f5f7eeeb5052c block=evidence -->

## Researcher notes

