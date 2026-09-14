---
access: public
aliases: []
claim_ids:
- clm_38802e992c323b0c3772365c82c4d3c5228e8cd06ee342b87af5f840288c35e3
- clm_4f6790d79109c2af1a8e29c7601bd75a44033d73a294658db5e635ad3c6277d3
- clm_6e34f0918824d10bbc18e4c655bb9a8208177c37650d5d8786fc358697c5f903
- clm_892b17f9d243d77fbdda0a3b6d2293d1a1a02a44f375bb4b550d21a41e0ecb6c
- clm_9898baa4293b785f998b047fd9e75ac557663249290b5c00743af2b494cdeb29
- clm_a04e8c4b1684de0695edef34e3e9c971362ac1e985cbd39229659a81c88738c6
- clm_a3587c5c5ca174845d6e4cafea96026f314e4869f60627c583f8ac65ba34533d
- clm_c05feff024bc3d2c437852991ede8b9984b4c6fdcb23a233fda5af8e4249f7d1
- clm_d750e279a85365211b4d8f2c3bd325f1ce1a2be42ccb7267d5260fd70db0f13a
- clm_edd71fb9fc6c8aaf4c6e591bb5ca20930f2faf275be81c0a8ef9f7045a006c50
maturity: draft
page_id: pg_2711b60da26451ec99355fd022a1e9ae
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bf415efb5e1055d583ada98510945b8a
title: samholt/L2MAC/README.md @ 105e74afdc67
updated_at: '2026-09-14T02:39:03Z'
---

# samholt/L2MAC/README.md @ 105e74afdc67

<!-- rcw:begin owner=source:src_bf415efb5e1055d583ada98510945b8a block=evidence -->
- The tools_enabled parameter controls which functions agents can use, defaulting to all available tools; for codebase generation, tools include syntax-error checking and running unit tests. [@claim:clm_38802e992c323b0c3772365c82c4d3c5228e8cd06ee342b87af5f840288c35e3]
- L2MAC reads and updates existing code files created many instruction steps earlier, and generates unit tests used as an error checker to fix code that fails after updates. [@claim:clm_4f6790d79109c2af1a8e29c7601bd75a44033d73a294658db5e635ad3c6277d3]
- Each prompt-program instruction step is loaded into a new LLM agent whose context is managed by a control unit and given tools to read and write a persistent file-store holding final and intermediate outputs. [@claim:clm_6e34f0918824d10bbc18e4c655bb9a8208177c37650d5d8786fc358697c5f903]
- The README reports benchmark results: the highest percentage of implemented user-specified features on system design tasks (averaged over 10 random seeds) and a claimed 90.2% Pass@1 on HumanEval. [@claim:clm_892b17f9d243d77fbdda0a3b6d2293d1a1a02a44f375bb4b550d21a41e0ecb6c]
- The prompt-program is a sequence of instruction-step prompts; unless explicitly given, it is self-generated (bootstrapped) and then executed. [@claim:clm_9898baa4293b785f998b047fd9e75ac557663249290b5c00743af2b494cdeb29]
- L2MAC is described as an LLM-based multi-agent system implementing a stored-program von Neumann-style architecture for extensive, consistent output generation. [@claim:clm_a04e8c4b1684de0695edef34e3e9c971362ac1e985cbd39229659a81c88738c6]
- L2MAC offers a CLI (e.g. `l2mac "..."` creating a codebase repo in ./workspace) and a Python library API including generate_codebase and run_l2mac, plus helper functions for book and custom domains. [@claim:clm_a3587c5c5ca174845d6e4cafea96026f314e4869f60627c583f8ac65ba34533d]
- Configuration uses an LLM API with api_type (e.g. openai or azure), model (example gpt-4o), base_url, and api_key, set in ~/.l2mac/config.yaml or initialized via `l2mac --init-config`. [@claim:clm_c05feff024bc3d2c437852991ede8b9984b4c6fdcb23a233fda5af8e4249f7d1]
- The framework aims to produce outputs unbounded by the underlying LLM's fixed context window by persisting outputs to a file store. [@claim:clm_d750e279a85365211b4d8f2c3bd325f1ce1a2be42ccb7267d5260fd70db0f13a]
- requirements.txt lists pyyaml, pydantic, typer>=0.9.0, numpy, openai, tiktoken, timeout-decorator, and pygame==2.1.2; the README states Python 3.7+ is needed. [@claim:clm_edd71fb9fc6c8aaf4c6e591bb5ca20930f2faf275be81c0a8ef9f7045a006c50]
<!-- rcw:end owner=source:src_bf415efb5e1055d583ada98510945b8a block=evidence -->

## Researcher notes

