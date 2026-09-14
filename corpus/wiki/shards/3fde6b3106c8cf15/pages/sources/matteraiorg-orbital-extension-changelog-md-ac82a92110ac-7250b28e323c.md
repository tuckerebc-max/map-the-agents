---
access: public
aliases: []
claim_ids:
- clm_20e3e817d292ded8844cc4ba33bfb41d055ac7cbeb21295d6a5470f08ec7094e
- clm_48b917c6e30b3d5d9bca9f7730e80d83ca628f6b0092b16634f5e37ba31cf7f0
- clm_4a6639708a628936ef72a8b27396a72bb4fe2813e0887b9352946354e110d577
- clm_57396ddeffff09e57df546c57b442ba66a1e5bc0b40e1bc5eff2bd86df3eb00f
- clm_5c41c45eff133494a955862ad2a3fcc3b5c05073676bd61a8287a4614a9f5524
- clm_b5262fbb4f45509d498fda953b33db229247b4f4756b6c0fcb5ba7e1fecdfa35
- clm_b97dcb4745b89dc4e389bb8187538b90c523817ba4a56b4c74f72b7e1ea422f5
maturity: draft
page_id: pg_6ba9db44a1875749bde37250b28e323c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0c71e76a85045de39bee0694ef1b117c
title: MatterAIOrg/Orbital-Extension/CHANGELOG.md @ ac82a92110ac
updated_at: '2026-09-14T02:16:22Z'
---

# MatterAIOrg/Orbital-Extension/CHANGELOG.md @ ac82a92110ac

<!-- rcw:begin owner=source:src_0c71e76a85045de39bee0694ef1b117c block=evidence -->
- search_files is ripgrep-first with FFF as fallback, one-shot with no cursor parameter, and results capped at 100 with pages telling the model to refine the pattern instead of paginating. [@claim:clm_20e3e817d292ded8844cc4ba33bfb41d055ac7cbeb21295d6a5470f08ec7094e]
- A generate_file native tool produces file artifacts (PDF, DOCX, PPTX, XLSX, CSV, MD, TXT, HTML) via the MatterAI backend, holding binaries in memory until the user explicitly saves to the Downloads folder. [@claim:clm_48b917c6e30b3d5d9bca9f7730e80d83ca628f6b0092b16634f5e37ba31cf7f0]
- A /create-skill command lets users describe a workflow in plain language and creates or updates a reusable skill under .orb/skills/<skill-name>/ with supporting scripts and assets. [@claim:clm_4a6639708a628936ef72a8b27396a72bb4fe2813e0887b9352946354e110d577]
- AGENTS.md project memory is loaded from the repo-level .orb/ directory (alongside project root and legacy .orbital/), shared between the IDE extension and the OrbCode CLI. [@claim:clm_57396ddeffff09e57df546c57b442ba66a1e5bc0b40e1bc5eff2bd86df3eb00f]
- Models are fetched from the backend /v1/models endpoint and registered into the client registry, refreshing on window focus, via a refresh button, and through a 10-minute background poller. [@claim:clm_5c41c45eff133494a955862ad2a3fcc3b5c05073676bd61a8287a4614a9f5524]
- Independent read-only tools (read_file, search_files, list_files, list_code_definition_names, codebase_search, lsp) run concurrently up to 4 at a time, with results committed in model order; mutating and interactive tools stay serialized. [@claim:clm_b5262fbb4f45509d498fda953b33db229247b4f4756b6c0fcb5ba7e1fecdfa35]
- File-edit tools require old_string to match exactly one location copied verbatim from a current read, and replace_all must be set intentionally after verifying all occurrences should change. [@claim:clm_b97dcb4745b89dc4e389bb8187538b90c523817ba4a56b4c74f72b7e1ea422f5]
<!-- rcw:end owner=source:src_0c71e76a85045de39bee0694ef1b117c block=evidence -->

## Researcher notes

