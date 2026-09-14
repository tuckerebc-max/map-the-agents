# josephsenior/grinta-coding-agent -- full detail

[Back to orientation](grinta-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/josephsenior/grinta-coding-agent/918df240e0a5095f7171b6e72bb9b8c05dbc936d/3ff10eff6d798156.json](../../../wiki/dossiers/josephsenior/grinta-coding-agent/918df240e0a5095f7171b6e72bb9b8c05dbc936d/3ff10eff6d798156.json)

## specifications (2 claim(s))

- [observation/documented] Grinta is described as a local-first coding agent built to finish long, failure-prone software tasks, released under the MIT license and maintained by Youssef Mejdi. -- evidence: [README.md#L397-L398](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L397-L398), [README.md#L7-L9](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L7-L9) (`clm_04dbdf3064d0ed53717683a7f0a82219cd60aa6cfa784828b043d71e90b14348`)
- [observation/documented] The runtime targets Python 3.12 or 3.13, supports Linux, Windows, macOS, and WSL2, and the package metadata reports version 1.0.0. -- evidence: [README.md#L43-L52](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L43-L52), [docs/ARCHITECTURE.md#L242-L242](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L242-L242), [README.md#L308-L313](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L308-L313) (`clm_72a8c1f7689632e9ce04b446bfe238777e5fc2f82e756f19f061df714c8cbd70`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The architecture has four layers: interface (launcher, TUI, non-interactive runner), orchestration (planning, retries, finish validation), execution (local commands, files, tools), and durability (event stream and persisted state). -- evidence: [docs/ARCHITECTURE.md#L10-L13](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L10-L13), [README.md#L239-L246](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L239-L246) (`clm_1099654794c6eea5d9cde50bc7321254a9cd8302496c5da94d7cba3849c53752`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo and run a platform setup script (start_here.sh or START_HERE.ps1 on Windows), then run pre-commit on all files and unit tests via PYTHONPATH=. uv run pytest backend/tests/unit before opening a pull request. -- evidence: [README.md#L357-L361](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L357-L361), [README.md#L363-L365](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L363-L365), [README.md#L367-L367](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L367-L367), [README.md#L355-L355](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L355-L355), [README.md#L369-L372](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L369-L372) (`clm_9bc3daf3960e3112634b1072f816832e7c8391bfaba41bdfdbab81126441518d`)
- [observation/documented] Repository development practice: the project follows a maintainer-led governance model with a single lead maintainer holding release and merge authority, and best-effort review targets of 5 business days for bugs and 7 for pull requests. -- evidence: [MAINTAINERS.md#L3-L3](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L3-L3), [MAINTAINERS.md#L12-L14](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L12-L14), [MAINTAINERS.md#L16-L16](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L16-L16), [MAINTAINERS.md#L7-L8](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/MAINTAINERS.md#L7-L8), [GOVERNANCE.md#L5-L5](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/GOVERNANCE.md#L5-L5) (`clm_222d0bf6cd230f7fe798ed8f6fcc2f1d969ae90817f497cabe132ad021becac1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product offers a Textual terminal UI for TTY stdin and a non-interactive runner for piped input where each input line is one turn, plus slash commands like /mode, /model, /checkpoint, and /resume. -- evidence: [README.md#L43-L52](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L43-L52), [README.md#L190-L191](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L190-L191), [README.md#L164-L176](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L164-L176), [docs/ARCHITECTURE.md#L88-L89](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L88-L89) (`clm_79045bfc980a19397cbb57414993fee68a8dc3c38164ee897da41a368c9e7d31`)
- [observation/documented] CLI subcommands include grinta init, grinta doctor, grinta sessions list/show/export/prune, and flags such as --project, --model, --theme, --minimal, --accessible, and --cleanup-storage. -- evidence: [README.md#L103-L106](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L103-L106), [README.md#L180-L188](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L180-L188), [docs/ARCHITECTURE.md#L81-L84](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L81-L84) (`clm_310275175c08ec391624e5e55960d7e3bd01afe08009dc60debcbe1df68f534a`)

## memory-state (1 claim(s))

- [observation/documented] Sessions, event history, and checkpoints persist locally; workspace checkpoints use the standalone ShadowGit package writing content-addressed snapshots to a private object store without touching the user's .git. -- evidence: [README.md#L269-L272](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L269-L272), [docs/ARCHITECTURE.md#L217-L225](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L217-L225), [README.md#L259-L267](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L259-L267), [README.md#L19-L22](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L19-L22) (`clm_de969f704188b66dd746ba6381675ba1115903f4d5f997a56ca84ff4d91de802`)

## orchestration (2 claim(s))

- [observation/documented] A SessionOrchestrator coordinates focused services (retry, circuit breaker, stuck detection, task validation, state transitions) and runs actions through a middleware pipeline where safety checks execute first and telemetry last. -- evidence: [docs/ARCHITECTURE.md#L165-L165](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L165-L165), [README.md#L248-L252](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L248-L252), [docs/ARCHITECTURE.md#L108-L130](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L108-L130) (`clm_50fcd673989fdddb93625ad1a28efe99c2b4bc31e64122d28c774d638bfd504c`)
- [observation/documented] Errors are classified as recoverable or terminal; recoverable errors retry with backoff, while terminal errors emit an error observation and transition to an ERROR state. Public lifecycle states include RUNNING, RETRYING, RATE_LIMITED, FINISHED, and others. -- evidence: [docs/ARCHITECTURE.md#L179-L183](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L179-L183), [docs/ARCHITECTURE.md#L186-L190](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L186-L190) (`clm_0ae662a46b21eab9245fb2812159d268190ef2c8c1db1bf48ff875b359490756`)

## tools-permissions (2 claim(s))

- [observation/documented] Agent mode has three autonomy levels: conservative confirms shell commands, edits, MCP calls, and delegation; balanced (the default) confirms high-risk actions; full removes confirmation prompts while policy blocks still apply. -- evidence: [README.md#L149-L149](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L149-L149), [README.md#L151-L155](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L151-L155) (`clm_8ea3a48af0c2ba3540bf2ab8ac1ebe371ba550ba27570eaa758e21a7420f23fe`)
- [observation/documented] The sandboxed_local execution profile adds OS-native process-scoped isolation (bwrap, AppContainer, sandbox-exec) for supported non-interactive subprocess commands, but interactive PTY sessions stay outside that boundary and it is not a VM or host isolation. -- evidence: [README.md#L342-L347](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L342-L347), [docs/ARCHITECTURE.md#L19-L28](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/docs/ARCHITECTURE.md#L19-L28) (`clm_77148b411b4da0daa393e82964d948e18c9da30aa00ab5e782baac530a3c433e`)

## evaluation (1 claim(s))

- [observation/documented] The repository includes a headless adapter for the DeepSWE v1.1 benchmark that runs Grinta in an isolated task workspace, captures the patch and trajectory, and leaves pass/fail decisions to the benchmark verifier. -- evidence: [README.md#L328-L331](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L328-L331) (`clm_779361263f7a1e553499ad22f825ad495ceffe2a90d1d5e896b3b6b93c2c3fd8`)

## dependencies (2 claim(s))

- [observation/documented] Inference supports OpenAI, Anthropic, Google, OpenRouter and other gateways, OpenAI-compatible endpoints, and local servers via Ollama, LM Studio, or vLLM; an optional rag extra provides semantic retrieval. -- evidence: [README.md#L205-L208](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L205-L208), [README.md#L297-L297](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L297-L297), [README.md#L299-L301](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L299-L301) (`clm_62dd357b79cf35123c935e9a457f8ce1beccc7491cf8314bf89a0713281705a3`)
- [observation/documented] Recommended installation is via pipx to isolate Grinta from project dependencies; API keys can come from environment variables like OPENAI_API_KEY or GEMINI_API_KEY or Grinta's local configuration area. -- evidence: [README.md#L83-L84](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L83-L84), [README.md#L108-L112](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L108-L112) (`clm_b0b7a9800826d84ff1267d5b368ecb62cde65beadcd2205938034ca0b18dcc37`)

## limitations (1 claim(s))

- [observation/documented] Grinta runs commands with the local user's privileges; confirmation prompts, secret masking, workspace boundaries, and process isolation reduce risk but do not make hostile code safe, and the docs recommend a VM or container for untrusted repositories. -- evidence: [README.md#L338-L340](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L338-L340), [README.md#L342-L347](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L342-L347) (`clm_31ec52affa00f6538887dbaf8bc0196fcb029c46ba143b15e5eefdb097251ef8`)

## relevance (1 claim(s))

- [observation/documented] The project is relevant to autonomous long-horizon coding: it showcases a 4h33m autonomous run with 16,393 events reaching FINISHED, and a Raft key-value-store case study finishing with 39/39 tests passing. -- evidence: [README.md#L75-L77](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L75-L77), [README.md#L321-L324](https://github.com/josephsenior/Grinta-Coding-Agent/blob/918df240e0a5095f7171b6e72bb9b8c05dbc936d/README.md#L321-L324) (`clm_bb5cbebef58124f178713e20f77616379893195656d2be795d12b34bc554dd80`)

