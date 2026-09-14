# Anthropic Thinking Effort Review Findings Log

## Status

- First final review ran with `codex review --uncommitted -c model="gpt-5.4" -c model_reasoning_effort="medium"`.
- Five P2 findings and one P3 finding were classified and fixed.
- The latest review raised one P1 finding that was classified as a contract conflict and was not implemented.

## Findings

### P2: Gate thinking-effort menu by provider capability

- Classification: true blocker.
- Reason: the accepted contract exposes `thinkingEffort` as Anthropic-scoped capability metadata, and showing a selectable effort control for non-Anthropic providers would create UI state that does not affect execution.
- Action: Web now parses runtime-defaults `profile.provider` plus `capabilities.thinkingEffort.provider`, passes a `thinkingEffortSupported` boolean through AppShell/TranscriptPane/ComposerDock, and hides effort choices when the active provider does not match the capability provider.
- Verification:
  - `npm --prefix packages/web-reference-react run test -- src/components/TranscriptPane.test.tsx src/app/ui/AppShell.test.tsx src/app/runtime/buildAppShellProps.test.ts src/app/core/rpcContracts.test.ts src/__tests__/app-composer.integration.test.tsx`
  - `npm --prefix packages/web-reference-react run type-check`
  - `bun run type-check`

### P2: Recompute thinking-effort availability when the active profile changes

- Classification: true blocker.
- Reason: startup-only provider gating can become stale when the active thread or effective runtime profile changes; the UI must reflect the profile that will execute future turns.
- Action: Web now stores the runtime-default provider and capability provider separately, hydrates per-thread effective provider from `thread/runtimeState/read`, updates it after `thread/runtimeState/patch`, and computes `thinkingEffortSupported` from the active thread provider with a global fallback.
- Verification:
  - `npm --prefix packages/web-reference-react run test -- src/components/TranscriptPane.test.tsx src/app/ui/AppShell.test.tsx src/app/runtime/buildAppShellProps.test.ts src/app/core/rpcContracts.test.ts src/__tests__/app-composer.integration.test.tsx`
  - `npm --prefix packages/web-reference-react run type-check`
  - `bun run type-check`

### P2: Keep `xhigh` out of non-Anthropic supported model metadata

- Classification: true blocker.
- Reason: `query.supportedModels()` metadata is provider-facing and must not advertise Anthropic-only `xhigh` for OpenAI reasoning models.
- Action: SDK model metadata now uses all five `ThinkingEffort` values only for Anthropic providers and keeps the existing four-value metadata for non-Anthropic reasoning providers.
- Verification:
  - `bun run test -- packages/core/src/sdk/query.test.ts packages/core/src/sdk/query.options-alignment.test.ts`
  - `bun run type-check`

### P3: Do not infer thread effort support from global provider before hydration

- Classification: true blocker despite P3 severity, because it is the same unsupported-control semantic cluster as the earlier provider-gating findings.
- Reason: while an active thread's effective provider is unknown, falling back to global provider can briefly expose Anthropic-only controls for a non-Anthropic thread.
- Action: active-thread effort support now stays disabled until that thread's effective provider has hydrated from `thread/runtimeState/read` or `thread/runtimeState/patch`; draft/no-thread surfaces still use the global runtime provider.
- Verification:
  - `npm --prefix packages/web-reference-react run test -- src/components/TranscriptPane.test.tsx src/app/ui/AppShell.test.tsx src/app/runtime/buildAppShellProps.test.ts src/app/core/rpcContracts.test.ts src/__tests__/app-composer.integration.test.tsx`
  - `bun run type-check`

### P2: Guard thread runtime hydration against stale read responses

- Classification: true blocker.
- Reason: a background `thread/runtimeState/read` response started before a user patch could overwrite the newer patch result in Web state.
- Action: Web now tracks a per-thread runtime hydration epoch. Starting a thread hydration read claims an epoch, and starting a thread preference patch bumps the epoch so older reads cannot apply stale preferences or provider metadata.
- Verification:
  - `npm --prefix packages/web-reference-react run test -- src/components/TranscriptPane.test.tsx src/app/ui/AppShell.test.tsx src/app/runtime/buildAppShellProps.test.ts src/app/core/rpcContracts.test.ts src/__tests__/app-composer.integration.test.tsx`
  - `npm --prefix packages/web-reference-react run type-check`
  - `bun run type-check`

### P2: Disable effort controls until runtime provider metadata hydrates

- Classification: true blocker in the provider-gating cluster.
- Reason: initial `null` provider/capability metadata must not optimistically expose Anthropic-only controls before runtime defaults or thread profile metadata have loaded.
- Action: Web now treats thinking effort as supported only when both the capability provider is known and the active provider matches it; tests were updated to supply provider metadata for Anthropic-capable mock runtimes.
- Verification:
  - `npm --prefix packages/web-reference-react run test -- src/components/TranscriptPane.test.tsx src/app/ui/AppShell.test.tsx src/app/runtime/buildAppShellProps.test.ts src/app/core/rpcContracts.test.ts src/__tests__/app-composer.integration.test.tsx`
  - `npm --prefix packages/web-reference-react run type-check`
  - `bun run type-check`

### P1: Preserve the previous thinking-token ceiling for Anthropic turns

- Classification: conflicts with accepted contract.
- Reason: this task intentionally moves supported Anthropic requests from manual extended thinking (`thinking: { type: 'enabled', budget_tokens: ... }`) to adaptive thinking plus `output_config.effort`; the accepted contract explicitly requires enabled payloads to no longer send `budget_tokens`.
- Action: not implemented. The durable preference remains `thinkingMode` plus `thinkingEffort`, and Anthropic request payloads remain `thinking: { type: 'adaptive' }` with `output_config.effort`.
- Supporting validation:
  - Anthropic adaptive-thinking guidance treats fixed thinking budgets as replaced by adaptive thinking and effort.
  - Stream payload tests assert no `budget_tokens` on enabled adaptive-effort requests.
