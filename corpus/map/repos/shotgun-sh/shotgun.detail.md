# shotgun-sh/shotgun -- full detail

[Back to orientation](shotgun.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shotgun-sh/shotgun/4d344d5a46aafc815de441ff670d4131187f33e6/8d70e09acc259e1e.json](../../../wiki/dossiers/shotgun-sh/shotgun/4d344d5a46aafc815de441ff670d4131187f33e6/8d70e09acc259e1e.json)

## specifications (1 claim(s))

- [observation/documented] Shotgun is described as a spec-driven development CLI that reads the whole codebase, plans features upfront, and splits work into staged PRs with file-by-file instructions for AI coding agents. -- evidence: [README.md#L7-L24](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L7-L24), [README.md#L42-L42](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L42-L42), [docs/CASE_STUDY.md#L5-L5](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/docs/CASE_STUDY.md#L5-L5), [README.md#L40-L40](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L40-L40) (`clm_bf1e3d45dca2818e5e4e6aaa8935aab5b327ca3b878bd33aea79a99a259e5582`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Each phase (research, spec, plan, tasks, export) uses a separate specialized agent with phase-tailored prompts rather than a single general-purpose agent. -- evidence: [README.md#L295-L303](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L295-L303) (`clm_b7966cd9bce6febff9fd6e88692784866d379d3ff15884ac345056398f6dde81`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README points contributors to a Contributing Guide, Git Hooks (Lefthook, trufflehog, security scanning), CI/CD via GitHub Actions, observability, and Docker docs, and welcomes bug/feature/doc issue templates. -- evidence: [README.md#L382-L382](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L382-L382), [README.md#L400-L404](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L400-L404), [README.md#L386-L388](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L386-L388) (`clm_8df1d931bdb2261cdf91dcfcc816469147bd78c479a618093881da892e8dfe5f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Planning mode proposes a plan with confirmation checkpoints before file-changing agents run, while Drafting runs the full plan without intermediate prompts; Shift+Tab switches modes and '/' opens the command palette. -- evidence: [README.md#L171-L174](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L171-L174), [README.md#L176-L176](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L176-L176) (`clm_870dcb4e0d70138c7db12e6e236616b85f246a5be147737561e5a75d967ad90e`)
- [observation/documented] Keyboard shortcuts include Shift+Tab for mode switching, Ctrl+C to cancel, Escape to exit Q&A or stop an agent, and Ctrl+U to view usage stats. -- evidence: [README.md#L201-L207](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L201-L207) (`clm_77571a0f2de0d4af5d0ad6d9076ba71dc0fa5f53972c5c5a94a554396d601999`)
- [observation/documented] Specs can be exported as AGENTS.md files for tools like Cursor, Claude Code, Windsurf, and Lovable, and shared to a workspace as versioned snapshots on paid plans, leaving local .shotgun/*.md files unchanged. -- evidence: [README.md#L259-L260](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L259-L260), [README.md#L315-L323](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L315-L323), [README.md#L242-L242](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L242-L242), [README.md#L244-L244](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L244-L244) (`clm_47ddd1ae8467f7be96a97695d56c45ff34ad9028c0bf9da8ca38d8069eb5cb22`)

## memory-state (1 claim(s))

- [observation/documented] Codebase indexing runs locally using tree-sitter parsing, producing a searchable code graph stored under ~/.shotgun-sh/codebases/ that the FAQ says is never sent to a server. -- evidence: [README.md#L377-L377](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L377-L377), [README.md#L359-L359](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L359-L359) (`clm_5f6f7f2bfcd7279a4e02c023558757a3b9c8fb22ad1d8650485edc200fc459b7`)

## orchestration (1 claim(s))

- [observation/documented] A Router internally dispatches specialized sub-agents across Research, Specify, Plan, Tasks, and Export phases; users control only the Planning and Drafting execution modes. -- evidence: [README.md#L181-L193](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L181-L193), [README.md#L195-L195](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L195-L195), [README.md#L179-L179](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L179-L179) (`clm_44ad574cf9b9121fe5a6ad9ef72908997f7519cf88e3f3aeda7452349213480c`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Supported LLM providers are OpenAI, Anthropic (Claude), and Google Gemini; local LLM support is stated as planned, and internet access is required for LLM API calls. -- evidence: [README.md#L369-L369](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L369-L369), [README.md#L373-L373](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L373-L373), [README.md#L365-L365](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L365-L365) (`clm_a5c1b216c29d31b9179623560b2f58bafc001c7b3ef489e42b96f9da4d720d04`)
- [observation/documented] Installation uses uv (via Homebrew or curl) and running 'uvx shotgun-sh@latest'; on Windows, PowerShell is required with x64 and Python 3.11-3.13 supported, while 32-bit Python and 3.14+ are not supported. -- evidence: [README.md#L118-L121](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L118-L121), [README.md#L82-L84](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L82-L84), [README.md#L66-L67](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L66-L67), [README.md#L63-L63](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L63-L63), [README.md#L71-L73](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L71-L73), [README.md#L123-L123](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L123-L123), [README.md#L115-L116](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L115-L116), [README.md#L88-L90](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L88-L90) (`clm_da039d8b31fc7b68a6a652c0b282b46542bf848061d2f8d73e79deb3f12ed034`)

## limitations (1 claim(s))

- [observation/documented] The FAQ states only minimal anonymous event telemetry (e.g., install, server start, tool call) is collected via PostHog, without collecting event content. -- evidence: [README.md#L355-L355](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L355-L355) (`clm_040e22b3eb948f4668f1332a875f3149005ef39721dd769c2b8aca0070d1f5ef`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

