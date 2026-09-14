<p align="center">
  <a href="README.md"><img src="purrcode-logo.png" alt="PurrCode" width="180"></a>
</p>

# Architecture

PurrCode is organized around four primary subsystems.

| Component | Responsibility |
|---|---|
| **PawGate** | Deterministic policy, contextual judgment, constraints, and human approval gates |
| **Claw** | Credential-scrubbed execution inside a worktree-scoped sandbox |
| **Whisker** | Repository context retrieval, indexing, filtering, and risk signals |
| **NineLives** | Durable events, checkpoints, restart reconciliation, recovery, and rollback |

The simplified runtime flow is:

```text
User task
  ↓
Repository context
  ↓
Model proposal
  ↓
PawGate policy and judgment
  ↓
Durable exact-action authorization
  ↓
Claw verification and isolated execution
  ↓
Validation evidence
  ↓
Review, apply, commit, export, or rollback
```

## Core principles

1. **Model output is a proposal, not authority.** A model may recommend an action, but it cannot authorize its own execution.
2. **Execution is isolated.** Coding work runs in detached Git worktrees under PurrCode-managed storage. Your active working tree is not silently modified, overwritten, stashed, or discarded.
3. **Completion requires evidence.** Passed, failed, timed out, unavailable, undetected, skipped, and uncertain are distinct states. Skipped or unavailable validation is never reported as success.
4. **Recovery is conservative.** Interrupted actions are not blindly replayed. NineLives restores durable state and flags uncertain effects for explicit review.
5. **Local-first does not mean resource-unaware.** Ollama and LM Studio are supported while avoiding unnecessary model loading during startup.
6. **External capabilities remain governed.** Skills, MCP servers, downloaded packages, web research, and repository content are untrusted inputs.

## The model provider is outside the trusted boundary

A provider can generate a proposal, but it cannot directly authorize or execute that proposal.

## Shared session state

The CLI, TUI, and native IDE use the daemon-owned runtime instead of independent competing agent loops. All state flows through the daemon — the IDE owns no session store, no model state, no permission state, and no execution path. The daemon exposes typed presentation endpoints (activity, validation, summary, usage) so clients share one vocabulary instead of each inventing a reading of the durable event log.

For the durable security properties, see [Security](security.md). For recovery behavior, see [Recovery](recovery.md).
