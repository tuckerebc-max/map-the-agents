---
access: public
aliases: []
claim_ids:
- clm_0d2c6407043f93932ea467ed70c3d65bd76bf7093381a73dc2821fc9257c2103
- clm_13fcef1ae52698d9948197d72669883f086d8f6ba7fe9b83d1bf8b6b564b0094
- clm_1caa37303fed99480a7ce966db1b0a01d4faf742ee8cc7666f21d0c75e7565f5
- clm_1cf045c138894d6a98637646e2305274b22e7959a56bbe93359f3d84ea2ff5ea
- clm_3367429383423186304e142183e99eab653d1e43ca258d6590092ce051076d5e
- clm_3d756c464c48877f6ac4619ca3be8b4701cd7b35802ae6efd521137287be81d7
- clm_74c4f58be9edf75c088f9459d5f638f508d6404b9af72586c89041a08d99b668
- clm_79f46fb8f916fcbf0fed1fc9d1b87f8f456f71e8fd20e20e28ed0177f71a7c75
- clm_b686418741edf4ba6d7a9d48a3ce12436e74572079770c3e84db5c1db8dd2d37
- clm_cd5435c7dff41ff183a8e3789f41666f895d9d386fbb3e2e139e8f2686a44acf
- clm_e12e970d694a1febeaa1801002dcccda5099b5bbf805f01114ca64e32074a48c
maturity: draft
page_id: pg_3d069e2c7df350e0a3fdcc96a913ae92
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b55226a6a8a25a78af53881cbe5f5802
title: scaleapi/SWE-Interact/README.md @ b32f98c3b8f7
updated_at: '2026-09-14T04:19:37Z'
---

# scaleapi/SWE-Interact/README.md @ b32f98c3b8f7

<!-- rcw:begin owner=source:src_b55226a6a8a25a78af53881cbe5f5802 block=evidence -->
- Modal is set up to provide sandbox environments, via installing the modal package with uv pip and running modal setup. [@claim:clm_0d2c6407043f93932ea467ed70c3d65bd76bf7093381a73dc2821fc9257c2103]
- Per-agent configs require different credentials: Codex configs need only the common block, Claude Code configs need ANTHROPIC_API_KEY, OpenCode needs GEMINI_API_KEY, and kimi-cli needs an OpenAI-compatible endpoint. [@claim:clm_13fcef1ae52698d9948197d72669883f086d8f6ba7fe9b83d1bf8b6b564b0094]
- The work is associated with an arXiv paper (2606.30573) titled 'SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions' by Raghavendra, Gunjal, Sabharwal, and He. [@claim:clm_1caa37303fed99480a7ce966db1b0a01d4faf742ee8cc7666f21d0c75e7565f5]
- Runs are launched from the repository root by executing a run config script, e.g. bash run_configs/multiturn/gpt-5p5-high_codex.sh; a single-turn baseline example is also provided. [@claim:clm_1cf045c138894d6a98637646e2305274b22e7959a56bbe93359f3d84ea2ff5ea]
- Multi-turn run configs set the simulated user model to openai/gpt-5.5 through the SIM_USER_MODEL variable. [@claim:clm_3367429383423186304e142183e99eab653d1e43ca258d6590092ce051076d5e]
- Run scripts write outputs under results/, and custom configs are made by copying an existing script and adjusting the agent, model, sampling count, or Harbor arguments. [@claim:clm_3d756c464c48877f6ac4619ca3be8b4701cd7b35802ae6efd521137287be81d7]
- The repository ships task data under data/multiturn and example run configs under run_configs/multiturn that correspond to that data directory. [@claim:clm_74c4f58be9edf75c088f9459d5f638f508d6404b9af72586c89041a08d99b668]
- The benchmark uses a simulated user (GPT 5.5 high) and rubric grading; the RF task default rubric model is Anthropic Opus 4.5, matching the original SWE Atlas Refactoring task. [@claim:clm_79f46fb8f916fcbf0fed1fc9d1b87f8f456f71e8fd20e20e28ed0177f71a7c75]
- Running the tasks requires installing Harbor, done by cloning the laude-institute/harbor repository and installing it with uv tool install. [@claim:clm_b686418741edf4ba6d7a9d48a3ce12436e74572079770c3e84db5c1db8dd2d37]
- The configured API gateway must support both openai/gpt-5.5 and the rubric model anthropic/claude-opus-4-5-20251101; a LiteLLM gateway works, while direct OpenAI endpoints need an EVAL_MODEL override. [@claim:clm_cd5435c7dff41ff183a8e3789f41666f895d9d386fbb3e2e139e8f2686a44acf]
- Run configs load credentials from a harbor/.env file located relative to the repository root, which must be created before launching a run. [@claim:clm_e12e970d694a1febeaa1801002dcccda5099b5bbf805f01114ca64e32074a48c]
<!-- rcw:end owner=source:src_b55226a6a8a25a78af53881cbe5f5802 block=evidence -->

## Researcher notes

