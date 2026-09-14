# Marketing attribution and new-camel activation

camelAI uses an opaque `attribution_id` to connect a first visit on
`camelai.com` with a later authenticated product activation.

## Ownership

- `camelai.com` creates the ID and stores the immutable first-touch record in
  the shared `APP_KV` namespace.
- `camelai.dev` reads that record, associates a sanitized snapshot with the
  stable internal user ID, and records the user's first meaningful activation.
- The marketing warehouse exports the resulting records for page-level
  acquisition reporting.

Production sales and product workers intentionally share the same `APP_KV`
namespace.

## Durable records

| Key | Purpose |
|---|---|
| `marketing_attribution:{attributionId}` | Anonymous immutable first touch |
| `user_marketing_attribution:{userId}` | Immutable user-to-first-touch link |
| `new_camel_activation:{userId}` | First accepted-message activation |

User attribution and activation records contain opaque IDs and sanitized
marketing fields. They must not contain email addresses or message content.

## Event definition

`new_camel_activation` means:

> The first time an authenticated user submits a non-empty message through the
> product and the backend accepts it for processing.

Reaching `/chat`, completing onboarding, logging in, or merely focusing the
composer does not qualify.

The browser calls the authenticated activation endpoint only after the
`sendMessage` RPC returns `accepted`. `UserDO.claimNewCamelActivation` provides
the durable, cross-tab idempotency boundary. The resulting browser analytics
event uses `completion_basis = first_message_accepted`.

## Relevant implementation

- `src/lib/marketing-attribution.server.ts`
- `src/lib/marketing-attribution.client.ts`
- `src/routes/api/marketing-attribution.ts`
- `src/routes/api/marketing-attribution.activate.ts`
- `workers/main/src/identity/user-do.ts`
- `src/components/Chat.tsx`

Focused checks:

```bash
bun run test:run -- tests/marketing-attribution.test.ts tests/marketing-attribution-server.test.ts
bun run test:workers -- workers/main/tests/auth-do.test.ts
bun run typecheck
```
