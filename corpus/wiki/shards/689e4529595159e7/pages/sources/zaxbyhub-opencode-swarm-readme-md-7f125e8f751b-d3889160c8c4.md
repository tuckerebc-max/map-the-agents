---
access: public
aliases: []
claim_ids:
- clm_1b82732244aeee43b333d731bebe2643fb94641ca114f6da0a2f569c0a9673fe
- clm_3f6276ac7af9effb3c97d9c80fd79a35118398d4f37919bf9803b9cde14301ec
- clm_470eccd6b9e191c97674dbe01ae6b610a7a70f3fb1e4a1ecfff4ea44d4ee9ab0
- clm_5070f17df1fe0a91481c35870c8a8dcbebc6d533bdc656883eebd9cdd3d5c2cf
- clm_512d036dd1b953bcfcdd4ad222ee49c3dfe258172159d4d3b7759badbb4503c5
- clm_637132fa5b482cc9775e48c03591257212c91aba29fb66288cc97109ac74fdd5
- clm_745856266830a1c250f163740d2fa551d146c81be61e353a9eb83dddf9bd2ba7
- clm_818bf167be682d2499db5ea26ef5ea1d878879986eb93948abb5be5b51358642
- clm_9e8ff51a3f4f73b3a3d7b3f16568e872e49bc3690cb8eb9e5b28a2737b77d4d6
- clm_a50a29e048c031836f58dee920145352b8e5b906bafdd41e12c08f6a9e88bc0b
- clm_a76b520c22e5337ddcfeb7af14544d0d2f85df16f81284a70df3f2c8ffc0f0e3
- clm_ae028039f5e456161f35305ce871ea5f3f78f8cd46f70621c6aa3bd496ddd2be
- clm_cc8d96af30ea61a78a259ced6982e312765c5b4282a06370c4cd5870f0ed207f
- clm_eb511d332b8b6e20bf1e3a825c946ca706ffcf25d4c3798990d47683fcc86c22
- clm_f731f55bf02f31e47433ce01eb812333e69e78da9a4f05fb18d21a0a69196f1e
maturity: draft
page_id: pg_f1bbcddf90505258907ed3889160c8c4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c01ca3e3d8aa57eb95521c277e643878
title: ZaxbyHub/opencode-swarm/README.md @ 7f125e8f751b
updated_at: '2026-09-14T04:33:39Z'
---

# ZaxbyHub/opencode-swarm/README.md @ 7f125e8f751b

<!-- rcw:begin owner=source:src_c01ca3e3d8aa57eb95521c277e643878 block=evidence -->
- Declared task scopes persist to .swarm/scopes/scope-{taskId}.json with 24-hour TTL default, symlink guards, and fail-closed validation; recursive deletes are blocked unless targets fall within scope. [@claim:clm_1b82732244aeee43b333d731bebe2643fb94641ca114f6da0a2f569c0a9673fe]
- The pipeline is gated: code does not ship without reviewer and test-engineer approval, and agents never mutate the codebase in parallel. [@claim:clm_3f6276ac7af9effb3c97d9c80fd79a35118398d4f37919bf9803b9cde14301ec]
- Installation requires Bun >= 1.3.13 or Node.js >= 22.13 for npm installs, with the Node-hosted sidecar using the built-in node:sqlite module. [@claim:clm_470eccd6b9e191c97674dbe01ae6b610a7a70f3fb1e4a1ecfff4ea44d4ee9ab0]
- Slash commands include /swarm help, status, show-plan, agents, diagnose, evidence, and reset --confirm; deprecated aliases like /swarm plan and /swarm info still function but are hidden from help. [@claim:clm_5070f17df1fe0a91481c35870c8a8dcbebc6d533bdc656883eebd9cdd3d5c2cf]
- Every agent runs inside a circuit breaker with defaults of 200 tool calls, 30-minute duration, 10x same-tool repetition, and 5 consecutive errors, reset per task with per-agent overrides available. [@claim:clm_512d036dd1b953bcfcdd4ad222ee49c3dfe258172159d4d3b7759badbb4503c5]
- Shell write detection statically analyzes commands (bash-parser AST for POSIX, regex for PowerShell/cmd) to intercept redirects, write builtins, in-place edits, downloads, and destructive git operations before execution. [@claim:clm_637132fa5b482cc9775e48c03591257212c91aba29fb66288cc97109ac74fdd5]
- Session modes are toggled via slash commands (balanced default, turbo, lean turbo, full-auto) while project mode is set persistently via the execution_mode config key (strict, balanced, fast). [@claim:clm_745856266830a1c250f163740d2fa551d146c81be61e353a9eb83dddf9bd2ba7]
- The README notes some PRM configuration fields (max_trajectory_lines, escalation_enabled) are defined in schema but not yet enforced at runtime. [@claim:clm_818bf167be682d2499db5ea26ef5ea1d878879986eb93948abb5be5b51358642]
- Per-agent file authority restricts writes: coder to src/tests/docs/scripts, reviewer to .swarm/evidence, explorer and sme read-only, overridable via authority.rules config. [@claim:clm_9e8ff51a3f4f73b3a3d7b3f16568e872e49bc3690cb8eb9e5b28a2737b77d4d6]
- Seven skill lifecycle tools (skill_generate through skill_improve) are opt-in via skills.enabled (default false); with the flag off they are host-denied for all agents except skill_improver. [@claim:clm_a50a29e048c031836f58dee920145352b8e5b906bafdd41e12c08f6a9e88bc0b]
- A Swarm architect coordinates all internal agents automatically; users never manually switch roles, and if the active OpenCode agent is not a Swarm architect the plugin workflow is bypassed. [@claim:clm_a76b520c22e5337ddcfeb7af14544d0d2f85df16f81284a70df3f2c8ffc0f0e3]
- Skill propagation logs usage to .swarm/skill-usage.jsonl, scores relevance (threshold 0.5, max 5 recommendations), optionally enforces a SKILLS: field on delegations, and supports .opencode/skill-routing.yaml routing. [@claim:clm_ae028039f5e456161f35305ce871ea5f3f78f8cd46f70621c6aa3bd496ddd2be]
- All project state lives under .swarm/: plan-ledger.jsonl as authoritative source, context.md, evidence/, telemetry.jsonl, and curator-summary.json; sessions are resumable, skipping discovery when state exists. [@claim:clm_cc8d96af30ea61a78a259ced6982e312765c5b4282a06370c4cd5870f0ed207f]
- The plugin registers a roster of specialized agents including architect, coder, reviewer, test_engineer, critic, explorer, sme, docs, designer, plus optional and conditional critic, curator, and council agents. [@claim:clm_eb511d332b8b6e20bf1e3a825c946ca706ffcf25d4c3798990d47683fcc86c22]
- A Process Remediation Model detects five failure patterns (repetition loop, ping-pong, expansion drift, stuck-on-test, context thrashing) and escalates from advisory guidance to architect alert to hard stop. [@claim:clm_f731f55bf02f31e47433ce01eb812333e69e78da9a4f05fb18d21a0a69196f1e]
<!-- rcw:end owner=source:src_c01ca3e3d8aa57eb95521c277e643878 block=evidence -->

## Researcher notes

