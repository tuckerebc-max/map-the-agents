---
access: public
aliases: []
claim_ids:
- clm_0433acbcca766d672753f97367c4d8cecbd4f29ae50909cac5bbf9e4db7ff8da
- clm_0e4461bf63c389885ab13b17aa546fcc8fc969c3d7365c24f1a596b18d934be3
- clm_15115c9702acfde23f8080158c219e20ad809419dc9b0ea645fa184e61b2ad59
- clm_288a878406ef189584834c5e3bef380c88480dbda58585a9d87298c277727271
- clm_4fe280ae0ebad84e3e958285aeb43e55dc4e70afefe65d0ca63330aded856a3a
- clm_7b382e8e1bdec6d5402aa132785429faab624fecc81549d93feefed9e2266828
- clm_8c083fb17025912a3eb0e21fb10f302ccf40210b82f1489eb8f515bbc4b09e21
- clm_9b07ed4c91f2fefb38813660dc5f49003fcbae9ab4075d4da4a2eb7cc8068f6e
- clm_f884f36b5fcfc0868775d5a96528d718689830afd139f55a030f772a97ad4f2e
maturity: draft
page_id: pg_4077e7bda5f359968eaf047c208a0009
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3e4ec6c338e351fa90dd8f18ade587a7
title: Zentar-Ai/Zentara-Code/README.md @ 57038931fbae
updated_at: '2026-09-14T03:27:03Z'
---

# Zentar-Ai/Zentara-Code/README.md @ 57038931fbae

<!-- rcw:begin owner=source:src_3e4ec6c338e351fa90dd8f18ade587a7 block=evidence -->
- A debugging tool suite of 35+ operations covers session management, execution control, breakpoint management, stack/source inspection, and state evaluation. [@claim:clm_0433acbcca766d672753f97367c4d8cecbd4f29ae50909cac5bbf9e4db7ff8da]
- Subagent writes are opt-in and constrained to allowed paths, with workers read-only by default; impactful actions like file writes and network access require explicit user approval. [@claim:clm_0e4461bf63c389885ab13b17aa546fcc8fc969c3d7365c24f1a596b18d934be3]
- Zentara Code is distributed as a VS Code extension, installable from the marketplace, and built for VS Code 1.96.4 and later. [@claim:clm_15115c9702acfde23f8080158c219e20ad809419dc9b0ea645fa184e61b2ad59]
- Independent subagents run in parallel with isolated contexts, non-overlapping scope separation, opt-in write permissions (read-only by default), and per-agent timeouts. [@claim:clm_288a878406ef189584834c5e3bef380c88480dbda58585a9d87298c277727271]
- Effective Python debugging requires a correctly configured Python interpreter in VS Code settings, and pytest must be installed for pytest-based debugging; TypeScript debugging needs npm and tsx. [@claim:clm_4fe280ae0ebad84e3e958285aeb43e55dc4e70afefe65d0ca63330aded856a3a]
- The product exposes 25+ LSP tools for semantic code intelligence, including document symbols, workspace-wide semantic usages, call hierarchy, and targeted snippets. [@claim:clm_7b382e8e1bdec6d5402aa132785429faab624fecc81549d93feefed9e2266828]
- The /init slash command analyzes a codebase and generates AGENTS.md at the project root plus mode-specific files under .zentara/rules-*/, focusing on non-obvious project patterns. [@claim:clm_8c083fb17025912a3eb0e21fb10f302ccf40210b82f1489eb8f515bbc4b09e21]
- Code understanding is LSP-first: the workflow moves from document symbols to usages, call hierarchy, and targeted snippets rather than text matching. [@claim:clm_9b07ed4c91f2fefb38813660dc5f49003fcbae9ab4075d4da4a2eb7cc8068f6e]
- Repository development practice: contributors build from source by cloning the repo, installing dependencies with pnpm, and running 'pnpm vsix' to compile TypeScript and package a .vsix into bin/. [@claim:clm_f884f36b5fcfc0868775d5a96528d718689830afd139f55a030f772a97ad4f2e]
<!-- rcw:end owner=source:src_3e4ec6c338e351fa90dd8f18ade587a7 block=evidence -->

## Researcher notes

