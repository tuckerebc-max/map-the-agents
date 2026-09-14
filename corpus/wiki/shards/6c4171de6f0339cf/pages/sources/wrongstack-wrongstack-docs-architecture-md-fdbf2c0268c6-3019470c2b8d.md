---
access: public
aliases: []
claim_ids:
- clm_0b7f8c828e6c72e4572b81b9ff45544d11fdf4d4672858519187ce2cec128475
- clm_178b637578644b0417467dcd1e86e1583787964770d4a60c7f8ce6c7fbf9c481
- clm_257aeee85c267b770ac61cd8de75b161eab843b918df61e03490cfb92591335b
- clm_aaaf3643238f70ad111c89386316e1f04e21520704536c0578975d028eb0128f
- clm_b2c4784c44b87e58c723a87a7066d1dfe3d800b73949ca453d3040f5f24b93bd
- clm_fc3f6747e01874ea79dbda4991632607ddc3d7b348ba8d54909f805b65c6783f
maturity: draft
page_id: pg_02e4dd3f5a7e59f697303019470c2b8d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7b5eee5cb47356a292d943be7701708b
title: WrongStack/WrongStack/docs/architecture.md @ fdbf2c0268c6
updated_at: '2026-09-14T03:23:42Z'
---

# WrongStack/WrongStack/docs/architecture.md @ fdbf2c0268c6

<!-- rcw:begin owner=source:src_7b5eee5cb47356a292d943be7701708b block=evidence -->
- The kernel is described as four primitives — Container, Pipeline, EventBus, RunController — with extension points in registries and services bound through the Container. [@claim:clm_0b7f8c828e6c72e4572b81b9ff45544d11fdf4d4672858519187ce2cec128475]
- The pnpm workspace reportedly contains 29 packages and two applications, with foundation packages persistence, kanban, and core, plus runtime, providers, tools, and user-surface packages. [@claim:clm_178b637578644b0417467dcd1e86e1583787964770d4a60c7f8ce6c7fbf9c481]
- Every tool call passes a permission policy; project-root containment cannot be overridden by YOLO, absolute denies remain enforced, and destructive shell actions stay confirmable unless destructive YOLO is explicitly enabled. [@claim:clm_257aeee85c267b770ac61cd8de75b161eab843b918df61e03490cfb92591335b]
- Tools declare a JSON-schema input plus permission/risk/mutation profile, and the ToolExecutor evaluates permission before execution with sequential, parallel, and smart scheduling. [@claim:clm_aaaf3643238f70ad111c89386316e1f04e21520704536c0578975d028eb0128f]
- Repository development practice: release verification uses pnpm release:check with 18 gates, root Vitest coverage thresholds are set (>=76% lines, >=75% functions, >=66% branches), and package-boundary rules are enforced by a dedicated architecture test. [@claim:clm_b2c4784c44b87e58c723a87a7066d1dfe3d800b73949ca453d3040f5f24b93bd]
- Providers span multiple wire families including native Anthropic, OpenAI, Google, OpenAI-compatible, and OAuth adapters, with a catalog fetched from models.dev and one-command Ollama/vLLM/LM Studio local presets. [@claim:clm_fc3f6747e01874ea79dbda4991632607ddc3d7b348ba8d54909f805b65c6783f]
<!-- rcw:end owner=source:src_7b5eee5cb47356a292d943be7701708b block=evidence -->

## Researcher notes

