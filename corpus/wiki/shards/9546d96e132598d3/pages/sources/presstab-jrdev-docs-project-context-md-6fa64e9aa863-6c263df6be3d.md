---
access: public
aliases: []
claim_ids:
- clm_18d5627d2211c8599bc39302273b1f50d3d3ce8fb81175ea2ef46e6c2512ce76
- clm_426a84bdac74b688192cf0b1631beb17609fb60c06034f6f1b59cb1480019ab5
- clm_eb69fd348ee217f0bd0a37562962196fffc520cb0e68a89881920b27879d1f59
maturity: draft
page_id: pg_22afe7026ed95bd8a8f46c263df6be3d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7474f03bafcd55e4b59591f81b5b63fe
title: presstab/jrdev/docs/project_context.md @ 6fa64e9aa863
updated_at: '2026-09-14T02:32:45Z'
---

# presstab/jrdev/docs/project_context.md @ 6fa64e9aa863

<!-- rcw:begin owner=source:src_7474f03bafcd55e4b59591f81b5b63fe block=evidence -->
- An index.json in .jrdev tracks context files, their last modification times, and summary file paths; /projectcontext update and refresh handle outdated files. [@claim:clm_18d5627d2211c8599bc39302273b1f50d3d3ce8fb81175ea2ef46e6c2512ce76]
- The /projectcontext command supports subcommands on|off, status, list, view <filepath>, update, refresh <filepath>, add <filepath>, and remove <filepath> for managing project context. [@claim:clm_426a84bdac74b688192cf0b1631beb17609fb60c06034f6f1b59cb1480019ab5]
- The /init command builds persistent project context: a file tree scan, AI-selected key files (up to 20), machine-readable file summaries in .jrdev/context/, plus generated jrdev_conventions.md and jrdev_overview.md in .jrdev. [@claim:clm_eb69fd348ee217f0bd0a37562962196fffc520cb0e68a89881920b27879d1f59]
<!-- rcw:end owner=source:src_7474f03bafcd55e4b59591f81b5b63fe block=evidence -->

## Researcher notes

