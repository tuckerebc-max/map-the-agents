# ADR-0001: Store LLM Prompts in Database Instead of Source Code

- **Status:** Accepted
- **Date:** 2026-04-02
- **Deciders:** Obfox

---

## Context

All LLM system prompts were hardcoded as Python string constants in `agents/prompts.py` and as inline strings in `services/flow_executor.py` and `api/routes/preferences.py`.

This meant that any prompt change — even a one-word tweak — required:
1. Editing source code
2. Code review
3. A full deployment

This created a high friction loop between prompt experimentation and production. Prompt engineering iteration was effectively gated behind the engineering deploy cycle.

---

## Decision

Move all static LLM prompts into a `prompts` MySQL table and load them at runtime via `PromptService`.

### Table schema

| Column | Type | Notes |
|---|---|---|
| `id` | INT PK | autoincrement |
| `slug` | VARCHAR(128) UNIQUE | machine key, e.g. `pm_system_prompt` |
| `name` | VARCHAR(255) | human-readable label |
| `category` | VARCHAR(64) | `agent` / `flow` / `api` |
| `content` | TEXT | the prompt body |
| `description` | TEXT | what the prompt does |
| `is_active` | BOOL | soft-disable without deletion |
| `version` | INT | incremented on edits |
| `created_at` | DATETIME | |
| `updated_at` | DATETIME | auto-updated |

### Slugs seeded in migration `0023_prompts_table`

| Slug | Category | Used in |
|---|---|---|
| `fetch_context_system_prompt` | agent | `CrewAIAgentRunner.fetch_context` |
| `pm_system_prompt` | agent | `CrewAIAgentRunner.run_product_manager` |
| `dev_system_prompt` | agent | `CrewAIAgentRunner.run_developer` |
| `ai_plan_system_prompt` | agent | `CrewAIAgentRunner.run_ai_plan` |
| `ai_code_system_prompt` | agent | `CrewAIAgentRunner.run_ai_code`, `run_developer` (direct mode) |
| `reviewer_system_prompt` | agent | `CrewAIAgentRunner.run_reviewer` |
| `finalize_system_prompt` | agent | `CrewAIAgentRunner.finalize` |
| `flow_product_review_system_prompt` | flow | `flow_executor._run_product_review_node` |
| `flow_agent_node_system_prompt` | flow | `flow_executor._run_agent_node` (template: `{role}`) |
| `flow_pr_review_system_prompt` | flow | `flow_executor._build_ai_lead_review_comment` |
| `repo_analysis_system_prompt` | api | `preferences.POST /repo-profile-scan` |

### Loading strategy

`PromptService.get(db, slug)` checks an in-process `dict` cache first. On a cache miss it queries the DB and fills the cache. The cache lives for the lifetime of the process — call `PromptService.invalidate(slug)` to bust it (e.g. after an admin edit API endpoint).

### Call chain for agent pipeline prompts

```
OrchestrationService._build_orchestrator(db)
  → AgentOrchestrator(db=self.db)
    → CrewAIAgentRunner(db=db)
      → PromptService.get(self.db, slug)
```

---

## Consequences

### Positive

- Prompts can be edited in the database without a code change or redeploy.
- Enables a future admin UI for prompt management.
- Prompt history/versioning can be tracked via `version` and `updated_at`.
- Single source of truth — no risk of the same prompt drifting across multiple constants.
- `is_active` flag allows disabling a prompt without deletion.

### Negative / Risks

- Every new deployment on a fresh database requires the migration `0023_prompts_table` to run before the app starts receiving traffic.
- A missing or inactive prompt slug raises a `ValueError` at call time (runtime failure, not startup failure).
- Cache is per-process — in multi-process deployments (multiple uvicorn workers), each process maintains its own cache. An edit must be followed by `PromptService.invalidate()` called in each worker, or a rolling restart.

---

## Next Steps

- Build an admin API (`GET /admin/prompts`, `PUT /admin/prompts/{slug}`) to view and edit prompt records
- Add `version` increment logic on content change (DB trigger or service layer)
-  Expose prompt editing in the frontend settings UI
