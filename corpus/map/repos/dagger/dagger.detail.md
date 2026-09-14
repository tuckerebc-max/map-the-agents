# dagger/dagger -- full detail

[Back to orientation](dagger.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dagger/dagger/7c35e6274737acff0f6bd76614abb5e04efa7d12/409fbc1fde736715.json](../../../wiki/dossiers/dagger/dagger/7c35e6274737acff0f6bd76614abb5e04efa7d12/409fbc1fde736715.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Dagger is documented as a platform for automating software delivery, providing an execution engine and a system API for orchestrating containers, filesystems, secrets, git repositories, and network tunnels. -- evidence: [README.md#L25-L25](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L25-L25), [README.md#L3-L3](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L3-L3), [README.md#L15-L15](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L15-L15) (`clm_d7651630f5ed41c4ce88358af829f17a99056ade0591290c15a1edbd1c8c5b3f`)
- [observation/documented] Every operation emits OpenTelemetry spans enriched with logs and metrics; the CLI includes a live TUI and traces can be exported to Jaeger, Honeycomb, or any OTel-compatible backend. -- evidence: [README.md#L21-L21](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L21-L21), [README.md#L35-L35](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L35-L35) (`clm_086248ef5f19a63b47e04a84c1bdf7b482a6b01858d7ed067ab46c332d36ab37`)

## design-choices (1 claim(s))

- [observation/documented] Custom object types are content-addressed and can cross SDK and module boundaries without serialization; every operation is keyed by its inputs so only affected operations re-run, with content-addressed caching across local runs and CI. -- evidence: [README.md#L31-L31](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L31-L31), [README.md#L29-L29](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L29-L29) (`clm_59b369010545209ec952eeffada33e1ff4e0d3e43186baf6c143b19a121b7b97`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: the Code of Conduct (Contributor Covenant 2.1) defines community standards, a four-step enforcement ladder (correction, warning, temporary ban, permanent ban), and reporting to legal@dagger.io. -- evidence: [CODE_OF_CONDUCT.md#L96-L97](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L96-L97), [CODE_OF_CONDUCT.md#L61-L63](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L61-L63), [CODE_OF_CONDUCT.md#L119-L120](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L119-L120), [CODE_OF_CONDUCT.md#L84-L85](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L84-L85), [CODE_OF_CONDUCT.md#L107-L109](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L107-L109), [CODE_OF_CONDUCT.md#L75-L76](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L75-L76), [CODE_OF_CONDUCT.md#L116-L117](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/CODE_OF_CONDUCT.md#L116-L117) (`clm_41e8affd90d19597ff3999a7066592e58e2a5b89750594c41b8bf92a8027d91b`)
- [observation/documented] Repository development practice: RELEASING.md prescribes a release process using changie for release notes, the gh CLI, and a prep PR; internal/version/VERSION is the single source of truth propagated by `dagger generate`. -- evidence: [RELEASING.md#L219-L222](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L219-L222), [RELEASING.md#L111-L116](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L111-L116), [RELEASING.md#L172-L174](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L172-L174), [RELEASING.md#L169-L170](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L169-L170), [RELEASING.md#L211-L215](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L211-L215), [RELEASING.md#L150-L152](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L150-L152) (`clm_3184e7b87fbfef61d605b31fe4c05dd591697492696f715f93da57427a2f711e`)
- [observation/documented] Repository development practice: pushing a version tag triggers the publish.yml workflow, and patch releases may be cut from release branches with a separate catch-up PR to main. -- evidence: [RELEASING.md#L298-L298](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L298-L298), [RELEASING.md#L289-L292](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L289-L292), [RELEASING.md#L78-L81](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L78-L81) (`clm_0f3694a87625c36771cfceaadfaf1ba3d1713f1d4be7e64722c86df75de43ff9`)
- [observation/documented] Repository development practice: RELEASING.md says backwards compatibility between mismatched CLI and engine versions is attempted where possible, with minimum versions bumped in engine/version.go when protocol or feature changes require it. -- evidence: [RELEASING.md#L45-L46](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L45-L46), [RELEASING.md#L37-L40](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L37-L40), [RELEASING.md#L48-L50](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/RELEASING.md#L48-L50) (`clm_22ae115ba65a74d9e0ac789e8cc3cfbdc75330c0ccf98faa010c486d6eb06529`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product ships SDKs in eight languages (Go, Python, TypeScript, PHP, Java, .NET, Elixir, Rust), each generated from the API schema, plus an interactive REPL. -- evidence: [README.md#L27-L27](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L27-L27), [README.md#L15-L15](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L15-L15) (`clm_1e6f3b614732ff6c7ae3f62b98bccd4113ba50e3ae08c6b9e851f393fe9a7985`)
- [observation/documented] The CLI can be installed via Homebrew with `brew install dagger/tap/dagger`, and the product runs locally, in CI servers, or in the cloud. -- evidence: [README.md#L5-L5](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L5-L5), [README.md#L7-L9](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L7-L9) (`clm_84814ade7823a272e5849b4b71a5f5426530ab84b13a38cd66b762f21df7fd8a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The only runtime requirement is a Linux container runtime such as Docker; it runs natively on Linux and via Docker Desktop or similar on macOS and Windows, with identical local and CI behavior. -- evidence: [README.md#L17-L17](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L17-L17), [README.md#L33-L33](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/README.md#L33-L33) (`clm_e9e4b4e91c4aef35598f73a1b5cd9aa5f8585b9b0c0b9d2e664fefccce4272e7`)

## limitations (1 claim(s))

- [observation/documented] A tracking document reports that `dagger migrate` produced no settings-hint comments in `.dagger/config.toml` on a fresh clone, and that hint introspection failures were logged via slog.Warn without surfacing in default CLI output. -- evidence: [migrate-settings-hints-tracking.md#L81-L89](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/migrate-settings-hints-tracking.md#L81-L89), [migrate-settings-hints-tracking.md#L9-L9](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/migrate-settings-hints-tracking.md#L9-L9), [migrate-settings-hints-tracking.md#L36-L36](https://github.com/dagger/dagger/blob/7c35e6274737acff0f6bd76614abb5e04efa7d12/migrate-settings-hints-tracking.md#L36-L36) (`clm_834fc871f84bd767bfe4df1cc86a58af9e09b4d88a082006f065bcfaef5beb74`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

