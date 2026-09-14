# vincentkoc/tokenjuice

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 43a621ab06ef @ b841247bdb2e28e8

## Summary (orientation draft, not independently verified)

tokenjuice is a documented CLI that deterministically compacts terminal command output for agent workflows via rule-driven reducers, exposing reduce/wrap/reduce-json surfaces, install/uninstall/doctor commands for many agent hosts, and npm/pnpm/yarn/Homebrew distribution; several integrations are documented as beta and guidance-only.

## Source coverage

Source coverage (partial): 6 of 103 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] tokenjuice is described as a deterministic output compactor for terminal-heavy agent workflows: it observes command output after execution and returns a smaller payload built from rule-driven reducers instead of the full terminal text. -- evidence: [README.md#L9-L9](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L9-L9)
- components (1 claim(s)):
  - [observation/documented] The reduction engine is rule-driven: built-in JSON rules live in src/rules, user overrides in ~/.config/tokenjuice/rules, and project overrides in .tokenjuice/rules, with later layers overriding earlier ones by rule id. -- evidence: [README.md#L192-L192](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L192-L192)
- design-choices (2 claim(s)):
  - [observation/documented] The design keeps command semantics untouched, exposes raw output only via explicit --raw/--full or opt-in artifact storage, keeps rules as inspectable JSON, and keeps host integrations as thin wrappers around one shared core reducer. -- evidence: [README.md#L11-L11](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L11-L11), [README.md#L9-L9](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L9-L9)
  - [observation/documented] Host adapters apply a narrow safe-inventory policy: exact file-content reads stay raw, standalone repository inventory commands can be compacted, and unsafe mixed command sequences stay raw. -- evidence: [README.md#L192-L192](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L192-L192)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: Homebrew publication is owned by the Tokenjuice workflow in the canonical vincentkoc/homebrew-tap repository, and release maintainers dispatch it manually with the published tag until GitHub App automation lands. -- evidence: [README.md#L139-L141](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L139-L141)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI has three surfaces: `reduce` compacts existing text, `wrap` runs a command and compacts its observed output, and `reduce-json` provides a stable machine protocol for host adapters. -- evidence: [README.md#L190-L190](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L190-L190)
  - [observation/documented] `reduce-json` reads JSON from stdin or a file and always writes JSON to stdout; the documented payload includes fields such as toolName, command, argv, combinedText, and exitCode. -- evidence: [README.md#L218-L226](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L218-L226), [README.md#L214-L214](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L214-L214)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] tokenjuice is distributed via npm (`npm install -g tokenjuice`), pnpm, yarn global, and a Homebrew tap (`brew tap vincentkoc/tap; brew install tokenjuice`). -- evidence: [README.md#L133-L133](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L133-L133), [README.md#L131-L131](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L131-L131), [README.md#L135-L137](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L135-L137), [README.md#L128-L129](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L128-L129)
- limitations (2 claim(s)):
More evidence: [full detail](tokenjuice.detail.md)

Metadata and full claim list: [full detail](tokenjuice.detail.md)
Human notes ([notes](tokenjuice.notes.md), never overwritten by build)

[Back to map index](../../index.md)
