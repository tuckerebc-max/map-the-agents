# larens94/codedna -- full detail

[Back to orientation](codedna.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/larens94/codedna/b3fe577b47c9589e911224e2092b12cd3afc9e4a/2fbd854a2942e463.json](../../../wiki/dossiers/larens94/codedna/b3fe577b47c9589e911224e2092b12cd3afc9e4a/2fbd854a2942e463.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] codedna install creates a .codedna directory, installs a Git pre-commit gate, and adds the selected agent's instruction file while preserving existing instruction files and hooks. -- evidence: [README.md#L73-L73](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L73-L73) (`clm_6d5dbae82c73711ab5230e04e374ac3d97233304aff66398d5f5a2867f2f7d5a`)
- [observation/documented] An optional post-commit wiki-sync hook regenerates docs/codedna-wiki.md after each commit; it is non-blocking (failures silenced) and never overwrites an existing hook, looking for a CodeDNA marker instead. -- evidence: [README.md#L157-L157](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L157-L157), [README.md#L147-L147](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L147-L147) (`clm_af1c9de4d49fbf9c5348cf643f93d97bc44563485a9aed5a90cb827ff5bf346a`)

## design-choices (2 claim(s))

- [observation/documented] The protocol embeds structured header fields in source files: exports, used_by (importers, with [cascade] markers), related (semantic links without imports), rules, wiki pointers, and agent messages with model and date. -- evidence: [README.md#L228-L228](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L228-L228), [README.md#L224-L224](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L224-L224), [README.md#L226-L226](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L226-L226), [README.md#L198-L213](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L198-L213), [README.md#L220-L220](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L220-L220), [README.md#L222-L222](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L222-L222) (`clm_9d40d4d6f8200614834eb2f1e31aefeb44a2cfa513adc2151e211443db498edc`)
- [observation/documented] Header comment syntax adapts to the language: PHP/TS/Go use //, Python uses docstrings, Ruby uses #, and Blade uses {{-- --}}. -- evidence: [README.md#L171-L173](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L171-L173), [README.md#L113-L114](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L113-L114) (`clm_0c3d655cc8da39df988898bf2762492a5a7366ac063243388f8af8622853351c`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product exposes a CLI with commands including init, update, refresh, check, verify, impact, doctor, manifest, mode, install, and wiki bootstrap/sync, all of which auto-detect languages. -- evidence: [README.md#L127-L127](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L127-L127), [README.md#L129-L143](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L129-L143) (`clm_abd15c7722d159cbbdb92933104dd0a95eea5618208fcabd6db94924474f1f65`)
- [observation/documented] A Claude Code plugin exposes slash commands (/codedna:init, /codedna:check, /codedna:manifest, /codedna:impact) as an alternative to the CLI for Claude Code users. -- evidence: [README.md#L99-L99](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L99-L99), [README.md#L118-L118](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L118-L118), [README.md#L120-L125](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L120-L125) (`clm_c959748cf46bb5ab3531ea2a4dcb6b933f5bc57f113433b0f7e3fb67950407be`)
- [observation/documented] codedna install supports a --tools flag selecting integrations for agents such as claude, codex, opencode, aider, cursor, copilot, cline, windsurf, roo, and agents, writing the corresponding instruction files and hooks. -- evidence: [README.md#L88-L88](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L88-L88), [README.md#L75-L86](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L75-L86) (`clm_fc13f5b7ffcb9ed5fb15c552d81feb0bf2f192f6df1dc5d41b6039f454f3de71`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The docs state these are historical results whose raw run artifacts are not included in the checkout, so CI does not claim to reproduce the numerical advantage; versioned traces and a reproduction command are required first. -- evidence: [docs/benchmark.md#L9-L9](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/docs/benchmark.md#L9-L9), [README.md#L240-L240](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L240-L240) (`clm_46020c87fe9e583359f2f757c200b53ff09d372ed450381b9b2d70410d2123e4`)

## dependencies (1 claim(s))

- [observation/documented] The CLI is installed via pipx and requires Python 3.11+; non-Python language adapters rely on tree-sitter, while Swift and VB.NET use structural parsers. -- evidence: [README.md#L66-L71](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L66-L71), [README.md#L171-L173](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L171-L173) (`clm_8f04bee140652d5709f0620afb3e0aa6e6dd82eed9715c3ab9084056ad4746ef`)

## limitations (2 claim(s))

- [observation/documented] The benchmark notes CodeDNA v0.7 shows roughly zero benefit on cross-cutting tasks with no call chain (e.g. task 11808); a proposed cross_cutting_patterns: feature is referenced in SPEC.md §2.4, and the related: field addresses the cross-cutting gap. -- evidence: [docs/benchmark.md#L51-L51](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/docs/benchmark.md#L51-L51), [docs/benchmark.md#L45-L45](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/docs/benchmark.md#L45-L45) (`clm_85c91b3ba0efda61cb94dea0fe86ae9bc7fe9e01c8ce45932bf18c018ebf9040`)
- [observation/documented] Python is described as the most tested language; non-Python adapters have seen less real-world usage, and users are asked to report wrong exports or header format issues. -- evidence: [README.md#L171-L173](https://github.com/Larens94/codedna/blob/b3fe577b47c9589e911224e2092b12cd3afc9e4a/README.md#L171-L173) (`clm_9ac30038584937f8777a79e6bdfbf103fcd8c526b53aa592e586896916ed5d3e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

