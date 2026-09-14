---
access: public
aliases: []
claim_ids:
- clm_052571a1c1da8ea7b55ebdaa74f87c9cf4cea6e5a99254afd7c39f8173633377
- clm_1161a84c8f529c80732b7fbb8a9b5d9f9d9dd5b9ea72df9919e89c954a67fe44
- clm_19dfb56f8ede235698ab5a67a970b9ba69f15e6b5b88430f89e36cf25ec7f891
- clm_281ad775e8af44edfd9e8652234069f68bf53b030257eba1d51062df4cb95854
- clm_3ac761b8b4fe21289e374fd08e07b31ddd65466deef4c8d0815dc9eb9f635b68
- clm_77ffb8378a20cbe48320c90f3889366b2c0ad9968bd963a66d813154c4570b8f
- clm_94f6e2d6e5bc4d7aa873614dab8a327ba546955f0b7dfa7eb98134e192acf4c1
- clm_c14f5a145426c3a5009dc2f8808ebb2f91ed12d8841553076fe830ab86c64058
- clm_c5e87c823659c35b2fb41aee4c91621c8d93bc67c36c0e1e27aed676c8db1287
- clm_f1d68e2463f56d7957cc7a4bfbfadeccf95cb0c036dd027b77285f382ad5130b
- clm_febdbcdb88fb466a33a45a7ba82bfc319a1bfc594fb00e8f4e416a1b798d6507
maturity: draft
page_id: pg_9b70e5b299e15ff1a1ff5319a7662687
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cc7e9e9911445a7fa0c6bfce0558567c
title: tempont/small-opencode-orchestrator/README.md @ 8f7702cef997
updated_at: '2026-09-14T04:25:44Z'
---

# tempont/small-opencode-orchestrator/README.md @ 8f7702cef997

<!-- rcw:begin owner=source:src_cc7e9e9911445a7fa0c6bfce0558567c block=evidence -->
- The repo ships eleven agent definition files (orchestrator, plan-runner, code-executor, test-verifier, code-reviewer, docs-reviewer, security-reviewer, spec-critic, api-docs-researcher, host-security-investigator, code-explorer), a plugin source file, model profiles, and skills directories. [@claim:clm_052571a1c1da8ea7b55ebdaa74f87c9cf4cea6e5a99254afd7c39f8173633377]
- The orchestrator agent has no write permissions by default to force subagent usage, and per AGENTS.md it must not use native read, glob, grep, list, lsp, or bash tools for repo discovery, delegating to code-explorer instead. [@claim:clm_1161a84c8f529c80732b7fbb8a9b5d9f9d9dd5b9ea72df9919e89c954a67fe44]
- Shared skills include agent-delegation (routing decision table), task-management (CLI tracking feature subtasks with dependencies), pythonic-quality, security-investigation, and skill-creator. [@claim:clm_19dfb56f8ede235698ab5a67a970b9ba69f15e6b5b88430f89e36cf25ec7f891]
- The project depends on OpenCode itself and npm dependencies installed via npm install in the config directory; the changelog notes @opencode-ai/plugin aligned to 1.14.20. [@claim:clm_281ad775e8af44edfd9e8652234069f68bf53b030257eba1d51062df4cb95854]
- Concrete plans are written as files under .opencode/plans/, and the task-management skill includes TypeScript scripts (task-cli.ts, migrate-schema.ts) plus a router.sh for tracking feature subtasks. [@claim:clm_3ac761b8b4fe21289e374fd08e07b31ddd65466deef4c8d0815dc9eb9f635b68]
- A plugin, plugin-src/plan-post-approval.ts loaded via the plugin tuple in opencode.jsonc, automates handoff after PlanApprove: it extracts plan paths, routes plan sessions to build via session.summarize and session.prompt with backoff retries, and reads plan_post_approval_handoff_agent from plugin options. [@claim:clm_77ffb8378a20cbe48320c90f3889366b2c0ad9968bd963a66d813154c4570b8f]
- The project is intentionally small and not a general-purpose agent platform; goals include understandable orchestration, reduced inter-agent context, explicit planning/review, and avoiding automation that hides what is happening. [@claim:clm_94f6e2d6e5bc4d7aa873614dab8a327ba546955f0b7dfa7eb98134e192acf4c1]
- Subagents receive focused tasks rather than the full problem context when possible, an approach the README describes as token-conscious delegation. [@claim:clm_c14f5a145426c3a5009dc2f8808ebb2f91ed12d8841553076fe830ab86c64058]
- The default entry point is the orchestrator agent; for non-trivial tasks it delegates planning, writes a plan under .opencode/plans/, obtains user approval, then delegates implementation in scoped slices followed by review agents. [@claim:clm_c5e87c823659c35b2fb41aee4c91621c8d93bc67c36c0e1e27aed676c8db1287]
- Configuration supports alternate model profiles under profiles/* that merge additively over the global opencode.jsonc, selected via the OPENCODE_CONFIG environment variable; profiles only override models and variants while inheriting plugins and permissions. [@claim:clm_f1d68e2463f56d7957cc7a4bfbfadeccf95cb0c036dd027b77285f382ad5130b]
- opencode.jsonc provides a minimal deny-by-default workspace permission baseline, and each agent declares its own tool policy in its agents/<id>.md frontmatter. [@claim:clm_febdbcdb88fb466a33a45a7ba82bfc319a1bfc594fb00e8f4e416a1b798d6507]
<!-- rcw:end owner=source:src_cc7e9e9911445a7fa0c6bfce0558567c block=evidence -->

## Researcher notes

