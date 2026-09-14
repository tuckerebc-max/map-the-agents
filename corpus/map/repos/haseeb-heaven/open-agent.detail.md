# haseeb-heaven/open-agent -- full detail

[Back to orientation](open-agent.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/haseeb-heaven/open-agent/575401684ec13df646fa831f1c824388b5b30574/37fd1230e5bca33c.json](../../../wiki/dossiers/haseeb-heaven/open-agent/575401684ec13df646fa831f1c824388b5b30574/37fd1230e5bca33c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] A web search tool (google_web_search) auto-selects a backend from available keys, with a no-key fallback chain of Exa (hosted MCP) then DuckDuckGo, and supports Brave, Tavily, and Serper, forcible via WEB_SEARCH_PROVIDER. -- evidence: [README.md#L93-L94](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L93-L94), [README.md#L83-L85](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L83-L85) (`clm_3309447abf730f003b0a346f99dc0a4c49d6b284260cf4854c6cddc799fefce2`)
- [observation/documented] Model definitions live in a registry file configs/models.toml, referenced from the README alongside a full matrix in Models.MD. -- evidence: [README.md#L113-L114](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L113-L114) (`clm_72e29153a1b938bae6668649d18a9b37493835887ed2795639b83140672538e6`)

## design-choices (2 claim(s))

- [observation/documented] The tool is positioned as local-first and BYOK: it supports free OpenRouter models, local Ollama/LM Studio, runs on Windows/Mac/Linux, and requires no account. -- evidence: [README.md#L12-L13](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L12-L13), [README.md#L24-L25](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L24-L25) (`clm_48e2c63efded4442153e778be4db95df3283d21b7f6db3301eeab5ba2382193b`)
- [observation/documented] The project is a fork of Google's Gemini CLI (Apache-2.0) with modifications by Haseeb Mir, and is itself licensed Apache-2.0. -- evidence: [README.md#L180-L181](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L180-L181), [README.md#L185-L185](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L185-L185) (`clm_2a90ca5fcfb6bc246d49970c362b7f29a134f6fb8053b4a0b3adde4c1c7dd425`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: tests run from repo root with npm test using Vitest, which auto-loads root .env (missing keys skip; live quota soft-skips); unit and live provider test commands are documented, with live tests gated by RUN_LIVE_PROVIDER_TESTS / RUN_LOCAL_PROVIDER_TESTS env vars. -- evidence: [README.md#L163-L163](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L163-L163), [README.md#L167-L168](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L167-L168), [README.md#L156-L157](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L156-L157), [README.md#L165-L165](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L165-L165), [README.md#L153-L154](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L153-L154) (`clm_5441a2e6c3f6353140a6343b08ec26f6e7481d1eae09875704ed271f54863bb8`)
- [observation/documented] Repository development practice: canonical agent instructions for AI coding agents working in this repo live in OPENAGENT.md, referenced from GEMINI.md as applying to Claude Code, Gemini CLI, Codex, opencode, and OpenAgent itself. -- evidence: [GEMINI.md#L3-L5](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/GEMINI.md#L3-L5) (`clm_1a267d1f9e59ecbe3f9857f319f910fd34fac681ce0ec2aa22a46761640b06f9`)

## skills-patterns (1 claim(s))

- [observation/documented] Agent Skills follow a lifecycle of discovery (metadata injected into the system prompt), activation via an activate_skill tool, user consent, injection of SKILL.md content, and execution; skills are discovered from built-in, extension, user (~/.openagent/skills/), and workspace (.openagent/skills/) tiers with precedence rules. -- evidence: [docs/cli/skills.md#L40-L48](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L40-L48), [docs/cli/skills.md#L52-L55](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L52-L55), [docs/cli/skills.md#L20-L33](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L20-L33) (`clm_9c07edf6b8f8ff4d1190fe96579f0b71919b6fbdc401b131f35fcf1fa29410ba`)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes flags including --provider, -m/--model, --free, --models, --byok, and -y/--yolo for auto-approving tools in trusted workspaces. -- evidence: [README.md#L116-L123](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L116-L123) (`clm_22f4fa86ee392f64e6390e9420e18aff548b990b1a3813c3c5a990273a2732c6`)
- [observation/documented] Interactive sessions support slash commands such as /models, /byok, /websearch, and /skills subcommands (list, link, enable, disable, reload). -- evidence: [README.md#L60-L60](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L60-L60), [docs/cli/skills.md#L92-L99](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L92-L99) (`clm_46cdf845cb15ed25573e62229f3861127c7e235e94501c86bef3a11792babc2a`)
- [observation/documented] Extensions install from the Slack marketplace or Claude .claude-plugin manifests (plus open-agent-extension.json and .mcp.json formats) via --install-extension, with --auto skipping trust prompts for trusted extensions. -- evidence: [README.md#L127-L128](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L127-L128), [README.md#L135-L138](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L135-L138), [README.md#L140-L141](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L140-L141), [README.md#L130-L133](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L130-L133) (`clm_bb97f98c3b39d626bef4e5d449a9f80a2a6a3dd4215b80c5e14c8d44c9523ccd`)

## memory-state (1 claim(s))

- [observation/documented] The agent persists durable facts and preferences by editing Markdown memory files: shared project instructions in OPENAGENT.md, private notes in a per-project folder, and personal preferences in ~/.openagent/OPENAGENT.md, loaded into future sessions' context. -- evidence: [docs/tools/memory.md#L8-L11](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/tools/memory.md#L8-L11), [docs/tools/memory.md#L3-L4](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/tools/memory.md#L3-L4), [docs/tools/memory.md#L15-L19](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/tools/memory.md#L15-L19) (`clm_c617d814fd8de28670bb3c0326c61e1334b9856a7562f78c2513efc14d874f14`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (3 claim(s))

- [observation/documented] Sandboxing can be enabled via the -s/--sandbox flag, the OPENAGENT_SANDBOX env var (docker, podman, sandbox-exec, runsc, lxc, with legacy GEMINI_SANDBOX alias), or settings.json, in that precedence order. -- evidence: [docs/cli/sandbox.md#L75-L80](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L75-L80), [docs/cli/sandbox.md#L73-L73](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L73-L73) (`clm_e193c63cea3e784214f330ee56e1ac19e4f123666a3daa67cb426fad634255e1`)
- [observation/documented] A 'Sandbox Expansion Request' mechanism lets the agent ask for extra permissions (directories, network) when a sandboxed command is denied or proactively flagged, executed only after user approval for that run. -- evidence: [docs/cli/sandbox.md#L302-L305](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L302-L305), [docs/cli/sandbox.md#L309-L314](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L309-L314), [docs/cli/sandbox.md#L299-L300](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L299-L300) (`clm_034d9f2726efc55bc1b8b61472a3cb2c4b7435cc0dfe0a13f07f8007aa7ee584`)
- [observation/documented] macOS Seatbelt sandboxing offers profiles (permissive-open default, permissive-proxied, restrictive-*, strict-*) selected via the SEATBELT_PROFILE env var, controlling write and network restrictions. -- evidence: [docs/cli/sandbox.md#L96-L101](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L96-L101), [docs/cli/sandbox.md#L91-L92](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L91-L92) (`clm_6327d588d85fdc9505c10bace3cd7ec0cf7d455216763f2c08866c280019c36c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project requires Node.js 22+ and is published on npm as @haseeb_heaven/open-agent, installable globally with npm install -g. -- evidence: [README.md#L29-L29](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L29-L29), [README.md#L34-L37](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L34-L37), [README.md#L31-L32](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L31-L32) (`clm_bc552c8bb4c9506aa2ba14f95e6498304c955b506af5d878d7978ddcb3e38fa6`)
- [observation/documented] Cloud providers are configured via per-provider environment variables (e.g. OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY), while local Ollama and LM Studio need no key. -- evidence: [README.md#L64-L65](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L64-L65), [README.md#L67-L79](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L67-L79) (`clm_1c1f6a71d7299884be3e3e3131414a10ed170939206e5b50e4184e154d56d023`)

## limitations (2 claim(s))

- [observation/documented] LXC/LXD sandboxing is Linux-only and experimental: the container must already exist and be running before starting open-agent, which does not create it automatically, and the workspace must be writable at the same absolute path inside the container. -- evidence: [docs/cli/sandbox.md#L233-L236](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L233-L236), [docs/cli/sandbox.md#L226-L229](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L226-L229), [docs/cli/sandbox.md#L262-L266](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L262-L266) (`clm_a56667b19e5ead01debe255e8bcd864f3c171dc0425718866fee2fc03234d132`)
- [observation/documented] The docs note sandboxing reduces but does not eliminate risk, and GUI applications may not work inside sandboxes. -- evidence: [docs/cli/sandbox.md#L465-L468](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/sandbox.md#L465-L468) (`clm_12f396a2de65bc00993fb3d150ecdedf95e292e3d7a7cb8b6e2271714a11f29e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

