---
access: public
aliases: []
claim_ids:
- clm_468c5c1ae1ae6b478fc7ff3d1c29c1f008e0c5d7059cd5c600a6781644b11068
- clm_67acda3a4f656d110d3cc1f516153c97d1261e1600b7139d0e7939c04e5e2f32
- clm_75b5815b0090f20052326fae8ec7601288a8ef2a5e94d455fa4506bd6e8514b8
maturity: draft
page_id: pg_f45dfb6529015285aec33ba92f530c9a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_283a78178ec25110ae9839024a84a29d
title: tastyeffectco/sandboxd/README.md @ 146711407bb9
updated_at: '2026-09-14T03:18:13Z'
---

# tastyeffectco/sandboxd/README.md @ 146711407bb9

<!-- rcw:begin owner=source:src_283a78178ec25110ae9839024a84a29d block=evidence -->
- Running sandboxd requires Docker plus the Compose plugin and git on Linux (macOS via Docker Desktop is best-effort), runs natively on amd64 and arm64, and installs via a one-line curl script. [@claim:clm_468c5c1ae1ae6b478fc7ff3d1c29c1f008e0c5d7059cd5c600a6781644b11068]
- sandboxd is an open-source, self-hosted AI app builder: a prompt causes a coding agent to build a real app in an isolated sandbox on the user's server, each app live at a preview URL. [@claim:clm_67acda3a4f656d110d3cc1f516153c97d1261e1600b7139d0e7939c04e5e2f32]
- The project is beta 0.x: isolation is containers rather than VMs, it is single-server, API auth is off by default, and breaking changes are expected before 1.0. [@claim:clm_75b5815b0090f20052326fae8ec7601288a8ef2a5e94d455fa4506bd6e8514b8]
<!-- rcw:end owner=source:src_283a78178ec25110ae9839024a84a29d block=evidence -->

## Researcher notes

