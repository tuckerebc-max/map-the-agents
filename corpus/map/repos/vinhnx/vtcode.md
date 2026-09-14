# vinhnx/vtcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 18f7d26c76e2 @ d83edd9c49fa70e2

## Summary (orientation draft, not independently verified)

VT Code is a Rust terminal coding agent with a harness architecture (tools, sandbox, context compaction, event stream), TOML-based layered configuration with live reload, and documented plan/build/evaluate orchestration and delegation semantics. Evidence is documentation-heavy; no contributor workflow or eval-harness execution evidence appears in these slices. Evidence coverage: 132 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 246 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] VT Code is described as a secure, open-source terminal coding agent written in Rust, shipped as a single static binary for interactive and long-running autonomous work. -- evidence: [README.md#L7-L7](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L7-L7), [README.md#L62-L62](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L62-L62)
- components (1 claim(s)):
  - [observation/documented] ThreadEvent (vtcode-exec-events) is the authoritative runtime event contract feeding replay, checkpoints, memory, and trajectory export; follow-up inputs queue and inject one at a time at idle boundaries. -- evidence: [README.md#L91-L97](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L91-L97), [docs/ARCHITECTURE.md#L44-L44](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L44-L44)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture separates the model (reasoning) from the harness (runtime supplying tools, context, sandboxing, state, and verification), organized as seven reinforcing subsystems. -- evidence: [docs/ARCHITECTURE.md#L26-L30](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L26-L30), [README.md#L64-L64](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L64-L64)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI separates data on stdout from diagnostics on stderr, uses clap for argument parsing, isolates subcommands (ask, exec, chat) in dedicated modules, and handles SIGINT/SIGTERM gracefully. -- evidence: [docs/ARCHITECTURE.md#L108-L111](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L108-L111)
  - [observation/documented] Default public tool surface includes exec_command (shell via policy/sandbox/approvals), write_stdin for live-session continuation, and apply_patch with workspace-boundary checks. -- evidence: [docs/ARCHITECTURE.md#L196-L198](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L196-L198)
- memory-state (1 claim(s)):
  - [observation/documented] A persisted SessionMemoryEnvelope summarizes objective, constraints, touched files, grounded facts, verification status, and delegated findings for resume and summarized-fork handoff. -- evidence: [docs/ARCHITECTURE.md#L34-L42](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L34-L42), [docs/ARCHITECTURE.md#L89-L93](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L89-L93)
- orchestration (2 claim(s)):
  - [observation/documented] With agent.harness.orchestration_mode = plan_build_evaluate, a planner writes spec/contract artifacts, the generator runs on the main session, and an evaluator performs a skeptical post-build pass; failed evaluation triggers bounded revision rounds. -- evidence: [docs/ARCHITECTURE.md#L74-L75](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L74-L75), [docs/ARCHITECTURE.md#L77-L80](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L77-L80)
  - [observation/documented] Delegation is modeled as explicit thread spawning: child agents do bounded sidecar work, their output is advisory until the parent validates and merges it into the SessionMemoryEnvelope at turn boundaries. -- evidence: [docs/ARCHITECTURE.md#L89-L93](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L89-L93), [docs/ARCHITECTURE.md#L87-L87](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L87-L87)
- tools-permissions (1 claim(s)):
  - [observation/documented] Feature flags include human_in_the_loop (tool approval prompts, default true) and mcp_enabled (default false), toggled via the [features] table in vtcode.toml. -- evidence: [docs/config/config.md#L106-L112](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L106-L112), [docs/config/config.md#L96-L102](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L96-L102)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](vtcode.detail.md)

Metadata and full claim list: [full detail](vtcode.detail.md)
Human notes ([notes](vtcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
