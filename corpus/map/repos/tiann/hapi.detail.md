# tiann/hapi -- full detail

[Back to orientation](hapi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tiann/hapi/de6c9dee2032059b11fa3a4e23f5a805b28667b4/73f1d2d4ce7cd239.json](../../../wiki/dossiers/tiann/hapi/de6c9dee2032059b11fa3a4e23f5a805b28667b4/73f1d2d4ce7cd239.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The repository includes SwiftUI/UIKit and Kotlin Compose native clients offering chat, approvals, session creation, files, dictation, and push notifications, with a documented client protocol contract. -- evidence: [README.md#L53-L53](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L53-L53) (`clm_e2aa800e73da93d1f2bbf0763a8970b3e1279af2bb7299f0df078b35fc38d5d3`)
- [observation/documented] A workspace browser feature is opt-in via one or more `hapi runner start --workspace-root <path>` flags, allowing scoped file-tree browsing and session starts in allowed subdirectories. -- evidence: [README.md#L9-L16](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L9-L16) (`clm_e09f7fa66afb0e913115a56795f5958808d3298a9a79943f2c0cc936cf70e5c1`)

## design-choices (2 claim(s))

- [observation/documented] HAPI positions itself as a local-first alternative to Happy, wrapping the user's existing AI agent rather than replacing it, keeping the same terminal experience. -- evidence: [README.md#L5-L5](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L5-L5), [README.md#L9-L16](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L9-L16) (`clm_7c8f0dc080f0b5730216a9b8bee7511fe782c97ecff68892721ed228073d1753`)
- [observation/documented] The relay uses WireGuard plus TLS for end-to-end encryption, with data encrypted from the user's device to their machine; self-hosted options like Cloudflare Tunnel and Tailscale are documented. -- evidence: [README.md#L37-L37](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L37-L37), [README.md#L39-L39](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L39-L39) (`clm_dd39cf4d5b9324b3e266cc5904641b6b379bc2951c4d219f1d517f03e08ee514`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use Bun workspaces (cli, shared, hub, web, website, docs, relay) with TypeScript strict typing, and root scripts `bun typecheck` and `bun run test` cover CLI/Web Vitest and Hub/Shared/Relay Bun tests. -- evidence: [AGENTS.md#L31-L34](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/AGENTS.md#L31-L34), [AGENTS.md#L53-L56](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/AGENTS.md#L53-L56), [CONTRIBUTING.md#L68-L71](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L68-L71) (`clm_b35d425c9aa09593d3ccb40719ad001753f42b90106d93c6cfbe520273d0e7cb`)
- [observation/documented] Repository development practice: PRs must stay focused on a single concern, oversized 'mega PRs' are rejected, significant features require an issue discussion first, and AI-generated code must disclose the model used in the PR description. -- evidence: [CONTRIBUTING.md#L14-L14](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L14-L14), [CONTRIBUTING.md#L30-L34](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L30-L34), [CONTRIBUTING.md#L26-L26](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L26-L26), [CONTRIBUTING.md#L20-L20](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L20-L20) (`clm_9051264088e7623642fe366d273f4b48d52c82d2f6c11562bcb7321963cf978d`)

## skills-patterns (1 claim(s))

- [observation/documented] Shared Codex sessions let users work with Codex from terminal and phone simultaneously, requiring Codex 0.154.0 or newer. -- evidence: [README.md#L9-L16](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L9-L16) (`clm_b1ceb97a8839df933eaa2e9813f147d431c2a3f32e37db5e922738250ae98434`)

## interfaces (4 claim(s))

- [observation/documented] HAPI lets users run sessions of agents such as Claude Code, Codex, Cursor Agent, Grok Build, OpenCode, Kimi, Copilot, Antigravity, Pi, and DeepSeek Harness, controlled remotely via iOS/Android apps, Web/PWA, or a Telegram Mini App. -- evidence: [README.md#L3-L3](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L3-L3) (`clm_9bdcbe211c84c42942a1f6a9cb86971d33f564fbf9a983ae2d64c0c5d4fc8711`)
- [observation/documented] The CLI supports starting an agent directly with `hapi <agent> [options]` (e.g. `hapi claude`), and scripts must specify the agent explicitly; `hapi --help` lists commands and supported agents. -- evidence: [README.md#L31-L33](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L31-L33) (`clm_414f7631e6713b6e127c4c177ce42ce772f96d6e0f9c68ed052f659428faf56f`)
- [observation/documented] Running `npx @twsxtd/hapi hub --relay` starts a hub with an E2E-encrypted relay, and `hapi server` remains supported as an alias for the hub command. -- evidence: [README.md#L24-L27](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L24-L27), [README.md#L29-L29](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L29-L29) (`clm_e558d7f83a46d596e6e8efbc5b20af221c95d2d6413a304bf040a1da84c4934f`)
- [observation/documented] The hub displays a URL and two QR codes for opening the web UI or pairing a native companion app. -- evidence: [README.md#L35-L35](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L35-L35) (`clm_5c83388b27e89bed3c1533bf498fb5ca502c4fb975f810dc990e674b496010e5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Bun 1.4.0, with `bun install` and `bun run build:single-exe` as the documented build steps. -- evidence: [README.md#L57-L57](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L57-L57), [README.md#L59-L62](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L59-L62) (`clm_5fa01145d448042d5b1e6d53cc05cd02db24926025b16bd674ca2405c0fb0666`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

