---
access: public
aliases: []
claim_ids:
- clm_4ca0acbd119c0a76dcc6e61a4d0299dc11f70e8bd2bce1508105e876b65025dc
- clm_a378fdb9a094a873bb83d46b5118b2a3f2873d99fa934d8b18aeb0104c1bffab
- clm_b6be0f3ba68d5ef85f7684365a62f4500fb18601c41c3b9c6d7865a450c3eae0
- clm_d271c94cc50229bfcfe81198c11c22bd1ddcf93db26cbb10c9c73c02196f72c6
- clm_e3f570167f7d2e358fd3e333103b3ad27503fb55e9eb71ca43c0ab2bd37baad8
- clm_e3fcfaf02ec85d132dad9b63e64946e462c119c89fc3ddb2c3117c09be1d7750
- clm_e849bca338ab918e93e03a8c5f8e13fe0c87fe0de7b9530a451a7ee4f61c3127
- clm_fa47b82fe64ebeccc7e77411ea3e5a0aa71191aad4978a1424cff84597b0c5f7
maturity: draft
page_id: pg_1295e319af0e5a32bfca1db1157a526a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0fb9558030ff570d9fa84ee174f90b86
title: Gerome-Elassaad/CodingIT/README.md @ b21eff408c44
updated_at: '2026-09-14T01:50:19Z'
---

# Gerome-Elassaad/CodingIT/README.md @ b21eff408c44

<!-- rcw:begin owner=source:src_0fb9558030ff570d9fa84ee174f90b86 block=evidence -->
- Repository development practice: setup requires cloning the repo, running npm i, creating .env.local with E2B and LLM provider API keys, then npm run dev or npm run build. [@claim:clm_4ca0acbd119c0a76dcc6e61a4d0299dc11f70e8bd2bce1508105e876b65025dc]
- Supported LLM providers include OpenAI, Anthropic, Google Generative AI, Google Vertex AI, Mistral, Groq, Fireworks, Together AI, Ollama, xAI, and DeepSeek. [@claim:clm_a378fdb9a094a873bb83d46b5118b2a3f2873d99fa934d8b18aeb0104c1bffab]
- The app is built on Next.js 14 (App Router, Server Actions) with shadcn/ui, TailwindCSS, and the Vercel AI SDK, and streams output in the UI. [@claim:clm_b6be0f3ba68d5ef85f7684365a62f4500fb18601c41c3b9c6d7865a450c3eae0]
- Repository development practice: custom personas are added by creating a sandbox-templates folder, building an E2B template via the E2B CLI, and registering it in lib/templates.json. [@claim:clm_d271c94cc50229bfcfe81198c11c22bd1ddcf93db26cbb10c9c73c02196f72c6]
- AI-generated code is executed via the E2B SDK (code-interpreter), which the README describes as executing such code securely. [@claim:clm_e3f570167f7d2e358fd3e333103b3ad27503fb55e9eb71ca43c0ab2bd37baad8]
- Repository development practice: the project welcomes community contributions via issues or pull requests for bugs and improvements. [@claim:clm_e3fcfaf02ec85d132dad9b63e64946e462c119c89fc3ddb2c3117c09be1d7750]
- The product ships several sandbox personas/stacks, including Python data analyst, Next.js, Vue.js, Streamlit, Gradio, and CodinIT Engineer. [@claim:clm_e849bca338ab918e93e03a8c5f8e13fe0c87fe0de7b9530a451a7ee4f61c3127]
- Repository development practice: custom LLM models are added in lib/models.json and providers via providerConfigs in lib/models.ts, with optional structured-output mode adjustments. [@claim:clm_fa47b82fe64ebeccc7e77411ea3e5a0aa71191aad4978a1424cff84597b0c5f7]
<!-- rcw:end owner=source:src_0fb9558030ff570d9fa84ee174f90b86 block=evidence -->

## Researcher notes

