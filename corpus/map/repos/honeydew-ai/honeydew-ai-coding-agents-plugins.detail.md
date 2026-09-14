# honeydew-ai/honeydew-ai-coding-agents-plugins -- full detail

[Back to orientation](honeydew-ai-coding-agents-plugins.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/120377ae/aac60f1b/36797d906d0ae0730e9580ab59995df48431d442/075790f34c5eb551.json](../../../wiki/dossiers/120377ae/aac60f1b/36797d906d0ae0730e9580ab59995df48431d442/075790f34c5eb551.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Skills are written as agent-agnostic markdown documentation that any MCP-capable coding agent can consume as prompts or instructions, rather than being tied to one agent's plugin format. -- evidence: [README.md#L93-L93](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L93-L93) (`clm_e7f90bae5ffc00a9572e7dab1ba4435578342d45b9999b123ace762c72a09bb6`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: version bumps treat .claude-plugin/plugin.json as the source of truth, require updating ten version-bearing files, and contributors run ./scripts/validate-versions.sh locally before pushing. -- evidence: [AGENTS.md#L40-L49](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L40-L49), [AGENTS.md#L51-L51](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L51-L51), [AGENTS.md#L36-L36](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L36-L36) (`clm_b8df81b2a76109e7eb7063c0052b95ca8c0fb7d932dc8c233d6044270f7f2365`)
- [observation/documented] Repository development practice: GitHub Actions CI on PRs validates YAML frontmatter, plugin structure and version consistency, and skill registration (Copilot skills array, .cursor/skills symlinks, README table and count). -- evidence: [AGENTS.md#L76-L76](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L76-L76), [AGENTS.md#L108-L110](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L108-L110) (`clm_dd1c51eed1e72df619f1676282df2f108f775b635f5a311ab01f9e4af6ecae64`)
- [observation/documented] Repository development practice: adding a new skill requires creating SKILL.md with YAML frontmatter, updating .cursor/skills symlinks, the GitHub Copilot plugin.json skills array, the README table, and AGENTS.md, then bumping the version. -- evidence: [AGENTS.md#L67-L67](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L67-L67), [AGENTS.md#L69-L74](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L69-L74) (`clm_92be926ba41044dd0a9a93026967b48c013cf07ab3be04e0a2f0c79b544c4ead`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The plugin is distributed through agent-specific marketplaces: Claude Code and Copilot CLI use /plugin marketplace add, Codex uses codex plugin marketplace add, Cursor uses a Team Marketplace dashboard, and Gemini CLI uses gemini extensions install. -- evidence: [README.md#L44-L46](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L44-L46), [README.md#L77-L81](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L77-L81), [README.md#L65-L67](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L65-L67), [README.md#L24-L26](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L24-L26), [README.md#L87-L89](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L87-L89) (`clm_30b49378fa7be3341529dc148e09ddb4567e000c8ad2af473d6cce3e5a358de4`)
- [observation/documented] A Claude-specific release zip packages the plugin in claude.ai's expected layout, with .claude-plugin/plugin.json at the zip root alongside .mcp.json, hooks/, assets/, and skill markdown files. -- evidence: [README.md#L191-L191](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L191-L191) (`clm_1998c197a235053dba156a5b5715d51791b7297d28707cff0744e86639051dd1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] PreToolUse hooks gate Honeydew MCP tool calls: query, exploration, and typed create/update calls are blocked once per session when the matching skill is not loaded, with the block naming the skill to load before the retry proceeds. -- evidence: [CHANGELOG.md#L55-L56](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/CHANGELOG.md#L55-L56), [CHANGELOG.md#L276-L276](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/CHANGELOG.md#L276-L276) (`clm_1bc47c994d43ff224e4c0e0b2db88fb2be7b3bc98418608bb6920fe662d92a4b`)
- [observation/documented] The hook gating is designed to be non-wedging: a block fires at most once per skill so a retry always goes through, and uncertain cases such as a missing skill or unparseable payload let the call proceed. -- evidence: [CHANGELOG.md#L55-L56](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/CHANGELOG.md#L55-L56) (`clm_2a906f7fa72b7c6c0e561a1ba549193a9d800a50f6484e37a34c037faa77bc4e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites are a coding agent with plugin/skill or MCP support (e.g., Claude Code, Codex, Cursor, Copilot CLI, Gemini CLI) and a Honeydew AI workspace with the Honeydew MCP server configured. -- evidence: [README.md#L15-L16](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L15-L16) (`clm_8d0ac02a03ee4384318e38132f61956406d7eb4e58ea9b3bd515e889ce5483b2`)
- [observation/documented] Supported data warehouses are Snowflake, Databricks, and BigQuery. -- evidence: [README.md#L183-L185](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L183-L185) (`clm_0e62889ea81350963a827d5b27535a93ddd0c3a318d54a58b1241741cc2aca2c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

