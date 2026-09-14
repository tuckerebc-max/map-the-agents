# Crush → zap Feature Backlog

Features observed in [charmbracelet/crush](https://github.com/charmbracelet/crush) worth pulling into zap.
Assessed against zap's existing capabilities (v0.15.67).

Source: live comparison done 2026-06-23.

---

## Priority 1 — High value, tractable

### 1. Background job control (`job_kill` / `job_output`)

**What crush does:** Shell commands can be backgrounded after a configurable timeout. The model gets a job ID and can poll output or kill the job via `job_kill`/`job_output` tools.

**Why it matters for zap:** Long-running shell commands (builds, test suites, dev servers) currently block the turn. The model has to wait or the user times out. Background jobs let the agent start a `cargo build`, move on, and check back.

**Implementation sketch:**
- Add `shell_background` tool that spawns a tokio task and returns a job ID
- Store active jobs in `Session` as `HashMap<JobId, JoinHandle + output_buf>`
- Add `job_output(id)` and `job_kill(id)` tools
- Surface active jobs in the sidebar

**Effort:** M (2–3 days)

---

### 2. `todos` tool — model-writable task list

**What crush does:** The `todos` tool lets the model read/write a structured TODO list persisted in the session DB. Used for autonomous task tracking mid-turn.

**Why it matters for zap:** `/goal` runs autonomously but has no shared state between turns beyond the message history. A model-writable todo list would make multi-step plans more reliable and visible to the user.

**Implementation sketch:**
- Add `todos` table to SQLite: `(session_id, id, text, done, created_at)`
- Add `todo_list`, `todo_add`, `todo_complete`, `todo_remove` tools
- Surface open todos in sidebar (replace or augment current context bar)

**Effort:** S (1 day)

---

### 3. Catwalk-style model registry (auto-synced provider/model list)

**What crush does:** `catwalk` is an open registry of provider → model listings. crush auto-fetches and caches this at startup so `/model` always shows current models without manual maintenance.

**Why zap has friction:** Static fallback lists in `provider_picker.rs` go stale. Users see old model names or miss new releases (e.g. `claude-opus-4-8` not showing until we bump the list).

**Implementation sketch:**
- Fetch `https://raw.githubusercontent.com/charmbracelet/catwalk/main/models.json` (or maintain a zap-hosted equivalent) at startup with a 24h cache in `~/.config/zap/model_cache.json`
- Merge live models with static fallback; mark cached entries with age
- No blocking: show cached list immediately, refresh async

**Effort:** S (1 day) — mostly JSON fetch + cache logic

---

### 4. Stats / usage dashboard

**What crush does:** `crush stats` generates an HTML file with SVG charts: tokens per day, cost per provider, model usage breakdown.

**Why it matters for zap:** Users running zap heavily (or comparing providers) have no visibility into token spend trends. The data is already in `agent.db`.

**Implementation sketch:**
- Query `sessions` + `messages` tables for per-day token/cost aggregates
- `/stats` command writes `~/.config/zap/stats.html` (or opens a TUI summary)
- Could also add a TUI `/cost` upgrade that shows 7-day sparkline in the sidebar

**Effort:** S (half-day for TUI summary, 2 days for HTML report)

---

### 5. AWS Bedrock provider

**What crush does:** First-class Bedrock client using the AWS SDK (sigv4 signing, region/profile config).

**Why it matters for zap:** Enterprise users in AWS-locked environments can't use direct Anthropic API. Bedrock gives Claude access without a direct Anthropic account.

**Implementation sketch:**
- Add `bedrock` slug to `provider_slug` detection
- Bedrock's `InvokeModelWithResponseStream` API is Anthropic-format under the hood — can reuse `AnthropicClient` with a sigv4 request interceptor
- Read `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` from env (standard AWS SDK conventions)

**Effort:** M (2 days — sigv4 signing + Bedrock endpoint mapping)

---

## Priority 2 — Medium value

### 6. Named agent definitions in config

**What crush does:** `crush.json` supports multiple named agents, each with its own `allowed_tools`, `allowed_mcp`, `context_paths`, and `model`. Switch agents with `crush --agent <name>`.

**Why it matters for zap:** Power users want a "secure" agent (no shell, read-only tools) for exploring untrusted repos, and a "full" agent for normal work. Currently there's only one profile controlled by permission mode.

**Implementation sketch:**
- Add `[agents.<name>]` TOML sections with `tool_profile`, `allowed_tools`, `context_paths`, `model`
- `zap --agent <name>` flag selects the agent at startup
- `/provider` picker shows current agent name in the header

**Effort:** M (2 days)

---


### 8. Google Vertex AI provider

**What crush does:** Uses `google.golang.org/genai` with Vertex AI credentials (Application Default Credentials or service account JSON).

**Why zap already has:** `gcloud` ADC for Gemini via the OpenAI-compat endpoint. But Vertex AI is a distinct endpoint with different auth requirements for enterprise GCP users.

**Implementation sketch:**
- Vertex AI Gemini endpoint is `https://{region}-aiplatform.googleapis.com/v1beta1/projects/{proj}/locations/{region}/endpoints/openapi/chat/completions` — OpenAI-compat
- Add `vertex` slug; read `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_REGION` from env
- Reuse existing gcloud ADC token fetch logic

**Effort:** S (1 day — mostly config wiring; auth already exists)

---

### 9. `download` tool

**What crush does:** Explicit `download(url, dest_path)` tool that saves a file to disk, distinct from `web_fetch` which returns content as text.

**Why it matters for zap:** `web_fetch` returns content in the context window. For binary files or large downloads the model needs to save to disk and reference the path. Common in data-science and asset-download tasks.

**Implementation sketch:**
- Add `download_file(url, dest_path)` tool using `reqwest` (already a dep)
- Respect sandbox `allowed_paths`
- Return `{bytes, mime, dest_path}` on success

**Effort:** XS (half-day)

---

### 10. Sourcegraph code search tool

**What crush does:** `sourcegraph(query)` tool that hits a configured Sourcegraph instance for cross-repo symbol search.

**Why it matters for zap:** Users at large companies with Sourcegraph can search across all company repos, not just the local checkout.

**Implementation sketch:**
- `sourcegraph_search(query, context_lines?)` tool
- Config key: `[providers.sourcegraph] base_url = "https://sourcegraph.example.com" token = "..."`
- Uses Sourcegraph GraphQL search API

**Effort:** S (1 day)

---

## Priority 3 — Lower priority / nice to have

### 11. Config JSON/TOML schema file (`zap schema`)

**What crush does:** `crush schema` writes a JSON Schema to `$XDG_CONFIG_HOME/crush/schema.json`, auto-included in `crush.json` via `$schema`. IDEs validate the config live.

**For zap:** Generate a TOML schema or a commented reference config at `zap schema`. Less critical given TOML's readability but would help with IDE integration.

**Effort:** S (1 day — schema is largely mechanical from the `Config` structs)

---

### 12. `crush projects` / project registry

**What crush does:** Maintains a registry of known project directories with per-project session history stats. `crush projects` lists them with last-used timestamp.

**For zap:** zap already scopes sessions by `cwd` in SQLite. A `/projects` command listing known cwds with session counts is a minor TUI addition.

**Effort:** XS (half-day)

---

## Won't pull

| Item | Reason |
|---|---|
| GitHub Copilot provider | `api.githubcopilot.com` is a private API — not open to third parties. The OAuth client_id must be whitelisted by GitHub; crush likely has a direct arrangement with GitHub that zap can't replicate. Borrowing VS Code's client_id would violate ToS. Revisit if GitHub opens a Copilot developer program. |
| Catwalk JSON config format | TOML is zap's format; JSON schema is the only upside, addressable separately (item 11) |
| Multi-agent `crush login` for each provider | zap's per-provider TOML already handles this; dedicated login flow adds complexity for marginal gain |
| `crush_info` / `crush_logs` tools | Internal to crush's architecture; zap has `/audit` and `zap_warn!` log |
| Docker MCP containers | MCP is low priority for zap overall; Docker adds a heavy dependency |

---

## Summary table

| # | Feature | Effort | Priority |
|---|---|---|---|
| 1 | Background job control | M | P1 |
| 2 | `todos` tool | S | P1 |
| 3 | Catwalk model registry | S | P1 |
| 4 | Stats / usage dashboard | S–M | P1 |
| 5 | AWS Bedrock provider | M | P1 |
| 6 | Named agent definitions | M | P2 |
| 7 | Google Vertex AI | S | P2 |
| 8 | `download` tool | XS | P2 |
| 9 | Sourcegraph tool | S | P2 |
| 11 | Config schema / `zap schema` | S | P3 |
| 12 | Project registry | XS | P3 |

Effort key: XS = half-day, S = 1 day, M = 2–3 days
