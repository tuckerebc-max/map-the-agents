---
access: public
aliases: []
claim_ids:
- clm_16fc195e30b88a6f14b3c4327b712a21a8e9a48e454e2eb808cb1d3f047c6a00
- clm_25a22abb2fce87d1fdebcc579ff996b5087be6662439dbec544342611709e7ab
- clm_40e8742748f4b353e4ab660fa9abb1d37056bbfa74d9b9ca256705cdcff6697b
- clm_4170e27e02cc42fc0cdb0a3b06496b14d3a24e1eb0e926a39a46cdc164378528
- clm_48a92d73476203355692fa7c90fb2535b48f5d4841e452f12384498c7abd6248
- clm_5d66398481cecc9e6dca38a982a4972da34aedd4647540ca7b9dd29dfb03572d
- clm_6de23617388c9955e472d89de91b27965f3e49d63b4fcb1a3edd41d793b0e82a
- clm_87b8ad6587bdbdd17dfcd877e5a0b68cce67d0c668b26c9db35865373c468892
- clm_d46d9cd4fa4a473c72a80352c464eda15edba5034589e4ffab62e9bf3b901f48
- clm_de4b3dcc199b979c1c8a31ca1cba229cf0effd5b92a3eb30f1550755b4f825bd
- clm_e0755b3cbd2e4cf37b6c09685056b0fb17121a4f24ecd2ec96aa16ceba3db888
- clm_ed74e1f69cdf1d5dcd11f67b12bf2314572b3a3f62ca2ae79938e737b55f069e
maturity: draft
page_id: pg_55cce2f76d6756a28f9e03e52cbd073a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ce90548df0915fd4ac0aa79055f26175
title: smol-ai/developer/readme.md @ a6747d1a6ccd
updated_at: '2026-09-14T02:40:55Z'
---

# smol-ai/developer/readme.md @ a6747d1a6ccd

<!-- rcw:begin owner=source:src_ce90548df0915fd4ac0aa79055f26175 block=evidence -->
- Community forks exist in JS/TS, C#/.NET, and Go, and the README links demos including a Chrome extension and a React/Node/MongoDB full-stack scaffold. [@claim:clm_16fc195e30b88a6f14b3c4327b712a21a8e9a48e454e2eb808cb1d3f047c6a00]
- Generation is slow: the README reports roughly 2-4 minutes to generate a program with GPT4 even with parallelization via Modal, occasionally spiking higher. [@claim:clm_25a22abb2fce87d1fdebcc579ff996b5087be6662439dbec544342611709e7ab]
- The tool is described as a 'junior developer' agent that scaffolds an entire codebase from a product spec, or provides building blocks to embed a similar agent in other apps. [@claim:clm_40e8742748f4b353e4ab660fa9abb1d37056bbfa74d9b9ca256705cdcff6697b]
- The workflow is human-in-the-loop: the human writes/extends a markdown prompt, runs generated code, and pastes errors back into the prompt; debugger.py reads the whole codebase to suggest specific fixes. [@claim:clm_4170e27e02cc42fc0cdb0a3b06496b14d3a24e1eb0e926a39a46cdc164378528]
- The shared_dependencies.md approach is acknowledged as imperfect, sometimes not comprehensive about hard dependencies between files, requiring explicit names in the prompt as a workaround. [@claim:clm_48a92d73476203355692fa7c90fb2535b48f5d4841e452f12384498c7abd6248]
- For whole-program coherence, the tool adds an intermediate step generating shared_dependencies.md and insists on using it when generating each file, since hallucinated cross-file dependencies break programs. [@claim:clm_5d66398481cecc9e6dca38a982a4972da34aedd4647540ca7b9dd29dfb03572d]
- Library mode exposes functions plan(), specify_file_paths(), and generate_code_sync() from smol_dev.prompts, plus an async generate_code() variant, installable via pip as smol_dev. [@claim:clm_6de23617388c9955e472d89de91b27965f3e49d63b4fcb1a3edd41d793b0e82a]
- The repo is installed with poetry ('poetry install') in git repo mode, and the library is published as the pip package smol_dev. [@claim:clm_87b8ad6587bdbdd17dfcd877e5a0b68cce67d0c668b26c9db35865373c468892]
- specify_file_paths reportedly relies on OpenAI's Function Calling API to guarantee JSON output of file paths. [@claim:clm_d46d9cd4fa4a473c72a80352c464eda15edba5034589e4ffab62e9bf3b901f48]
- In git repo mode the CLI is run as 'python main.py' with a prompt string argument, defaulting to gpt-4-0613, and supports --prompt and --debug flags. [@claim:clm_de4b3dcc199b979c1c8a31ca1cba229cf0effd5b92a3eb30f1550755b4f825bd]
- An API mode implements the Agent Protocol: start with 'poetry run api' or 'python smol_dev/api.py', then create tasks and execute steps via POST endpoints on localhost:8000. [@claim:clm_e0755b3cbd2e4cf37b6c09685056b0fb17121a4f24ecd2ec96aa16ceba3db888]
- Using Anthropic as the coding layer reportedly does not work well because Anthropic does not follow instructions to generate file code reliably. [@claim:clm_ed74e1f69cdf1d5dcd11f67b12bf2314572b3a3f62ca2ae79938e737b55f069e]
<!-- rcw:end owner=source:src_ce90548df0915fd4ac0aa79055f26175 block=evidence -->

## Researcher notes

