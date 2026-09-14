---
access: public
aliases: []
claim_ids:
- clm_5d9100d5c44897ec2ac9e389f8ba0a6907932f67d63eeae6232aad31ff52363a
- clm_c29a242e29d2aaa2b2e09f37629326a9db8e9ad257196324124698b97d2d5f17
- clm_e007aa779d0827cb75d9e77a4d5dffc2eb2ad237cee1d1197e549223957fe770
- clm_e6be9196497b053573dee7d3a6fdcd15fb7ec8ac364a14c07270e61f8c58fa76
- clm_f0aa1e354583391d27e16712a01167dbf73da0dd39532d9279fc33f1294d4288
- clm_fd3cdf004ae18f452e19063e3fef75fafd7efe0110999b0fcf7c5c29408993d6
maturity: draft
page_id: pg_61dc97eed4e856258839c8ba5a1cea20
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_92d709ad7385564a852f5e97e513e5af
title: sammwyy/singulary/ARCHITECTURE.md @ 5b51298504a4
updated_at: '2026-09-14T02:38:43Z'
---

# sammwyy/singulary/ARCHITECTURE.md @ 5b51298504a4

<!-- rcw:begin owner=source:src_92d709ad7385564a852f5e97e513e5af block=evidence -->
- The backend (apps/server) is an Express application on Node.js using TypeScript, responsible for API routing, an agent loop with SSE-streamed LLM responses, Docker orchestration, and SQLite metadata storage. [@claim:clm_5d9100d5c44897ec2ac9e389f8ba0a6907932f67d63eeae6232aad31ff52363a]
- The browser client communicates with the Express API over REST, SSE, and WebSocket, and the backend manages interactive shells via WebSocket. [@claim:clm_c29a242e29d2aaa2b2e09f37629326a9db8e9ad257196324124698b97d2d5f17]
- Singulary is a monorepo with a React frontend and an Express backend; in production the frontend is built to static assets and served by the same Express process that exposes the API under /api. [@claim:clm_e007aa779d0827cb75d9e77a4d5dffc2eb2ad237cee1d1197e549223957fe770]
- Frontend data flow follows View -> hook -> service -> API, with hooks writing results into Zustand stores that cache fetched data; mutations update stores and hooks may expose refetch() to bypass the cache. [@claim:clm_e6be9196497b053573dee7d3a6fdcd15fb7ec8ac364a14c07270e61f8c58fa76]
- SQLite stores instance metadata by default at storage/singulary.sqlite, tracking user accounts, token limits, rules, and workspace topology. [@claim:clm_f0aa1e354583391d27e16712a01167dbf73da0dd39532d9279fc33f1294d4288]
- The frontend (apps/web) is a React app powered by Vite and styled with Tailwind CSS, organized into components, hooks, services, Zustand stores, utils, and views directories. [@claim:clm_fd3cdf004ae18f452e19063e3fef75fafd7efe0110999b0fcf7c5c29408993d6]
<!-- rcw:end owner=source:src_92d709ad7385564a852f5e97e513e5af block=evidence -->

## Researcher notes

