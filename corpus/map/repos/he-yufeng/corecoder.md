# he-yufeng/corecoder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 069948d180cb @ 3c89ac2ec67501ad

## Summary (orientation draft, not independently verified)

CoreCoder is a minimal, MIT-licensed Python coding-agent engine (~1,171-line engine, 2,398 total lines) published on PyPI, featuring a bounded agent loop, eight built-in tools, consent-gated mutating tools, three-tier context compaction, sessions, plan mode, hooks, and an MCP stdio client. All claims below are product/runtime statements from the README; contributor-instruction claims were omitted per correction. Evidence coverage: 134 of 140 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CoreCoder is a Python 3.10+ coding-agent engine, MIT-licensed and published on PyPI as 'corecoder', described as a ~1,171-line engine within 2,398 total lines of pure Python. -- evidence: [README.md#L5-L5](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L5-L5), [README.md#L11-L16](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L11-L16)
- components (1 claim(s)):
  - [observation/documented] The package layout includes agent.py (main loop, 213 lines), llm.py (streaming client, retry, cost, 267 lines), context.py (three-tier compaction), session.py, permissions.py, hooks.py, mcp.py, cli.py, config.py, and a tools/ directory with bash, edit, grep, glob, read, write, todo, and sub-agent tools. -- evidence: [README.md#L88-L112](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L88-L112)
- design-choices (1 claim(s)):
  - [observation/documented] edit_file uses unique-match search-and-replace rather than line numbers: no match returns the file start for re-anchoring, multiple matches require more context, and success returns a diff. -- evidence: [README.md#L139-L139](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L139-L139)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The product ships a CLI with an interactive REPL and a one-shot mode ('corecoder -p "..."' that exits when done), plus REPL slash commands such as /model, /compact, /tokens, /diff, /undo, /plan, /save, and /sessions. -- evidence: [README.md#L189-L198](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L189-L198), [README.md#L79-L82](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L79-L82)
  - [observation/documented] The package can be imported as a library: the top level exports Agent, LLM, and Config, and an example constructs an LLM with model, api_key, and base_url and calls Agent(llm=llm).chat(...). -- evidence: [README.md#L172-L174](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L172-L174), [README.md#L164-L167](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L164-L167)
- memory-state (2 claim(s)):
  - [observation/documented] Context is compacted in three tiers: at 50% full it trims over-long tool outputs mechanically, at 70% the model summarizes older turns while keeping recent ones verbatim, and at 90% it compresses everything to its tightest form. -- evidence: [README.md#L141-L141](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L141-L141)
  - [observation/documented] Sessions can be saved and listed under ~/.corecoder/sessions; session IDs are sanitized to safe filename characters so a malicious session name cannot traverse out of the directory. -- evidence: [README.md#L189-L198](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L189-L198), [README.md#L200-L200](https://github.com/he-yufeng/CoreCoder/blob/069948d180cb0ceb1a6d7aafeb0e141c166a009d/README.md#L200-L200)
- orchestration (2 claim(s)):
More evidence: [full detail](corecoder.detail.md)

Metadata and full claim list: [full detail](corecoder.detail.md)
Human notes ([notes](corecoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
