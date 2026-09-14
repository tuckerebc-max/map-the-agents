# alibaba/open-code-review

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 494bf1c8d7a1 @ 5996e384ce40ea12

## Summary (orientation draft, not independently verified)

Selected evidence records: The product exposes an `ocr` CLI with commands including `ocr review` (workspace, --from/--to branch range, --commit), `ocr scan`, `ocr config provider/model`, `ocr session list`, and `ocr delegate`. The core design pairs deterministic engineering (file selection, file bundling, template-based rule matching, positioning/reflection modules) with an agent for dynamic decisions and context retrieval.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository layout includes cmd/opencodereview (CLI entry), internal packages for agent, config, diff parsing, LLM clients (Anthropic & OpenAI), session, tool, telemetry (OpenTelemetry), and viewer, plus a pages/ WebUI frontend. -- evidence: [CONTRIBUTING.ko-KR.md#L120-L136](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ko-KR.md#L120-L136), [CONTRIBUTING.ja-JP.md#L120-L135](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L120-L135)
- design-choices (2 claim(s)):
  - [observation/documented] The core design pairs deterministic engineering (file selection, file bundling, template-based rule matching, positioning/reflection modules) with an agent for dynamic decisions and context retrieval. -- evidence: [README.md#L79-L79](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L79-L79), [README.md#L85-L88](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L85-L88), [README.md#L94-L95](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L94-L95), [README.md#L90-L90](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L90-L90)
  - [observation/documented] Security defaults follow fail-safe principles: API keys come only from environment variables and are never logged or written to output files, and LLM responses undergo JSON schema validation with line-number bounds checking. -- evidence: [ASSURANCE_CASE.md#L59-L67](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L59-L67), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AI-assisted contributions must be disclosed early, contributors must understand and be able to explain all AI-generated code, AI/LLM may only be used for translation or prose polishing of replies, and 'Assisted-by'/'Co-developed-by' trailers are prohibited. -- evidence: [CONTRIBUTING.ja-JP.md#L145-L152](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L145-L152), [CONTRIBUTING.ko-KR.md#L146-L153](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ko-KR.md#L146-L153)
  - [observation/documented] Repository development practice: PRs must be focused on one logical change, include tests for behavior changes, update docs when user-facing behavior changes, pass all CI checks, and every contributor must sign the Alibaba CLA before merge. -- evidence: [CONTRIBUTING.ja-JP.md#L199-L203](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L199-L203), [CONTRIBUTING.ja-JP.md#L233-L233](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L233-L233), [CONTRIBUTING.ja-JP.md#L223-L229](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L223-L229)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes an `ocr` CLI with commands including `ocr review` (workspace, --from/--to branch range, --commit), `ocr scan`, `ocr config provider/model`, `ocr session list`, and `ocr delegate`. -- evidence: [README.md#L121-L124](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L121-L124), [README.md#L141-L141](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L141-L141), [README.md#L111-L111](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L111-L111), [README.md#L144-L144](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L144-L144), [README.md#L138-L138](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L138-L138), [README.md#L151-L153](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L151-L153), [README.md#L160-L162](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L160-L162)
  - [observation/documented] The product optionally serves a local web viewer for browsing review session history; the viewer binds to localhost by default and uses a host-header allowlist (configurable via OCR_VIEWER_ALLOWED_HOSTS) to block DNS rebinding. -- evidence: [ASSURANCE_CASE.md#L11-L14](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L11-L14), [ASSURANCE_CASE.md#L59-L67](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L59-L67), [ASSURANCE_CASE.md#L18-L24](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L18-L24), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82)
- memory-state (1 claim(s)):
  - [observation/documented] Each review session writes to its own JSONL file with no shared state between sessions, and interrupted reviews can be resumed via `--resume <session-id>`. -- evidence: [README.md#L147-L148](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L147-L148), [README.md#L151-L153](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L151-L153), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82)
- orchestration (1 claim(s)):
More evidence: [full detail](open-code-review.detail.md)

Metadata and full claim list: [full detail](open-code-review.detail.md)
Human notes ([notes](open-code-review.notes.md), never overwritten by build)

[Back to map index](../../index.md)
