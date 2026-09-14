# nano-collective/nanocoder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0cb0afb026ef @ 2d433bc2d82c310f

## Summary (orientation draft, not independently verified)

Selected evidence records: The CLI accepts --provider and --model flags in both interactive form and with a non-interactive 'run' subcommand, and flags may appear before or after the run subcommand. A starting development mode can be selected at launch via --mode; documented examples include yolo and plan modes.

## Source coverage

Source coverage (partial): 6 of 70 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The agent supports 20+ providers: native cloud integrations (e.g. Anthropic, OpenAI, Google Gemini, OpenRouter, Copilot, Mistral, Z.ai), seven documented local servers (Ollama, llama.cpp, llama-swap, LM Studio, LocalAI, MLX Server, vLLM), and any custom OpenAI-compatible endpoint. -- evidence: [docs/battlemap.md#L69-L71](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L69-L71)
- design-choices (2 claim(s)):
  - [observation/documented] Stated design principles are zero telemetry, zero tracking, and local-first operation, with the whole loop able to run on-machine against local models with no outbound network traffic. -- evidence: [docs/battlemap.md#L173-L173](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L173-L173), [docs/battlemap.md#L21-L23](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L21-L23)
  - [observation/documented] Tool calling uses three paths: native function calling plus XML and JSON fallbacks, with malformed-output repair on both fallback paths so weaker or non-conforming models still work end to end. -- evidence: [docs/battlemap.md#L189-L189](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L189-L189)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README directs contributors to CONTRIBUTING.md for development setup and guidelines, and notes shared conventions, tests, and release standards across Nano Collective projects. -- evidence: [README.md#L77-L77](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L77-L77), [README.md#L104-L107](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L104-L107)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI accepts --provider and --model flags in both interactive form and with a non-interactive 'run' subcommand, and flags may appear before or after the run subcommand. -- evidence: [README.md#L39-L39](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L39-L39), [README.md#L42-L42](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L42-L42), [README.md#L45-L45](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L45-L45)
  - [observation/documented] A starting development mode can be selected at launch via --mode; documented examples include yolo and plan modes. -- evidence: [README.md#L48-L49](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/README.md#L48-L49)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A per-project daemon ('nanocoder daemon start') owns file-watch and cron event sources, letting Skills subscribe to file.changed or schedule.cron events and run headless without the TUI; launchd plist and systemd user-unit installers ship in-tree. -- evidence: [docs/battlemap.md#L109-L109](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L109-L109), [docs/battlemap.md#L197-L197](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L197-L197)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The cron-driven scheduler is documented as powered by the croner library. -- evidence: [docs/battlemap.md#L195-L195](https://github.com/Nano-Collective/nanocoder/blob/0cb0afb026efaad90a62a64020866adb4fb21244/docs/battlemap.md#L195-L195)
- limitations (1 claim(s)):
More evidence: [full detail](nanocoder.detail.md)

Metadata and full claim list: [full detail](nanocoder.detail.md)
Human notes ([notes](nanocoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
