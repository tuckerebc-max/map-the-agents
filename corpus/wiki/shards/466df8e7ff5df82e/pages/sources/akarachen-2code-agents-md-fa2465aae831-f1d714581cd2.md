---
access: public
aliases: []
claim_ids:
- clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e
- clm_f5cf8800e6b7e498dc4d3a3efecfdb95d5898bbc7b3248f52ee84080ead95e0d
maturity: draft
page_id: pg_0f00289f6ff15ac89827f1d714581cd2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_af7a325fac025b8cb7c1e4ba34bc0e59
title: AkaraChen/2code/AGENTS.md @ fa2465aae831
updated_at: '2026-09-14T03:32:48Z'
---

# AkaraChen/2code/AGENTS.md @ fa2465aae831

<!-- rcw:begin owner=source:src_af7a325fac025b8cb7c1e4ba34bc0e59 block=evidence -->
- Repository development practice: contributors add Tauri commands in handler/*.rs, register them in lib.rs, then run cargo tauri-typegen generate; Rust tests run via cargo test with in-memory SQLite, and CI includes a Tauri smoke test on ubuntu-24.04 with xvfb-run. [@claim:clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e]
- The app is a Tauri 2 desktop shell with a React 19 + TypeScript + Vite frontend, Zustand/Immer client state, TanStack Query server state, and a Rust workspace backend with SQLite via Diesel. [@claim:clm_f5cf8800e6b7e498dc4d3a3efecfdb95d5898bbc7b3248f52ee84080ead95e0d]
<!-- rcw:end owner=source:src_af7a325fac025b8cb7c1e4ba34bc0e59 block=evidence -->

## Researcher notes

