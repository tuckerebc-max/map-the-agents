# ADR-0002: Add `extra_config` JSON Field to `integration_configs`

- **Status:** Accepted
- **Date:** 2026-04-08
- **Deciders:** Obfox

---

## Context

The `integration_configs` table stored provider credentials using a fixed set of columns:
`base_url`, `project`, `username`, `secret`.

This schema worked for providers whose auth surface is predictable (Azure: org URL + PAT, Jira: base URL + email + token, GitHub: base URL + owner + token). However, some integrations require additional fields that don't map cleanly to the existing columns. Rather than adding a new column for every new provider, a flexible overflow mechanism was needed.

The immediate driver was the HAL integration, which requires:
- `login_url` — the endpoint path used for token acquisition
- `chat_url` — the endpoint path used for AI chat calls

Neither fits naturally into `project` or any existing column.

---

## Decision

Add a nullable `extra_config` column of type `JSON` to `integration_configs`.

### Schema change

| Column | Type | Notes |
|---|---|---|
| `extra_config` | JSON, nullable | Arbitrary key-value map per provider |

Applied via migration `0028_integration_extra`.

### API surface changes

- `IntegrationConfigUpsertRequest` — new optional field `extra_config: dict | None`
- `IntegrationConfigResponse` — new field `extra_config: dict | None` (returned in all provider responses; `null` for providers that don't use it)
- `IntegrationConfigService.upsert_config()` — accepts and persists `extra_config`; on update, only overwrites if value is not `None`
- `IntegrationConfigService.to_public_dict()` — includes `extra_config` in output (not masked; does not contain secrets)

### Base URL handling for providers without a fixed URL

`IntegrationConfigService.OPTIONAL_BASE_URL_PROVIDERS = {'hal'}` — providers in this set are exempt from the `base_url` required validation. This avoids forcing an empty string workaround while still enforcing the constraint for all other providers.

---

## Consequences

### Positive

- New providers with non-standard config can be onboarded without a schema migration.
- Existing provider integrations are unaffected; `extra_config` is `null` for them.
- Frontend can read `extra_config` fields directly from the API response to pre-populate form fields.

### Negative / Risks

- `extra_config` is untyped at the DB level — no validation of its shape beyond "is valid JSON".
- Keys inside `extra_config` are not indexed; lookups inside the JSON require application-level parsing.
- `extra_config` must not store secrets — it is returned to the client without masking. Secrets must continue to use the `secret` column.

---

## Alternatives Considered

**Per-provider columns** — adding `login_url`, `chat_url` etc. as dedicated columns. Rejected: causes schema churn for each new provider and adds nullable columns that are irrelevant to most rows.

**Separate `provider_settings` table** — a key-value child table keyed by `integration_config_id`. Rejected: overkill for the current volume; the JSON column achieves the same flexibility with simpler queries.
