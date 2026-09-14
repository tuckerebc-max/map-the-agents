---
access: public
aliases: []
claim_ids:
- clm_1ea97589fc09cc3c9a5e2a5a8c20af49bddfd7f15319a0ec5b417763f9138c6a
- clm_3824115687f4cc94ace7178046d3b164211a05fda3dee54eac83d040d7f65454
- clm_53db1ddb3fbd397fc41e84bc33f89088fe682ca065ceb7d7586c89e18e455c3a
- clm_5ecc33fbadd124697e74a982b0fe802ac7e9e0a3ee0dba791d70824c97974b5e
- clm_6e2bc898058983798aa8946eb6f71cdcfab870b15b58d1820581a43bad0cf843
- clm_917a7ec2031df2d25e238e9f3bd9fc3697cbae2f55d77be1dc75a59512c3db1b
- clm_cc6dfd0780483a2792d13ae3b92ad8c3e0d78e4390d6f2d0638042a3de825313
maturity: draft
page_id: pg_a90a3204063b54ea9f0e9706255094d4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8f788fa20ca65049a2a5c4dd31bb13df
title: letstri/druk/ARCHITECTURE.md @ 0027143d76ae
updated_at: '2026-09-14T04:05:49Z'
---

# letstri/druk/ARCHITECTURE.md @ 0027143d76ae

<!-- rcw:begin owner=source:src_8f788fa20ca65049a2a5c4dd31bb13df block=evidence -->
- Repository development practice: the extension market is a folder in this repo served raw from main, so a merged pull request makes an extension installable immediately; contributing one is a JSON file plus a PR. [@claim:clm_1ea97589fc09cc3c9a5e2a5a8c20af49bddfd7f15319a0ec5b417763f9138c6a]
- Repository development practice: highlight queries should be compiled against their grammar and asserted in test/languages.test.ts, since bad queries fail silently. [@claim:clm_3824115687f4cc94ace7178046d3b164211a05fda3dee54eac83d040d7f65454]
- Settings live in two layers: a global config.json rewritten whole and a per-project .druk/settings.json of overrides that wins after merging. [@claim:clm_53db1ddb3fbd397fc41e84bc33f89088fe682ca065ceb7d7586c89e18e455c3a]
- A filetype may have several language servers and all run concurrently; diagnostics are kept per sender and merged, while feature requests go to each ready server in turn with the first real answer winning. [@claim:clm_5ecc33fbadd124697e74a982b0fe802ac7e9e0a3ee0dba791d70824c97974b5e]
- The app is a Solid application rendered to the terminal by OpenTUI, which supplies layout, text buffer, undo/redo, mouse hit-testing and the tree-sitter worker; the repo is the wiring around it. [@claim:clm_6e2bc898058983798aa8946eb6f71cdcfab870b15b58d1820581a43bad0cf843]
- Repository development practice: a boundary test fails the suite if ui/ or feature folders import from app/, enforcing one-way dependency direction. [@claim:clm_917a7ec2031df2d25e238e9f3bd9fc3697cbae2f55d77be1dc75a59512c3db1b]
- Extensions are JSON manifests, never code: installing one executes nothing, and manifests are read at startup with reload available via 'r' in the extensions panel. [@claim:clm_cc6dfd0780483a2792d13ae3b92ad8c3e0d78e4390d6f2d0638042a3de825313]
<!-- rcw:end owner=source:src_8f788fa20ca65049a2a5c4dd31bb13df block=evidence -->

## Researcher notes

