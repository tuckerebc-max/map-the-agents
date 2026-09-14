---
access: public
aliases: []
claim_ids:
- clm_101f7e00ff34f7ccea06b203ff83aa3ab87ff1a413b252b32e6a4cc7926f5211
- clm_203167658e9a2e03be549e03c232da21291494f5abbc9226c168f3b7a9fcfc9c
- clm_2a37d36a83cf4d8675b278742d6b6c5337765261a76de7dadb396ade4ece8a84
- clm_5b09faba5a4f174ff7a23f395e99cdbd3de749800ec582886281c587518497be
- clm_7117449dacc0dcbfd7408e9cbb45b91546ed513da3b64cab26eeeeda4fbfe30f
- clm_886b11ce4d897bd6ec6cb1b66b4b4079b2e8a7abd2762495533131dfcea78ef9
- clm_b4a9b5b818c4783eeae5a055490de74356fc260d486e728a1a66bbf1dd7803f1
- clm_c37f543125b41806690d40c2f5c0ac9e9305e5b2bdf98c5488a5358a612a43d8
- clm_c5c482f23db77414b49daaaf4c6a80a711fed9b756f7ae283c68db604ac60510
- clm_d457024e103612076e6bde7b550beafc7afd7ba6f3aa3a1a5b835227302c9f52
maturity: draft
page_id: pg_9541b7778514546887cf2c03904cddea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6ea2cc2a460755b08a5902ec415e782e
title: codefuse-ai/codefuse-chatbot/README.md @ d6932ecfc855
updated_at: '2026-09-14T02:00:19Z'
---

# codefuse-ai/codefuse-chatbot/README.md @ d6932ecfc855

<!-- rcw:begin owner=source:src_6ea2cc2a460755b08a5902ec415e782e block=evidence -->
- Offline private deployment is possible using open-source LLM and embedding models, and calling the OpenAI API is also supported. [@claim:clm_101f7e00ff34f7ccea06b203ff83aa3ab87ff1a413b252b32e6a4cc7926f5211]
- Setup documentation recommends optionally managing Python 3.9 with conda, installing dependencies via pip install -r requirements.txt, and starting services from the examples directory with start.sh. [@claim:clm_203167658e9a2e03be549e03c232da21291494f5abbc9226c168f3b7a9fcfc9c]
- A model table lists chatgpt and codellama-34b-int4 (34B, int4 quantization, about 20GB GPU memory), with the latter's Hugging Face availability marked 'coming soon' and a ModelScope link provided. [@claim:clm_2a37d36a83cf4d8675b278742d6b6c5337765261a76de7dadb396ade4ece8a84]
- The documented roadmap lists a multi-agent scheduling core, multi-source web crawler, data processor for document loading/cleaning/splitting, text embedding and indexing, vector and graph databases, prompt management, a sandbox, LLM integration, and API management. [@claim:clm_5b09faba5a4f174ff7a23f395e99cdbd3de749800ec582886281c587518497be]
- The project was tested under Python 3.9.18 with CUDA 11.7 on Windows and X86-architecture macOS; users install NVIDIA drivers themselves, and Apple Silicon users may need qpdf installed via brew. [@claim:clm_7117449dacc0dcbfd7408e9cbb45b91546ed513da3b64cab26eeeeda4fbfe30f]
- The stated approach uses retrieval-augmented generation, tool learning, and sandbox environments to build an assistant spanning design, coding, testing, deployment, and operations phases. [@claim:clm_886b11ce4d897bd6ec6cb1b66b4b4079b2e8a7abd2762495533131dfcea78ef9]
- CodeFuse-ChatBot is described as an open-source AI assistant from Ant Group's CodeFuse team that combines multi-agent coordination with tool, code, and knowledge bases plus a sandbox so LLMs can handle DevOps tasks. [@claim:clm_b4a9b5b818c4783eeae5a055490de74356fc260d486e728a1a66bbf1dd7803f1]
- Repository development practice: suggestions, comments, and contributions (code, tests, tooling, documentation) are welcomed via GitHub Issues and an external contribution guide, with contributors added to a contributor list. [@claim:clm_c37f543125b41806690d40c2f5c0ac9e9305e5b2bdf98c5488a5358a612a43d8]
- The project acknowledges being built on the open-source projects langchain-chatchat and codebox-api. [@claim:clm_c5c482f23db77414b49daaaf4c6a80a711fed9b756f7ae283c68db604ac60510]
- A configurable multi-agent framework, codefuse-muAgent, was announced in January 2024 and is installable via pip (pip install codefuse-muagent), with documentation hosted externally. [@claim:clm_d457024e103612076e6bde7b550beafc7afd7ba6f3aa3a1a5b835227302c9f52]
<!-- rcw:end owner=source:src_6ea2cc2a460755b08a5902ec415e782e block=evidence -->

## Researcher notes

