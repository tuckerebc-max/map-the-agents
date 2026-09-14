---
access: public
aliases: []
claim_ids:
- clm_014efa31d843bbb47a19b2d3b28430df70b01f416a0c7375c783f077740869b0
- clm_06f879da88d06b60c7d388e387046f56fe6af506ee18a4faed579a5a6074eb2f
- clm_2f02b6e277ce76e7d7282b7833b43336acd884213f0401d0b26b412ee479a181
- clm_68c1220a2a0a7d6c4d5bdce2eea7edde21e6fd2dfdcf975b6d38b5dfd80918c1
- clm_831cd3f04849cbaf0aaed82937ff9acb1e7d437acc1c8812074a55b2cdd8a781
- clm_887d5c322105074da3db71751862963606db9f40fae237959bceb4761a383ebf
- clm_90ddd792716c7c1436680b20d23f7600f124afb7a9f95b5c8e39c3dcb0c81381
- clm_a67c06a5f2ab6d4e8ac5e6a7f35d4d232bbfdf7bf0f18e1b9fc9477d009ebd62
- clm_bdbc751880a4565e4848c7705f9621ad5297786aa9b74c162f3ea62391dc3eca
- clm_c093bbdd09ceed9813b5537e4a98a5d10d9dc9deb7b938e8501327f0070ae494
- clm_c180d343e079be4586ea2d8cac3941d78a8c025e546919e30111b532736cc7b1
- clm_d7658fc4ac558cdedcb010254b54914e39b1c8b7ece2d637cbfd72c09bed5c87
- clm_deba28b2125e020653931f5c1282c19369f51a307a81664818dd2f3cc5f06a47
maturity: draft
page_id: pg_6e0e2a7b32fe5fbab36b9a78bb2a12b8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f489b474fcc85d7d846578b9c12de013
title: alexgreensh/outsourcerer/README.md @ 0ad71828e118
updated_at: '2026-09-14T01:32:15Z'
---

# alexgreensh/outsourcerer/README.md @ 0ad71828e118

<!-- rcw:begin owner=source:src_f489b474fcc85d7d846578b9c12de013 block=evidence -->
- The tool is described as a self-contained bash script with no server, proxy, or resident process, shelling out to existing CLIs such as claude, codex, devin, and agy. [@claim:clm_014efa31d843bbb47a19b2d3b28430df70b01f416a0c7375c783f077740869b0]
- Named lanes map to providers: OpenRouter lanes (hy3, glm-5.2, deepseek-*), Codex native (sol/terra/luna), Claude native (fable/opus/sonnet/haiku), keyless Gemini via Antigravity, Hermes, and local ollama:<model>/local lanes. [@claim:clm_06f879da88d06b60c7d388e387046f56fe6af506ee18a4faed579a5a6074eb2f]
- For local agentic runs, the harness plumbing is described as certified end to end, but how much workload it can handle depends on the local model's own tool-calling ability. [@claim:clm_2f02b6e277ce76e7d7282b7833b43336acd884213f0401d0b26b412ee479a181]
- Before any cloud delegation, a hard-block refuses the route if credential files (.env, id_rsa, credentials, etc.) exist anywhere in the working tree; the scan runs on every call and fails closed. [@claim:clm_68c1220a2a0a7d6c4d5bdce2eea7edde21e6fd2dfdcf975b6d38b5dfd80918c1]
- Repository development practice: the project is audited with repo-forensics (27 scanners, 500+ patterns) on every release, with every finding triaged by name and no suppressions, per README and SECURITY.md. [@claim:clm_831cd3f04849cbaf0aaed82937ff9acb1e7d437acc1c8812074a55b2cdd8a781]
- Routing precedence is explicitly ordered: global -m wins, then --route name mapping, then per-agent frontmatter, then the default lane. [@claim:clm_887d5c322105074da3db71751862963606db9f40fae237959bceb4761a383ebf]
- Advisor panels convene several strong models in parallel to review a plan or diff, and work is greenlit only on consensus; a split decision is returned to the user. [@claim:clm_90ddd792716c7c1436680b20d23f7600f124afb7a9f95b5c8e39c3dcb0c81381]
- The fleet view currently covers only Claude Code sessions and Outsourcerer's own jobs; seeing sessions launched by other tools is listed as future work. [@claim:clm_a67c06a5f2ab6d4e8ac5e6a7f35d4d232bbfdf7bf0f18e1b9fc9477d009ebd62]
- The CLI exposes verbs including run/research/edit/yolo, bg/status/watch/result/logs/cancel, second-opinion, image, tab/estimate, suggest/deals, doctor/models, and parity variants. [@claim:clm_bdbc751880a4565e4848c7705f9621ad5297786aa9b74c162f3ea62391dc3eca]
- A fanout command runs multi-agent squads across backends, with fanout status <id> --json returning a stable JSON envelope and fanout collect gathering results into one place. [@claim:clm_c093bbdd09ceed9813b5537e4a98a5d10d9dc9deb7b938e8501327f0070ae494]
- The project is licensed under PolyForm Noncommercial 1.0.0, with commercial use requiring a separate license from the author. [@claim:clm_c180d343e079be4586ea2d8cac3941d78a8c025e546919e30111b532736cc7b1]
- The Tab ledger separates real cash cost (read back exactly from OpenRouter per generation) from subscription plan-limit usage, never labeling subscription spend as free. [@claim:clm_d7658fc4ac558cdedcb010254b54914e39b1c8b7ece2d637cbfd72c09bed5c87]
- Delegates are watchdog-supervised to a classified end state (done / blocked / timed-out), with exit codes distinguishing done, done-but-unverified, and blocked, and stalled delegates killed rather than silently retried. [@claim:clm_deba28b2125e020653931f5c1282c19369f51a307a81664818dd2f3cc5f06a47]
<!-- rcw:end owner=source:src_f489b474fcc85d7d846578b9c12de013 block=evidence -->

## Researcher notes

