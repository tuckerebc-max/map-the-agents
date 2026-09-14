# amersarhan/darce-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1b90c379ab74 @ edcbe6956310fb55

## Summary (orientation draft, not independently verified)

The evidence is README-only documentation for darce-cli, a terminal-based AI coding agent distributed via npm, describing its tools, slash commands, model routing, pricing tiers, and contributor setup. No source code is included in the snapshot.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Darce includes smart routing that automatically picks a model per task, and users can override routing with rules in a ~/.darcerc config file mapping conditions like large-context or complex-reasoning to specific models. -- evidence: [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101), [README.md#L152-L165](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L152-L165)
  - [observation/documented] The tool is git-aware, tracking branch, changes, and recent commits, and supports session resume via 'darce --resume' plus context compaction for long conversations. -- evidence: [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install, use 'npm run dev' to run from source, run tests with 'npx tsx test.ts' (106 tests), and build with 'npm run build'. -- evidence: [README.md#L169-L176](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L169-L176)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes slash commands including /help, /model, /clear, /cost, /compact, and /quit, with short aliases such as /m, /c, and /q. -- evidence: [README.md#L139-L146](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L139-L146)
  - [observation/documented] The agent provides seven tools: Read, Write, Edit, Bash, Glob, Grep, and WebFetch, plus keyboard shortcuts like Ctrl+M for model switching and triple-quote multi-line input. -- evidence: [README.md#L86-L92](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L86-L92), [README.md#L94-L101](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L94-L101)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Tool access is tier-gated: the free Starter plan limits users to 3 tools (Read, Grep, Glob) while paid tiers unlock all 7 tools, and resume/history is paid-only. -- evidence: [README.md#L121-L128](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L121-L128)
- evaluation (1 claim(s)):
  - [inference/documented] No agent performance benchmarks or eval harness appear in the evidence; the only test-related content is the repository's own test suite instructions, so evaluation capability appears undocumented. -- evidence: [README.md#L169-L176](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L169-L176)
- dependencies (1 claim(s)):
  - [observation/documented] The product routes to multiple external models, listing qwen3-coder (default), grok-4.1-fast, claude-sonnet-4, gemini-2.5-pro, deepseek-r1, deepseek-chat, and llama-4-maverick. -- evidence: [README.md#L107-L115](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L107-L115)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] Darce is a terminal AI coding agent that reads, writes, and edits code, runs shell commands, and searches codebases, positioning itself against Claude Code, Cursor, and Copilot CLI. -- evidence: [README.md#L10-L14](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L10-L14), [README.md#L50-L60](https://github.com/AmerSarhan/darce-cli/blob/1b90c379ab746da96a1b099e905043895bd013ca/README.md#L50-L60)
More evidence: [full detail](darce-cli.detail.md)

Metadata and full claim list: [full detail](darce-cli.detail.md)
Human notes ([notes](darce-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
