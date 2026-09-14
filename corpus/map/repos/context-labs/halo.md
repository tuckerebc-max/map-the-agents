# context-labs/halo

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b7f8509745d6 @ 9f2700ac05de7f87

## Summary (orientation draft, not independently verified)

HALO is an RLM-based agent-harness optimizer that consumes OpenTelemetry/OpenInference-shaped JSONL traces, ships as a desktop app plus a PyPI engine/CLI, and documents an AppWorld benchmark evaluation. Evidence is mostly README and integration docs; development workflow details are limited to the README's Development section.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] HALO is described as a methodology for building recursively self-improving agent harnesses using RLMs, with the repo containing a desktop app, methodology docs, a Python engine package, and demos. -- evidence: [README.md#L125-L125](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L125-L125), [README.md#L127-L131](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L127-L131)
  - [observation/documented] The HALO loop: collect OpenTelemetry-compatible traces from an agent harness, feed them to the HALO-RLM engine, which decomposes traces into common failure modes and produces a report that a coding agent turns into harness changes, then the cycle repeats. -- evidence: [README.md#L138-L142](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L138-L142)
- components (1 claim(s)):
  - [observation/documented] The project ships a HALO Desktop App for local use, a Python package (halo-engine on PyPI) implementing the core HALO-RLM engine, and a demo project showing HALO loops with the OpenAI Agents SDK. -- evidence: [README.md#L156-L156](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L156-L156), [README.md#L158-L159](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L158-L159), [README.md#L127-L131](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L127-L131)
- design-choices (1 claim(s)):
  - [observation/documented] The authors argue general harnesses like Claude Code overfit to errors in single traces when analyzing long traces, motivating a specialized RLM for systemic trace analysis. -- evidence: [README.md#L148-L148](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L148-L148)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: local development uses uv and go-task; task env:setup installs uv, syncs the venv from uv.lock, and configures git hooks, with tasks for pre-commit checks, unit tests, and integration tests. -- evidence: [README.md#L298-L303](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L298-L303), [README.md#L292-L292](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L292-L292), [README.md#L282-L282](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L282-L282)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI takes a required JSONL trace path and prompt, with flags like --model (default gpt-5.4-mini) and --synthesis-model for trace summarization, and supports --base-url and custom headers as shown in an OpenRouter example. -- evidence: [README.md#L185-L204](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L185-L204), [README.md#L176-L177](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L176-L177), [README.md#L208-L213](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L208-L213)
  - [observation/documented] HALO uses OPENAI_API_KEY and OPENAI_BASE_URL; if the base URL is unset it defaults to https://api.openai.com/v1, and CLI settings mirror the SDK's ModelConfig and ModelProviderConfig. -- evidence: [README.md#L179-L181](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L179-L181)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] HALO's own telemetry is off by default; passing --telemetry emits OpenInference-shaped traces, uploaded over OTLP to inference.net when INFERENCE_API_KEY is set, otherwise written to a local JSONL file. -- evidence: [README.md#L217-L217](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L217-L217), [README.md#L223-L223](https://github.com/context-labs/HALO/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md#L223-L223)
- evaluation (1 claim(s)):
More evidence: [full detail](halo.detail.md)

Metadata and full claim list: [full detail](halo.detail.md)
Human notes ([notes](halo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
