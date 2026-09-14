---
access: public
aliases: []
claim_ids:
- clm_051358a600903fbf2629c7c1a561eee89dd5de0c3655d1627a9b228931e1a927
- clm_173b7290be7533fd5fa8243574757901fc60c16016201c5656df6e7269512b5e
- clm_2008f132505d8df7fbc5c33e85d8f44eccddae40c209aac60bacd754f2e858a3
- clm_4eff98b8074953d663bdce06a6abee90be9bf0067f6777166a4ac60674a91ade
- clm_815defda74edca82280645dffd090daa13f499b1492fbd8147e5a6407eea8966
- clm_b0ee847eb7d63b4303837772521ccbd33b007ca63bdaf91ffb1993ce5be31575
- clm_deefff07348a46499f52b6ff51222f85f1987fe6394b4d731d8395423503141b
maturity: draft
page_id: pg_b66489240f04526681278b643d5f706c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c07ad8106cee5d98bd51c238a4b75c06
title: hivemoot/hivemoot/docs/adr/002-plugin-architecture.md @ a49baa71cf00
updated_at: '2026-09-14T02:03:40Z'
---

# hivemoot/hivemoot/docs/adr/002-plugin-architecture.md @ a49baa71cf00

<!-- rcw:begin owner=source:src_c07ad8106cee5d98bd51c238a4b75c06 block=evidence -->
- Per ADR-002, the agent CLI surface is fixed and generic: `hivemoot-agent run`, `oneshot`, `worker`, `plugin list`, `plugin doctor <name>`, and `doctor`, with no plugin-specific subcommands. [@claim:clm_051358a600903fbf2629c7c1a561eee89dd5de0c3655d1627a9b228931e1a927]
- ADR-002's accepted decision is that the host is plugin-agnostic: all plugin-specific behavior lives inside the plugin directory, and adding a plugin must not change the CLI surface or require host changes. [@claim:clm_173b7290be7533fd5fa8243574757901fc60c16016201c5656df6e7269512b5e]
- A cron plugin provides a stdlib-only 5-field cron parser, an @every shorthand, per-entry prompts with optional jitter and session resume, all times UTC, configured via CRON_SCHEDULES_JSON. [@claim:clm_2008f132505d8df7fbc5c33e85d8f44eccddae40c209aac60bacd754f2e858a3]
- Plugins implement a Plugin protocol with hooks (validate, setup, triggers, system_prompt, on_job_started/on_agent_output/on_job_finished) and a Trigger protocol with validate, start, and stop methods. [@claim:clm_4eff98b8074953d663bdce06a6abee90be9bf0067f6777166a4ac60674a91ade]
- The container entrypoint is `hivemoot-agent run` in daemon mode: it loads plugins from AGENT_PLUGINS, starts each plugin's triggers in-process, and dispatches jobs to an agent subprocess (e.g. Claude) in the same container. [@claim:clm_815defda74edca82280645dffd090daa13f499b1492fbd8147e5a6407eea8966]
- Under the plugin engine, jobs run sequentially within an agent container, and crash isolation is per-agent-container rather than per-job, mitigated by systemd restart policy. [@claim:clm_b0ee847eb7d63b4303837772521ccbd33b007ca63bdaf91ffb1993ce5be31575]
- Persistent state such as sessions and memory is scoped per plugin/job via session_key and per-plugin workspace conventions, per ADR-002's consequences section. [@claim:clm_deefff07348a46499f52b6ff51222f85f1987fe6394b4d731d8395423503141b]
<!-- rcw:end owner=source:src_c07ad8106cee5d98bd51c238a4b75c06 block=evidence -->

## Researcher notes

