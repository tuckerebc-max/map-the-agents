# stacklok/brood-box -- full detail

[Back to orientation](brood-box.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stacklok/brood-box/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/7d277f4201e40de9.json](../../../wiki/dossiers/stacklok/brood-box/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/7d277f4201e40de9.json)

## specifications (1 claim(s))

- [observation/documented] Brood Box is an experimental CLI for running coding agents in hardware-isolated microVMs, with APIs, flags, and config format subject to change between releases. -- evidence: [README.md#L6-L6](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L6-L6), [README.md#L3-L4](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L3-L4) (`clm_91eebdde1a6ee0a53a552c7670f0143c2243775b0ca029dab88381cd2fc04dbf`)

## components (2 claim(s))

- [observation/documented] The project follows a strict DDD layering: pure domain packages under pkg/domain, an application SandboxRunner in pkg/sandbox, infrastructure implementations in internal/infra, and a Cobra CLI composition root in cmd/bbox. -- evidence: [docs/ARCHITECTURE.md#L8-L34](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L8-L34), [docs/ARCHITECTURE.md#L163-L163](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L163-L163), [docs/ARCHITECTURE.md#L88-L88](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L88-L88), [docs/ARCHITECTURE.md#L110-L110](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L110-L110), [docs/ARCHITECTURE.md#L165-L169](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L165-L169), [docs/ARCHITECTURE.md#L3-L4](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L3-L4) (`clm_1a357f8736b6cc0a08657b1756e8df4ef2f442266db5a604078341f7ba94e5cb`)
- [observation/documented] Built-in agents (claude-code, codex, opencode, hermes, gemini) each ship as a per-agent client package pairing an Agent value with a Plugin for MCP config injection and credential seeding, and custom agents can be defined in config. -- evidence: [README.md#L291-L297](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L291-L297), [README.md#L301-L311](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L301-L311), [CLAUDE.md#L69-L73](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/CLAUDE.md#L69-L73) (`clm_b8de62be6f9bf9952a4806e1599889fd995a1335b1f94f45901501b498b0eaaa`)

## design-choices (2 claim(s))

- [observation/documented] The guest VM runs a custom Go init binary (bbox-init) as PID 1 that handles boot, networking, workspace mounting, and an embedded SSH server, with no shell scripts or external sshd. -- evidence: [docs/ARCHITECTURE.md#L222-L280](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L222-L280), [README.md#L360-L362](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L360-L362) (`clm_b02eefd131eba01a9e345283241e7337ffbada4866c63f197ed1d6eca9f1b7ad`)
- [observation/documented] Snapshot mode uses FICLONE (Linux) or clonefile (macOS) for copy-on-write cloning, SHA-256 based diffing with unified diffs, hash re-verification on flush to prevent TOCTOU, and the VM is stopped before review begins. -- evidence: [README.md#L364-L368](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L364-L368), [README.md#L374-L383](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L374-L383) (`clm_f4a6e91efd9543ebb023224d80d8793ed58f5daa6dda08bb19b51bdeabed9570`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must always use `task` targets (build, test, lint, fmt, verify) rather than raw go/docker commands, because the Taskfile sets critical flags, ldflags, and environment variables. -- evidence: [README.md#L421-L423](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L421-L423), [CLAUDE.md#L10-L10](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/CLAUDE.md#L10-L10) (`clm_b7fcc5c1ad3a89004acda19fee5016125a8b4ef5dd8eb7eb3f715ede62262b20`)
- [observation/documented] Repository development practice: the project enforces strict DDD layer boundaries with dependency injection, and code that violates layer boundaries is treated as a blocking merge issue. -- evidence: [CLAUDE.md#L44-L44](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/CLAUDE.md#L44-L44) (`clm_8008fbafa15bc55a7f8c0ab1be53cfd09640010748e31a598d0605dc81226881`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes commands like `bbox claude-code`, `bbox list`, and `bbox run-image <oci-image>`, with flags for cpus, memory, workspace, review, egress profile, allow-host, and MCP settings. -- evidence: [README.md#L159-L159](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L159-L159), [README.md#L141-L141](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L141-L141), [README.md#L156-L156](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L156-L156), [README.md#L144-L144](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L144-L144), [README.md#L128-L128](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L128-L128), [README.md#L138-L138](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L138-L138), [README.md#L116-L119](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L116-L119), [README.md#L122-L122](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L122-L122) (`clm_0374eac973af986c4f781388f7b41d5bc279408f3f9c30ffff6ce4fb0232429f`)
- [observation/documented] Configuration is three-level (CLI flags > per-workspace .broodbox.yaml > global ~/.config/broodbox/config.yaml), with CLI flags always winning. -- evidence: [README.md#L231-L231](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L231-L231), [README.md#L187-L187](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L187-L187), [README.md#L191-L191](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L191-L191) (`clm_1f8e416306bbbd34b82897322ae7a3649fd268e329ce7705d71bc1fedd2908d8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The SandboxRunner lifecycle resolves the agent, merges config, collects forwarded env vars, creates a snapshot, starts the VM, runs an interactive SSH session, stops the VM, diffs, reviews per-file, flushes accepted changes, and cleans up. -- evidence: [docs/ARCHITECTURE.md#L90-L100](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L90-L100), [docs/ARCHITECTURE.md#L88-L88](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L88-L88) (`clm_024b85fabc3ed6fdccecf18b94b19125e6b36492f5d3805ce8e9a348b818f0b3`)

## tools-permissions (2 claim(s))

- [observation/documented] A DNS-aware egress firewall offers three profiles: permissive (all outbound), standard (LLM provider plus common dev infrastructure), and locked (LLM provider only), with additional hosts allowed via --allow-host using DNS hostnames only. -- evidence: [README.md#L141-L141](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L141-L141), [README.md#L272-L276](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L272-L276), [README.md#L270-L270](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L270-L270), [README.md#L286-L287](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L286-L287) (`clm_40d45552c2f6e55adc339acc419f33fe3542416fbe60cc3b28401bf5ca1c187b`)
- [observation/documented] Per-workspace config cannot widen egress or disable review; workspace.mode: direct cannot be enabled by .broodbox.yaml, and security-sensitive exclude patterns like .env* and *.pem are always excluded and cannot be negated. -- evidence: [README.md#L246-L249](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L246-L249), [README.md#L251-L251](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L251-L251), [README.md#L243-L244](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L243-L244), [README.md#L266-L266](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L266-L266) (`clm_764c6adc1e1811a38f971b42ea9c353fa7a0aa7ab06ced7a69a0d64d81f0c167`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Brood Box depends on stacklok/go-microvm as a tagged module (e.g. v0.0.16); task build downloads pre-built go-microvm runtime artifacts and embeds them into a self-contained pure-Go bbox binary, while libkrunfw firmware is downloaded at runtime and cached. -- evidence: [README.md#L89-L91](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L89-L91), [README.md#L93-L95](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L93-L95), [docs/ARCHITECTURE.md#L355-L359](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/docs/ARCHITECTURE.md#L355-L359) (`clm_60cac2514d40779efa690ed3303a1b062c073b159d3ce90fa05c9dac8c721d35`)

## limitations (1 claim(s))

- [observation/documented] The project is explicitly experimental and warns that APIs, CLI flags, config format, and behavior may change without notice between releases. -- evidence: [README.md#L3-L4](https://github.com/stacklok/brood-box/blob/5f27eeb76988dd38d18bf2af0e515b50ec9dca25/README.md#L3-L4) (`clm_134925bbe0509c11bbd12dbc3ba9165d81f4b3e35b41910fcec58d6144bd3fc3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

