# tempont/small-opencode-orchestrator -- full detail

[Back to orientation](small-opencode-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tempont/small-opencode-orchestrator/8f7702cef997bb852f62b07b37146692806c3a4a/8d5411959d6f036b.json](../../../wiki/dossiers/tempont/small-opencode-orchestrator/8f7702cef997bb852f62b07b37146692806c3a4a/8d5411959d6f036b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repo ships eleven agent definition files (orchestrator, plan-runner, code-executor, test-verifier, code-reviewer, docs-reviewer, security-reviewer, spec-critic, api-docs-researcher, host-security-investigator, code-explorer), a plugin source file, model profiles, and skills directories. -- evidence: [README.md#L45-L91](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L45-L91) (`clm_052571a1c1da8ea7b55ebdaa74f87c9cf4cea6e5a99254afd7c39f8173633377`)

## design-choices (1 claim(s))

- [observation/documented] The project is intentionally small and not a general-purpose agent platform; goals include understandable orchestration, reduced inter-agent context, explicit planning/review, and avoiding automation that hides what is happening. -- evidence: [README.md#L31-L31](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L31-L31), [README.md#L35-L41](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L35-L41) (`clm_94f6e2d6e5bc4d7aa873614dab8a327ba546955f0b7dfa7eb98134e192acf4c1`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributing agents to plan before non-trivial edits, keep diffs small and reversible, verify with the narrowest sufficient command and never claim success without output, and never push without explicit user intent. -- evidence: [AGENTS.md#L23-L26](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L23-L26), [AGENTS.md#L7-L11](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L7-L11), [AGENTS.md#L15-L19](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L15-L19), [AGENTS.md#L48-L50](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L48-L50) (`clm_8a9c8c329eec4604560aef3deec7c2bc32dc58eb39f61719ce48c3ae8b499577`)
- [observation/documented] Repository development practice: AGENTS.md prescribes strict role separation (code-explorer read-only, code-executor writes without exploring, code-reviewer neither writes nor explores) and a typical delegation order from exploration through review. -- evidence: [AGENTS.md#L34-L36](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L34-L36), [AGENTS.md#L38-L38](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L38-L38) (`clm_06c3dbf08fd8321eb9d057ad62c53946e1075cb8a3790d96fa883330c0b04f77`)

## skills-patterns (1 claim(s))

- [observation/documented] Shared skills include agent-delegation (routing decision table), task-management (CLI tracking feature subtasks with dependencies), pythonic-quality, security-investigation, and skill-creator. -- evidence: [README.md#L218-L222](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L218-L222) (`clm_19dfb56f8ede235698ab5a67a970b9ba69f15e6b5b88430f89e36cf25ec7f891`)

## interfaces (2 claim(s))

- [observation/documented] A plugin, plugin-src/plan-post-approval.ts loaded via the plugin tuple in opencode.jsonc, automates handoff after PlanApprove: it extracts plan paths, routes plan sessions to build via session.summarize and session.prompt with backoff retries, and reads plan_post_approval_handoff_agent from plugin options. -- evidence: [README.md#L209-L214](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L209-L214), [README.md#L205-L205](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L205-L205) (`clm_77ffb8378a20cbe48320c90f3889366b2c0ad9968bd963a66d813154c4570b8f`)
- [observation/documented] Configuration supports alternate model profiles under profiles/* that merge additively over the global opencode.jsonc, selected via the OPENCODE_CONFIG environment variable; profiles only override models and variants while inheriting plugins and permissions. -- evidence: [README.md#L149-L153](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L149-L153), [README.md#L142-L143](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L142-L143), [README.md#L145-L145](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L145-L145) (`clm_f1d68e2463f56d7957cc7a4bfbfadeccf95cb0c036dd027b77285f382ad5130b`)

## memory-state (1 claim(s))

- [observation/documented] Concrete plans are written as files under .opencode/plans/, and the task-management skill includes TypeScript scripts (task-cli.ts, migrate-schema.ts) plus a router.sh for tracking feature subtasks. -- evidence: [README.md#L218-L222](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L218-L222), [README.md#L45-L91](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L45-L91), [README.md#L99-L104](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L99-L104) (`clm_3ac761b8b4fe21289e374fd08e07b31ddd65466deef4c8d0815dc9eb9f635b68`)

## orchestration (2 claim(s))

- [observation/documented] The default entry point is the orchestrator agent; for non-trivial tasks it delegates planning, writes a plan under .opencode/plans/, obtains user approval, then delegates implementation in scoped slices followed by review agents. -- evidence: [README.md#L245-L245](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L245-L245), [README.md#L95-L95](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L95-L95), [README.md#L99-L104](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L99-L104) (`clm_c5e87c823659c35b2fb41aee4c91621c8d93bc67c36c0e1e27aed676c8db1287`)
- [observation/documented] Subagents receive focused tasks rather than the full problem context when possible, an approach the README describes as token-conscious delegation. -- evidence: [README.md#L22-L27](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L22-L27) (`clm_c14f5a145426c3a5009dc2f8808ebb2f91ed12d8841553076fe830ab86c64058`)

## tools-permissions (2 claim(s))

- [observation/documented] opencode.jsonc provides a minimal deny-by-default workspace permission baseline, and each agent declares its own tool policy in its agents/<id>.md frontmatter. -- evidence: [README.md#L267-L271](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L267-L271) (`clm_febdbcdb88fb466a33a45a7ba82bfc319a1bfc594fb00e8f4e416a1b798d6507`)
- [observation/documented] The orchestrator agent has no write permissions by default to force subagent usage, and per AGENTS.md it must not use native read, glob, grep, list, lsp, or bash tools for repo discovery, delegating to code-explorer instead. -- evidence: [README.md#L309-L318](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L309-L318), [AGENTS.md#L42-L42](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L42-L42) (`clm_1161a84c8f529c80732b7fbb8a9b5d9f9d9dd5b9ea72df9919e89c954a67fe44`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project depends on OpenCode itself and npm dependencies installed via npm install in the config directory; the changelog notes @opencode-ai/plugin aligned to 1.14.20. -- evidence: [README.md#L226-L226](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L226-L226), [README.md#L278-L288](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L278-L288), [README.md#L236-L239](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L236-L239) (`clm_281ad775e8af44edfd9e8652234069f68bf53b030257eba1d51062df4cb95854`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

