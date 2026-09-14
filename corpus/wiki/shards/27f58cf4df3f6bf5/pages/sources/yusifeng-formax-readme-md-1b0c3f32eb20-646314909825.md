---
access: public
aliases: []
claim_ids:
- clm_3a1f0e62659b41600126be7b4c6929462af4abbb92205d9f0971f3be959e20b4
- clm_62d4e197ca0260a7c7725bfc4927cb52562edbf2664c51a77b19df0e809d2cc7
- clm_78387d22ebf55ebcddfe5bde6533ae6cdf03ffa18bb081894f450f4ab705f7ce
- clm_7d3f3bbb38fb44ca01152792aea227f19d5d381c3b2a4b91aac84bdd0d7fff52
- clm_8531910071aaa72815c09764c3809ff19e50d1d3fd0c3b76400c8b0afa1f4100
- clm_a0074d620198de57396be460aaa841b5c8891ac4fe8d46cc4f7e05f1bf41f9bd
- clm_d1ae779c5821a002ca883b7805e586d448a0ce5b93da7590669ac9b1898de270
- clm_d7f55ec8a4496a4ea4b97386c4ea2e623b55cde5467fcddeac95f3fbb40b6e19
maturity: draft
page_id: pg_2c830f0481a1548f96cc646314909825
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c7490f2f0d6c5b8c8829b91434f558ee
title: yusifeng/formax/README.md @ 1b0c3f32eb20
updated_at: '2026-09-14T03:26:09Z'
---

# yusifeng/formax/README.md @ 1b0c3f32eb20

<!-- rcw:begin owner=source:src_c7490f2f0d6c5b8c8829b91434f558ee block=evidence -->
- Documented gaps: hooks support is incomplete, WebFetch/WebSearch have known stability and behavior gaps, MCP is not supported in this version, and the Web UI is minimal. [@claim:clm_3a1f0e62659b41600126be7b4c6929462af4abbb92205d9f0971f3be959e20b4]
- The CLI exposes commands including bare `formax` (REPL in a project directory), `formax setup`, `formax web`, `formax app-server`, and `formax serve`. [@claim:clm_62d4e197ca0260a7c7725bfc4927cb52562edbf2664c51a77b19df0e809d2cc7]
- Formax is an open-source implementation of a Claude Code-style AI assistant for software engineering tasks, offering both TUI and GUI workflows. [@claim:clm_78387d22ebf55ebcddfe5bde6533ae6cdf03ffa18bb081894f450f4ab705f7ce]
- The project is in Beta and is positioned as better suited for learning, experimentation, and architecture study than for stable production daily use. [@claim:clm_7d3f3bbb38fb44ca01152792aea227f19d5d381c3b2a4b91aac84bdd0d7fff52]
- Anthropic and OpenAI-compatible providers work in setup/runtime flows, while Gemini appears in config surfaces but is not fully supported in runtime execution yet. [@claim:clm_8531910071aaa72815c09764c3809ff19e50d1d3fd0c3b76400c8b0afa1f4100]
- The package is published to npm as `@yusifeng/formax` (installed via `npm i -g @yusifeng/formax@beta`) and requires Node.js >= 20 per the README badge. [@claim:clm_a0074d620198de57396be460aaa841b5c8891ac4fe8d46cc4f7e05f1bf41f9bd]
- Repository development practice: the project is built 100% with Codex, keeping `.codex/skills`, `docs/`, and `plans/` as traces of AI-assisted development, and semantic changes follow a contract-first change workflow. [@claim:clm_d1ae779c5821a002ca883b7805e586d448a0ce5b93da7590669ac9b1898de270]
- `formax app-server` provides a JSON-RPC backend over stdio for GUI/IDE clients, and `formax serve` starts only the WebSocket bridge for advanced debugging or split deployments. [@claim:clm_d7f55ec8a4496a4ea4b97386c4ea2e623b55cde5467fcddeac95f3fbb40b6e19]
<!-- rcw:end owner=source:src_c7490f2f0d6c5b8c8829b91434f558ee block=evidence -->

## Researcher notes

