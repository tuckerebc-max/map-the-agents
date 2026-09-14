# burtson-labs/bandit-agent-framework -- full detail

[Back to orientation](bandit-agent-framework.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/burtson-labs/bandit-agent-framework/e926d20a48e61918946439a5e99c1d259dca45b3/d3f4e5b0d79a465f.json](../../../wiki/dossiers/burtson-labs/bandit-agent-framework/e926d20a48e61918946439a5e99c1d259dca45b3/d3f4e5b0d79a465f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Stated design rules include local models as first-class citizens, one host-agnostic runtime, language adapters validating before write so invalid content never reaches disk, and intent-based skill activation. -- evidence: [README.md#L535-L538](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L535-L538) (`clm_1dbbbdb85218b30d9152e205e6bc411774314fa1eb5e154ddf2245e36d97dc0b`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run pnpm test (what CI runs on PRs), add contract tests for new behaviors, and add real-trace replay fixtures for recurring failure modes per the agent-core test docs. -- evidence: [README.md#L568-L568](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L568-L568), [README.md#L570-L572](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L570-L572) (`clm_7e0a4441f147aec848bce9c9bb65b312e48ffc98c4eae25fd36a05842ffff777`)
- [observation/documented] Repository development practice: the repo's own BANDIT.md instructs agents to read files before editing, prefer replace_range for large changes, run typecheck/smoke/vitest before claiming done, and bump versions without amending tagged releases. -- evidence: [BANDIT.md#L6-L8](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/BANDIT.md#L6-L8), [BANDIT.md#L17-L20](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/BANDIT.md#L17-L20) (`clm_ee038efea301253a57025e31e3e1732a13a67723e006b543c821114418a3408f`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are markdown files with YAML frontmatter in .bandit/skills/ that load on the next turn; triggers are regex matches on the user prompt, activation:always skills run every turn, and legacy JSON skills still load. -- evidence: [README.md#L76-L80](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L76-L80) (`clm_a9d3ebab90df761807b0c54ea64938edde31f9c4a7acb025d701b97ed849f3fb`)
- [observation/documented] The default skill set includes always-on filesystem and git skills plus context-triggered code review, testing, planning, semantic search, and Gmail-dependent mail search skills. -- evidence: [README.md#L84-L90](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L84-L90) (`clm_684a550a16caee7f470af13ddda067f9f4da2aa8d1f58bc88d8b6581bd1dc23e`)

## interfaces (4 claim(s))

- [observation/documented] The product ships two hosts — a VS Code/Cursor extension (Bandit Stealth) and a terminal CLI — both backed by the same stealth-core-runtime package, with skills, memory files, and hooks working identically across them. -- evidence: [README.md#L34-L34](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L34-L34), [README.md#L29-L32](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L29-L32) (`clm_98d0a292e320cc708dde134f1e1cbf94eccf13812eb6a40e66ad61c5e0e469b9`)
- [observation/documented] The CLI offers slash commands including /help, /doctor, /model, /skills, /session, /memory, /remember, /trace, /insights, and /exit. -- evidence: [README.md#L200-L212](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L200-L212) (`clm_b4cf88bb45a9446372f3045c3c8b769337cc985b5912824d46df790098820d3b`)
- [observation/documented] Prompts can prefix a path with @ to inline file contents before the model sees them, up to 8 mentions per prompt at 64 KB each with auto-truncation. -- evidence: [README.md#L164-L164](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L164-L164), [README.md#L170-L170](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L170-L170) (`clm_368c811b2f240b0eb27d8d650b71cbf0e30518db9771dcd1e0cf829ceca18eeb`)
- [observation/documented] Bandit speaks MCP as both client and server: MCP server tools surface as <server>.<tool>, and 'bandit mcp serve' exposes native tools over stdio with a --read-only mode. -- evidence: [README.md#L308-L308](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L308-L308), [README.md#L306-L306](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L306-L306) (`clm_a2287ad834121f12a6c0d5acc61f674360815699748900a7c9f4390a7900e309`)

## memory-state (3 claim(s))

- [observation/documented] The agent auto-loads BANDIT.md, CLAUDE.md, or AGENTS.md from the workspace root into the system prompt; /remember appends facts and /init scaffolds a new BANDIT.md. -- evidence: [README.md#L131-L133](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L131-L133), [README.md#L98-L101](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L98-L101) (`clm_3570b701bdb26bed063ca22ce75d9f3e28d8ef66bf4ba9fca0a6dcc7220a78f3`)
- [observation/documented] A MEMORY.md topic index (capped at 4 KB) loads every turn while linked memory/ files (32 KB cap) are lazily fetched via read_memory when the task matches. -- evidence: [README.md#L149-L152](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L149-L152) (`clm_a038da8ae22405f36d982eb495b5528892dcfae8b635cfcff48c01474f92bfe5`)
- [observation/documented] REPL sessions persist as JSONL under ~/.bandit/sessions/ and can be resumed via bandit --resume or /session resume. -- evidence: [README.md#L179-L181](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L179-L181), [README.md#L174-L174](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L174-L174), [README.md#L176-L177](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L176-L177) (`clm_7f949bfb1e8a5de4019db59c9021065ca79d964b271e0aab8f2194fafcdd3b5b`)

## orchestration (2 claim(s))

- [observation/documented] The agent can spawn background subagents whose synopses inject into the parent's next iteration; /tasks inspects and cancels them, and stopping cascades to in-flight subagents. -- evidence: [README.md#L316-L316](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L316-L316) (`clm_80552685c338060e46d875c12c80b31b61e7337a6c99684fd454ece4f28d0233`)
- [observation/documented] The tool-use loop is capped by BANDIT_MAX_ITERATIONS (default 20); a documented benchmark run hit this ceiling and was forced to synthesize after 13 exploration rounds. -- evidence: [README.md#L473-L473](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L473-L473), [README.md#L488-L503](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L488-L503) (`clm_b3b7e55327a9f0b522b19994c79eaa233f03d7dff3fc50dd039d3b2effac0bce`)

## tools-permissions (3 claim(s))

- [observation/documented] Every file-edit tool call passes an approval gate that shows a compact diff before touching disk, with scoped grant options such as allow once, allow turn, allow session, always allow, and deny; approving a command grants only that command pattern. -- evidence: [README.md#L231-L235](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L231-L235), [README.md#L216-L216](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L216-L216), [README.md#L237-L238](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L237-L238) (`clm_d5bf5513b4c9e4e4eabf5963d91d9c1128296926518a6a8754c0e250fc52d6fd`)
- [observation/documented] Auto mode runs routine work unprompted but always asks before destructive actions (deletions, history rewrites, credential files, exfiltration-style sends), and this floor cannot be disabled by settings or saved allow rules. -- evidence: [README.md#L250-L258](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L250-L258), [README.md#L246-L248](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L246-L248), [README.md#L242-L244](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L242-L244) (`clm_7e716087bf8447d90a47a8bc062defccc9343339f0d2ea65157bf89072c3aa0e`)
- [observation/documented] web_fetch is SSRF-guarded, refusing RFC1918, loopback, and cloud-metadata targets unless BANDIT_ALLOW_PRIVATE_WEB_FETCH=1 is set. -- evidence: [README.md#L189-L192](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L189-L192) (`clm_117d5b932ab2dc04cb2b29d749481e018a2b03714517bba6b9bdab72d3da06e4`)

## evaluation (1 claim(s))

- [observation/documented] The README reports two reproducible benchmark runs of the agent on repo deep-dive prompts, with metrics like turn duration, LLM iterations, and tool-call counts, plus reproduction commands. -- evidence: [README.md#L460-L469](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L460-L469), [README.md#L430-L439](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L430-L439), [README.md#L424-L424](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L424-L424), [README.md#L477-L482](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L477-L482) (`clm_e0cc24667cc91c70001515cff6d6e5b39e178622f92fee0ca28f9ce1a9e39100`)

## dependencies (1 claim(s))

- [observation/documented] The runtime targets Ollama (local daemon or Ollama Cloud via the same API) and optionally Bandit Cloud hosted inference; web_search uses Tavily with a TAVILY_API_KEY. -- evidence: [README.md#L488-L503](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L488-L503), [README.md#L194-L196](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L194-L196), [README.md#L372-L376](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L372-L376) (`clm_ac5ff94bc857614f3616ae21e74660dff389c3014232521bd2d7bff1d4e5bc2e`)

## limitations (1 claim(s))

- [observation/documented] The README lists maturing areas: plan mode in the CLI, status-line/TUI polish, and lossless trace replay for native-tool runs; PreToolUse hook failures warn but do not yet abort. -- evidence: [README.md#L280-L282](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L280-L282), [README.md#L546-L548](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L546-L548) (`clm_86c2c1a06c2562134d3d737bf93c7378657c9c112f083261cd1f2a844d8683fb`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

