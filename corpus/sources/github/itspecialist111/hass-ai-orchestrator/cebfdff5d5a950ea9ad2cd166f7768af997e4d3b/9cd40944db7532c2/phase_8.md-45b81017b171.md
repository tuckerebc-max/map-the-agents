# Phase 8 — "The Loop Closes"

> **Status:** in progress (D1–D3 landing in this branch).
> **Target version:** 0.11.0
> **Vision:** Phase 7 gave the orchestrator a brain. Phase 8 gives it
> **memory**, **a conscience**, and **a heartbeat** — turning a
> reactive reasoner into a genuinely autonomous, learning operator
> that you can trust to run with `dry_run_mode: false`.

---

## 1. Why these four milestones

Phase 7 closed the *capability* gap (the reasoner can think and act).
Phase 8 closes the *accountability* gap. Looking at the system today:

| Today | Problem |
|---|---|
| Each reasoning run is a cold start | No learning across runs |
| One-shot execution | No way to preview a plan before high-impact actions |
| Reactive only (chat / cadence) | Not actually autonomous |
| `/api/reasoning/run` returns one blob after N seconds | Bad UX for long runs |
| 14 MCP prompt workflows from OpenClaw sit unused | Free product surface |

Each milestone targets one of these.

---

## 2. Milestones

### Milestone D — Episodic memory & recall

The deep reasoner remembers what it did, what worked, and what the
human said about it.

| # | Task | Files |
|---|---|---|
| **D1** | `MemoryStore` typed wrapper around `RagManager.memory` for *reasoning episodes* (goal, answer, tools used, outcome, score, embedding) | new `memory_store.py` |
| **D2** | Pre-flight recall — `DeepReasoningAgent.run()` retrieves top-k similar past episodes (recency × score weighted) and injects them as a `## Relevant past experience` block in the system prompt | `agents/deep_reasoning_agent.py` |
| **D3** | Post-run persistence — every `HarnessResult` is summarised by a small LLM call to ~200 tokens and stored as an episode | `agents/deep_reasoning_agent.py`, `memory_store.py` |
| **D4** | Feedback API — `POST /api/reasoning/runs/{id}/feedback {rating, note}` updates the episode score | `main.py`, `memory_store.py` |
| **D5** | `GET /api/reasoning/memory?q=...` — search past episodes (powers the future memory browser UI) | `main.py` |

**Acceptance:** A reasoning run that solved "why is the lounge hot at
22:00" should, when asked again a week later, recall the prior
investigation and short-circuit (or at minimum cite the prior
finding).

---

### Milestone E — Plan → Approve → Execute (PAE)

High-stakes goals run dry-first, surface a full execution plan, wait
for human approval, then replay deterministically.

| # | Task | Files |
|---|---|---|
| **E1** | Add `mode: "plan" \| "execute" \| "auto"` to `POST /api/reasoning/run` (default `auto`) | `main.py`, `agents/deep_reasoning_agent.py` |
| **E2** | `DryRunInterceptor` wraps every mutating tool executor in `ToolRegistry`; returns synthetic success and records the intent. Read-only tools pass through. Classification driven by tool name patterns (`set_*`, `turn_*`, `lock`, `unlock`, etc.) plus an explicit `read_only_tools` set | `reasoning_harness.py` |
| **E3** | `PlanProposal {id, steps, risk_summary, requires_approval}` returned in plan mode and persisted to SQLite (extends `ApprovalQueue`) | `approval_queue.py`, `main.py` |
| **E4** | `POST /api/reasoning/plans/{id}/execute` replays the recorded calls deterministically — no LLM round-trip — matching exactly what the human approved | `main.py`, `agents/deep_reasoning_agent.py` |
| **E5** | `auto` mode = run plan, auto-execute if no high-impact actions, else queue | `agents/deep_reasoning_agent.py` |

**Acceptance:** With `dry_run_mode: false`, a goal like "lock all
external doors and arm the alarm" returns a plan, not a fait
accompli; user clicks Approve; the *recorded* lock/arm calls fire,
not an LLM-regenerated set.

---

### Milestone F — Proactive triggers

The reasoner fires on its own.

| # | Task | Files |
|---|---|---|
| **F1** | `TriggerRegistry` + `triggers.yaml` config — types: `cron`, `state_change`, `pattern` | new `triggers.py`, new `triggers.yaml` |
| **F2** | Cron triggers via `apscheduler` — e.g. nightly `energy_optimizer` audit at 22:00 | `triggers.py` |
| **F3** | State-change triggers — subscribe via `HAWebSocketClient.subscribe_entities`, match patterns, debounce, fire reasoner with templated goal | `triggers.py`, `ha_client.py` |
| **F4** | `/api/triggers` CRUD + minimal dashboard panel | `main.py`, new `dashboard/src/components/TriggerPanel.jsx` |
| **F5** | Trigger run history surfaces in existing decisions stream | `analytics.py` |

**Acceptance:** A trigger configured for `binary_sensor.front_door` =
`on` for >5min while `person.user` = `not_home` automatically fires
the reasoner with goal `"Investigate why the front door has been open
for 5+ minutes while no-one is home"`.

---

### Milestone G — Streaming + MCP prompts as workflows

Polish that finally makes the system feel modern.

| # | Task | Files |
|---|---|---|
| **G1** | `GET /api/reasoning/run/stream` (Server-Sent Events) — same payload as `/run` but emitted incrementally as `thought` / `tool_call` / `tool_result` / `final` events | `main.py`, `reasoning_harness.py` |
| **G2** | `GET /api/reasoning/prompts` — auto-discover external MCP prompts; dashboard renders them as one-click goal buttons (`Run security audit`, `Optimise routines`, etc.) | `main.py`, `external_mcp.py`, `dashboard/src/components/ReasoningPanel.jsx` |
| **G3** | Memory browser UI panel | new `dashboard/src/components/MemoryBrowser.jsx` |
| **G4** | Token & latency telemetry per run (`HarnessResult.tokens_in/out`, per-step latencies) when the backend exposes it | `reasoning_harness.py` |

---

## 3. Implementation order

D1 → D3 → D2 → D4 → D5 → E1 → E2 → E3 → E4 → E5 → G1 → G2 → F1–F5 → G3 → G4.

Reason: memory is the foundation (used by PAE for "did this kind of
plan work last time?" and by triggers for "have I already
investigated this?"). PAE is the safety net needed before turning on
triggers in a non-dry-run deployment. Streaming + MCP prompts are
quick wins that improve daily UX once the substance is in place.

---

## 4. Open design decisions (decide as we go)

* **Episode summariser model.** Default to the same backend the
  reasoner used (cheap on Ollama, costlier on Claude). Configurable.
* **Recall window.** Start with top-3 episodes within last 90 days,
  weighted `score × exp(-age_days / 30)`. Tune with telemetry.
* **Plan replay safety.** What if entity state has drifted between
  plan and execute? Re-validate each call against the current state
  immediately before executing; abort the replay on mismatch and
  surface to the human.
* **Trigger debouncing.** State triggers need cooldowns to avoid
  thrash; default 10 min per trigger.
* **Memory privacy.** Episodes contain user goals — they live in
  `/data/chroma` only, never sent off-device unless an Anthropic
  backend is in use (in which case they're included in the system
  prompt sent to Claude). Document this clearly.

---

*Phase 8 starting with the Milestone D vertical slice.*
