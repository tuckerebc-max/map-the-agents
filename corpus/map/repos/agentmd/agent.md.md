# agentmd/agent.md

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e86e5c8b57d5 @ d9bd0b2eecce1b16

## Summary (orientation draft, not independently verified)

The repository contains an informational specification document (July 2025, Sourcegraph) defining AGENT.md, a standardized Markdown configuration file for agentic coding tools, including placement rules, hierarchical files, @-mentions, migration commands, and tool-integration status.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (4 claim(s)):
  - [observation/documented] The spec requires AGENT.md to be placed in a project's root directory and written in Markdown, and recommends sections covering structure, commands, style, architecture, testing, and security. -- evidence: [README.md#L57-L57](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L57-L57), [README.md#L59-L64](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L59-L64)
  - [observation/documented] Implementations should support a hierarchy of AGENT.md files: root-level for general guidance, subdirectory files for subsystems, and a user-global file at ~/.config/AGENT.md. -- evidence: [README.md#L70-L70](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L70-L70), [README.md#L72-L74](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L72-L74)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The format is intended to be human-readable while remaining parseable by agentic coding tools, positioning one file as a universal voice for any AI coding tool. -- evidence: [README.md#L51-L51](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L51-L51), [README.md#L66-L66](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L66-L66)
  - [observation/documented] Tool implementers are advised to parse AGENT.md at project initialization, extract tool-relevant configuration, provide fallback behavior when absent, and respect legacy tool-specific config files. -- evidence: [README.md#L86-L89](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L86-L89), [README.md#L84-L84](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L84-L84)
- workflows (1 claim(s)):
  - [observation/documented] The document provides migration commands that move legacy configs (e.g., .clinerules, CLAUDE.md, .cursorrules) to AGENT.md and symlink the old paths back, preserving backward compatibility. -- evidence: [README.md#L125-L125](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L125-L125), [README.md#L101-L101](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L101-L101), [README.md#L107-L107](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L107-L107), [README.md#L104-L104](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L104-L104)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] AGENT.md files may reference other files via @-mentions (e.g., @filename.md) to pull in additional context or documentation. -- evidence: [README.md#L80-L80](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L80-L80)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The document lists RFC 2119 and Gruber's Markdown as normative references, and states no IANA actions are required since the .md extension is already registered. -- evidence: [README.md#L254-L254](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L254-L254), [README.md#L252-L252](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L252-L252), [README.md#L246-L246](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L246-L246), [README.md#L250-L250](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L250-L250)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (2 claim(s)):
  - [observation/documented] The document motivates AGENT.md by the proliferation of per-tool config files such as .cursorrules, .windsurfrules, and .clauderules that consumers must maintain separately. -- evidence: [README.md#L49-L49](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L49-L49)
  - [observation/documented] Per the document, Amp has native AGENT.md support since 2025-05-07 (multiple files since 2025-07-07), while several other tools support it via symbolic linking. -- evidence: [README.md#L234-L242](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L234-L242)

(2 additional claim(s) omitted for length; see [full detail](agent.md.detail.md) for every claim.)

Metadata and full claim list: [full detail](agent.md.detail.md)
Human notes ([notes](agent.md.notes.md), never overwritten by build)

[Back to map index](../../index.md)
