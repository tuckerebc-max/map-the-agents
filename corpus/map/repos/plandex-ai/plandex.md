# plandex-ai/plandex

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e2d772072efa @ 99984345a25cc48d

## Summary (orientation draft, not independently verified)

Plandex is a terminal-based AI coding tool offering both a REPL (started with `plandex` or `pdx`) and a CLI for scripting and piping data into context. AI-generated changes are kept in a cumulative diff review sandbox separate from project files until applied, with controlled command execution so changes can be rolled back and debugged.

## Source coverage

Source coverage (partial): 6 of 37 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Project maps and syntax validation are built on tree-sitter, with support for 30+ languages. -- evidence: [README.md#L97-L97](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L97-L97)
- design-choices (3 claim(s)):
  - [observation/documented] AI-generated changes are kept in a cumulative diff review sandbox separate from project files until applied, with controlled command execution so changes can be rolled back and debugged. -- evidence: [README.md#L83-L83](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L83-L83)
  - [observation/documented] The tool handles up to 2M tokens of context directly (~100k per file) and can index directories of 20M+ tokens using tree-sitter project maps, loading only what each step needs. -- evidence: [README.md#L81-L81](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L81-L81), [README.md#L93-L93](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L93-L93)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] Plandex is a terminal-based AI coding tool offering both a REPL (started with `plandex` or `pdx`) and a CLI for scripting and piping data into context. -- evidence: [README.md#L121-L121](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L121-L121), [README.md#L190-L190](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L190-L190), [README.md#L198-L200](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L198-L200), [README.md#L81-L81](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L81-L81), [README.md#L123-L123](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L123-L123)
  - [observation/documented] A configuration system exposes settings such as auto-mode (none/basic/plus/semi/full, default semi), auto-apply (default false), auto-commit (default true), and can-exec, viewable via `plandex config` and modifiable via `plandex set-config`. -- evidence: [docs/docs/core-concepts/configuration.md#L31-L33](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L31-L33), [docs/docs/core-concepts/configuration.md#L62-L65](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L62-L65), [docs/docs/core-concepts/configuration.md#L8-L8](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L8-L8), [docs/docs/core-concepts/configuration.md#L53-L58](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L53-L58), [docs/docs/core-concepts/configuration.md#L12-L15](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L12-L15), [docs/docs/core-concepts/configuration.md#L37-L41](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L37-L41), [docs/docs/core-concepts/configuration.md#L19-L23](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L19-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Plandex supports models from Anthropic, OpenAI, Google, and open-source providers, with curated model packs trading off capability, cost, and speed; context caching is used for OpenAI, Anthropic, and Google models. -- evidence: [README.md#L99-L99](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L99-L99), [README.md#L85-L85](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L85-L85), [README.md#L111-L111](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L111-L111)
- limitations (2 claim(s)):
  - [observation/documented] On Windows, Plandex works only in the WSL shell; it does not work in the Windows CMD prompt or PowerShell. -- evidence: [README.md#L149-L149](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L149-L149)
  - [observation/documented] Plandex Cloud is winding down as of 10/3/2025 and is no longer accepting new users; self-hosted/local mode with Docker and your own provider API keys is the documented alternative. -- evidence: [README.md#L155-L158](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L155-L158)
More evidence: [full detail](plandex.detail.md)

Metadata and full claim list: [full detail](plandex.detail.md)
Human notes ([notes](plandex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
