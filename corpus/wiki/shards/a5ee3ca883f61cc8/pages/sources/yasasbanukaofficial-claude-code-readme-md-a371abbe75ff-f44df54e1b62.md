---
access: public
aliases: []
claim_ids:
- clm_09411e6dba7d6f2b5511883328dcad9c45b93b4229027c4c1020ca08a3823d83
- clm_10df1ba7a42e3cc9bf3eaec7b182b0393805577b71ab43ea26392851c4aae5d2
- clm_6bcdb1b99c50a0ac0a77065c0d2fcc3e21b2806696b0103802a872f8b4843421
- clm_8317ce599d9d69d4b9ee99d5b07c4d272996bab64ca4d3f94667edbf3898c91a
- clm_87aac1aa8e852b35465ea4044ceb7f45dc817c4930574086a2e1b0c743dd1319
- clm_8c0dc3c3ec8d05b04b1c90c629710af3cad0021837d700308bfb7c09a329ac4b
- clm_a1bb46c5bd482585c3e644789b267e0125562ae3184f2b9c035314761ac1856e
- clm_a4b889356da5f2ed2337fdfc09d37bf9aed296f1d42969210ff994ca6213f8cd
- clm_a4cb666a7415aeaf02c72fe763201c8d852956e46be69f0e3b79537639e45eb1
- clm_c9e0041c94e7847a5c5a975448b86e356244df56a642cc888b2252ae2010db3c
- clm_e97b4284efb870561d375cdfbc05624473d889f7fe3aa0507dfd88296ffce8d7
- clm_f4911b719dde4be77d7c5680e0564632e61d9ad2d1dabd3f169bbd5ac2ce1e8a
maturity: draft
page_id: pg_4e1963e4a3c65184a4f5f44df54e1b62
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e6e8d43384d459649ddd8f4813015d24
title: yasasbanukaofficial/claude-code/README.md @ a371abbe75ff
updated_at: '2026-09-14T04:32:29Z'
---

# yasasbanukaofficial/claude-code/README.md @ a371abbe75ff

<!-- rcw:begin owner=source:src_e6e8d43384d459649ddd8f4813015d24 block=evidence -->
- KAIROS is described as an always-on proactive assistant watching logs, and ULTRAPLAN offloads complex tasks to a remote Opus 4.6 session for up to 30 minutes of planning. [@claim:clm_09411e6dba7d6f2b5511883328dcad9c45b93b4229027c4c1020ca08a3823d83]
- The repo is a backup and breakdown of Claude Code source code that was exposed on npm via a bundled sourcemap file, credited to a discovery shared on Twitter/X. [@claim:clm_10df1ba7a42e3cc9bf3eaec7b182b0393805577b71ab43ea26392851c4aae5d2]
- The README states the author did not leak the files and only documents access to the codebase for research purposes, with all code remaining proprietary to Anthropic PBC. [@claim:clm_6bcdb1b99c50a0ac0a77065c0d2fcc3e21b2806696b0103802a872f8b4843421]
- An 'Undercover Mode' utility is described that blocks internal model codenames and hides that the user is an AI, apparently intended for Anthropic employees contributing to public repos. [@claim:clm_8317ce599d9d69d4b9ee99d5b07c4d272996bab64ca4d3f94667edbf3898c91a]
- Repository development practice: the README instructs cloning the repo, running npm install, building with npm run build, and running the CLI via node dist/main.js. [@claim:clm_87aac1aa8e852b35465ea4044ceb7f45dc817c4930574086a2e1b0c743dd1319]
- The repo ships an MCP server command (claude mcp add code-explorer with claude-code-explorer-mcp) intended to let users explore the source using Claude. [@claim:clm_8c0dc3c3ec8d05b04b1c90c629710af3cad0021837d700308bfb7c09a329ac4b]
- An autoDream background service is described that reads MEMORY.md, gathers signals from daily logs, consolidates durable memory files, and prunes context. [@claim:clm_a1bb46c5bd482585c3e644789b267e0125562ae3184f2b9c035314761ac1856e]
- A Tamagotchi-style companion system is described under src/buddy/, using a Mulberry32 PRNG seeded from userId, 18 species tiers, and stats such as DEBUGGING, CHAOS, and SNARK. [@claim:clm_a4b889356da5f2ed2337fdfc09d37bf9aed296f1d42969210ff994ca6213f8cd]
- The README lists Bun runtime as highly recommended (or Node.js v18+) and globally installed TypeScript as prerequisites for the mirrored code. [@claim:clm_a4cb666a7415aeaf02c72fe763201c8d852956e46be69f0e3b79537639e45eb1]
- Claude Code is described as a large CLI with a 785KB main.tsx entry point using a React/Ink terminal renderer, 40+ tools, and multi-agent orchestration. [@claim:clm_c9e0041c94e7847a5c5a975448b86e356244df56a642cc888b2252ae2010db3c]
- The described source layout includes main.tsx as CLI entrypoint, QueryEngine.ts for core LLM logic, a tools directory, services, a coordinator for swarm orchestration, a bridge for IDE integration, and a buddy directory. [@claim:clm_e97b4284efb870561d375cdfbc05624473d889f7fe3aa0507dfd88296ffce8d7]
- The leak mechanism appears to be that source maps embed original source under sourcesContent, and the package reportedly shipped .map files because npmignore/build settings omitted them. [@claim:clm_f4911b719dde4be77d7c5680e0564632e61d9ad2d1dabd3f169bbd5ac2ce1e8a]
<!-- rcw:end owner=source:src_e6e8d43384d459649ddd8f4813015d24 block=evidence -->

## Researcher notes

