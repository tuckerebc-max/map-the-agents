---
access: public
aliases: []
claim_ids:
- clm_4c65b4db85feb487fadaf1cf896b9e78c5694531131908bb1ee4bfa6eec7913f
- clm_6c09f7f3268f9571d5ef067bd4b16aa0b7d99a7dda9b97b0f7b95ea7a8bde254
- clm_7a4359e0ce5debf9d1744e4fa427e19066036f4b785f2750d248c7595fe1f42c
- clm_b09bc830f2a70cc6465620b593cf964c2e0fa59edf489ad8e23e7a38504202b2
- clm_b0e4cd46aefc75a2605ffd866daf5a42f1aa0da8abfd4652d0eddd991cae5599
maturity: draft
page_id: pg_f7917516603557c582f432e690ab82d6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_52a90da7cbd75fea9519d0578ce94f4e
title: dyad-sh/dyad/docs/architecture.md @ 0c8403662504
updated_at: '2026-09-14T01:47:29Z'
---

# dyad-sh/dyad/docs/architecture.md @ 0c8403662504

<!-- rcw:begin owner=source:src_52a90da7cbd75fea9519d0578ce94f4e block=evidence -->
- By default each LLM request includes the entire codebase plus a system prompt instructing XML-like responses; Smart Context uses smaller models to filter important files, and agentic iterative search is avoided mainly for cost reasons. [@claim:clm_4c65b4db85feb487fadaf1cf896b9e78c5694531131908bb1ee4bfa6eec7913f]
- Dyad historically simulated tool calling with custom XML-like tags instead of models' formal tool calling, citing the ability to batch many calls and evidence that JSON code output hurts quality; a newer agent architecture moves toward standard tool calling. [@claim:clm_6c09f7f3268f9571d5ef067bd4b16aa0b7d99a7dda9b97b0f7b95ea7a8bde254]
- The LLM responds with <dyad-*> tags (e.g. <dyad-write path=...>) that a specialized Markdown parser renders in the UI, and a response processor in the main process applies after user approval—writing or deleting files, adding NPM packages, etc. [@claim:clm_7a4359e0ce5debf9d1744e4fa427e19066036f4b785f2750d248c7595fe1f42c]
- Dyad is an Electron app with a React renderer process (sandboxed) and a privileged Node.js main process that accesses the filesystem, communicating via IPC. [@claim:clm_b09bc830f2a70cc6465620b593cf964c2e0fa59edf489ad8e23e7a38504202b2]
- Dyad deliberately keeps a simple agentic loop—usually a single AI request, with optional auto-fix of TypeScript compiler errors—to keep costs low compared to more agentic tools. [@claim:clm_b0e4cd46aefc75a2605ffd866daf5a42f1aa0da8abfd4652d0eddd991cae5599]
<!-- rcw:end owner=source:src_52a90da7cbd75fea9519d0578ce94f4e block=evidence -->

## Researcher notes

