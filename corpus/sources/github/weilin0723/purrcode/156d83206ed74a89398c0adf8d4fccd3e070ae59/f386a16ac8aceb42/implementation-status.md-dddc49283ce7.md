# Implementation status

Updated: 2026-08-02 (UX trust/task/evidence implementation integrated locally; user and external qualification gates remain)

## v1.0 UX optimization — implemented locally, awaiting user acceptance

- Daemon-owned Ask/Plan/Build/Review, permission, execution-style, workflow, search, routing-capability, and budget contracts now reach the native runtime. New sessions default to Ask/Governed; read-only modes refuse mutation, Collaborative pauses at real boundaries, unsupported routing fails preflight, and external search/MCP usage is reserved durably before effects.
- Durable Spec Bundle, task graph, task retries, and requirement-linked evidence replay through NineLives. A command exit code never passes a task; final validation can close only executed work and explicit validation-only tasks. Required work without closing evidence blocks completion.
- Spec, Tasks, and Evidence have typed daemon presentation endpoints. The IDE consumes them through four bounded query workers plus dedicated ordinary/urgent control workers; Stop, approval, and terminal ownership bypass snapshot and mutation queues.
- IDE/Studio/TUI/CLI safe defaults and payloads are aligned. Studio execution style is no longer a toast-only control, TUI SSE reconnect preserves partial output, CLI skill installation uses the daemon lifecycle, and terminal resize/session filtering use the canonical contract.
- Recovery reconciliation never replays or discards effects automatically. Rollback in daemon/TUI/CLI requires an exact preview digest and explicit unattributed-effect acknowledgement. Invalid event append/replay fails loudly.
- Verification evidence and the user walkthrough were recorded in the v1.0 product-review cycle. Live provider/platform/accessibility and 30-task dogfood gates remain unperformed and explicitly external.

## v1.0 feat-adding-IDE — native desktop IDE (implemented locally)

- **`crates/purrcode-ide` is the v1.0 visual product**: a pure-Rust `eframe`/`egui` desktop application with no browser, no loopback portal and no dependency on a third-party editor. It draws the application bar, icon rail, session navigation, project tree, conversation Workbench, composer, syntax-highlighted editor, and the docked Diff/Tests/Terminal/Problems/Output panel itself.
- `purrcode ide --repository PATH` starts or reuses a compatible authenticated local daemon and opens the repository with no session selected. It never resumes a latest session implicitly; only an explicit `--session UUID --repository PATH` is accepted, after canonical repository ownership is verified. `crates/purrcode-cli` carries tests for that boundary and for never launching a browser or third-party editor.
- The VS Code extension has been **removed** from the repository together with its CI job and documentation.
- The IDE owns no session store, no model state, no permission state and no execution path. All HTTP runs on a worker thread and reaches the UI through channels, so an unreachable daemon reports itself as disconnected instead of freezing the window (covered by a test).
- The IDE enforces the canonical vocabulary at the boundary: an unknown runtime status resolves to a canonical label rather than reaching the screen, a plan awaiting review reads `Plan ready`, a repository with no worktree reports "no changes yet" rather than "0 files changed", and only `passed` validation renders as success.
- Three appearances (dark, light, high contrast) share one token set; every foreground/background pair is unit-tested against WCAG contrast floors.
- Native settings apply the selected appearance without writing repository state and expose explicit Apply/Reset actions; the window opens with the editor and artifact column visible rather than an empty right pane.
- Native IDE usability remediation now opens with Agent work and a persistent code/artifact column, uses the supplied blue-eyed longhair mascot consistently for every small product mark, and presents searchable responsive settings grouped around appearance, models/providers, authority, agent behavior, context/skills, terminal/Git, privacy/recovery, and diagnostics. A compact semantic type scale is shared across the workbench chrome and settings.
- Historical session loads are generation-bound bounded panel batches: every successful, empty, unavailable, failed, or queue-rejected panel completes one slot, the typed view model updates as each panel arrives, and a later selection cannot be overwritten by stale history. Background refreshes preserve the populated transcript and cannot overlap, so they no longer replace the visible session with a loading skeleton or cause periodic flashing.
- The Agent surface has one universal composer per frame: the ordinary right-panel toggle opens the read-only Changes/Source view, while an explicit Split is the only route that moves Agent into the auxiliary column. Routine tool/context activity is grouped into a collapsed, height-bounded Work log between the request and final answer; failed and blocked activity remains directly visible.
- Intermediate model rationale remains in durable execution/activity evidence instead of entering the user conversation. A `complete=true` turn that only inventories reads or says it is ready to answer receives at most two semantic repair attempts; repeated meta-completion fails closed rather than recording `SessionCompleted`, while a valid final answer is the only assistant message promoted into the transcript.
- New sessions use daemon-resolved `auto` task mode. Failed initial or follow-up messages restore the exact draft instead of discarding it. Settings can select a configured model for the current session, make one the daemon default role, and test/add provider profiles using keychain references only; the IDE never accepts a provider secret.
- The IDE consumes `/v1/models` defensively across array, `models`, `data`, `items`, and `results` envelopes, shows a configured model before a session exists, groups sessions by Today/Yesterday/date, and marks unread activity with a dot.
- New IDE sessions use an agent-directed strategy: the user describes the outcome and keeps permission explicit, while the daemon resolves direct conversation, read-only inspection, planning, review, or Build. A simple greeting completes without a workflow plan, worktree, or validation; explicit Plan/Review constraints remain available through intent/API contracts rather than an obligatory IDE mode picker.
- The workspace source-control rail is available without a selected session and shows branch, dirty-file count, and ten bounded recent commits. A GitHub remote is labeled as configured only; authentication and network reachability are never inferred from its URL.
- Legacy sessions whose event logs cannot replay are quarantined individually. Healthy repositories and new sessions remain usable, explicitly quarantined legacy rows are omitted from the IDE working list, older audit history is collapsed by default, and access/append to damaged sessions remains fail-closed without deleting durable records.
- Editor tabs show file-type colour icons, a bounded minimap, and cursor position; the dock is open by default with DIFF/TESTS/TERMINAL/PROBLEMS/OUTPUT available.
- The native terminal uses the daemon's typed PTY routes and the shared ANSI screen buffer for incremental output, input, stop, reconnect-safe offsets, and ownership generations. Diff review exposes daemon hunk digest plus Apply/Reject actions.
- Workspace continuity value objects cover canonical workspace identity, Auto/Ask/Off recall ranking, a bounded continuity capsule, and deterministic 60%/85% context compaction with same-session searchable-history retention.
- Added authenticated daemon presentation/control routes for summary, conversation, artifacts, changes, validation, usage, workflow controls, bootstrap, GitHub state, and file-diff content; all state remains daemon-owned
- Added Rust domain types for v1.0 adaptive orchestration:
  - TaskComplexity (Simple, Moderate, Complex, Unknown) with evidence-based classification
  - WorkflowProfile (Direct, Standard, Ultra) with bounded parallel specialist lanes
  - SearchPolicy (Off, Auto, Always) with evidence-triggered research
  - BudgetProfile (Economy, Balanced, MaxQuality, Custom) with token/cost enforcement
  - UsageRecord for per-request/model/provider/credential accounting
  - CredentialProfile/CredentialPool with secure reference storage and selection strategies
  - ModelRouteDecision with privacy-boundary enforcement and fallback policies
  - MCPServerProfile with transport/scope/trust and output limits
- Added production brand assets: icons (16/24/32/48/64/128/256/512px), monochrome cat-head SVGs, wordmark
- `purrcode studio` remains a secure browser maintenance/development client. It is not the v1.0 release IDE and nothing routes to it automatically.
- Updated README with v1.0 overview and development instructions
- Copied v1.0 PRD and reference assets into repo under docs/prd/ and brand/
- No second runtime or session store - all state flows through the daemon
- GitHub-native delivery is wired through explicit `git`/`gh` argument vectors for status, branch, pull request, checks, merge, and issue inspection; authentication remains intentionally interactive and never claims success when unavailable
- TUI workflow/search/budget controls update durable `SessionControls`; `/usage` exposes the recorded ledger and the header shows Auto/Direct/Standard/Ultra plus search policy
- `purrcode ide`, `/ide` from the TUI, and `purrcode resume --tui` all attach to the same daemon session in both directions; the IDE runs as its own process because a desktop event loop must own its main thread
- IDE problems/tests are sourced from the daemon's truthful validation artifacts; missing or skipped evidence renders as unavailable/pending, never as passing

## v0.8 PR6 — Test orchestration (complete locally)

- `purrcode-test-orchestrator` is the public orchestration crate, with the existing validation
  engine retained behind it for durable v0.7 evidence-schema compatibility. Repository detection
  is bounded and covers Cargo, npm/pnpm/yarn/Bun, pytest/unittest, Maven, Gradle wrapper or system
  Gradle, Go, .NET, Make, CMake, Docker Compose, and declared package/Make CI and smoke scripts.
  Nested projects become module-test stages and directory traversal does not follow symlinks.
- Plans use the explicit syntax/static, focused, module, full-unit, integration, packaging, and
  production-smoke progression. Commands are explicit program-plus-argv actions with network
  disabled; each is durably proposed, judged, exactly authorized, and reverified by Claw before
  execution. Missing tools and undetected stages remain unavailable/not-detected evidence, never
  passing evidence.
- Validation output is classified into compilation, dependency, assertion, configuration,
  environment, compatibility, migration, network, timeout, resource, infrastructure, or unknown
  failures and routed to a bounded specialist repair prompt. The native agent permits three repair
  cycles, reruns only unresolved stages before the complete plan, and pauses with durable routing
  evidence when the budget is exhausted.
- Completion now requires a derived completion event plus every detected required stage passing,
  unless a blueprint explicitly accepts an unavailable required stage. A model's `complete` claim
  alone cannot complete an implementation session.
- A real integration test starts with a failing Make check, observes the failure, routes a model
  repair, requires durable human approval for the write, reruns the affected stage, runs final
  validation, and only then completes. Nine detector/runner tests and 50 agent tests pass, including
  external-symlink rejection and .NET/unittest/custom-CI detection. Platform-specific tools not
  installed on this host are covered by detection tests and are not represented as live passes.

## v0.8 PR5 — Environment provisioning (in progress)

- The environment runtime performs bounded, read-only project detection for Node package managers,
  Maven/Gradle/JDK, Python/uv, Rust, Go, .NET, Docker, and Git. It rejects symlinked or oversized
  manifests rather than following untrusted repository content outside the workspace.
- Host inspection records the real OS, architecture, distribution, shell, package manager,
  elevation/container availability, memory, and disk evidence. Tool discovery prefers repository
  wrappers and managed roots before PATH tools, executes only explicit argv probes in a scrubbed
  environment, applies a five-second timeout, and fails closed when a version cannot be observed.
- `purrcode doctor --repository PATH`, authenticated `POST /v1/environment/inspect`, and Studio's
  explicit Environment surface return one evidence-bearing plan with detected, missing, install,
  and verification records. A local run against this repository observed Git 2.39.3 and Rust
  1.97.1, independently re-probed both, and reported ready from real exit-zero evidence.
- Twelve environment tests cover manifest/version inference, missing requirements, real process
  evidence, and external-symlink rejection; a daemon HTTP test verifies the authenticated surface.
- Checksum-verified managed downloads, atomic installation, repair execution through durable exact
  authorization, and Windows/Linux execution evidence remain pending. Missing tools produce an
  explicit plan and warning; they are never represented as installed or ready.

## v0.8 PR4 — Native PTY terminals (complete locally)

- `purrcode-terminal-runtime` now opens the platform-native backend supplied by `portable-pty`
  (Unix PTY and Windows ConPTY), always spawns an explicit program plus argv, uses absolute working
  directories, and rebuilds child environments from a small system allowlist. Credential-like
  environment keys are rejected and provider credentials are never inherited.
- Long-lived terminals support bounded transcript replay, attach/detach without termination,
  resize, inspect/list, timed wait, process-group termination with escalation, and one-shot command
  execution. Ownership transitions increment a generation and input must match it exactly, closing
  delayed-agent-input races after human takeover.
- The authenticated daemon exposes list/start/get/output/input/resize/attach/detach/owner/stop
  terminal routes. `GET /v1/terminals/{id}/output?since=` serves only the bytes produced after a
  caller's offset and reports when the ring buffer discarded output it never saw, so a live client
  appends instead of re-reading the transcript on a timer.
- Both clients emulate the terminal rather than stripping it: the Workbench renders a real screen
  buffer (`purrcode-tui::terminal`) with tabs, human takeover/return and direct keystroke input,
  and Studio renders the same semantics in `assets/term.js`. The browser retains only its HttpOnly
  Studio cookie; the daemon bearer token remains confined to the shell.
- Eleven runtime tests exercise real PTY commands, interactive input, replay, resize, detach,
  takeover rejection, secret-environment rejection, stop, and exit evidence. A real daemon HTTP
  test drives `/bin/cat`, proves stale generation conflict, observes PTY output, and stops it.
- Real-browser acceptance created an interactive login shell, observed WebSocket output, transferred
  ownership in both directions, confirmed selectable text and no page overflow, stopped the process,
  refreshed Studio, and recovered the complete exited-terminal transcript.
- Terminal records currently survive browser disconnect and Studio restart while the daemon remains
  alive. Durable recovery across daemon/VM restart belongs to the v0.9 Forever Runtime and is not
  represented as complete here. Windows ConPTY compilation/execution remains a cross-platform gate.

## v0.8 PR3 — Workbench (complete)

- Studio now renders a real three-pane Workbench: durable conversation and complete assistant
  output, semantic runtime activity, and a separately selected evidence inspector. Raw event JSON
  is never used as the activity presentation; it is shown only on explicit inspector selection.
- Run cards open durable sessions, and the Workbench loads session metadata, conversation messages,
  and complete events from the authenticated daemon. Follow-up messages use the existing daemon
  route and therefore retain secret detection, session leases, PawGate, and Claw boundaries.
- The browser attaches to the daemon SSE stream through the credential-confining shell proxy.
  Bounded partial assistant output remains visible while generating, durable audit events trigger
  refresh, EventSource reconnect is explicit in the UI, and the daemon bearer token never enters
  JavaScript.
- Diff Review uses the real isolated-worktree patch API and reports a missing worktree truthfully.
- Validation filters only recorded validation/outcome/completion events; absence is displayed as
  pending evidence, never success.
- A failed initial agent configuration is now appended durably as `SessionFailed` before the API
  returns its error. The UI refreshes the durable run list after such a failure instead of leaving
  an apparently active orphan session.
- Real-browser acceptance created a disposable durable run, opened Conversation/Activity/Inspector,
  selected and rendered an exact event payload, exercised Diff Review and Validation unavailable
  states, and proved the three panels collapse to one 700 px column without page overflow. Five
  Studio tests cover HTTP/authentication/SSE proxying and the embedded Workbench contract; the new
  daemon regression test proves initial configuration failure becomes terminal durable state.

## v0.8 PR2 — Studio shell (complete)

- `purrcode-studio-shell` serves a real responsive graphical application from a loopback-only
  Axum server. The dashboard shows daemon health, repository/HEAD/dirty state, durable runs, a
  one-goal run composer, the eleven PRD §10.1 product surfaces, and a visible human-authority
  summary. It uses only white/black canvases with system light/dark mode and a responsive mobile
  navigation layout.
- The browser never receives the daemon bearer credential. `purrcode ui` verifies the daemon and
  Studio API versions before binding, then exchanges a 256-bit one-time bootstrap link for an
  HttpOnly, SameSite=Strict session cookie. The shell consumes the bootstrap exactly once, rejects
  non-loopback binds, rejects cross-origin mutations, applies a restrictive CSP/security headers,
  and forwards only `/v1/*` to the authenticated daemon. PawGate/Claw and the existing daemon remain
  the only execution path.
- Bare `purrcode` launches the terminal Workbench on every platform (v0.9 PRD §3.1, §7.1). Display
  detection no longer rewrites the default interface. `purrcode studio [--remote URL] [--no-open]
  [--repository PATH]` launches the graphical client; `purrcode ui` is a backward-compatible alias,
  and `purrcode tui` is an explicit alias of the bare command. Browser opening uses explicit
  platform argument vectors, never a shell string. `--daemon-token` supports isolated daemon
  instances without changing the secure default token location.
- Daemon health now advertises `studio_api_version` from `purrcode-ui-contracts`; incompatible
  clients fail before the UI server is exposed.
- Three real-HTTP Studio tests prove cookie enforcement, one-time bootstrap consumption, daemon
  credential confinement, authenticated proxying, same-origin mutation enforcement, public-bind
  rejection, and compatibility failure. A real local daemon plus in-app browser acceptance proved
  bootstrap redirect, dashboard rendering, repository inspection, zero sessions/model requests at
  startup, Workbench navigation, and a 700 px layout with no page overflow.
- `cargo fmt --check`, `cargo clippy --workspace --all-targets -- -D warnings`, and
  `cargo test --workspace --no-fail-fast` pass. The existing live Ollama and disposable macOS
  Keychain tests remain explicitly ignored external checks; they were not represented as passing.

## v0.8 PR1 — UI and runtime contracts (complete)

PRD §24 PR1 pins the shapes of the v0.8 UI↔daemon boundary, the workspace/run
lifecycle, terminal actions, environment provisioning, human authority, and
automatic model selection as six dependency-light contract crates. They carry no
I/O and no tokio dependency, so PR2–PR6 build stable targets against them.

### New crates

- `purrcode-workspace-contracts` — `Workspace` / `WorkspaceId` / `RunId` /
  `RunStatus` / `RepositoryReference` (Local | Remote) / `EnvironmentProfileId`
  / `TerminalId` / `GrantId` per PRD §11.2. Owns the shared newtype ids that the
  sibling crates re-export. `WorkspaceStatus` includes `Disconnected` which is
  *live* so builds and tests survive client disconnect (PRD §11.3). 7 unit tests.
- `purrcode-terminal-runtime` — `TerminalAction` enum (ExecuteCommand /
  StartTerminal / SendInput / ResizeTerminal / InspectProcess / WaitForProcess /
  StopProcess / AttachTerminal / DetachTerminal) with concrete action structs,
  `TerminalOwner` (Human | Agent | Shared), `OwnershipGeneration` for stale-
  input rejection (PRD §12.1), `ManagedProcessSpec`/`ReadinessProbe`/
  `HealthProbe`/`RestartPolicy` (§12.2), and `TerminalSnapshot` for reconnect.
  Pure contracts; the PTY backend lands in PR4. 7 unit tests.
- `purrcode-environment-runtime` — `EnvironmentPlan` (PRD §9.2) with
  required/detected/missing tools, `ProvisionAction`, `EnvironmentCheck`
  verification actions, `ToolKind`, `ToolOrigin` with §9.3 preference ranking,
  `InstallStrategy` and the exact `INSTALL_PREFERENCE_ORDER`,
  `HostEnvironment`/`OsFamily`. `compute_missing`/`satisfies`/`version_at_least`
  fail closed on an empty observed version. 9 unit tests.
- `purrcode-authority-contracts` — `HumanAuthorityMode` (Governed/Elevated/
  Unrestricted, §15.1), `AutonomyGrant` (§15.2), `HumanSubject` with BLAKE3
  identity-claims digest, `CapabilitySet`, `PersistScope` (§15.3), `AgentId`,
  `AzureResourceScope`. The six PRD §15.5 model-restriction invariants are
  pure `assert_model_may_not_*` guards with no allow path: a model can never
  create, widen, re-scope, impersonate, escalate, or hide a grant. 9 unit tests.
- `purrcode-model-selection` — `ModelRole` (§7.2, `as_str()` canonicalizes the
  existing loose role strings), `ModelDeployment`, `QualificationReport`/
  `QualificationStatus` (Unverified is never Qualified), `ModelSelectionPolicy`
  with the §7.4 default, and a pure `select_models` that errors only when the
  policy is unsatisfiable (PRD §7.5), plus `selection_is_stale`. 8 unit tests.
- `purrcode-ui-contracts` — `StudioAction`/`StudioEvent` tagged enums (PRD
  §4/§10), `StudioScreen` registry of all eleven §10.1 screens,
  `STUDIO_API_VERSION = 1` with `is_compatible` exact-major-match gate, and
  `UiContractError`. 7 unit tests.

Total: 47 new unit tests; `cargo fmt --check`, `cargo clippy --workspace
--all-targets -- -D warnings`, and the six-crate test run are green.

## v0.7.0 evaluation runtime, adversarial suite, evidence bundles, and TUI foundation

[... existing v0.7 content truncated for brevity ...]

## v0.6.0 typed actions and deterministic state machine — release candidate

[... existing v0.6 content truncated for brevity ...]

## v0.5.2 provider-routing hotfix — implemented

[... existing v0.5.2 content truncated for brevity ...]

## v0.5.1 connection recovery — implemented

[... existing v0.5.1 content truncated for brevity ...]

## v0.5 usability recovery — Phases 1–6 complete

[... existing v0.5 content truncated for brevity ...]

## v0.4 product redesign — implemented, provider model qualification failed

[... existing v0.4 content truncated for brevity ...]
