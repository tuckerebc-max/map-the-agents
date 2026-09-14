# gerome-elassaad/codingit

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b21eff408c44 @ 0a9071aac76f43b8

## Summary (orientation draft, not independently verified)

CodingIT is a Next.js 14 AI code-generation app that executes AI-generated code in E2B sandboxes, supports multiple LLM providers and sandbox personas, and adds S3-backed chat persistence, Stripe subscription billing with tiered usage limits, and security hardening per its README and CHANGELOG. Evidence coverage: 152 of 241 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The app is built on Next.js 14 (App Router, Server Actions) with shadcn/ui, TailwindCSS, and the Vercel AI SDK, and streams output in the UI. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43)
  - [observation/documented] AI-generated code is executed via the E2B SDK (code-interpreter), which the README describes as executing such code securely. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43)
- design-choices (2 claim(s)):
  - [observation/documented] The theme system was simplified to dark mode only; light theme support and the theme toggle were removed. -- evidence: [CHANGELOG.md#L275-L276](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L275-L276), [CHANGELOG.md#L238-L243](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L238-L243)
  - [observation/documented] Security hardening includes SSRF prevention with domain allowlisting for PyPI/npm requests, input validation, rate limiting, and a centralized lib/security.ts module. -- evidence: [CHANGELOG.md#L246-L251](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L246-L251), [CHANGELOG.md#L220-L225](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L220-L225)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: setup requires cloning the repo, running npm i, creating .env.local with E2B and LLM provider API keys, then npm run dev or npm run build. -- evidence: [README.md#L77-L77](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L77-L77), [README.md#L135-L137](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L135-L137), [README.md#L58-L61](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L58-L61), [README.md#L67-L69](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L67-L69), [README.md#L73-L73](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L73-L73), [README.md#L141-L143](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L141-L143)
  - [observation/documented] Repository development practice: custom personas are added by creating a sandbox-templates folder, building an E2B template via the E2B CLI, and registering it in lib/templates.json. -- evidence: [README.md#L182-L182](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L182-L182), [README.md#L216-L216](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L216-L216), [README.md#L184-L186](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L184-L186), [README.md#L153-L153](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L153-L153), [README.md#L194-L194](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L194-L194), [README.md#L151-L151](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L151-L151)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships several sandbox personas/stacks, including Python data analyst, Next.js, Vue.js, Streamlit, Gradio, and CodinIT Engineer. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43)
  - [observation/documented] Chat session REST endpoints cover listing/creating sessions, per-session management, messages, cross-history search, analytics, and JSON/CSV export. -- evidence: [CHANGELOG.md#L77-L80](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L77-L80), [CHANGELOG.md#L82-L86](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L82-L86)
- memory-state (1 claim(s)):
  - [observation/documented] Chat persistence stores sessions and messages in AWS S3 under a users/{userId}/sessions/{sessionId} layout with metadata.json and messages.json, plus aggregate analytics folders. -- evidence: [CHANGELOG.md#L62-L66](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L62-L66), [CHANGELOG.md#L118-L127](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L118-L127), [CHANGELOG.md#L68-L73](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L68-L73)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Usage limits are enforced per tier: GitHub imports 5/50/unlimited per month, storage 100MB/5GB/unlimited, and execution time 30s/300s/600s for Free/Pro/Enterprise. -- evidence: [CHANGELOG.md#L312-L317](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L312-L317)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](codingit.detail.md)

Metadata and full claim list: [full detail](codingit.detail.md)
Human notes ([notes](codingit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
