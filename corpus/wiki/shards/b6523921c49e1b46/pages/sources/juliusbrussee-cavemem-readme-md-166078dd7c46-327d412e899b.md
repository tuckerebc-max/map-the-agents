---
access: public
aliases: []
claim_ids:
- clm_18acbaf207d45397b5f47addc0e5747760c7e681967331a2aa39d8d00550abb7
- clm_2dc40f3f1621f08f7f134df1cf8eb2329213d80b85017dd08d9224d6d3095f15
- clm_351188e71d23d66b0f6244052fa9c8a7e615a26f9a71c7801bdce4688162ab51
- clm_3a40fa0208bb18e5513f35db0e9746a1e7c454a6c705c37c1d65d401f8d9120c
- clm_480027dceffab8387cd4e6f137c4e4000d2e01c942ca21d43dfd440fac4d33fb
- clm_5876598e81e58c868cf404f2baa200a4126ea147b0101e82383e4a359dcaa183
- clm_678ba0783d1b892060edc42a069e4f41b9b62d173e8bcbc803e80e3812eb98f6
- clm_709d3de502f98f815dd6192a06d792030c4c8233931a2f2d64d83755f34a14af
- clm_88e327d845e8cf0a9d80c8b1987b52295573e0bbd7f024ed555958ff70fda8a3
maturity: draft
page_id: pg_ebb523cd39cb571cb0e2327d412e899b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_963027d9569757669775d414e46e68a8
title: JuliusBrussee/cavemem/README.md @ 166078dd7c46
updated_at: '2026-09-14T04:02:15Z'
---

# JuliusBrussee/cavemem/README.md @ 166078dd7c46

<!-- rcw:begin owner=source:src_963027d9569757669775d414e46e68a8 block=evidence -->
- The project is frozen as of August 2026: no new features or fixes are expected, and development continues in the related caveman repository. [@claim:clm_18acbaf207d45397b5f47addc0e5747760c7e681967331a2aa39d8d00550abb7]
- The viewer worker binds to 127.0.0.1 only, checks Host/Origin headers, and requires a local bearer token (mode 0600) on /api/* endpoints. [@claim:clm_2dc40f3f1621f08f7f134df1cf8eb2329213d80b85017dd08d9224d6d3095f15]
- The npm package cavemem installs globally via npm; the default embedding provider is local (Transformers.js per CLAUDE.md), with ollama and openai as opt-in remote providers. [@claim:clm_351188e71d23d66b0f6244052fa9c8a7e615a26f9a71c7801bdce4688162ab51]
- Memory persists in a local SQLite database with FTS5 updated via triggers; embeddings are computed out-of-band by a background worker that auto-spawns on the first hook and self-exits when idle. [@claim:clm_3a40fa0208bb18e5513f35db0e9746a1e7c454a6c705c37c1d65d401f8d9120c]
- Search is hybrid: SQLite FTS5 BM25 keyword matching blended with a local vector index, weighted by the tunable search.alpha setting (default 0.5). [@claim:clm_480027dceffab8387cd4e6f137c4e4000d2e01c942ca21d43dfd440fac4d33fb]
- Per-IDE installers wire hooks and MCP: Claude Code, OpenCode, Codex, Copilot, and Augment capture observations, while Cursor, Gemini CLI, Antigravity, and IBM Bob are query-only over memory captured elsewhere. [@claim:clm_5876598e81e58c868cf404f2baa200a4126ea147b0101e82383e4a359dcaa183]
- The MCP server exposes search, timeline, get_observations, and list_sessions, plus an opt-in enrich tool; search and timeline return compact results while get_observations fetches full bodies. [@claim:clm_678ba0783d1b892060edc42a069e4f41b9b62d173e8bcbc803e80e3812eb98f6]
- The CLI offers commands including install/uninstall per IDE, status, config show/get/set/open, viewer, doctor, search, compress, reindex, export/import JSONL, and an stdio MCP server. [@claim:clm_709d3de502f98f815dd6192a06d792030c4c8233931a2f2d64d83755f34a14af]
- The enrich tool is off by default and unregistered when disabled, so no network call occurs; when enabled it enforces SSRF protections, rejecting private, loopback, link-local, and unique-local targets including obfuscated numeric forms. [@claim:clm_88e327d845e8cf0a9d80c8b1987b52295573e0bbd7f024ed555958ff70fda8a3]
<!-- rcw:end owner=source:src_963027d9569757669775d414e46e68a8 block=evidence -->

## Researcher notes

