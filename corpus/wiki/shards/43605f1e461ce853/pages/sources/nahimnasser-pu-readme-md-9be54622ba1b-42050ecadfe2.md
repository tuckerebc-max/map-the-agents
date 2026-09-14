---
access: public
aliases: []
claim_ids:
- clm_0e12b42128982ccd353390ab600e8e309a961944f182f74c570567a2fd8517c8
- clm_0e8569c145933e4a051bdbecfc26e541704088fb667eb05bdb166e28387b44bd
- clm_1f7a063cba3f8645c37209eec0ab806ab5ad9571b978a5d951bc326e3111df67
- clm_50ec630a018d822b3d13910c3143d12b3f61bcf341a99f98653a0a7f48b8ffd8
- clm_5b332f4c08569f771d957d3dbc900d04c5c9628cd47bf9bbbccb67c255028760
- clm_69e27dce557db67449db79e4d67f34fbf5394ab99d65255b38ad6cc10c9b233f
- clm_7e58d101d574324e7e9c35aed41665f7c477d2d38a68ab75c0135466f164413c
- clm_92504300d97300e83c6850719c6f8c691918ecfae991857cb16ba0c2c8fe7f67
- clm_9e5e3e6575b1a0008d9254552127a72454431655ace264803f2f4fba9b73d181
- clm_cab2eb7aac798984571282d87c74a2a95754be62d32c5968fe6253d1e1b40deb
- clm_e496a4a437195d971538982c16ff16b00f3cd7acd2a9b1ccbe05874f394529eb
maturity: draft
page_id: pg_7adab7a9eae95731a5ac42050ecadfe2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_77c62fd2fde95d3d949913f558fe1001
title: NahimNasser/pu/README.md @ 9be54622ba1b
updated_at: '2026-09-14T02:22:10Z'
---

# NahimNasser/pu/README.md @ 9be54622ba1b

<!-- rcw:begin owner=source:src_77c62fd2fde95d3d949913f558fe1001 block=evidence -->
- The product is a single shell script, pu.sh, described as under 50KB with zero package dependencies, relying on curl, awk, common Unix tools, and an API key. [@claim:clm_0e12b42128982ccd353390ab600e8e309a961944f182f74c570567a2fd8517c8]
- File writes and edits use mktemp temp files, preserve trailing newlines via sentinel capture, keep executable mode on edits, and edit requires a unique oldText match. [@claim:clm_0e8569c145933e4a051bdbecfc26e541704088fb667eb05bdb166e28387b44bd]
- JSON handling uses targeted awk parsing rather than a general JSON parser or jq, a deliberate choice to keep the install dependency-free. [@claim:clm_1f7a063cba3f8645c37209eec0ab806ab5ad9571b978a5d951bc326e3111df67]
- The README references 30+ experiments in final_report.md on harness portability and an eval/COMPARISON.md feature-by-feature comparison against Pi, suggesting evaluation effort beyond unit tests, though no scored agent benchmarks appear in the provided slices. [@claim:clm_50ec630a018d822b3d13910c3143d12b3f61bcf341a99f98653a0a7f48b8ffd8]
- The bash tool executes model-provided commands unsandboxed via a temp script; AGENT_CONFIRM=1 can be set to ask before each tool call. [@claim:clm_5b332f4c08569f771d957d3dbc900d04c5c9628cd47bf9bbbccb67c255028760]
- Documented gaps include no TUI, no streaming display, no image input, no OAuth login, no native Windows support, and no general JSON parser. [@claim:clm_69e27dce557db67449db79e4d67f34fbf5394ab99d65255b38ad6cc10c9b233f]
- The agent exposes seven tools: bash, read, write, edit, grep, find, and ls, described as a Pi-shaped tool surface. [@claim:clm_7e58d101d574324e7e9c35aed41665f7c477d2d38a68ab75c0135466f164413c]
- It targets two providers: Anthropic via /v1/messages and OpenAI via /v1/responses, with API keys supplied via environment variables or a first-run login wizard saving ~/.pu.env. [@claim:clm_92504300d97300e83c6850719c6f8c691918ecfae991857cb16ba0c2c8fe7f67]
- It offers an interactive REPL with commands including /model, /effort, /login, /logout, /flush, /compact, /export, /skill:name, /quit, and !cmd for inline shell execution. [@claim:clm_9e5e3e6575b1a0008d9254552127a72454431655ace264803f2f4fba9b73d181]
- The CLI accepts a one-shot task argument, an interactive multi-turn mode, and a --pipe mode for chaining agent outputs, e.g. piping a write task into a security review. [@claim:clm_cab2eb7aac798984571282d87c74a2a95754be62d32c5968fe6253d1e1b40deb]
- Sessions persist to .pu-history.json for resumable memory and .pu-events.jsonl for event replay/export; long sessions auto-compact by summarizing older transcript entries while keeping a bounded recent tail. [@claim:clm_e496a4a437195d971538982c16ff16b00f3cd7acd2a9b1ccbe05874f394529eb]
<!-- rcw:end owner=source:src_77c62fd2fde95d3d949913f558fe1001 block=evidence -->

## Researcher notes

