# omnigent-ai/omnigent -- full detail

[Back to orientation](omnigent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/omnigent-ai/omnigent/270eca52b1e0ca66f1174f759da1218faf462f0e/94cb8b38f0cdc681.json](../../../wiki/dossiers/omnigent-ai/omnigent/270eca52b1e0ca66f1174f759da1218faf462f0e/94cb8b38f0cdc681.json)

## specifications (1 claim(s))

- [observation/documented] Omnigent is described as an open-source meta-harness providing a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and self-written agents, allowing harness swapping without rewrites. -- evidence: [README.md#L7-L7](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L7-L7) (`clm_195b44f5fa73a7a3340245e42ff229d065c713e83dee93bda2dee1a0f49e6709`)

## components (1 claim(s))

- [observation/documented] Agents are defined in YAML files declaring a prompt, an executor harness (e.g. claude-sdk, codex, cursor, pi, openai-agents), tools including local Python functions, MCP servers, and delegatable sub-agents. -- evidence: [README.md#L574-L577](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L574-L577), [README.md#L583-L586](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L583-L586), [README.md#L594-L597](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L594-L597), [README.md#L599-L605](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L599-L605), [README.md#L588-L592](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L588-L592) (`clm_002cf7947be38670f1434eb7440d1a7bc1b1304333f3f20bb5f5a483172f911d`)

## design-choices (1 claim(s))

- [observation/documented] On Linux, native harness terminal wrappers and the pi harness sandbox each agent terminal with bubblewrap, and that isolation is mandatory; macOS uses the built-in seatbelt sandbox instead. -- evidence: [README.md#L139-L165](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L139-L165) (`clm_98fdaa60decedd2ee4d6a4b1e6133d4ed6b386825a8e23972a1c7844f73544d2`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs AI contributors to run the pre-commit hook before committing and fix reported issues so commits land clean, since CI runs the same checks. -- evidence: [AGENTS.md#L8-L10](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L8-L10) (`clm_13e01de6a89ff11b6dedc76ebbebcca947a3d37d7eeee9ce444dc652ced320e7`)
- [observation/documented] Repository development practice: contributors use 'just' recipes for common tasks (ensure, dev, lint, electron builds, lockfile normalization) and must fill in the repo's PR template with summary, test plan, and demo sections. -- evidence: [AGENTS.md#L14-L14](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L14-L14), [AGENTS.md#L25-L27](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L25-L27), [AGENTS.md#L29-L38](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L29-L38), [AGENTS.md#L16-L21](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/AGENTS.md#L16-L21) (`clm_23bc56bc5afdca5b65d8372981ab5dfcd73b59b6146cca959f600769ef87e2a5`)
- [observation/documented] Repository development practice: PRs adding or changing harness support should run the harness test bench to check the capability matrix against observed behavior. -- evidence: [README.md#L634-L636](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L634-L636) (`clm_27d5a60e43b207a685868421aac1af684470a84d097282e043f1bb79cdf78980`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI exposes per-harness launchers such as omnigent claude, codex, cursor, agy, opencode, hermes, and pi, plus an interchangeable short alias 'omni' installed alongside the main command. -- evidence: [README.md#L278-L286](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L278-L286), [README.md#L263-L265](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L263-L265) (`clm_2d7ced6b7f349171358d615d676aa22c6c6ab2bf71192fc74d87def6377db0af`)
- [observation/documented] Running omnigent starts a terminal session and a local web UI at http://localhost:6767 showing the same session; a macOS desktop app wraps that UI with OS notifications and a dock badge. -- evidence: [README.md#L14-L14](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L14-L14), [README.md#L256-L261](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L256-L261) (`clm_e5e55063a220dae21408caea327daa642d79b2aa64815b81692659941f6753a8`)
- [observation/documented] YAML-defined agents are launched with 'omnigent run path/to/agent.yaml', and examples such as polly, debby, and deep-research can be run the same way, optionally with a --harness override. -- evidence: [README.md#L609-L611](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L609-L611), [README.md#L338-L340](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L338-L340), [README.md#L332-L335](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L332-L335) (`clm_43450c85f57135b8ae245b7263c8f75740bc9f822d8037f88535c10a40610de2`)
- [observation/documented] Multi-user accounts are enabled via OMNIGENT_AUTH_ENABLED=1; signup is invite-only through single-use invite links, and OIDC providers (Google, GitHub, Okta, Microsoft) can be configured on a deployed server. -- evidence: [README.md#L478-L479](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L478-L479), [README.md#L490-L494](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L490-L494), [README.md#L525-L530](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L525-L530), [README.md#L481-L483](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L481-L483) (`clm_7b7f209c83b18616329a752c5115c70f2b96f3bc7b6e9f2294b592fa97331b48`)

## memory-state (1 claim(s))

- [observation/documented] Sessions follow the user across devices: started in a terminal, they continue in the browser or on a phone, with messages, sub-agents, terminals, and files staying in sync. -- evidence: [README.md#L28-L30](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L28-L30) (`clm_2e01678dd72e9bc366ad28851e51f3bb465b5645608857fd265f787f34b9a2c6`)

## orchestration (2 claim(s))

- [observation/documented] The Polly example is a multi-agent orchestrator that delegates coding to sub-agents (Claude Code, Codex, or Pi) in parallel git worktrees and routes each diff to a reviewer from a different vendor. -- evidence: [README.md#L342-L345](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L342-L345) (`clm_76d59394a7f8bd34d614d0d9f48ff311ba7a9075783d3b18db938879d2c8c21a`)
- [observation/documented] Sessions can run in disposable cloud sandboxes on providers including Modal, Daytona, E2B, Kubernetes, CoreWeave, and Databricks, launched from the CLI or provisioned per session by the server as managed hosts. -- evidence: [README.md#L44-L54](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L44-L54) (`clm_133e70c679f59c54b8ac659997e5b8e03128cfb16065b2f8c1eaaff4ce12c78b`)

## tools-permissions (1 claim(s))

- [observation/documented] Policies check every agent action and allow, block, or pause for approval; builtins can cap tool calls and spend, and policies stack at server-wide, per-agent, and per-session levels with stricter session rules checked first. -- evidence: [README.md#L564-L566](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L564-L566), [README.md#L546-L562](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L546-L562), [README.md#L534-L536](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L534-L536) (`clm_e516c802c2946b3c6d2f6844e2ad5ce6bf3275d45d111e684adc8cfc4a279320`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Omnigent requires Python 3.12+ and is installable via a curl installer script, uv/pip, or Homebrew; optional extras cover model providers (databricks, bedrock, vertex), sandbox providers, SDK harnesses, and storage/memory backends. -- evidence: [README.md#L85-L89](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L85-L89), [README.md#L96-L96](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L96-L96), [README.md#L98-L100](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L98-L100), [README.md#L110-L112](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L110-L112), [README.md#L69-L71](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L69-L71) (`clm_f4256438dd509e1a63cb9c40b67f1108e6d1545285e79003e0bcc0629b204292`)
- [observation/documented] Native harness terminal wrappers require tmux, the coding-harness CLIs installed by omnigent run need Node.js 22 LTS or newer with npm, and pnpm is needed for the web UI. -- evidence: [README.md#L139-L165](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L139-L165) (`clm_965166d942a5105687c49903a0d04b85535d9fecd4f155a10c993aebf394a50f`)

## limitations (1 claim(s))

- [observation/documented] On Windows the product runs in a degraded mode: tmux/PTY terminal wrappers and bwrap/seatbelt filesystem and network sandboxing are unavailable; the Windows Job Object backend contains the process tree but does not isolate filesystem or network. -- evidence: [README.md#L188-L192](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L188-L192), [README.md#L181-L184](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L181-L184), [README.md#L172-L173](https://github.com/omnigent-ai/omnigent/blob/270eca52b1e0ca66f1174f759da1218faf462f0e/README.md#L172-L173) (`clm_ab72d6b5b17ea95eacab811c0fc8e81b3db675a8cf5a00ac800d680213dcb061`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

