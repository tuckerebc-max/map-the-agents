# looptroop-ai/looptroop -- full detail

[Back to orientation](looptroop.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/looptroop-ai/looptroop/b96f5448251cbe88cd845cd5f262adda02701413/3f7a06becba16b57.json](../../../wiki/dossiers/looptroop-ai/looptroop/b96f5448251cbe88cd845cd5f262adda02701413/3f7a06becba16b57.json)

## specifications (1 claim(s))

- [observation/documented] The product converts a ticket into a PRD with Epics and User Stories plus decomposed implementation steps, stored as a durable artifact for later bead execution. -- evidence: [README.md#L288-L288](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L288-L288) (`clm_2abe9024f33cbd37a0d4709f08deab2d872cdc0379d9b3a20488cef244401e56`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Planning uses an LLM Council where multiple model instances draft plans, score each other with a weighted rubric, vote, and the winner refines and verifies coverage. -- evidence: [README.md#L271-L274](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L271-L274), [README.md#L269-L269](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L269-L269) (`clm_efe666d19a18be7b48c5b911e171840a73774f754f6de7d2d3e4b63a099841df`)
- [observation/documented] Work is decomposed into 'beads' — small independently implementable units with purpose, acceptance criteria, dependencies, target files, and validation steps. -- evidence: [README.md#L303-L303](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L303-L303), [README.md#L296-L301](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L296-L301) (`clm_da2552b636d8ce46930655b064a0ebe0d27af4dc6b37c9759ac5210b5f4f26b9`)
- [observation/documented] Context engineering feeds the agent only minimal per-status context (active bead, target file, test file) instead of full transcripts, to avoid context rot. -- evidence: [README.md#L261-L261](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L261-L261), [README.md#L263-L263](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L263-L263) (`clm_d69ba7a1fdb830462d2306c75adc875e445ffdf868adc47da1a8ef361a24c6ed`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors run `npm install` and `npm run dev` (dev server at localhost:5173), with lint, typecheck, and test scripts available, and a preview mode serving a built bundle. -- evidence: [CONTRIBUTING.md#L35-L37](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L35-L37), [CONTRIBUTING.md#L22-L27](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L22-L27), [CONTRIBUTING.md#L29-L29](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L29-L29), [CONTRIBUTING.md#L45-L49](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L45-L49) (`clm_bf135ab44661ce02e9ae835846df128830396284bf74cd08c16cea3085d647dd`)
- [observation/documented] Repository development practice: pull requests should stay focused, include a summary, rationale, affected workflow areas, tests run, and doc/changelog updates, avoiding unrelated refactors mixed with behavior changes. -- evidence: [CONTRIBUTING.md#L84-L84](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L84-L84), [CONTRIBUTING.md#L92-L92](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L92-L92), [CONTRIBUTING.md#L86-L90](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L86-L90) (`clm_2a1f086ab6ba4d9de067b49fae50613bcfbc7672b9cc59d6a48b8892dd95b901`)
- [observation/documented] Repository development practice: user-visible changes need a CHANGELOG.md entry under `## Unreleased`, and releases changing install paths, commands, flags, or channels must ship website doc updates in the same batch. -- evidence: [CONTRIBUTING.md#L65-L65](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L65-L65), [CONTRIBUTING.md#L63-L63](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L63-L63) (`clm_dd0684002259ee7d4232fa0c7cd1fab19785a1316bad917df98c0b36a374700f`)
- [observation/documented] Repository development practice: bug reports should include reproduction steps, expected behavior, environment details (OS, Node, browser, OpenCode/provider), and logs with secrets removed. -- evidence: [CONTRIBUTING.md#L71-L71](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L71-L71), [CONTRIBUTING.md#L73-L78](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L73-L78) (`clm_081ffea18127ed9d6a49e25f656a93446a08e32c82d4d82217c684c1ed6f941e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A CLI is provided: `looptroop open` starts the app in the background if not running, and `looptroop start` runs the service without a browser. -- evidence: [README.md#L66-L69](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L66-L69), [README.md#L71-L72](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L71-L72) (`clm_69e7b28e17c7c9cd3cb62f6703a31855cef9ef7c7de36dfb200688a37ec3842f`)
- [observation/documented] A local GUI dashboard lets users manage attached repositories, configure implementer and council models, answer interview questions, and track ticket, bead, and execution-log state. -- evidence: [README.md#L35-L36](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L35-L36), [README.md#L41-L42](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L41-L42), [README.md#L26-L27](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L26-L27), [README.md#L32-L33](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L32-L33), [README.md#L29-L30](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L29-L30) (`clm_7d72436a35c6911703a34bc27f83f0608d467a48771687b442901d14fabc07a4`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Execution runs each bead via OpenCode in isolated Git worktrees; on failure a Ralph-style loop logs the trace, resets the worktree, discards the session, and retries fresh until tests pass or limits are hit. -- evidence: [README.md#L315-L315](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L315-L315), [README.md#L311-L313](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L311-L313), [README.md#L309-L309](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L309-L309) (`clm_79e8d01bb7cca8c65d5e547819fb6446a45c092360becd077008e0137c17d57b`)
- [observation/documented] The ticket pipeline flows from codebase discovery through council planning, an approval gate, isolated bead execution, final tests, optional manual QA, and integration/PR review, with QA failures spawning fix beads. -- evidence: [README.md#L239-L251](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L239-L251), [README.md#L253-L253](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L253-L253) (`clm_033d8e8301d3f6e3cb58b3f2a2fb44a08ba5a7b6a8d31fbaf9bc012720704d9c`)

## tools-permissions (1 claim(s))

- [observation/documented] The orchestrator runs OpenCode in dangerously-skip-permissions (YOLO) mode, giving the agent full local execution rights without confirmation prompts; worktrees isolate code but not command execution. -- evidence: [README.md#L342-L342](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L342-L342), [README.md#L344-L344](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L344-L344) (`clm_c4cd945265732b7bb583c43f88fd873886f55696f36a2fd3be84af724c406f56`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The product requires git and authenticated `gh` for the PR step, plus OpenCode with at least one configured model provider; it can start OpenCode if installed but will not install it. -- evidence: [README.md#L219-L225](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L219-L225) (`clm_9ab483c3e8ba2c80a49d5d377d7be79d1c03b30e24c1c0bccbecbcc55fa9273b`)
- [observation/documented] npm/bun/pnpm/Yarn installs need Node 24.18.1+ and git and gh; Homebrew and Scoop ship locked bundles pulling in node@24, git, and gh; Docker images include Node, git, and gh but need an external OpenCode server and a mounted project. -- evidence: [README.md#L206-L210](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L206-L210), [README.md#L117-L118](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L117-L118), [README.md#L128-L132](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L128-L132), [README.md#L143-L145](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L143-L145) (`clm_ccbe11c3fcb65bc48edc088b700798cf7c05da855c8c14a1f98e4125da75fadd`)

## limitations (2 claim(s))

- [observation/documented] In alpha, LLM Councils support 2–10 distinct models including the main implementer, and each project allows only one active ticket in the execution band at a time. -- evidence: [README.md#L402-L402](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L402-L402) (`clm_470e331903969e540e10930219b7073fb196f926befaa3de9e163cf79ff031f0`)
- [observation/documented] The tool is unsuited to urgent quick fixes or trivial tasks due to orchestration overhead and high API token usage from multi-model councils and long retry loops. -- evidence: [README.md#L372-L374](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L372-L374) (`clm_b00207897340c2e07835c964b9903801cb62727d88e67234867ff03b7c4abfa9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

