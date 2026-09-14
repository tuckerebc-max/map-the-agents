# fuxicodex/fuxi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ab2785904754 @ 2d08cae774751f9b

## Summary (orientation draft, not independently verified)

Selected evidence records: FuXi is documented as a terminal AI coding agent built in Go, shipped as a single static binary with no runtime dependencies, positioned as a provider-agnostic alternative to Claude Code. The agent is described as running a Think → Act → Verify loop: it reasons about a task, acts with built-in tools, inspects results, and iterates until the work is verified.

## Source coverage

Source coverage (partial): 6 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] FuXi is documented as a terminal AI coding agent built in Go, shipped as a single static binary with no runtime dependencies, positioned as a provider-agnostic alternative to Claude Code. -- evidence: [README.md#L12-L17](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L12-L17)
- components (1 claim(s)):
  - [observation/documented] Documentation claims 50+ built-in tools including file read/write/edit, bash and PowerShell shell, ripgrep search, web fetch, LSP diagnostics, Jupyter, browser use, background tasks, and parallel sub-agents. -- evidence: [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82)
- design-choices (1 claim(s)):
  - [observation/documented] The agent is described as running a Think → Act → Verify loop: it reasons about a task, acts with built-in tools, inspects results, and iterates until the work is verified. -- evidence: [docs/faq.md#L70-L72](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L70-L72), [README.md#L12-L17](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L12-L17)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a TUI with slash commands (/model, /config, /cost, /usage, /context, /compact, /permissions, /commit, /review, etc.) plus CLI subcommands such as fuxi doctor, verify, wizard, update, proxy, and mcp serve. -- evidence: [README.md#L297-L317](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L297-L317), [README.md#L276-L291](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L276-L291)
  - [observation/documented] Configuration resolves with precedence environment variables > ~/.fuxi/config.yaml > built-in defaults, and config changes are said to hot-reload while the agent runs. -- evidence: [README.md#L342-L350](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L342-L350), [docs/environment.md#L3-L8](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/environment.md#L3-L8)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are described as durable: transcripts persist to disk, checkpoints allow resume, rollback, or fork, long conversations auto-compact, and an idle 'dreaming' pass consolidates memory across sessions. -- evidence: [docs/faq.md#L97-L99](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L97-L99), [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82)
- orchestration (1 claim(s)):
  - [observation/documented] Documentation describes cost-aware routing across LLM providers with automatic failover, a smart routing proxy (fuxi proxy), and fork agents with a default fork concurrency of 4 (FUXI_FORK_MAX_CONCURRENCY). -- evidence: [docs/environment.md#L48-L54](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/environment.md#L48-L54), [README.md#L12-L17](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L12-L17), [README.md#L276-L291](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L276-L291)
- tools-permissions (1 claim(s)):
  - [observation/documented] Shell commands reportedly pass an AST safety classifier and rule set before execution, with fine-grained permissions and audit logging; permission modes are default, plan, and bypassPermissions, plus a classifier-gated --auto mode with a circuit breaker. -- evidence: [docs/faq.md#L105-L107](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L105-L107), [README.md#L66-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/README.md#L66-L82), [docs/faq.md#L80-L82](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L80-L82), [docs/faq.md#L76-L78](https://github.com/fuxicodex/Fuxi/blob/ab2785904754a3ca695e7cef1c1238496d0b1697/docs/faq.md#L76-L78)
- evaluation (2 claim(s)):
More evidence: [full detail](fuxi.detail.md)

Metadata and full claim list: [full detail](fuxi.detail.md)
Human notes ([notes](fuxi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
