---
access: public
aliases: []
claim_ids:
- clm_1531260f91c653fa4c15b7c41d95a9ea9c4f142a9fe5e0507c4f2ecc01fb1d5a
- clm_452ecfe8a0d36f6915ac00b185c19e61165c13ed3084eec5974b604104394ad8
- clm_7cf3d97f1febdc9766ac5836e7d427d736e2fae0e272230e807300788d0a2b77
- clm_84543e5ada30fb8932ed4193251aec378a6f9f4ea09ef3a75d4f7ae6fc67dae7
- clm_8d03659d538be2699885d99bc76202f05203bbe79a349eda801f3ff3d322b443
- clm_ad2bb538fb90c3bc61469d1b465199b517a3ffcfd2b5fedea4f16525e0783c35
- clm_b202a97f65e3f8f609c8c5afeffafc22b7823e43a831e3626077f005d65d7251
- clm_bb86068238d8c481dce6683e1a576c19b52f099c16b234acf533f3c3189763e4
- clm_e1a7d73e5dbd257e6e1b261e3a0e5d064f034c6784b6b9ee6269d590ba9a5ebd
- clm_e590d26b6adf75a691a8925dd138f07fe0c29bf8f51145627a10a10c8b467f32
maturity: draft
page_id: pg_3d4bf4fc657e52a7983964ec687cbde0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e0deca96a36857d8bcfcad0322447ca2
title: lajosdeme/mole/README.md @ fcb92379120d
updated_at: '2026-09-14T04:05:07Z'
---

# lajosdeme/mole/README.md @ fcb92379120d

<!-- rcw:begin owner=source:src_e0deca96a36857d8bcfcad0322447ca2 block=evidence -->
- Claims whose quotes do not appear verbatim in the mined page are discarded at extraction; surviving claims can be re-read against sources and marked unsupported in the report. [@claim:clm_1531260f91c653fa4c15b7c41d95a9ea9c4f142a9fe5e0507c4f2ecc01fb1d5a]
- The pipeline runs planner, executor, actor (search/fetch/extract/mine), verifier (pairing, adjudication, claim graph, re-read sampling), and output stages, with three actor types: web, academic (Crossref, OpenAlex, arXiv, PubMed), and local_compute. [@claim:clm_452ecfe8a0d36f6915ac00b185c19e61165c13ed3084eec5974b604104394ad8]
- Toolkit mode (`mole serve --toolkit`) exposes fourteen `mole.<tool>` tools alongside the research tools, including search/fetch through an SSRF guard, robots handling and rate limiter, plus verify_quote, claim_add, aggregate and dataset tools. [@claim:clm_7cf3d97f1febdc9766ac5836e7d427d736e2fae0e272230e807300788d0a2b77]
- Mole grades its own runs: `mole eval <session-id>` prints a scorecard, and reported metrics include 0% budget overshoot, 100% claim integrity and citation accuracy, 80% grounding rate, and 70% contradiction precision with the confirm pass. [@claim:clm_84543e5ada30fb8932ed4193251aec378a6f9f4ea09ef3a75d4f7ae6fc67dae7]
- Every model call is reserved before it happens and settled after, against a ledger with non-negative constraints in the database schema, so a set budget ceiling is enforced rather than estimated. [@claim:clm_8d03659d538be2699885d99bc76202f05203bbe79a349eda801f3ff3d322b443]
- Mole is a deep-research agent that decomposes a question, searches, extracts claims, quote-checks each against its source, detects contradictions, and writes a cited answer. [@claim:clm_ad2bb538fb90c3bc61469d1b465199b517a3ffcfd2b5fedea4f16525e0783c35]
- Repository development practice: code contributions require a CLA plus Signed-off-by (DCO) on every commit; the project's non-negotiable practice is to falsify your own fix by reverting the mechanism and confirming the test fails, and PRs must pass gofmt, go build, go test (no new skips) and go vet. [@claim:clm_b202a97f65e3f8f609c8c5afeffafc22b7823e43a831e3626077f005d65d7251]
- Local-data analysis supports CSV, TSV, JSON and JSONL but not Parquet; release binaries are unsigned, so macOS users may need to clear the Gatekeeper quarantine attribute manually. [@claim:clm_bb86068238d8c481dce6683e1a576c19b52f099c16b234acf533f3c3189763e4]
- Installs produce two static binaries built with CGO_ENABLED=0 and no runtime dependencies; the database is SQLite created on first use under the XDG data directory, and building from source needs Go 1.25+. [@claim:clm_e1a7d73e5dbd257e6e1b261e3a0e5d064f034c6784b6b9ee6269d590ba9a5ebd]
- For local data, the model only picks a hypothesis template and column names; mole renders and runs the SQL, and only aggregates covering at least five records may leave the machine, with `mole crossings` showing what was sent. [@claim:clm_e590d26b6adf75a691a8925dd138f07fe0c29bf8f51145627a10a10c8b467f32]
<!-- rcw:end owner=source:src_e0deca96a36857d8bcfcad0322447ca2 block=evidence -->

## Researcher notes

