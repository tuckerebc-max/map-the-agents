# gabrielchasukjin/cloi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1da62db7aa3a @ 797f9eefb3e6fe1a

## Summary (orientation draft, not independently verified)

Cloi is a local-first terminal coding agent backed by Ollama, with hardware-based model selection, escalation, answer verification, named result storage, a Python scratchpad, and permission/secret guardrails. Evidence is documentation-only (README and docs), so claims are documented rather than code-inspected. Evidence coverage: 140 of 189 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Cloi is described as a local-first terminal coding agent that reads, searches, writes and edits files and runs commands in the workspace, with everything running locally and no API key. -- evidence: [README.md#L3-L3](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L3-L3), [README.md#L5-L7](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L5-L7)
- components (2 claim(s)):
  - [observation/documented] The architecture includes src/agent modules (loop, prompt, permission, verify, judge), tools (fs-tools, shell, todo, workspace, registry), a SQLite session store, an Ollama provider, and setup/hardware/recommendation utilities. -- evidence: [docs/internals.md#L8-L32](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L8-L32)
  - [observation/documented] A session-long Python interpreter exposes stored results as variables and tools as callable functions; variables, imports and helpers persist across sessions, and the namespace is saved per variable between runs. -- evidence: [docs/internals.md#L356-L362](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L356-L362), [README.md#L99-L101](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L99-L101), [README.md#L90-L91](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L90-L91), [docs/internals.md#L349-L350](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L349-L350)
- design-choices (3 claim(s)):
  - [observation/documented] Setup reads VRAM, RAM and core count and proposes two models: a primary that must fit in VRAM and a fallback that only needs to fit in RAM, stepping down the primary if the prediction was wrong. -- evidence: [README.md#L47-L51](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L47-L51), [docs/models.md#L15-L20](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/models.md#L15-L20), [docs/models.md#L12-L13](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/models.md#L12-L13)
  - [observation/documented] Answers are verified before display: filesystem-settled claims are checked without a model call (line citations, quotes, absence claims), and a model-based judge review runs only after an escalation. -- evidence: [docs/internals.md#L118-L122](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L118-L122), [README.md#L66-L69](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L66-L69), [README.md#L71-L72](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L71-L72), [docs/internals.md#L113-L116](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L113-L116)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: tests are run with npm test; the suite covers 126 tests including tool-name repair, permission gating, credential containment, and regression tests for false positives found in live runs. -- evidence: [docs/internals.md#L472-L474](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L472-L474), [docs/internals.md#L476-L481](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L476-L481)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports interactive sessions, one-shot requests, --continue to resume a session, and cloi setup to re-pick models; in-session slash commands include /model, /tools, /plan, /usage, /sessions, /help. -- evidence: [README.md#L131-L136](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L131-L136), [README.md#L138-L139](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L138-L139)
  - [observation/documented] Configuration lives in ~/.cloi/config.json (overridable via CLOI_DATA_DIR) with settings for model, host, maxIterations, escalationModel, verifyAnswers, compaction, temperature, and autoApprove. -- evidence: [docs/configuration.md#L7-L7](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L7-L7), [docs/configuration.md#L27-L35](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L27-L35), [docs/configuration.md#L9-L12](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L9-L12), [docs/configuration.md#L19-L20](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L19-L20), [docs/configuration.md#L22-L25](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L22-L25), [docs/configuration.md#L14-L17](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L14-L17)
- memory-state (3 claim(s)):
  - [observation/documented] Conversation state is persisted in SQLite and rebuilt from the database on every loop iteration, so interrupted turns leave a coherent, resumable session. -- evidence: [docs/internals.md#L8-L32](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L8-L32), [docs/internals.md#L46-L49](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L46-L49)
More evidence: [full detail](cloi.detail.md)

Metadata and full claim list: [full detail](cloi.detail.md)
Human notes ([notes](cloi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
