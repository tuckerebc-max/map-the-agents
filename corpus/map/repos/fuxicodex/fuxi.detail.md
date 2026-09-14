# fuxicodex/fuxi -- full detail

[Back to orientation](fuxi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fuxicodex/fuxi/ab2785904754a3ca695e7cef1c1238496d0b1697/2d08cae774751f9b.json](../../../wiki/dossiers/fuxicodex/fuxi/ab2785904754a3ca695e7cef1c1238496d0b1697/2d08cae774751f9b.json)

## specifications (1 claim(s))

- [observation/documented] FuXi is documented as a terminal AI coding agent built in Go, shipped as a single static binary with no runtime dependencies, positioned as a provider-agnostic alternative to Claude Code. -- evidence: [README.md#L12-L17](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L12-L17) (`clm_1ed1e451ac0798b98b6ec6988e60c30f7fe95b1295ba005cb4d95d63a9a993da`)

## components (1 claim(s))

- [observation/documented] Documentation claims 50+ built-in tools including file read/write/edit, bash and PowerShell shell, ripgrep search, web fetch, LSP diagnostics, Jupyter, browser use, background tasks, and parallel sub-agents. -- evidence: [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82) (`clm_bd5f199b443d927b519e8170830ebb4e569be917b8e713abee7f7923d0a21f1e`)

## design-choices (1 claim(s))

- [observation/documented] The agent is described as running a Think → Act → Verify loop: it reasons about a task, acts with built-in tools, inspects results, and iterates until the work is verified. -- evidence: [docs/faq.md#L70-L72](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L70-L72), [README.md#L12-L17](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L12-L17) (`clm_639ee5fabe7c55abd2aa268bd6483507d749312f36ab51860a108e802933efe4`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a TUI with slash commands (/model, /config, /cost, /usage, /context, /compact, /permissions, /commit, /review, etc.) plus CLI subcommands such as fuxi doctor, verify, wizard, update, proxy, and mcp serve. -- evidence: [README.md#L297-L317](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L297-L317), [README.md#L276-L291](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L276-L291) (`clm_6e0c0c38c0c4e4d787c181c835eee9e04bc4f7681f58cab2beb5430df9300ac9`)
- [observation/documented] Configuration resolves with precedence environment variables > ~/.fuxi/config.yaml > built-in defaults, and config changes are said to hot-reload while the agent runs. -- evidence: [README.md#L342-L350](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L342-L350), [docs/environment.md#L3-L8](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/environment.md#L3-L8) (`clm_de0125b1027710e4759bf0c58e9c6d1703e655f983fcad6e46a975fef87d011b`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are described as durable: transcripts persist to disk, checkpoints allow resume, rollback, or fork, long conversations auto-compact, and an idle 'dreaming' pass consolidates memory across sessions. -- evidence: [docs/faq.md#L97-L99](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L97-L99), [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82) (`clm_6920e1412e414365b7e7e3f04f6a409ff062ee2b2d8713a9ea02e329e5c722c7`)

## orchestration (1 claim(s))

- [observation/documented] Documentation describes cost-aware routing across LLM providers with automatic failover, a smart routing proxy (fuxi proxy), and fork agents with a default fork concurrency of 4 (FUXI_FORK_MAX_CONCURRENCY). -- evidence: [docs/environment.md#L48-L54](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/environment.md#L48-L54), [README.md#L12-L17](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L12-L17), [README.md#L276-L291](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L276-L291) (`clm_b24b23ff187da7326df112088f851726de351373db6fce4bdcbec5194197115a`)

## tools-permissions (1 claim(s))

- [observation/documented] Shell commands reportedly pass an AST safety classifier and rule set before execution, with fine-grained permissions and audit logging; permission modes are default, plan, and bypassPermissions, plus a classifier-gated --auto mode with a circuit breaker. -- evidence: [docs/faq.md#L105-L107](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L105-L107), [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82), [docs/faq.md#L80-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L80-L82), [docs/faq.md#L76-L78](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L76-L78) (`clm_69f246579dd0af64583445181b87e87579175c693e7815b8d8477d26624cf843`)

## evaluation (2 claim(s))

- [observation/documented] The README reports a self-run head-to-head benchmark against another coding agent using an objective pytest+coverage scorer across 15 micro and 4 large-project dimensions, and explicitly cautions it is a small, non-third-party task set measuring the agent loop. -- evidence: [README.md#L102-L104](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L102-L104), [README.md#L96-L100](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L96-L100) (`clm_5bb1f3847f4984638c76a18d3c27a8df1cddf1c5ee443a5c338165a44b9d0a38`)
- [observation/documented] The project states it currently ships without published scores on third-party benchmarks such as SWE-bench or Terminal-Bench, and instead offers a do-it-yourself evaluation checklist plus in-TUI /cost, /usage, /context, and /status commands. -- evidence: [README.md#L128-L131](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L128-L131), [README.md#L110-L113](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L110-L113) (`clm_ab8341aabfd3ebff291e36f706f043ee5f89a1b5f9cf9286ef4457378de024b1`)

## dependencies (1 claim(s))

- [observation/documented] The agent is documented as provider-agnostic: it accepts any OpenAI-compatible endpoint, Gemini, Bedrock/Vertex keys, or FuXi OAuth login, and acts as an MCP client. -- evidence: [README.md#L19-L19](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L19-L19), [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82), [docs/faq.md#L56-L58](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L56-L58) (`clm_d0e8c9ab428966612f3c83877527df401f3cedcfe59eb36b03befe04d55e2c91`)

## limitations (1 claim(s))

- [observation/documented] The repository hosts only documentation, release installers, and the issue tracker; the product source is proprietary and not published here, under a proprietary license. -- evidence: [README.md#L388-L389](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L388-L389), [README.md#L371-L373](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L371-L373) (`clm_a300fbc4166ce220b18aafa906be1ee3ecccd6905726b07d1adadc51aaa8f197`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

