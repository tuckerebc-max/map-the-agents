---
access: public
aliases: []
claim_ids:
- clm_284ee53b233a5bd7c32a72700fcc6a4d9e4965a94b412fb5beefda8e0a3637ef
- clm_28df0c67b0b8449675e230afee62f7d2a96ad031d0fa61fab0eaa418df445c98
- clm_8047ed3e8fc4752d42b18ec7d0cf6aeccda90403ba3a1a219ed7d520e1ccb6fe
- clm_b2172dee153cf5264e5a3d605f07cb9cf2220701514c1611f774b563ae6a37e8
maturity: draft
page_id: pg_1b8480662a5b56df88aa9593be5aba67
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5469a0a0bd0d5a82951335ed2a7d1f7b
title: dazuiba/handoff/CLAUDE.md @ 717ac79e1885
updated_at: '2026-09-14T03:06:31Z'
---

# dazuiba/handoff/CLAUDE.md @ 717ac79e1885

<!-- rcw:begin owner=source:src_5469a0a0bd0d5a82951335ed2a7d1f7b block=evidence -->
- The CLI exposes run, resume, list/ls, tail, env, init, and new commands; list and tail provide interactive TUI views of task history and live output streams. [@claim:clm_284ee53b233a5bd7c32a72700fcc6a4d9e4965a94b412fb5beefda8e0a3637ef]
- State persists under ~/.handoff, including config.yaml, a SQLite runs database (handoff.db), and tui_state.json storing the user's TUI theme choice. [@claim:clm_28df0c67b0b8449675e230afee62f7d2a96ad031d0fa61fab0eaa418df445c98]
- Repository development practice: CLAUDE.md provides guidance to Claude Code when working with code in this repository, including a file map of the cli/ package and release steps. [@claim:clm_8047ed3e8fc4752d42b18ec7d0cf6aeccda90403ba3a1a219ed7d520e1ccb6fe]
- Repository development practice: releases are made by bumping the version in pyproject.toml, committing, tagging vX.Y.Z, and pushing; a v* tag triggers a workflow that builds with uv build and publishes to PyPI. [@claim:clm_b2172dee153cf5264e5a3d605f07cb9cf2220701514c1611f774b563ae6a37e8]
<!-- rcw:end owner=source:src_5469a0a0bd0d5a82951335ed2a7d1f7b block=evidence -->

## Researcher notes

