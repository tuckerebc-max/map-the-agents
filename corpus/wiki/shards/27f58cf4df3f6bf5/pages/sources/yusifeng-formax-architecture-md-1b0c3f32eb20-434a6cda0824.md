---
access: public
aliases: []
claim_ids:
- clm_a2b72fe6c9159f1cc7ca9e7411e9c792349829a39505fa5b21ecf28608fed28a
- clm_d1ae779c5821a002ca883b7805e586d448a0ce5b93da7590669ac9b1898de270
- clm_d7f55ec8a4496a4ea4b97386c4ea2e623b55cde5467fcddeac95f3fbb40b6e19
- clm_eda160accb8e372065199d6a12c3dd5e94a6018276819f4488040d0f9f712eaf
- clm_fdbed5c714abe7de13d4cd1926db43328a0c1cc8c568163fefc94aab7c1c6bc4
maturity: draft
page_id: pg_2f5d1884e760577f9f37434a6cda0824
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_38a480eaa5db5229af249c1ae39b4326
title: yusifeng/formax/ARCHITECTURE.md @ 1b0c3f32eb20
updated_at: '2026-09-14T03:26:09Z'
---

# yusifeng/formax/ARCHITECTURE.md @ 1b0c3f32eb20

<!-- rcw:begin owner=source:src_38a480eaa5db5229af249c1ae39b4326 block=evidence -->
- Permissions use a deny/ask/allow rule matcher, a policy engine with preflight enforcement before tool execution, and an approval service with user prompts and remember behavior. [@claim:clm_a2b72fe6c9159f1cc7ca9e7411e9c792349829a39505fa5b21ecf28608fed28a]
- Repository development practice: the project is built 100% with Codex, keeping `.codex/skills`, `docs/`, and `plans/` as traces of AI-assisted development, and semantic changes follow a contract-first change workflow. [@claim:clm_d1ae779c5821a002ca883b7805e586d448a0ce5b93da7590669ac9b1898de270]
- `formax app-server` provides a JSON-RPC backend over stdio for GUI/IDE clients, and `formax serve` starts only the WebSocket bridge for advanced debugging or split deployments. [@claim:clm_d7f55ec8a4496a4ea4b97386c4ea2e623b55cde5467fcddeac95f3fbb40b6e19]
- The architecture follows a single shared semantic core (packages/core semantics) consumed by three entry points — TUI, app-server, and Web — with renderers forbidden from forking semantic state. [@claim:clm_eda160accb8e372065199d6a12c3dd5e94a6018276819f4488040d0f9f712eaf]
- Architectural invariants include transcript truth from semantics projection, single-writer discipline, replay parity, `replaySeq` as ordering authority, and input lifecycle closure. [@claim:clm_fdbed5c714abe7de13d4cd1926db43328a0c1cc8c568163fefc94aab7c1c6bc4]
<!-- rcw:end owner=source:src_38a480eaa5db5229af249c1ae39b4326 block=evidence -->

## Researcher notes

