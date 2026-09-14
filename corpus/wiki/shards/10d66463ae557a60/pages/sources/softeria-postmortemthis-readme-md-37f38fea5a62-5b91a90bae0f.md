---
access: public
aliases: []
claim_ids:
- clm_2a3accaea063c5b2034e3021746828036e5691cc3cbabd138bceba84756b850b
- clm_33d6b7b3148a0696b260f02ed4a3f6387f5f9f2933b90c04950ab5b8956c7a4e
- clm_3551f3e984d483d060a6f5956da13eab791355a510486b5a1ab0e5dbb37d6e6e
- clm_396f0a5dc8223be646839082bd6331e6110ab12fb269d66185e7d18ea6ec0e38
- clm_4e7e58d859372c706bfc3c119cc90fdf2f6189973539cc8d87ec101a03a2fc16
- clm_55f18fecfc63c413d6278f1140f7475275a087c0149e918ca865bf38e83a23be
- clm_6ce8b38c0e210435c12601f8b2371b8a5b4a9dedfd9d5b0e93d2d447562d3d53
- clm_a5af11315f5cad9e7c39df4a5ffeeae36dd11b5bbacfeb0d37cdc34fffeeb863
- clm_e55ff74319cdb43b20b074a3a5f2c4faa169fa9489f4a8dde42e7f4d88571949
- clm_ea01a76bb5e758d13ca9c68c8ad398be3e27ce336952d92c21efb7600031f40c
maturity: draft
page_id: pg_007b8f023d5152958aa05b91a90bae0f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_69067cef4cac5fb5a3bca5618ae26977
title: Softeria/postmortemthis/README.md @ 37f38fea5a62
updated_at: '2026-09-14T02:40:58Z'
---

# Softeria/postmortemthis/README.md @ 37f38fea5a62

<!-- rcw:begin owner=source:src_69067cef4cac5fb5a3bca5618ae26977 block=evidence -->
- Read-only operation is enforced by each agent's own CLI, except Antigravity which lacks such a switch and is instead constrained via its plan mode; the user is notified if the tree changes during a run. [@claim:clm_2a3accaea063c5b2034e3021746828036e5691cc3cbabd138bceba84756b850b]
- Per the README, read-only enforcement is not uniform: Antigravity's CLI has no read-only switch, so it is held to read-only behavior only through its plan mode. [@claim:clm_33d6b7b3148a0696b260f02ed4a3f6387f5f9f2933b90c04950ab5b8956c7a4e]
- The design keeps the user inside their own agent, which makes the final call, while the external agents only read the diff; the script is described as the only fixed part of the system. [@claim:clm_3551f3e984d483d060a6f5956da13eab791355a510486b5a1ab0e5dbb37d6e6e]
- Installation is prompt-driven: the user pastes a prompt that makes their coding agent create a /postmortemthis skill, downloading the .cmd script once into the skill folder; the repo's SKILL.md is described as a starting point. [@claim:clm_396f0a5dc8223be646839082bd6331e6110ab12fb269d66185e7d18ea6ec0e38]
- A `setup` command probes each agent, lets the user log in, force OpenRouter, or disable an agent, optionally fires a test prompt, and saves the choices for later runs. [@claim:clm_4e7e58d859372c706bfc3c119cc90fdf2f6189973539cc8d87ec101a03a2fc16]
- It runs one prompt across several coding-agent CLIs (Claude Code, Codex, Antigravity, Qwen, Vibe, Grok) in parallel, each reading the current diff. [@claim:clm_55f18fecfc63c413d6278f1140f7475275a087c0149e918ca865bf38e83a23be]
- Grok is run through an OpenAI-compatible harness against the OpenRouter model x-ai/grok-build-0.1, since Grok's own CLI cannot reach OpenRouter. [@claim:clm_6ce8b38c0e210435c12601f8b2371b8a5b4a9dedfd9d5b0e93d2d447562d3d53]
- The tool depends on the user's installed coding-agent CLIs and their logins; for agents without access, OpenRouter is used via OAuth login or an OPENROUTER_API_KEY, with usage billed to the user's account. [@claim:clm_a5af11315f5cad9e7c39df4a5ffeeae36dd11b5bbacfeb0d37cdc34fffeeb863]
- The tool is invoked as a shell script: piping a prompt to `sh postmortemthis.cmd` runs it across all agents, with `setup` and `doctor` subcommands for configuration and availability checks. [@claim:clm_e55ff74319cdb43b20b074a3a5f2c4faa169fa9489f4a8dde42e7f4d88571949]
- The product is described as a single small script that installs, updates, and runs all the agents on Windows, macOS, and Linux, with no server or MCP required. [@claim:clm_ea01a76bb5e758d13ca9c68c8ad398be3e27ce336952d92c21efb7600031f40c]
<!-- rcw:end owner=source:src_69067cef4cac5fb5a3bca5618ae26977 block=evidence -->

## Researcher notes

