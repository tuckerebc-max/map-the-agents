---
access: public
aliases: []
claim_ids:
- clm_27fb9b7b9870be1372716dbbee667b3005fdc2cd0a72ba2618c32c9873d04939
- clm_45ee35485f6fb08a9641f7fdbf320af99e88e35f867ef8d8b5e0bbd13b749fb8
- clm_6c92e9683047e7cc46371c8efb77ae3c8a9fdc89743ad0b7a5f5546bad0378ee
- clm_ab162e8dc66e92a32ac979db517974f05fa7fa925f586657879566d9a5b12804
- clm_b59504dbc6a2e2fc2c5b091b4799ff2ae0f423adfcf2c99403f04520f9ca65fb
- clm_c3d8e4b253000de701b7c2fc4ab91385f78dcb218ff881074ae495b0471d9843
- clm_f9faca4de03ad88168dcc7b9fdfda5a72ca44e8f2328f8aad9de107c44c51907
maturity: draft
page_id: pg_95fadcd50e055ba4bc3e5ba832257289
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_99a905feba42511ba6fb11182ff62324
title: ultraworkers/claw-code/concept.md @ 08106b0c3771
updated_at: '2026-09-14T03:20:41Z'
---

# ultraworkers/claw-code/concept.md @ 08106b0c3771

<!-- rcw:begin owner=source:src_99a905feba42511ba6fb11182ff62324 block=evidence -->
- Heavy indexing and embedding storage are deliberately kept out of claw-analog; the agent only calls retrieval over HTTP so the vector store and embedding secrets can be scaled or changed independently. [@claim:clm_27fb9b7b9870be1372716dbbee667b3005fdc2cd0a72ba2618c32c9873d04939]
- The Rust workspace contains the main `claw` CLI (rusty-claude-cli), an `api` crate for provider clients and streaming, a `runtime` crate with sessions and permission policy/enforcer, a `tools` crate, `claw-analog`, and `claw-rag-service`. [@claim:clm_45ee35485f6fb08a9641f7fdbf320af99e88e35f867ef8d8b5e0bbd13b749fb8]
- claw-analog supports --output-format json emitting NDJSON on stdout for scripts and CI, --stream for SSE streaming, and explicit limits such as --max-turns (default 24), --max-read-bytes (262144), and glob/grep caps. [@claim:clm_6c92e9683047e7cc46371c8efb77ae3c8a9fdc89743ad0b7a5f5546bad0378ee]
- claw-analog enforces a canonical workspace root with relative paths, no `..`, and symlink/canonicalize containment checks; a PermissionPolicy and PermissionEnforcer gate tools, and dangerous modes are blocked in non-interactive runs unless explicitly accepted. [@claim:clm_ab162e8dc66e92a32ac979db517974f05fa7fa925f586657879566d9a5b12804]
- The main `claw` CLI is described as a full agent with a REPL, OAuth, an extended toolset including bash, MCP and plugins, streaming, and integration with Anthropic, OpenAI-compatible, and xAI providers. [@claim:clm_b59504dbc6a2e2fc2c5b091b4799ff2ae0f423adfcf2c99403f04520f9ca65fb]
- claw-analog is a lean agent on the same API layer with a narrow filesystem-only toolset (read_file, list_dir, glob_workspace, grep_workspace, git_diff, git_log, optional write_file and retrieve_context) and no arbitrary shell, MCP, or plugins. [@claim:clm_c3d8e4b253000de701b7c2fc4ab91385f78dcb218ff881074ae495b0471d9843]
- claw-rag-service is a separate process that indexes a repository into SQLite chunks plus embeddings and exposes an HTTP API with routes including /, /health, /v1/stats, and /v1/query, plus a minimal web UI. [@claim:clm_f9faca4de03ad88168dcc7b9fdfda5a72ca44e8f2328f8aad9de107c44c51907]
<!-- rcw:end owner=source:src_99a905feba42511ba6fb11182ff62324 block=evidence -->

## Researcher notes

