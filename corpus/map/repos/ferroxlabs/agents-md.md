# ferroxlabs/agents-md

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 90c7198cfa97 @ b15adb8e01836996

## Summary (orientation draft, not independently verified)

The repository ships a single MIT-licensed AGENTS.md template of operating instructions for coding agents, installable by hand or via an agent-driven prompt, with symlink guidance for Claude Code and Gemini CLI. The file's internal rules are contributor/agent instructions and are reported under workflows.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository's product is a single drop-in AGENTS.md file of operating instructions intended to be placed at any project's root and read by coding agents, released under the MIT license. -- evidence: [README.md#L119-L119](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L119-L119), [README.md#L7-L7](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L7-L7), [README.md#L5-L5](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The file is deliberately kept tight (about 200 lines per the README, with under 300 suggested as a ceiling) so rules stay loaded, and sections 0-9 are meant to be left untouched by users. -- evidence: [README.md#L83-L83](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L83-L83), [AGENTS.md#L145-L145](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L145-L145), [README.md#L64-L71](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L64-L71)
  - [observation/documented] The template synthesizes Karpathy's four principles on LLM coding failure modes, Boris Cherny's Claude Code workflow with reactive pruning, Anthropic's Claude Code best practices, community anti-sycophancy patterns, and the AGENTS.md standard. -- evidence: [README.md#L109-L113](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L109-L113), [AGENTS.md#L198-L204](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L198-L204)
- workflows (8 claim(s)):
  - [observation/documented] Installation is documented two ways: an agent-driven prompt that fetches the raw file, symlinks CLAUDE.md/GEMINI.md, and fills section 10 from the codebase, or a manual curl download of AGENTS.md. -- evidence: [README.md#L21-L27](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L21-L27), [README.md#L33-L35](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L33-L35)
  - [observation/documented] Repository development practice: the file's non-negotiables instruct agents to skip flattery, disagree with false premises, never fabricate facts, ask when a task has two plausible interpretations, and touch only lines traceable to the request. -- evidence: [AGENTS.md#L20-L24](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L20-L24)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The file targets the AGENTS.md open standard: tools like Codex, Cursor, Aider, Windsurf, Copilot, and Devin read it natively, while Claude Code and Gemini CLI require CLAUDE.md and GEMINI.md symlinks (or copies) pointing to it. -- evidence: [README.md#L39-L39](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L39-L39), [README.md#L37-L37](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L37-L37), [README.md#L101-L101](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L101-L101)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(6 additional claim(s) omitted for length; see [full detail](agents-md.detail.md) for every claim.)

Metadata and full claim list: [full detail](agents-md.detail.md)
Human notes ([notes](agents-md.notes.md), never overwritten by build)

[Back to map index](../../index.md)
