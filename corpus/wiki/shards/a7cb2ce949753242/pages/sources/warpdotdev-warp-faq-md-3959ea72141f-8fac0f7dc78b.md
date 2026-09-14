---
access: public
aliases: []
claim_ids:
- clm_297ba371e28c71fed9f839583e66a8e7e3da8167d748ac379e216e8dca401548
- clm_7c5f892d169b977226e2500467871b71343df62d2d007f33437254d597d624be
- clm_8de74709cf5dc0277db517103889e498b0541c16aee968091c2ddbf899124843
- clm_aa4e524f10c87a45e56ba83c230708116e7fb8adf4eb1c97772dea0e025332cf
- clm_abb8854e58d35956b509194910b8753a0a99655e88ffdcf6a513cff0ea91ad67
- clm_b5f9b3c639ca7fe384065b7558a08b8ac24d2eb63eed2c6750b6b5f4771932e7
- clm_c9776c75c1dbb5f245d29ac1780a8202acc203318ef5002964930c24e0ff5d9f
- clm_d82042df7cf48253c27f0a9a7220288d44c40d5603848b02cd3603158acb4cd7
- clm_edd5773819d5ba003096fbc343c4b26e572b9fbdc085294431c4ced4b2a96e0e
- clm_f1faf50466731188deb092a2eae9e830216a4182f981198225bbd539488a0f07
maturity: draft
page_id: pg_9a093d243bf953e696f28fac0f7dc78b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b55ff0a089b55d44b84243f22aef37b0
title: warpdotdev/warp/FAQ.md @ 3959ea72141f
updated_at: '2026-09-14T03:22:42Z'
---

# warpdotdev/warp/FAQ.md @ 3959ea72141f

<!-- rcw:begin owner=source:src_b55ff0a089b55d44b84243f22aef37b0 block=evidence -->
- Running Warp provides a /feedback command that files an issue with logs and environment details attached automatically. [@claim:clm_297ba371e28c71fed9f839583e66a8e7e3da8167d748ac379e216e8dca401548]
- The client app is licensed AGPL v3 to keep derivatives open, while the warpui_core and warpui UI framework crates are MIT-licensed to maximize reuse. [@claim:clm_7c5f892d169b977226e2500467871b71343df62d2d007f33437254d597d624be]
- Warp's built-in agent harness runs server-side and is not open in this repository, so Codex or Claude models cannot currently be used with existing subscriptions in Warp. [@claim:clm_8de74709cf5dc0277db517103889e498b0541c16aee968091c2ddbf899124843]
- The server, Warp Drive backend, hosted authentication, and the Oz agent orchestration layer are not in this repository and remain proprietary. [@claim:clm_aa4e524f10c87a45e56ba83c230708116e7fb8adf4eb1c97772dea0e025332cf]
- Repository development practice: collaborators — contributors with a track record of merged PRs — can apply labels, dispatch Oz directly with @oz on ready issues, and use complimentary Oz credits. [@claim:clm_abb8854e58d35956b509194910b8753a0a99655e88ffdcf6a513cff0ea91ad67]
- Repository development practice: build and run locally via ./script/bootstrap and ./script/run (or cargo run), with ./script/presubmit running fmt, clippy, and tests; tests can also run via cargo nextest. [@claim:clm_b5f9b3c639ca7fe384065b7558a08b8ac24d2eb63eed2c6750b6b5f4771932e7]
- Repository development practice: security vulnerabilities must not be opened as public issues; they are reported via security@warp.dev or a private GitHub Security Advisory. [@claim:clm_c9776c75c1dbb5f245d29ac1780a8202acc203318ef5002964930c24e0ff5d9f]
- Repository development practice: contributions start with a GitHub issue; maintainers apply readiness labels (ready-to-spec, ready-to-implement, needs-mocks), and feature work requires a spec PR adding product.md and tech.md under specs/GH<issue-number>/ before code. [@claim:clm_d82042df7cf48253c27f0a9a7220288d44c40d5603848b02cd3603158acb4cd7]
- The team plans to support the Agent Client Protocol (ACP) in Warp so other models or subscriptions could connect directly; this is tracked on their roadmap. [@claim:clm_edd5773819d5ba003096fbc343c4b26e572b9fbdc085294431c4ced4b2a96e0e]
- Repository development practice: opened PRs are auto-assigned to Oz for an initial review, then a Warp subject-matter expert is requested; contributors can comment /warp-agent-review up to three times per PR for re-review. [@claim:clm_f1faf50466731188deb092a2eae9e830216a4182f981198225bbd539488a0f07]
<!-- rcw:end owner=source:src_b55ff0a089b55d44b84243f22aef37b0 block=evidence -->

## Researcher notes

