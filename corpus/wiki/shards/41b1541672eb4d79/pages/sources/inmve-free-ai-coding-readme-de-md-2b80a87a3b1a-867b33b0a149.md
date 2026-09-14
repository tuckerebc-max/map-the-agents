---
access: public
aliases: []
claim_ids:
- clm_25197a54967c2b7cd6b8f585acccc786e88958c0020d02f68313b98ad805327e
- clm_3d92da6958903bc56d5b9a69539e8614a23777d0529b148c6584d1f2a29f4328
- clm_5e04295eb3eebd9d42fd1f665176b0eee2b13678395e7c55da1704b4353fe695
- clm_6b63a72c3c358dd4f6a0307d656b444f2008b708dce597635674cad0b1750d76
- clm_71915ae72da13d58875dd4b291bc4dc84756b837eda4c74e9b342a80c2d24676
- clm_7552ca59c841e1999351bcf73bba5d86deb843e7f47f59207bdb741826e82bee
- clm_9b5bd9b74862df6944e1ae6f7f201fde42ca7d7d3bc70ec79e23241436e49da9
- clm_b28e94daa604b2f3359b60f38036170b694615c8eb0cadad537908d1ff4622ce
- clm_be83fceb494a1a5e06c0cc7b2f32fa17dab7ef4c6d543f967603d9069065d03f
- clm_c44fa6543d0e0331c73f67f1377027ded4894a49214983118ee16e82a287e964
- clm_edf29572eb8245d18c7538dbc06f057d17379187fafc2e2e099a6b3c15aa78d5
- clm_fd68686cfcaec05fad5557d282af244c5b7c937b93fcb9271bf463512c114875
maturity: draft
page_id: pg_9c0a8942d2b455b2986c867b33b0a149
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_34b9e775dd5d5c37813db5dadda59f29
title: inmve/free-ai-coding/README-de.md @ 2b80a87a3b1a
updated_at: '2026-09-14T03:58:12Z'
---

# inmve/free-ai-coding/README-de.md @ 2b80a87a3b1a

<!-- rcw:begin owner=source:src_34b9e775dd5d5c37813db5dadda59f29 block=evidence -->
- Per-tool entries include details such as Qwen Code's 2,000 requests/day via Qwen OAuth with a 60 requests/minute rate limit, and Rovo Dev CLI's 5M tokens/day (20M on day one) resetting at midnight UTC. [@claim:clm_25197a54967c2b7cd6b8f585acccc786e88958c0020d02f68313b98ad805327e]
- The TL;DR table ranks free tiers from most to least generous, listing tools like Qwen Code (2,000 requests/day), Rovo Dev CLI (5M tokens/day beta), Gemini CLI, Cursor, Kilo Code, Warp, Trae, Amazon Q Developer, GitHub Copilot, Windsurf, and Jules. [@claim:clm_3d92da6958903bc56d5b9a69539e8614a23777d0529b148c6584d1f2a29f4328]
- A local-models section recommends running open-weight frontier models with tools like Cline, Aider, and Continue.dev via Ollama, and notes Qwen3-Coder-480B's GGUF is roughly 150GB with practical inference potentially needing ~150GB unified memory. [@claim:clm_5e04295eb3eebd9d42fd1f665176b0eee2b13678395e7c55da1704b4353fe695]
- Repository development practice: contributors are asked to open an issue or PR with a source when reporting errors or updated quota/model info, and are directed to CONTRIBUTING.md for detailed guidelines; new tool contributions are welcome. [@claim:clm_6b63a72c3c358dd4f6a0307d656b444f2008b708dce597635674cad0b1750d76]
- The comparison notes acknowledge that differing limit types (requests, tokens, credits, chats) make direct comparison difficult and that real-world usage depends on coding style, task costs, and tool implementation. [@claim:clm_71915ae72da13d58875dd4b291bc4dc84756b837eda4c74e9b342a80c2d24676]
- The list covers API providers separately, noting they are backends for existing tools rather than standalone coding tools; examples include OpenRouter (50 free requests/day, OpenAI-compatible API) and Cerebras (1M tokens/day free tier). [@claim:clm_7552ca59c841e1999351bcf73bba5d86deb843e7f47f59207bdb741826e82bee]
- The README is maintained in multiple languages, linking Spanish, Portuguese, Chinese, French, Japanese, Hindi, and German versions, with the German and Spanish copies last updated 5 December 2025. [@claim:clm_9b5bd9b74862df6944e1ae6f7f201fde42ca7d7d3bc70ec79e23241436e49da9]
- Entries also record paid-tier pricing, e.g. Claude Code Max 5x at $100/month (~225 messages/5h) and Max 20x at $200/month (~900 messages/5h), with weekly resets in rolling 5-hour windows. [@claim:clm_b28e94daa604b2f3359b60f38036170b694615c8eb0cadad537908d1ff4622ce]
- The repository is a curated list comparing AI coding tools side by side to show what is actually free, since tools use differing limits (credits, tokens, requests) that make comparison hard. [@claim:clm_be83fceb494a1a5e06c0cc7b2f32fa17dab7ef4c6d543f967603d9069065d03f]
- The README is organized into sections covering free pro-grade tools, API providers, paid-tier tools, tools with free basic models, and local models, plus comparison notes and related resources. [@claim:clm_c44fa6543d0e0331c73f67f1377027ded4894a49214983118ee16e82a287e964]
- The list applies an explicit qualification bar: only models scoring above 60% on SWE-bench Verified count as pro-grade, and it tabulates qualifying models such as Claude Opus 4.5 (80.9%) and GPT-5.1-Codex-Max (77.9%). [@claim:clm_edf29572eb8245d18c7538dbc06f057d17379187fafc2e2e099a6b3c15aa78d5]
- The README carries a disclaimer stating it has no vendor affiliation, information is for research purposes only, accuracy is not guaranteed, and limits/prices change frequently. [@claim:clm_fd68686cfcaec05fad5557d282af244c5b7c937b93fcb9271bf463512c114875]
<!-- rcw:end owner=source:src_34b9e775dd5d5c37813db5dadda59f29 block=evidence -->

## Researcher notes

