# marsz42/awel

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3687fea3fa73 @ 4b213dd8f93324f0

## Summary (orientation draft, not independently verified)

Awel is an AI development overlay for Next.js: a proxy in front of the dev server injects a chat dashboard through which an AI agent reads, writes, and edits project files. Evidence is README documentation (English and Chinese) plus contributor-oriented CLAUDE.md notes; no source code slices are present.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] HMR/WebSocket traffic is proxied through transparently and paused while the agent edits files, to prevent hot-reload interference. -- evidence: [README.md#L60-L60](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L60-L60)
  - [observation/documented] The dashboard offers an element inspector for attaching selected DOM elements as prompt context, a screenshot annotator, image attachments, plan approval, per-session undo of agent file changes, and diff review before accepting changes. -- evidence: [README.md#L104-L104](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L104-L104), [README.md#L112-L120](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L112-L120), [README.md#L108-L108](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L108-L108)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's Development section lists npm scripts for building everything, CLI watch mode, running tests, and test watch mode; contributor notes specify Vitest for tests and separate build pipelines (tsc for CLI, Vite for dashboard, esbuild for host). -- evidence: [CLAUDE.md#L292-L297](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/CLAUDE.md#L292-L297), [CLAUDE.md#L31-L38](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/CLAUDE.md#L31-L38), [README.md#L133-L137](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L133-L137), [README.md#L124-L129](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L124-L129)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Awel runs a proxy on port 3001 in front of the Next.js dev server on port 3000, intercepts HTML responses to inject a script, and opens a full-screen chat dashboard in an iframe from a floating Shadow DOM button. -- evidence: [README.md#L55-L58](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L55-L58), [README.md#L34-L34](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L34-L34), [README.md#L51-L53](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L51-L53), [README.md#L5-L5](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L5-L5)
  - [observation/documented] The CLI exposes two commands: `awel create` to scaffold a new Next.js project in creation mode, and `awel dev` with options `-p/--port` (default 3000), `-v/--verbose` for LLM stream events on stderr, and `--no-open`. -- evidence: [README.md#L23-L23](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L23-L23), [README.md#L42-L45](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L42-L45), [README.md#L38-L40](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L38-L40)
- memory-state (1 claim(s)):
  - [observation/documented] The agent includes a Memory tool to store and retrieve persistent project knowledge, and the product advertises saving and recalling project-specific knowledge across sessions. -- evidence: [README.md#L92-L100](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L92-L100), [README.md#L112-L120](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L112-L120)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The agent has tools for file read/write/edit, shell commands, code search, web search/fetch, plan proposal, user questions, dev-server restart, todo tracking, and persistent memory, with file edits and shell commands subject to optional user confirmation. -- evidence: [README.md#L92-L100](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L92-L100)
More evidence: [full detail](awel.detail.md)

Metadata and full claim list: [full detail](awel.detail.md)
Human notes ([notes](awel.notes.md), never overwritten by build)

[Back to map index](../../index.md)
