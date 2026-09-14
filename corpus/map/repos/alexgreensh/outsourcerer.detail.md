# alexgreensh/outsourcerer -- full detail

[Back to orientation](outsourcerer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/alexgreensh/outsourcerer/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/bb346553aa25c2f8.json](../../../wiki/dossiers/alexgreensh/outsourcerer/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/bb346553aa25c2f8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The tool is described as a self-contained bash script with no server, proxy, or resident process, shelling out to existing CLIs such as claude, codex, devin, and agy. -- evidence: [README.md#L189-L189](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L189-L189) (`clm_014efa31d843bbb47a19b2d3b28430df70b01f416a0c7375c783f077740869b0`)

## design-choices (2 claim(s))

- [observation/documented] Routing precedence is explicitly ordered: global -m wins, then --route name mapping, then per-agent frontmatter, then the default lane. -- evidence: [README.md#L224-L224](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L224-L224) (`clm_887d5c322105074da3db71751862963606db9f40fae237959bceb4761a383ebf`)
- [observation/documented] The Tab ledger separates real cash cost (read back exactly from OpenRouter per generation) from subscription plan-limit usage, never labeling subscription spend as free. -- evidence: [README.md#L183-L183](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L183-L183), [README.md#L169-L169](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L169-L169) (`clm_d7658fc4ac558cdedcb010254b54914e39b1c8b7ece2d637cbfd72c09bed5c87`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the project is audited with repo-forensics (27 scanners, 500+ patterns) on every release, with every finding triaged by name and no suppressions, per README and SECURITY.md. -- evidence: [README.md#L264-L264](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L264-L264), [SECURITY.md#L3-L4](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L3-L4), [SECURITY.md#L8-L11](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L8-L11) (`clm_831cd3f04849cbaf0aaed82937ff9acb1e7d437acc1c8812074a55b2cdd8a781`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes verbs including run/research/edit/yolo, bg/status/watch/result/logs/cancel, second-opinion, image, tab/estimate, suggest/deals, doctor/models, and parity variants. -- evidence: [README.md#L302-L312](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L302-L312) (`clm_bdbc751880a4565e4848c7705f9621ad5297786aa9b74c162f3ea62391dc3eca`)
- [observation/documented] Named lanes map to providers: OpenRouter lanes (hy3, glm-5.2, deepseek-*), Codex native (sol/terra/luna), Claude native (fable/opus/sonnet/haiku), keyless Gemini via Antigravity, Hermes, and local ollama:<model>/local lanes. -- evidence: [README.md#L314-L316](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L314-L316) (`clm_06f879da88d06b60c7d388e387046f56fe6af506ee18a4faed579a5a6074eb2f`)
- [observation/documented] A fanout command runs multi-agent squads across backends, with fanout status <id> --json returning a stable JSON envelope and fanout collect gathering results into one place. -- evidence: [README.md#L226-L230](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L226-L230) (`clm_c093bbdd09ceed9813b5537e4a98a5d10d9dc9deb7b938e8501327f0070ae494`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Delegates are watchdog-supervised to a classified end state (done / blocked / timed-out), with exit codes distinguishing done, done-but-unverified, and blocked, and stalled delegates killed rather than silently retried. -- evidence: [README.md#L191-L191](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L191-L191), [README.md#L216-L216](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L216-L216) (`clm_deba28b2125e020653931f5c1282c19369f51a307a81664818dd2f3cc5f06a47`)
- [observation/documented] Advisor panels convene several strong models in parallel to review a plan or diff, and work is greenlit only on consensus; a split decision is returned to the user. -- evidence: [README.md#L89-L91](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L89-L91) (`clm_90ddd792716c7c1436680b20d23f7600f124afb7a9f95b5c8e39c3dcb0c81381`)

## tools-permissions (2 claim(s))

- [observation/documented] Before any cloud delegation, a hard-block refuses the route if credential files (.env, id_rsa, credentials, etc.) exist anywhere in the working tree; the scan runs on every call and fails closed. -- evidence: [SECURITY.md#L48-L61](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L48-L61), [README.md#L266-L270](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L266-L270) (`clm_68c1220a2a0a7d6c4d5bdce2eea7edde21e6fd2dfdcf975b6d38b5dfd80918c1`)
- [observation/documented] Keys are read one variable at a time from ~/.env via targeted grep, never sourcing the whole file, and keys are never written into command-line arguments, logs, or config. -- evidence: [SECURITY.md#L34-L41](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L34-L41) (`clm_a8ac17ae18bb73c54e70b647c6c55e45617787687a898ab2ae07ec5193c8b0c7`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is licensed under PolyForm Noncommercial 1.0.0, with commercial use requiring a separate license from the author. -- evidence: [README.md#L338-L340](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L338-L340) (`clm_c180d343e079be4586ea2d8cac3941d78a8c025e546919e30111b532736cc7b1`)

## limitations (2 claim(s))

- [observation/documented] The fleet view currently covers only Claude Code sessions and Outsourcerer's own jobs; seeing sessions launched by other tools is listed as future work. -- evidence: [README.md#L256-L256](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L256-L256) (`clm_a67c06a5f2ab6d4e8ac5e6a7f35d4d232bbfdf7bf0f18e1b9fc9477d009ebd62`)
- [observation/documented] For local agentic runs, the harness plumbing is described as certified end to end, but how much workload it can handle depends on the local model's own tool-calling ability. -- evidence: [README.md#L161-L161](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L161-L161) (`clm_2f02b6e277ce76e7d7282b7833b43336acd884213f0401d0b26b412ee479a181`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

