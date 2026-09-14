---
access: public
aliases: []
claim_ids:
- clm_0337996feec59dd33c4b3d34b8c3696c00cea779d6897ef81fa7f83a0f43d5d6
- clm_533c81dd384a202572178406512950b400861323cee51997ca4c6a69a627fce7
- clm_6c92e9683047e7cc46371c8efb77ae3c8a9fdc89743ad0b7a5f5546bad0378ee
- clm_84d30e9a9f5496a3e59d34b72ac62b55cf4d7995dddbb03bbffad299ce02f9d8
- clm_ab162e8dc66e92a32ac979db517974f05fa7fa925f586657879566d9a5b12804
- clm_b5dd0e031cb9792a299221ab42700412b646fa9e72f6dce5e7483ecd9168e041
- clm_c3d8e4b253000de701b7c2fc4ab91385f78dcb218ff881074ae495b0471d9843
maturity: draft
page_id: pg_c08ba58e2e245025b5ad6347174a095f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9bcd6d7a96365db1ac42b8c81f113522
title: ultraworkers/claw-code/how_to_run.md @ 08106b0c3771
updated_at: '2026-09-14T03:20:41Z'
---

# ultraworkers/claw-code/how_to_run.md @ 08106b0c3771

<!-- rcw:begin owner=source:src_9bcd6d7a96365db1ac42b8c81f113522 block=evidence -->
- claw-analog exposes subcommands including doctor (config preview, env status, workspace search, optional build, TCP ping), config validate (offline TOML/profile check with --strict), and complete for shell completion in bash, zsh, fish, and powershell. [@claim:clm_0337996feec59dd33c4b3d34b8c3696c00cea779d6897ef81fa7f83a0f43d5d6]
- The harness requires a provider API key (e.g. ANTHROPIC_API_KEY or OPENAI_API_KEY); Claude subscription login is not a supported auth path, and claw-analog selects providers by model and environment variables. [@claim:clm_533c81dd384a202572178406512950b400861323cee51997ca4c6a69a627fce7]
- claw-analog supports --output-format json emitting NDJSON on stdout for scripts and CI, --stream for SSE streaming, and explicit limits such as --max-turns (default 24), --max-read-bytes (262144), and glob/grep caps. [@claim:clm_6c92e9683047e7cc46371c8efb77ae3c8a9fdc89743ad0b7a5f5546bad0378ee]
- Permission modes include read-only, workspace-write, prompt, and danger-full-access/allow; write_file is unavailable in read-only and prompt modes, and danger modes are forbidden non-interactively without an explicit accept flag. [@claim:clm_84d30e9a9f5496a3e59d34b72ac62b55cf4d7995dddbb03bbffad299ce02f9d8]
- claw-analog enforces a canonical workspace root with relative paths, no `..`, and symlink/canonicalize containment checks; a PermissionPolicy and PermissionEnforcer gate tools, and dangerous modes are blocked in non-interactive runs unless explicitly accepted. [@claim:clm_ab162e8dc66e92a32ac979db517974f05fa7fa925f586657879566d9a5b12804]
- claw-analog supports JSON session files (version 1) holding workspace, model, optional preset, and API-format messages; history is loaded on resume and saved after each tool round, with a --save-session export path and warnings about secrets and token cost. [@claim:clm_b5dd0e031cb9792a299221ab42700412b646fa9e72f6dce5e7483ecd9168e041]
- claw-analog is a lean agent on the same API layer with a narrow filesystem-only toolset (read_file, list_dir, glob_workspace, grep_workspace, git_diff, git_log, optional write_file and retrieve_context) and no arbitrary shell, MCP, or plugins. [@claim:clm_c3d8e4b253000de701b7c2fc4ab91385f78dcb218ff881074ae495b0471d9843]
<!-- rcw:end owner=source:src_9bcd6d7a96365db1ac42b8c81f113522 block=evidence -->

## Researcher notes

