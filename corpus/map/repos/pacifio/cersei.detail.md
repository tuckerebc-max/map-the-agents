# pacifio/cersei -- full detail

[Back to orientation](cersei.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pacifio/cersei/708c5055845ba6c682d92960cec99e3adbcca3e1/0499d6a79e014dbf.json](../../../wiki/dossiers/pacifio/cersei/708c5055845ba6c682d92960cec99e3adbcca3e1/0499d6a79e014dbf.json)

## specifications (1 claim(s))

- [observation/documented] Cersei is described as a Rust SDK exposing the building blocks of a coding agent — tool execution, LLM streaming, sub-agent orchestration, persistent memory, skills, and MCP integration — as composable library functions. -- evidence: [README.md#L5-L5](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L5-L5), [README.md#L3-L3](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L3-L3) (`clm_a2c4be17e1ec17fd42aec0f2457c1802da1b4606e364f6a1a9ad8b0374109dfb`)

## components (1 claim(s))

- [observation/documented] The workspace is organized into crates including cersei-types, cersei-provider, cersei-tools, cersei-tools-derive, cersei-agent, cersei-memory, cersei-hooks, cersei-mcp, a cersei facade crate, and abstract-cli. -- evidence: [README.md#L118-L129](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L118-L129) (`clm_a21cb760f77cdf377656f6df7fb6c870c2a5ac597fc0e9ee5735a8837521aa16`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the README instructs running the workspace test suite with 'cargo test --workspace', optionally with '--features graph', or per-crate with 'cargo test -p cersei-tools' and similar. -- evidence: [README.md#L475-L475](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L475-L475), [README.md#L478-L478](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L478-L478), [README.md#L481-L485](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L481-L485) (`clm_51939f3e0ab35c2240d6fbd7ca403c16c7400d8aa61742866f5d9de88b95365c`)
- [observation/documented] Repository development practice: the docs subdirectory is a Next.js/Fumadocs application; its README describes starting a dev server via npm run dev, pnpm dev, or yarn dev on localhost:3000. -- evidence: [docs/README.md#L16-L16](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L16-L16), [docs/README.md#L11-L11](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L11-L11), [docs/README.md#L13-L14](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L13-L14), [docs/README.md#L8-L9](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L8-L9), [docs/README.md#L3-L4](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L3-L4) (`clm_91e5e63fffac48e7fe134d3adc566f1fab75e4dd5b0379bfe7b584205d5d4a65`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills auto-discover from .claude/commands/*.md, .claude/skills/*/SKILL.md, user-level ~/.claude/commands, and bundled skills; a SkillTool lists skills and expands $ARGUMENTS templates. -- evidence: [README.md#L239-L242](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L239-L242), [README.md#L232-L237](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L232-L237) (`clm_259d5738952c044e6d62eb05076b3cb496f5f5074538b22c426de2e9939724d6`)

## interfaces (2 claim(s))

- [observation/documented] Agents are constructed via a builder API supporting provider, tools, model/temperature/max_tokens, system prompt, working directory, permission policy, memory, hooks, and context-management options. -- evidence: [README.md#L343-L346](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L343-L346), [README.md#L333-L335](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L333-L335), [README.md#L348-L351](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L348-L351), [README.md#L337-L341](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L337-L341), [README.md#L329-L331](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L329-L331), [README.md#L325-L327](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L325-L327), [README.md#L318-L323](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L318-L323), [README.md#L309-L312](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L309-L312) (`clm_f8fa920e10027f871240ab9bc5cfcdf64ba8763a63c7b89c23d9523498455dc1`)
- [observation/documented] MCP integration connects stdio and SSE servers via McpManager and exposes their tool definitions to the agent builder; the MCP client uses JSON-RPC 2.0 over stdio transport. -- evidence: [README.md#L118-L129](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L118-L129), [README.md#L295-L296](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L295-L296), [README.md#L283-L293](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L283-L293) (`clm_06f4228bb952599dbd759e294fcf575aad6e909b9e285be969fba93d634a9a21`)

## memory-state (2 claim(s))

- [observation/documented] Memory is three-tier: flat markdown files scanned with frontmatter, a CLAUDE.md hierarchy merged into context, and an optional Grafeo graph layer supporting tagged store/recall queries with text fallback. -- evidence: [README.md#L220-L223](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L220-L223), [README.md#L213-L215](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L213-L215), [README.md#L217-L218](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L217-L218) (`clm_99c766990a956f80d84f6e9a94579da166d052fe3c0f83715ed932e8bc0e1f96`)
- [observation/documented] Sessions persist as append-only JSONL with tombstone soft-delete, and messages can be written and reloaded per session id. -- evidence: [README.md#L225-L228](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L225-L228) (`clm_7c7b381fa6f40cdf53fb0762e308f25144a875960519f212a18e78b787a2873d`)

## orchestration (1 claim(s))

- [observation/documented] Sub-agent orchestration includes an AgentTool the model can spawn autonomously, a coordinator mode with parallel workers whose tools are filtered to prevent recursion, and a task system (TaskCreate through TaskOutput). -- evidence: [README.md#L201-L203](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L201-L203), [README.md#L191-L194](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L191-L194), [README.md#L196-L199](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L196-L199) (`clm_fce70803312adb0ffbb1d477af132890972a30ef4725ca58b2ad07c16f118bfd`)

## tools-permissions (1 claim(s))

- [observation/documented] The SDK exposes a runtime permission model with selectable policies including AllowAll, AllowReadOnly, DenyAll, RuleBased, and Interactive, plus interactive permissions with session caching in the CLI. -- evidence: [README.md#L329-L331](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L329-L331), [README.md#L86-L96](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L86-L96) (`clm_9a43e031744baf7f41efecd557529d3510fe04ef902fa22b76dd03a752d11c6b`)

## evaluation (1 claim(s))

- [observation/documented] The repo ships agent-performance benchmarks: Terminal Bench 2.0 end-to-end coding tasks in Daytona sandboxes, LongMemEval recall accuracy vs Mastra/Zep/Supermemory with LLM-as-judge, and general-agent framework comparisons. -- evidence: [README.md#L401-L409](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L401-L409) (`clm_b059bd89bafae3c4faf876bae440748168ab533584db7412cc64054d43773065`)

## dependencies (1 claim(s))

- [observation/documented] Using the SDK requires adding cersei (via git), tokio with the 'full' feature, and anyhow; the #[derive(Tool)] macro additionally needs async-trait and a cersei-tools dependency. -- evidence: [README.md#L164-L170](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L164-L170), [README.md#L102-L107](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L102-L107) (`clm_6c5954b537d41eb74d6d9fae0c51a418d72da816264d745e43ded2facae57883`)

## limitations (1 claim(s))

- [observation/documented] After a replace_all that matched a fuzzy candidate, the reported replacements_made count is only an approximation; the docs warn against depending on an exact fuzzy-replace-all count. -- evidence: [docs/atlas-edit-tool-migration.md#L77-L90](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/atlas-edit-tool-migration.md#L77-L90) (`clm_c7e46f3bc51c1043600c06f89b92e290022052837a300142453bd195c537d746`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

