# aider-ai/aider

Status: distilled - Freshness: stale
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5dc9490bb35f @ 4c420a36be9587f3

## Summary (orientation draft, not independently verified)

Aider is a terminal-based AI pair programming tool that connects to many LLM providers, maps the codebase via a repo map, auto-commits with git, and offers watch-files, voice, and web-chat workflows. Evidence is documentation-only (README and HISTORY release notes); no runtime source code appears in the snapshot. Evidence coverage: 97 of 260 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Aider builds a map of the entire codebase (repo map) to work well in larger projects, with tree-sitter based support for many languages including Fortran, Haskell, Julia, Zig, Kotlin, Scala, OCaml, Dart and MATLAB. -- evidence: [README.md#L51-L52](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L51-L52), [HISTORY.md#L307-L320](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L307-L320), [HISTORY.md#L574-L584](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L574-L584), [HISTORY.md#L439-L447](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L439-L447), [HISTORY.md#L5-L20](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L5-L20)
  - [observation/documented] Aider integrates with git, automatically committing changes with generated commit messages so users can diff, manage and undo AI edits with normal git tools. -- evidence: [README.md#L65-L66](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L65-L66)
- design-choices (2 claim(s)):
  - [observation/documented] Aider supports multiple edit formats per model family, including diff, udiff-simple, patch, editor-diff, editor-whole and editor-diff-fenced, and can auto-select the best format in architect mode. -- evidence: [HISTORY.md#L154-L163](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L154-L163), [HISTORY.md#L180-L186](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L180-L186)
  - [observation/documented] Model-specific behaviors are configurable: thinking-tokens and reasoning-effort settings, temperature disabling for GPT-5 models, and per-model weak/editor model defaults. -- evidence: [HISTORY.md#L39-L41](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L39-L41), [HISTORY.md#L62-L87](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L62-L87), [HISTORY.md#L307-L320](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L307-L320), [HISTORY.md#L285-L297](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L285-L297), [HISTORY.md#L24-L24](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L24-L24)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: release notes state that Aider itself wrote a large share of each release's code (e.g. 88% in v0.86.0 and 92% in v0.82.0), indicating heavy dogfooding of the tool in its own development. -- evidence: [HISTORY.md#L180-L186](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L180-L186), [HISTORY.md#L28-L29](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L28-L29)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Aider is a terminal application for AI pair programming with LLMs, usable to start new projects or work on existing codebases. -- evidence: [README.md#L5-L7](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L5-L7), [README.md#L10-L12](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L10-L12)
  - [observation/documented] The CLI accepts --model and --api-key flags, e.g. aider --model deepseek --api-key deepseek=<key>, and models can be selected via short aliases like sonnet or o3-mini. -- evidence: [README.md#L119-L120](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L119-L120), [README.md#L113-L113](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L113-L113), [README.md#L116-L116](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L116-L116)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The project maintains a public code-editing leaderboard; release notes cite model scores on it (e.g. Claude 3.5 Haiku at 75%) and benchmark statistics include token counts. -- evidence: [README.md#L136-L140](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L136-L140), [HISTORY.md#L118-L150](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L118-L150), [HISTORY.md#L634-L645](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L634-L645)
- dependencies (1 claim(s)):
More evidence: [full detail](aider.detail.md)

Metadata and full claim list: [full detail](aider.detail.md)
Human notes ([notes](aider.notes.md), never overwritten by build)

[Back to map index](../../index.md)
