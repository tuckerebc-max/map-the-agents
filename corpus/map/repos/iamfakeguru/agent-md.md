# iamfakeguru/agent-md

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ae8117e903fe @ a5409b0fff9c0932

## Summary (orientation draft, not independently verified)

agent-md is an installer that provisions cross-agent rules files, hooks, memory files, and helper scripts so coding agents verify their work deterministically. Evidence covers its installed layout, enforcement matrix, config format, and stated limits; no source code beyond docs is shown. Evidence coverage: 175 of 179 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] agent-md.toml declares deterministic verification: a [verify] section for typecheck, lint, test, and per-file lint commands, and a [visual] section with required, artifacts_dir, and freshness_seconds. -- evidence: [README.md#L162-L166](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L162-L166), [README.md#L155-L160](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L155-L160)
- components (1 claim(s)):
  - [observation/documented] The installer provisions AGENT.md as source of truth plus agent-specific rule files, hook directories, .agents/skills, .agent-md/bin helper scripts, memory/*.md files, and an optional .githooks/pre-commit fallback. -- evidence: [README.md#L27-L32](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L27-L32), [README.md#L42-L44](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L42-L44), [README.md#L55-L60](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L55-L60), [README.md#L38-L40](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L38-L40), [README.md#L34-L36](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L34-L36), [README.md#L49-L53](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L49-L53), [README.md#L46-L47](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L46-L47), [README.md#L62-L63](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L62-L63)
- design-choices (1 claim(s)):
  - [observation/documented] The design separates agent guidance into two layers: advisory rules files for judgment and process, and enforceable hooks/artifacts for checks, state updates, and visual evidence. -- evidence: [README.md#L74-L75](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L74-L75), [README.md#L69-L72](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L69-L72)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run bats tests/ and shellcheck over hook and helper scripts, and CI runs Bats, ShellCheck, JSON validation, alias-sync checks, and installer smoke tests. -- evidence: [README.md#L243-L244](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L243-L244), [README.md#L238-L241](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L238-L241)
- skills-patterns (1 claim(s)):
  - [observation/documented] Native Codex skills live under .agents/skills/<name>/SKILL.md (agent-md-verify and visual-evidence) and are invoked with $agent-md-verify or $visual-evidence, distinct from plain shell helpers in .agent-md/bin. -- evidence: [README.md#L215-L216](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L215-L216), [README.md#L42-L44](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L42-L44), [README.md#L225-L225](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L225-L225)
- interfaces (2 claim(s)):
  - [observation/documented] install.sh accepts flags including --agent=<list>, --githooks/--no-githooks, and --claude-settings=skip|merge|replace, and can be run via a curl-piped one-liner. -- evidence: [README.md#L125-L125](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L125-L125), [README.md#L20-L21](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L20-L21), [README.md#L136-L139](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L136-L139), [README.md#L132-L133](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L132-L133), [README.md#L128-L129](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L128-L129)
  - [observation/documented] Visual evidence is captured with ./.agent-md/bin/playwright-capture.sh <url> <png path>, producing artifacts under .agent/visual/ alongside a structured markdown note. -- evidence: [README.md#L187-L191](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L187-L191), [README.md#L179-L179](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L179-L179), [README.md#L175-L177](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L175-L177)
- memory-state (1 claim(s)):
  - [observation/documented] A memory/ directory with agents.md, plan.md, progress.md, verify.md, and gotchas.md serves as durable cross-session state; a state hook blocks completion when source files changed but progress.md did not. -- evidence: [README.md#L199-L199](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L199-L199), [README.md#L201-L205](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L201-L205), [README.md#L207-L208](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L207-L208)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Bash safety is hard-blocked for Claude Code via .claude/hooks/block-destructive.sh and for Codex via .codex/hooks/pre-tool-use.sh, but is not covered for Cursor, Windsurf, or other agents. -- evidence: [README.md#L102-L110](https://github.com/iamfakeguru/agent-md/blob/ae8117e903fe07266c97560cbe286285e0562b82/README.md#L102-L110)
- evaluation (1 claim(s)):
More evidence: [full detail](agent-md.detail.md)

Metadata and full claim list: [full detail](agent-md.detail.md)
Human notes ([notes](agent-md.notes.md), never overwritten by build)

[Back to map index](../../index.md)
