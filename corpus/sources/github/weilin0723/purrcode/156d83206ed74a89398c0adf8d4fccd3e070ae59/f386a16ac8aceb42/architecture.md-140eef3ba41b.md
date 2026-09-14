# PurrCode architecture

PurrCode is organized as four cooperating subsystems: **PawGate** owns judgment and authorization,
**Claw** owns controlled tool execution and sandboxing, **Whisker** owns repository context and risk
signals, and **NineLives** owns durable checkpoints, recovery, and rollback.

The first vertical slice deliberately keeps model providers outside the trusted decision path.

```text
ProposedAction
  -> deterministic Policy
  -> JudgmentDecision + constraints
  -> append-only SQLite authorization
  -> exact action/constraint digest verification
  -> atomic single-use authorization consumption
  -> shell-free process execution
  -> validation event
```

## Trust boundaries

- `runtime-core` owns serializable provider-independent domain types, including typed actions and
  the state machine reducer.
- `pawgate-runtime` is deterministic and has no model or network dependency.
- `ninelives-recovery` owns durable events and single-use authorizations.
- `claw-sandbox` must independently verify the authorization digest against the proposed action
  before spawning.
- `provider-gateway` defines model contracts but cannot authorize tools.
- `purrcode-cli` composes these crates; it is not itself a trust boundary.

The current process backend scrubs credentials and uses an explicit argument vector. macOS uses
`sandbox-exec` and Linux uses Bubblewrap when present; weaker host isolation is reported accurately
and is never described as a full sandbox. Read-command forms are typed so they cannot smuggle
mutating predicates past the policy layer.

## Typed actions

`purrcode-runtime-core::ProposedAction` is a strongly typed enum. The model-facing schema
(`purrcode-agent-runtime::AgentAction`) and the runtime-domain action are the same shape; the
agent emits typed fields, the runtime stores them, PawGate evaluates them, and Claw executes them.
There is no shell-string parsing in the trusted path.

```text
ProposedAction
  ├── Command(CommandAction)              // typed program + arguments + working directory
  ├── RepositoryRead(RepositoryReadAction) // bounded allowlisted reads (see below)
  ├── WriteFile(WriteFileAction)           // optimistic-concurrency digest
  ├── DeleteFile(DeleteFileAction)         // required exact-digest match
  └── ExternalTool(ExternalToolAction)     // MCP-only, always RequireApproval
```

### Repository read action

`RepositoryReadAction` is the privileged read class. Every variant is allowlisted, network-denied,
time-bounded, and confined to the session worktree. Claw deterministically maps each variant to a
safe shell invocation; the model never supplies shell syntax.

| Variant | Synthesized invocation |
|---|---|
| `GitStatus` | `git status --porcelain` |
| `GitRevParse { revision }` | `git rev-parse <revision>` |
| `GitLog { max_count, oneline }` | `git log [--oneline] [-N]` |
| `GitDiff { paths }` | `git diff -- <paths>` |
| `GitShow { revision, path }` | `git show <revision>:<path>` |
| `GitLsFiles { pathspec }` | `git ls-files <pathspec>` |
| `RepositoryGrep { pattern, paths, case_insensitive }` | `rg --no-heading --line-number [-i] -- <pattern> <paths>` |
| `Find { paths }` | `find <paths>` |
| `List { paths }` | `ls -la <paths>` |

`unsafe_repository_read` rejects `..` traversal, absolute paths, non-`Normal`/`CurDir` components,
and patterns that resolve outside the worktree. After validation, the policy returns
`AllowWithConstraints` with no network, no write globs, `maximum_changed_files = 0`, and the
configured `timeout_seconds` and `maximum_output_bytes`. Reads never require contextual judgment.

## State machine

`SessionState::reduce_event` is the authoritative transition function. `SessionState::apply` is a
deprecated wrapper retained for callers that have not yet migrated; it silently swallows invalid
transitions so callers must use `reduce_event` to enforce invariants.

`reduce_event` validates the transition before mutating state. Invalid transitions return one of:

- `DomainError::InvalidStateTransition` — the current `SessionStatus` forbids the requested change
  (e.g. accepting an approval after `Completed`).
- `DomainError::UnexpectedApproval` — an `ApprovalRecorded` or `ApprovalRejected` event referenced
  an `ActionId` that is not the currently pending approval.

Terminal statuses (`Completed`, `Cancelled`, `Failed`) only accept recovery events. `Uncertain`
transitions to `Active`, `Paused`, `AwaitingApproval`, `Executing`, or `AwaitingReview`. The full
transition table lives in `runtime_core::is_valid_transition`; tests cover the typed-read happy
path, terminal-state rejection, wrong-approval-id rejection, and approval for an unknown action.

`ExecutionStarted` is permitted without a prior `ActionProposed` so that partial sessions recovered
from disk remain replayable; the execution adapter independently re-verifies the authorization
record against the action's digest, so an orphan execution cannot reach the sandbox.

## Sandbox reality

`docs/security.md` is the authoritative statement. The repository architecture summary intentionally
says "credential-scrubbed execution inside a worktree-scoped OS sandbox when available; weaker
host isolation is reported accurately". Tests in `purrcode-claw` exercise the credential scrub,
process-group timeout, and exact-action digest recheck. Capability claims that are not backed by
an executed test in this workspace are marked as external gates in the implementation status.
