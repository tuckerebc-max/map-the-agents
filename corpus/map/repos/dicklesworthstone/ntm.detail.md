# dicklesworthstone/ntm -- full detail

[Back to orientation](ntm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dicklesworthstone/ntm/3c35f474879f1f64e0a8448f71ec70da656570ad/5c8f6d031fcbbfb6.json](../../../wiki/dossiers/dicklesworthstone/ntm/3c35f474879f1f64e0a8448f71ec70da656570ad/5c8f6d031fcbbfb6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] NTM is a single Go binary combining tmux session orchestration, work triage, safety policy and approvals, Agent Mail coordination, durable state capture, and a local REST/WebSocket API. -- evidence: [README.md#L16-L19](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L16-L19), [README.md#L65-L65](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L65-L65) (`clm_cf2049569598bd6c38faf8a10a088498986ce784f3eba0016edff457d2c9605a`)

## design-choices (1 claim(s))

- [observation/documented] Stated design principles include no silent data loss, graceful degradation when optional integrations are missing, idempotent orchestration, auditable actions, and safe-by-default destructive-operation handling. -- evidence: [README.md#L679-L680](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L679-L680), [README.md#L656-L657](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L656-L657), [README.md#L661-L662](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L661-L662), [README.md#L666-L667](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L666-L667), [README.md#L675-L675](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L675-L675) (`clm_2e0fb02a8e5cb60f6c9ae00e476361c11c045990c3b3f2c64a43223a3b9b0cd1`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's Development section gives build and verification commands (go build ./cmd/ntm, go test -short ./..., golangci-lint run). -- evidence: [README.md#L863-L863](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L863-L863), [README.md#L865-L869](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L865-L869) (`clm_cab57b915db763974386d5d96386906777f874530f4c0af627cdcd5a7928b23f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes machine-readable automation via --robot-* CLI flags plus an ntm serve server offering REST under /api/v1, SSE at /events, WebSocket at /ws, /health, and a generated OpenAPI spec. -- evidence: [README.md#L500-L503](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L500-L503), [README.md#L492-L496](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L492-L496), [README.md#L454-L455](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L454-L455) (`clm_28a2aedfa9321ca60b9ebc7e1d13fb11b506cbbad2e8954efaef24cd1ec5c2e0`)
- [observation/documented] Custom agent types load from TOML files in an agents/ directory next to the config, declaring name/alias spawn selectors, a command template, and optional readiness regexes; NTM never modifies files in agents/. -- evidence: [README.md#L618-L626](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L618-L626) (`clm_11f65fda7bb8794881d634cabfd9da4720472afffe9e4414c1a6b5ae4cf56c4e`)

## memory-state (1 claim(s))

- [observation/documented] Durable state features include checkpoints, timelines, audit logs, history search, pipeline state with resume, and saved sessions; pipeline resume preserves completed step outputs by default and re-runs the first incomplete step. -- evidence: [README.md#L442-L448](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L442-L448), [README.md#L437-L440](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L437-L440), [README.md#L433-L435](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L433-L435), [README.md#L426-L429](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L426-L429) (`clm_e6d5c20d8d3b2a12df7b4db76d998040d6feabfa2058111409c23cbf6e9a3ee9`)

## orchestration (2 claim(s))

- [observation/documented] NTM spawns named tmux sessions with labeled agent panes and a user pane, supports labels for multiple swarms per project, and --worktrees creates per-agent ntm/<session>/<agent> branches and worktrees for isolation. -- evidence: [README.md#L112-L114](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L112-L114), [README.md#L160-L161](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L160-L161), [README.md#L172-L175](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L172-L175) (`clm_7146c544074f47c9fccb64d2dfa73bc5fe5bce693d2a990383d49f05959b4d1e`)
- [observation/documented] Automated assignment treats tracker labels as an authorization boundary: operator-gated labels are configurable in .ntm/config.toml, project labels extend but cannot remove built-in gates, and any plan or coverage failure stops assignment before dispatch. -- evidence: [README.md#L235-L239](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L235-L239), [README.md#L226-L228](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L226-L228) (`clm_de5796eda0afe09a6e1a846757c3d6a75382895a558b40ba5aec943627091acc`)

## tools-permissions (2 claim(s))

- [observation/documented] Destructive operations are governed by policy rules that allow, block, or approval-gate actions; approvals are durable and auditable, with two-person workflows where self-approval is rejected. -- evidence: [README.md#L378-L380](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L378-L380), [README.md#L315-L321](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L315-L321) (`clm_c6f2438413f9a631febb3b74d87347e692a23127511dfd50d1c9979289105ec6`)
- [observation/documented] ntm locks force-release is approval-gated by default (automation.force_release: approval): a second operator grants via ntm approve, and the serve HTTP endpoint and dashboard conflict action honor the same policy. -- evidence: [README.md#L315-L321](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L315-L321) (`clm_36c2aaa1c4508617f1d71c64a88832760a22fe172b7ffb58e0c9a213910b314e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] tmux is required; agent spawning needs CLIs such as Claude Code, Codex, Antigravity, or Grok Build (Gemini legacy); br, bv, Agent Mail, cass, dcg, and pt are optional integrations checkable via ntm deps -v. -- evidence: [README.md#L67-L70](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L67-L70) (`clm_579ff8daf1dd6c38ac5600ef26801a30e250c320ca1c8f42d84b8f5c59d054c1`)

## limitations (1 claim(s))

- [observation/documented] Documented limitations: tmux-centric, Linux/macOS primary, some workflows depend on external tools, Grok Build support is phase one (TUI readiness, prompt delivery, interrupt-with-message, restart, and restore-time relaunch fail closed), and it is local-first, not hosted SaaS. -- evidence: [README.md#L151-L158](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L151-L158), [README.md#L855-L859](https://github.com/Dicklesworthstone/ntm/blob/3c35f474879f1f64e0a8448f71ec70da656570ad/README.md#L855-L859) (`clm_6a2e44aa1e265a14c7468d894848b65b9fbc2a4ba487eb592265ad425644af0d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

