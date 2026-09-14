# yasasbanukaofficial/claude-code

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a371abbe75ff @ 73a49aa297deb07e

## Summary (orientation draft, not independently verified)

The repository is a mirror/breakdown of leaked Claude Code source code exposed via an npm sourcemap, with README-described architecture and features of the leaked product; no actual source files are present in the provided evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Claude Code is described as a large CLI with a 785KB main.tsx entry point using a React/Ink terminal renderer, 40+ tools, and multi-agent orchestration. -- evidence: [README.md#L46-L46](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L46-L46)
  - [observation/documented] The described source layout includes main.tsx as CLI entrypoint, QueryEngine.ts for core LLM logic, a tools directory, services, a coordinator for swarm orchestration, a bridge for IDE integration, and a buddy directory. -- evidence: [README.md#L75-L85](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L75-L85)
- design-choices (1 claim(s)):
  - [inference/documented] The leak mechanism appears to be that source maps embed original source under sourcesContent, and the package reportedly shipped .map files because npmignore/build settings omitted them. -- evidence: [README.md#L27-L27](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L27-L27), [README.md#L38-L38](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L38-L38)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README instructs cloning the repo, running npm install, building with npm run build, and running the CLI via node dist/main.js. -- evidence: [README.md#L113-L116](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L113-L116), [README.md#L108-L111](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L108-L111), [README.md#L97-L101](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L97-L101), [README.md#L103-L106](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L103-L106)
- skills-patterns (1 claim(s)):
  - [observation/documented] A Tamagotchi-style companion system is described under src/buddy/, using a Mulberry32 PRNG seeded from userId, 18 species tiers, and stats such as DEBUGGING, CHAOS, and SNARK. -- evidence: [README.md#L49-L52](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L49-L52)
- interfaces (1 claim(s)):
  - [observation/documented] The repo ships an MCP server command (claude mcp add code-explorer with claude-code-explorer-mcp) intended to let users explore the source using Claude. -- evidence: [README.md#L119-L122](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L119-L122)
- memory-state (1 claim(s)):
  - [observation/documented] An autoDream background service is described that reads MEMORY.md, gathers signals from daily logs, consolidates durable memory files, and prunes context. -- evidence: [README.md#L61-L65](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L61-L65)
- orchestration (1 claim(s)):
  - [observation/documented] KAIROS is described as an always-on proactive assistant watching logs, and ULTRAPLAN offloads complex tasks to a remote Opus 4.6 session for up to 30 minutes of planning. -- evidence: [README.md#L68-L69](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L68-L69)
- tools-permissions (1 claim(s)):
  - [observation/documented] An 'Undercover Mode' utility is described that blocks internal model codenames and hides that the user is an AI, apparently intended for Anthropic employees contributing to public repos. -- evidence: [README.md#L55-L58](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L55-L58)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README lists Bun runtime as highly recommended (or Node.js v18+) and globally installed TypeScript as prerequisites for the mirrored code. -- evidence: [README.md#L92-L93](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L92-L93)
- limitations (1 claim(s)):
More evidence: [full detail](claude-code.detail.md)

Metadata and full claim list: [full detail](claude-code.detail.md)
Human notes ([notes](claude-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
