# snarktank/ralph -- full detail

[Back to orientation](ralph.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/snarktank/ralph/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/5018f9fc18d59882.json](../../../wiki/dossiers/snarktank/ralph/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/5018f9fc18d59882.json)

## specifications (1 claim(s))

- [observation/documented] Ralph runs AI coding tools (Amp or Claude Code) repeatedly until all PRD items are complete; each iteration is a fresh instance with clean context. -- evidence: [README.md#L5-L5](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L5-L5) (`clm_9a7896f2edf35bc19945f1729418be774036f20f093564a57f0b34383ae9bdd7`)

## components (1 claim(s))

- [observation/documented] Key files include ralph.sh (the bash loop), prompt.md and CLAUDE.md prompt templates, prd.json task list, progress.txt, skills/prd and skills/ralph, and a .claude-plugin manifest. -- evidence: [README.md#L134-L145](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L134-L145) (`clm_4412202e98be0eb0f48be3c6cf6b8e5c85a79d03521ae77972a26e0ec3eb67d1`)

## design-choices (3 claim(s))

- [observation/documented] PRD items are intentionally kept small enough to finish in one context window, since oversized tasks exhaust context and yield poor code. -- evidence: [README.md#L172-L172](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L172-L172) (`clm_b0970ae2289f347e3b740d6edfbef7738e057d1b2e0e8e5d8e9ae6be44cc5ae6`)
- [observation/documented] A recommended Amp auto-handoff setting (context 90) enables automatic handoff when context fills, letting Ralph handle stories larger than one context window. -- evidence: [README.md#L86-L86](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L86-L86), [README.md#L80-L84](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L80-L84) (`clm_47b5afd707d9cc986839d139be55dbfbcc73b24ae3b0cb0f0a93e083f74c254c`)
- [observation/documented] Frontend stories' acceptance criteria must include browser verification via the dev-browser skill, which Ralph uses to navigate and confirm UI changes. -- evidence: [README.md#L203-L203](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L203-L203) (`clm_57f12a42be43f6b3e1b258a72291259eaf9ad55766b65f8c964fa999e4191098`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Two skills are provided: /prd for generating Product Requirements Documents and /ralph for converting PRDs to prd.json, installable via Amp config, the Claude skills directory, or a Claude Code marketplace plugin. -- evidence: [README.md#L58-L60](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L58-L60), [README.md#L68-L70](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L68-L70), [README.md#L64-L66](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L64-L66), [README.md#L48-L52](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L48-L52), [README.md#L42-L46](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L42-L46) (`clm_31d1ad6ebb0ad4e089bf2979226464e68b3a5f0d67edf8f811e74a9951c6193d`)

## interfaces (1 claim(s))

- [observation/documented] ralph.sh accepts an optional max_iterations argument and a --tool flag selecting amp (the default) or claude; the default iteration count is 10. -- evidence: [README.md#L117-L118](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L117-L118), [README.md#L120-L120](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L120-L120), [README.md#L114-L114](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L114-L114), [README.md#L13-L17](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L13-L17) (`clm_d9a0a1184b1fdee9bb9995fea7c7bef8b13ba613e9fac7b34c39458be7537488`)

## memory-state (1 claim(s))

- [observation/documented] The only memory between iterations is git history, the append-only progress.txt learnings file, and prd.json story status. -- evidence: [README.md#L165-L168](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L165-L168) (`clm_924725008f8e5bf781aa2703f913c55af8ca337ae3a13f763bc365c534cab01e`)

## orchestration (3 claim(s))

- [observation/documented] Each loop iteration creates a feature branch from the PRD branchName, picks the highest-priority story with passes:false, implements it, runs quality checks, commits, marks it passes:true, and repeats until done or max iterations. -- evidence: [README.md#L122-L130](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L122-L130) (`clm_54a1a0f5098ee00a2e3990252799d74d4bb67491bccd573b68936b6dec47101c`)
- [observation/documented] When all stories have passes:true, Ralph outputs <promise>COMPLETE</promise> and the loop exits. -- evidence: [README.md#L207-L207](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L207-L207) (`clm_4456223d7175bb2ae9491440dee1bedabe78226ebae884a9882ebb095a7911b4`)
- [observation/documented] Ralph automatically archives previous runs when a new feature with a different branchName starts, saving them under archive/YYYY-MM-DD-feature-name/. -- evidence: [README.md#L233-L233](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L233-L233) (`clm_f7d31f86b5f5fdba0b3543e9ddc5bffb9fc17e7209f6d85eed4a9deed025747b`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are one installed and authenticated AI coding tool (Amp CLI default or Claude Code), jq, and a git repository for the project. -- evidence: [README.md#L13-L17](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L13-L17) (`clm_8f58b84e7fbc4706fa22097cb989b448fad63a8691342c2d6f7c16125910eb4c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

