---
access: public
aliases: []
claim_ids:
- clm_126a818828fc5fa39f06e210bd38b6c840d848de7d23f950b5aeff418a258820
- clm_15f483d5d0c948bfe8e6127d664719d02a455c1a5824d49471240ada74787872
- clm_2b2a5c0e9ab28f334d6022174762e1e3d9ddfe36689f7e69aba58e5ebd5753a5
- clm_642ecc87f8d114510b4607622cddbb5cd26f19a1dd8564ff83e91bcd69aa67a1
- clm_79e8877558d9eaf91ce5e5890999044b24a08ed93b0d6966189de4ee440695df
- clm_d5533bd1e3377a071c2ae63ce897ff4fda76d5e6e90aefceb0792a09329194a0
- clm_ee1fde860d23a596c41016df08bd69a10e3eb29382052903093ce6bd3c5362ba
maturity: draft
page_id: pg_6bf1412d0b175d0d9b82a4a82148fe8c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa242b07a9145b78970a5ad23a1cb1e5
title: Human-Agent-Society/CORAL/README.md @ 0123dfb939b3
updated_at: '2026-09-14T03:57:24Z'
---

# Human-Agent-Society/CORAL/README.md @ 0123dfb939b3

<!-- rcw:begin owner=source:src_aa242b07a9145b78970a5ad23a1cb1e5 block=evidence -->
- A skills-first plugin (no MCP) for Claude Code and Codex teaches the coral workflow, scaffolds a .coral_workspace with a seed and grader, and loops coral validate until launch-ready; it includes coral-task-author and coral-run-doctor subagents on Claude Code. [@claim:clm_126a818828fc5fa39f06e210bd38b6c840d848de7d23f950b5aeff418a258820]
- coral start creates shared state, per-agent git worktrees, a grader daemon, generated CORAL.md instructions, and agent subprocesses; the manager interrupts agents with heartbeat prompts like reflect, consolidate, and pivot. [@claim:clm_15f483d5d0c948bfe8e6127d664719d02a455c1a5824d49471240ada74787872]
- Repository development practice: contributors install dev deps with uv sync --extra dev, run tests via uv run pytest tests/ -v, and lint/format with ruff; CONTRIBUTING.md and AGENTS.md cover PR workflow and rules for agent-authored contributions. [@claim:clm_2b2a5c0e9ab28f334d6022174762e1e3d9ddfe36689f7e69aba58e5ebd5753a5]
- In Docker sessions the agent runs as an unprivileged user while the manager and grader stay root, preventing agents from reading .coral/private/ grader material; on the host this isolation is opt-in via agents.isolate_user. [@claim:clm_642ecc87f8d114510b4607622cddbb5cd26f19a1dd8564ff83e91bcd69aa67a1]
- Some built-in graders (e.g. SWE-bench, terminal-bench) use Harbor to run evaluations in Docker containers, and CORAL itself must not run inside Docker in that case. [@claim:clm_79e8877558d9eaf91ce5e5890999044b24a08ed93b0d6966189de4ee440695df]
- The coral CLI includes commands such as init, start, validate, status, log, notes, skills, wait, checkout, and heartbeat set, with dotlist key=value config overrides supported on start. [@claim:clm_d5533bd1e3377a071c2ae63ce897ff4fda76d5e6e90aefceb0792a09329194a0]
- Shared state lives in .coral/public/ (attempts, notes, skills, logs, heartbeat, steering, eval counter) and is symlinked into every agent worktree; grader venvs and answer keys stay hidden in .coral/private/. [@claim:clm_ee1fde860d23a596c41016df08bd69a10e3eb29382052903093ce6bd3c5362ba]
<!-- rcw:end owner=source:src_aa242b07a9145b78970a5ad23a1cb1e5 block=evidence -->

## Researcher notes

