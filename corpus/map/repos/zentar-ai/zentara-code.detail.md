# zentar-ai/zentara-code -- full detail

[Back to orientation](zentara-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zentar-ai/zentara-code/57038931fbae3b3d3d419c496af7b5bb02e75659/340c80d7850dd1e8.json](../../../wiki/dossiers/zentar-ai/zentara-code/57038931fbae3b3d3d419c496af7b5bb02e75659/340c80d7850dd1e8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The product exposes 25+ LSP tools for semantic code intelligence, including document symbols, workspace-wide semantic usages, call hierarchy, and targeted snippets. -- evidence: [README.md#L129-L135](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L129-L135), [README.md#L92-L96](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L92-L96) (`clm_7b382e8e1bdec6d5402aa132785429faab624fecc81549d93feefed9e2266828`)
- [observation/documented] A debugging tool suite of 35+ operations covers session management, execution control, breakpoint management, stack/source inspection, and state evaluation. -- evidence: [docs/Debugging.md#L58-L58](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L58-L58), [README.md#L112-L116](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L112-L116), [docs/Debugging.md#L97-L102](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L97-L102), [docs/Debugging.md#L67-L72](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L67-L72), [docs/Debugging.md#L76-L84](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L76-L84), [docs/Debugging.md#L88-L93](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L88-L93), [docs/Debugging.md#L62-L63](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L62-L63) (`clm_0433acbcca766d672753f97367c4d8cecbd4f29ae50909cac5bbf9e4db7ff8da`)
- [observation/documented] The /init slash command analyzes a codebase and generates AGENTS.md at the project root plus mode-specific files under .zentara/rules-*/, focusing on non-obvious project patterns. -- evidence: [docs/init-command-overview.md#L18-L18](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/init-command-overview.md#L18-L18), [docs/init-command-overview.md#L13-L13](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/init-command-overview.md#L13-L13), [README.md#L21-L21](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L21-L21), [docs/init-command-overview.md#L15-L16](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/init-command-overview.md#L15-L16), [docs/init-command-overview.md#L5-L5](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/init-command-overview.md#L5-L5) (`clm_8c083fb17025912a3eb0e21fb10f302ccf40210b82f1489eb8f515bbc4b09e21`)

## design-choices (1 claim(s))

- [observation/documented] Code understanding is LSP-first: the workflow moves from document symbols to usages, call hierarchy, and targeted snippets rather than text matching. -- evidence: [README.md#L149-L153](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L149-L153), [README.md#L83-L87](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L83-L87) (`clm_9b07ed4c91f2fefb38813660dc5f49003fcbae9ab4075d4da4a2eb7cc8068f6e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors build from source by cloning the repo, installing dependencies with pnpm, and running 'pnpm vsix' to compile TypeScript and package a .vsix into bin/. -- evidence: [README.md#L69-L69](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L69-L69), [README.md#L47-L47](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L47-L47), [README.md#L58-L63](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L58-L63), [README.md#L65-L67](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L65-L67) (`clm_f884f36b5fcfc0868775d5a96528d718689830afd139f55a030f772a97ad4f2e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Zentara Code is distributed as a VS Code extension, installable from the marketplace, and built for VS Code 1.96.4 and later. -- evidence: [README.md#L23-L23](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L23-L23), [README.md#L25-L29](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L25-L29), [README.md#L19-L19](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L19-L19) (`clm_15115c9702acfde23f8080158c219e20ad809419dc9b0ea645fa184e61b2ad59`)
- [observation/documented] Named debug operations include debug_launch, debug_quit, debug_continue, debug_step_in/out, debug_jump, debug_until, debug_set_breakpoint, debug_evaluate, and debug_execute_statement, among others. -- evidence: [docs/Debugging.md#L97-L102](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L97-L102), [docs/Debugging.md#L67-L72](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L67-L72), [docs/Debugging.md#L76-L84](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L76-L84), [docs/Debugging.md#L62-L63](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L62-L63) (`clm_15e4b0ea7626243d14df9ce1975b8f5ab287d9b32fed410ede935fb1f47b8b0f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Independent subagents run in parallel with isolated contexts, non-overlapping scope separation, opt-in write permissions (read-only by default), and per-agent timeouts. -- evidence: [README.md#L99-L103](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L99-L103), [README.md#L13-L15](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L13-L15), [README.md#L139-L143](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L139-L143) (`clm_288a878406ef189584834c5e3bef380c88480dbda58585a9d87298c277727271`)

## tools-permissions (1 claim(s))

- [observation/documented] Subagent writes are opt-in and constrained to allowed paths, with workers read-only by default; impactful actions like file writes and network access require explicit user approval. -- evidence: [README.md#L139-L143](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L139-L143), [README.md#L83-L87](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L83-L87) (`clm_0e4461bf63c389885ab13b17aa546fcc8fc969c3d7365c24f1a596b18d934be3`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Effective Python debugging requires a correctly configured Python interpreter in VS Code settings, and pytest must be installed for pytest-based debugging; TypeScript debugging needs npm and tsx. -- evidence: [README.md#L37-L42](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L37-L42), [README.md#L25-L29](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/README.md#L25-L29) (`clm_4fe280ae0ebad84e3e958285aeb43e55dc4e70afefe65d0ca63330aded856a3a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project is a fork of Roo-Code (per its own docs) and, per the license section, of ZentaraCodeInc/Zentara-Code, licensed under Apache 2.0. -- evidence: [docs/Debugging.md#L393-L393](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L393-L393), [docs/Debugging.md#L397-L397](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L397-L397), [docs/Debugging.md#L32-L32](https://github.com/Zentar-Ai/Zentara-Code/blob/57038931fbae3b3d3d419c496af7b5bb02e75659/docs/Debugging.md#L32-L32) (`clm_9482fa5d520c99814c5ef863b83b6bd98d3202377889b5156f084e3a25a1ad98`)

