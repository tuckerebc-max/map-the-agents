# sa4hnd/vibra-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0a8524a68899 @ 1b89e3adc0f154c1

## Summary (orientation draft, not independently verified)

Selected evidence records: Vibra Code is an open-source AI app builder: users describe mobile apps in plain English, a backend runs Claude Code inside an E2B cloud sandbox to generate apps, and a live preview appears on the phone. The architecture diagram shows three tiers: an Expo iOS app talking over an API to a Next.js + Convex server, which queues work via Inngest to an E2B sandbox running the AI agent.

## Source coverage

Source coverage (partial): 3 of 3 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vibra Code is an open-source AI app builder: users describe mobile apps in plain English, a backend runs Claude Code inside an E2B cloud sandbox to generate apps, and a live preview appears on the phone. -- evidence: [README.md#L70-L70](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L70-L70)
- components (2 claim(s)):
  - [observation/documented] The architecture diagram shows three tiers: an Expo iOS app talking over an API to a Next.js + Convex server, which queues work via Inngest to an E2B sandbox running the AI agent. -- evidence: [README.md#L132-L140](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L132-L140)
  - [observation/documented] The mobile app's core is a native iOS chat UI built with Texture (AsyncDisplayKit) and IGListKit, described as off-main-thread rendering targeting 60fps scrolling. -- evidence: [README.md#L100-L100](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L100-L100), [README.md#L258-L258](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L258-L258)
- design-choices (2 claim(s)):
  - [observation/documented] The product supports multiple AI providers — Claude (default), Cursor, and Gemini — switchable with a single environment variable. -- evidence: [README.md#L102-L102](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L102-L102)
  - [observation/documented] The project is licensed under AGPL-3.0 and is positioned as self-hostable with customizable AI prompts and swappable AI providers. -- evidence: [README.md#L24-L26](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L24-L26), [README.md#L346-L346](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L346-L346), [README.md#L72-L72](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L72-L72)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Users can describe apps by voice or attach mockup screenshots as input, and generated projects can be pushed directly to GitHub. -- evidence: [README.md#L113-L113](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L113-L113), [README.md#L111-L111](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L111-L111)
- interfaces (2 claim(s)):
  - [observation/documented] Chat messages from Convex are rendered as distinct node types: text with markdown, file reads (blue), edits (orange), bash commands (green), todo task cards, and a working-status indicator. -- evidence: [README.md#L310-L317](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L310-L317)
  - [observation/documented] The iOS client exposes modals for selecting the AI provider, browsing generated files, viewing live sandbox logs, publishing to GitHub, haptic settings, and editing environment variables. -- evidence: [README.md#L297-L304](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L297-L304)
- memory-state (1 claim(s)):
  - [observation/documented] Real-time synchronization is handled by Convex, with changes streaming from the sandbox to the phone instantly. -- evidence: [README.md#L106-L106](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L106-L106)
- orchestration (1 claim(s)):
More evidence: [full detail](vibra-code.detail.md)

Metadata and full claim list: [full detail](vibra-code.detail.md)
Human notes ([notes](vibra-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
