---
access: public
aliases: []
claim_ids:
- clm_098c74ed0d2c35d80eb08d50034835ecbde6526d89b5d276b8f2e3af7ca7e7e7
- clm_81db7311c1cca63c59ee9d4fc09f6bd5a58ff79ca078086b811c0c0ea82a40e1
- clm_b7423a1778e84c83b35ead9ca8b2b9e18d8ce3a69fdd10e9aefbb219b2779611
maturity: draft
page_id: pg_ce0348cddf1c57869e8921961770d3bd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6aaa47dd31245717b0d5522959ab620b
title: pchalasani/claude-code-tools/docs/find-claude-session.md @ ee0f3099c05c
updated_at: '2026-09-14T04:15:23Z'
---

# pchalasani/claude-code-tools/docs/find-claude-session.md @ ee0f3099c05c

<!-- rcw:begin owner=source:src_6aaa47dd31245717b0d5522959ab620b block=evidence -->
- find-claude-session maps a project directory to ~/.claude/projects/<path with slashes replaced by dashes>, streams JSONL line by line, requires all keywords case-insensitively, sorts by modification time, and shows the top 10 matches. [@claim:clm_098c74ed0d2c35d80eb08d50034835ecbde6526d89b5d276b8f2e3af7ca7e7e7]
- find-claude-session is a CLI that keyword-searches Claude Code session files with an interactive selection UI and automatic resumption via claude -r; a -g/--global flag searches across all projects. [@claim:clm_81db7311c1cca63c59ee9d4fc09f6bd5a58ff79ca078086b811c0c0ea82a40e1]
- find-claude-session requires Python 3.11+ and click, with rich as an optional dependency for the interactive UI. [@claim:clm_b7423a1778e84c83b35ead9ca8b2b9e18d8ce3a69fdd10e9aefbb219b2779611]
<!-- rcw:end owner=source:src_6aaa47dd31245717b0d5522959ab620b block=evidence -->

## Researcher notes

