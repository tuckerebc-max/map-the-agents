---
access: public
aliases: []
claim_ids:
- clm_12c60edba7a308a82be3f81c29c71c2eb639390ea1e236841cf3a70b9fd5eff4
- clm_735a327598ce7b0decf61d1f827a564edb2d08ccab93bbd6b104e417e8f48e20
- clm_dad1a5bf1de07d03a0856f07526352d88fca3e59476413bff9f3b0b3dda7959e
- clm_fb337e2cf51c4d55e0ea07500271d803daf8ee09719cd38d19a134f779f14511
maturity: draft
page_id: pg_967372f5d24054e1a61432dfa79308d6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_880d5122b7ad573b90f5c82a98faa882
title: Dicklesworthstone/frankenterm/SECURITY.md @ 9416f404da44
updated_at: '2026-09-14T03:07:04Z'
---

# Dicklesworthstone/frankenterm/SECURITY.md @ 9416f404da44

<!-- rcw:begin owner=source:src_880d5122b7ad573b90f5c82a98faa882 block=evidence -->
- `ft` runs as the invoking user with no privilege separation; captured terminal bytes are redacted only on read surfaces, with the on-disk SQLite store holding raw bytes protected by file permissions. [@claim:clm_12c60edba7a308a82be3f81c29c71c2eb639390ea1e236841cf3a70b9fd5eff4]
- The threat model treats host compromise and pre-existing DB write access as out of scope (attacker-equivalent), and notes findings requiring those positions should be reported as normal bugs. [@claim:clm_735a327598ce7b0decf61d1f827a564edb2d08ccab93bbd6b104e417e8f48e20]
- Per its security policy, the project has no CVE pipeline (fixes tracked by bead and commit) and release artifacts are not yet signed. [@claim:clm_dad1a5bf1de07d03a0856f07526352d88fca3e59476413bff9f3b0b3dda7959e]
- The stdio MCP transport (`ft mcp serve`) inherits the OS uid/gid with no in-band authentication, while MCP tool inputs are validated via workspace containment, size caps, and approval gating on mutating tools. [@claim:clm_fb337e2cf51c4d55e0ea07500271d803daf8ee09719cd38d19a134f779f14511]
<!-- rcw:end owner=source:src_880d5122b7ad573b90f5c82a98faa882 block=evidence -->

## Researcher notes

