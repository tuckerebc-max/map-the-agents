# Monitor-owned compaction recovery

The ordinary session monitor now owns automatic compaction recovery
(`bd-xa7ry`). Closing the dashboard no longer stops recovery, and opening
multiple dashboards does not create additional prompt senders. The dashboard's
existing compaction checks are observation-only.

Use the existing configuration section:

```toml
[context_rotation.recovery]
enabled = true
cooldown_seconds = 30
max_recoveries_per_pane = 5
include_bead_context = true
prompt = "Reread AGENTS.md so it's still fresh in your mind. Use ultrathink."
```

This applies to sessions with an ordinary, running internal monitor. A dashboard
does not create that owner, and the dedicated account-rotation-only monitor does
not start unrelated recovery work. The recovery worker starts after the resident
lease's startup authorization, shares the existing ten-second timeline capture,
and is cancelled and joined before the monitor releases ownership. Optional
timeline-persistence failure does not disable otherwise enabled recovery.

## Detection and delivery

Detection looks for provider-specific completion banners, not broad prose about
context limits. The supported forms are Claude's `Conversation compacted` (or
its full continuation banner), Codex's `Context compacted`, and Gemini's
`Chat history compressed from N to N tokens.` Terminal message glyphs and ANSI
styling are normalized; fenced code, quoted prose, generic summaries, and
limit/reset errors do not by themselves authorize a recovery.

A pane's first capture only establishes a baseline. Subsequent captures must
align with retained output before a new banner is recorded. Identical captures,
scroll-off, and footer/spinner redraws do not repeatedly consume the same banner.
Unalignable captures and observation gaps establish a new baseline instead of
replaying old scrollback. A new monitor therefore does not recover an old banner
that was already visible when it started. Multiple new banners in one capture
coalesce into one pending reminder for the latest occurrence.

A new banner may be observed while the agent is working. The reminder waits for
fresh, confident idle evidence and the configured cooldown, for at most five
minutes. Immediately before delivery, the existing stable non-shell-process
check and a new canonical observation must confirm the same pane ID, shell PID,
agent type, and idle state. Dead, service, missing, duplicate, stale, failed, or
low-confidence pane evidence cannot authorize a send. Recovery targets the tmux
`%N` identity, not a pane index in whichever window is active.

Each attempt has a ten-second context budget. Optional Beads enrichment uses one
two-second triage query in the manifest's absolute project directory; unavailable
context falls back to the configured reminder. It does not claim work or change
assignment/reservation policy. Multiline delivery retains the shared agent-aware
tmux send mechanism. Sends are synchronous: a success receipt is recorded only
after delivery returns, and no fire-and-forget sender outlives monitor shutdown.

The cooldown and per-pane attempt budget are reserved immediately before sending.
A delivery failure may have partially written input, so it consumes that attempt
and is **not automatically retried** from the same banner. Inspect the pane before
manual recovery. Failures and completed deliveries are logged with session/pane
identity, without logging raw prompts or transcripts. Failures before delivery do
not consume an attempt. An agent that becomes busy during the final check retains
its pending reminder for a later idle observation.

## Boundaries

Terminal text is heuristic evidence, not an authenticated provider event. An
exact banner reproduced as unfenced output cannot always be distinguished from a
real banner. Conversely, unsupported banner formats or captures without overlap
may be missed; they are not guessed into automatic sends. The checks are not an
atomic lock against another sender or a process changing after the final read.

Detection history, pending reminders, and recovery counts are process-local.
This change does not add durable exactly-once delivery, remote monitor support,
provider quota handling, or an automatic retry of uncertain sends. The dashboard
retains local compaction observations; it does not mirror the monitor's recovery
history. Existing manual recovery APIs still use the shared delivery manager.

## Durable restart metadata during fleet changes

The session manifest also holds the per-agent command, model and account-profile
binding used by crash recovery. `ntm add` (including scale-up) writes each agent
through `UpsertAgentConfig`. Concurrent processes now serialize the complete
read/modify/write, not merely the final rename. Each updater reads the latest
manifest after taking ownership and preserves unrelated agents plus the session's
project, auto-restart policy, monitor generation and account-rotation settings.
A newly created manifest still leaves automatic restart disabled.

Save, per-agent update and delete use the same per-session mutation fence:
`<ManifestDir>/<session>.mutation.lock`, under the existing XDG data directory.
This is separate from the monitor's lifetime lease and from fleet-admission locks.
It works even when spawn count limits are disabled. An idle monitor does not block
manifest edits, and different sessions do not serialize behind one global mutex.
Readers remain lock-free and see complete versions through the existing atomic
writer; successful writes continue to synchronize the file and parent directory.

Lock acquisition waits at most five seconds; an unavailable or unsafe lock fails
the operation rather than writing unlocked. The shared Unix lock primitive rejects
symlinks, FIFOs, directories, hard links, foreign-owned files and group/world-accessible
files, and marks descriptors close-on-exec. A process exit releases ownership.
Delete removes the JSON manifest but keeps the lock inode, so later recreations
still rendezvous with existing waiters. Do not remove or replace live lock files.
These guarantees require cooperating Unix processes sharing a manifest directory;
unsupported platforms reject mutations instead of claiming process-shared locking.

Per-agent updates refuse malformed or null JSON, a manifest naming another session,
and duplicate records for the target pane without replacing the evidence. Failures
propagate through add's existing partial-mutation reporting: a launched pane may
still exist, and an error is not permission to blindly repeat the launch.

`SaveManifest` is intentionally a complete-snapshot replacement, not a merge or
compare-and-swap for snapshots read earlier. A caller explicitly saving an old
whole snapshot can still replace newer rows; individual-agent changes must use
`UpsertAgentConfig`. A delete ordered before a new upsert may be followed by a new
manifest. This fence does not establish tmux session identity or prevent manual
filesystem edits, and it does not change the process-local compaction reminder
history described above. File I/O after acquisition is synchronous; the five-second
budget bounds lock waiting, not a stalled filesystem's write or fsync.
