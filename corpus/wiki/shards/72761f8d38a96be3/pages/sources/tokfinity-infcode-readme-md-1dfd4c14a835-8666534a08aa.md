---
access: public
aliases: []
claim_ids:
- clm_2c01104390a38d7a52a30d586ad8825f364021fad2769f4141ed439c20c96294
- clm_5cf254e6e1ed8c90a8b86f0f9e196079f6f64f54c43385de4e18c8055eb6fae0
- clm_68005e7d743b28f600a450b55d3e52d11d23f90e9887c1e525323b5d20690e08
- clm_7635ee7dfab8b20122b5594403f9ee5467e48055bf0638cfe69f984a7b98ea8a
- clm_7952de424bdccaa9757528a2c39691c57e1fdf44db4aefb5cd1350c785ff456b
- clm_7ca9a74339684ca7084e23faf0f2c19201ce74cac3f66e6acb7a1fcfa36cb04d
- clm_7f08e2eb308c1ce923702c5c449c2f9455d107f26d0a41c54db007862c128b6a
- clm_ae595767ed99c65b1312ade293bba5579142d045a5280cd2af734742293dd025
- clm_aec938a77df1928f5bb99a69206768dc87853469b26ed6afef15d3e09e595909
- clm_c3544f193d90f5b2941cdd929e21f436acdb86c45b50b5769f2813f8eb7efe4f
- clm_cd4c4cb8b488ebfb9b85a4cf0a29023e340da6238da6bf33a37545cc49510146
- clm_db0689e4e1fc9fdfb930d96977d0c4203bde1e3d566e80f497b11a4d0db06956
- clm_e63cb73bd39e0753070f26cf188b3e805abc93c03a9e30544fc2e32f9d3281ff
- clm_ef6ccd1b88ec1c77f1d64c49abe2b8ed49747036ae78e3e4e466f868ed2b0a34
- clm_fb6caf8bfa167f383a746f378b714a3736ac956fb5f44764a5533ba02123d692
- clm_fd762139d56f0054f80cc703d8b9ef917667b0b5d9c823951b496d87dec5898a
maturity: draft
page_id: pg_d58fca4fae17576388628666534a08aa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_01d5a0a2df025f53aa60aaed62f93ecb
title: Tokfinity/InfCode/README.md @ 1dfd4c14a835
updated_at: '2026-09-14T03:19:51Z'
---

# Tokfinity/InfCode/README.md @ 1dfd4c14a835

<!-- rcw:begin owner=source:src_01d5a0a2df025f53aa60aaed62f93ecb block=evidence -->
- Auxiliary modules include an Image Builder (per-example container images stored locally and reused), a Tool Executor (runs commands in containers and returns outputs), and an LLM API Manager. [@claim:clm_2c01104390a38d7a52a30d586ad8825f364021fad2769f4141ed439c20c96294]
- Repository development practice: configuration lives in config/config.yaml with sections for providers, runner (concurrency, iterations), builder (Docker image build), and log settings. [@claim:clm_5cf254e6e1ed8c90a8b86f0f9e196079f6f64f54c43385de4e18c8055eb6fae0]
- An eval.sh script verifies generated patches using the official SWE-bench evaluation tool, with multi-process parallel evaluation (default 20 workers) and results including pass rates and failure reasons. [@claim:clm_68005e7d743b28f600a450b55d3e52d11d23f90e9887c1e525323b5d20690e08]
- A batch CLI (_batch_run.py) accepts flags for config file, run name, issue list, concurrency (default 20), output directory cleaning, and output directory. [@claim:clm_7635ee7dfab8b20122b5594403f9ee5467e48055bf0638cfe69f984a7b98ea8a]
- The system uses a dual-agent adversarial refinement framework that iteratively improves both test patches and code patches, aiming to produce fixes verified under strengthened test suites. [@claim:clm_7952de424bdccaa9757528a2c39691c57e1fdf44db4aefb5cd1350c785ff456b]
- Inside the Generator, a Test Patch Generator strengthens tests to expose faults while a Code Patch Generator refines patches to satisfy the enhanced tests, in an adversarial loop. [@claim:clm_7ca9a74339684ca7084e23faf0f2c19201ce74cac3f66e6acb7a1fcfa36cb04d]
- The Result Submitter tool runs git diff inside the container to obtain and return the generated patch content after the LLM finishes patch generation and testing. [@claim:clm_7f08e2eb308c1ce923702c5c449c2f9455d107f26d0a41c54db007862c128b6a]
- The project appears MIT-licensed and acknowledges anthropic-quickstart and bytedance's trae-agent as references for tool building. [@claim:clm_ae595767ed99c65b1312ade293bba5579142d045a5280cd2af734742293dd025]
- Agents interact with tools including File Editor (view/create/str_replace/insert), File Searcher, Bash Executor, and Result Submitter, all operating within containerized environments. [@claim:clm_aec938a77df1928f5bb99a69206768dc87853469b26ed6afef15d3e09e595909]
- InfCode adopts a generate-select architecture: Patch Generation produces candidate patches and Patch Selection picks the optimal one. [@claim:clm_c3544f193d90f5b2941cdd929e21f436acdb86c45b50b5769f2813f8eb7efe4f]
- The File Searcher tool is implemented on top of ripgrep, chosen for speed over traditional grep and fuzzy-matching support. [@claim:clm_cd4c4cb8b488ebfb9b85a4cf0a29023e340da6238da6bf33a37545cc49510146]
- Repository development practice: setup instructions direct users to create a .env file with API keys (e.g. OPENROUTER_API_KEY), install pip dependencies from requirements.txt, and ensure Docker is installed and running. [@claim:clm_db0689e4e1fc9fdfb930d96977d0c4203bde1e3d566e80f497b11a4d0db06956]
- The LLM API Manager invokes models via the completion endpoint and supports OpenAI, OpenRouter, DeepSeek clients, and self-hosted LLM instances. [@claim:clm_e63cb73bd39e0753070f26cf188b3e805abc93c03a9e30544fc2e32f9d3281ff]
- The README reports a 79.4% solution rate on SWE-Bench Verified, claimed as latest SOTA performance. [@claim:clm_ef6ccd1b88ec1c77f1d64c49abe2b8ed49747036ae78e3e4e466f868ed2b0a34]
- InfCode is described as an adversarial multi-agent code agent system that uses LLMs to automatically analyze and fix repository issues, developed by Tokfinity's Code Research team and Beihang University. [@claim:clm_fb6caf8bfa167f383a746f378b714a3736ac956fb5f44764a5533ba02123d692]
- The Patch Generator registers multiple generator groups, each in a separate container generating and repairing candidate patches in parallel, running up to 5 attempts and gathering all produced patches. [@claim:clm_fd762139d56f0054f80cc703d8b9ef917667b0b5d9c823951b496d87dec5898a]
<!-- rcw:end owner=source:src_01d5a0a2df025f53aa60aaed62f93ecb block=evidence -->

## Researcher notes

