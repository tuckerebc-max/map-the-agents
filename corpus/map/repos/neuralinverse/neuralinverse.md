# neuralinverse/neuralinverse

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2d68ded2f2b7 @ 37e53038d42926c0

## Summary (orientation draft, not independently verified)

The snapshot is documentation-only (README, contribution guides, codebase guide, licenses) for NeuralInverse, an AI-native IDE forked from VS Code, describing product features, module layout, and contributor workflows. No source code or eval harness is present in the evidence.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] CE-specific code is organized under src/vs/workbench/contrib/ in modules for AI chat (void/), Power Mode, Agent Manager (neuralInverse/), firmware, and modernisation. -- evidence: [HOW_TO_CONTRIBUTE.md#L17-L20](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/HOW_TO_CONTRIBUTE.md#L17-L20), [README.md#L88-L94](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L88-L94), [NEURALINVERSE_CODEBASE_GUIDE.md#L5-L5](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L5-L5)
  - [observation/documented] voidSettingsService stores all settings including providers, models, and global preferences, and is an implicit dependency of core services; chat modes include normal, gather, and agent. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L79-L85](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L79-L85), [NEURALINVERSE_CODEBASE_GUIDE.md#L77-L77](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L77-L77)
- design-choices (2 claim(s)):
  - [observation/documented] LLM messages are sent from the Electron main process, which the guide says avoids CSP issues with local providers and allows use of node_modules. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L17-L22](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L17-L22), [NEURALINVERSE_CODEBASE_GUIDE.md#L40-L40](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L40-L40)
  - [observation/documented] Apply has two modes: Fast Apply prompts the LLM for Search/Replace blocks for quick edits on large files, while Slow Apply rewrites the whole file; edits render as red/green DiffZones. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L49-L57](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L49-L57), [NEURALINVERSE_CODEBASE_GUIDE.md#L47-L47](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L47-L47), [NEURALINVERSE_CODEBASE_GUIDE.md#L67-L70](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L67-L70)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors build from source with npm install, npm run watch and watchreact watchers, and launch a dev instance via scripts/code.sh or code.bat; Node 20.18.2 is specified via .nvmrc. -- evidence: [HOW_TO_CONTRIBUTE.md#L45-L45](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/HOW_TO_CONTRIBUTE.md#L45-L45), [README.md#L107-L113](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L107-L113)
  - [observation/documented] Repository development practice: PRs should be focused (one fix or feature), pass the build, use the PR template, target main, and avoid non-ASCII characters in TS/JS string literals. -- evidence: [HOW_TO_CONTRIBUTE.md#L118-L123](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/HOW_TO_CONTRIBUTE.md#L118-L123)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The IDE exposes AI chat and inline edit via Ctrl+L/Ctrl+K keybindings, with sidebar chat, inline diffs, autocomplete, and Fast Apply. -- evidence: [README.md#L43-L49](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L43-L49)
  - [observation/documented] Power Mode (Cmd+Alt+P) is an autonomous coding agent with 22+ tools and concurrent sub-agents; Agent Manager (Cmd+Alt+A) handles model management and orchestration. -- evidence: [README.md#L43-L49](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L43-L49)
- memory-state (1 claim(s)):
  - [observation/documented] Code changes are written to a text model identified only by the file's URI via voidModelService, without requiring the file to be loaded or saved. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L74-L74](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L74-L74)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](neuralinverse.detail.md)

Metadata and full claim list: [full detail](neuralinverse.detail.md)
Human notes ([notes](neuralinverse.notes.md), never overwritten by build)

[Back to map index](../../index.md)
