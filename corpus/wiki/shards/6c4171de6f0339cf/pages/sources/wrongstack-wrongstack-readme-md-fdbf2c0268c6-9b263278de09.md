---
access: public
aliases: []
claim_ids:
- clm_0b7f8c828e6c72e4572b81b9ff45544d11fdf4d4672858519187ce2cec128475
- clm_257aeee85c267b770ac61cd8de75b161eab843b918df61e03490cfb92591335b
- clm_3da31d32a5706a942ff6bee114483550d0a3272dd070bac941e6cf413967ad22
- clm_5a41a6a7ca5b89e8afc9cb1e587155e92d021febb56d34644e00c261e2e2fec4
- clm_9e8fd75ac6b39c23376b3569621e763a6256ae39f386f0248f0abd34194e7167
- clm_b2c4784c44b87e58c723a87a7066d1dfe3d800b73949ca453d3040f5f24b93bd
- clm_bc84cf2441ef9b2710134c276d45208a21858275d524fac2592fa7de9744be3a
- clm_d6e4cdf5f33b9cae66c30a2b682ab2d2a96090bfd10983dfb94e39f8b2d1cd79
- clm_f0378279ef38c0c12b39967a1709aaa13781c1f69fbe25c584ac0215fb3240ea
- clm_fc3f6747e01874ea79dbda4991632607ddc3d7b348ba8d54909f805b65c6783f
maturity: draft
page_id: pg_43182783325d5bb7a5b49b263278de09
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0997037ff50456c081ada722fa7b5b74
title: WrongStack/WrongStack/README.md @ fdbf2c0268c6
updated_at: '2026-09-14T03:23:42Z'
---

# WrongStack/WrongStack/README.md @ fdbf2c0268c6

<!-- rcw:begin owner=source:src_0997037ff50456c081ada722fa7b5b74 block=evidence -->
- The kernel is described as four primitives — Container, Pipeline, EventBus, RunController — with extension points in registries and services bound through the Container. [@claim:clm_0b7f8c828e6c72e4572b81b9ff45544d11fdf4d4672858519187ce2cec128475]
- Every tool call passes a permission policy; project-root containment cannot be overridden by YOLO, absolute denies remain enforced, and destructive shell actions stay confirmable unless destructive YOLO is explicitly enabled. [@claim:clm_257aeee85c267b770ac61cd8de75b161eab843b918df61e03490cfb92591335b]
- A Director-led specialist fleet fans out subagents, each isolated with its own budget and JSONL transcript, coordinated over a project-wide mailbox with typed messages and live presence. [@claim:clm_3da31d32a5706a942ff6bee114483550d0a3272dd070bac941e6cf413967ad22]
- SAGE is project-local long-term memory backed by SQLite/FTS5 under .wrongstack/memories/, with typed knowledge, anchors to files/symbols/commands/commits, a knowledge graph, and auto-injection into context each turn. [@claim:clm_5a41a6a7ca5b89e8afc9cb1e587155e92d021febb56d34644e00c261e2e2fec4]
- Repository development practice: pnpm release:fast skips only the audit and instrumented-coverage gates that CI covers, and the release matrix verifies the packed providers package installs with npm 10. [@claim:clm_9e8fd75ac6b39c23376b3569621e763a6256ae39f386f0248f0abd34194e7167]
- Repository development practice: release verification uses pnpm release:check with 18 gates, root Vitest coverage thresholds are set (>=76% lines, >=75% functions, >=66% branches), and package-boundary rules are enforced by a dedicated architecture test. [@claim:clm_b2c4784c44b87e58c723a87a7066d1dfe3d800b73949ca453d3040f5f24b93bd]
- The project requires Node.js >= 22.19.0 with pnpm (recommended) or npm, or Bun >= 1.3.10 as an alternative runtime; it is ESM-only with no CommonJS bundles. [@claim:clm_bc84cf2441ef9b2710134c276d45208a21858275d524fac2592fa7de9744be3a]
- The product offers six launch surfaces: a readline REPL, an Ink TUI behind --tui, a WebUI, SimpleUI, an Electron Desktop shell, and a cross-machine HQ dashboard. [@claim:clm_d6e4cdf5f33b9cae66c30a2b682ab2d2a96090bfd10983dfb94e39f8b2d1cd79]
- The @wrongstack/bench package is described as a benchmark harness covering Aider polyglot and SWE-bench Verified. [@claim:clm_f0378279ef38c0c12b39967a1709aaa13781c1f69fbe25c584ac0215fb3240ea]
- Providers span multiple wire families including native Anthropic, OpenAI, Google, OpenAI-compatible, and OAuth adapters, with a catalog fetched from models.dev and one-command Ollama/vLLM/LM Studio local presets. [@claim:clm_fc3f6747e01874ea79dbda4991632607ddc3d7b348ba8d54909f805b65c6783f]
<!-- rcw:end owner=source:src_0997037ff50456c081ada722fa7b5b74 block=evidence -->

## Researcher notes

