# lidge-jun/ima2-gen

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7fa7d426d928 @ ba2849709af842f3

## Summary (orientation draft, not independently verified)

ima2-gen is a local-first image/video generation runtime and studio with a Node CLI (bin/ima2.js), a local HTTP server, multiple provider lanes, packaged agent skills, and LAN token-based access control; the cited slices document its runtime interfaces, providers, configuration, and documented provider limits. Evidence coverage: 114 of 344 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 43 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Image generation supports multiple provider lanes: oauth (local Codex proxy), api (OpenAI Responses API), grok (xAI OAuth), grok-api (XAI_API_KEY), nai (NovelAI), agy (Antigravity CLI spawning Gemini image generation), and gemini-api. -- evidence: [docs/API.md#L61-L61](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L61-L61), [README.md#L171-L179](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L171-L179), [docs/API.md#L63-L73](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L63-L73)
- design-choices (2 claim(s)):
  - [observation/documented] CLI generation fails closed with NO_DEFAULT_MODEL until an explicit --model/--provider or a saved default is set, to prevent upgrades from silently switching providers or billing lanes. -- evidence: [README.md#L66-L66](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L66-L66)
  - [observation/documented] If port 3333 is busy the server binds the next available port and records the actual URL in ~/.ima2/server.json; CLI commands follow the advertised URL, overridable via --server or IMA2_SERVER. -- evidence: [README.md#L68-L68](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L68-L68), [README.md#L305-L305](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L305-L305)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install, npm run dev, npm run typecheck, npm test, and npm run build; npm run dev starts the TypeScript server with --watch and verbose diagnostics. -- evidence: [README.md#L441-L441](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L441-L441), [README.md#L431-L439](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L431-L439)
- skills-patterns (1 claim(s)):
  - [observation/documented] The package ships three Markdown agent skills (core, frontend, UI/UX) exposed via ima2 skill commands, with listing, JSON wrappers, reference modules, and installation to an agent's skill directory. -- evidence: [README.md#L145-L155](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L145-L155), [README.md#L135-L137](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L135-L137), [README.md#L139-L143](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L139-L143)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes a CLI (entry bin/ima2.js) with commands such as ima2 serve, setup, models, gen, video, edit, vectorize, multimode, skill, doctor, and stop. -- evidence: [README.md#L3-L12](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L3-L12), [README.md#L271-L281](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L271-L281), [README.md#L287-L303](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L287-L303)
  - [observation/documented] The local server exposes an HTTP API at localhost:3333, including /api/capabilities, /api/models, /api/auth/switch, /api/video/generate, and prompt-builder endpoints. -- evidence: [docs/API.md#L3-L3](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L3-L3), [docs/API.md#L7-L9](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L7-L9), [docs/API.md#L131-L134](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L131-L134), [README.md#L380-L381](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/README.md#L380-L381), [docs/API.md#L161-L164](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L161-L164), [docs/API.md#L75-L76](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L75-L76)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Loopback binds run single-user with no token; non-loopback binds require IMA2_LAN_TOKEN, protecting /api and /generated with in-memory, origin-bound sessions that expire after eight hours. -- evidence: [docs/API.md#L24-L32](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L24-L32), [docs/API.md#L13-L16](https://github.com/lidge-jun/ima2-gen/blob/7fa7d426d92813caeeff667a458b781237029df0/docs/API.md#L13-L16)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](ima2-gen.detail.md)

Metadata and full claim list: [full detail](ima2-gen.detail.md)
Human notes ([notes](ima2-gen.notes.md), never overwritten by build)

[Back to map index](../../index.md)
