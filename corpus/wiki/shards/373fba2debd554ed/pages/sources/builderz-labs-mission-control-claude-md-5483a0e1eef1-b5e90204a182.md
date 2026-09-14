---
access: public
aliases: []
claim_ids:
- clm_31212c1d4d335e7942fc8bd6f87a23ae17c6ec1c7d1f146cf5e319ac534ba5af
- clm_35b971152edc765141f3e51ab6883445e05b12e0599dc358fe2d2dba684db957
- clm_37cdac3e5f3e8fcda08363661f418cae560fc71eb6b56a4bee2a08617ac17bd1
maturity: draft
page_id: pg_20077d14bd6c5965b9d0b5e90204a182
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d05969d4458a590fb8cc3279135f9337
title: builderz-labs/mission-control/CLAUDE.md @ 5483a0e1eef1
updated_at: '2026-09-14T01:59:56Z'
---

# builderz-labs/mission-control/CLAUDE.md @ 5483a0e1eef1

<!-- rcw:begin owner=source:src_d05969d4458a590fb8cc3279135f9337 block=evidence -->
- Runtime data defaults to a .data/ directory, overridable via the MISSION_CONTROL_DATA_DIR environment variable; the database defaults to <data dir>/mission-control.db. [@claim:clm_31212c1d4d335e7942fc8bd6f87a23ae17c6ec1c7d1f146cf5e319ac534ba5af]
- The stack is documented as Next.js 16 App Router, React 19, TypeScript 5, Tailwind CSS 4, Zustand, Recharts, xterm.js, and SQLite via better-sqlite3 in WAL mode, with Zod validation at input boundaries. [@claim:clm_35b971152edc765141f3e51ab6883445e05b12e0599dc358fe2d2dba684db957]
- Repository development practice: contributors run pnpm install --frozen-lockfile, lint, typecheck, test, build, and test:e2e, with pnpm quality:gate running the full repository gate; commits follow Conventional Commits with no AI-attribution trailers and pnpm is the only package manager. [@claim:clm_37cdac3e5f3e8fcda08363661f418cae560fc71eb6b56a4bee2a08617ac17bd1]
<!-- rcw:end owner=source:src_d05969d4458a590fb8cc3279135f9337 block=evidence -->

## Researcher notes

