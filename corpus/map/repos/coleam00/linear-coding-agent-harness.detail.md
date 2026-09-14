# coleam00/linear-coding-agent-harness -- full detail

[Back to orientation](linear-coding-agent-harness.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coleam00/linear-coding-agent-harness/c37dc096993011cb0cc48a0afab176cd9c8f2375/d9f454e04233bbea.json](../../../wiki/dossiers/coleam00/linear-coding-agent-harness/c37dc096993011cb0cc48a0afab176cd9c8f2375/d9f454e04233bbea.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The repository includes modules for agent session logic, Claude SDK/MCP client configuration, security validation, progress tracking, prompt loading, and Linear configuration constants, plus prompt files for both agent roles. -- evidence: [README.md#L134-L148](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L134-L148) (`clm_2ca5c2316937bebc9d8de3e618d020ba99a37b6f0cd8df11f414401fa12b84a4`)
- [observation/documented] Two MCP servers are used: Linear over Streamable HTTP for issue/status/comment management, and Puppeteer over stdio for browser-based UI testing. -- evidence: [README.md#L165-L168](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L165-L168) (`clm_f02865e7349fae78db6de377cd6186055c5bd38c4e33153d8608c25c12a16416`)

## design-choices (2 claim(s))

- [observation/documented] The demo implements a two-agent pattern: an initializer agent that sets up the Linear project and issues, and a coding agent that implements them. -- evidence: [README.md#L7-L12](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L7-L12), [README.md#L3-L3](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L3-L3) (`clm_15fb0436c39a19e24c9b79c6ca7854bafdad0e0a00ce4dfa8616107cb93ca7b0`)
- [observation/documented] All work tracking and inter-agent communication happens through Linear issues, comments, and status transitions rather than local text files. -- evidence: [README.md#L112-L115](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L112-L115), [README.md#L7-L12](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L7-L12) (`clm_936ec1081078c657e68c24358c811c53f7dcf5a090f771b3ca47749d03454f8a`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The entry point is autonomous_agent_demo.py, invoked with --project-dir, with optional --max-iterations (default unlimited) and --model (default claude-opus-4-5-20251101) flags. -- evidence: [README.md#L58-L61](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L58-L61), [README.md#L54-L56](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L54-L56), [README.md#L126-L130](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L126-L130) (`clm_7a293a8c57aa685022deaf9f24fa830eb428202fe4fe364a16a5a80461a97b12`)

## memory-state (1 claim(s))

- [observation/documented] Generated projects contain a .linear_project.json marker file holding Linear project state, alongside the copied spec, init.sh, and .claude_settings.json security settings. -- evidence: [README.md#L154-L161](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L154-L161) (`clm_88a412ddd9a8647bc6d4fdf655a4d15e02e60f8cff9023c01594671f2934d6ec`)

## orchestration (2 claim(s))

- [observation/documented] The initializer agent reads app_spec.txt, creates a Linear project, generates 50 detailed issues, creates a META issue for session tracking, and sets up project structure, init.sh, and git. -- evidence: [README.md#L187-L190](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L187-L190), [README.md#L93-L98](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L93-L98) (`clm_68e7fb7b7505587796df7638005783276c414a28a66d1fe96aeddd71f4d52297`)
- [observation/documented] The coding agent queries Linear for the highest-priority Todo issue, claims it, implements and tests the feature, comments on the issue, marks it Done, and updates the META issue with a session summary. -- evidence: [README.md#L100-L108](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L100-L108) (`clm_bbb648958a017c3fb6c6e1d341182e35773fb4152c576934ebdbe96781b05868`)

## tools-permissions (2 claim(s))

- [observation/documented] The runtime uses a defense-in-depth security model: OS-level sandboxing of bash commands, filesystem restrictions to the project directory, a bash command allowlist, and explicit MCP tool permissions. -- evidence: [README.md#L174-L177](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L174-L177), [README.md#L172-L172](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L172-L172) (`clm_046c0a6e0a5d1af08bca75e702ec3c4d2530bd60caf36c85d3923c6d290fa637`)
- [observation/documented] The bash allowlist permits only specific commands such as npm, node, and git, and is configurable via ALLOWED_COMMANDS in security.py. -- evidence: [README.md#L174-L177](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L174-L177), [README.md#L206-L206](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L206-L206), [README.md#L219-L220](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L219-L220) (`clm_c4a4b12f1f15604ad78cf01360ce792e5c8a180bf0776089b8f03a3a1751e756`)

## evaluation (1 claim(s))

- [inference/documented] The coding agent appears to verify previously completed features and test new ones via Puppeteer browser automation, though no benchmark or success-rate metrics are documented. -- evidence: [README.md#L100-L108](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L100-L108), [README.md#L7-L12](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L7-L12) (`clm_8da806ec88a5b9b09e1e5656a1f9ace793ddcbd6334a34359f1c564f4cdea000`)

## dependencies (2 claim(s))

- [observation/documented] The project requires the Claude Code CLI installed globally via npm and Python dependencies from requirements.txt, which pins claude-code-sdk>=0.0.25. -- evidence: [README.md#L23-L24](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L23-L24), [README.md#L20-L20](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L20-L20), [requirements.txt#L1-L1](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/requirements.txt#L1-L1) (`clm_7644cf6ab4f2fb2a412be03388876cb38e50467171ca65774d399ed1cbc3163c`)
- [observation/documented] Two environment variables are required at runtime: CLAUDE_CODE_OAUTH_TOKEN (from claude setup-token) and LINEAR_API_KEY for MCP access. -- evidence: [README.md#L119-L122](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L119-L122) (`clm_f3d7ee020109e6940489f0bce0bf79b2b4412feb7a2c1631ff983d182da231f7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

