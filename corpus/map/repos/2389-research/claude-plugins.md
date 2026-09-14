# 2389-research/claude-plugins

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 017d34612ebf @ bb0f6c55bd4c81bf

## Summary (orientation draft, not independently verified)

This repository is the 2389 Research Claude Code plugin marketplace: documentation and site content cataloging ~28 plugins and 4 MCP servers, plus a development guide for maintaining the CSS and Firebase skills. Evidence is mostly documentation; no plugin implementation code appears in the slices.

## Source coverage

Source coverage (partial): 6 of 63 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository is a marketplace of 28 plugins and MCP servers for Claude Code covering parallel exploration, iterative refinement, binary reverse engineering, and structured decision-making. -- evidence: [README.md#L6-L6](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L6-L6)
- components (2 claim(s)):
  - [observation/documented] The catalog includes plugins such as simmer (iterative refinement with investigation-first judges), test-kitchen (parallel implementation exploration), thrifty (tiered Sonnet/Haiku delegation), and binary-re (ELF reverse engineering). -- evidence: [README.md#L42-L51](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L42-L51), [README.md#L55-L64](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L55-L64), [docs/index.md#L35-L42](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L35-L42)
  - [observation/documented] The marketplace lists four MCP servers: agent-drugs, socialmedia, journal, and slack-mcp, providing behavior modification, social media, journaling, and Slack integration. -- evidence: [README.md#L84-L89](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L84-L89)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: adding a plugin requires creating a repo under 2389-research/, adding a marketplace.json entry, running 'npm run generate', then committing and pushing. -- evidence: [README.md#L93-L96](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L93-L96)
  - [observation/documented] Repository development practice: after modifying a skill, contributors copy it into ~/.claude/skills/, test manually against tests/integration scenarios, and verify auto-detection, TodoWrite checklists, and step ordering. -- evidence: [docs/DEVELOPMENT.md#L78-L81](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L78-L81), [docs/DEVELOPMENT.md#L87-L87](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L87-L87), [docs/DEVELOPMENT.md#L89-L93](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L89-L93)
- skills-patterns (4 claim(s)):
  - [observation/documented] Skills are defined in SKILL.md markdown files with YAML frontmatter containing a name and a description used for auto-detection. -- evidence: [docs/DEVELOPMENT.md#L56-L60](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L56-L60), [docs/DEVELOPMENT.md#L52-L52](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L52-L52)
  - [observation/documented] The css-development and firebase-development plugins use a main orchestrator SKILL.md plus sub-skill directories (e.g., create-component, validate, refactor; project-setup, add-feature, debug). -- evidence: [docs/DEVELOPMENT.md#L7-L46](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L7-L46)
- interfaces (2 claim(s)):
  - [observation/documented] Plugins can be installed in any agent (Claude Code, Cursor, Codex) via vercel-labs/skills using 'npx skills add 2389-research/<plugin>'. -- evidence: [README.md#L14-L14](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L14-L14), [README.md#L16-L18](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L16-L18), [docs/index.md#L9-L11](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L9-L11)
  - [observation/documented] Native Claude Code installation uses '/plugin marketplace add 2389-research/claude-plugins' followed by '/plugin install <plugin>@2389-research'. -- evidence: [README.md#L24-L26](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L24-L26), [docs/llms.txt#L15-L18](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/llms.txt#L15-L18)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [inference/documented] The thrifty plugin is documented as benchmarked at roughly 64% lower cost than Opus at equal quality, suggesting some agent-performance evaluation exists, though no eval harness appears in the evidence. -- evidence: [docs/index.md#L48-L52](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L48-L52), [README.md#L42-L51](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L42-L51)
- dependencies (2 claim(s)):
More evidence: [full detail](claude-plugins.detail.md)

Metadata and full claim list: [full detail](claude-plugins.detail.md)
Human notes ([notes](claude-plugins.notes.md), never overwritten by build)

[Back to map index](../../index.md)
