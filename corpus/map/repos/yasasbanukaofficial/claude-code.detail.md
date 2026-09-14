# yasasbanukaofficial/claude-code -- full detail

[Back to orientation](claude-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yasasbanukaofficial/claude-code/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/73a49aa297deb07e.json](../../../wiki/dossiers/yasasbanukaofficial/claude-code/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/73a49aa297deb07e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Claude Code is described as a large CLI with a 785KB main.tsx entry point using a React/Ink terminal renderer, 40+ tools, and multi-agent orchestration. -- evidence: [README.md#L46-L46](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L46-L46) (`clm_c9e0041c94e7847a5c5a975448b86e356244df56a642cc888b2252ae2010db3c`)
- [observation/documented] The described source layout includes main.tsx as CLI entrypoint, QueryEngine.ts for core LLM logic, a tools directory, services, a coordinator for swarm orchestration, a bridge for IDE integration, and a buddy directory. -- evidence: [README.md#L75-L85](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L75-L85) (`clm_e97b4284efb870561d375cdfbc05624473d889f7fe3aa0507dfd88296ffce8d7`)

## design-choices (1 claim(s))

- [inference/documented] The leak mechanism appears to be that source maps embed original source under sourcesContent, and the package reportedly shipped .map files because npmignore/build settings omitted them. -- evidence: [README.md#L27-L27](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L27-L27), [README.md#L38-L38](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L38-L38) (`clm_f4911b719dde4be77d7c5680e0564632e61d9ad2d1dabd3f169bbd5ac2ce1e8a`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README instructs cloning the repo, running npm install, building with npm run build, and running the CLI via node dist/main.js. -- evidence: [README.md#L113-L116](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L113-L116), [README.md#L108-L111](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L108-L111), [README.md#L97-L101](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L97-L101), [README.md#L103-L106](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L103-L106) (`clm_87aac1aa8e852b35465ea4044ceb7f45dc817c4930574086a2e1b0c743dd1319`)

## skills-patterns (1 claim(s))

- [observation/documented] A Tamagotchi-style companion system is described under src/buddy/, using a Mulberry32 PRNG seeded from userId, 18 species tiers, and stats such as DEBUGGING, CHAOS, and SNARK. -- evidence: [README.md#L49-L52](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L49-L52) (`clm_a4b889356da5f2ed2337fdfc09d37bf9aed296f1d42969210ff994ca6213f8cd`)

## interfaces (1 claim(s))

- [observation/documented] The repo ships an MCP server command (claude mcp add code-explorer with claude-code-explorer-mcp) intended to let users explore the source using Claude. -- evidence: [README.md#L119-L122](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L119-L122) (`clm_8c0dc3c3ec8d05b04b1c90c629710af3cad0021837d700308bfb7c09a329ac4b`)

## memory-state (1 claim(s))

- [observation/documented] An autoDream background service is described that reads MEMORY.md, gathers signals from daily logs, consolidates durable memory files, and prunes context. -- evidence: [README.md#L61-L65](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L61-L65) (`clm_a1bb46c5bd482585c3e644789b267e0125562ae3184f2b9c035314761ac1856e`)

## orchestration (1 claim(s))

- [observation/documented] KAIROS is described as an always-on proactive assistant watching logs, and ULTRAPLAN offloads complex tasks to a remote Opus 4.6 session for up to 30 minutes of planning. -- evidence: [README.md#L68-L69](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L68-L69) (`clm_09411e6dba7d6f2b5511883328dcad9c45b93b4229027c4c1020ca08a3823d83`)

## tools-permissions (1 claim(s))

- [observation/documented] An 'Undercover Mode' utility is described that blocks internal model codenames and hides that the user is an AI, apparently intended for Anthropic employees contributing to public repos. -- evidence: [README.md#L55-L58](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L55-L58) (`clm_8317ce599d9d69d4b9ee99d5b07c4d272996bab64ca4d3f94667edbf3898c91a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README lists Bun runtime as highly recommended (or Node.js v18+) and globally installed TypeScript as prerequisites for the mirrored code. -- evidence: [README.md#L92-L93](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L92-L93) (`clm_a4cb666a7415aeaf02c72fe763201c8d852956e46be69f0e3b79537639e45eb1`)

## limitations (1 claim(s))

- [observation/documented] The README states the author did not leak the files and only documents access to the codebase for research purposes, with all code remaining proprietary to Anthropic PBC. -- evidence: [README.md#L137-L137](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L137-L137), [README.md#L11-L11](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L11-L11) (`clm_6bcdb1b99c50a0ac0a77065c0d2fcc3e21b2806696b0103802a872f8b4843421`)

## relevance (1 claim(s))

- [observation/documented] The repo is a backup and breakdown of Claude Code source code that was exposed on npm via a bundled sourcemap file, credited to a discovery shared on Twitter/X. -- evidence: [README.md#L15-L15](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L15-L15), [README.md#L19-L19](https://github.com/yasasbanukaofficial/claude-code/blob/a371abbe75ffa0d0a3c92290e2bbf56a7ef54367/README.md#L19-L19) (`clm_10df1ba7a42e3cc9bf3eaec7b182b0393805577b71ab43ea26392851c4aae5d2`)

