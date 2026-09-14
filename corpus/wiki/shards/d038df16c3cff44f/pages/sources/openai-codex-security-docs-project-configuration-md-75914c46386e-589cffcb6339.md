---
access: public
aliases: []
claim_ids:
- clm_18328b54eba69035bddc8cf88ccce85a6b4bc3c7ae71b378d15a81d269fd50de
- clm_2f62067f36b9b46e934c430d2f741d85ceafbe390c4ac1e975c87653276385fa
- clm_8ad1ae0be8c3b10cd6cbcbdef14751b4938ec90f4cfa90e9fc335b3d7d05684d
- clm_aaaf86f72f1cb8a6fbe88d44d815d5b6878878711f18bd2d71abf7012a53326e
maturity: draft
page_id: pg_66e25abb4e215ab8b56b589cffcb6339
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c17def866e145294ac5fb65fa6c7cc0d
title: openai/codex-security/docs/project-configuration.md @ 75914c46386e
updated_at: '2026-09-14T03:11:02Z'
---

# openai/codex-security/docs/project-configuration.md @ 75914c46386e

<!-- rcw:begin owner=source:src_c17def866e145294ac5fb65fa6c7cc0d block=evidence -->
- Project configuration files use snake_case keys while SDK options use camelCase and CLI flags kebab-case; a shared ScanSettings type underlies all three resolution paths. [@claim:clm_18328b54eba69035bddc8cf88ccce85a6b4bc3c7ae71b378d15a81d269fd50de]
- Settings precedence is built-in defaults, legacy deep settings, the project file, then explicit CLI values; lists are replaced rather than concatenated, and scope selectors from the CLI override the file's scope variant. [@claim:clm_2f62067f36b9b46e934c430d2f741d85ceafbe390c4ac1e975c87653276385fa]
- Deep diff scans and custom validation remain unsupported in deep mode, and discovery time cannot exceed 96 hours; the cost limit is per scan attempt and in-flight work may exceed it. [@claim:clm_8ad1ae0be8c3b10cd6cbcbdef14751b4938ec90f4cfa90e9fc335b3d7d05684d]
- Config loading is deliberately literal: no JavaScript evaluation, environment interpolation, remote includes, or multi-file merging; unknown keys and invalid types are errors, and YAML anchors are supported with alias-expansion guards. [@claim:clm_aaaf86f72f1cb8a6fbe88d44d815d5b6878878711f18bd2d71abf7012a53326e]
<!-- rcw:end owner=source:src_c17def866e145294ac5fb65fa6c7cc0d block=evidence -->

## Researcher notes

