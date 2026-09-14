# alibaba/open-code-review -- full detail

[Back to orientation](open-code-review.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/alibaba/open-code-review/494bf1c8d7a19196ab166960a06fef38d69a1d16/5996e384ce40ea12.json](../../../wiki/dossiers/alibaba/open-code-review/494bf1c8d7a19196ab166960a06fef38d69a1d16/5996e384ce40ea12.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository layout includes cmd/opencodereview (CLI entry), internal packages for agent, config, diff parsing, LLM clients (Anthropic & OpenAI), session, tool, telemetry (OpenTelemetry), and viewer, plus a pages/ WebUI frontend. -- evidence: [CONTRIBUTING.ko-KR.md#L120-L136](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ko-KR.md#L120-L136), [CONTRIBUTING.ja-JP.md#L120-L135](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L120-L135) (`clm_b4cca94010c68f4a00f99b87b5a5728f695746469b1192ce87afe3d94729b8f9`)

## design-choices (2 claim(s))

- [observation/documented] The core design pairs deterministic engineering (file selection, file bundling, template-based rule matching, positioning/reflection modules) with an agent for dynamic decisions and context retrieval. -- evidence: [README.md#L79-L79](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L79-L79), [README.md#L85-L88](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L85-L88), [README.md#L94-L95](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L94-L95), [README.md#L90-L90](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L90-L90) (`clm_7911bd8adf73c81b8e0a95864815a9047316ecf757607bcfe0ab936e4fb17937`)
- [observation/documented] Security defaults follow fail-safe principles: API keys come only from environment variables and are never logged or written to output files, and LLM responses undergo JSON schema validation with line-number bounds checking. -- evidence: [ASSURANCE_CASE.md#L59-L67](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L59-L67), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82) (`clm_56229336c50ba397bb242254f2fbe4cefda45d8c863c4e2a8ec1d030e049f5d9`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AI-assisted contributions must be disclosed early, contributors must understand and be able to explain all AI-generated code, AI/LLM may only be used for translation or prose polishing of replies, and 'Assisted-by'/'Co-developed-by' trailers are prohibited. -- evidence: [CONTRIBUTING.ja-JP.md#L145-L152](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L145-L152), [CONTRIBUTING.ko-KR.md#L146-L153](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ko-KR.md#L146-L153) (`clm_afe52be53242a691c9958a7c95729c1cc094e4ea2ff2b8a45e2b42147c40f3e8`)
- [observation/documented] Repository development practice: PRs must be focused on one logical change, include tests for behavior changes, update docs when user-facing behavior changes, pass all CI checks, and every contributor must sign the Alibaba CLA before merge. -- evidence: [CONTRIBUTING.ja-JP.md#L199-L203](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L199-L203), [CONTRIBUTING.ja-JP.md#L233-L233](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L233-L233), [CONTRIBUTING.ja-JP.md#L223-L229](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ja-JP.md#L223-L229) (`clm_09b5fddd434153c0becee974b4945ee1ea9e124eb6fb9f96e71f05f38c1efbb5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes an `ocr` CLI with commands including `ocr review` (workspace, --from/--to branch range, --commit), `ocr scan`, `ocr config provider/model`, `ocr session list`, and `ocr delegate`. -- evidence: [README.md#L121-L124](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L121-L124), [README.md#L141-L141](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L141-L141), [README.md#L111-L111](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L111-L111), [README.md#L144-L144](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L144-L144), [README.md#L138-L138](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L138-L138), [README.md#L151-L153](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L151-L153), [README.md#L160-L162](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L160-L162) (`clm_4db274464bd36c34f3faa27a3f21083ae8508ada708359789f4c62244b442338`)
- [observation/documented] The product optionally serves a local web viewer for browsing review session history; the viewer binds to localhost by default and uses a host-header allowlist (configurable via OCR_VIEWER_ALLOWED_HOSTS) to block DNS rebinding. -- evidence: [ASSURANCE_CASE.md#L11-L14](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L11-L14), [ASSURANCE_CASE.md#L59-L67](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L59-L67), [ASSURANCE_CASE.md#L18-L24](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L18-L24), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82) (`clm_55f2c41ecca2f0651e336554e0448c4c81c5ba78cb74a1b39f80aa6dae785844`)

## memory-state (1 claim(s))

- [observation/documented] Each review session writes to its own JSONL file with no shared state between sessions, and interrupted reviews can be resumed via `--resume <session-id>`. -- evidence: [README.md#L147-L148](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L147-L148), [README.md#L151-L153](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L151-L153), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82) (`clm_cd7a1bf6231d79a4a7d502245a606370cbfde2e93d85bfa5efe5f906f364050c`)

## orchestration (1 claim(s))

- [observation/documented] Related files are grouped into bundles, and each bundle runs as a sub-agent with isolated context, described as a divide-and-conquer strategy that stays stable on large changesets and supports concurrent review. -- evidence: [README.md#L85-L88](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L85-L88) (`clm_32ef382ea12467e64979669c4b49e9d3923e03704b47ddfd7f2c12e82ad608c3`)

## tools-permissions (2 claim(s))

- [observation/documented] The agent has tool-use capabilities: it can read full file contents, search the codebase, and inspect other changed files for context; built-in tools include file_read and code_search. -- evidence: [README.md#L41-L41](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L41-L41), [CONTRIBUTING.ko-KR.md#L120-L136](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/CONTRIBUTING.ko-KR.md#L120-L136) (`clm_ef944e2c12e0e9d22011b892636f1b17fc6f493a5f9bafcd7fe1474ba70090c6`)
- [observation/documented] Per the assurance case, agent file paths are validated against the repository root before and after symlink resolution, and external process execution is limited to git with hardcoded subcommands, plus a few user-configured call sites. -- evidence: [ASSURANCE_CASE.md#L59-L67](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L59-L67), [ASSURANCE_CASE.md#L73-L82](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L73-L82), [ASSURANCE_CASE.md#L88-L100](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/ASSURANCE_CASE.md#L88-L100) (`clm_5e672a90824e6b18afaa8845da6b8d906e4dd2b188dcfc290d2475f8c1794579`)

## evaluation (1 claim(s))

- [observation/documented] The README reports a benchmark built from 50 open-source repositories, 200 real PRs, and 10 languages with 1,505 annotated issues, measuring F1, precision, recall, average time, and tokens; it claims higher precision/F1 than Claude Code at ~1/9 the tokens but lower recall by design. -- evidence: [README.md#L55-L61](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L55-L61), [README.md#L51-L51](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L51-L51), [README.md#L49-L49](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L49-L49) (`clm_907db88c7eb34dcb1278b0d9d49cd32cc541aac3cc2424fbae1dbda54ada8a86`)

## dependencies (1 claim(s))

- [observation/documented] The tool requires Git >= 2.41 for diff generation, code search, and repository operations, and is distributed as an npm package `@alibaba-group/open-code-review`. -- evidence: [README.md#L107-L109](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L107-L109), [README.md#L101-L101](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L101-L101) (`clm_f4d0ec550119d8f1b82a56bcf0230b312989bb4051a35651252247dc329247af`)

## limitations (1 claim(s))

- [observation/documented] The README acknowledges lower recall than general-purpose agents, framed as a deliberate trade-off favoring precision over noise. -- evidence: [README.md#L49-L49](https://github.com/alibaba/open-code-review/blob/494bf1c8d7a19196ab166960a06fef38d69a1d16/README.md#L49-L49) (`clm_69566f5e26c42329412adf5da2bee2455861ae1a111f0c3a1c3789802db73670`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

