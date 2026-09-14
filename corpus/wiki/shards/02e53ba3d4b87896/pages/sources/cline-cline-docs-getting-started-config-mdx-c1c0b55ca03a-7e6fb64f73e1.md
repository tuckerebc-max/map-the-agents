---
access: public
aliases: []
claim_ids:
- clm_763d40f53afb4d9336220bf23ccd58ad63d9f143823ab3e6911520e75807f8d4
- clm_b349330bcd7c830e7aec3560106bd0ae829bd972a279b7bbdb33d99a7660bae0
- clm_e19b334c79f94df6bbfd1f0dccdbd94d688298ce17ac9cdeb66f5a139ce50c8b
maturity: draft
page_id: pg_f468137ed2ec5693bcd47e6fb64f73e1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d87d8cf7a2e15163bdcd9a6a00091494
title: cline/cline/docs/getting-started/config.mdx @ c1c0b55ca03a
updated_at: '2026-09-14T01:42:03Z'
---

# cline/cline/docs/getting-started/config.mdx @ c1c0b55ca03a

<!-- rcw:begin owner=source:src_d87d8cf7a2e15163bdcd9a6a00091494 block=evidence -->
- Sandbox mode can be enabled via the CLINE_SANDBOX environment variable, with sandbox session storage configurable through CLINE_SANDBOX_DATA_DIR. [@claim:clm_763d40f53afb4d9336220bf23ccd58ad63d9f143823ab3e6911520e75807f8d4]
- Configuration lives in two scopes: global `~/.cline/` (with data/settings, teams, sessions, SQLite databases, workflows, rules, hooks, skills, agents, plugins, cron) and per-workspace `.cline/`; a custom directory can be set via CLINE_DATA_DIR. [@claim:clm_b349330bcd7c830e7aec3560106bd0ae829bd972a279b7bbdb33d99a7660bae0]
- Shell command execution can be restricted at runtime via the CLINE_COMMAND_PERMISSIONS environment variable, a JSON policy with allow/deny glob patterns where deny overrides allow, plus an allowRedirects option defaulting to false. [@claim:clm_e19b334c79f94df6bbfd1f0dccdbd94d688298ce17ac9cdeb66f5a139ce50c8b]
<!-- rcw:end owner=source:src_d87d8cf7a2e15163bdcd9a6a00091494 block=evidence -->

## Researcher notes

