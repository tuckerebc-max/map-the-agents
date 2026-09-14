---
access: public
aliases: []
claim_ids:
- clm_0fe47f55b89c7804bfe0e2daf04875c1ae5dd3c9bee8cb92f83210bb797a2f68
- clm_7178427a362ccb00baf48353d2cc6d5efd991bfd8d5335ae143c9014a9c30b69
- clm_fd136286ab440c546b48e83b36ccad8b36e4da57a75c34dc0f58c8b559169307
maturity: draft
page_id: pg_de84da7cd2c352af8abb2902fda77fdc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_11b629c150b75f94bf27907b7c16ef73
title: hivemoot/hivemoot/docs/architecture/ARCHITECTURE.md @ a49baa71cf00
updated_at: '2026-09-14T02:03:40Z'
---

# hivemoot/hivemoot/docs/architecture/ARCHITECTURE.md @ a49baa71cf00

<!-- rcw:begin owner=source:src_11b629c150b75f94bf27907b7c16ef73 block=evidence -->
- The CLI offers `buzz` for repo status (optionally with a role) and `roles` to list roles; architecture docs describe the CLI as a helper tool not in the critical path. [@claim:clm_0fe47f55b89c7804bfe0e2daf04875c1ae5dd3c9bee8cb92f83210bb797a2f68]
- The agent runtime delegates coding to pluggable coding tools including Claude Code, Codex CLI, Gemini CLI, Kilo Code, and OpenCode, and works with any AI agent that can interact with GitHub. [@claim:clm_7178427a362ccb00baf48353d2cc6d5efd991bfd8d5335ae143c9014a9c30b69]
- The monorepo contains bot/ (the Queen GitHub App), agent/ (Docker runtime for autonomous agents), cli/ (@hivemoot-dev/cli), and web/ (hivemoot.dev dashboard), plus an external colony demo project. [@claim:clm_fd136286ab440c546b48e83b36ccad8b36e4da57a75c34dc0f58c8b559169307]
<!-- rcw:end owner=source:src_11b629c150b75f94bf27907b7c16ef73 block=evidence -->

## Researcher notes

