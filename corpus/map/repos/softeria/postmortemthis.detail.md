# softeria/postmortemthis -- full detail

[Back to orientation](postmortemthis.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/softeria/postmortemthis/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/cd1cf2daf51dc0f0.json](../../../wiki/dossiers/softeria/postmortemthis/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/cd1cf2daf51dc0f0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product is described as a single small script that installs, updates, and runs all the agents on Windows, macOS, and Linux, with no server or MCP required. -- evidence: [README.md#L11-L11](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L11-L11) (`clm_ea01a76bb5e758d13ca9c68c8ad398be3e27ce336952d92c21efb7600031f40c`)

## design-choices (2 claim(s))

- [observation/documented] Grok is run through an OpenAI-compatible harness against the OpenRouter model x-ai/grok-build-0.1, since Grok's own CLI cannot reach OpenRouter. -- evidence: [README.md#L30-L30](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L30-L30) (`clm_6ce8b38c0e210435c12601f8b2371b8a5b4a9dedfd9d5b0e93d2d447562d3d53`)
- [observation/documented] The design keeps the user inside their own agent, which makes the final call, while the external agents only read the diff; the script is described as the only fixed part of the system. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9), [README.md#L24-L24](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L24-L24) (`clm_3551f3e984d483d060a6f5956da13eab791355a510486b5a1ab0e5dbb37d6e6e`)

## workflows (1 claim(s))

- [observation/documented] A `setup` command probes each agent, lets the user log in, force OpenRouter, or disable an agent, optionally fires a test prompt, and saves the choices for later runs. -- evidence: [README.md#L32-L32](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L32-L32) (`clm_4e7e58d859372c706bfc3c119cc90fdf2f6189973539cc8d87ec101a03a2fc16`)

## skills-patterns (1 claim(s))

- [observation/documented] Installation is prompt-driven: the user pastes a prompt that makes their coding agent create a /postmortemthis skill, downloading the .cmd script once into the skill folder; the repo's SKILL.md is described as a starting point. -- evidence: [README.md#L24-L24](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L24-L24), [README.md#L17-L20](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L17-L20) (`clm_396f0a5dc8223be646839082bd6331e6110ab12fb269d66185e7d18ea6ec0e38`)

## interfaces (1 claim(s))

- [observation/documented] The tool is invoked as a shell script: piping a prompt to `sh postmortemthis.cmd` runs it across all agents, with `setup` and `doctor` subcommands for configuration and availability checks. -- evidence: [README.md#L36-L40](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L36-L40) (`clm_e55ff74319cdb43b20b074a3a5f2c4faa169fa9489f4a8dde42e7f4d88571949`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] It runs one prompt across several coding-agent CLIs (Claude Code, Codex, Antigravity, Qwen, Vibe, Grok) in parallel, each reading the current diff. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9), [README.md#L17-L20](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L17-L20) (`clm_55f18fecfc63c413d6278f1140f7475275a087c0149e918ca865bf38e83a23be`)

## tools-permissions (1 claim(s))

- [observation/documented] Read-only operation is enforced by each agent's own CLI, except Antigravity which lacks such a switch and is instead constrained via its plan mode; the user is notified if the tree changes during a run. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9) (`clm_2a3accaea063c5b2034e3021746828036e5691cc3cbabd138bceba84756b850b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool depends on the user's installed coding-agent CLIs and their logins; for agents without access, OpenRouter is used via OAuth login or an OPENROUTER_API_KEY, with usage billed to the user's account. -- evidence: [README.md#L28-L28](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L28-L28) (`clm_a5af11315f5cad9e7c39df4a5ffeeae36dd11b5bbacfeb0d37cdc34fffeeb863`)

## limitations (1 claim(s))

- [observation/documented] Per the README, read-only enforcement is not uniform: Antigravity's CLI has no read-only switch, so it is held to read-only behavior only through its plan mode. -- evidence: [README.md#L9-L9](https://github.com/Softeria/postmortemthis/blob/37f38fea5a621e7c06669625f3cc2ee3f0c895ab/README.md#L9-L9) (`clm_33d6b7b3148a0696b260f02ed4a3f6387f5f9f2933b90c04950ab5b8956c7a4e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

