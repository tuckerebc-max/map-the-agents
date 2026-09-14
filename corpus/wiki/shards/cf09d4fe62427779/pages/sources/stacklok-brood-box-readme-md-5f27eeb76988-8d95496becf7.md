---
access: public
aliases: []
claim_ids:
- clm_0374eac973af986c4f781388f7b41d5bc279408f3f9c30ffff6ce4fb0232429f
- clm_134925bbe0509c11bbd12dbc3ba9165d81f4b3e35b41910fcec58d6144bd3fc3
- clm_1f8e416306bbbd34b82897322ae7a3649fd268e329ce7705d71bc1fedd2908d8
- clm_40d45552c2f6e55adc339acc419f33fe3542416fbe60cc3b28401bf5ca1c187b
- clm_60cac2514d40779efa690ed3303a1b062c073b159d3ce90fa05c9dac8c721d35
- clm_764c6adc1e1811a38f971b42ea9c353fa7a0aa7ab06ced7a69a0d64d81f0c167
- clm_91eebdde1a6ee0a53a552c7670f0143c2243775b0ca029dab88381cd2fc04dbf
- clm_b02eefd131eba01a9e345283241e7337ffbada4866c63f197ed1d6eca9f1b7ad
- clm_b7fcc5c1ad3a89004acda19fee5016125a8b4ef5dd8eb7eb3f715ede62262b20
- clm_b8de62be6f9bf9952a4806e1599889fd995a1335b1f94f45901501b498b0eaaa
- clm_f4a6e91efd9543ebb023224d80d8793ed58f5daa6dda08bb19b51bdeabed9570
maturity: draft
page_id: pg_d84a806050a15beea81c8d95496becf7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_241dcdb897f356c4ba42b667d45abd2a
title: stacklok/brood-box/README.md @ 5f27eeb76988
updated_at: '2026-09-14T02:42:31Z'
---

# stacklok/brood-box/README.md @ 5f27eeb76988

<!-- rcw:begin owner=source:src_241dcdb897f356c4ba42b667d45abd2a block=evidence -->
- The CLI exposes commands like `bbox claude-code`, `bbox list`, and `bbox run-image <oci-image>`, with flags for cpus, memory, workspace, review, egress profile, allow-host, and MCP settings. [@claim:clm_0374eac973af986c4f781388f7b41d5bc279408f3f9c30ffff6ce4fb0232429f]
- The project is explicitly experimental and warns that APIs, CLI flags, config format, and behavior may change without notice between releases. [@claim:clm_134925bbe0509c11bbd12dbc3ba9165d81f4b3e35b41910fcec58d6144bd3fc3]
- Configuration is three-level (CLI flags > per-workspace .broodbox.yaml > global ~/.config/broodbox/config.yaml), with CLI flags always winning. [@claim:clm_1f8e416306bbbd34b82897322ae7a3649fd268e329ce7705d71bc1fedd2908d8]
- A DNS-aware egress firewall offers three profiles: permissive (all outbound), standard (LLM provider plus common dev infrastructure), and locked (LLM provider only), with additional hosts allowed via --allow-host using DNS hostnames only. [@claim:clm_40d45552c2f6e55adc339acc419f33fe3542416fbe60cc3b28401bf5ca1c187b]
- Brood Box depends on stacklok/go-microvm as a tagged module (e.g. v0.0.16); task build downloads pre-built go-microvm runtime artifacts and embeds them into a self-contained pure-Go bbox binary, while libkrunfw firmware is downloaded at runtime and cached. [@claim:clm_60cac2514d40779efa690ed3303a1b062c073b159d3ce90fa05c9dac8c721d35]
- Per-workspace config cannot widen egress or disable review; workspace.mode: direct cannot be enabled by .broodbox.yaml, and security-sensitive exclude patterns like .env* and *.pem are always excluded and cannot be negated. [@claim:clm_764c6adc1e1811a38f971b42ea9c353fa7a0aa7ab06ced7a69a0d64d81f0c167]
- Brood Box is an experimental CLI for running coding agents in hardware-isolated microVMs, with APIs, flags, and config format subject to change between releases. [@claim:clm_91eebdde1a6ee0a53a552c7670f0143c2243775b0ca029dab88381cd2fc04dbf]
- The guest VM runs a custom Go init binary (bbox-init) as PID 1 that handles boot, networking, workspace mounting, and an embedded SSH server, with no shell scripts or external sshd. [@claim:clm_b02eefd131eba01a9e345283241e7337ffbada4866c63f197ed1d6eca9f1b7ad]
- Repository development practice: contributors must always use `task` targets (build, test, lint, fmt, verify) rather than raw go/docker commands, because the Taskfile sets critical flags, ldflags, and environment variables. [@claim:clm_b7fcc5c1ad3a89004acda19fee5016125a8b4ef5dd8eb7eb3f715ede62262b20]
- Built-in agents (claude-code, codex, opencode, hermes, gemini) each ship as a per-agent client package pairing an Agent value with a Plugin for MCP config injection and credential seeding, and custom agents can be defined in config. [@claim:clm_b8de62be6f9bf9952a4806e1599889fd995a1335b1f94f45901501b498b0eaaa]
- Snapshot mode uses FICLONE (Linux) or clonefile (macOS) for copy-on-write cloning, SHA-256 based diffing with unified diffs, hash re-verification on flush to prevent TOCTOU, and the VM is stopped before review begins. [@claim:clm_f4a6e91efd9543ebb023224d80d8793ed58f5daa6dda08bb19b51bdeabed9570]
<!-- rcw:end owner=source:src_241dcdb897f356c4ba42b667d45abd2a block=evidence -->

## Researcher notes

