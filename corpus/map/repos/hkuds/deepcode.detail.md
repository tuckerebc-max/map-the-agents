# hkuds/deepcode -- full detail

[Back to orientation](deepcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hkuds/deepcode/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/13ff9f4a8d3f5a21.json](../../../wiki/dossiers/hkuds/deepcode/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/13ff9f4a8d3f5a21.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Completion is evidence-driven rather than rule-based: the agent selects task-appropriate evidence such as test results, build output, static checks, diagnostics, diffs, or artifacts, and a failed verification feeds the next repair instead of being reported as success. -- evidence: [README.md#L681-L683](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L681-L683), [README.md#L677-L679](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L677-L679) (`clm_526e69148fffdc87e4a7a3e11afb11e8c5d99c0d0d39c5b7e0f77d4cace61d31`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are discovered from project `.agents/skills` and personal `~/.agents/skills`, plus bundled pinned upstream skills for authoring, review, security, frontend, MCP, and web testing; a Skill can narrow already-allowed tools but cannot grant new permissions. -- evidence: [README.md#L426-L430](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L426-L430), [README.md#L482-L501](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L482-L501), [README.md#L710-L715](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L710-L715), [README.md#L717-L719](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L717-L719) (`clm_e9bb72f0c587d495934aaf4fba94709f0fe3dc447123fe1984767ed52da03c4e`)
- [observation/documented] Skills can declare tool and skill dependencies that are expanded in order with cycle detection, failing before the first model request if a requirement is unavailable; sessions persist only skill identity, invocation kind, and revision, not the instruction body. -- evidence: [README.md#L482-L501](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L482-L501) (`clm_3718b754eab28a42da0e179bf0de1c1c7f055801699dff600343993ec63eb3f6`)

## interfaces (2 claim(s))

- [observation/documented] DeepCode ships TUI, Desktop, and Web clients over one shared local service, launched via `deepcode`, `deepcode desktop`, or `deepcode web`; all three share projects, sessions, models, skills, permissions, goals, and automations. -- evidence: [README.md#L637-L639](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L637-L639), [README.md#L81-L84](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L81-L84) (`clm_fd525f652754d207dd48211c085581357b7731c42653cd7f409cc12ecb4f02a2`)
- [observation/documented] The TUI exposes slash commands such as /model, /preset, /effort, /permissions, /transcript, /skill, /resume, /compact, and /context, with bare invocations opening a picker and argument forms keeping text paths. -- evidence: [README.md#L368-L404](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L368-L404), [README.md#L186-L197](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L186-L197), [README.md#L304-L316](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L304-L316) (`clm_3a88cdb910818510cdddaf176ee9708e816ef6b05336c0d616cd72e20de48e17`)

## memory-state (2 claim(s))

- [observation/documented] Sessions are stored locally and linked to their project, keeping tool calls, permission decisions, goals, model configuration, and verification records; history survives restarts and model switches, and compaction preserves the recent tail verbatim. -- evidence: [README.md#L691-L694](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L691-L694), [README.md#L248-L267](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L248-L267), [README.md#L566-L592](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L566-L592), [README.md#L687-L689](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L687-L689) (`clm_06969276b3a98a4869f3a2f25a5dccbd9832a791f96cd33a6f382a8221d2cfd8`)
- [observation/documented] Compaction summaries are written into workspace memory on a background thread, and injected memory content is wrapped in an escaped `<untrusted-data>` boundary so a poisoned note cannot forge instructions. -- evidence: [README.md#L186-L197](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L186-L197) (`clm_a3bdcb20d3f2d6fc2f9513dabdae78f6acdbd83a71228f68273bdf8160e9ea40`)

## orchestration (2 claim(s))

- [observation/documented] For multi-step work, users give a natural-language Goal and the agent loops through analyzing, implementing, verifying, and fixing; users can add requirements, revise the goal, queue instructions, or pause, stop, and resume while it runs. -- evidence: [README.md#L537-L555](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L537-L555), [README.md#L660-L662](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L660-L662), [README.md#L666-L670](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L666-L670), [README.md#L664-L664](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L664-L664) (`clm_e82ef438f974b5aa0242d88f7e21bed91370c64b7c65b1a904b687731fa7a9b0`)
- [observation/documented] Complex work can be split across focused parallel agents that run in isolated Git worktrees to avoid editing the same directory; conflicts are surfaced explicitly and the main agent owns the final goal. -- evidence: [README.md#L736-L737](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L736-L737), [README.md#L739-L742](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L739-L742), [README.md#L566-L592](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L566-L592) (`clm_0ed3360e813d3487b706ad97c3bb57bf1a097d0868e24ee7a4be376600e75be1`)

## tools-permissions (2 claim(s))

- [observation/documented] Projects must be explicitly trusted before execution, and each session uses one of three modes: Ask (confirm sensitive operations), Read only, or Full access; individual tools also support allow, ask, and deny settings shared between CLI and Desktop. -- evidence: [README.md#L726-L728](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L726-L728), [README.md#L730-L732](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L730-L732), [README.md#L723-L724](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L723-L724) (`clm_674ef61b2b0b45162c14489af92a761e146d9afafe61600dd35cf25a5b53f94d`)
- [observation/documented] Command execution includes a sandbox as the security boundary, with a legacy dangerous-command screen matching on argv (not substrings) as a cheap first pass, and native file commands declining operands outside the working directory. -- evidence: [README.md#L201-L214](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L201-L214), [README.md#L229-L232](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L229-L232) (`clm_0eacd21a288181e5cd3ef9da5467fee8f5a9ce8bf6bc5c172a987a6fd275835c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The agent is model-provider agnostic, supporting OpenRouter, OpenAI, Anthropic, DeepSeek, Gemini, OpenAI-compatible gateways, Ollama, vLLM, and other compatible endpoints with the user's own API key; the README badge indicates Python 3.12+. -- evidence: [README.md#L37-L53](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L37-L53), [README.md#L698-L700](https://github.com/HKUDS/DeepCode/blob/4bb4fd9cb9e8261cba5b5575e4cefe2acfc9c9d2/README.md#L698-L700) (`clm_c05868133baa7c64ea4ca4e40e503df30ab8f1bb0f97186c1084ac287d784e88`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

