---
access: public
aliases: []
claim_ids:
- clm_24110e2b6ad40a5cd2af708ac128f94a4a5bae1af4fa4efac8baad657674fe23
- clm_25dd500618bdf9c53eed6ddee81deb65f1144c1e92316b5ec196b0d98078cb12
- clm_3384f6bcccb3fa09eb73342374d7bdfbc47ba7a8d4164f73e8c3cbe46e33f00a
- clm_6f11fd89a42681307162b5c49ae13be88edc20ffa484b3ec19b317872ae998b8
- clm_8efb349f183f7a88b30698147b76889477a25266e95b93eebd58a1c52ab6d5ab
- clm_a60d9b8df125f915071f46ee77c9a72d03a0cd71c2f08d1ab737307e826949ec
- clm_a78d355f451c898cb1b42259bbf50d5956c3c621ed442ee069d272bb62380ab4
- clm_b540b14b26731fc78f268047b0f98ffa3f28a27522217ded9e76c74a5d059e2c
- clm_b953ac8cec4e233459c51d230c5ab4c1dec89403aa6f1654a8472c6822fb2d8b
- clm_cd29cd1d6a68a4dfdc276cb6a7ec06cc2f9a19a40599417d5974e2509b806e31
- clm_d8d853376968fb336d714ae6a88d4643fd4b555ef3055ef54406398506ee49bd
maturity: draft
page_id: pg_e1fd3bc7736b5c72bebff35acb23221b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_792f0e2b9dc8533d90a9adb9f0b97f95
title: 2389-research/breakaway-agent/README.md @ a426c399d50f
updated_at: '2026-09-14T01:25:59Z'
---

# 2389-research/breakaway-agent/README.md @ a426c399d50f

<!-- rcw:begin owner=source:src_792f0e2b9dc8533d90a9adb9f0b97f95 block=evidence -->
- The agent supports self-modification: editing tools.ts, policy.ts, or system.txt then SIGHUP or /reload hot-reloads via cache-busted dynamic import, while SIGUSR2 or /restart exits with code 42 so a wrapper relaunches it (up to 20 times). [@claim:clm_24110e2b6ad40a5cd2af708ac128f94a4a5bae1af4fa4efac8baad657674fe23]
- spawn_agent launches child agents whose stdout/stderr go to spawn-<ts> files; nesting depth is tracked via BREAK_AWAY_DEPTH and capped by BREAK_AWAY_MAX_DEPTH (default 3), returning an error at the cap. [@claim:clm_25dd500618bdf9c53eed6ddee81deb65f1144c1e92316b5ec196b0d98078cb12]
- The agent runs one-shot with a task argument or as an interactive REPL; in one-shot mode only the final answer goes to stdout so output can be piped cleanly. [@claim:clm_3384f6bcccb3fa09eb73342374d7bdfbc47ba7a8d4164f73e8c3cbe46e33f00a]
- The agent runs with no permission prompts, sandboxing, or confirmation dialogs; it executes arbitrary shell commands the model requests, so the README advises running it in a throwaway environment. [@claim:clm_6f11fd89a42681307162b5c49ae13be88edc20ffa484b3ec19b317872ae998b8]
- Each run writes a JSONL transcript to .transcripts/ (or $BREAK_AWAY_TRANSCRIPT_DIR), one file per run. [@claim:clm_8efb349f183f7a88b30698147b76889477a25266e95b93eebd58a1c52ab6d5ab]
- The core agent loop is described as policy-blind: all behavior is injected through a Policy object, and the run() loop in src/agent.ts is roughly 165 lines. [@claim:clm_a60d9b8df125f915071f46ee77c9a72d03a0cd71c2f08d1ab737307e826949ec]
- In the compiled binary, self-modification and hot-reload do not work: SIGHUP warns instead of reloading and /reload reports failure, since the binary is a frozen snapshot; rebuilding is required. [@claim:clm_a78d355f451c898cb1b42259bbf50d5956c3c621ed442ee069d272bb62380ab4]
- The model drives five tools: read_file with paged line-window reads, write_file, atomic single-occurrence edit_file, bash with process-group timeout kill and 8000-char output cap, and spawn_agent. [@claim:clm_b540b14b26731fc78f268047b0f98ffa3f28a27522217ded9e76c74a5d059e2c]
- CLI flags include --cwd, --model, --system, --serious (long-horizon profile with retries, error nudging, and a completion audit), --max-turns, --quiet, --debug, and --help. [@claim:clm_b953ac8cec4e233459c51d230c5ab4c1dec89403aa6f1654a8472c6822fb2d8b]
- The project targets Bun (bun install, bun src/index.ts, bun build --compile producing a ~61 MB self-contained binary); the plan lists Bun 1.3.14 and TypeScript as the tech stack. [@claim:clm_cd29cd1d6a68a4dfdc276cb6a7ec06cc2f9a19a40599417d5974e2509b806e31]
- An agents.jsonl registry records spawn, start, and done events across parent and child agents, and done records carry status (ok/error) and stop_reason. [@claim:clm_d8d853376968fb336d714ae6a88d4643fd4b555ef3055ef54406398506ee49bd]
<!-- rcw:end owner=source:src_792f0e2b9dc8533d90a9adb9f0b97f95 block=evidence -->

## Researcher notes

