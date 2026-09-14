# hofstadter-io/hof

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 52feda8ce076 @ 671461f5d33a01fd

## Summary (orientation draft, not independently verified)

Selected evidence records: hof exposes two interfaces: a CLI suited to scripting and automation, and a TUI for exploring and designing, the latter with a built-in help system. The CLI offers main commands including chat, create, datamodel, def, eval, export, flow, fmt, gen, mod, tui, and vet, plus additional commands like update, version, completion, and feedback.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is organized around a Go CLI entrypoint (cmd/hof), core logic in lib/, a CUE-based task engine in flow/, docs site source, and CI scripts. -- evidence: [README.md#L75-L80](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L75-L80)
- design-choices (2 claim(s)):
  - [observation/documented] hof is built on CUE, which the project treats as the language for schemas, configuration, and declarative sources of truth, powering both developer experience and implementation. -- evidence: [README.md#L26-L29](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L26-L29)
  - [observation/documented] Core features include technology-agnostic code generation from data plus templates, evolvable data models with checkpoint and diff support, an extensible DAG task engine based on cue/flow, and LLM-assisted chat combined with code generation. -- evidence: [README.md#L13-L22](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L13-L22), [README.md#L7-L11](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L7-L11)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors build the binary with 'make build', run tests with 'make test', and serve docs locally with 'make docs-serve'. -- evidence: [README.md#L92-L94](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L92-L94), [README.md#L86-L88](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L86-L88), [README.md#L98-L100](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L98-L100)
  - [observation/documented] Repository development practice: AGENTS.md instructs contributing agents to run only one build/validate command at a time (go install ./cmd/hof, then hof version) and forbids other hof commands or go test unless the user explicitly instructs it. -- evidence: [AGENTS.md#L65-L65](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L65-L65), [AGENTS.md#L54-L55](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L54-L55), [AGENTS.md#L59-L59](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L59-L59), [AGENTS.md#L62-L63](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L62-L63)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] hof exposes two interfaces: a CLI suited to scripting and automation, and a TUI for exploring and designing, the latter with a built-in help system. -- evidence: [README.md#L120-L120](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L120-L120), [README.md#L122-L123](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L122-L123), [README.md#L178-L180](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L178-L180)
  - [observation/documented] The CLI offers main commands including chat, create, datamodel, def, eval, export, flow, fmt, gen, mod, tui, and vet, plus additional commands like update, version, completion, and feedback. -- evidence: [README.md#L149-L154](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L149-L154), [README.md#L135-L147](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L135-L147)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
More evidence: [full detail](hof.detail.md)

Metadata and full claim list: [full detail](hof.detail.md)
Human notes ([notes](hof.notes.md), never overwritten by build)

[Back to map index](../../index.md)
