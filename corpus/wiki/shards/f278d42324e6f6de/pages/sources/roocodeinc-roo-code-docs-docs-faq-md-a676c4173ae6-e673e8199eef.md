---
access: public
aliases: []
claim_ids:
- clm_04b6e6bcbce6196afe2db6dc3c60e25934e6154c9f8ee9196c069db90c17b791
- clm_13349ec979372deeb9bdfd0a78f945550e3b6a4693b06120a5548c5a179d5569
- clm_1ba5a56949fe34e5779ab36b91775b653cb9ce44b8bf69815ada8f2ae5013f83
- clm_1d98e3d1b67a3ef5804a63eb48960974cff0d5ebfe18f7c9a8de7f2261b31f85
- clm_23f9032d6ebdc270b86603ebc8f35ef7352edf509ca9a8729da43edf4f2c0cea
- clm_a6ac58067ab16fa74de44a386f8ca07adb977585736be1dd6babf1ff6c85bd14
- clm_ad76642e27e43a267cfe65564ead533f967bbc69e0ab7207c0e60dee7710baa0
- clm_da81f65c1a1a6dc7e561d3af81a7b02a1e40ced407a8a35f5766a0f6b9cefaf7
maturity: draft
page_id: pg_67e72eb25999585e91e8e673e8199eef
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a5aba4cf58595aec81d0279a9b193de6
title: RooCodeInc/Roo-Code-Docs/docs/faq.md @ a676c4173ae6
updated_at: '2026-09-14T04:18:42Z'
---

# RooCodeInc/Roo-Code-Docs/docs/faq.md @ a676c4173ae6

<!-- rcw:begin owner=source:src_a5aba4cf58595aec81d0279a9b193de6 block=evidence -->
- Roo Code can read/write project files, execute shell commands, browse the web if enabled, and use external tools via MCP; users are prompted to approve or reject each tool use, with optional auto-approval settings. [@claim:clm_04b6e6bcbce6196afe2db6dc3c60e25934e6154c9f8ee9196c069db90c17b791]
- Documented caveats include that Roo Code can make mistakes and changes should be reviewed, and that markdown write failures can occur when VS Code extensions or settings (e.g., format-on-save, markdown preview) interfere with file editing. [@claim:clm_13349ec979372deeb9bdfd0a78f945550e3b6a4693b06120a5548c5a179d5569]
- Local model use is supported via Ollama and LM Studio, and the FAQ states offline use is possible when a local model is used. [@claim:clm_1ba5a56949fe34e5779ab36b91775b653cb9ce44b8bf69815ada8f2ae5013f83]
- Roo Code relies on external LLM inference providers such as Anthropic, OpenAI, OpenRouter, and Requesty, requiring users to obtain API keys; the Roo Code Router is offered as an alternative that needs no API key. [@claim:clm_1d98e3d1b67a3ef5804a63eb48960974cff0d5ebfe18f7c9a8de7f2261b31f85]
- Roo Code offers persona-based modes (Code, Architect, Ask, Debug) plus user-created Custom Modes, switchable via a dropdown or the '/' command. [@claim:clm_23f9032d6ebdc270b86603ebc8f35ef7352edf509ca9a8729da43edf4f2c0cea]
- Roo Code is described as an AI-powered suite of coding products that uses large language models to understand user requests and translate them into actions. [@claim:clm_a6ac58067ab16fa74de44a386f8ca07adb977585736be1dd6babf1ff6c85bd14]
- Codebase Indexing builds a semantic search index of the project using AI embeddings, requiring an OpenAI API key for embeddings and a Qdrant vector database for storage; initial indexing is the most expensive step with cheaper incremental updates. [@claim:clm_ad76642e27e43a267cfe65564ead533f967bbc69e0ab7207c0e60dee7710baa0]
- The Extension exposes a chat panel (Kangaroo icon) where tasks are typed, supports '@' context mentions for files, folders, and problems, and offers error diagnostics export with basic and detailed options. [@claim:clm_da81f65c1a1a6dc7e561d3af81a7b02a1e40ced407a8a35f5766a0f6b9cefaf7]
<!-- rcw:end owner=source:src_a5aba4cf58595aec81d0279a9b193de6 block=evidence -->

## Researcher notes

