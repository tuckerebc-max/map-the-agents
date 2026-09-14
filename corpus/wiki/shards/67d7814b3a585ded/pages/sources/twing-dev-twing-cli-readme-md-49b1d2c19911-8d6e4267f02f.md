---
access: public
aliases: []
claim_ids:
- clm_03781343b95aef32fa839709ff11869f60d675c0430ddc28bea754659ada912b
- clm_258832d01acf169428b6ca31164e2571b8e7c74118c4b5ec7c7d6dc40b830962
- clm_2a056bc6b6a616d2b04e593858ae9bd68ac56b574396f2acc932e7c3b689f3e6
- clm_35473d2c0360a2cd5247908de09429f3f37633a3941330e45ea2e7566085671c
- clm_4370133f04cf4eca1cf6fc2b618293a8bf215e39bc0e670c4d027b3922d476ce
- clm_580a470fef8f579e4cd916b542bcc50f02d688e7cb6c2e8f9dcb2e419042402f
- clm_752afc4d5f3c5b3e7ce6d7a9215271068d38f5259fcba201859d1ca0f6c40b4e
- clm_84fdd5de41d572865cc3dd427ce9bd11fecc5ea5640f283367bfeaa0dd5ffeff
- clm_c77eb8366432496f2dca7c960bc3b5db7b4d3b62fa55d2a150927e064d5e58f5
- clm_cb633858ce268c0ad56d668ba7e2ae71866314b4d336fcc2b638ad6f1be27744
- clm_d1a5ce253807ae88417c4098343f326cb1d431c864da3db5ee5cbd46d0bacfba
- clm_ec541e5cef76b42759dcbbad9d5650b786eba1d1761952b3dd290a0c46197fc7
- clm_f9ad7a2c9c060ab8eca3b2ca0bc421414c60af4112b4bf2c7c478e6ca06c09fc
maturity: draft
page_id: pg_a3d0d975c6c55c7d968f8d6e4267f02f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5d6d6f2ab9135edf952c47856431bec5
title: Twing-dev/twing-cli/README.md @ 49b1d2c19911
updated_at: '2026-09-14T04:28:45Z'
---

# Twing-dev/twing-cli/README.md @ 49b1d2c19911

<!-- rcw:begin owner=source:src_5d6d6f2ab9135edf952c47856431bec5 block=evidence -->
- The CLI needs Node.js >= 20; no Go toolchain is required for users because the twing-hook Go binary is fetched automatically on first init, though contributors with Go build it from source. [@claim:clm_03781343b95aef32fa839709ff11869f60d675c0430ddc28bea754659ada912b]
- Bucket 3 conflicts come from Tree-sitter-parsed claims and bucket 4 from an async Bedrock semantic pass, so those findings can arrive after the edit already succeeded via align or an alignment thread. [@claim:clm_258832d01acf169428b6ca31164e2571b8e7c74118c4b5ec7c7d6dc40b830962]
- The CLI exposes commands such as twing init, twing align, and twing design register/amend/close, with register taking a summary and touched paths. [@claim:clm_2a056bc6b6a616d2b04e593858ae9bd68ac56b574396f2acc932e7c3b689f3e6]
- Repository development practice: contributors need Node.js >= 20, git, and Go for the hook; the repo builds packages/core, packages/cli, and packages/server via TypeScript project references with npm install and npm run build, and npm link in packages/cli provides a local twing command. [@claim:clm_35473d2c0360a2cd5247908de09429f3f37633a3941330e45ea2e7566085671c]
- Windows hook-execution behavior for the bootstrap mechanism is unverified, and init's OS-level service install is cited as a known gap. [@claim:clm_4370133f04cf4eca1cf6fc2b618293a8bf215e39bc0e670c4d027b3922d476ce]
- Twing is a CLI plus a hook for coding agents (Claude Code today, others planned) and a small server that every agent's client talks to, letting multiple agents on a team coordinate. [@claim:clm_580a470fef8f579e4cd916b542bcc50f02d688e7cb6c2e8f9dcb2e419042402f]
- Conflicts collapse into four buckets; bucket 1 (constraint violations) is admin-gated and blocking, bucket 2 never blocks, and peer-vs-peer buckets 3/4 can be self-resolved with a justification. [@claim:clm_752afc4d5f3c5b3e7ce6d7a9215271068d38f5259fcba201859d1ca0f6c40b4e]
- A simulator directory runs two real claude CLI sessions concurrently against a shared fixture project to exercise the align feature end to end. [@claim:clm_84fdd5de41d572865cc3dd427ce9bd11fecc5ea5640f283367bfeaa0dd5ffeff]
- The twing review command (test-delta integrity on top of align) is not built yet, and a second-admin-approves-first flow for constraint changes is tracked follow-up work, not yet built. [@claim:clm_c77eb8366432496f2dca7c960bc3b5db7b4d3b62fa55d2a150927e064d5e58f5]
- The coordinator server (packages/server) is described as a single process with no external database, and it generates a one-time bootstrap token on first run. [@claim:clm_cb633858ce268c0ad56d668ba7e2ae71866314b4d336fcc2b638ad6f1be27744]
- Plan-text design checks need an LLM provider, auto-detected in precedence order AWS, GCP, OpenRouter, Bifrost; with none configured the check fails soft to clean while the registered-design rule still applies. [@claim:clm_d1a5ce253807ae88417c4098343f326cb1d431c864da3db5ee5cbd46d0bacfba]
- Setup installs a hook wired into Claude Code and starts a background daemon; hooks are stateless per-invocation, while the daemon watches edits and syncs them to the server. [@claim:clm_ec541e5cef76b42759dcbbad9d5650b786eba1d1761952b3dd290a0c46197fc7]
- Authentication mints a local personal access token of which only the hash reaches the server; it reuses the gh CLI token when available, else falls back to a browser OAuth device flow. [@claim:clm_f9ad7a2c9c060ab8eca3b2ca0bc421414c60af4112b4bf2c7c478e6ca06c09fc]
<!-- rcw:end owner=source:src_5d6d6f2ab9135edf952c47856431bec5 block=evidence -->

## Researcher notes

