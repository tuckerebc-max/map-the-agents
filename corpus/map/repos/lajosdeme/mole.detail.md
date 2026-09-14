# lajosdeme/mole -- full detail

[Back to orientation](mole.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lajosdeme/mole/fcb92379120d1d4205f1ac1276c41c0abbd20042/955c751591a38231.json](../../../wiki/dossiers/lajosdeme/mole/fcb92379120d1d4205f1ac1276c41c0abbd20042/955c751591a38231.json)

## specifications (1 claim(s))

- [observation/documented] Mole is a deep-research agent that decomposes a question, searches, extracts claims, quote-checks each against its source, detects contradictions, and writes a cited answer. -- evidence: [README.md#L10-L14](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L10-L14) (`clm_ad2bb538fb90c3bc61469d1b465199b517a3ffcfd2b5fedea4f16525e0783c35`)

## components (1 claim(s))

- [observation/documented] The pipeline runs planner, executor, actor (search/fetch/extract/mine), verifier (pairing, adjudication, claim graph, re-read sampling), and output stages, with three actor types: web, academic (Crossref, OpenAlex, arXiv, PubMed), and local_compute. -- evidence: [README.md#L267-L270](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L267-L270), [README.md#L255-L265](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L255-L265) (`clm_452ecfe8a0d36f6915ac00b185c19e61165c13ed3084eec5974b604104394ad8`)

## design-choices (3 claim(s))

- [observation/documented] Every model call is reserved before it happens and settled after, against a ledger with non-negative constraints in the database schema, so a set budget ceiling is enforced rather than estimated. -- evidence: [README.md#L31-L34](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L31-L34), [README.md#L10-L14](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L10-L14) (`clm_8d03659d538be2699885d99bc76202f05203bbe79a349eda801f3ff3d322b443`)
- [observation/documented] Claims whose quotes do not appear verbatim in the mined page are discarded at extraction; surviving claims can be re-read against sources and marked unsupported in the report. -- evidence: [README.md#L36-L40](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L36-L40) (`clm_1531260f91c653fa4c15b7c41d95a9ea9c4f142a9fe5e0507c4f2ecc01fb1d5a`)
- [observation/documented] For local data, the model only picks a hypothesis template and column names; mole renders and runs the SQL, and only aggregates covering at least five records may leave the machine, with `mole crossings` showing what was sent. -- evidence: [README.md#L42-L46](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L42-L46), [README.md#L193-L195](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L193-L195) (`clm_e590d26b6adf75a691a8925dd138f07fe0c29bf8f51145627a10a10c8b467f32`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: code contributions require a CLA plus Signed-off-by (DCO) on every commit; the project's non-negotiable practice is to falsify your own fix by reverting the mechanism and confirming the test fails, and PRs must pass gofmt, go build, go test (no new skips) and go vet. -- evidence: [CONTRIBUTING.md#L42-L45](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L42-L45), [README.md#L298-L300](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L298-L300), [CONTRIBUTING.md#L65-L68](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L65-L68), [README.md#L304-L307](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L304-L307), [README.md#L309-L313](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L309-L313), [CONTRIBUTING.md#L113-L118](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L113-L118) (`clm_b202a97f65e3f8f609c8c5afeffafc22b7823e43a831e3626077f005d65d7251`)
- [observation/documented] Repository development practice: dependencies policy forbids copyleft (GPL/LGPL/MPL/AGPL) and cgo-requiring dependencies, one change per pull request, and Conventional Commits subjects with explanatory bodies. -- evidence: [CONTRIBUTING.md#L101-L103](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L101-L103), [CONTRIBUTING.md#L107-L109](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L107-L109), [CONTRIBUTING.md#L126-L129](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/CONTRIBUTING.md#L126-L129) (`clm_149cb5c751712fb390528802a0796354c2c561cc09448e346f00c4544903597f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Toolkit mode (`mole serve --toolkit`) exposes fourteen `mole.<tool>` tools alongside the research tools, including search/fetch through an SSRF guard, robots handling and rate limiter, plus verify_quote, claim_add, aggregate and dataset tools. -- evidence: [README.md#L234-L241](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L234-L241), [README.md#L231-L232](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L231-L232), [README.md#L218-L220](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L218-L220) (`clm_7cf3d97f1febdc9766ac5836e7d427d736e2fae0e272230e807300788d0a2b77`)

## evaluation (1 claim(s))

- [observation/documented] Mole grades its own runs: `mole eval <session-id>` prints a scorecard, and reported metrics include 0% budget overshoot, 100% claim integrity and citation accuracy, 80% grounding rate, and 70% contradiction precision with the confirm pass. -- evidence: [README.md#L285-L292](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L285-L292), [README.md#L282-L283](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L282-L283) (`clm_84543e5ada30fb8932ed4193251aec378a6f9f4ea09ef3a75d4f7ae6fc67dae7`)

## dependencies (1 claim(s))

- [observation/documented] Installs produce two static binaries built with CGO_ENABLED=0 and no runtime dependencies; the database is SQLite created on first use under the XDG data directory, and building from source needs Go 1.25+. -- evidence: [README.md#L105-L107](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L105-L107), [README.md#L95-L95](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L95-L95) (`clm_e1a7d73e5dbd257e6e1b261e3a0e5d064f034c6784b6b9ee6269d590ba9a5ebd`)

## limitations (2 claim(s))

- [observation/documented] Local-data analysis supports CSV, TSV, JSON and JSONL but not Parquet; release binaries are unsigned, so macOS users may need to clear the Gatekeeper quarantine attribute manually. -- evidence: [RELEASING.md#L68-L70](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/RELEASING.md#L68-L70), [RELEASING.md#L76-L78](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/RELEASING.md#L76-L78), [README.md#L193-L195](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/README.md#L193-L195) (`clm_bb86068238d8c481dce6683e1a576c19b52f099c16b234acf533f3c3189763e4`)
- [observation/documented] The database schema migrates forward automatically but has no down-migrations, so downgrading across a schema change requires restoring a database copy. -- evidence: [RELEASING.md#L111-L113](https://github.com/lajosdeme/mole/blob/fcb92379120d1d4205f1ac1276c41c0abbd20042/RELEASING.md#L111-L113) (`clm_d459809a90f8e3cb3877a46ae4678c5148ef17fd01d65c9a5428fc1bdb399ea9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

