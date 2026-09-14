# 2389-research/breakaway-agent -- full detail

[Back to orientation](breakaway-agent.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/breakaway-agent/a426c399d50f8a478752a1beb776a3eb264c2b70/fa31829804eca3a3.json](../../../wiki/dossiers/2389-research/breakaway-agent/a426c399d50f8a478752a1beb776a3eb264c2b70/fa31829804eca3a3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The core agent loop is described as policy-blind: all behavior is injected through a Policy object, and the run() loop in src/agent.ts is roughly 165 lines. -- evidence: [README.md#L72-L72](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L72-L72) (`clm_a60d9b8df125f915071f46ee77c9a72d03a0cd71c2f08d1ab737307e826949ec`)
- [observation/documented] The agent supports self-modification: editing tools.ts, policy.ts, or system.txt then SIGHUP or /reload hot-reloads via cache-busted dynamic import, while SIGUSR2 or /restart exits with code 42 so a wrapper relaunches it (up to 20 times). -- evidence: [README.md#L80-L80](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L80-L80), [README.md#L82-L87](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L82-L87), [README.md#L78-L78](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L78-L78) (`clm_24110e2b6ad40a5cd2af708ac128f94a4a5bae1af4fa4efac8baad657674fe23`)
- [observation/documented] The plan's architecture detects compiled-binary mode via import.meta.dir starting with /$bunfs/, redirecting system prompt, transcripts, and spawn commands to writable paths while leaving source mode untouched. -- evidence: [docs/superpowers/plans/2026-08-30-first-class-binary.md#L7-L7](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L7-L7), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L35-L35](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L35-L35) (`clm_1c8c7de48fd125368cd9eb1d20e7d8bb28a1094fc3e217e006d9487a1efc8cf4`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the implementation plan mandates TDD (write failing test, verify failure, implement, verify pass), conventional commits with a Claude-Session trailer, bun test staying green (80+ tests), no mocks of own code, stdout purity, and .env never committed or printed. -- evidence: [docs/superpowers/plans/2026-08-30-first-class-binary.md#L15-L22](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L15-L22), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L37-L37](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L37-L37), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L56-L56](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L56-L56), [docs/superpowers/plans/2026-08-30-first-class-binary.md#L73-L73](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L73-L73) (`clm_def100601a9493d34fb9b469aae6b38d92d41ab5fea815d780066a84f748203d`)
- [observation/documented] Repository development practice: the plan document instructs agentic workers to use superpowers:subagent-driven-development or superpowers:executing-plans to implement tasks with checkbox tracking. -- evidence: [docs/superpowers/plans/2026-08-30-first-class-binary.md#L3-L3](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L3-L3) (`clm_e067d5adb55ab124b76bb7a40a282b8115fe72135021c5ba8a824b36a6bbe04f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The model drives five tools: read_file with paged line-window reads, write_file, atomic single-occurrence edit_file, bash with process-group timeout kill and 8000-char output cap, and spawn_agent. -- evidence: [README.md#L55-L60](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L55-L60) (`clm_b540b14b26731fc78f268047b0f98ffa3f28a27522217ded9e76c74a5d059e2c`)
- [observation/documented] CLI flags include --cwd, --model, --system, --serious (long-horizon profile with retries, error nudging, and a completion audit), --max-turns, --quiet, --debug, and --help. -- evidence: [README.md#L29-L42](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L29-L42) (`clm_b953ac8cec4e233459c51d230c5ab4c1dec89403aa6f1654a8472c6822fb2d8b`)
- [observation/documented] The agent runs one-shot with a task argument or as an interactive REPL; in one-shot mode only the final answer goes to stdout so output can be piped cleanly. -- evidence: [README.md#L44-L47](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L44-L47), [README.md#L24-L27](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L24-L27), [README.md#L19-L22](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L19-L22) (`clm_3384f6bcccb3fa09eb73342374d7bdfbc47ba7a8d4164f73e8c3cbe46e33f00a`)

## memory-state (1 claim(s))

- [observation/documented] Each run writes a JSONL transcript to .transcripts/ (or $BREAK_AWAY_TRANSCRIPT_DIR), one file per run. -- evidence: [README.md#L49-L49](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L49-L49) (`clm_8efb349f183f7a88b30698147b76889477a25266e95b93eebd58a1c52ab6d5ab`)

## orchestration (2 claim(s))

- [observation/documented] spawn_agent launches child agents whose stdout/stderr go to spawn-<ts> files; nesting depth is tracked via BREAK_AWAY_DEPTH and capped by BREAK_AWAY_MAX_DEPTH (default 3), returning an error at the cap. -- evidence: [README.md#L99-L99](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L99-L99), [README.md#L97-L97](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L97-L97) (`clm_25dd500618bdf9c53eed6ddee81deb65f1144c1e92316b5ec196b0d98078cb12`)
- [observation/documented] An agents.jsonl registry records spawn, start, and done events across parent and child agents, and done records carry status (ok/error) and stop_reason. -- evidence: [README.md#L110-L110](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L110-L110), [README.md#L101-L101](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L101-L101) (`clm_d8d853376968fb336d714ae6a88d4643fd4b555ef3055ef54406398506ee49bd`)

## tools-permissions (1 claim(s))

- [observation/documented] The agent runs with no permission prompts, sandboxing, or confirmation dialogs; it executes arbitrary shell commands the model requests, so the README advises running it in a throwaway environment. -- evidence: [README.md#L7-L7](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L7-L7) (`clm_6f11fd89a42681307162b5c49ae13be88edc20ffa484b3ec19b317872ae998b8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project targets Bun (bun install, bun src/index.ts, bun build --compile producing a ~61 MB self-contained binary); the plan lists Bun 1.3.14 and TypeScript as the tech stack. -- evidence: [docs/superpowers/plans/2026-08-30-first-class-binary.md#L9-L9](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/docs/superpowers/plans/2026-08-30-first-class-binary.md#L9-L9), [README.md#L14-L15](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L14-L15), [README.md#L128-L128](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L128-L128), [README.md#L19-L22](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L19-L22) (`clm_cd29cd1d6a68a4dfdc276cb6a7ec06cc2f9a19a40599417d5974e2509b806e31`)

## limitations (1 claim(s))

- [observation/documented] In the compiled binary, self-modification and hot-reload do not work: SIGHUP warns instead of reloading and /reload reports failure, since the binary is a frozen snapshot; rebuilding is required. -- evidence: [README.md#L139-L141](https://github.com/2389-research/breakaway-agent/blob/a426c399d50f8a478752a1beb776a3eb264c2b70/README.md#L139-L141) (`clm_a78d355f451c898cb1b42259bbf50d5956c3c621ed442ee069d272bb62380ab4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

