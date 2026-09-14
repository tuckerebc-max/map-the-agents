# zaxbyhub/opencode-swarm -- full detail

[Back to orientation](opencode-swarm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zaxbyhub/opencode-swarm/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/1ea8b5b5f4e58f3d.json](../../../wiki/dossiers/zaxbyhub/opencode-swarm/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/1ea8b5b5f4e58f3d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The plugin registers a roster of specialized agents including architect, coder, reviewer, test_engineer, critic, explorer, sme, docs, designer, plus optional and conditional critic, curator, and council agents. -- evidence: [README.md#L315-L335](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L315-L335), [README.md#L40-L54](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L40-L54) (`clm_eb511d332b8b6e20bf1e3a825c946ca706ffcf25d4c3798990d47683fcc86c22`)

## design-choices (2 claim(s))

- [observation/documented] The pipeline is gated: code does not ship without reviewer and test-engineer approval, and agents never mutate the codebase in parallel. -- evidence: [README.md#L19-L19](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L19-L19), [README.md#L31-L31](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L31-L31) (`clm_3f6276ac7af9effb3c97d9c80fd79a35118398d4f37919bf9803b9cde14301ec`)
- [observation/documented] A Process Remediation Model detects five failure patterns (repetition loop, ping-pong, expansion drift, stuck-on-test, context thrashing) and escalates from advisory guidance to architect alert to hard stop. -- evidence: [README.md#L480-L484](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L480-L484), [README.md#L486-L489](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L486-L489), [README.md#L478-L478](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L478-L478) (`clm_f731f55bf02f31e47433ce01eb812333e69e78da9a4f05fb18d21a0a69196f1e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] Skill propagation logs usage to .swarm/skill-usage.jsonl, scores relevance (threshold 0.5, max 5 recommendations), optionally enforces a SKILLS: field on delegations, and supports .opencode/skill-routing.yaml routing. -- evidence: [README.md#L616-L627](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L616-L627), [README.md#L585-L590](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L585-L590), [README.md#L592-L596](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L592-L596), [README.md#L583-L583](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L583-L583) (`clm_ae028039f5e456161f35305ce871ea5f3f78f8cd46f70621c6aa3bd496ddd2be`)
- [observation/documented] Seven skill lifecycle tools (skill_generate through skill_improve) are opt-in via skills.enabled (default false); with the flag off they are host-denied for all agents except skill_improver. -- evidence: [README.md#L633-L633](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L633-L633) (`clm_a50a29e048c031836f58dee920145352b8e5b906bafdd41e12c08f6a9e88bc0b`)

## interfaces (2 claim(s))

- [observation/documented] Slash commands include /swarm help, status, show-plan, agents, diagnose, evidence, and reset --confirm; deprecated aliases like /swarm plan and /swarm info still function but are hidden from help. -- evidence: [README.md#L291-L291](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L291-L291), [README.md#L273-L281](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L273-L281), [README.md#L293-L305](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L293-L305), [README.md#L307-L307](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L307-L307) (`clm_5070f17df1fe0a91481c35870c8a8dcbebc6d533bdc656883eebd9cdd3d5c2cf`)
- [observation/documented] Session modes are toggled via slash commands (balanced default, turbo, lean turbo, full-auto) while project mode is set persistently via the execution_mode config key (strict, balanced, fast). -- evidence: [README.md#L157-L157](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L157-L157), [README.md#L149-L149](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L149-L149), [README.md#L138-L143](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L138-L143), [README.md#L151-L155](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L151-L155), [README.md#L136-L136](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L136-L136) (`clm_745856266830a1c250f163740d2fa551d146c81be61e353a9eb83dddf9bd2ba7`)

## memory-state (1 claim(s))

- [observation/documented] All project state lives under .swarm/: plan-ledger.jsonl as authoritative source, context.md, evidence/, telemetry.jsonl, and curator-summary.json; sessions are resumable, skipping discovery when state exists. -- evidence: [README.md#L518-L518](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L518-L518), [README.md#L520-L520](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L520-L520), [README.md#L512-L512](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L512-L512), [README.md#L514-L514](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L514-L514), [README.md#L516-L516](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L516-L516), [README.md#L128-L128](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L128-L128) (`clm_cc8d96af30ea61a78a259ced6982e312765c5b4282a06370c4cd5870f0ed207f`)

## orchestration (2 claim(s))

- [observation/documented] A Swarm architect coordinates all internal agents automatically; users never manually switch roles, and if the active OpenCode agent is not a Swarm architect the plugin workflow is bypassed. -- evidence: [README.md#L56-L56](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L56-L56), [README.md#L313-L313](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L313-L313) (`clm_a76b520c22e5337ddcfeb7af14544d0d2f85df16f81284a70df3f2c8ffc0f0e3`)
- [observation/documented] Every agent runs inside a circuit breaker with defaults of 200 tool calls, 30-minute duration, 10x same-tool repetition, and 5 consecutive errors, reset per task with per-agent overrides available. -- evidence: [README.md#L526-L531](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L526-L531), [README.md#L533-L533](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L533-L533), [README.md#L524-L524](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L524-L524) (`clm_512d036dd1b953bcfcdd4ad222ee49c3dfe258172159d4d3b7759badbb4503c5`)

## tools-permissions (3 claim(s))

- [observation/documented] Per-agent file authority restricts writes: coder to src/tests/docs/scripts, reviewer to .swarm/evidence, explorer and sme read-only, overridable via authority.rules config. -- evidence: [README.md#L547-L547](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L547-L547), [README.md#L541-L545](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L541-L545), [README.md#L539-L539](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L539-L539) (`clm_9e8ff51a3f4f73b3a3d7b3f16568e872e49bc3690cb8eb9e5b28a2737b77d4d6`)
- [observation/documented] Shell write detection statically analyzes commands (bash-parser AST for POSIX, regex for PowerShell/cmd) to intercept redirects, write builtins, in-place edits, downloads, and destructive git operations before execution. -- evidence: [README.md#L62-L62](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L62-L62), [README.md#L76-L79](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L76-L79), [README.md#L66-L74](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L66-L74) (`clm_637132fa5b482cc9775e48c03591257212c91aba29fb66288cc97109ac74fdd5`)
- [observation/documented] Declared task scopes persist to .swarm/scopes/scope-{taskId}.json with 24-hour TTL default, symlink guards, and fail-closed validation; recursive deletes are blocked unless targets fall within scope. -- evidence: [README.md#L85-L89](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L85-L89) (`clm_1b82732244aeee43b333d731bebe2643fb94641ca114f6da0a2f569c0a9673fe`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation requires Bun >= 1.3.13 or Node.js >= 22.13 for npm installs, with the Node-hosted sidecar using the built-in node:sqlite module. -- evidence: [README.md#L25-L25](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L25-L25) (`clm_470eccd6b9e191c97674dbe01ae6b610a7a70f3fb1e4a1ecfff4ea44d4ee9ab0`)

## limitations (1 claim(s))

- [observation/documented] The README notes some PRM configuration fields (max_trajectory_lines, escalation_enabled) are defined in schema but not yet enforced at runtime. -- evidence: [README.md#L508-L508](https://github.com/ZaxbyHub/opencode-swarm/blob/7f125e8f751b0a2d54cb014f823e46bd47ce5efa/README.md#L508-L508) (`clm_818bf167be682d2499db5ea26ef5ea1d878879986eb93948abb5be5b51358642`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

