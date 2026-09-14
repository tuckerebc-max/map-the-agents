---
access: public
aliases: []
claim_ids:
- clm_68c1220a2a0a7d6c4d5bdce2eea7edde21e6fd2dfdcf975b6d38b5dfd80918c1
- clm_831cd3f04849cbaf0aaed82937ff9acb1e7d437acc1c8812074a55b2cdd8a781
- clm_a8ac17ae18bb73c54e70b647c6c55e45617787687a898ab2ae07ec5193c8b0c7
maturity: draft
page_id: pg_1084e3ed0bd15a8babde8b59c47da1ad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c2fe5d56968c53a2a86353900bd81dcf
title: alexgreensh/outsourcerer/SECURITY.md @ 0ad71828e118
updated_at: '2026-09-14T01:32:15Z'
---

# alexgreensh/outsourcerer/SECURITY.md @ 0ad71828e118

<!-- rcw:begin owner=source:src_c2fe5d56968c53a2a86353900bd81dcf block=evidence -->
- Before any cloud delegation, a hard-block refuses the route if credential files (.env, id_rsa, credentials, etc.) exist anywhere in the working tree; the scan runs on every call and fails closed. [@claim:clm_68c1220a2a0a7d6c4d5bdce2eea7edde21e6fd2dfdcf975b6d38b5dfd80918c1]
- Repository development practice: the project is audited with repo-forensics (27 scanners, 500+ patterns) on every release, with every finding triaged by name and no suppressions, per README and SECURITY.md. [@claim:clm_831cd3f04849cbaf0aaed82937ff9acb1e7d437acc1c8812074a55b2cdd8a781]
- Keys are read one variable at a time from ~/.env via targeted grep, never sourcing the whole file, and keys are never written into command-line arguments, logs, or config. [@claim:clm_a8ac17ae18bb73c54e70b647c6c55e45617787687a898ab2ae07ec5193c8b0c7]
<!-- rcw:end owner=source:src_c2fe5d56968c53a2a86353900bd81dcf block=evidence -->

## Researcher notes

