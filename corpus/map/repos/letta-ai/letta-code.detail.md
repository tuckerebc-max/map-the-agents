# letta-ai/letta-code -- full detail

[Back to orientation](letta-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/letta-ai/letta-code/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/28b1a65f09718697.json](../../../wiki/dossiers/letta-ai/letta-code/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/28b1a65f09718697.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The example memory-citations mod is intentionally conservative: it observes memory paths passed to tools at tool_start (before execution), not successful reads, and marks shell-command matches as medium confidence. -- evidence: [docs/examples/mods/README.md#L12-L16](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L12-L16), [docs/examples/mods/README.md#L18-L20](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L18-L20) (`clm_620c8ca987a08b92188ef8ac08e403edde0b3af25f50a365292b8282f0657b16`)
- [observation/documented] The /mods learn TUI command never auto-installs learned mods; users must review the generated candidate before copying it into their mod directory and running /reload. -- evidence: [docs/examples/mods/README.md#L46-L49](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L46-L49) (`clm_d338eb607bc396e4231717c3d02b0f41570d497fda647f9a6755aa95951af61e`)
- [observation/documented] A plan document specifies a bounded resume-tail fast path for boot/resume, with a backend getConversationResumeTail operation returning messages and pending approvals, and forbids conversation enumeration during normal boot. -- evidence: [docs/plans/resume-tail-fast-path.md#L28-L30](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/plans/resume-tail-fast-path.md#L28-L30), [docs/plans/resume-tail-fast-path.md#L34-L38](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/plans/resume-tail-fast-path.md#L34-L38), [docs/plans/resume-tail-fast-path.md#L25-L26](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/plans/resume-tail-fast-path.md#L25-L26), [docs/plans/resume-tail-fast-path.md#L19-L23](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/plans/resume-tail-fast-path.md#L19-L23), [docs/plans/resume-tail-fast-path.md#L7-L11](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/plans/resume-tail-fast-path.md#L7-L11) (`clm_a5af5e66f9b7ec630cf5849be87015b824226d2caa4e8cb36fafeda8d6bc02b6`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the AI policy requires contributors to disclose all AI tool usage in issues and PRs, select an authorship option, include a human-verification phrase, and noncompliant submissions are automatically closed. -- evidence: [AI_POLICY.md#L19-L22](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L19-L22), [AI_POLICY.md#L24-L24](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L24-L24), [AI_POLICY.md#L5-L5](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L5-L5), [AI_POLICY.md#L9-L13](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/AI_POLICY.md#L9-L13) (`clm_6f011801553da56d6b80491e324532f5200cd8f9bd91899cd26b9947f402a5a2`)
- [observation/documented] Repository development practice: when bun.lock changes, contributors should regenerate the Nix dependency expression with `bunx bun2nix -o bun.nix` before opening a PR. -- evidence: [docs/nix.md#L97-L97](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/nix.md#L97-L97), [docs/nix.md#L99-L101](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/nix.md#L99-L101) (`clm_1ba4043fccbf2bdf6d064a5540ce7a058466779ebd05a22fef6a4318d49c4156`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills load from global (~/.letta), project-scoped (.agents/skills), and agent-scoped (MemFS) locations, and can be installed from GitHub, ClawHub, or Hermes Skills Hub with `letta skills install`. -- evidence: [README.md#L103-L107](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L103-L107), [README.md#L101-L101](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L101-L101), [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32) (`clm_aa91f3cd8e00f1038f0642b4ddad49270ffd46eff271899f42bb88928a5560ef`)

## interfaces (3 claim(s))

- [observation/documented] Letta Code is distributed as the npm package @letta-ai/letta-code, installed globally via npm, and run with the `letta` command in a project directory. -- evidence: [README.md#L40-L42](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L40-L42), [README.md#L38-L38](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L38-L38), [README.md#L3-L3](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L3-L3), [README.md#L44-L47](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L44-L47) (`clm_88f8897dcdd82b2bc128f44a6edd2889a2dd609032981ea5f72c689fa5a80245`)
- [observation/documented] Agents can be interacted with through a local CLI, a desktop app for macOS/Windows/Linux, a browser client at chat.letta.com, and messaging integrations such as Telegram, Slack, and Discord. -- evidence: [README.md#L7-L11](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L7-L11) (`clm_0bdf3ad755279b20dc2cdf76e202c766c339f8fc0c6fa68dc16d3896c4140f43`)
- [observation/documented] The CLI exposes slash commands including /sleeptime, /doctor, /palace, /search, /memory-repository, /skills, /skill-creator, /connect, /model, and /login. -- evidence: [README.md#L49-L49](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L49-L49), [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32), [README.md#L66-L66](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L66-L66) (`clm_485351eacc6c4c9e5178ec7a259199c840e61270f7b49d3e2e77bd77589f06ee`)

## memory-state (2 claim(s))

- [observation/documented] Agent context, including memory blocks, is tracked via git under MemFS and can be synced to a user's GitHub repository via /memory-repository set. -- evidence: [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32) (`clm_2929c9a941b9b177a2c2b23d466b31633afe5495aaf8d48cc5275ed311070e6d`)
- [observation/documented] Agents rewrite their own context over time, including system-prompt learning via memory blocks and skill learning, with periodic 'dreaming' configurable via /sleeptime. -- evidence: [README.md#L5-L5](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L5-L5), [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32) (`clm_150b395f7f29843d07ce5140d29260b0aef513ddfb0c2c63729c720cad005f29`)

## orchestration (2 claim(s))

- [observation/documented] Built-in subagents (general-purpose, forked, recall, history-analyzer) can run in the background, and agents can call any other agent, including themselves, as subagents. -- evidence: [README.md#L20-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L20-L32) (`clm_826b4ab57436728791fd3e246da44a122d50fc6f270597566eff4b816809111f`)
- [observation/documented] Cloud-stored agents can run on multiple machines: `letta server --computer-name` registers a computer, `letta computers list/current` manage routing, and `--computer` routes headless messages to a specific machine or the cloud sandbox. -- evidence: [README.md#L55-L55](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L55-L55), [README.md#L69-L88](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L69-L88) (`clm_f0b286b5159d06786ef6d6efc694c78ef59c848b171f22134e16fd8ccb31ab93`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A mod-learning harness (scripts/mod-learning/learn-mod.ts) runs a headless agent to generate a candidate mod, then a second headless eval with LETTA_MODS_DIR pointed at it, saving prompts, output, and a pass/fail report under .letta/mod-learning-runs/. -- evidence: [docs/examples/mods/README.md#L24-L25](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L24-L25), [docs/examples/mods/README.md#L27-L32](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/examples/mods/README.md#L27-L32) (`clm_ba1bf2a9771b6650f3912fdcc2dbfb5ac4a52bf4f56f82ec7c51dea906a1bfb4`)

## dependencies (1 claim(s))

- [observation/documented] The Nix flake builds the CLI with Bun; dependency resolution is driven by the checked-in bun.lock, with a generated bun.nix enabling reproducible offline Nix builds. -- evidence: [docs/nix.md#L95-L95](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/docs/nix.md#L95-L95) (`clm_af2163f126c36bc2be5d465fe8af34f4edb0309259661cdc66ca2d5ac18b6c25`)

## limitations (1 claim(s))

- [observation/documented] AgentFile (.af) export/import has been removed: /export, /download, --import, and --from-af are no longer supported, though memory and transcript export are unaffected. -- evidence: [README.md#L95-L95](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L95-L95), [README.md#L97-L97](https://github.com/letta-ai/letta-code/blob/f2bd2392a8241d7f2a8eac48cdc067b2c488571e/README.md#L97-L97) (`clm_471bc2006d66076d78180ecdd35f562327cd33eea584472c90ba5205c8beca48`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

