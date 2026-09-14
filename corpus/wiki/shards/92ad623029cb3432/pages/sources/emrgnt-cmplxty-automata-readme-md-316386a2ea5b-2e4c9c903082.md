---
access: public
aliases: []
claim_ids:
- clm_1081b78582db481837b5c1291c68b5fbd23ab049048203e646bf065556f34a2e
- clm_43e379b31b240f9e3e7bf7f40e9e0a2d6c217e8f24540ff918d6dfea559294b4
- clm_53f2661cb03643611bf2ba4cac75f59f373f92de40a1d681bd146b1f3cb806de
- clm_6b974e0d9f4385f3780b3bbdb0d47e9644d509ed4358053da3d918be6f87cc38
- clm_748309999bd42126656b07956940a61515bf55088a5c85d93ef72ed2de4243a2
- clm_9f3f7ba7e9352de750866c46f451dc2220b6786d763b852257ee880b0587bbfe
- clm_b22474d246151d7c9b7439b12dbf6c59b686e813a9991bcf33861ddf71cb333b
- clm_cd48e3de9055f3e69d33a5de85e1fec0dc54a1fccbe440873b5f0095cddc12a0
maturity: draft
page_id: pg_dff7e9eda4565b3f9c632e4c9c903082
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7d79e14c31895a51ab23d641224b5a1e
title: emrgnt-cmplxty/automata/README.md @ 316386a2ea5b
updated_at: '2026-09-14T01:48:10Z'
---

# emrgnt-cmplxty/automata/README.md @ 316386a2ea5b

<!-- rcw:begin owner=source:src_7d79e14c31895a51ab23d641224b5a1e block=evidence -->
- Automata Search requires SCIP indices, which build a code graph relating symbols by dependencies; new indices are generated periodically and users may need to generate them manually for local development. [@claim:clm_1081b78582db481837b5c1291c68b5fbd23ab049048203e646bf065556f34a2e]
- The system combines large language models such as GPT-4 with a vector database to document, search, and write code, forming the basis of its self-coding potential. [@claim:clm_43e379b31b240f9e3e7bf7f40e9e0a2d6c217e8f24540ff918d6dfea559294b4]
- Repository development practice: contributors are directed to review CONTRIBUTING.md and a code of conduct, with GitHub issues for bugs and Discussions for general questions. [@claim:clm_53f2661cb03643611bf2ba4cac75f59f373f92de40a1d681bd146b1f3cb806de]
- Repository development practice: setup involves cloning, initializing git submodules, installing via poetry, and running automata configure; Docker installation is also documented, and Windows users may need C++ build tools and gcc-11/g++-11. [@claim:clm_6b974e0d9f4385f3780b3bbdb0d47e9644d509ed4358053da3d918be6f87cc38]
- A Python API lets users build an OpenAIAutomataAgent from a named config (e.g. 'automata-main'), attach factory-built tools, and run it with instructions via agent.run(). [@claim:clm_748309999bd42126656b07956940a61515bf55088a5c85d93ef72ed2de4243a2]
- Automata's stated goal is to become a fully autonomous, self-programming AI system, based on the idea that code is a form of memory that lets AI evolve real-time capabilities. [@claim:clm_9f3f7ba7e9352de750866c46f451dc2220b6786d763b852257ee880b0587bbfe]
- The product exposes a CLI via poetry, including commands like automata configure, install-indexing, run-code-embedding, run-doc-embedding, and run-agent with an --instructions flag. [@claim:clm_b22474d246151d7c9b7439b12dbf6c59b686e813a9991bcf33861ddf71cb333b]
- Symbol embeddings are represented by classes such as SymbolCodeEmbedding (code-related) and SymbolDocEmbedding (documentation-related), storing a symbol plus a high-dimensional vector. [@claim:clm_cd48e3de9055f3e69d33a5de85e1fec0dc54a1fccbe440873b5f0095cddc12a0]
<!-- rcw:end owner=source:src_7d79e14c31895a51ab23d641224b5a1e block=evidence -->

## Researcher notes

