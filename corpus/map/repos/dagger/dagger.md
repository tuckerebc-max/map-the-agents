# dagger/dagger

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7c35e6274737 @ 409fbc1fde736715

## Summary (orientation draft, not independently verified)

Selected evidence records: Dagger is documented as a platform for automating software delivery, providing an execution engine and a system API for orchestrating containers, filesystems, secrets, git repositories, and network tunnels. The product ships SDKs in eight languages (Go, Python, TypeScript, PHP, Java, .NET, Elixir, Rust), each generated from the API schema, plus an interactive REPL.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Dagger is documented as a platform for automating software delivery, providing an execution engine and a system API for orchestrating containers, filesystems, secrets, git repositories, and network tunnels. -- evidence: [README.md#L25-L25](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L25-L25), [README.md#L3-L3](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L3-L3), [README.md#L15-L15](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L15-L15)
  - [observation/documented] Every operation emits OpenTelemetry spans enriched with logs and metrics; the CLI includes a live TUI and traces can be exported to Jaeger, Honeycomb, or any OTel-compatible backend. -- evidence: [README.md#L21-L21](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L21-L21), [README.md#L35-L35](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L35-L35)
- design-choices (1 claim(s)):
  - [observation/documented] Custom object types are content-addressed and can cross SDK and module boundaries without serialization; every operation is keyed by its inputs so only affected operations re-run, with content-addressed caching across local runs and CI. -- evidence: [README.md#L31-L31](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L31-L31), [README.md#L29-L29](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L29-L29)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: the Code of Conduct (Contributor Covenant 2.1) defines community standards, a four-step enforcement ladder (correction, warning, temporary ban, permanent ban), and reporting to legal@dagger.io. -- evidence: [CODE_OF_CONDUCT.md#L96-L97](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L96-L97), [CODE_OF_CONDUCT.md#L61-L63](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L61-L63), [CODE_OF_CONDUCT.md#L119-L120](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L119-L120), [CODE_OF_CONDUCT.md#L84-L85](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L84-L85), [CODE_OF_CONDUCT.md#L107-L109](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L107-L109), [CODE_OF_CONDUCT.md#L75-L76](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L75-L76), [CODE_OF_CONDUCT.md#L116-L117](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L116-L117)
  - [observation/documented] Repository development practice: RELEASING.md prescribes a release process using changie for release notes, the gh CLI, and a prep PR; internal/version/VERSION is the single source of truth propagated by `dagger generate`. -- evidence: [RELEASING.md#L219-L222](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L219-L222), [RELEASING.md#L111-L116](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L111-L116), [RELEASING.md#L172-L174](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L172-L174), [RELEASING.md#L169-L170](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L169-L170), [RELEASING.md#L211-L215](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L211-L215), [RELEASING.md#L150-L152](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L150-L152)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships SDKs in eight languages (Go, Python, TypeScript, PHP, Java, .NET, Elixir, Rust), each generated from the API schema, plus an interactive REPL. -- evidence: [README.md#L27-L27](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L27-L27), [README.md#L15-L15](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L15-L15)
  - [observation/documented] The CLI can be installed via Homebrew with `brew install dagger/tap/dagger`, and the product runs locally, in CI servers, or in the cloud. -- evidence: [README.md#L5-L5](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L5-L5), [README.md#L7-L9](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L7-L9)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](dagger.detail.md)

Metadata and full claim list: [full detail](dagger.detail.md)
Human notes ([notes](dagger.notes.md), never overwritten by build)

[Back to map index](../../index.md)
