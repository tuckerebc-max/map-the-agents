# aizenvoltprime/damocles

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b8787a5e9b69 @ 87e325b5b99a6e04

## Summary (orientation draft, not independently verified)

Damocles is a VS Code extension AI coding assistant built on the pi agent engine, with a Vue 3 webview chat UI, permission rules, hooks, skills/commands, and SQLite-backed persistent memory. Evidence is mostly README documentation plus a hooks guide; no source code is included in the slices. Evidence coverage: 138 of 273 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture consists of a Node.js extension host running the pi engine, tools, and permissions; a Vue 3 + Tailwind webview chat interface; and a postMessage bridge between them. -- evidence: [README.md#L543-L545](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L543-L545)
- design-choices (2 claim(s)):
  - [observation/documented] Asset precedence is builtin > .damocles > .claude/.codex, with project overriding user within a scope and damocles.assetSourcePrecedence (default claude) breaking ties between compat sources; matching is case-insensitive. -- evidence: [README.md#L189-L189](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L189-L189)
  - [observation/documented] Project-scope commands, skills, and instruction files are gated on VS Code workspace trust so an untrusted repository cannot inject prompts or hooks; user-scope assets remain unaffected. -- evidence: [README.md#L222-L222](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L222-L222), [README.md#L193-L193](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L193-L193)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: build from source by cloning, running npm install, npm run build, and pressing F5 for the Extension Development Host; npm test runs tests, npm run typecheck type-checks, and npm run build && npm run package produces a .vsix. -- evidence: [README.md#L525-L526](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L525-L526), [README.md#L108-L111](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L108-L111), [README.md#L522-L522](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L522-L522), [README.md#L516-L516](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L516-L516), [README.md#L532-L534](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L532-L534), [README.md#L513-L513](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L513-L513)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills load from .damocles/skills, .claude/skills and .codex/skills SKILL.md files (project and user scopes), with YAML frontmatter descriptions and a name: field that can override the directory name. -- evidence: [README.md#L216-L216](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L216-L216)
  - [observation/documented] Skill invocation via slash command is auto-approved without a prompt, while agent-initiated skill use triggers an approval prompt with options to approve once, auto-approve for the session, deny, or redirect with new instructions. -- evidence: [README.md#L201-L203](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L201-L203), [README.md#L207-L207](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L207-L207), [README.md#L209-L212](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L209-L212)
- interfaces (3 claim(s)):
  - [observation/documented] The product is a VS Code extension offering a chat panel in the secondary sidebar or as an editor panel (Ctrl+Shift+U), with both modes supporting independent simultaneous sessions. -- evidence: [README.md#L26-L44](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L26-L44)
  - [observation/documented] Slash commands include built-ins like /clear, /compact, /rewind, /remember, /note, /memories, /context and /usage, plus custom commands loaded from .damocles/commands, .claude/commands and .codex/prompts. -- evidence: [README.md#L175-L185](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L175-L185), [README.md#L187-L187](https://github.com/AizenvoltPrime/damocles/blob/b8787a5e9b69694cd607326dcce721bbf1e04bab/README.md#L187-L187)
- memory-state (3 claim(s)):
More evidence: [full detail](damocles.detail.md)

Metadata and full claim list: [full detail](damocles.detail.md)
Human notes ([notes](damocles.notes.md), never overwritten by build)

[Back to map index](../../index.md)
