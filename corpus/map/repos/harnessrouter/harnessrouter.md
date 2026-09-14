# harnessrouter/harnessrouter

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5637717816b5 @ c748d5b31d944b02

## Summary (orientation draft, not independently verified)

Evidence covers HarnessRouter Community Edition: a self-hosted Docker deployment exposing an OpenAI Responses-compatible API (UHP) over a Console/Gateway/Runner architecture, plus contributor workflow rules in CONTRIBUTING.md. No source code slices are present, so claims are documentation-based.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] One Docker container runs three parts: Console on :3000 (only published port, entry point for UI and API), Gateway on :8080 (Responses API and harness lifecycle), and Runner on :8081 (runs harnesses in session workspaces). -- evidence: [README.md#L325-L325](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L325-L325), [README.md#L311-L323](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L311-L323)
  - [observation/documented] A /data volume persists the database, files, secrets, installed harness CLIs, and workspaces across container restarts. -- evidence: [README.md#L76-L76](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L76-L76), [README.md#L311-L323](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L311-L323)
- design-choices (2 claim(s)):
  - [observation/documented] Sessions use separate workspaces and operating-system users rather than separate containers; the Console and Gateway run unprivileged while the entrypoint and Runner need root to manage per-session users. -- evidence: [README.md#L325-L325](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L325-L325), [README.md#L85-L85](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L85-L85)
  - [observation/documented] Community Edition disables the Console analytics pipeline, and provider keys, sessions, files, and workspaces remain under the self-hosting operator's control. -- evidence: [README.md#L286-L289](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L286-L289)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: substantial changes require an issue describing problem, proposal, and impact before implementation; small obvious fixes may go straight to a pull request. -- evidence: [CONTRIBUTING.md#L27-L29](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L27-L29), [CONTRIBUTING.md#L31-L32](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L31-L32)
  - [observation/documented] Repository development practice: protocol changes follow a UEP process (issue labelled 'uep' with Problem, Proposal, Compatibility, Alternatives; maintainer response within 10 working days; accepted UEPs land as one PR updating spec, schema, implementation, conformance test, and changelog). -- evidence: [CONTRIBUTING.md#L36-L42](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/CONTRIBUTING.md#L36-L42)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes an OpenAI Responses-compatible API; callers select a harness via metadata.harness_id and can set stream:true for server-sent events. -- evidence: [README.md#L197-L206](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L197-L206), [README.md#L35-L35](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L35-L35), [README.md#L186-L186](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L186-L186), [README.md#L208-L208](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L208-L208)
  - [observation/documented] The API surface supports starting tasks, continuing sessions with previous_response_id, streaming progress, file attach/retrieve, cancellation, and structured errors/traces. -- evidence: [README.md#L214-L224](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L214-L224)
- memory-state (1 claim(s)):
  - [observation/documented] The product handles persistent sessions: follow-up instructions can be sent with previous_response_id, and tasks with transcripts appear in the same Console workspace. -- evidence: [README.md#L214-L224](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L214-L224), [README.md#L35-L35](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L35-L35), [README.md#L208-L208](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L208-L208)
- orchestration (1 claim(s)):
  - [observation/documented] The Runner executes harnesses inside per-session workspaces, and the first container launch installs the enabled harness CLIs. -- evidence: [README.md#L97-L97](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L97-L97), [README.md#L325-L325](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L325-L325), [README.md#L311-L323](https://github.com/HarnessRouter/harnessrouter/blob/5637717816b5923c58bb3b1779e1ccab7359349f/README.md#L311-L323)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](harnessrouter.detail.md)

Metadata and full claim list: [full detail](harnessrouter.detail.md)
Human notes ([notes](harnessrouter.notes.md), never overwritten by build)

[Back to map index](../../index.md)
