# pacifio/cersei

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 708c5055845b @ 0499d6a79e014dbf

## Summary (orientation draft, not independently verified)

Selected evidence records: Cersei is described as a Rust SDK exposing the building blocks of a coding agent — tool execution, LLM streaming, sub-agent orchestration, persistent memory, skills, and MCP integration — as composable library functions. The workspace is organized into crates including cersei-types, cersei-provider, cersei-tools, cersei-tools-derive, cersei-agent, cersei-memory, cersei-hooks, cersei-mcp, a cersei facade crate, and abstract-cli.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Cersei is described as a Rust SDK exposing the building blocks of a coding agent — tool execution, LLM streaming, sub-agent orchestration, persistent memory, skills, and MCP integration — as composable library functions. -- evidence: [README.md#L5-L5](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L5-L5), [README.md#L3-L3](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The workspace is organized into crates including cersei-types, cersei-provider, cersei-tools, cersei-tools-derive, cersei-agent, cersei-memory, cersei-hooks, cersei-mcp, a cersei facade crate, and abstract-cli. -- evidence: [README.md#L118-L129](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L118-L129)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the README instructs running the workspace test suite with 'cargo test --workspace', optionally with '--features graph', or per-crate with 'cargo test -p cersei-tools' and similar. -- evidence: [README.md#L475-L475](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L475-L475), [README.md#L478-L478](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L478-L478), [README.md#L481-L485](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L481-L485)
  - [observation/documented] Repository development practice: the docs subdirectory is a Next.js/Fumadocs application; its README describes starting a dev server via npm run dev, pnpm dev, or yarn dev on localhost:3000. -- evidence: [docs/README.md#L16-L16](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L16-L16), [docs/README.md#L11-L11](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L11-L11), [docs/README.md#L13-L14](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L13-L14), [docs/README.md#L8-L9](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L8-L9), [docs/README.md#L3-L4](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/docs/README.md#L3-L4)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills auto-discover from .claude/commands/*.md, .claude/skills/*/SKILL.md, user-level ~/.claude/commands, and bundled skills; a SkillTool lists skills and expands $ARGUMENTS templates. -- evidence: [README.md#L239-L242](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L239-L242), [README.md#L232-L237](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L232-L237)
- interfaces (2 claim(s)):
  - [observation/documented] Agents are constructed via a builder API supporting provider, tools, model/temperature/max_tokens, system prompt, working directory, permission policy, memory, hooks, and context-management options. -- evidence: [README.md#L343-L346](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L343-L346), [README.md#L333-L335](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L333-L335), [README.md#L348-L351](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L348-L351), [README.md#L337-L341](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L337-L341), [README.md#L329-L331](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L329-L331), [README.md#L325-L327](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L325-L327), [README.md#L318-L323](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L318-L323), [README.md#L309-L312](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L309-L312)
  - [observation/documented] MCP integration connects stdio and SSE servers via McpManager and exposes their tool definitions to the agent builder; the MCP client uses JSON-RPC 2.0 over stdio transport. -- evidence: [README.md#L118-L129](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L118-L129), [README.md#L295-L296](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L295-L296), [README.md#L283-L293](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L283-L293)
- memory-state (2 claim(s)):
  - [observation/documented] Memory is three-tier: flat markdown files scanned with frontmatter, a CLAUDE.md hierarchy merged into context, and an optional Grafeo graph layer supporting tagged store/recall queries with text fallback. -- evidence: [README.md#L220-L223](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L220-L223), [README.md#L213-L215](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L213-L215), [README.md#L217-L218](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L217-L218)
  - [observation/documented] Sessions persist as append-only JSONL with tombstone soft-delete, and messages can be written and reloaded per session id. -- evidence: [README.md#L225-L228](https://github.com/pacifio/cersei/blob/708c5055845ba6c682d92960cec99e3adbcca3e1/README.md#L225-L228)
- orchestration (1 claim(s)):
More evidence: [full detail](cersei.detail.md)

Metadata and full claim list: [full detail](cersei.detail.md)
Human notes ([notes](cersei.notes.md), never overwritten by build)

[Back to map index](../../index.md)
