---
access: public
aliases: []
claim_ids:
- clm_1aaf239871483e32b6de25808c7fb28e166782c6304efe89c385c40b9ac0eb56
- clm_3a29f9569888acd3850c28df21479573b2b7ec11368864de98f7a558b6578a6b
- clm_6890487d638c6d5bb3fa7a2d580b989dad1fc18be1fd852c0bb318b7fbdfac34
maturity: draft
page_id: pg_f151222c9fc6558faefd2c96a3bfb006
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0b31519402275c90b2650b68ac73ff78
title: mattolson/agent-sandbox/docs/cli.md @ 5df0b4bc6c57
updated_at: '2026-09-14T04:08:39Z'
---

# mattolson/agent-sandbox/docs/cli.md @ 5df0b4bc6c57

<!-- rcw:begin owner=source:src_0b31519402275c90b2650b68ac73ff78 block=evidence -->
- The agentbox CLI appears to be written in Go, per the CLI reference's description of the tool. [@claim:clm_1aaf239871483e32b6de25808c7fb28e166782c6304efe89c385c40b9ac0eb56]
- agentbox init prompts interactively for project name, agent, mode, and IDE, then generates docker compose and network policy files under .agent-sandbox/ plus a devcontainer.json for devcontainer mode. [@claim:clm_3a29f9569888acd3850c28df21479573b2b7ec11368864de98f7a558b6578a6b]
- agentbox switch changes the active agent without reinitializing, preserving user override files and per-agent state volumes, and regenerating devcontainer.json in devcontainer projects. [@claim:clm_6890487d638c6d5bb3fa7a2d580b989dad1fc18be1fd852c0bb318b7fbdfac34]
<!-- rcw:end owner=source:src_0b31519402275c90b2650b68ac73ff78 block=evidence -->

## Researcher notes

