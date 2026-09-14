---
access: public
aliases: []
claim_ids:
- clm_0d4acf8c87ce6457c0b4373cb82e21077c86bb58297f90ec4fc45e2218f7497f
- clm_3583f0bab1f1da9c69758a7f5a1c737fe396a5711ae11a14173817037a38aaee
- clm_472a2fdfc08d8dd6af09eb4f69c9475f3ef3a51f9d4a60837623f09a71498d3d
- clm_4ac07b97f002f03fba8240f94ac5a77e39a02828ea07027ebe5de00f3eb3a309
- clm_723a24201ae3daec8ee92d9dc3ac62fe7b9f08c3e32ddb0f5748b8f0419c5bc9
- clm_abfadf4a69b40849c0a722fb0645406439abab413aa92dbe0d01f813cf71d45d
- clm_b3a030a47b253c69a1c59f927a3ae7246034eca268b12130f3b2ae265f837a67
- clm_cc73f83e42cc6881db95f65c6621b0d14743ef91d55fbcd9ba987785c7b754ed
- clm_e3bf6bdbc6792c3b5d15c8bfd7195699ce4086a4aab582a99d3f60053134bf29
- clm_e5a719fa3fa0bcf85e985621ff77e441090a3c4dc5c1fcf828e995eb72fc4806
- clm_fa652421aae754c885aadb6715eb9ca7fe66ac697976972a1c5249038347718c
- clm_fb55657a2a5b8644cfd58327bb594ea822280b175d65f8f262ddb208b409164c
maturity: draft
page_id: pg_c5e1c05b39d8523aa7921fa5abeabe8b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb58e1a14bea52ef835d736e6128fdf6
title: FSoft-AI4Code/HyperAgent/README.md @ c3092f2601ab
updated_at: '2026-09-14T01:49:13Z'
---

# FSoft-AI4Code/HyperAgent/README.md @ c3092f2601ab

<!-- rcw:begin owner=source:src_eb58e1a14bea52ef835d736e6128fdf6 block=evidence -->
- The system comprises four specialized agents: Planner, Navigator, Code Editor, and Executor, covering the SE task lifecycle from conception to verification. [@claim:clm_0d4acf8c87ce6457c0b4373cb82e21077c86bb58297f90ec4fc45e2218f7497f]
- Agent configuration is per-role: the config dict keys nav, edit, exec, and plan each take model settings (e.g., Claude models with API keys, stop sequences, base URLs), plus a 'type' field such as 'patch'. [@claim:clm_3583f0bab1f1da9c69758a7f5a1c737fe396a5711ae11a14173817037a38aaee]
- Tasks are implemented as task classes with a run(system, idx) method that constructs a prompt, calls system.query_codebase, and returns a result; example scripts live in the scripts folder and src/hyperagent/tasks. [@claim:clm_472a2fdfc08d8dd6af09eb4f69c9475f3ef3a51f9d4a60837623f09a71498d3d]
- HyperAgent is described as a generalist multi-agent system for a wide range of software engineering tasks across programming languages, mimicking human developer workflows. [@claim:clm_4ac07b97f002f03fba8240f94ac5a77e39a02828ea07027ebe5de00f3eb3a309]
- Currently only Python and Java are supported; expansion to other languages and benchmarks is planned for the future. [@claim:clm_723a24201ae3daec8ee92d9dc3ac62fe7b9f08c3e32ddb0f5748b8f0419c5bc9]
- Repository development practice: reproduction scripts are provided in the scripts folder for SWE-Bench, RepoExec, and Defects4J, e.g. run_swe_bench.py, run_defects4j_fl.py, and run_defects4j_apr.py. [@claim:clm_abfadf4a69b40849c0a722fb0645406439abab413aa92dbe0d01f813cf71d45d]
- Installation requires a conda environment named 'hyperagent' with Python 3.10, because the Executor uses a jupyter kernel of that name; the pinned requirements include anthropic, docker, GitPython, and e2b packages. [@claim:clm_b3a030a47b253c69a1c59f927a3ae7246034eca268b12130f3b2ae265f837a67]
- HyperAgent depends on Zoekt for code search, requiring a recent Go installation, plus universal-ctags with CTAGS_COMMAND=universal-ctags set for semantic code search. [@claim:clm_cc73f83e42cc6881db95f65c6621b0d14743ef91d55fbcd9ba987785c7b754ed]
- Reported repository-level code generation result is 53.3% Pass@5 on RepoExec-Python, and 249 bugs fixed on Defects4J-Java for fault localization and repair. [@claim:clm_e3bf6bdbc6792c3b5d15c8bfd7195699ce4086a4aab582a99d3f60053134bf29]
- HyperAgent supports two modes: patch mode generates a patch for a task, and predict mode predicts the next token (e.g., for repoQA or fault location). [@claim:clm_e5a719fa3fa0bcf85e985621ff77e441090a3c4dc5c1fcf828e995eb72fc4806]
- A Python API exposes HyperAgent(repo, commit, language, clone_dir, config) for use, and a CLI via main.py accepts repo path, commit hash, language, clone dir, and a free-form prompt. [@claim:clm_fa652421aae754c885aadb6715eb9ca7fe66ac697976972a1c5249038347718c]
- Reported results include 31.4% resolved rate on SWE-Bench Verified and 25% on SWE-Bench Lite, with verification noted as in progress via a swe-bench experiments PR. [@claim:clm_fb55657a2a5b8644cfd58327bb594ea822280b175d65f8f262ddb208b409164c]
<!-- rcw:end owner=source:src_eb58e1a14bea52ef835d736e6128fdf6 block=evidence -->

## Researcher notes

