# shinpr/galley -- full detail

[Back to orientation](galley.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shinpr/galley/b542bd7adb37039a5bc69393f199d8e9c7937679/b672269c9deea4f0.json](../../../wiki/dossiers/shinpr/galley/b542bd7adb37039a5bc69393f199d8e9c7937679/b672269c9deea4f0.json)

## specifications (2 claim(s))

- [observation/documented] Task YAML is trusted local input describing goal, acceptance criteria, scope, executor overrides, verification, and worktree, with a documented reference at docs/task-yaml.md. -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174) (`clm_2ed1c888f692d25f45055a745e8c0ce0ec7717c0d97ab68492b861eeb96941f5`)
- [observation/documented] Repositories are configured via two profile types: a quality profile (required checks, review dimensions, evidence, pass criteria) and an environment profile (commands, executor CLI/model/effort, constraints, PR behavior, cleanup). -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174) (`clm_f13e25185d4a23b868a16d5d3c8c861efda20641c98b23efd62d889aa24f9b99`)

## components (1 claim(s))

- [observation/documented] The system comprises a galley CLI, a background daemon that claims queued tasks, executor backends that implement tasks, and supervisor backends that act as the acceptance gate. -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174), [README.md#L144-L164](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L144-L164) (`clm_d135c5f58b64bbd0e65db2a27058b9d63c503607f44fc3f628a6f51139cfb381`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run gofmt, go test ./..., go build ./cmd/galley, and scripts/smoke-local.sh before opening a PR, and validate examples and plugin metadata when changing schemas or plugin files. -- evidence: [CONTRIBUTING.md#L14-L14](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L14-L14), [CONTRIBUTING.md#L16-L21](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L16-L21), [CONTRIBUTING.md#L38-L38](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L38-L38), [CONTRIBUTING.md#L40-L43](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L40-L43), [CONTRIBUTING.md#L25-L29](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L25-L29), [CONTRIBUTING.md#L23-L23](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L23-L23) (`clm_0739514d0879c50424af8232723805bfe4da1d24d9a8a5269823f298f38fd0b0`)
- [observation/documented] Repository development practice: releases are created from the GitHub UI, triggering a GoReleaser workflow that attaches macOS, Linux, and Windows archives; contributors add CHANGELOG.md entries for user-visible changes. -- evidence: [CONTRIBUTING.md#L68-L68](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L68-L68), [CONTRIBUTING.md#L72-L72](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L72-L72) (`clm_7436ed74d467404be417b19607c82aeceb6b27b5da18d045eb28d24ce24c2796`)

## skills-patterns (1 claim(s))

- [observation/documented] The plugin packages one Agent Skill for Claude Code, Codex, and Grok Build covering setup, CLI checks, task YAML drafting/validation, profile authoring, approval-gated queueing, and failed-run diagnosis; skills-compatible clients can symlink plugins/galley/skills/galley/. -- evidence: [README.md#L136-L138](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L136-L138), [README.md#L134-L134](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L134-L134), [README.md#L126-L126](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L126-L126), [README.md#L128-L132](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L128-L132) (`clm_e12979d6490fe9b2630c58f337f2c87e53fe6240d8efb3880a6dbed37585589e`)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes commands including daemon config init, daemon start, daemon status --output json, daemon run --once, task validate, profile validate, and schema generate/check. -- evidence: [CONTRIBUTING.md#L33-L36](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L33-L36), [README.md#L217-L222](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L217-L222), [README.md#L50-L52](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L50-L52), [CONTRIBUTING.md#L25-L29](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L25-L29) (`clm_97737edea9274ad95e9d132e02609a4c4d8eb87448532aa810b5fcb6f33cde16`)
- [observation/documented] Executor and supervisor model fields resolve from the task, then the environment profile; only the executor cli has a built-in default (claude), and empty model/effort values defer to the provider CLI's defaults. -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174) (`clm_34e8458e64599f828f575cd85fd5e73cb00c70ff47a9adf0b4e22b3843ca49bb`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The pipeline flows from task YAML plus repository policy through queueing, daemon claim, isolated git worktree execution, supervisor review, then acceptance (PR or local completion), retry within budget, or failure for human review. -- evidence: [README.md#L144-L164](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L144-L164) (`clm_6d00c05fdd0b4ad5e18e6abdfa193bdab2835d5186e3b1bc5c0ed0fee6e5dbc7`)
- [observation/documented] On revision, the supervisor reviews acceptance criteria before quality policy, preserves verified passes, and focuses the next attempt on unresolved work and regression risks. -- evidence: [README.md#L29-L34](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L29-L34) (`clm_e1b8484b31c51aca1e91efb81b90591024bf8025b75fc591ffe284a9c9852d26`)

## tools-permissions (1 claim(s))

- [observation/documented] Task YAML, profiles, and PR rerun comments are treated as privileged inputs that can influence local execution; PR comment requeueing is accepted only from the recorded PR author. -- evidence: [README.md#L228-L228](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L228-L228), [README.md#L226-L226](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L226-L226), [SECURITY.md#L5-L5](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/SECURITY.md#L5-L5) (`clm_2d557867a9dab6f3dc5710744b8e538f944f043bb5711093c936fb1dc7bdafce`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The plugin installs Galley tooling only; users must separately install and authenticate provider CLIs (claude, codex, grok), and GLM/Kimi run through Claude Code using glm_api_key or kimi_api_key in ~/.galley/daemon.yaml. -- evidence: [README.md#L56-L59](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L56-L59), [README.md#L40-L46](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L40-L46), [README.md#L38-L38](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L38-L38), [README.md#L48-L48](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L48-L48) (`clm_f0faf6f768e665824b32c69003b784d1d9f674e543f9a47039f87659c6135c3e`)
- [observation/documented] The standalone skill expects the galley CLI on PATH, and some workflows also use claude, codex, gh, and python3. -- evidence: [README.md#L140-L140](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L140-L140) (`clm_27b3eb0dcb69df7feafedd29e884acc74bf5ce51a2e432a16d3989addd44588b`)

## limitations (1 claim(s))

- [observation/documented] Run evidence is recorded for review but is explicitly not a sandbox boundary; stronger isolation requires isolated worktrees, scoped paths, and local OS or container controls. -- evidence: [SECURITY.md#L41-L41](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/SECURITY.md#L41-L41) (`clm_b1dc2bcf9fd858e42b55be9d90fd47cf1b25274f91483f3e1855d26587ff0a73`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

