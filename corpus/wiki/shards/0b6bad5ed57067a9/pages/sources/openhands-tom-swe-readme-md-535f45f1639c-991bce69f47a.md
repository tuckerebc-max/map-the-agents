---
access: public
aliases: []
claim_ids:
- clm_1378b366fd2cd78902aeb6cf9629d535c58510fddab83ef0ea8730f0b1469ad4
- clm_184d3e1b65131040a752b93e065831af8844753529e371cd1acfa55df8f84fac
- clm_217056c77de82371e9f7f3a8e534544d59ea65367c8fa14b64b2c9c4c36722de
- clm_2c3c1800f852dd30312e11d2cebcf6baaf28a61c84fb0f6081790446768d855a
- clm_49b718ce73a898506c17ed8ce206ee98616694a8b5664d359b409ddb71d119e8
- clm_5313374995c16ecd961d538b34a45a799ba11edac9a0c164a18a5fa09f2ac7a3
- clm_9230a771c56198945d13cc4947ca206371243d2f6860597207db354a7ac7e571
- clm_98a1017f97e069986f4f2a0651b4389738280e278de846cb70a5d7b2ffc3a21b
maturity: draft
page_id: pg_218bb5c154ba581f8b58991bce69f47a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_958ef78bbf03585ebe07129671ac5584
title: OpenHands/ToM-SWE/README.md @ 535f45f1639c
updated_at: '2026-09-14T04:14:11Z'
---

# OpenHands/ToM-SWE/README.md @ 535f45f1639c

<!-- rcw:begin owner=source:src_958ef78bbf03585ebe07129671ac5584 block=evidence -->
- LLM access is configured through a .env file with LITELLM_API_KEY, LITELLM_BASE_URL, and a default model of litellm_proxy/claude-sonnet-4-20250514. [@claim:clm_1378b366fd2cd78902aeb6cf9629d535c58510fddab83ef0ea8730f0b1469ad4]
- ToM-SWE is a Theory of Mind package intended to give software engineering agents personalized user understanding and adaptive behavior. [@claim:clm_184d3e1b65131040a752b93e065831af8844753529e371cd1acfa55df8f84fac]
- The package exposes a TomModule class importable from tom_swe.tom_module and instantiated inside an async demo function. [@claim:clm_217056c77de82371e9f7f3a8e534544d59ea65367c8fa14b64b2c9c4c36722de]
- The project ships CLI commands including user-analysis, tom-test, tom-analyze, rag-agent, and tom-config, runnable via uv. [@claim:clm_2c3c1800f852dd30312e11d2cebcf6baaf28a61c84fb0f6081790446768d855a]
- OpenHands integration is provided through a TomCodeActAgent, set as default_agent in config, which automatically supplies consultation and personalized guidance and processes user sessions. [@claim:clm_49b718ce73a898506c17ed8ce206ee98616694a8b5664d359b409ddb71d119e8]
- README requirements list Python 3.8+, the uv package manager, and an LLM API key obtained from All Hands AI. [@claim:clm_5313374995c16ecd961d538b34a45a799ba11edac9a0c164a18a5fa09f2ac7a3]
- The system uses a three-tier memory structure: cleaned sessions, then session analyses, then user profiles. [@claim:clm_9230a771c56198945d13cc4947ca206371243d2f6860597207db354a7ac7e571]
- TomModule provides an async consult method taking user_id and current_context parameters and returning a consultation result that the demo prints. [@claim:clm_98a1017f97e069986f4f2a0651b4389738280e278de846cb70a5d7b2ffc3a21b]
<!-- rcw:end owner=source:src_958ef78bbf03585ebe07129671ac5584 block=evidence -->

## Researcher notes

