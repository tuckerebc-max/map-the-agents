---
access: public
aliases: []
claim_ids:
- clm_8374dcf6a5449d05bc5027669e5d3eef0dd0489cc761195d0962650a7f29ee71
- clm_c210ef6ff92d634ad5e213f0898363670b8f34945e7c5920323c7154ea61b5ab
- clm_ca0202b988c8d7907b8680595a89a1420534460b8d6bd605e8ccf58feb8bc9f1
maturity: draft
page_id: pg_4166b62ddfba5f1ab514bfc2b1cedc8d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a9e795df0a0b5833ba369768739c3a52
title: charmbracelet/fantasy/AGENTS.md @ 1dada21b01e8
updated_at: '2026-09-14T03:06:09Z'
---

# charmbracelet/fantasy/AGENTS.md @ 1dada21b01e8

<!-- rcw:begin owner=source:src_a9e795df0a0b5833ba369768739c3a52 block=evidence -->
- Repository development practice: style notes prefer cmp.Or for defaults, use json/description/enum struct tags for schema generation, and use charm.land/x/vcr rather than go-vcr for HTTP test recording. [@claim:clm_8374dcf6a5449d05bc5027669e5d3eef0dd0489cc761195d0962650a7f29ee71]
- Repository development practice: provider integration tests use VCR cassettes in testdata, with API keys supplied via FANTASY_<PROVIDER>_API_KEY env vars loaded from .env, and the recorder injected as an http.Client transport. [@claim:clm_c210ef6ff92d634ad5e213f0898363670b8f34945e7c5920323c7154ea61b5ab]
- Repository development practice: contributors build with go build ./..., test via task test or go test with a 30m timeout, and lint/format using golangci-lint and gofumpt. [@claim:clm_ca0202b988c8d7907b8680595a89a1420534460b8d6bd605e8ccf58feb8bc9f1]
<!-- rcw:end owner=source:src_a9e795df0a0b5833ba369768739c3a52 block=evidence -->

## Researcher notes

