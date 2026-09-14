# agentlas-ai/agentlas-os -- full detail

[Back to orientation](agentlas-os.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agentlas-ai/agentlas-os/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/9dd257fdc1d230aa.json](../../../wiki/dossiers/agentlas-ai/agentlas-os/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/9dd257fdc1d230aa.json)

## specifications (3 claim(s))

- [observation/documented] The agent's mission is to route rough agent, team, or package requests to the right core builder and produce a portable Agentlas-compatible package. -- evidence: [agent.md#L5-L6](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L5-L6) (`clm_a692fdea4dd38903f37de5e42ef443834dcde85f71b13e14394778f048ecfa44`)
- [observation/documented] Inputs include a user goal plus optional target project path, repository, ZIP, prompt, existing agent, runtime requirements, and a public/private boundary. -- evidence: [agent.md#L10-L13](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L10-L13) (`clm_442dced50544ec622ef145569cd890b475db488f5e73e638f0da868f00303bfd`)
- [observation/documented] Outputs include a selected mode, a canonical AGENTS.md, .agentlas contract files, thin runtime adapters for Codex, Claude Code, Gemini CLI, and Cursor, a global command registry, and interview/research/eval artifacts. -- evidence: [agent.md#L27-L41](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L27-L41) (`clm_565971245ff9a52f6c3edf00baa303577f04f73907e3bcb6b6b51354d0d65c05`)

## components (1 claim(s))

- [observation/documented] Four core builders are defined: single-agent-builder, multi-agent-team-builder, agentlas-packager, and session-agent-builder, each with a distinct role such as converting exported sessions into reviewed reusable candidates. -- evidence: [ARCHITECTURE.md#L23-L34](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L23-L34), [agent.md#L17-L23](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L17-L23) (`clm_853994d3d623d71cfcd6c590acc385a91da44914187cfbe43bafd3eb277775d0`)

## design-choices (1 claim(s))

- [observation/documented] The canonical core is runtime-neutral, with adapters translating the same core into each runtime and adapters instructed not to contain private logic missing from the canonical core. -- evidence: [ARCHITECTURE.md#L186-L186](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L186-L186), [ARCHITECTURE.md#L38-L38](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L38-L38), [ARCHITECTURE.md#L197-L198](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L197-L198) (`clm_8ba789e4b0a265eff1258280f6a1a982b75ce1600c398ea38b9c7503fe567b2d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the packaging flow runs a Hephaestus security scan, adds .agentlas contracts, removes private or unsafe material, and verifies the package via scripts/verify-package.sh; CI contract gates such as scripts/verify-host-authority-contract.sh run in the cross-platform-wiring workflow. -- evidence: [ARCHITECTURE.md#L202-L216](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L202-L216), [ARCHITECTURE.md#L222-L230](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L222-L230), [CHANGELOG.md#L17-L27](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L17-L27) (`clm_cfc3a26b6f9e516661ba43fdb0e17ce767c366278c0f59e27815ba03f0a57497`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Runtime adapter surfaces include codex/marketplace.json, .claude/commands, GEMINI.md files, a root AGENTS.md for generic tools, and a bin/ontology CLI for local-first storage/search/graph/memory. -- evidence: [ARCHITECTURE.md#L188-L195](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L188-L195) (`clm_aeff2315f8bf0a924fca0e1220adbbc736bd641789ba8815dec3caa00c7f961f`)
- [observation/documented] The product exposes an MCP tool agentlas_resolve_plugins and a plugins tool-search command; tool search ranks servers before tools and loads input schemas only for the chosen tool. -- evidence: [CHANGELOG.md#L82-L97](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L82-L97), [CHANGELOG.md#L159-L170](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L159-L170) (`clm_de5741d5d37e64d5d547a81429f17b6f978f3a84e9c508e4aac1b4112ac7aeb5`)

## memory-state (1 claim(s))

- [observation/documented] Durable memory writes go through Memory Events and Memory Tickets, and generated packages may include memory-map, memory-tickets, and vault-reference files; recall counters and semantic index state serialize read-modify-writes. -- evidence: [ARCHITECTURE.md#L40-L105](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L40-L105), [agent.md#L45-L66](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L45-L66), [CHANGELOG.md#L49-L62](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L49-L62) (`clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The permissionPolicy schema accepts a host mode for network, shell, fileRead.mode, and mcp.mode, where the package declares no tool ceiling and the host runtime decides at execution time, emitting enforcement receipts. -- evidence: [CHANGELOG.md#L17-L27](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L17-L27) (`clm_4ef40794cd24585f5e7f8e15fce73a70bfba12458ba45877e6deb70dc3b270c8`)

## evaluation (1 claim(s))

- [observation/documented] Changelog entries report measured task performance: tool search placed the expected server in a four-candidate shortlist 5/5 times at ~209 tokens and ~3ms, and candidate menus put the right agent in the top four 97.4% of the time over 116 profiles and 389 queries. -- evidence: [CHANGELOG.md#L159-L170](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L159-L170), [CHANGELOG.md#L172-L179](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L172-L179) (`clm_e83f3e96d8a6e8e8464dac596c2780de6f70e737c3ebd47d09f878e0ca7c454d`)

## dependencies (1 claim(s))

- [observation/documented] The runtime vendors pure-Python jsonschema 4.17.3 (with attrs and pyrsistent) behind a loader that prefers a healthy installed copy, so schema validation works on Python 3.9 without the native rpds module. -- evidence: [CHANGELOG.md#L320-L340](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L320-L340) (`clm_12f6fa3da4ddb59b4552dbced47346bb0cc58a6450921cb613cde70d2875ea69`)

## limitations (1 claim(s))

- [observation/documented] The per-agent package ceiling is 10 MB transport and 2 MB per file (40 MB as authored), constrained by a 16 MiB MongoDB manifest record with base64 content. -- evidence: [CHANGELOG.md#L551-L577](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L551-L577) (`clm_1f10b98de5155d11144b69ac91238c3ae78e5cd5c5a0858464387a43671ac817`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

