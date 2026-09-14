# Coding and evaluation options guide

Six repositories give source-linked evidence for coding-agent feature choices: worktree/session
isolation, approval stages, model/tool interfaces, small agent loops, recovery boundaries, review
practice and measured evaluation. All citations below are exact commit-pinned GitHub URLs from the
frozen six-repository evidence context. Repo-relevance notes are design inference, not measured
outcomes; no code from these repositories was run, imported, or purchased for this guide.

## Worktree and session isolation

[1code](../../corpus/map/repos/21st-dev/1code.md) documents one isolated git worktree per chat
session, with background agents executing in cloud sandboxes while the local machine sleeps
([orchestration, README](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L88-L88),
[README](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L44-L48)).
This is a directly reusable pattern for a coding loop that must isolate concurrent sessions on one
checkout: one worktree per session, one sandbox per background run.

[hcom](../../corpus/map/repos/aannoo/hcom.md) isolates configuration per project via an `HCOM_DIR`
override and layers precedence as defaults < `config.toml` < environment variables, with per-agent
overrides via `hcom config -i`
([interfaces, README](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L349-L352),
[precedence](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L313-L313),
[`config -i`](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L315-L321)).
Config-precedence layering like this is a narrower-scope, unmeasured substitute for full worktree
isolation: it changes which settings apply per session, but changing settings alone does not give a
session its own filesystem — a worktree still isolates working-tree state that a config override
cannot.

## Approval stages

Two repositories document explicit human-approval gates before an agent acts. 1code's plan mode
requires the proposed plan be reviewed and approved, or modified, before execution
([tools-permissions, README](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L77-L82)).
[OpenCode](../../corpus/map/repos/anomalyco/opencode.md) ships a Tab-switchable `plan` agent that is
read-only and asks before bash commands, versus a full-access `build` agent
([components, README](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L104-L108),
[Tab key](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L102-L102)).
Underneath, OpenCode's agent permissions are inspected code, not just prompt text: rulesets of
allow/ask/deny actions default to allow but ask before reading `.env` files and deny the question
tool
([tools-permissions, agent.ts](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L119-L136)),
and the plan agent's own ruleset denies all edit tools except plan files under `.opencode/plans`
([tools-permissions, agent.ts](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L140-L265)).
[Codex](../../corpus/map/repos/openai/codex.md) documents sandboxing/approvals and a separate
execution-policy rules system via external docs pages, without the policy text itself in this
snapshot
([sandbox documentation](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/sandbox.md#L3-L3), [execution-policy documentation](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/execpolicy.md#L3-L3)),
and lets an admin force managed-hooks-only via `requirements.toml`, a setting that is not honored in
the user-facing `config.toml`
([design-choices, config.md](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/config.md#L11-L15)).
For an agent that must protect secrets, hcom's remote `config_get`/`config_set` explicitly refuse to
return `relay_psk`, `relay_token`, `relay_id`, or the broker URL
([tools-permissions, README](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L183-L183)).
A mode-keyed permission ruleset (OpenCode) plus a distinct denylist for sensitive config reads
(hcom) is a stronger, code-level candidate pair than a single natural-language plan-approval prompt
alone.

## Model and tool interfaces

[strands-agents/harness-sdk](../../corpus/map/repos/strands-agents/harness-sdk.md) exposes a small,
symmetric surface in two languages: Python's `Agent(tools=[...])` called with a prompt string
([interfaces, README](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L69-L71),
[example](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L73-L75)),
and TypeScript's `new Agent()` with an async `invoke(prompt)`
([interfaces, README](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L87-L88),
[example](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L90-L93)).
It defaults to Amazon Bedrock but documents Anthropic, OpenAI, Gemini, and Ollama as configurable
alternatives
([dependencies, README](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L59-L59)),
a useful reference shape for a provider-agnostic model interface. OpenCode's agent layer is built on
the Effect ecosystem and the Vercel AI SDK's `generateObject`/`streamObject`
([AI SDK imports](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L7-L10), [Effect imports](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L12-L33), [additional imports](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L1-L5)),
and the same call path backs a "generate" capability that has an LLM synthesize a new agent
configuration (identifier, `whenToUse`, system prompt) from a description
([AI SDK imports](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L7-L10), [generated schema](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L58-L62), [generation call](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L388-L416), [result fields](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L435-L439)) —
a concrete, small experiment for meta-tooling rather than a claim that this pattern is validated.
hcom forwards unknown CLI flags straight to the underlying coding tool and lists automatic message
delivery for Claude Code, Codex, Gemini CLI, OpenCode, Cursor, and others
([interfaces/dependencies, README](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L227-L240)),
a low-friction routing pattern for wrapping several external CLIs without forking each one. Codex
and OpenCode both document multi-channel install: OpenCode via a curl script, npm/bun/pnpm/yarn,
Homebrew, Scoop, Chocolatey, pacman, AUR, mise, and Nix
([interfaces, README](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L53-L62),
[README](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L50-L50)),
worth copying for any distributed CLI tool independent of coding-agent behavior. Codex additionally
documents an environment-variable escape hatch (`CODEX_INSTALLER_USE_RELEASES_OPENAI_COM`) that
forces its installer to a GitHub Releases fallback
([workflows, README](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L34-L36)).

## Small agent loops

[tiny-agent](../../corpus/map/repos/bombap/tiny-agent.md) is the smallest inspected loop: a
`ReactAgentRuntime` calls `_step()` until completion, and in `SAFE_MODE` stops after `MAX_STEPS`
(default 20, overridable by env var)
([orchestration, reactRuntime.ts](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L11-L11)).
Each step builds a prompt from templates, calls the model, and parses Thought/Action/Observation
into a scratchpad capped at 33 entries, with a similarly capped, oldest-evicted message buffer
([memory-state, reactRuntime.ts](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L173-L178)).
This is a legible reference for a first small experiment: bounded step count plus bounded, evictable
history. harness-sdk's documented loop is the richer target once a bounded prototype works: model
call, tool execution, feedback, repeat, with turn/token limits, mid-loop cancellation, stop reasons,
concurrent-invocation guards, hooks, and retry strategies
([orchestration, agent-loop.mdx](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/site/src/content/docs/user-guide/concepts/agents/agent-loop.mdx#L19-L25)).
Codex's inspected authorization code caps root-thread context at 8 messages and filters out summary
and internal `<user_action>` messages before an authorization decision
([memory-state, user_authorization.rs](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/codex-rs/core/src/agent/control/user_authorization.rs#L48-L230),
[MAX_ROOT_MESSAGES declaration](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/codex-rs/core/src/agent/control/user_authorization.rs#L30-L30)),
a small, bounded-context pattern worth reusing anywhere a loop needs a cheap decision without full
history.

## Recovery boundaries

1code's terminal module retries a failed PTY spawn once with a fallback shell
([components, session.ts](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L93-L113)),
and falls back to the user's home directory when the requested working directory does not exist or
is not a directory
([limitations, session.ts](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L32-L43),
[session.ts](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L21-L30)) —
narrow, concrete recovery boundaries at the process-launch edge. harness-sdk's delegation plugin
raises `ValueError` on stateful models rather than exit mid-turn, because an early loop exit would
leave an unclosed function call server-side
([design-choices, _agent_delegation.py](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L97-L110)),
and skips its own turn-ending shortcut when the parent expects structured output or the result is
blank
([structured-output branch](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L196-L206), [blank-result branch](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/strands-py/src/strands/agent/_agent_delegation.py#L208-L215)) —
both are explicit refuse-rather-than-corrupt-state boundaries. OpenCode's own docs flag an unresolved
gap: a legacy hook can arbitrarily mutate the baseline system prompt while its V2 plugin system has
no equivalent hook
([limitations, CONTEXT.md](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L225-L225)).
hcom documents its relay as a single all-or-nothing trust domain with no scoped roles
([limitations, README](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L158-L158)),
where a leaked shared key cannot be revoked and exposes prior captured traffic with no forward
secrecy
([README](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L191-L191),
[README](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L174-L177)) —
a boundary to design around, not copy, for anything handling untrusted peers.

## Review practice and measured evaluation

Four repositories document contributor-facing build/test/CI commands: hcom's `cargo build && cargo
test` and `just ci` gate
([build workflow](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L432-L432), [CI workflow](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L434-L439)),
harness-sdk's `hatch test`/`hatch fmt` and `npm ci && npm run build && npm test`
([Python workflow](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L114-L120), [TypeScript workflow](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L122-L127)),
tiny-agent's `pnpm install`/`pnpm dev` setup
([install workflow](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L29-L32), [run workflow](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L39-L42)),
and OpenCode's pointer to `CONTRIBUTING.md`
([workflows, README](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L121-L121)).
These are repository development practice for human or CI contributors; none of them measure a
coding agent's task success, and none should be read as agent-effectiveness evidence. Only
harness-sdk mentions agent evaluation at all, and only as an inference: its README advertises an
"evals SDK" as part of the product, but no harness, metric, or benchmark detail appears in the
supplied slices
([evaluation, README, inference](https://github.com/strands-agents/harness-sdk/blob/08ed4cfd3eb42ae9f668595e675d5f196eee7e44/README.md#L35-L35)).
For 1code, hcom, OpenCode, Codex, and tiny-agent, the evaluation facet has no submitted claim at
all — an explicit gap in the frozen evidence, not evidence that these projects lack evaluation
capability.

## Decision worksheet

No purchase, adoption, or code execution occurred for any candidate; every verdict below is a design
inference from the cited evidence, held open for a future bounded prototype.

| Candidate | Strongest evidence area | Prototype test run | Cost measured | Failure behavior noted | Adoption verdict |
|---|---|---|---|---|---|
| 1code | worktree isolation, plan approval, terminal recovery | none | none | PTY retry + home-dir fallback (documented) | candidate for isolation pattern; not evaluated |
| hcom | multi-tool routing, config precedence, relay limitations | none | none | relay is single trust domain, no forward secrecy (documented) | candidate for routing pattern; relay boundary not for untrusted peers |
| OpenCode | permission rulesets (code-inspected), agent schema | none | none | legacy hook prompt-mutation gap (documented) | candidate for permission-ruleset pattern; evaluation unknown |
| tiny-agent | smallest bounded ReAct loop (code-inspected) | none | none | none documented beyond step/buffer caps | candidate as a first small-loop prototype |
| Codex | install-channel fallback, bounded root-context filtering | none | none | none documented beyond context cap | candidate for install/routing pattern; sandbox docs not in snapshot |
| harness-sdk | dual-language interface, rich loop controls, delegation guards | none | none | ValueError on stateful delegation, skipped end_turn cases (documented) | candidate for loop/interface reference; evals capability unknown |
