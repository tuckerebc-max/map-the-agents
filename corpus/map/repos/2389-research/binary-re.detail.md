# 2389-research/binary-re -- full detail

[Back to orientation](binary-re.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/binary-re/42aee9063f3f3d52616700df3aa16df82b848604/fa6ea75b7b34d0e2.json](../../../wiki/dossiers/2389-research/binary-re/42aee9063f3f3d52616700df3aa16df82b848604/fa6ea75b7b34d0e2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The repo includes reference documentation covering per-architecture tooling considerations (ARM, ARM64, x86_64, MIPS), Ghidra headless decompilation usage, and Python bytecode reverse engineering. -- evidence: [docs/python-bytecode-re.md#L5-L5](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/python-bytecode-re.md#L5-L5), [docs/arch-adapters.md#L5-L5](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/arch-adapters.md#L5-L5), [docs/ghidra-headless.md#L5-L5](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/ghidra-headless.md#L5-L5) (`clm_c8d0f5f6a73515c224d721bbe63f46ce55a2321f93b2c133dfb9351409ff6eeb`)
- [observation/documented] A dated case-study document analyzes an LZSS compressor binary, identifying a window-position wrap bug in decompression and a 9-byte instruction-reorder patch verified by MD5 comparison of outputs. -- evidence: [docs/bad-compression-analysis-2026-01-06.md#L112-L116](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L112-L116), [docs/bad-compression-analysis-2026-01-06.md#L106-L108](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L106-L108), [docs/bad-compression-analysis-2026-01-06.md#L5-L7](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L5-L7), [docs/bad-compression-analysis-2026-01-06.md#L77-L77](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L77-L77) (`clm_35540d822326bd186a94e2b9e4ec20befee2784835956ac7459266ecfc223d0c`)

## design-choices (2 claim(s))

- [observation/documented] The stated philosophy is that the LLM drives analysis while the human provides context: the user supplies platform, hardware, theories, and constraints, and Claude runs tools, forms hypotheses, and designs experiments. -- evidence: [README.md#L80-L80](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L80-L80), [README.md#L84-L84](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L84-L84), [README.md#L82-L82](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L82-L82) (`clm_5fc43892852603f17cd786b50be6fff722d04b80118e640a1d1863e552eded77`)
- [observation/documented] The example interaction shows the skill recording facts, stating a hypothesis with a confidence score of 0.7, then asking the user whether to proceed with static analysis or dynamic analysis under QEMU. -- evidence: [README.md#L49-L51](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L49-L51), [README.md#L44-L47](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L44-L47), [README.md#L53-L55](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L53-L55) (`clm_9d44c3cf6906aad16366cfc5e077b1295f4e0242f31e3bea36d3be2f73a5c5be`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] The plugin ships a 'binary-re' skill described as a structured RE workflow with hypothesis-driven analysis, driven by hypothesis-testing rather than blind exploration. -- evidence: [README.md#L16-L16](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L16-L16), [README.md#L3-L3](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L3-L3) (`clm_db1dc933e9900f1bd3d50f0946ee0369a125a3731bcbd64642929293e9648ce0`)
- [observation/documented] The case study records lessons for the skill: compare known inputs/outputs first, trace circular-buffer wrap-around carefully, and watch for divergent code paths implementing the same operation. -- evidence: [docs/bad-compression-analysis-2026-01-06.md#L124-L124](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L124-L124), [docs/bad-compression-analysis-2026-01-06.md#L122-L122](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L122-L122), [docs/bad-compression-analysis-2026-01-06.md#L126-L126](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L126-L126) (`clm_a01152ebcf3907c3e1a9e6f235ada2680a26a6543cced0664d4ae74e29663735`)

## interfaces (1 claim(s))

- [observation/documented] Installation is via Claude Code plugin marketplace commands: '/plugin marketplace add 2389-research/claude-plugins' followed by '/plugin install binary-re@2389-research'. -- evidence: [README.md#L7-L10](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L7-L10) (`clm_36d3adddb1c1512f5da3cd83283c196217521694e3075cc544a3bc78429f0993`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The skill asks for confirmation before executing binaries (even sandboxed), network-capable dynamic analysis, operations requiring device access, and major changes in analysis direction. -- evidence: [README.md#L88-L92](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L88-L92) (`clm_f5ec2725684eae24f606cc5f01f3ba2624d8f1baf909c7af4ed5d1dc79d90437`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Required external tools include radare2, qemu-user, and gdb-multiarch installed via apt, plus frida-tools via pip and ARM hard-float/arm64 cross sysroot packages (libc6-armhf-cross, libc6-arm64-cross). -- evidence: [README.md#L68-L69](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L68-L69), [README.md#L65-L65](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L65-L65), [README.md#L61-L61](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L61-L61) (`clm_9c886225fbed3bab1747bdb8ad8417e4a35fca5eb14b483119b64816ccff7cb1`)
- [observation/documented] The architecture guide lists fallbacks when QEMU user-mode emulation fails: Qiling Framework, Unicorn CPU-only emulation, full-system QEMU, or running on actual hardware. -- evidence: [docs/arch-adapters.md#L324-L327](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/arch-adapters.md#L324-L327), [docs/arch-adapters.md#L322-L322](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/arch-adapters.md#L322-L322) (`clm_f0d0733e9b8c00fb2d8bf10f3ae31b2d54383ecabb1dcbcd95b8cc4deb2beeec`)

## limitations (1 claim(s))

- [inference/documented] The emulation compatibility matrix suggests MIPS 64 emulation is limited and less tested, and ARM 64 user-mode emulation requires a newer QEMU version. -- evidence: [docs/arch-adapters.md#L312-L318](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/arch-adapters.md#L312-L318) (`clm_e7a1f02613658b4b09660e4f7825bbe680b467f2f60ac2799de83209f9102405`)

## relevance (1 claim(s))

- [observation/documented] Stated use cases include firmware analysis, protocol reverse engineering, security research on embedded systems, and hardware hacking of robot/IoT device internals. -- evidence: [README.md#L73-L76](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L73-L76) (`clm_e7295b2093cdf142c0d288f5b9d22d7ff5129dd115d4a4f6ef6559afb4f0c6dc`)

