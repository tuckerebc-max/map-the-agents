# arch1esun/arcgentic -- full detail

[Back to orientation](arcgentic.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/arch1esun/arcgentic/645c345077d78a6525055f641eb677c361ae767a/8f6a77ad6d7d02bc.json](../../../wiki/dossiers/arch1esun/arcgentic/645c345077d78a6525055f641eb677c361ae767a/8f6a77ad6d7d02bc.json)

## specifications (2 claim(s))

- [observation/documented] Arcgentic is described as a harness engineering layer for AI coding agents, turning ad-hoc prompting into a gated engineering workflow for Codex and Claude Code. -- evidence: [README.md#L44-L49](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L44-L49), [README.md#L7-L8](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L7-L8) (`clm_5ce3ba16420e452bfac529a0b48e2c457fb4456e8dc54dc5f18261b01cc6f089`)
- [observation/documented] The V2 workflow sequence is: idea, brainstorm/planning, round handoff, development, developer self-audit, optional user-test, external audit, pass-or-fix, then next round, next phase, or closeout. -- evidence: [README.md#L229-L239](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L229-L239) (`clm_6e3691dc845547df4ee44d44d8c693cfe19c971fba524d5ccfb51c0dcff9dd02`)

## components (3 claim(s))

- [observation/documented] Five fixed roles are defined: Orchestrator (routing/dispatch), Planner (planning and closeout decisions), Developer (building, fixes, self-audit), Test (realistic user testing when needed), and Auditor (independent PASS/NEEDS_FIX/AUDIT_INCOMPLETE review). -- evidence: [README.md#L243-L249](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L243-L249), [README.md#L251-L252](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L251-L252) (`clm_713b9b4d15ca07423e17080b8b519178076b68a0b51a8b102d9a9ae0e54788d0`)
- [observation/documented] Role/state routing is implemented as a Topology module (toolkit/src/arcgentic/topology.py) that projects can override via project.arcgentic_v2.topology in state.yaml; custom topologies are validated at parse time and zero-config projects keep the default 5-role sequence. -- evidence: [README.md#L256-L266](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L256-L266) (`clm_2420627bb93950f04f5d3f5322240c6668e9f8e9161a3878bf1174ea2b7f3980`)
- [observation/documented] An optional MCP server exposes a round_status_panel tool rendering round id, per-role dispatch progress, and latest audit verdict; the panel has no write path and falls back to a plain text summary on hosts without MCP Apps support. -- evidence: [README.md#L355-L358](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L355-L358), [README.md#L377-L384](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L377-L384) (`clm_8c5ba1c4989f77d3eba76de6aaab63d517befb0f652840d261b5860ade31f325`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the CLAUDE handoff file instructs the contributing dev session to follow a 30-task build contract in order, use TDD for Bash scripts, commit once per task with conventional-commit prefixes directly on main, and never add paid-API integrations or force-push. -- evidence: [CLAUDE-v0.1.0-handoff.md#L232-L243](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L232-L243), [CLAUDE-v0.1.0-handoff.md#L113-L114](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L113-L114), [CLAUDE-v0.1.0-handoff.md#L118-L121](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L118-L121), [CLAUDE-v0.1.0-handoff.md#L72-L72](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L72-L72), [CLAUDE-v0.1.0-handoff.md#L107-L109](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L107-L109) (`clm_6b6b55b40f44e087986346716c32c2db3f0c18177671fcd7b6a4d0604de240fe`)
- [observation/documented] Repository development practice: the handoff defines six mechanical completion checks (commits count, all test files passing, plugin.json version bump, tag creation, dogfood gate files present, and everything pushed to origin) before reporting done. -- evidence: [CLAUDE-v0.1.0-handoff.md#L191-L191](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L191-L191), [CLAUDE-v0.1.0-handoff.md#L220-L221](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L220-L221), [CLAUDE-v0.1.0-handoff.md#L214-L217](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L214-L217), [CLAUDE-v0.1.0-handoff.md#L208-L208](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L208-L208), [CLAUDE-v0.1.0-handoff.md#L200-L205](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L200-L205), [CLAUDE-v0.1.0-handoff.md#L211-L211](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L211-L211), [CLAUDE-v0.1.0-handoff.md#L197-L197](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L197-L197) (`clm_a5c21d1cc098e49905a060f22999d02e6e849325791befe32f71497e8e287b44`)
- [observation/documented] Repository development practice: the contributing environment requires Bash >= 4, Python 3 >= 3.8 with PyYAML and jsonschema, Claude Code >= 1.0, and the superpowers plugin, with plugin-dev recommended for skill review. -- evidence: [CLAUDE-v0.1.0-handoff.md#L249-L258](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L249-L258) (`clm_912731bd43ea3a6cbb594ccb11937737658aec58ff09f63bfe6e80d2d6bd00ca`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The Auditor role returns one of three verdicts — PASS, NEEDS_FIX, or AUDIT_INCOMPLETE — and the Orchestrator routes the next step based on that outcome. -- evidence: [README.md#L174-L185](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L174-L185), [README.md#L243-L249](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L243-L249), [README.md#L471-L474](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L471-L474) (`clm_fd3ed60846126e05a825e0061cf8a6a37a7bfdb462ec1bcae1b3befaedba8acb`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (3 claim(s))

- [observation/documented] In the verified Codex path, the current conversation becomes Orchestrator, which creates or reuses fixed role threads, sends role prompts, waits for return signals, and dispatches the next role without manual thread switching. -- evidence: [README.md#L286-L287](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L286-L287), [README.md#L276-L284](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L276-L284), [README.md#L73-L76](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L73-L76) (`clm_d83de37e3b95aae5307efb7bbb4317a9edbe3cc93dd49933f3e5a6dcb941a73f`)
- [observation/documented] Two project-level modes are offered: single-session with named role agents inside the Orchestrator session (faster, weaker audit isolation) and multi-session with fixed project threads (slower, stronger audit discipline); the choice is made once per project. -- evidence: [README.md#L203-L204](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L203-L204), [README.md#L198-L201](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L198-L201) (`clm_a8d80e58f3d4e58974041b790c6aee231b14469fbbbb5da1381f5241022cbce1`)
- [observation/documented] In multi-thread mode the Orchestrator should sleep after dispatching a role and wake only on the role's return, to avoid guessing completion or dispatching duplicate auditors. -- evidence: [README.md#L313-L315](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L313-L315) (`clm_78f91e40e3c96fbcfc2341b19b081ff62f10f3bc7d04624cfc94427933bc26c9`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The npm package arcgentic@2.2.0 is described as a zero-dependency plugin bundle containing skills, agents, scripts, schemas, templates, and platform manifests, while the Python CLI is published separately on PyPI. -- evidence: [README.md#L88-L93](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L88-L93), [README.md#L120-L122](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L120-L122) (`clm_9813df8558bf24e68b0de0f6b144bbb9331843a1a96edbacfc6717fbf29cb0d1`)
- [observation/documented] The MCP status panel is optional and installed via pip install 'arcgentic[mcp]', and it depends on host support for the MCP Apps extension. -- evidence: [README.md#L484-L496](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L484-L496), [README.md#L386-L387](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L386-L387), [README.md#L360-L362](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L360-L362) (`clm_e34a039faaf2387b92efb6c3a62dc9cf703c6ddbeb39e20639e4499339dd5c59`)

## limitations (2 claim(s))

- [observation/documented] For Claude Code, only single-session-subagent mode via a foreground Agent tier-0 broker dispatch has dogfood evidence; multi-session-subthread mode, the SendMessage-based retry path, ListAgents, and the hook-backed fallback path are documented as unverified. -- evidence: [README.md#L78-L84](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L78-L84), [README.md#L68-L71](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L68-L71), [README.md#L325-L329](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L325-L329) (`clm_7f36ca9e1482194b24fab4dd1b4df7bdbfbec5c6bb1ec26c275dc822d3448fa5`)
- [observation/documented] The README states Arcgentic is intentionally heavier than normal prompting and is not suited to one-line commands, tiny edits, quick experiments, or work where auditability does not matter. -- evidence: [README.md#L401-L403](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L401-L403), [README.md#L407-L412](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L407-L412) (`clm_f8b477392ef4571c46d66b44366e6ed00a3029cd4ec158051d04db5cba76f9c6`)

## relevance (1 claim(s))

- [observation/documented] Arcgentic targets frequent Codex/Claude Code users, agent builders, small AI-native teams, and complex multi-round work where AI-written code must be shown to have passed planning, testing, and audit. -- evidence: [README.md#L393-L399](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L393-L399) (`clm_e7538650d16c48edc5c4685df2d79ba79a61ffce8b354085c66ce511c13a2a81`)

