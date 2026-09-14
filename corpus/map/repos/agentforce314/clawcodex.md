# agentforce314/clawcodex

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4706a57fc29f @ 920fad287979953b

## Summary (orientation draft, not independently verified)

Selected evidence records: The product exposes a CLI with subcommands including tui, web, login, logout, config, and --version, plus a headless -p/--print mode for non-interactive runs. The interactive UI is a TypeScript Ink TUI that spawns a Python agent-server child and communicates over an NDJSON pipe; running clawcodex with no mode flags launches it.

## Source coverage

Source coverage (partial): 6 of 22 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The tool system implements file operations (Read/Write/Edit/Glob/Grep), Bash, WebFetch/WebSearch, task management, agent tools, and configuration tools; MCP tools are wired but the full client/runtime is still evolving. -- evidence: [README.md#L582-L592](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L582-L592)
- design-choices (2 claim(s)):
  - [observation/documented] The /eco mode compresses model-bound Bash output with deterministic filters (failure-focused summaries, ceremony stripping, dedup, head-caps), discards any compression not better than the raw rendering, and tees lossy output to disk with a recovery hint. -- evidence: [README.md#L224-L230](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L224-L230), [README.md#L321-L328](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L321-L328)
  - [observation/documented] Requests keep a byte-stable prefix so DeepSeek's prompt cache covers system, tools, and history across turns; /cost is stated to follow DeepSeek's peak/off-peak pricing schedule. -- evidence: [README.md#L69-L70](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L69-L70), [README.md#L72-L74](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L72-L74)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are markdown SKILL.md slash commands with front matter supporting descriptions, allowed-tools limits, and named arguments, available at project and user scope. -- evidence: [README.md#L377-L378](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L377-L378), [README.md#L364-L372](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L364-L372)
- interfaces (5 claim(s)):
  - [observation/documented] The product exposes a CLI with subcommands including tui, web, login, logout, config, and --version, plus a headless -p/--print mode for non-interactive runs. -- evidence: [README.md#L446-L448](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L446-L448), [README.md#L435-L443](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L435-L443)
  - [observation/documented] The interactive UI is a TypeScript Ink TUI that spawns a Python agent-server child and communicates over an NDJSON pipe; running clawcodex with no mode flags launches it. -- evidence: [README.md#L406-L406](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L406-L406)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (3 claim(s)):
  - [observation/documented] Interactive sessions start in Full Access by default; /permissions offers Ask-for-approval, Approve-for-me, and Full Access levels, saved to permissions.defaultMode in ~/.clawcodex/settings.json. -- evidence: [README.md#L465-L469](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L465-L469), [README.md#L462-L463](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L462-L463), [README.md#L471-L475](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L471-L475)
  - [observation/documented] Headless -p runs default to the 'default' permission mode; a saved Full Access setting dials headless down rather than up, and --dangerously-skip-permissions or --permission-mode can override per run. -- evidence: [README.md#L477-L481](https://github.com/agentforce314/clawcodex/blob/4706a57fc29fb6f3512e4162eb9adbe4709a5035/README.md#L477-L481)
- evaluation (1 claim(s)):
More evidence: [full detail](clawcodex.detail.md)

Metadata and full claim list: [full detail](clawcodex.detail.md)
Human notes ([notes](clawcodex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
