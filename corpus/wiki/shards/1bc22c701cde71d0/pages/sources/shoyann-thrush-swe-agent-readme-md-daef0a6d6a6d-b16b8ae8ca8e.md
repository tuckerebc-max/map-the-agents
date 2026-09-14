---
access: public
aliases: []
claim_ids:
- clm_3c2f5390bbb0afe128de2d0e68b8c9e306100cf4913dec904c880f587b3b2d1a
- clm_4dbc1854ca6ee65c4edb73b974457d5cb7c7e3fe0a2d7143f1c3ed208d30ff4e
- clm_7e6464333ecf12589fc953d9d751453083ee9243650e60a1f3ab0b41c14c0a89
- clm_93207794c906f7a5a3a5e6e38ba6ddc9a9805a92efd99242a9b5a319a3bdb448
- clm_c8dbd520fe1832b697c76f960007c48bfad79cb9920a451cc59687cd6e6dde45
- clm_caebe72601b17f80ddb6c1159a90fea84a793edaa0f60c8de3addc9fd4d7c9a4
- clm_cb8a432e7cfe1bdf21b8a023f1eff93e4828ede144acb95f3bef8d40e8ef5d2b
- clm_da554f128ee17778a6872f38ab62432877141a3474cb58e3567b7d1f19ffd8b1
- clm_e8315007274e6a17064b2d3d7e1cb1b81721f103b1bff49beab64cb58bfdca43
- clm_f2bc33ea7684df7f6a7858e9d8226ef2e94d3c3d788a7b3926bba918a7b18b80
maturity: draft
page_id: pg_d39018a97ff65f1db509b16b8ae8ca8e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2f501cf3fdf6502f8d9676eea2fd6654
title: shoyann/thrush-swe-agent/README.md @ daef0a6d6a6d
updated_at: '2026-09-14T02:40:06Z'
---

# shoyann/thrush-swe-agent/README.md @ daef0a6d6a6d

<!-- rcw:begin owner=source:src_2f501cf3fdf6502f8d9676eea2fd6654 block=evidence -->
- The app is built with Next.js 15 and TypeScript 5, uses SQLite for local state, and bundles mini-swe-agent; a bootstrap step prepares data/mini-venv with the bundled agent and Python dependencies. [@claim:clm_3c2f5390bbb0afe128de2d0e68b8c9e306100cf4913dec904c880f587b3b2d1a]
- Auto runs collect diff, diff stat, changed files, logs, and trajectory, and generate a human-readable Auto Report shown with these artifacts in a side drawer. [@claim:clm_4dbc1854ca6ee65c4edb73b974457d5cb7c7e3fe0a2d7143f1c3ed208d30ff4e]
- Auto Mode is backed by a bundled mini-swe-agent checkout in vendor/mini-swe-agent with a non-interactive runner at scripts/mini-auto-run.py; an ADR states the bundled copy should be managed as a Git submodule or clearly tracked vendored dependency. [@claim:clm_7e6464333ecf12589fc953d9d751453083ee9243650e60a1f3ab0b41c14c0a89]
- Before Auto starts, an Environment Doctor checks Git clean state, Docker availability, mini runtime readiness, model API key configuration, and GitHub readiness. [@claim:clm_93207794c906f7a5a3a5e6e38ba6ddc9a9805a92efd99242a9b5a319a3bdb448]
- Repository development practice: contributors run npm run test, npx tsc --noEmit, and npm run lint; the repo includes tests for Auto data flow, readiness checks, recommended environments, the mini resolver, and runner behavior with fake mini results. [@claim:clm_c8dbd520fe1832b697c76f960007c48bfad79cb9920a451cc59687cd6e6dde45]
- Thrush offers two modes in one UI: Assist, where the agent drafts edits and the user approves before files are written, and Auto, where the agent attempts a full task in isolation and returns a report and diff. [@claim:clm_caebe72601b17f80ddb6c1159a90fea84a793edaa0f60c8de3addc9fd4d7c9a4]
- Auto Mode runs mini-swe-agent in a separate Git worktree under data/auto-runs/<autoRunId>/worktree on a branch auto/<autoRunId>, leaving the main workspace unchanged; Draft PR creation is a user action, not automatic. [@claim:clm_cb8a432e7cfe1bdf21b8a023f1eff93e4828ede144acb95f3bef8d40e8ef5d2b]
- Local state lives under data/: a SQLite database (thrush.db) with separate tables for Auto runs, events, artifacts, and presets, plus workspace, auto-runs, mini-venv, and pip/uv cache directories. [@claim:clm_da554f128ee17778a6872f38ab62432877141a3474cb58e3567b7d1f19ffd8b1]
- In Assist Mode the agent can inspect files, search code, read pages, and run allowlisted commands; file writes are staged as pending drafts requiring explicit approval, and file tools reject paths outside the active workspace. [@claim:clm_e8315007274e6a17064b2d3d7e1cb1b81721f103b1bff49beab64cb58bfdca43]
- Model providers are configurable via environment variables: MODEL_PROVIDER supports deepseek (default), openai, or anthropic, with per-provider API key, base URL, and model variables, plus an AGENT_API_SECRET bearer token for /api/agent. [@claim:clm_f2bc33ea7684df7f6a7858e9d8226ef2e94d3c3d788a7b3926bba918a7b18b80]
<!-- rcw:end owner=source:src_2f501cf3fdf6502f8d9676eea2fd6654 block=evidence -->

## Researcher notes

