# dicklesworthstone/ntm

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3c35f474879f @ 5c8f6d031fcbbfb6

## Summary (orientation draft, not independently verified)

NTM is a Go binary that turns tmux into a local control plane for orchestrating multiple coding-agent panes, with safety/approval workflows, Agent Mail coordination, durable state, and robot/REST automation surfaces. Evidence is README-only, so claims are documentation-based. Evidence coverage: 151 of 250 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 66 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] NTM is a single Go binary combining tmux session orchestration, work triage, safety policy and approvals, Agent Mail coordination, durable state capture, and a local REST/WebSocket API. -- evidence: [README.md#L16-L19](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L16-L19), [README.md#L65-L65](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L65-L65)
- design-choices (1 claim(s)):
  - [observation/documented] Stated design principles include no silent data loss, graceful degradation when optional integrations are missing, idempotent orchestration, auditable actions, and safe-by-default destructive-operation handling. -- evidence: [README.md#L679-L680](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L679-L680), [README.md#L656-L657](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L656-L657), [README.md#L661-L662](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L661-L662), [README.md#L666-L667](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L666-L667), [README.md#L675-L675](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L675-L675)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's Development section gives build and verification commands (go build ./cmd/ntm, go test -short ./..., golangci-lint run). -- evidence: [README.md#L863-L863](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L863-L863), [README.md#L865-L869](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L865-L869)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes machine-readable automation via --robot-* CLI flags plus an ntm serve server offering REST under /api/v1, SSE at /events, WebSocket at /ws, /health, and a generated OpenAPI spec. -- evidence: [README.md#L500-L503](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L500-L503), [README.md#L492-L496](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L492-L496), [README.md#L454-L455](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L454-L455)
  - [observation/documented] Custom agent types load from TOML files in an agents/ directory next to the config, declaring name/alias spawn selectors, a command template, and optional readiness regexes; NTM never modifies files in agents/. -- evidence: [README.md#L618-L626](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L618-L626)
- memory-state (1 claim(s)):
  - [observation/documented] Durable state features include checkpoints, timelines, audit logs, history search, pipeline state with resume, and saved sessions; pipeline resume preserves completed step outputs by default and re-runs the first incomplete step. -- evidence: [README.md#L442-L448](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L442-L448), [README.md#L437-L440](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L437-L440), [README.md#L433-L435](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L433-L435), [README.md#L426-L429](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L426-L429)
- orchestration (2 claim(s)):
  - [observation/documented] NTM spawns named tmux sessions with labeled agent panes and a user pane, supports labels for multiple swarms per project, and --worktrees creates per-agent ntm/<session>/<agent> branches and worktrees for isolation. -- evidence: [README.md#L112-L114](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L112-L114), [README.md#L160-L161](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L160-L161), [README.md#L172-L175](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L172-L175)
  - [observation/documented] Automated assignment treats tracker labels as an authorization boundary: operator-gated labels are configurable in .ntm/config.toml, project labels extend but cannot remove built-in gates, and any plan or coverage failure stops assignment before dispatch. -- evidence: [README.md#L235-L239](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L235-L239), [README.md#L226-L228](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L226-L228)
- tools-permissions (2 claim(s)):
More evidence: [full detail](ntm.detail.md)

Metadata and full claim list: [full detail](ntm.detail.md)
Human notes ([notes](ntm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
