---
access: public
aliases: []
claim_ids:
- clm_05d8215d865e467a426d0800ac395d2ee6a65ddabc98a0c34fe34a4945c88f1f
- clm_0b29ad6fd633ae791ef5d8d0edf63959f0b5278dcf6cf56dcb2b34701f66da7b
- clm_0c59b8f0b1df3804d825264dd20858df9ce3e9d132caea80644c1baf5ed829c4
- clm_13a6fe5ae0fec041c39ce21da4e5b3bb1b56ca137bb945c283ae26efdab0c8b0
- clm_1f2479b10825892ed072c522fdd035ab32d873b95f6858e675277628f62e7570
- clm_6921439416cf368d91e329598a3d02a70295ef10e309770768eebd65384d5f7a
- clm_71b5236595fb74ee0a762d5c5f921f39791c7ad91c404752097a678aeac7edf3
- clm_7df3a5dbdf9586bcc6b93014c53bdce9205c527e0f92a5f6efce6638c00bbef7
- clm_938980f911fb84af243f7cd646c194a223807ef28a246a2acad88b54d40351c2
- clm_d539bc03b6fc4b52f2c80abc382ed3c484755af10320f5dce1a14a17e618e5f6
maturity: draft
page_id: pg_96c6de64dded5cb7a0945bb4060c72a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c9bd916485bb51fda92100fc22bbece4
title: context-labs/HALO/README.md @ b7f8509745d6
updated_at: '2026-09-14T03:42:54Z'
---

# context-labs/HALO/README.md @ b7f8509745d6

<!-- rcw:begin owner=source:src_c9bd916485bb51fda92100fc22bbece4 block=evidence -->
- HALO uses OPENAI_API_KEY and OPENAI_BASE_URL; if the base URL is unset it defaults to https://api.openai.com/v1, and CLI settings mirror the SDK's ModelConfig and ModelProviderConfig. [@claim:clm_05d8215d865e467a426d0800ac395d2ee6a65ddabc98a0c34fe34a4945c88f1f]
- Repository development practice: local development uses uv and go-task; task env:setup installs uv, syncs the venv from uv.lock, and configures git hooks, with tasks for pre-commit checks, unit tests, and integration tests. [@claim:clm_0b29ad6fd633ae791ef5d8d0edf63959f0b5278dcf6cf56dcb2b34701f66da7b]
- The project ships a HALO Desktop App for local use, a Python package (halo-engine on PyPI) implementing the core HALO-RLM engine, and a demo project showing HALO loops with the OpenAI Agents SDK. [@claim:clm_0c59b8f0b1df3804d825264dd20858df9ce3e9d132caea80644c1baf5ed829c4]
- The CLI takes a required JSONL trace path and prompt, with flags like --model (default gpt-5.4-mini) and --synthesis-model for trace summarization, and supports --base-url and custom headers as shown in an OpenRouter example. [@claim:clm_13a6fe5ae0fec041c39ce21da4e5b3bb1b56ca137bb945c283ae26efdab0c8b0]
- HALO's own telemetry is off by default; passing --telemetry emits OpenInference-shaped traces, uploaded over OTLP to inference.net when INFERENCE_API_KEY is set, otherwise written to a local JSONL file. [@claim:clm_1f2479b10825892ed072c522fdd035ab32d873b95f6858e675277628f62e7570]
- HALO is described as a methodology for building recursively self-improving agent harnesses using RLMs, with the repo containing a desktop app, methodology docs, a Python engine package, and demos. [@claim:clm_6921439416cf368d91e329598a3d02a70295ef10e309770768eebd65384d5f7a]
- On AppWorld, harness-only optimization reportedly raised SGC: Gemini 3 Flash dev 36.8%→52.6% and test_normal 37.5%→48.2%; Sonnet 4.6 dev 73.7%→89.5% and test_normal 62.5%→73.2%, iterating on dev and checking test_normal for overfitting. [@claim:clm_71b5236595fb74ee0a762d5c5f921f39791c7ad91c404752097a678aeac7edf3]
- The HALO loop: collect OpenTelemetry-compatible traces from an agent harness, feed them to the HALO-RLM engine, which decomposes traces into common failure modes and produces a report that a coding agent turns into harness changes, then the cycle repeats. [@claim:clm_7df3a5dbdf9586bcc6b93014c53bdce9205c527e0f92a5f6efce6638c00bbef7]
- The engine exposes multiple entry points from engine.main (e.g. stream_engine_async, run_engine_async, stream_engine_output) yielding AgentOutputItem and AgentTextDelta types, trading off streaming observability versus simplicity. [@claim:clm_938980f911fb84af243f7cd646c194a223807ef28a246a2acad88b54d40351c2]
- The authors argue general harnesses like Claude Code overfit to errors in single traces when analyzing long traces, motivating a specialized RLM for systemic trace analysis. [@claim:clm_d539bc03b6fc4b52f2c80abc382ed3c484755af10320f5dce1a14a17e618e5f6]
<!-- rcw:end owner=source:src_c9bd916485bb51fda92100fc22bbece4 block=evidence -->

## Researcher notes

