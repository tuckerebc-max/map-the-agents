# iamfakeguru/agent-md -- full detail

[Back to orientation](agent-md.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/iamfakeguru/agent-md/ae8117e903fe07266c97560cbe286285e0562b82/a5409b0fff9c0932.json](../../../wiki/dossiers/iamfakeguru/agent-md/ae8117e903fe07266c97560cbe286285e0562b82/a5409b0fff9c0932.json)

## specifications (1 claim(s))

- [observation/documented] agent-md.toml declares deterministic verification: a [verify] section for typecheck, lint, test, and per-file lint commands, and a [visual] section with required, artifacts_dir, and freshness_seconds. -- evidence: [README.md#L162-L166](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L162-L166), [README.md#L155-L160](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L155-L160) (`clm_0a90814568fcabed14766bd9ae06bc16372c53b2ab579a632deed9dc0b815fc1`)

## components (1 claim(s))

- [observation/documented] The installer provisions AGENT.md as source of truth plus agent-specific rule files, hook directories, .agents/skills, .agent-md/bin helper scripts, memory/*.md files, and an optional .githooks/pre-commit fallback. -- evidence: [README.md#L27-L32](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L27-L32), [README.md#L42-L44](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L42-L44), [README.md#L55-L60](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L55-L60), [README.md#L38-L40](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L38-L40), [README.md#L34-L36](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L34-L36), [README.md#L49-L53](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L49-L53), [README.md#L46-L47](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L46-L47), [README.md#L62-L63](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L62-L63) (`clm_f5b413af9d02a5adc2b7859737a8b3907b7a1ed9f69cfd14991644c80e9aba9c`)

## design-choices (1 claim(s))

- [observation/documented] The design separates agent guidance into two layers: advisory rules files for judgment and process, and enforceable hooks/artifacts for checks, state updates, and visual evidence. -- evidence: [README.md#L74-L75](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L74-L75), [README.md#L69-L72](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L69-L72) (`clm_a6ae2137ded79b6af742a27427f8195a29350c7cdc718a58b9625265b949bda3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run bats tests/ and shellcheck over hook and helper scripts, and CI runs Bats, ShellCheck, JSON validation, alias-sync checks, and installer smoke tests. -- evidence: [README.md#L243-L244](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L243-L244), [README.md#L238-L241](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L238-L241) (`clm_a79f1b1a8bfa2911a6e70b31b70a99d0706942eeb96748efca7fa9118b5ef5f5`)

## skills-patterns (1 claim(s))

- [observation/documented] Native Codex skills live under .agents/skills/<name>/SKILL.md (agent-md-verify and visual-evidence) and are invoked with $agent-md-verify or $visual-evidence, distinct from plain shell helpers in .agent-md/bin. -- evidence: [README.md#L215-L216](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L215-L216), [README.md#L42-L44](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L42-L44), [README.md#L225-L225](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L225-L225) (`clm_398de9d2b9b722c8237b5085f7a2548a0eb8a6b0a417104c8a5229a48ec29810`)

## interfaces (2 claim(s))

- [observation/documented] install.sh accepts flags including --agent=<list>, --githooks/--no-githooks, and --claude-settings=skip|merge|replace, and can be run via a curl-piped one-liner. -- evidence: [README.md#L125-L125](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L125-L125), [README.md#L20-L21](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L20-L21), [README.md#L136-L139](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L136-L139), [README.md#L132-L133](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L132-L133), [README.md#L128-L129](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L128-L129) (`clm_558c6db627c162c3743654e3dfde42b716630ec7f04ad5de4370b7bb1a530537`)
- [observation/documented] Visual evidence is captured with ./.agent-md/bin/playwright-capture.sh <url> <png path>, producing artifacts under .agent/visual/ alongside a structured markdown note. -- evidence: [README.md#L187-L191](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L187-L191), [README.md#L179-L179](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L179-L179), [README.md#L175-L177](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L175-L177) (`clm_38206e2fa2d294f98e74ccbc615d8a90db1bbd33b77fcdcadd53ac22d257f00a`)

## memory-state (1 claim(s))

- [observation/documented] A memory/ directory with agents.md, plan.md, progress.md, verify.md, and gotchas.md serves as durable cross-session state; a state hook blocks completion when source files changed but progress.md did not. -- evidence: [README.md#L199-L199](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L199-L199), [README.md#L201-L205](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L201-L205), [README.md#L207-L208](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L207-L208) (`clm_974c349f61af1b85e37dfb31c9eceba5d24565568a8a54afc9834f5c88b1ad9d`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Bash safety is hard-blocked for Claude Code via .claude/hooks/block-destructive.sh and for Codex via .codex/hooks/pre-tool-use.sh, but is not covered for Cursor, Windsurf, or other agents. -- evidence: [README.md#L102-L110](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L102-L110) (`clm_a17c3ed4b6a94ef5c0ebe0f7a056874331986af96d160b05be07b12e0ba25287`)

## evaluation (1 claim(s))

- [observation/documented] The product enforces verification of agent work: stop hooks require type-check/lint/tests, and the strict visual hook requires a fresh non-empty markdown note referencing a fresh non-empty image with required fields. -- evidence: [README.md#L193-L195](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L193-L195), [README.md#L102-L110](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L102-L110) (`clm_147c40d8ef14db521b4f7ab30cb438f5f4239dc2b8463d926869e414e4d2845e`)

## dependencies (1 claim(s))

- [observation/documented] Codex hook support is described as experimental and requires enabling codex_hooks = true under [features] in ~/.codex/config.toml. -- evidence: [README.md#L112-L112](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L112-L112), [README.md#L114-L117](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L114-L117), [README.md#L119-L119](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L119-L119) (`clm_0342236ffe4cea150b506721513f43a2a3040cfb1946b830869165d8d12d10e0`)

## limitations (1 claim(s))

- [observation/documented] Documented limits: rules cannot force judgment, hooks only cover host-exposed events, pre-commit can be bypassed with git commit --no-verify, bash safety hooks are guardrails not a sandbox, and Cursor/Windsurf get only rules plus optional git-hook fallback. -- evidence: [README.md#L229-L234](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L229-L234) (`clm_0c0833d9ba1bb78e5fa275c4249624eee998c56479c2ab93e638f379094500a0`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

