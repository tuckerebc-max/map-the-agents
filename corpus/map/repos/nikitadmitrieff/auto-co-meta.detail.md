# nikitadmitrieff/auto-co-meta -- full detail

[Back to orientation](auto-co-meta.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nikitadmitrieff/auto-co-meta/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/953e0670bb31dedd.json](../../../wiki/dossiers/nikitadmitrieff/auto-co-meta/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/953e0670bb31dedd.json)

## specifications (1 claim(s))

- [observation/documented] auto-co is described as a bash loop that invokes Claude Code every two minutes, letting 14 AI agents debate, decide, build, and deploy software continuously without human supervision. -- evidence: [README.md#L22-L22](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L22-L22) (`clm_b8d976f0cb09e9301e2c3c30d2d2020e352852401d942c7fddf5445d244a59f1`)

## components (1 claim(s))

- [observation/documented] Key runtime files include auto-loop.sh (the loop with monitoring, error handling, and adaptive frequency), PROMPT.md (per-cycle system prompt), memories/consensus.md, .claude/agents/*.md personas, and a Makefile of commands. -- evidence: [README.md#L131-L136](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L131-L136) (`clm_dcd9ccd68aa128d21b14400f99a9a2ac6a5d5b69b7bf51efccf25c1ff072240d`)

## design-choices (1 claim(s))

- [observation/documented] The design deliberately avoids a database, server, or framework: state persists in markdown files plus git, with Claude Code as the sole dependency. -- evidence: [README.md#L138-L138](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L138-L138), [README.md#L30-L30](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L30-L30) (`clm_de7a4cdde55ae79390b307a73cf866d76afef04319135effca0e8a31e5185257`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md instructs the operating agent instance to make auto-co production-ready, act autonomously without waiting for human approval, treat CEO (Bezos) as final decision-maker, and never modify safety red lines or break the loop. -- evidence: [CLAUDE.md#L42-L47](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L42-L47), [CLAUDE.md#L5-L5](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L5-L5), [CLAUDE.md#L10-L10](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L10-L10), [CLAUDE.md#L16-L20](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L16-L20) (`clm_53894fc2f45808cad821dd913758373a096f20faed346d4a57c4854d2bd0df07`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Makefile exposes operational commands such as make start, monitor, status, health, history, export, stop, pause, and resume, plus a Next.js dashboard runnable on port 3000. -- evidence: [docs/devops/runbook.md#L242-L245](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L242-L245), [docs/devops/runbook.md#L49-L50](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L49-L50), [docs/devops/runbook.md#L39-L42](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L39-L42), [docs/devops/runbook.md#L240-L240](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L240-L240), [README.md#L156-L162](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L156-L162), [docs/devops/runbook.md#L62-L65](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L62-L65) (`clm_0a74b819a7480753aa876342746598bdfe2258d89b2a31763bae36761d981001`)
- [observation/documented] Configuration is environment-based via .env, with documented variables including MODEL (default sonnet), LOOP_INTERVAL (120s), CYCLE_TIMEOUT_SECONDS (1800s), MAX_CONSECUTIVE_ERRORS (3), and COOLDOWN_SECONDS (300). -- evidence: [docs/devops/runbook.md#L107-L107](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L107-L107), [docs/devops/runbook.md#L109-L117](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L109-L117) (`clm_8bac5388a7862c739ce4f150b191cfc5d1c1a50cfc84e7ea8a45ba7fb7a3b3a3`)

## memory-state (2 claim(s))

- [observation/documented] Consensus.md acts as the relay baton carrying state between cycles, written atomically via a .consensus.tmp temp file and rename, with a .bak backup restored automatically on cycle failure. -- evidence: [PROMPT.md#L47-L51](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/PROMPT.md#L47-L51), [docs/devops/runbook.md#L255-L255](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L255-L255), [docs/devops/runbook.md#L251-L253](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L251-L253) (`clm_1798dfaec9bdee2883e3cd53b17f79eda74d5d6fc76f12dd61ff9effdf1f3568`)
- [observation/documented] Agents append structured records to four append-only JSONL files under state/: decisions, tasks, metrics, and artifacts, each with a defined schema; these files must never be overwritten or truncated. -- evidence: [PROMPT.md#L124-L124](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/PROMPT.md#L124-L124), [docs/plans/2026-03-07-v2-improvements-design.md#L21-L21](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/plans/2026-03-07-v2-improvements-design.md#L21-L21), [docs/plans/2026-03-07-v2-improvements-design.md#L23-L26](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/plans/2026-03-07-v2-improvements-design.md#L23-L26) (`clm_7cf8828ffe631e7bb38aec20284d51442fb3deade8d44cbc03745b551e94ba6f`)

## orchestration (2 claim(s))

- [observation/documented] Each cycle reads consensus.md, builds a prompt from PROMPT.md, calls 'claude -p', has agents update consensus, appends structured JSONL logs, then sleeps and repeats; each cycle selects 3-5 of the 14 relevant agents. -- evidence: [README.md#L82-L82](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L82-L82), [README.md#L121-L129](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L121-L129) (`clm_a6c36e215eeca7d418b2f7a389a2e01d4ac4270965798689bafac833f9cd1aa1`)
- [observation/documented] The loop includes resilience mechanisms: a circuit breaker after MAX_CONSECUTIVE_ERRORS failures with a cooldown, and automatic sleep of LIMIT_WAIT_SECONDS (default one hour) on API usage-limit errors. -- evidence: [docs/devops/runbook.md#L188-L191](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L188-L191), [docs/devops/runbook.md#L172-L175](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L172-L175) (`clm_c9fe278c0bbdac0610debda0408f1dc1b15947791c49d293626a6b4be2007ad5`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Claude Code installed and working is listed as the prerequisite; the comparison table states the only dependency is Claude Code itself, with no framework or database required. -- evidence: [README.md#L182-L189](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L182-L189), [README.md#L36-L36](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L36-L36) (`clm_a8b505c44e482774ae0d8d52ccb9ba7dc1df1cce8f8e2218aaa8d9843e2ba226`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

