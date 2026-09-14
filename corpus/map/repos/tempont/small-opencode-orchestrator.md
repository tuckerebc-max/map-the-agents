# tempont/small-opencode-orchestrator

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8f7702cef997 @ 8d5411959d6f036b

## Summary (orientation draft, not independently verified)

The repository is an OpenCode configuration implementing a multi-agent orchestrator pattern with planning, approval-gated implementation, review subagents, model profiles, and a plan post-approval plugin; AGENTS.md provides contributor-facing delegation and verification guidance.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repo ships eleven agent definition files (orchestrator, plan-runner, code-executor, test-verifier, code-reviewer, docs-reviewer, security-reviewer, spec-critic, api-docs-researcher, host-security-investigator, code-explorer), a plugin source file, model profiles, and skills directories. -- evidence: [README.md#L45-L91](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L45-L91)
- design-choices (1 claim(s)):
  - [observation/documented] The project is intentionally small and not a general-purpose agent platform; goals include understandable orchestration, reduced inter-agent context, explicit planning/review, and avoiding automation that hides what is happening. -- evidence: [README.md#L31-L31](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L31-L31), [README.md#L35-L41](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L35-L41)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributing agents to plan before non-trivial edits, keep diffs small and reversible, verify with the narrowest sufficient command and never claim success without output, and never push without explicit user intent. -- evidence: [AGENTS.md#L23-L26](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L23-L26), [AGENTS.md#L7-L11](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L7-L11), [AGENTS.md#L15-L19](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L15-L19), [AGENTS.md#L48-L50](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L48-L50)
  - [observation/documented] Repository development practice: AGENTS.md prescribes strict role separation (code-explorer read-only, code-executor writes without exploring, code-reviewer neither writes nor explores) and a typical delegation order from exploration through review. -- evidence: [AGENTS.md#L34-L36](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L34-L36), [AGENTS.md#L38-L38](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/AGENTS.md#L38-L38)
- skills-patterns (1 claim(s)):
  - [observation/documented] Shared skills include agent-delegation (routing decision table), task-management (CLI tracking feature subtasks with dependencies), pythonic-quality, security-investigation, and skill-creator. -- evidence: [README.md#L218-L222](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L218-L222)
- interfaces (2 claim(s)):
  - [observation/documented] A plugin, plugin-src/plan-post-approval.ts loaded via the plugin tuple in opencode.jsonc, automates handoff after PlanApprove: it extracts plan paths, routes plan sessions to build via session.summarize and session.prompt with backoff retries, and reads plan_post_approval_handoff_agent from plugin options. -- evidence: [README.md#L209-L214](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L209-L214), [README.md#L205-L205](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L205-L205)
  - [observation/documented] Configuration supports alternate model profiles under profiles/* that merge additively over the global opencode.jsonc, selected via the OPENCODE_CONFIG environment variable; profiles only override models and variants while inheriting plugins and permissions. -- evidence: [README.md#L149-L153](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L149-L153), [README.md#L142-L143](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L142-L143), [README.md#L145-L145](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L145-L145)
- memory-state (1 claim(s)):
  - [observation/documented] Concrete plans are written as files under .opencode/plans/, and the task-management skill includes TypeScript scripts (task-cli.ts, migrate-schema.ts) plus a router.sh for tracking feature subtasks. -- evidence: [README.md#L218-L222](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L218-L222), [README.md#L45-L91](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L45-L91), [README.md#L99-L104](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L99-L104)
- orchestration (2 claim(s)):
  - [observation/documented] The default entry point is the orchestrator agent; for non-trivial tasks it delegates planning, writes a plan under .opencode/plans/, obtains user approval, then delegates implementation in scoped slices followed by review agents. -- evidence: [README.md#L245-L245](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L245-L245), [README.md#L95-L95](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L95-L95), [README.md#L99-L104](https://github.com/tempont/small-opencode-orchestrator/blob/8f7702cef997bb852f62b07b37146692806c3a4a/README.md#L99-L104)
More evidence: [full detail](small-opencode-orchestrator.detail.md)

Metadata and full claim list: [full detail](small-opencode-orchestrator.detail.md)
Human notes ([notes](small-opencode-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
