# nano-collective/nanocoder -- full detail

[Back to orientation](nanocoder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nano-collective/nanocoder/0cb0afb026efaad90a62a64020866adb4fb21244/2d433bc2d82c310f.json](../../../wiki/dossiers/nano-collective/nanocoder/0cb0afb026efaad90a62a64020866adb4fb21244/2d433bc2d82c310f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The agent supports 20+ providers: native cloud integrations (e.g. Anthropic, OpenAI, Google Gemini, OpenRouter, Copilot, Mistral, Z.ai), seven documented local servers (Ollama, llama.cpp, llama-swap, LM Studio, LocalAI, MLX Server, vLLM), and any custom OpenAI-compatible endpoint. -- evidence: [docs/battlemap.md#L69-L71](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L69-L71) (`clm_873b896b0447d5efebc617f6830390d175fce36af2e3cea7443697f22e23b3fc`)

## design-choices (2 claim(s))

- [observation/documented] Stated design principles are zero telemetry, zero tracking, and local-first operation, with the whole loop able to run on-machine against local models with no outbound network traffic. -- evidence: [docs/battlemap.md#L173-L173](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L173-L173), [docs/battlemap.md#L21-L23](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L21-L23) (`clm_cccb0f6569f54d2856c1eef97db14aa5f0b59343e7526222882d431d4e560744`)
- [observation/documented] Tool calling uses three paths: native function calling plus XML and JSON fallbacks, with malformed-output repair on both fallback paths so weaker or non-conforming models still work end to end. -- evidence: [docs/battlemap.md#L189-L189](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L189-L189) (`clm_05adf1dbd5acc75a3ba51bffc8cfb4f07e4c07f801645595fc3e82a593b95ca5`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README directs contributors to CONTRIBUTING.md for development setup and guidelines, and notes shared conventions, tests, and release standards across Nano Collective projects. -- evidence: [README.md#L77-L77](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L77-L77), [README.md#L104-L107](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L104-L107) (`clm_6c5797fb6476e38bb5902669a8714e99dfcbced31260c20a754a8531d4e1a297`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI accepts --provider and --model flags in both interactive form and with a non-interactive 'run' subcommand, and flags may appear before or after the run subcommand. -- evidence: [README.md#L39-L39](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L39-L39), [README.md#L42-L42](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L42-L42), [README.md#L45-L45](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L45-L45) (`clm_c6fe79bbc9dcfc62600f9109ca921e0529d802a4e30a427bb689801bd1ca7162`)
- [observation/documented] A starting development mode can be selected at launch via --mode; documented examples include yolo and plan modes. -- evidence: [README.md#L48-L49](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L48-L49) (`clm_0715cc6329213e55f2e1d03b6342c2fbcc8a4afca6a270b14c5eede9410d3c69`)
- [observation/documented] Two rendering modes exist: a fullscreen alternate-screen layout with in-app scrolling (default, with a --mouse toggle) and an inline mode via --no-alt-screen or an "alternateScreen": false preference that prints into the terminal's native scrollback. -- evidence: [README.md#L59-L60](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L59-L60) (`clm_531f376dbad83d0cc191fdb0cecddc3f0eaf0505704832b1ac1578f717ef87d3`)
- [observation/documented] Nanocoder can run as an Agent Client Protocol agent via 'nanocoder --acp', exposing conversation, tool-calling, and permission flows to ACP-compatible editors such as Zed. -- evidence: [docs/battlemap.md#L209-L209](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L209-L209) (`clm_97479ad2a9c88ee3de0902260f1a81ed1753c63e9308e3d10d2b43133089d323`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A per-project daemon ('nanocoder daemon start') owns file-watch and cron event sources, letting Skills subscribe to file.changed or schedule.cron events and run headless without the TUI; launchd plist and systemd user-unit installers ship in-tree. -- evidence: [docs/battlemap.md#L109-L109](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L109-L109), [docs/battlemap.md#L197-L197](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L197-L197) (`clm_31c2f30736151c5c29b14451ea58282c1f34b0e1b5ed5db46f4193309f006ba0`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The cron-driven scheduler is documented as powered by the croner library. -- evidence: [docs/battlemap.md#L195-L195](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L195-L195) (`clm_6bf53e54f33c3a9316354f670cf4bf87d52e19c91cb99c39e9a9eda248cc2b34`)

## limitations (1 claim(s))

- [observation/documented] The project's own comparison doc acknowledges being behind peers in community size, surface breadth (no desktop or web app), extension depth relative to Pi, IDE-level code intelligence (LSP client only, no debugger integration), and distribution polish. -- evidence: [docs/battlemap.md#L253-L257](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L253-L257) (`clm_480bb4483b59ecd8f3f493b55e2845d1169cb1af32b4ebc759139612b4e030e4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

