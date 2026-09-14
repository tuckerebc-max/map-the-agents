# Credential Proxy — Implementation Plan

**Feature**: #20 Credential Proxy Pattern  
**Status**: COMPLETE  
**Effort**: ~3-4 days  
**Commercial Value**: HIGH — API keys never touch agent code; enterprise security selling point  
**Date**: March 20, 2026

---

## Architecture Analysis

CodeBuddy has two LLM call paths that both flow through `getAPIKeyAndModel()` in `src/utils/utils.ts`:

1. **Agent path** — LangChain wrappers (`ChatAnthropic`, `ChatOpenAI`, etc.) in `src/agents/developer/agent.ts`
2. **WebView path** — Native SDKs (`Anthropic`, `OpenAI`, `Groq`, etc.) in `src/webview-providers/`

Every SDK accepts a `baseURL` override. This means we can **redirect all LLM traffic through a local proxy** that injects credentials transparently.

### Provider Landscape

| Provider | SDK | Auth Header | Base URL |
|----------|-----|-------------|----------|
| Anthropic | `@anthropic-ai/sdk` | `x-api-key` | `https://api.anthropic.com` |
| OpenAI | `openai` | `Authorization: Bearer` | `https://api.openai.com` |
| Groq | `groq-sdk` | `Authorization: Bearer` | `https://api.groq.com/openai/v1` |
| Deepseek | `openai` (compatible) | `Authorization: Bearer` | `https://api.deepseek.com` |
| Qwen | `openai` (compatible) | `Authorization: Bearer` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| GLM | `openai` (compatible) | `Authorization: Bearer` | `https://open.bigmodel.cn/api/paas/v4` |
| Grok | `openai` (compatible) | `Authorization: Bearer` | `https://api.x.ai/` |
| Local | `openai` (compatible) | `Authorization: Bearer` | `http://localhost:11434/v1` (configurable) |
| Gemini | `@google/generative-ai` | `x-goog-api-key` | Google SDK (no `baseURL` override) |
| Tavily | Custom HTTP | `Authorization: Bearer` | `https://api.tavily.com` |

---

## Day 1: `CredentialProxyService` Core

**File**: `src/services/credential-proxy.service.ts`

### 1.1 Local HTTP Server

- Singleton HTTP server on `127.0.0.1:<dynamic-port>` (port `0` for OS-assigned — avoids conflicts)
- Localhost-only binding — **never `0.0.0.0`**
- `vscode.Disposable` — clean server shutdown on deactivation
- Startup: after `SecretStorageService.initialize()`, before webview provider init

### 1.2 Provider Routing Table

Incoming request paths are mapped to real provider base URLs:

```
/anthropic/*  → https://api.anthropic.com/*
/openai/*     → https://api.openai.com/*
/groq/*       → https://api.groq.com/openai/*
/deepseek/*   → https://api.deepseek.com/*
/qwen/*       → https://dashscope-intl.aliyuncs.com/compatible-mode/*
/glm/*        → https://open.bigmodel.cn/api/paas/*
/grok/*       → https://api.x.ai/*
/local/*      → http://localhost:11434/* (passthrough, no credential injection)
```

### 1.3 Credential Injection

Per-provider header injection using `SecretStorageService.getApiKey()`:

| Provider | Header |
|----------|--------|
| OpenAI, Groq, Deepseek, Qwen, GLM, Grok, Local | `Authorization: Bearer <key>` |
| Anthropic | `x-api-key: <key>` + `anthropic-version: 2023-06-01` |

### 1.4 Security

- **Strip incoming auth headers** — ensure the client never sends real keys through
- **Keys sourced from OS keychain** via `SecretStorageService` — never from environment
- **No key in process memory beyond the proxy request lifecycle**

### 1.5 Streaming Support

- Pipe request/response bodies through with `node:http` to preserve SSE (`text/event-stream`) for streaming completions
- No response buffering — pure passthrough after header injection

---

## Day 2: Wire Into LLM Call Paths

### 2.1 Modify `getAPIKeyAndModel()` (`src/utils/utils.ts`)

When proxy is enabled:

```typescript
// Before (direct):
return { apiKey: "sk-real-key", model: "claude-sonnet-4-20250514", baseUrl: "https://api.anthropic.com" }

// After (proxied):
return { apiKey: "proxy-managed", model: "claude-sonnet-4-20250514", baseUrl: "http://127.0.0.1:54321/anthropic" }
```

- `apiKey` becomes `"proxy-managed"` (dummy token — proxy injects the real one)
- `baseUrl` becomes `http://127.0.0.1:<port>/<provider>`
- **No changes needed in `agent.ts` or webview providers** — they already consume `apiKey` and `baseUrl` from `getAPIKeyAndModel()`

### 2.2 Extension Startup (`src/extension.ts`)

```typescript
// After SecretStorageService.initialize(), before webview providers:
if (getConfigValue("codebuddy.credentialProxy.enabled")) {
  const proxy = CredentialProxyService.getInstance();
  await proxy.start(secretStorageService);
  context.subscriptions.push(proxy);
}
```

### 2.3 Gemini Special Case

Google's `@google/generative-ai` SDK uses an `apiKey` constructor param — it doesn't support `baseURL` override. Two options:

- **Option A** _(recommended)_: Gemini calls bypass proxy. Key is still in OS keychain via `SecretStorageService`, not in environment. Acceptable security posture.
- **Option B**: Rewrite Gemini calls to use Google's REST API through the proxy. High effort, fragile.

**Decision**: Option A — Gemini keeps direct key injection. Document in README that Gemini is the exception.

---

## Day 3: Rate Limiting + Audit Log

### 3.1 Rate Limiting (Per-Provider, In-Memory)

Token bucket algorithm per provider:

- Default: 60 requests/minute for paid APIs, 30 for free tiers
- Returns HTTP `429` with `Retry-After` header when exhausted
- Configurable via `codebuddy.credentialProxy.rateLimits`

```jsonc
{
  "codebuddy.credentialProxy.rateLimits": {
    "anthropic": 60,
    "openai": 60,
    "groq": 30,
    "deepseek": 60
  }
}
```

### 3.2 Audit Log

Ring buffer (last 1000 entries) in memory:

```typescript
interface ProxyAuditEntry {
  timestamp: number;
  provider: string;
  method: string;
  path: string;
  statusCode: number;
  latencyMs: number;
  tokenCount?: number;     // Extracted from response `usage` field (best-effort)
}
```

- `codebuddy.credentialProxyAudit` command — dumps log to output channel
- Token count extracted from response `usage` JSON field when present (no response buffering for streaming — only for non-streaming responses)

---

## Day 4: Tests + Doctor Integration

### 4.1 Tests (`src/test/suite/credential-proxy.service.test.ts`)

| Test | What It Validates |
|------|-------------------|
| Server lifecycle | Starts on dynamic port, stops cleanly on dispose |
| Provider routing | Requests to `/anthropic/v1/messages` reach Anthropic URL |
| Auth injection | Correct header set per provider (Bearer vs x-api-key) |
| Auth stripping | Client-sent `Authorization` headers are removed |
| Rate limiting | Returns 429 after bucket exhaustion |
| Unknown provider | Returns 404 for `/unknown/foo` |
| Audit log | Entries recorded with correct fields |
| Streaming passthrough | SSE responses are not buffered |

### 4.2 Doctor Check (`src/services/doctor-checks/credential-proxy.check.ts`)

| Condition | Severity | Message |
|-----------|----------|---------|
| Proxy enabled + running | info | "Credential proxy active on port XXXXX" |
| Proxy enabled + not running | critical | "Credential proxy is enabled but not running" |
| Proxy disabled | info | "Credential proxy is disabled — API keys are passed directly to SDKs" |
| API keys in env vars | warn | "Found LLM API keys in environment variables — consider enabling credential proxy" |

---

## Settings

```jsonc
{
  // Opt-in — no behavior change for existing users
  "codebuddy.credentialProxy.enabled": false,

  // Per-provider rate limits (requests per minute)
  "codebuddy.credentialProxy.rateLimits": {
    "anthropic": 60,
    "openai": 60,
    "groq": 30,
    "deepseek": 60,
    "qwen": 60,
    "glm": 60,
    "grok": 60
  }
}
```

---

## What Does NOT Change

| Component | Reason |
|-----------|--------|
| `SecretStorageService` | Still the source of truth for key storage |
| Provider SDKs | Same npm packages, just pointed at localhost |
| LangChain wrappers | Same instantiation, different `baseURL` |
| WebView providers | Same code, different `baseURL` |
| Gemini | Keeps direct key injection (SDK limitation) |
| `CostTrackingService` | Reads token usage from LLM responses — unaffected |
| `ProviderFailoverService` | Switches provider → `getAPIKeyAndModel()` returns new proxy route |

---

## Security Properties

| Property | How |
|----------|-----|
| Keys never leave proxy process | Same Node.js process as extension host |
| No network exposure | Bound to `127.0.0.1` only |
| No key leakage via tools | Incoming auth headers stripped before forwarding |
| Audit trail | All proxied calls logged with timestamp + provider |
| OS keychain storage | Keys sourced from `SecretStorageService` → OS keychain |
| Graceful degradation | If proxy fails to start, falls back to direct SDK calls |

---

## File Manifest

| File | Type | Description |
|------|------|-------------|
| `src/services/credential-proxy.service.ts` | NEW | Core proxy server + routing + credential injection |
| `src/services/doctor-checks/credential-proxy.check.ts` | NEW | Doctor health check for proxy status |
| `src/utils/utils.ts` | MODIFY | `getAPIKeyAndModel()` returns proxy URLs when enabled |
| `src/extension.ts` | MODIFY | Start proxy on activation, add to subscriptions |
| `package.json` | MODIFY | Add settings schema, audit command |
| `src/test/suite/credential-proxy.service.test.ts` | NEW | Service + routing + rate limiting tests |
