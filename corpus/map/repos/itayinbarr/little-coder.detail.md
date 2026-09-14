# itayinbarr/little-coder -- full detail

[Back to orientation](little-coder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/itayinbarr/little-coder/a9e467f2be43b78441d723c84f173b98771b51ef/c1c886905f97db58.json](../../../wiki/dossiers/itayinbarr/little-coder/a9e467f2be43b78441d723c84f173b98771b51ef/c1c886905f97db58.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] little-coder is built on pi as a plain dependency, adding roughly 30 extensions, 30 skill markdown files, and a Python benchmark harness under .pi/extensions/, skills/, and benchmarks/. -- evidence: [README.md#L14-L14](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L14-L14) (`clm_4dec468a368c8cbe8d00d7d944e7378854cde64591c15b1bd8039f54920e9fd4`)
- [observation/documented] ShellStart runs background jobs with wake_on triggers (exit, regex match, silence, every_n_matches), delivering bounded excerpts plus exit code, with ShellLog, ShellList, ShellSend, and ShellStop companions. -- evidence: [README.md#L307-L312](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L307-L312), [README.md#L314-L319](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L314-L319), [README.md#L321-L321](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L321-L321) (`clm_a77b998a9e8b61909a17fa87a3daf1382d8639e325a8fd2201dfc8f2863de9c5`)

## design-choices (3 claim(s))

- [observation/documented] The launcher runs pi with --no-extensions and wires in only the bundled set, keeping cold-start context near 7k tokens and making loaded behavior fixed at ship time. -- evidence: [README.md#L16-L16](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L16-L16) (`clm_fe7a4ac89485c78a31919f0da9600f40d78c2026c0dd63664e0a09de80a16014`)
- [observation/documented] Per-phase model selection lets planning and implementation use different models via /plan-model, /action-model, and /model-handover auto|manual, with handover deferred until implementation begins. -- evidence: [README.md#L331-L337](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L331-L337), [README.md#L341-L341](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L341-L341) (`clm_d348bdaaf8e1252b4a40fc5a72530dedfd8a4bb573100306a6f25ba387f9e63d`)
- [observation/documented] A compaction watchdog checks context at every turn boundary and triggers pi's compaction at 80% of the window, tunable via LITTLE_CODER_COMPACT_AT_PERCENT, and pauses automatic compaction if a pass frees too little. -- evidence: [README.md#L429-L429](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L429-L429) (`clm_fa946be99f49e15972e8f99e58c2d792cb0da95917c4b25019266369dd2f55b8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] Users can opt into extra extensions via ~/.config/little-coder/extensions/, the LITTLE_CODER_EXTRA_EXTENSIONS variable, or a --with-pi-extensions relaunch; /extensions shows what loaded. -- evidence: [README.md#L18-L18](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L18-L18) (`clm_9d30a390208c87bd250b0333f8b31fa608e9950bc43de6c550de6fd49190c835`)
- [observation/documented] The CLI accepts --model (e.g. llamacpp/qwen3.6-35b-a3b, anthropic/claude-haiku-4-5, ollama/qwen3.5, lmstudio/local-model) and --list-models; bare invocation launches the models.json default. -- evidence: [README.md#L48-L52](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L48-L52), [README.md#L56-L56](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L56-L56), [README.md#L60-L66](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L60-L66) (`clm_0418c7aa98cb910ad8bed9a8fcdd37b47eea038ce0ddcbd03117eae3a3be5e78`)
- [observation/documented] Plan Mode (ctrl+q or --plan-mode) researches with sub-coders, asks 1-3 clarifying questions, writes a plan, and /implement starts a fresh session on the action model; Esc cancels. -- evidence: [README.md#L72-L82](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L72-L82) (`clm_d55d4e929c27f7aeb1c5d0a5a2dc62f8f4d5c1940e6cb80616cd2084af09eb16`)
- [observation/documented] Deep Research (f2 or /deep-research) fans out read-only sub-coders in an ephemeral scratch directory and returns one cited markdown report saved near the working directory. -- evidence: [README.md#L72-L82](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L72-L82) (`clm_b5a3c515f240c1b00522d67550c23f6c786bfb8c675f46126fd461653aaa01ad`)
- [observation/documented] Model overrides resolve from LITTLE_CODER_MODELS_FILE, XDG config, or ~/.config/little-coder/models.json, with provider-level full replacement rather than deep merge; base-URL env vars take precedence. -- evidence: [README.md#L204-L204](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L204-L204), [README.md#L200-L202](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L200-L202), [README.md#L266-L266](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L266-L266) (`clm_2f12b6a0e142666a8b84ea075846375078058067bf2b5955072552beba339218`)

## memory-state (1 claim(s))

- [observation/documented] Background jobs outlive a turn but not the session: they run in their own process group, are reaped on shutdown, and carry a watchdog that kills the group if little-coder's pid disappears. -- evidence: [README.md#L323-L323](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L323-L323) (`clm_649ede035a5382d279aabbe58ef0c8fd1bc9447aea1ea2316ee7b2bc97dc2c06`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Shell calls are gated against a built-in safe-prefix whitelist before pi's confirmation flow; rm and sudo are excluded, and LITTLE_CODER_BASH_ALLOW adds prefixes per deployment. -- evidence: [README.md#L345-L345](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L345-L345) (`clm_e91dc5eae3390e0b09056f77d137ac6333d38a0517c8ef6cbbaab84095a5d865`)
- [observation/documented] Every command in a chain is judged individually, and any shell write via redirects, tee, or dd of= is refused; LITTLE_CODER_PERMISSION_MODE offers auto, accept-all, and manual modes. -- evidence: [README.md#L349-L350](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L349-L350), [README.md#L356-L359](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L356-L359) (`clm_6b70715448dfe412c78f18c59a299169b75c1402dec1d394187c1a417e64abf0`)

## evaluation (1 claim(s))

- [observation/documented] Published results include Aider Polyglot 45.56% (Qwen3.5-9B) and 78.67% (Qwen3.6-35B-A3B), Terminal-Bench-Core 40.0%, Terminal-Bench 2.0 leaderboard 24.6%±3.2, and GAIA validation 40.00%, all on an 8 GB VRAM laptop with no cloud inference. -- evidence: [README.md#L377-L384](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L377-L384), [README.md#L386-L386](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L386-L386), [README.md#L394-L397](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L394-L397) (`clm_6eae57985efec0d87f8f20521e37212c48ba33a2d01ee70da2f97fa684fe0da5`)

## dependencies (1 claim(s))

- [observation/documented] Requires Node.js 22.19+; installable via a curl script, npm install -g, or bun, and the launcher is a Node script so Node must remain on PATH even when installed with bun. -- evidence: [README.md#L32-L34](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L32-L34), [README.md#L44-L44](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L44-L44), [README.md#L38-L40](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L38-L40), [README.md#L24-L24](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L24-L24), [README.md#L26-L28](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L26-L28) (`clm_571802fdf1548175cb5390dbb2a94c0d4733ad8a71d05a1b585d47718cc9d18d`)

## limitations (1 claim(s))

- [observation/documented] Without a vision projector (mmproj) on the llama.cpp server, image attachments are rejected with a 4xx, though text-only use still works. -- evidence: [README.md#L142-L142](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L142-L142), [README.md#L425-L425](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L425-L425) (`clm_e4ef3b41caa47b7d58c732c03f9b6383daf3ea49d75972dce7d45f25184e27b7`)

## relevance (1 claim(s))

- [observation/documented] The project targets coding agents for small local models on consumer laptops, with Phase 2 focused on operating large, messy markdown knowledge bases token-efficiently. -- evidence: [README.md#L403-L405](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L403-L405), [README.md#L401-L401](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L401-L401), [README.md#L6-L6](https://github.com/itayinbarr/little-coder/blob/a9e467f2be43b78441d723c84f173b98771b51ef/README.md#L6-L6) (`clm_e5dc8582abf328cc8f7666f6585d4704f093d9c7cc0cb6611d31726d874e4172`)

