---
access: public
aliases: []
claim_ids:
- clm_25363152c452bf19e2efff6645efd956dda603d3d67890705a6b148a13fcd562
- clm_374016996a4d2382d1e3d0ccb3ea5e011050353cd60b43d2faaeae96b0922d3e
- clm_3a041c22429b3f898fc6663f9bc8f495341370d26bd4840f4a588de114d90462
- clm_53902dd8776d89510703a7dd1bda9b61368e18f63af2b5d7f0d973d4b3f1227e
- clm_6340f4b40d39a6ebae702045c6865b9f3c824e9d12c7a3187aa4d03d2a2d2b74
- clm_66878d1f6fee583094ae9c6151f3dcb479e003a46bb4700ec648826b1c1bc992
- clm_7652b0d38c95dc1984745935570a94ebeb6206f5bdb5552daeb71599207824ba
- clm_79168ca2e27fe6ccb120922c70890011ca9f3f9a5ac7a19e6bd2f456999f5418
- clm_7e43de4b7fb7ca21bff6665ba8ea2333da2ead8c78ccaeb2df3cc93f6c3fa145
- clm_89193ffc48b5cc932f30f17491e81c404bdadc81f538f16036743e039e7772da
- clm_93c86f2ea07832d91898efac8f6deadeda74daf039e17593bae5f99b0781601c
- clm_c79820599b47901ecaf86d19b08f1f1c08c90782a6a2f78dfbac736a84f7524f
- clm_cd8e59df63c9985e56a68be3ab6edab7b4cb77583fa2d97b90df7199eaa7da93
- clm_d3a4e56397ed1074775915d9272892e82c7c6af80c816538cf40010a0dab808c
- clm_dad4471422640d70dc5d7332b0f51f110adc65e0dda3e27001cd915b2706cf6c
- clm_f35e9bc0609b7279d2048abd6c2481ca26394699048b8a75c0409ec6b2f67234
maturity: draft
page_id: pg_7aef969701a7506eb7279896943679b9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9226b8c15a4055bc9ff0c9e30ea8324a
title: agentforce314/clawcodex/README.md @ 4706a57fc29f
updated_at: '2026-09-14T01:59:12Z'
---

# agentforce314/clawcodex/README.md @ 4706a57fc29f

<!-- rcw:begin owner=source:src_9226b8c15a4055bc9ff0c9e30ea8324a block=evidence -->
- clawcodex web serves the same agent in a browser at 127.0.0.1:8081 by default, mounting the web bundle on the serve process rather than running a second server, and binds loopback unless --allow-remote is passed. [@claim:clm_25363152c452bf19e2efff6645efd956dda603d3d67890705a6b148a13fcd562]
- The /eco mode compresses model-bound Bash output with deterministic filters (failure-focused summaries, ceremony stripping, dedup, head-caps), discards any compression not better than the raw rendering, and tees lossy output to disk with a recovery hint. [@claim:clm_374016996a4d2382d1e3d0ccb3ea5e011050353cd60b43d2faaeae96b0922d3e]
- Requests keep a byte-stable prefix so DeepSeek's prompt cache covers system, tools, and history across turns; /cost is stated to follow DeepSeek's peak/off-peak pricing schedule. [@claim:clm_3a041c22429b3f898fc6663f9bc8f495341370d26bd4840f4a588de114d90462]
- An /eco benchmark replayed 27 real captured command outputs through the production pipeline, measuring 92,989 to 17,767 tokens (-80%) with tiktoken cl100k_base counting; reproduction scripts are provided under eval/eco. [@claim:clm_53902dd8776d89510703a7dd1bda9b61368e18f63af2b5d7f0d973d4b3f1227e]
- The README marks MCP support as partial: tools are wired but the full client/runtime is still evolving, and roadmap phases 3-4 are in progress with phase 5 pending. [@claim:clm_6340f4b40d39a6ebae702045c6865b9f3c824e9d12c7a3187aa4d03d2a2d2b74]
- Repo-shipped .clawcodex/settings.json may only set defaultMode to default or dontAsk, and is ignored if looser than what would otherwise apply; administrators can disable Full Access via config or managed policy. [@claim:clm_66878d1f6fee583094ae9c6151f3dcb479e003a46bb4700ec648826b1c1bc992]
- Skills are markdown SKILL.md slash commands with front matter supporting descriptions, allowed-tools limits, and named arguments, available at project and user scope. [@claim:clm_7652b0d38c95dc1984745935570a94ebeb6206f5bdb5552daeb71599207824ba]
- Headless -p runs default to the 'default' permission mode; a saved Full Access setting dials headless down rather than up, and --dangerously-skip-permissions or --permission-mode can override per run. [@claim:clm_79168ca2e27fe6ccb120922c70890011ca9f3f9a5ac7a19e6bd2f456999f5418]
- A native desktop app (clawcodex desktop) shares the same backend, config, and session store as the CLI/TUI, booting its own backend via clawcodex serve with loopback HTTP and WebSocket gateway. [@claim:clm_7e43de4b7fb7ca21bff6665ba8ea2333da2ead8c78ccaeb2df3cc93f6c3fa145]
- The product exposes a CLI with subcommands including tui, web, login, logout, config, and --version, plus a headless -p/--print mode for non-interactive runs. [@claim:clm_89193ffc48b5cc932f30f17491e81c404bdadc81f538f16036743e039e7772da]
- Interactive sessions start in Full Access by default; /permissions offers Ask-for-approval, Approve-for-me, and Full Access levels, saved to permissions.defaultMode in ~/.clawcodex/settings.json. [@claim:clm_93c86f2ea07832d91898efac8f6deadeda74daf039e17593bae5f99b0781601c]
- Headless runs support --output-format json and stream-json output with stream-json input, plus per-run overrides like --provider, --model, --max-turns, and --allowed-tools. [@claim:clm_c79820599b47901ecaf86d19b08f1f1c08c90782a6a2f78dfbac736a84f7524f]
- The interactive UI is a TypeScript Ink TUI that spawns a Python agent-server child and communicates over an NDJSON pipe; running clawcodex with no mode flags launches it. [@claim:clm_cd8e59df63c9985e56a68be3ab6edab7b4cb77583fa2d97b90df7199eaa7da93]
- The tool system implements file operations (Read/Write/Edit/Glob/Grep), Bash, WebFetch/WebSearch, task management, agent tools, and configuration tools; MCP tools are wired but the full client/runtime is still evolving. [@claim:clm_d3a4e56397ed1074775915d9272892e82c7c6af80c816538cf40010a0dab808c]
- The runtime targets Python 3.10+ and lists roughly 30 LLM providers including native formats (Anthropic, DeepSeek, Gemini, OpenAI), OpenAI-compatible vendors, and local servers (Ollama, vLLM, SGLang) requiring no API key. [@claim:clm_dad4471422640d70dc5d7332b0f51f110adc65e0dda3e27001cd915b2706cf6c]
- The WebSearch tool requires a Tavily API key (TAVILY_API_KEY), configurable in the env block of ~/.clawcodex/config.json. [@claim:clm_f35e9bc0609b7279d2048abd6c2481ca26394699048b8a75c0409ec6b2f67234]
<!-- rcw:end owner=source:src_9226b8c15a4055bc9ff0c9e30ea8324a block=evidence -->

## Researcher notes

