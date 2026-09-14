# larens94/codedna

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b3fe577b47c9 @ 2fbd854a2942e463

## Summary (orientation draft, not independently verified)

Selected evidence records: The product exposes a CLI with commands including init, update, refresh, check, verify, impact, doctor, manifest, mode, install, and wiki bootstrap/sync, all of which auto-detect languages. A Claude Code plugin exposes slash commands (/codedna:init, /codedna:check, /codedna:manifest, /codedna:impact) as an alternative to the CLI for Claude Code users.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] codedna install creates a .codedna directory, installs a Git pre-commit gate, and adds the selected agent's instruction file while preserving existing instruction files and hooks. -- evidence: [README.md#L73-L73](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L73-L73)
  - [observation/documented] An optional post-commit wiki-sync hook regenerates docs/codedna-wiki.md after each commit; it is non-blocking (failures silenced) and never overwrites an existing hook, looking for a CodeDNA marker instead. -- evidence: [README.md#L157-L157](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L157-L157), [README.md#L147-L147](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L147-L147)
- design-choices (2 claim(s)):
  - [observation/documented] The protocol embeds structured header fields in source files: exports, used_by (importers, with [cascade] markers), related (semantic links without imports), rules, wiki pointers, and agent messages with model and date. -- evidence: [README.md#L228-L228](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L228-L228), [README.md#L224-L224](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L224-L224), [README.md#L226-L226](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L226-L226), [README.md#L198-L213](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L198-L213), [README.md#L220-L220](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L220-L220), [README.md#L222-L222](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L222-L222)
  - [observation/documented] Header comment syntax adapts to the language: PHP/TS/Go use //, Python uses docstrings, Ruby uses #, and Blade uses {{-- --}}. -- evidence: [README.md#L171-L173](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L171-L173), [README.md#L113-L114](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L113-L114)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes a CLI with commands including init, update, refresh, check, verify, impact, doctor, manifest, mode, install, and wiki bootstrap/sync, all of which auto-detect languages. -- evidence: [README.md#L127-L127](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L127-L127), [README.md#L129-L143](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L129-L143)
  - [observation/documented] A Claude Code plugin exposes slash commands (/codedna:init, /codedna:check, /codedna:manifest, /codedna:impact) as an alternative to the CLI for Claude Code users. -- evidence: [README.md#L99-L99](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L99-L99), [README.md#L118-L118](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L118-L118), [README.md#L120-L125](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L120-L125)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The docs state these are historical results whose raw run artifacts are not included in the checkout, so CI does not claim to reproduce the numerical advantage; versioned traces and a reproduction command are required first. -- evidence: [docs/benchmark.md#L9-L9](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/docs/benchmark.md#L9-L9), [README.md#L240-L240](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L240-L240)
- dependencies (1 claim(s)):
  - [observation/documented] The CLI is installed via pipx and requires Python 3.11+; non-Python language adapters rely on tree-sitter, while Swift and VB.NET use structural parsers. -- evidence: [README.md#L66-L71](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L66-L71), [README.md#L171-L173](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L171-L173)
- limitations (2 claim(s)):
More evidence: [full detail](codedna.detail.md)

Metadata and full claim list: [full detail](codedna.detail.md)
Human notes ([notes](codedna.notes.md), never overwritten by build)

[Back to map index](../../index.md)
