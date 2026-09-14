# warpdotdev/warp -- full detail

[Back to orientation](warp.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/warpdotdev/warp/3959ea72141fc0ecd007665029a8058e0e6db0f8/afc2f384249b5adc.json](../../../wiki/dossiers/warpdotdev/warp/3959ea72141fc0ecd007665029a8058e0e6db0f8/afc2f384249b5adc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The client app is licensed AGPL v3 to keep derivatives open, while the warpui_core and warpui UI framework crates are MIT-licensed to maximize reuse. -- evidence: [FAQ.md#L115-L115](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L115-L115), [README.md#L56-L56](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L56-L56), [README.md#L54-L54](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L54-L54), [FAQ.md#L117-L117](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L117-L117) (`clm_7c5f892d169b977226e2500467871b71343df62d2d007f33437254d597d624be`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: contributions start with a GitHub issue; maintainers apply readiness labels (ready-to-spec, ready-to-implement, needs-mocks), and feature work requires a spec PR adding product.md and tech.md under specs/GH<issue-number>/ before code. -- evidence: [FAQ.md#L27-L27](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L27-L27), [README.md#L69-L69](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L69-L69), [FAQ.md#L9-L9](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L9-L9), [FAQ.md#L19-L21](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L19-L21) (`clm_d82042df7cf48253c27f0a9a7220288d44c40d5603848b02cd3603158acb4cd7`)
- [observation/documented] Repository development practice: opened PRs are auto-assigned to Oz for an initial review, then a Warp subject-matter expert is requested; contributors can comment /warp-agent-review up to three times per PR for re-review. -- evidence: [FAQ.md#L41-L41](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L41-L41), [FAQ.md#L45-L45](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L45-L45) (`clm_f1faf50466731188deb092a2eae9e830216a4182f981198225bbd539488a0f07`)
- [observation/documented] Repository development practice: build and run locally via ./script/bootstrap and ./script/run (or cargo run), with ./script/presubmit running fmt, clippy, and tests; tests can also run via cargo nextest. -- evidence: [AGENTS.md#L28-L30](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/AGENTS.md#L28-L30), [README.md#L75-L79](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L75-L79), [FAQ.md#L31-L35](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L31-L35) (`clm_b5f9b3c639ca7fe384065b7558a08b8ac24d2eb63eed2c6750b6b5f4771932e7`)
- [observation/documented] Repository development practice: security vulnerabilities must not be opened as public issues; they are reported via security@warp.dev or a private GitHub Security Advisory. -- evidence: [FAQ.md#L144-L144](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L144-L144), [SECURITY.md#L7-L7](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/SECURITY.md#L7-L7), [SECURITY.md#L11-L12](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/SECURITY.md#L11-L12) (`clm_c9776c75c1dbb5f245d29ac1780a8202acc203318ef5002964930c24e0ff5d9f`)
- [observation/documented] Repository development practice: collaborators — contributors with a track record of merged PRs — can apply labels, dispatch Oz directly with @oz on ready issues, and use complimentary Oz credits. -- evidence: [FAQ.md#L75-L75](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L75-L75), [FAQ.md#L51-L51](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L51-L51) (`clm_abb8854e58d35956b509194910b8753a0a99655e88ffdcf6a513cff0ea91ad67`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Running Warp provides a /feedback command that files an issue with logs and environment details attached automatically. -- evidence: [FAQ.md#L15-L15](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L15-L15) (`clm_297ba371e28c71fed9f839583e66a8e7e3da8167d748ac379e216e8dca401548`)
- [observation/documented] The team plans to support the Agent Client Protocol (ACP) in Warp so other models or subscriptions could connect directly; this is tracked on their roadmap. -- evidence: [FAQ.md#L69-L69](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L69-L69), [FAQ.md#L67-L67](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L67-L67) (`clm_edd5773819d5ba003096fbc343c4b26e572b9fbdc085294431c4ced4b2a96e0e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README calls out open-source dependencies including Tokio, NuShell, Alacritty, Hyper, FontKit, Smol, Fig completion specs, and the warp server framework. -- evidence: [README.md#L102-L110](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L102-L110), [README.md#L100-L100](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/README.md#L100-L100) (`clm_d32e1ab6efdbc6ca898ebed2bc6735352397d1f30806cbeba97599adfe1c2174`)

## limitations (2 claim(s))

- [observation/documented] The server, Warp Drive backend, hosted authentication, and the Oz agent orchestration layer are not in this repository and remain proprietary. -- evidence: [FAQ.md#L93-L93](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L93-L93), [FAQ.md#L99-L99](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L99-L99) (`clm_aa4e524f10c87a45e56ba83c230708116e7fb8adf4eb1c97772dea0e025332cf`)
- [observation/documented] Warp's built-in agent harness runs server-side and is not open in this repository, so Codex or Claude models cannot currently be used with existing subscriptions in Warp. -- evidence: [FAQ.md#L65-L65](https://github.com/warpdotdev/warp/blob/3959ea72141fc0ecd007665029a8058e0e6db0f8/FAQ.md#L65-L65) (`clm_8de74709cf5dc0277db517103889e498b0541c16aee968091c2ddbf899124843`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

