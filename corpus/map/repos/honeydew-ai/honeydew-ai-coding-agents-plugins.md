# honeydew-ai/honeydew-ai-coding-agents-plugins

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 36797d906d0a @ 075790f34c5eb551

## Summary (orientation draft, not independently verified)

The plugin is distributed through agent-specific marketplaces: Claude Code and Copilot CLI use /plugin marketplace add, Codex uses codex plugin marketplace add, Cursor uses a Team Marketplace dashboard, and Gemini CLI uses gemini extensions install. A Claude-specific release zip packages the plugin in claude.ai's expected layout, with .claude-plugin/plugin.json at the zip root alongside .mcp.json, hooks/, assets/, and skill markdown files.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Skills are written as agent-agnostic markdown documentation that any MCP-capable coding agent can consume as prompts or instructions, rather than being tied to one agent's plugin format. -- evidence: [README.md#L93-L93](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L93-L93)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: version bumps treat .claude-plugin/plugin.json as the source of truth, require updating ten version-bearing files, and contributors run ./scripts/validate-versions.sh locally before pushing. -- evidence: [AGENTS.md#L40-L49](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L40-L49), [AGENTS.md#L51-L51](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L51-L51), [AGENTS.md#L36-L36](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L36-L36)
  - [observation/documented] Repository development practice: GitHub Actions CI on PRs validates YAML frontmatter, plugin structure and version consistency, and skill registration (Copilot skills array, .cursor/skills symlinks, README table and count). -- evidence: [AGENTS.md#L76-L76](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L76-L76), [AGENTS.md#L108-L110](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/AGENTS.md#L108-L110)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The plugin is distributed through agent-specific marketplaces: Claude Code and Copilot CLI use /plugin marketplace add, Codex uses codex plugin marketplace add, Cursor uses a Team Marketplace dashboard, and Gemini CLI uses gemini extensions install. -- evidence: [README.md#L44-L46](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L44-L46), [README.md#L77-L81](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L77-L81), [README.md#L65-L67](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L65-L67), [README.md#L24-L26](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L24-L26), [README.md#L87-L89](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L87-L89)
  - [observation/documented] A Claude-specific release zip packages the plugin in claude.ai's expected layout, with .claude-plugin/plugin.json at the zip root alongside .mcp.json, hooks/, assets/, and skill markdown files. -- evidence: [README.md#L191-L191](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/README.md#L191-L191)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] PreToolUse hooks gate Honeydew MCP tool calls: query, exploration, and typed create/update calls are blocked once per session when the matching skill is not loaded, with the block naming the skill to load before the retry proceeds. -- evidence: [CHANGELOG.md#L55-L56](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/CHANGELOG.md#L55-L56), [CHANGELOG.md#L276-L276](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/CHANGELOG.md#L276-L276)
  - [observation/documented] The hook gating is designed to be non-wedging: a block fires at most once per skill so a retry always goes through, and uncertain cases such as a missing skill or unparseable payload let the call proceed. -- evidence: [CHANGELOG.md#L55-L56](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/blob/36797d906d0ae0730e9580ab59995df48431d442/CHANGELOG.md#L55-L56)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](honeydew-ai-coding-agents-plugins.detail.md)

Metadata and full claim list: [full detail](honeydew-ai-coding-agents-plugins.detail.md)
Human notes ([notes](honeydew-ai-coding-agents-plugins.notes.md), never overwritten by build)

[Back to map index](../../index.md)
