# snarktank/ralph

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6c53cb0b831e @ 5018f9fc18d59882

## Summary (orientation draft, not independently verified)

Ralph is a bash-loop tool that repeatedly spawns fresh Amp or Claude Code instances to implement PRD user stories, persisting state only via git history, progress.txt, and prd.json. Evidence is README documentation; contributor-instruction claims were dropped per correction guidance.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Ralph runs AI coding tools (Amp or Claude Code) repeatedly until all PRD items are complete; each iteration is a fresh instance with clean context. -- evidence: [README.md#L5-L5](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] Key files include ralph.sh (the bash loop), prompt.md and CLAUDE.md prompt templates, prd.json task list, progress.txt, skills/prd and skills/ralph, and a .claude-plugin manifest. -- evidence: [README.md#L134-L145](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L134-L145)
- design-choices (3 claim(s)):
  - [observation/documented] PRD items are intentionally kept small enough to finish in one context window, since oversized tasks exhaust context and yield poor code. -- evidence: [README.md#L172-L172](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L172-L172)
  - [observation/documented] A recommended Amp auto-handoff setting (context 90) enables automatic handoff when context fills, letting Ralph handle stories larger than one context window. -- evidence: [README.md#L86-L86](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L86-L86), [README.md#L80-L84](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L80-L84)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Two skills are provided: /prd for generating Product Requirements Documents and /ralph for converting PRDs to prd.json, installable via Amp config, the Claude skills directory, or a Claude Code marketplace plugin. -- evidence: [README.md#L58-L60](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L58-L60), [README.md#L68-L70](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L68-L70), [README.md#L64-L66](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L64-L66), [README.md#L48-L52](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L48-L52), [README.md#L42-L46](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L42-L46)
- interfaces (1 claim(s)):
  - [observation/documented] ralph.sh accepts an optional max_iterations argument and a --tool flag selecting amp (the default) or claude; the default iteration count is 10. -- evidence: [README.md#L117-L118](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L117-L118), [README.md#L120-L120](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L120-L120), [README.md#L114-L114](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L114-L114), [README.md#L13-L17](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L13-L17)
- memory-state (1 claim(s)):
  - [observation/documented] The only memory between iterations is git history, the append-only progress.txt learnings file, and prd.json story status. -- evidence: [README.md#L165-L168](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L165-L168)
- orchestration (3 claim(s)):
  - [observation/documented] Each loop iteration creates a feature branch from the PRD branchName, picks the highest-priority story with passes:false, implements it, runs quality checks, commits, marks it passes:true, and repeats until done or max iterations. -- evidence: [README.md#L122-L130](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L122-L130)
  - [observation/documented] When all stories have passes:true, Ralph outputs <promise>COMPLETE</promise> and the loop exits. -- evidence: [README.md#L207-L207](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L207-L207)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Prerequisites are one installed and authenticated AI coding tool (Amp CLI default or Claude Code), jq, and a git repository for the project. -- evidence: [README.md#L13-L17](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/README.md#L13-L17)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](ralph.detail.md)

Metadata and full claim list: [full detail](ralph.detail.md)
Human notes ([notes](ralph.notes.md), never overwritten by build)

[Back to map index](../../index.md)
