---
access: public
aliases: []
claim_ids:
- clm_456f413ca04a82c286606f0a4a47eceb2f130ae154f7da8f35e9a36f9e4b22a2
- clm_7881da5e2f26dfc648da0646b2f493c4f4bc5da1bf1ba971b44471413bb62c92
- clm_c99f30edad33a5e047615804d49935c65015a832f75453d7a4720d5fdb099983
- clm_f6b260120d0436848f1391d12ae14479baba2505bb47822879f2ee0512719db4
maturity: draft
page_id: pg_a806a06410da5110830ea13d6cd572d4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f1cd690361bb552196f8c904cf0aa135
title: talkcody/talkcody/docs/content/docs/en/open-source/architecture.mdx @ 5543bf926436
updated_at: '2026-09-14T03:17:52Z'
---

# talkcody/talkcody/docs/content/docs/en/open-source/architecture.mdx @ 5543bf926436

<!-- rcw:begin owner=source:src_f1cd690361bb552196f8c904cf0aa135 block=evidence -->
- All data, conversations, and code are stored locally on the user's machine, with local SQLite storage shown in the architecture diagram. [@claim:clm_456f413ca04a82c286606f0a4a47eceb2f130ae154f7da8f35e9a36f9e4b22a2]
- The Rust backend uses libSQL (SQLite-compatible embedded database with full-text and vector search) and tree-sitter for code navigation. [@claim:clm_7881da5e2f26dfc648da0646b2f493c4f4bc5da1bf1ba971b44471413bb62c92]
- Frontend stack includes React 19, TypeScript, Vite 7, Tailwind CSS 4, Shadcn UI, Zustand state management, Monaco Editor, and the Vercel AI SDK. [@claim:clm_c99f30edad33a5e047615804d49935c65015a832f75453d7a4720d5fdb099983]
- The product uses a two-tier architecture: a React 19 + TypeScript frontend and a Tauri 2 + Rust backend communicating over IPC. [@claim:clm_f6b260120d0436848f1391d12ae14479baba2505bb47822879f2ee0512719db4]
<!-- rcw:end owner=source:src_f1cd690361bb552196f8c904cf0aa135 block=evidence -->

## Researcher notes

