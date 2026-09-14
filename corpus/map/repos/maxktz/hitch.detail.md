# maxktz/hitch -- full detail

[Back to orientation](hitch.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/maxktz/hitch/bcbfca2602259507245e776e366666fee89f4d6b/a239af80cda50b58.json](../../../wiki/dossiers/maxktz/hitch/bcbfca2602259507245e776e366666fee89f4d6b/a239af80cda50b58.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Hitch is not a terminal multiplexer UI like tmux; the terminal feels like a normal shell while Hitch proxies input/output, records context, and exposes agent-friendly commands. -- evidence: [README.md#L44-L44](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L44-L44) (`clm_1b27170cff80c1d0ab3195277abc8e6a772ee1e06f9ab06cdc70a865c8064b81`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run `cargo fmt -- --check` and `cargo test` before committing, and build locally with `cargo build --release`. -- evidence: [CONTRIBUTING.md#L9-L12](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L9-L12), [CONTRIBUTING.md#L16-L18](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L16-L18), [CONTRIBUTING.md#L7-L7](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L7-L7) (`clm_8da2f6f795818f6575b7ae57a7877b48524e00fc9ebcf436419b60b05208b7d4`)
- [observation/documented] Repository development practice: releases use `npm run release -- <version>` and a tag push; GitHub Actions then builds native binaries, publishes hitch-cli to npm, and creates a GitHub release. -- evidence: [CONTRIBUTING.md#L24-L27](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L24-L27), [CONTRIBUTING.md#L29-L29](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L29-L29) (`clm_ba1c5f2217655bdacc2ef49bd6ab15bda6303007ae37d5d7f8e601acb69d685d`)

## skills-patterns (2 claim(s))

- [observation/documented] A SKILL.md (version 3) describes when agents should use hitch, e.g. before starting a dev server, watcher, tunnel, REPL, build, or log tail that may already be running. -- evidence: [SKILL.md#L1-L5](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L1-L5) (`clm_2bf1f55bf4047ff84256f81224f2612b07336f861e47aaf8fd03feebf89ffe86`)
- [observation/documented] The skill instructs agents to prefer `hitch context` first, avoid --all by default, use --wait instead of sleep polling, and only use hitch for collaboration rather than short tool calls. -- evidence: [SKILL.md#L99-L106](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L99-L106), [SKILL.md#L77-L77](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L77-L77), [SKILL.md#L29-L32](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L29-L32) (`clm_0ba161c12660d344be2c3507f0fdfb5068a0c68ced87cce3310cd76e0ff56d3e`)

## interfaces (5 claim(s))

- [observation/documented] Hitch is a CLI for sharing the user's real terminal with AI coding agents; running `hitch` gives agents terminal context, ability to send keys or commands, and inspect output. -- evidence: [README.md#L40-L40](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L40-L40) (`clm_3681a4756ba766be2a278fad254b29188671aa3945b873d82a9ea4cc5bd01575`)
- [observation/documented] The `hitch context` command shows compact terminal state and recent output, with forms for all project terminals, a specific terminal, or `--all` including terminals outside the project. -- evidence: [SKILL.md#L21-L24](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L21-L24), [SKILL.md#L17-L17](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L17-L17) (`clm_6dc0f5014bf85f06a57fd01d44d3497ffac6a9cbf647cb8cbf2e9c6c278947af`)
- [observation/documented] `hitch send-keys -t <terminal>` sends input to a terminal, supports keys like Enter, Tab, C-c, and options including --wait finish/quiet/time/output, --timeout (default 30s), --tail, and --force. -- evidence: [SKILL.md#L51-L58](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L51-L58), [SKILL.md#L36-L38](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L36-L38), [SKILL.md#L42-L47](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L42-L47) (`clm_2b50d452eefc34b43471e6de22d31a722a804fe8e38b6eeb3fdda4c1b6459d56`)
- [observation/documented] `hitch capture` mirrors tmux capture-pane behavior with tmux-compatible options (-p, -S, -E, -e) and accepts no-op compatibility flags such as -C, -J, -N, -T, -a, -q. -- evidence: [SKILL.md#L95-L95](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L95-L95), [SKILL.md#L83-L83](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L83-L83), [SKILL.md#L87-L91](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L87-L91) (`clm_52783d4ddb5d9029927b667fcfe7cef5edec8bd8404c7e2aacde3e259f84430a`)
- [observation/documented] Human-facing usage is minimal: `hitch` starts sharing and `unhitch` or `hitch off` stops it; remaining commands are built for agents. -- evidence: [README.md#L73-L73](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L73-L73), [README.md#L61-L63](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L61-L63), [README.md#L70-L71](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L70-L71), [README.md#L67-L68](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L67-L68) (`clm_97400cbe362db73191667eb7250e8c6c723d8c7fa3dcab69c865899f447cd763`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Hitch refuses by default sending shell commands into terminals with running processes, printing terminal context instead; `--force` overrides this, and a sequence starting with C-c is allowed. -- evidence: [SKILL.md#L99-L106](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L99-L106) (`clm_cb46d937cfce6256437e956c6d4eb4e6b5f2af0137f98e5a865edb6ddfc6b331`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation is via `npm install -g hitch-cli`; supported platforms are macOS and Linux on arm64 or x64. -- evidence: [README.md#L48-L51](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L48-L51), [README.md#L55-L55](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L55-L55) (`clm_173014819b1af3b4b441868ee2098845bf5b367c8e77a8cb4d24a31d65b0f2f6`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

