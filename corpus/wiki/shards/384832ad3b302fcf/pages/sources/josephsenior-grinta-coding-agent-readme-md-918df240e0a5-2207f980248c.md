---
access: public
aliases: []
claim_ids:
- clm_04dbdf3064d0ed53717683a7f0a82219cd60aa6cfa784828b043d71e90b14348
- clm_1099654794c6eea5d9cde50bc7321254a9cd8302496c5da94d7cba3849c53752
- clm_310275175c08ec391624e5e55960d7e3bd01afe08009dc60debcbe1df68f534a
- clm_31ec52affa00f6538887dbaf8bc0196fcb029c46ba143b15e5eefdb097251ef8
- clm_50fcd673989fdddb93625ad1a28efe99c2b4bc31e64122d28c774d638bfd504c
- clm_62dd357b79cf35123c935e9a457f8ce1beccc7491cf8314bf89a0713281705a3
- clm_72a8c1f7689632e9ce04b446bfe238777e5fc2f82e756f19f061df714c8cbd70
- clm_77148b411b4da0daa393e82964d948e18c9da30aa00ab5e782baac530a3c433e
- clm_779361263f7a1e553499ad22f825ad495ceffe2a90d1d5e896b3b6b93c2c3fd8
- clm_79045bfc980a19397cbb57414993fee68a8dc3c38164ee897da41a368c9e7d31
- clm_8ea3a48af0c2ba3540bf2ab8ac1ebe371ba550ba27570eaa758e21a7420f23fe
- clm_9bc3daf3960e3112634b1072f816832e7c8391bfaba41bdfdbab81126441518d
- clm_b0b7a9800826d84ff1267d5b368ecb62cde65beadcd2205938034ca0b18dcc37
- clm_bb5cbebef58124f178713e20f77616379893195656d2be795d12b34bc554dd80
- clm_de969f704188b66dd746ba6381675ba1115903f4d5f997a56ca84ff4d91de802
maturity: draft
page_id: pg_13d0dfc55ad553d397fe2207f980248c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_768fbe73690e547b8ff3d5f281258758
title: josephsenior/Grinta-Coding-Agent/README.md @ 918df240e0a5
updated_at: '2026-09-14T02:08:06Z'
---

# josephsenior/Grinta-Coding-Agent/README.md @ 918df240e0a5

<!-- rcw:begin owner=source:src_768fbe73690e547b8ff3d5f281258758 block=evidence -->
- Grinta is described as a local-first coding agent built to finish long, failure-prone software tasks, released under the MIT license and maintained by Youssef Mejdi. [@claim:clm_04dbdf3064d0ed53717683a7f0a82219cd60aa6cfa784828b043d71e90b14348]
- The architecture has four layers: interface (launcher, TUI, non-interactive runner), orchestration (planning, retries, finish validation), execution (local commands, files, tools), and durability (event stream and persisted state). [@claim:clm_1099654794c6eea5d9cde50bc7321254a9cd8302496c5da94d7cba3849c53752]
- CLI subcommands include grinta init, grinta doctor, grinta sessions list/show/export/prune, and flags such as --project, --model, --theme, --minimal, --accessible, and --cleanup-storage. [@claim:clm_310275175c08ec391624e5e55960d7e3bd01afe08009dc60debcbe1df68f534a]
- Grinta runs commands with the local user's privileges; confirmation prompts, secret masking, workspace boundaries, and process isolation reduce risk but do not make hostile code safe, and the docs recommend a VM or container for untrusted repositories. [@claim:clm_31ec52affa00f6538887dbaf8bc0196fcb029c46ba143b15e5eefdb097251ef8]
- A SessionOrchestrator coordinates focused services (retry, circuit breaker, stuck detection, task validation, state transitions) and runs actions through a middleware pipeline where safety checks execute first and telemetry last. [@claim:clm_50fcd673989fdddb93625ad1a28efe99c2b4bc31e64122d28c774d638bfd504c]
- Inference supports OpenAI, Anthropic, Google, OpenRouter and other gateways, OpenAI-compatible endpoints, and local servers via Ollama, LM Studio, or vLLM; an optional rag extra provides semantic retrieval. [@claim:clm_62dd357b79cf35123c935e9a457f8ce1beccc7491cf8314bf89a0713281705a3]
- The runtime targets Python 3.12 or 3.13, supports Linux, Windows, macOS, and WSL2, and the package metadata reports version 1.0.0. [@claim:clm_72a8c1f7689632e9ce04b446bfe238777e5fc2f82e756f19f061df714c8cbd70]
- The sandboxed_local execution profile adds OS-native process-scoped isolation (bwrap, AppContainer, sandbox-exec) for supported non-interactive subprocess commands, but interactive PTY sessions stay outside that boundary and it is not a VM or host isolation. [@claim:clm_77148b411b4da0daa393e82964d948e18c9da30aa00ab5e782baac530a3c433e]
- The repository includes a headless adapter for the DeepSWE v1.1 benchmark that runs Grinta in an isolated task workspace, captures the patch and trajectory, and leaves pass/fail decisions to the benchmark verifier. [@claim:clm_779361263f7a1e553499ad22f825ad495ceffe2a90d1d5e896b3b6b93c2c3fd8]
- The product offers a Textual terminal UI for TTY stdin and a non-interactive runner for piped input where each input line is one turn, plus slash commands like /mode, /model, /checkpoint, and /resume. [@claim:clm_79045bfc980a19397cbb57414993fee68a8dc3c38164ee897da41a368c9e7d31]
- Agent mode has three autonomy levels: conservative confirms shell commands, edits, MCP calls, and delegation; balanced (the default) confirms high-risk actions; full removes confirmation prompts while policy blocks still apply. [@claim:clm_8ea3a48af0c2ba3540bf2ab8ac1ebe371ba550ba27570eaa758e21a7420f23fe]
- Repository development practice: contributors clone the repo and run a platform setup script (start_here.sh or START_HERE.ps1 on Windows), then run pre-commit on all files and unit tests via PYTHONPATH=. uv run pytest backend/tests/unit before opening a pull request. [@claim:clm_9bc3daf3960e3112634b1072f816832e7c8391bfaba41bdfdbab81126441518d]
- Recommended installation is via pipx to isolate Grinta from project dependencies; API keys can come from environment variables like OPENAI_API_KEY or GEMINI_API_KEY or Grinta's local configuration area. [@claim:clm_b0b7a9800826d84ff1267d5b368ecb62cde65beadcd2205938034ca0b18dcc37]
- The project is relevant to autonomous long-horizon coding: it showcases a 4h33m autonomous run with 16,393 events reaching FINISHED, and a Raft key-value-store case study finishing with 39/39 tests passing. [@claim:clm_bb5cbebef58124f178713e20f77616379893195656d2be795d12b34bc554dd80]
- Sessions, event history, and checkpoints persist locally; workspace checkpoints use the standalone ShadowGit package writing content-addressed snapshots to a private object store without touching the user's .git. [@claim:clm_de969f704188b66dd746ba6381675ba1115903f4d5f997a56ca84ff4d91de802]
<!-- rcw:end owner=source:src_768fbe73690e547b8ff3d5f281258758 block=evidence -->

## Researcher notes

