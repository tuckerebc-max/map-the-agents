# chaterm/chaterm

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1ca378cb7eda @ 64cc986d19eee1ed

## Summary (orientation draft, not independently verified)

Selected evidence records: Chaterm is described as an AI-native terminal for infrastructure and cloud resource management, letting engineers perform tasks like deployment and troubleshooting via natural language. The agent is documented to understand targets, autonomously plan, and perform multi-host problem analysis and root-cause localization, closing the loop on complex processes.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Chaterm is described as an AI-native terminal for infrastructure and cloud resource management, letting engineers perform tasks like deployment and troubleshooting via natural language. -- evidence: [README.md#L51-L51](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L51-L51)
- components (1 claim(s)):
  - [observation/documented] The project structure includes an Electron main process, preload scripts, a Vue.js renderer, scripts, resources, tests, and docs directories. -- evidence: [CONTRIBUTING_zh.md#L72-L82](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L72-L82)
- design-choices (1 claim(s)):
  - [observation/documented] Knowledge retrieval combines vector and keyword search using RRF fusion into a unified ranking, with visible embedding, hybrid search, and reranking stages. -- evidence: [README.md#L100-L100](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L100-L100), [README.md#L98-L98](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L98-L98)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork the repo, branch from main, and submit PRs that require approval from at least one maintainer before merging. -- evidence: [CONTRIBUTING_zh.md#L18-L23](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L18-L23)
  - [observation/documented] Repository development practice: conventional commit message formats (feat, fix, docs, refactor, test) are required, with ESLint, Prettier, and TypeScript recommended for code style. -- evidence: [CONTRIBUTING_zh.md#L88-L90](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L88-L90), [CONTRIBUTING_zh.md#L109-L115](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L109-L115), [CONTRIBUTING_zh.md#L107-L107](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/CONTRIBUTING_zh.md#L107-L107)
- skills-patterns (1 claim(s)):
  - [observation/documented] Agent Skills encapsulate complex maintenance procedures into reusable AI skills for structured, reliable automated execution. -- evidence: [README.md#L104-L104](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L104-L104)
- interfaces (2 claim(s)):
  - [observation/documented] A database workspace supports connecting to MySQL, PostgreSQL, SQLite, and Oracle for schema browsing, queries, DDL inspection, row editing, and database-aware AI assistance. -- evidence: [README.md#L116-L116](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L116-L116)
  - [observation/documented] Settings allow configuring per-model context window and maximum output tokens, used for both context management and API requests. -- evidence: [README.md#L120-L120](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L120-L120)
- memory-state (1 claim(s)):
  - [observation/documented] The product claims long-term memory and team knowledge bases from which it learns team knowledge and user habits. -- evidence: [README.md#L55-L55](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L55-L55)
- orchestration (1 claim(s)):
  - [observation/documented] The agent is documented to understand targets, autonomously plan, and perform multi-host problem analysis and root-cause localization, closing the loop on complex processes. -- evidence: [README.md#L80-L80](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L80-L80)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] New retrieval configurations default to Qwen-Plus in the China edition and Gemini 2.5 Flash in the global edition for reranking. -- evidence: [README.md#L100-L100](https://github.com/chaterm/Chaterm/blob/1ca378cb7eda1371269034d01d9556f911a1de58/README.md#L100-L100)
More evidence: [full detail](chaterm.detail.md)

Metadata and full claim list: [full detail](chaterm.detail.md)
Human notes ([notes](chaterm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
