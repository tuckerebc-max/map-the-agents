# polymathwizard/bhil-ai-first-development-toolkit -- full detail

[Back to orientation](bhil-ai-first-development-toolkit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/8ad4b540/adc303d7/161f8e5311bdfc88bc650dcf800948437aecb93b/dffb30bc95fe376f.json](../../../wiki/dossiers/8ad4b540/adc303d7/161f8e5311bdfc88bc650dcf800948437aecb93b/dffb30bc95fe376f.json)

## specifications (3 claim(s))

- [observation/documented] The toolkit prescribes a traceable artifact chain — PRD (what), SPEC (how), ADR (why), TASK (steps) — flowing through code, review, deploy, and closed by a sprint retrospective. -- evidence: [README.md#L17-L21](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L17-L21), [01-methodology-overview.md#L60-L62](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/01-methodology-overview.md#L60-L62) (`clm_1c90b86d4e8b96db524ccf6dcd9f644b80fcb71a713068a8aa99dca13fd6d17b`)
- [observation/documented] Every artifact carries a traceability ID in YAML frontmatter with defined formats such as PRD-NNN, SPEC-NNN, ADR-NNN, TASK-NNN, S-NN, and PV-NNN. -- evidence: [README.md#L114-L114](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L114-L114), [README.md#L116-L123](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L116-L123) (`clm_5f36c5ea8b6ce0a874be89d00de2a3c9c45d6479e32ba7b4c75b8ea395571645`)
- [observation/documented] Traceability links are asymmetric: children reference parents (e.g., SPECs reference parent PRD-NNN; TASKs reference spec and ADRs), while PRDs reference nothing upstream. -- evidence: [README.md#L125-L129](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L125-L129) (`clm_3c7ce68dbbf6eee3d825392e647d9a80732755843ada1872d762ea421e26cc1d`)

## components (1 claim(s))

- [observation/documented] The repository ships copy-and-fill templates including PRD, SPEC, TASK, sprint plan, and four ADR variants: core MADR-style, model-selection, prompt-strategy, and agent-orchestration. -- evidence: [README.md#L29-L82](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L29-L82) (`clm_7fc09b5b0759d72c0499d8cf22b7d2352a6042e18241b3089ba761325f1831d3`)

## design-choices (1 claim(s))

- [observation/documented] Beyond standard ADRs, the toolkit defines three AI-native ADR categories — model selection, prompt strategy, and agent orchestration — each with its own template. -- evidence: [README.md#L139-L139](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L139-L139), [README.md#L135-L135](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L135-L135), [README.md#L141-L141](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L141-L141), [README.md#L137-L137](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L137-L137) (`clm_27451c3268805d2a8496acaa1f7f12edf909de6bba7c96be5d90dfd8a709318f`)

## workflows (3 claim(s))

- [observation/documented] A sprint is defined as a two-week cycle with four phases: specification (days 1-2), planning (days 3-5), implementation (week 2 days 1-3), and integration/evaluation/deploy/retro (days 4-5). -- evidence: [03-sprint-workflow.md#L13-L18](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L13-L18), [03-sprint-workflow.md#L9-L9](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L9-L9) (`clm_dfe5c310551a8491fba786290eca9de173a77b7e8ec36553d5581f721ae32a9b`)
- [observation/documented] The methodology mandates a test-first gate for AI-generated code: write tests, confirm they fail and commit that state, then implement without modifying test files. -- evidence: [03-sprint-workflow.md#L148-L150](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L148-L150), [03-sprint-workflow.md#L146-L146](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L146-L146) (`clm_12b749dc1f0360ef014f0c64bbc9a34af1029f8baef28c4f52cab1799af67eff`)
- [observation/documented] The init.sh setup script updates CLAUDE.md and AGENTS.md, creates a project ADR registry, initializes the first sprint folder, adds .gitignore entries, and installs pre-commit hooks. -- evidence: [00-getting-started.md#L47-L52](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/00-getting-started.md#L47-L52) (`clm_963c787ab7734db7a8ac55e168c1b2a9805c3d78d97907350bd2021e61dae5a5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Skills in .claude/skills/ are exposed as available slash-commands in Claude Code, and path-scoped rules in .claude/rules/ load when relevant files are opened. -- evidence: [00-getting-started.md#L62-L65](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/00-getting-started.md#L62-L65) (`clm_4949b5e8e914295888f8c48e7d8702fc6ce3eca18815cc1c8d3e26dda8ada960`)

## memory-state (1 claim(s))

- [observation/documented] The methodology assigns RuVector the role of maintaining persistent memory across sessions so agent context does not start cold; RuFlo optionally orchestrates agents across the artifact chain. -- evidence: [00-getting-started.md#L9-L9](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/00-getting-started.md#L9-L9), [README.md#L23-L23](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L23-L23) (`clm_a62a0b97bad6c36191699dc2cdf0c0e2576a5162cbc4d85f869a3020fae4cff5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] For AI-native features, the methodology prescribes running a promptfoo eval suite before merging, with the pass threshold defined in the feature's SPEC acceptance criteria; unmet thresholds mean the task is not done. -- evidence: [03-sprint-workflow.md#L215-L215](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L215-L215), [03-sprint-workflow.md#L210-L213](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/03-sprint-workflow.md#L210-L213) (`clm_c5698cc0922bb2b43e84506d7ff25c6d2666d1f57189c5abd5f82b9172ca83c7`)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites listed are Claude Code (installed via npm), Node.js 18+, configured Git, a GitHub account, and optionally RuFlo for multi-agent orchestration. -- evidence: [00-getting-started.md#L17-L21](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/00-getting-started.md#L17-L21) (`clm_593672f44c90e85d98355683a3e2fc7479392707d952363053aa7e9dcbbf2c30`)
- [observation/documented] The toolkit is released under the MIT License, with copyright attributed to BarryHurd.com. -- evidence: [README.md#L163-L163](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L163-L163), [README.md#L161-L161](https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit/blob/161f8e5311bdfc88bc650dcf800948437aecb93b/README.md#L161-L161) (`clm_c4b1ff73576888c48feeb92f86ad5c0a074f1abb8d16c1b66019a397cc770dcf`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

