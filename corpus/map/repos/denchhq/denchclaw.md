# denchhq/denchclaw

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f14eb4c23900 @ 3670cd3429a5893a

## Summary (orientation draft, not independently verified)

README and docs describe DenchClaw as an OpenClaw-based CRM framework installed via npx, running a separate gateway profile and web UI, with documented CLI commands, daemonless mode, device pairing, telemetry/privacy behavior, and release/development workflows.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The posthog-analytics OpenClaw plugin runs in-process with the gateway, hooks agent lifecycle events (e.g. before_model_resolve, before_tool_call, agent_end), and emits PostHog AI events; it is installed automatically during bootstrap when a PostHog project key is available. -- evidence: [TELEMETRY.md#L238-L256](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L238-L256), [TELEMETRY.md#L76-L78](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L76-L78)
- design-choices (3 claim(s)):
  - [observation/documented] Bootstrap creates a dedicated OpenClaw gateway under ~/.openclaw-dench on port 19001, separate from a usual ~/.openclaw gateway, with config in ~/.openclaw-dench/openclaw.json. -- evidence: [README.md#L33-L35](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L33-L35)
  - [observation/documented] Setting DENCHCLAW_DAEMONLESS=1 skips all gateway daemon management and launchd installation across commands, for Docker or environments without systemd/launchd; the gateway must then be run as a foreground process. -- evidence: [README.md#L72-L74](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L72-L74), [README.md#L76-L76](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L76-L76)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local development uses pnpm (pnpm install, pnpm build, pnpm dev, and pnpm web:dev for Web UI development). -- evidence: [README.md#L137-L140](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L137-L140), [README.md#L129-L130](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L129-L130), [README.md#L132-L133](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L132-L133)
  - [observation/documented] Repository development practice: releases are driven by package.json; pushing a version bump to main triggers .github/workflows/release.yml, which runs deploy.sh checks in validation mode before publishing to npm and creating a GitHub release, with reruns safe via existence checks. -- evidence: [RELEASING.md#L7-L12](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/RELEASING.md#L7-L12), [RELEASING.md#L3-L3](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/RELEASING.md#L3-L3), [RELEASING.md#L14-L14](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/RELEASING.md#L14-L14)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] DenchClaw provides an npm CLI with subcommands bootstrap, update, restart, start, and stop for onboarding and managing the web server. -- evidence: [README.md#L51-L56](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L51-L56)
  - [observation/documented] OpenClaw commands for DenchClaw must be prefixed with 'openclaw --profile dench', e.g. gateway restart or config set gateway.port 19001. -- evidence: [README.md#L62-L66](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L62-L66), [README.md#L59-L60](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L59-L60)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Gateway connections use device pairing: a 'pairing required' error means the local device awaits approval, and pending operator requests can be listed and approved via 'openclaw --profile dench devices list/approve'. -- evidence: [README.md#L106-L107](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L106-L107), [README.md#L96-L96](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L96-L96), [README.md#L100-L102](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L100-L102), [README.md#L104-L104](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/README.md#L104-L104)
- evaluation (1 claim(s)):
  - [observation/documented] PostHog Evaluations can score captured $ai_generation events using LLM-as-a-judge or deterministic Hog-based checks, storing pass/fail results with reasoning, configured entirely in the PostHog dashboard. -- evidence: [TELEMETRY.md#L129-L132](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L129-L132), [TELEMETRY.md#L134-L136](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L134-L136), [TELEMETRY.md#L126-L127](https://github.com/DenchHQ/DenchClaw/blob/f14eb4c239002d7b28673c60955b689b9d69db22/TELEMETRY.md#L126-L127)
- dependencies (1 claim(s)):
More evidence: [full detail](denchclaw.detail.md)

Metadata and full claim list: [full detail](denchclaw.detail.md)
Human notes ([notes](denchclaw.notes.md), never overwritten by build)

[Back to map index](../../index.md)
