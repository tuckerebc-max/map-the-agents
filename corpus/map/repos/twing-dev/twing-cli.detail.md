# twing-dev/twing-cli -- full detail

[Back to orientation](twing-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/twing-dev/twing-cli/49b1d2c199119d05ab217c8e659a21ea78be4ae5/77b105848016c816.json](../../../wiki/dossiers/twing-dev/twing-cli/49b1d2c199119d05ab217c8e659a21ea78be4ae5/77b105848016c816.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Twing is a CLI plus a hook for coding agents (Claude Code today, others planned) and a small server that every agent's client talks to, letting multiple agents on a team coordinate. -- evidence: [README.md#L3-L6](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L3-L6) (`clm_580a470fef8f579e4cd916b542bcc50f02d688e7cb6c2e8f9dcb2e419042402f`)
- [observation/documented] Setup installs a hook wired into Claude Code and starts a background daemon; hooks are stateless per-invocation, while the daemon watches edits and syncs them to the server. -- evidence: [README.md#L38-L57](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L38-L57) (`clm_ec541e5cef76b42759dcbbad9d5650b786eba1d1761952b3dd290a0c46197fc7`)

## design-choices (4 claim(s))

- [observation/documented] Conflicts collapse into four buckets; bucket 1 (constraint violations) is admin-gated and blocking, bucket 2 never blocks, and peer-vs-peer buckets 3/4 can be self-resolved with a justification. -- evidence: [README.md#L111-L127](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L111-L127), [README.md#L96-L100](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L96-L100) (`clm_752afc4d5f3c5b3e7ce6d7a9215271068d38f5259fcba201859d1ca0f6c40b4e`)
- [observation/documented] Bucket 3 conflicts come from Tree-sitter-parsed claims and bucket 4 from an async Bedrock semantic pass, so those findings can arrive after the edit already succeeded via align or an alignment thread. -- evidence: [README.md#L111-L127](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L111-L127) (`clm_258832d01acf169428b6ca31164e2571b8e7c74118c4b5ec7c7d6dc40b830962`)
- [observation/documented] Authentication mints a local personal access token of which only the hash reaches the server; it reuses the gh CLI token when available, else falls back to a browser OAuth device flow. -- evidence: [README.md#L38-L57](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L38-L57) (`clm_f9ad7a2c9c060ab8eca3b2ca0bc421414c60af4112b4bf2c7c478e6ca06c09fc`)
- [observation/documented] Plan-text design checks need an LLM provider, auto-detected in precedence order AWS, GCP, OpenRouter, Bifrost; with none configured the check fails soft to clean while the registered-design rule still applies. -- evidence: [README.md#L419-L428](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L419-L428) (`clm_d1a5ce253807ae88417c4098343f326cb1d431c864da3db5ee5cbd46d0bacfba`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors need Node.js >= 20, git, and Go for the hook; the repo builds packages/core, packages/cli, and packages/server via TypeScript project references with npm install and npm run build, and npm link in packages/cli provides a local twing command. -- evidence: [README.md#L548-L550](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L548-L550), [README.md#L541-L546](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L541-L546), [README.md#L533-L537](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L533-L537) (`clm_35473d2c0360a2cd5247908de09429f3f37633a3941330e45ea2e7566085671c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes commands such as twing init, twing align, and twing design register/amend/close, with register taking a summary and touched paths. -- evidence: [README.md#L291-L297](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L291-L297), [README.md#L129-L133](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L129-L133) (`clm_2a056bc6b6a616d2b04e593858ae9bd68ac56b574396f2acc932e7c3b689f3e6`)
- [observation/documented] The coordinator spec defines a single POST /v1/designs/check call that registers a design and returns a verdict (clean, overlap, or constraint_flag) in one blocking round trip. -- evidence: [docs/design-conflict-coordinator-spec.md#L117-L118](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L117-L118), [docs/design-conflict-coordinator-spec.md#L142-L158](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L142-L158), [docs/design-conflict-coordinator-spec.md#L160-L171](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L160-L171), [docs/design-conflict-coordinator-spec.md#L134-L140](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/docs/design-conflict-coordinator-spec.md#L134-L140) (`clm_c328fa290fb2431f3c6a4ebfd8b47218bb81c8486e59529ec60aba4ff641a79a`)

## memory-state (1 claim(s))

- [observation/documented] The coordinator server (packages/server) is described as a single process with no external database, and it generates a one-time bootstrap token on first run. -- evidence: [README.md#L407-L412](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L407-L412), [README.md#L399-L400](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L399-L400) (`clm_cb633858ce268c0ad56d668ba7e2ae71866314b4d336fcc2b638ad6f1be27744`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A simulator directory runs two real claude CLI sessions concurrently against a shared fixture project to exercise the align feature end to end. -- evidence: [README.md#L577-L579](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L577-L579) (`clm_84fdd5de41d572865cc3dd427ce9bd11fecc5ea5640f283367bfeaa0dd5ffeff`)

## dependencies (1 claim(s))

- [observation/documented] The CLI needs Node.js >= 20; no Go toolchain is required for users because the twing-hook Go binary is fetched automatically on first init, though contributors with Go build it from source. -- evidence: [README.md#L533-L537](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L533-L537), [README.md#L18-L20](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L18-L20) (`clm_03781343b95aef32fa839709ff11869f60d675c0430ddc28bea754659ada912b`)

## limitations (2 claim(s))

- [observation/documented] Windows hook-execution behavior for the bootstrap mechanism is unverified, and init's OS-level service install is cited as a known gap. -- evidence: [README.md#L278-L280](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L278-L280) (`clm_4370133f04cf4eca1cf6fc2b618293a8bf215e39bc0e670c4d027b3922d476ce`)
- [observation/documented] The twing review command (test-delta integrity on top of align) is not built yet, and a second-admin-approves-first flow for constraint changes is tracked follow-up work, not yet built. -- evidence: [README.md#L151-L160](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L151-L160), [README.md#L573-L573](https://github.com/Twing-dev/twing-cli/blob/49b1d2c199119d05ab217c8e659a21ea78be4ae5/README.md#L573-L573) (`clm_c77eb8366432496f2dca7c960bc3b5db7b4d3b62fa55d2a150927e064d5e58f5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

