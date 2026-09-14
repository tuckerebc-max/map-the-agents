# rizwan3d/stemcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dfe4dd789988 @ 7835cc5cd29fd935

## Summary (orientation draft, not independently verified)

StemCode is a local AI coding agent distributed as a desktop app, `stemcode` CLI, editor extensions, and an ACP-compatible server, with provider onboarding, tracked file edits, permission/sandbox controls, and versionable `.stemcode/` workspace files. Evidence is documentation-only; no runtime code is shown in these slices. Evidence coverage: 138 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Built-in tracked edit tools include `file_write`, `apply_patch`, `insert_content`, and `search_and_replace`, which record before/after state and participate in `/undo`, `/redo`, and edit summaries. -- evidence: [docs/documentation.md#L412-L412](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L412-L412), [docs/documentation.md#L403-L403](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L403-L403), [docs/documentation.md#L407-L410](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L407-L410), [docs/documentation.md#L405-L405](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L405-L405)
- design-choices (2 claim(s)):
  - [observation/documented] Budget controls are disabled by default and activate only via `/budget local`, `/budget cloud`, or an existing `.stemcode/budget-controls.*.json` file; while disabled, no usage is recorded and provider requests are never blocked. -- evidence: [docs/documentation.md#L212-L212](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L212-L212)
  - [observation/documented] Subagents run delegated tasks with independent contexts to keep the main conversation focused, and interactive user questions support clarification, multiple-choice, multi-select, and free-form input. -- evidence: [README.md#L81-L90](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L81-L90)
- workflows (1 claim(s)):
  - [observation/documented] Release assets publish SHA256SUMS and GitHub artifact attestations; the release pipeline verifies each checksum before publishing, and `gh attestation verify` is documented for provenance checks. -- evidence: [docs/documentation.md#L53-L53](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L53-L53), [README.md#L119-L119](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L119-L119)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] StemCode ships as a desktop app, a `stemcode` terminal command, VS Code and Visual Studio extensions, and an ACP-compatible editor server. -- evidence: [docs/documentation.md#L3-L3](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L3-L3)
  - [observation/documented] The CLI supports options including `--acp`, `--stdin`, `--json`, `-p/--prompt`, `--sandbox-mode`, `--session`, `--profile`, `--thinking`, and `--doctor`. -- evidence: [docs/documentation.md#L327-L345](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L327-L345)
- memory-state (2 claim(s)):
  - [observation/documented] Reusable commands live in `.stemcode/commands` and long-lived project knowledge in `.stemcode/memory`, stored as versionable files users can review and commit. -- evidence: [README.md#L94-L102](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L94-L102), [README.md#L81-L90](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L81-L90)
  - [observation/documented] Desktop sections are saved local conversation threads per workspace that preserve history, active model, profile, thinking mode, plan state, and session state when available. -- evidence: [docs/documentation.md#L183-L183](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L183-L183)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product uses approval prompts, permissions, and profiles to keep actions under human control; `--sandbox-mode` overrides sandbox policy per run with read-only, workspace-write, or danger-full-access values. -- evidence: [docs/documentation.md#L305-L305](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L305-L305), [docs/documentation.md#L327-L345](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L327-L345), [docs/documentation.md#L307-L309](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/docs/documentation.md#L307-L309), [README.md#L81-L90](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L81-L90), [README.md#L54-L55](https://github.com/rizwan3d/StemCode/blob/dfe4dd78998824cb61ad508e07050c4ab884e7e6/README.md#L54-L55)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](stemcode.detail.md)

Metadata and full claim list: [full detail](stemcode.detail.md)
Human notes ([notes](stemcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
