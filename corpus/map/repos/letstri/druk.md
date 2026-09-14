# letstri/druk

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0027143d76ae @ b4006ea39e978a75

## Summary (orientation draft, not independently verified)

Druk is a terminal code editor shipped as a single self-contained binary, built on Solid/OpenTUI, with file tree, tabs, search, git, review notes, markdown/PDF viewing, and a JSON-manifest extension market. Evidence is mostly README/ARCHITECTURE documentation; no agent-eval or runtime-permission material is present. Evidence coverage: 107 of 190 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The app is a Solid application rendered to the terminal by OpenTUI, which supplies layout, text buffer, undo/redo, mouse hit-testing and the tree-sitter worker; the repo is the wiring around it. -- evidence: [ARCHITECTURE.md#L3-L6](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L3-L6)
- design-choices (2 claim(s)):
  - [observation/documented] Extensions are JSON manifests, never code: installing one executes nothing, and manifests are read at startup with reload available via 'r' in the extensions panel. -- evidence: [README.md#L417-L422](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L417-L422), [ARCHITECTURE.md#L286-L291](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L286-L291)
  - [observation/documented] Settings live in two layers: a global config.json rewritten whole and a per-project .druk/settings.json of overrides that wins after merging. -- evidence: [ARCHITECTURE.md#L373-L380](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L373-L380)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the extension market is a folder in this repo served raw from main, so a merged pull request makes an extension installable immediately; contributing one is a JSON file plus a PR. -- evidence: [ARCHITECTURE.md#L318-L322](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L318-L322), [README.md#L289-L292](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L289-L292), [README.md#L339-L340](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L339-L340)
  - [observation/documented] Repository development practice: a boundary test fails the suite if ui/ or feature folders import from app/, enforcing one-way dependency direction. -- evidence: [ARCHITECTURE.md#L143-L153](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L143-L153)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Druk is a terminal code editor offering a file tree, tabs, search, PDF viewing, git marks, and syntax highlighting for 30+ languages, usable with keyboard and mouse. -- evidence: [README.md#L3-L4](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L3-L4)
  - [observation/documented] The CLI accepts a directory, a file, or a file with line/column (e.g. src/main.ts:42:7); npx and bunx work without installing. -- evidence: [README.md#L58-L64](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L58-L64), [README.md#L66-L66](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L66-L66)
- memory-state (2 claim(s)):
  - [observation/documented] Review notes persist in review.json beside the config, keyed by project, so an external agent can read and append answers while druk is open; answers reference a parent note id. -- evidence: [README.md#L241-L246](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L241-L246), [README.md#L224-L227](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L224-L227)
  - [observation/documented] Druk remembers each project's open tabs, active file and expanded folders and restores them on the next open of that directory. -- evidence: [README.md#L278-L279](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L278-L279)
- orchestration (1 claim(s)):
More evidence: [full detail](druk.detail.md)

Metadata and full claim list: [full detail](druk.detail.md)
Human notes ([notes](druk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
