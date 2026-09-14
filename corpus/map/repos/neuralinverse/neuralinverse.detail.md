# neuralinverse/neuralinverse -- full detail

[Back to orientation](neuralinverse.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/neuralinverse/neuralinverse/2d68ded2f2b7d4ba540855119433be86ed87bd84/37e53038d42926c0.json](../../../wiki/dossiers/neuralinverse/neuralinverse/2d68ded2f2b7d4ba540855119433be86ed87bd84/37e53038d42926c0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] CE-specific code is organized under src/vs/workbench/contrib/ in modules for AI chat (void/), Power Mode, Agent Manager (neuralInverse/), firmware, and modernisation. -- evidence: [HOW_TO_CONTRIBUTE.md#L17-L20](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/HOW_TO_CONTRIBUTE.md#L17-L20), [README.md#L88-L94](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L88-L94), [NEURALINVERSE_CODEBASE_GUIDE.md#L5-L5](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L5-L5) (`clm_77b3f5647a2ab4bd0aaa53a815091dae89240b4e37ccfafdc325e74c3e92244f`)
- [observation/documented] voidSettingsService stores all settings including providers, models, and global preferences, and is an implicit dependency of core services; chat modes include normal, gather, and agent. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L79-L85](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L79-L85), [NEURALINVERSE_CODEBASE_GUIDE.md#L77-L77](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L77-L77) (`clm_f5f5e5080557dcf8eaafc9876e1c021ef7fe57bbfe765dec709a531877b301db`)

## design-choices (2 claim(s))

- [observation/documented] LLM messages are sent from the Electron main process, which the guide says avoids CSP issues with local providers and allows use of node_modules. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L17-L22](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L17-L22), [NEURALINVERSE_CODEBASE_GUIDE.md#L40-L40](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L40-L40) (`clm_b4658a6f8b56d4e4b54e99bb5ba3269473613d12a0c19b50af2133d76c572ac0`)
- [observation/documented] Apply has two modes: Fast Apply prompts the LLM for Search/Replace blocks for quick edits on large files, while Slow Apply rewrites the whole file; edits render as red/green DiffZones. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L49-L57](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L49-L57), [NEURALINVERSE_CODEBASE_GUIDE.md#L47-L47](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L47-L47), [NEURALINVERSE_CODEBASE_GUIDE.md#L67-L70](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L67-L70) (`clm_60ebe396ad28e37aa93ef174f0bba34f73b811a6640bf67dcb65ec9ffea16e7d`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors build from source with npm install, npm run watch and watchreact watchers, and launch a dev instance via scripts/code.sh or code.bat; Node 20.18.2 is specified via .nvmrc. -- evidence: [HOW_TO_CONTRIBUTE.md#L45-L45](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/HOW_TO_CONTRIBUTE.md#L45-L45), [README.md#L107-L113](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L107-L113) (`clm_347c5aae074284cf8093545186ee780273a2de1ad5dcf43f01a262cadfcaa8a8`)
- [observation/documented] Repository development practice: PRs should be focused (one fix or feature), pass the build, use the PR template, target main, and avoid non-ASCII characters in TS/JS string literals. -- evidence: [HOW_TO_CONTRIBUTE.md#L118-L123](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/HOW_TO_CONTRIBUTE.md#L118-L123) (`clm_2fdf816320ad063a2e5f8e55f6ce04941d09f52d36528d14229180c80f87d79f`)
- [observation/documented] Repository development practice: the repo ships a Dev Containers/Codespaces container, with at least 4 cores and 6 GB RAM (8 GB recommended) needed for a full build. -- evidence: [README.md#L98-L98](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L98-L98), [README.md#L100-L101](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L100-L101), [README.md#L103-L103](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L103-L103) (`clm_70d444e2b608a2b5066b3fa2537f14ef1b22c3079dd0db567d1d503eda9fc66b`)
- [observation/documented] Repository development practice: AGENTS.md provides instructions for AI coding agents working with the codebase and points to Copilot instructions for architecture and validation steps. -- evidence: [AGENTS.md#L3-L3](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/AGENTS.md#L3-L3), [AGENTS.md#L5-L5](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/AGENTS.md#L5-L5) (`clm_ef08172e669fbdd2d9882165e697fb6a0b99c53cd2a0d14326518d1a1b104fd0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The IDE exposes AI chat and inline edit via Ctrl+L/Ctrl+K keybindings, with sidebar chat, inline diffs, autocomplete, and Fast Apply. -- evidence: [README.md#L43-L49](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L43-L49) (`clm_1c28f692173bd31c4f2d762a0612d63667ab3464043a61f684d94870b4738fe7`)
- [observation/documented] Power Mode (Cmd+Alt+P) is an autonomous coding agent with 22+ tools and concurrent sub-agents; Agent Manager (Cmd+Alt+A) handles model management and orchestration. -- evidence: [README.md#L43-L49](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L43-L49) (`clm_162a7d2e8c1640cc9d5a19a9d0e17a2f389d1ca9d45a6492822e89fe1e567f27`)
- [observation/documented] Specialized modules include Firmware & Embedded (Cmd+Alt+F) with 357 MCU variants, SVD register maps, 22 fw_* tools, and Legacy Modernisation (Cmd+Alt+M) with a 5-stage pipeline and 61 translation profiles. -- evidence: [README.md#L43-L49](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L43-L49) (`clm_f387c6efa74b31f252a990c48b24ad3573d6dbff336cd769c32181106591030c`)

## memory-state (1 claim(s))

- [observation/documented] Code changes are written to a text model identified only by the file's URI via voidModelService, without requiring the file to be loaded or saved. -- evidence: [NEURALINVERSE_CODEBASE_GUIDE.md#L74-L74](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/NEURALINVERSE_CODEBASE_GUIDE.md#L74-L74) (`clm_716a94ee2df9d2cc27e347a3f74868aa61fd6730ad2735e8c8ad8f5e50a48d48`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The product supports a bring-your-own-LLM model across 20 providers (cloud, local, gateway) with per-feature model selection, and the README states API keys never leave the user's machine. -- evidence: [README.md#L43-L49](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L43-L49), [README.md#L23-L23](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L23-L23) (`clm_61b2875ed31f9b14a511b022de11d8303e93564374c3e7bc9b2569c17bb4c3b2`)
- [observation/documented] The project is built on Microsoft's VS Code (MIT-licensed); the OSS edition's additions are licensed under Apache 2.0, and the commercial NeuralInverse product adds proprietary features. -- evidence: [README.md#L21-L21](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L21-L21), [README.md#L121-L121](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L121-L121), [README.md#L123-L123](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L123-L123), [LICENSE-VS-Code.txt#L1-L2](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/LICENSE-VS-Code.txt#L1-L2) (`clm_01f5e19021dc4290a8fd9a00bbcdeb6d986495a85e991f82c986b34febcd962a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets AI-assisted work on legacy modernization, firmware development, and regulated or safety-critical codebases, positioning itself as an open-source Cursor alternative. -- evidence: [README.md#L21-L21](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L21-L21), [README.md#L23-L23](https://github.com/NeuralInverse/neuralinverse/blob/2d68ded2f2b7d4ba540855119433be86ed87bd84/README.md#L23-L23) (`clm_30cbb58265061dd19205a8e14b540c65b087c7c18f7df3300a53ae1fd6313e79`)

