# Phase 7 — Deep Reasoning Harness & MCP Integration

> **Status:** implemented and unit-tested in v0.10.0 (April 2026).
> **Author:** GitHub Copilot (Claude Opus 4.7) working session.
> **Scope:** This document is the complete record of the architectural
> review, the changes shipped, and the plan going forward.

---

## 1. Executive summary

`HASS-AI-Orchestrator` (Phase 6, v0.9.47) is a working multi-agent
Home Assistant add-on, but its agents are **single-shot reasoners**:
each LLM call emits one batch of actions, and there is no way for an
agent to observe a tool result and decide what to do next. There is
also no real Model Context Protocol (MCP) integration — `mcp_server.py`
is a misnamed in-process tool registry — so the system has no path to
the rich entity / area / device / history surface that modern HA MCP
servers expose.

Phase 7 adds:

1. **A real MCP client** (`external_mcp.py`) that connects over
   Streamable HTTP to your separate
   [HASS_MCP_OpenClaw](https://github.com/ITSpecialist111/HASS_MCP_OpenClaw)
   add-on (76 tools, 11 resources, 14 prompts).
2. **A proper agentic harness** (`reasoning_harness.py`) — a recursive
   tool-use loop with provider-agnostic LLM backend, parallel tool
   execution, budget caps, and a transparent trace.
3. **A Deep Reasoning Agent** (`agents/deep_reasoning_agent.py`) — the
   "brain" — that runs on demand and combines the existing local
   safety-checked tools with the external MCP tools under one
   registry.
4. Two REST endpoints (`GET /api/reasoning/info`,
   `POST /api/reasoning/run`) so the dashboard and the orchestrator
   can drive it.

The fast deterministic specialists (heating / cooling / lighting /
security / universal) are **untouched** — they keep their fixed-cadence
loops as you wanted.

---

## 2. What we found in the existing codebase

### 2.1 Architecture (as of v0.9.47)

```
┌──────────── Home Assistant Add-on (host_network) ─────────────┐
│                                                                │
│  React dashboard (Vite) ─┐                                     │
│                          │                                     │
│  FastAPI :8999 ──────────┼── REST + /ws WebSocket              │
│   ├── IngressMiddleware  │                                     │
│   ├── /api/chat          │                                     │
│   ├── /api/agents        │                                     │
│   ├── /api/decisions     │                                     │
│   ├── /api/approvals     │                                     │
│   ├── /api/factory/*     │  (no-code agent factory)            │
│   └── /api/dashboard/*   │  (Gemini-generated visual)          │
│                                                                │
│  Singletons (globals):                                         │
│   ├── HAWebSocketClient   ── ws + reconnect loop               │
│   ├── MCPServer           ── 15 local tools, validation,       │
│   │                          dry-run, approval routing         │
│   ├── ApprovalQueue       ── SQLite, auto-approval rules       │
│   ├── RagManager          ── ChromaDB + nomic-embed-text       │
│   ├── KnowledgeBase       ── ingests HA registry + manuals     │
│   ├── Orchestrator        ── LangGraph plan loop               │
│   ├── ArchitectAgent      ── meta-agent (suggests new agents)  │
│   └── agents{}            ── UniversalAgent instances loaded   │
│                              from agents.yaml                  │
│                                                                │
│  Each UniversalAgent runs an independent decision loop:        │
│     gather_context → LLM (single shot) → parse JSON →          │
│     MCPServer.execute_tool(...) → log → sleep(interval)        │
└────────────────────────────────────────────────────────────────┘
       │                        │                  │
       ▼                        ▼                  ▼
   Home Assistant           Ollama             ChromaDB
   (ws + REST)              (local LLMs)       (vector DB)
```

### 2.2 The agent loop is single-shot

`base_agent.py` and `universal_agent.py` use the pattern:

```text
context = await gather_context()
decision = await llm.chat(prompt)        # one call, expects JSON
results  = await execute(decision.actions)
log + sleep
```

The model never sees a tool result. It cannot:

* Discover an entity it didn't know existed.
* Course-correct after a failed call.
* Combine multiple capabilities (e.g. *"check history, then if usage
  is rising, lower the setpoint"*).
* Ask follow-up questions.

This is **not** the modern agent pattern documented by Anthropic
("Building effective agents", Dec 2024 → still current as of April
2026 with the Claude Agent SDK). The modern pattern is a **loop with
environmental feedback** until the goal is met or budget is
exhausted.

### 2.3 "MCP" in this repo is not MCP

`mcp_server.py` is a local Python tool registry. It validates with
Pydantic, gates high-impact actions through `ApprovalQueue`, and calls
`HAWebSocketClient.call_service()`. That's all good — but it is **not**
the [Model Context Protocol](https://modelcontextprotocol.io). It does
not implement JSON-RPC, does not expose `tools/list` or `tools/call`,
and other AI clients (Claude Desktop, your OpenClaw add-on, etc.)
cannot talk to it.

The OpenClaw HASS_MCP add-on **is** a real MCP server. It runs at
`http://<ha-ip>:8080/mcp` over Streamable HTTP with bearer auth, and
exposes:

| Surface  | Count | Examples |
|----------|-------|----------|
| Tools    | 76    | `list_entities`, `search_entities`, `deep_search`, `get_areas`, `list_devices`, `get_history`, `get_logbook`, `render_template`, `conversation_process`, automation/scene/script CRUD, supervisor APIs |
| Resources| 11    | `hass://entities`, `hass://system`, `hass://devices`, `hass://areas/tree`, `hass://health` |
| Prompts  | 14    | `routine_optimizer`, `automation_health_check`, `energy_optimizer`, `security_audit`, `floor_plan_organizer` |

This is exactly the **discovery surface** the orchestrator's "brain"
needs.

### 2.4 Issues catalogued during the review

The review surfaced 18 distinct issues. Phase 7 addresses #1 (the
agentic loop) and #2 (real MCP). The rest remain open:

**Critical**

| # | File | Issue |
|---|---|---|
| 1 | `agents/*` | Single-shot agent loop, no environmental feedback. **Addressed by Phase 7 for the deep reasoner.** |
| 2 | `mcp_server.py` | Misnamed — local registry, not MCP. **Addressed by adding `external_mcp.py` alongside it.** |
| 3 | `main.py`, `factory_router.py`, `approvals` endpoints | **No auth.** Anyone on the LAN can chat, approve actions, or mutate `agents.yaml`. |
| 4 | `ha_client.py:50`, `main.py:471/518` | Bare `except:` swallows `KeyboardInterrupt` / `SystemExit`. |
| 5 | `mcp_server.py` | `call_ha_service` accepts arbitrary `domain.service`. Domain allow-listing is coarse. |

**Medium**

| # | File | Issue |
|---|---|---|
| 6 | `rag_manager.py` | `ollama.embeddings()` is sync; called on the event loop. |
| 7 | `factory_router.py` | PATCH agent hot reload is incomplete (variable scope bug, no in-memory swap). |
| 8 | `orchestrator.py` | `wait_for_agents()` has no timeout — a crashed specialist hangs the planner. |
| 9 | `universal_agent.py:311` | LLM JSON parsing falls back to empty actions on error, silently. |
| 10 | `knowledge_base.py:113` | MD5 used for delta detection — should be SHA-256. |

**Smells**

| # | File | Issue |
|---|---|---|
| 11 | many | `print(f"DEBUG: ...")` everywhere; should be `logger.debug`. |
| 12 | `analytics.py:147`, `main.py:533` | TODO placeholders (approval stats hardcoded). |
| 13 | `base_agent.py:112` | `think=False` Ollama option may be deprecated. |
| 14 | `requirements.txt` | `google-generativeai==0.8.3` is **end-of-life**; migrate to `google-genai`. |
| 15 | logging | Mixed `print` / `logger`; no structured logs. |
| 16 | `main.py` | Lazy-injection lambdas everywhere. Works but fragile. |
| 17 | none | No rate limiting on REST endpoints. |
| 18 | `orchestrator.py:81` | `task_ledger` grows forever (memory leak on long deployments). |

**Tests**

* `test_phase3_smoke.py` has wrong import path (`from backend.rag_manager` — should be `from rag_manager`). Pre-existing.
* 14 of the existing 53 tests fail under Python 3.14 / Pydantic v2 due to stale mocks. Pre-existing, **not caused by Phase 7**.

---

## 3. What we shipped (Phase 7)

### 3.1 New files

#### [`ai-orchestrator/backend/external_mcp.py`](ai-orchestrator/backend/external_mcp.py)

Real MCP client. Connects via `mcp.client.streamable_http.streamablehttp_client`
with `Authorization: Bearer <token>`. Discovers tools, resources,
prompts. Exposes:

* `connect()` / `aclose()` — lifecycle, never raises.
* `tools: dict[str, MCPToolSpec]` — discovered tools.
* `tool_schemas() -> list` — OpenAI/Ollama-compatible JSON schemas.
* `call_tool(name, arguments) -> {"ok", "text", "structured", ...}` — normalised result.
* `read_resource(uri)`.

Designed to **fail soft**: if the `mcp` package is not installed or
the server is unreachable, it returns an empty tool list and the
orchestrator keeps running.

#### [`ai-orchestrator/backend/reasoning_harness.py`](ai-orchestrator/backend/reasoning_harness.py)

The harness — a recursive tool-use loop:

```text
loop iteration in 1..max_iterations:
    response = await llm.chat(messages, tool_schemas)
    if response.tool_calls:
        results = await asyncio.gather(*[tools.call(c) for c in calls])
        append assistant turn + tool result messages
        emit trace events
    else:
        return final answer
return "max iterations reached"
```

Features:

* **Provider-agnostic** `LLMBackend` Protocol with two implementations:
    * `OllamaToolBackend` — Ollama 0.4+ native tool calling (use `qwen2.5:14b-instruct`, `llama3.1:8b-instruct`, `mistral-nemo`).
    * `AnthropicBackend` — Claude (default `claude-opus-4-7`) when `ANTHROPIC_API_KEY` is set.
* **Multi-provider tool registry** with collision-safe namespacing. External tools are prefixed (`hass_<name>`).
* **Parallel tool execution** with `asyncio.gather`.
* **Budget caps**: `max_iterations` (default 12) and `max_tool_calls_per_turn` (default 5).
* **Tracing**: every step records `thought`, `tool_calls`, `tool_results`, `duration_ms`. Events also stream to a callback (used to push to the dashboard).
* **Transparent**: returns a `HarnessResult` with `answer`, full `trace`, `iterations`, `tool_calls`, `stopped_reason`, `duration_ms`.

#### [`ai-orchestrator/backend/agents/deep_reasoning_agent.py`](ai-orchestrator/backend/agents/deep_reasoning_agent.py)

The "brain" agent. Goal-driven (not on a cadence).

* Wraps `ReasoningHarness` with a Home-Assistant-tuned system prompt
  (discovery-before-action, approval-aware, no inventing entity IDs).
* Combines **local** `MCPServer` tools (with safety + approval gating)
  and **external** `ExternalMCPClient` tools (with `hass_` prefix)
  into one `ToolRegistry`.
* Selects backend automatically: Anthropic if a key is set, otherwise
  Ollama.
* Exposes `info()` for the dashboard and `run(goal, context)` for
  invocation.

#### [`ai-orchestrator/backend/tests/test_reasoning_harness_smoke.py`](ai-orchestrator/backend/tests/test_reasoning_harness_smoke.py)

6 unit tests (all passing):

| Test | Verifies |
|---|---|
| `test_harness_returns_final_answer_without_tool_calls` | Final answer short-circuits the loop. |
| `test_harness_executes_tool_then_finalises` | Tool call → result → final answer flow, trace correctness. |
| `test_harness_runs_parallel_tool_calls` | Multiple tool calls in one turn execute concurrently. |
| `test_harness_respects_max_iterations` | Budget cap on iterations. |
| `test_harness_caps_tool_calls_per_turn` | Budget cap per turn. |
| `test_harness_emits_events` | Trace events fire to callback. |

### 3.2 Edited files

| File | Change |
|---|---|
| [`ai-orchestrator/backend/main.py`](ai-orchestrator/backend/main.py) | Read new options, init `ExternalMCPClient` + `DeepReasoningAgent` after the orchestrator, add `GET /api/reasoning/info` and `POST /api/reasoning/run`, clean shutdown of MCP session. |
| [`ai-orchestrator/config.json`](ai-orchestrator/config.json) | Bumped to `0.10.0`. New options: `mcp_server_url`, `mcp_server_token`, `deep_reasoning_model` (default `qwen2.5:14b-instruct`), `deep_reasoning_max_iterations` (default 12), `anthropic_api_key`, `anthropic_model` (default `claude-opus-4-7`). |
| [`ai-orchestrator/backend/requirements.txt`](ai-orchestrator/backend/requirements.txt) | `mcp>=1.0.0`, `anthropic>=0.40.0`. |

### 3.3 Resulting architecture

```
                                    /api/reasoning/run
                                    orchestrator escalation
                                    chat fallback (planned)
                                          │
                                          ▼
                              ┌───────────────────────┐
                              │  DeepReasoningAgent   │   <-- the "brain"
                              └──────────┬────────────┘
                                         │
                              ┌──────────▼────────────┐
                              │   ReasoningHarness    │
                              │   (loop: think →      │
                              │    parallel tools →   │
                              │    observe → repeat)  │
                              └────┬───────────┬──────┘
                  Ollama / Claude  │           │  ToolRegistry
                                   ▼           ▼
                        ┌───────────────┐  ┌────────────────────────────┐
                        │ Local MCPServer│  │ ExternalMCPClient          │
                        │ 15 safe tools  │  │ → OpenClaw HASS_MCP        │
                        │ + approval q   │  │   76 tools, 11 res, 14 pr  │
                        └───────────────┘  └────────────────────────────┘

Fast deterministic specialists (heating / cooling / lighting / security /
universal) keep their existing fixed-cadence single-shot loops and are
unchanged.
```

---

## 4. How to run it

### 4.1 Prerequisites

1. The OpenClaw HASS_MCP add-on installed and running on the same HA
   instance, with a long-lived access token configured.
2. Ollama reachable from the add-on with a tool-calling-capable model
   pulled:
   ```text
   ollama pull qwen2.5:14b-instruct
   ```
   (Or supply `anthropic_api_key` to use Claude Opus 4.7 instead.)
3. The add-on rebuilt — `requirements.txt` now includes `mcp` and
   `anthropic`.

### 4.2 Add-on options

```yaml
mcp_server_url: "http://homeassistant.local:8080/mcp"
mcp_server_token: "<your HA long-lived access token>"
deep_reasoning_model: "qwen2.5:14b-instruct"
deep_reasoning_max_iterations: 12
# Optional Claude backend (takes priority if set):
anthropic_api_key: ""
anthropic_model: "claude-opus-4-7"
```

### 4.3 Smoke test

```bash
# Tool surface
curl http://<addon>/api/reasoning/info

# Run a goal
curl -X POST http://<addon>/api/reasoning/run \
     -H 'Content-Type: application/json' \
     -d '{
           "goal": "Survey every climate entity, list which ones are above 22C, and propose a coordinated cool-down that respects the approval rules."
         }'
```

The response includes `answer`, `iterations`, `tool_calls`,
`stopped_reason`, `duration_ms`, and a `trace[]` of every thought,
tool call, and tool result.

### 4.4 Unit tests

```powershell
cd ai-orchestrator\backend
python -m pytest tests/test_reasoning_harness_smoke.py -v
# 6 passed
```

---

## 5. Plan going forward

The work is sequenced in three milestones. Each item lists the files
involved and the acceptance criteria.

### Milestone A — Wire the brain into the existing UX (1–2 sessions)

Goal: make Phase 7 visible and useful from the dashboard.

| # | Task | Files | Acceptance |
|---|---|---|---|
| A1 | Route ambiguous chat to the deep reasoner | `orchestrator.py`, `main.py` | If the orchestrator's classifier returns `complex`, hand the message to `deep_reasoner.run(...)` instead of doing a single LLM call. |
| A2 | Live reasoning trace in the dashboard | `dashboard/src/components/DecisionStream.jsx`, new `ReasoningTrace.jsx` | New WebSocket message type `reasoning_event` (already emitted) renders as a collapsible step list with thoughts, tool calls (name + args), tool results. |
| A3 | "Run a goal" UI | `dashboard/src/components/ChatAssistant.jsx` or new panel | Free-form goal input → calls `/api/reasoning/run`, streams trace, shows final answer. |
| A4 | Persist reasoning runs | `analytics.py` | Save each `HarnessResult` to `/data/decisions/deep_reasoner/<ts>.json` so they appear in `/api/decisions`. |

### Milestone B — Stability & safety hardening (1–2 sessions)

Goal: clear the critical / medium issues that block production trust.

| # | Task | Files | Acceptance |
|---|---|---|---|
| B1 | API auth | `main.py`, `factory_router.py` | Optional bearer token gate on all `/api/*` routes (`api_token` add-on option). HA Ingress requests already trusted. |
| B2 | Orchestrator agent timeout | `orchestrator.py` | `wait_for_agents()` wrapped in `asyncio.wait_for` with a configurable per-agent timeout. |
| B3 | Replace bare `except:` | `ha_client.py`, `main.py` | Catch specific exceptions; never swallow `BaseException`. |
| B4 | Async embeddings | `rag_manager.py` | Wrap `ollama.embeddings` in `run_in_executor`, or switch to `ollama.AsyncClient`. |
| B5 | Bounded `task_ledger` | `orchestrator.py` | Use `collections.deque(maxlen=…)` or a periodic prune. |
| B6 | Fix `factory_router.py` PATCH hot reload | `factory_router.py` | YAML write + in-memory `agents[id]` swap + entity rediscovery, with a regression test. |
| B7 | Tighten `call_ha_service` | `mcp_server.py` | Service-level allow-list (`domain.service` pairs) instead of domain-only. |
| B8 | Replace `print` debug noise with `logger.debug` | `main.py`, `ingress_middleware.py`, agents | One log handler, level driven by `log_level` option. |

### Milestone C — Modernisation & dependency hygiene (1 session)

| # | Task | Files | Acceptance |
|---|---|---|---|
| C1 | Migrate `google-generativeai` → `google-genai` | `orchestrator.py`, `requirements.txt` | New SDK works; old import removed. |
| C2 | Fix `test_phase3_smoke.py` import | `tests/test_phase3_smoke.py` | `from rag_manager import RagManager`. |
| C3 | Repair Pydantic-v2 / Python-3.14 mocks | `tests/test_api_smoke.py`, `test_agent_smoke.py`, `test_phase2_smoke.py`, `test_universal_agent_hass_integration.py` | All 53 pre-existing tests pass on Python 3.14. |
| C4 | Add live integration test for `external_mcp` | new `tests/test_external_mcp_live.py` (marked `integration`) | Optional test that hits a real OpenClaw add-on if `MCP_SERVER_URL` env var set. |

### Stretch (post-1.0)

* **Subagents.** Allow the deep reasoner to spawn focused child
  reasoners (e.g. an "energy audit" subagent) — mirrors the Claude
  Agent SDK's subagent pattern.
* **MCP prompts as workflows.** The OpenClaw add-on ships 14
  prompt templates (`routine_optimizer`, `energy_optimizer`,
  `security_audit`, etc.). Surface them in the dashboard as
  one-click "deep audits".
* **Evaluator-optimiser loop.** A second LLM critiques the deep
  reasoner's answer before it's returned (Anthropic's
  evaluator-optimiser pattern). Useful for security-audit-style
  goals where correctness matters.
* **HA Assist pipeline integration.** Expose the deep reasoner as a
  custom HA conversation agent so voice goes straight into the
  loop.
* **Memory.** Persist condensed run summaries to ChromaDB so the
  reasoner can recall prior decisions ("last week you turned this
  schedule off because…").
* **Plan / approve / execute mode.** Run the harness in a
  dry-run-only "plan" pass first, surface the planned tool calls in
  the dashboard, and only execute on user confirmation.

---

## 6. Reference — modern agentic patterns (2026 baseline)

The Phase 7 design follows the patterns Anthropic codified in
*Building effective agents* (Dec 2024) and operationalised in the
**Claude Agent SDK** (renamed from Claude Code SDK, current version
`v0.2.111+`, supports `claude-opus-4-7`):

* **Augmented LLM** = LLM + tools + retrieval + memory, run in a loop
  with environmental feedback.
* **Three core principles**: keep designs simple, keep planning
  visible, treat the agent-computer interface (tool docs, schemas,
  error shapes) as carefully as a human UI.
* **Workflows vs. agents**: deterministic specialists (your existing
  agents) handle predictable subtasks; an agent (the deep reasoner)
  handles open-ended goals where the steps can't be pre-coded.
* **Patterns used here**: orchestrator-workers (orchestrator → fast
  specialists), augmented-LLM-with-tools (the deep reasoner), and the
  observation loop (this is the harness).

OpenClaw / your HASS_MCP add-on provides the ACI (agent-computer
interface) for HA: 76 well-documented tools, lean entity responses,
template rendering, supervisor access. That ACI is what makes the
brain effective.

---

## 7. File map (Phase 7 only)

```
ai-orchestrator/
├── config.json                              # bumped to 0.10.0, new options
└── backend/
    ├── main.py                              # wires deep reasoner + endpoints
    ├── requirements.txt                     # +mcp, +anthropic
    ├── external_mcp.py                      # NEW — real MCP client
    ├── reasoning_harness.py                 # NEW — recursive loop
    ├── agents/
    │   └── deep_reasoning_agent.py          # NEW — the brain
    └── tests/
        └── test_reasoning_harness_smoke.py  # NEW — 6 passing tests
```

---

*End of Phase 7 documentation.*
