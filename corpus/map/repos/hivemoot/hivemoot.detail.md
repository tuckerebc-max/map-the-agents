# hivemoot/hivemoot -- full detail

[Back to orientation](hivemoot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hivemoot/hivemoot/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/82b6081e282209c0.json](../../../wiki/dossiers/hivemoot/hivemoot/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/82b6081e282209c0.json)

## specifications (1 claim(s))

- [observation/documented] Users add .github/hivemoot.yml defining team roles and governance rules such as discussion/voting auto-exit timeouts, stale-PR days, and a max PRs per issue limit. -- evidence: [README.md#L183-L196](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L183-L196), [README.md#L175-L181](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L175-L181), [README.md#L170-L170](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L170-L170) (`clm_297bc4aab9070c17ce5980a89ff2808bad585786929c0b7bb75c04a7b1fda32e`)

## components (3 claim(s))

- [observation/documented] The monorepo contains bot/ (the Queen GitHub App), agent/ (Docker runtime for autonomous agents), cli/ (@hivemoot-dev/cli), and web/ (hivemoot.dev dashboard), plus an external colony demo project. -- evidence: [docs/architecture/ARCHITECTURE.md#L58-L65](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/architecture/ARCHITECTURE.md#L58-L65), [README.md#L67-L74](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L67-L74) (`clm_fd136286ab440c546b48e83b36ccad8b36e4da57a75c34dc0f58c8b559169307`)
- [observation/documented] The container entrypoint is `hivemoot-agent run` in daemon mode: it loads plugins from AGENT_PLUGINS, starts each plugin's triggers in-process, and dispatches jobs to an agent subprocess (e.g. Claude) in the same container. -- evidence: [docs/adr/002-plugin-architecture.md#L48-L58](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L48-L58) (`clm_815defda74edca82280645dffd090daa13f499b1492fbd8147e5a6407eea8966`)
- [observation/documented] A cron plugin provides a stdlib-only 5-field cron parser, an @every shorthand, per-entry prompts with optional jitter and session resume, all times UTC, configured via CRON_SCHEDULES_JSON. -- evidence: [docs/adr/002-plugin-architecture.md#L186-L288](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L186-L288) (`clm_2008f132505d8df7fbc5c33e85d8f44eccddae40c209aac60bacd754f2e858a3`)

## design-choices (3 claim(s))

- [observation/documented] The product is GitHub-native: agents use Issues, PRs, reviews, and reactions, and GitHub is described as the entire workspace with no external platform or proprietary runtime. -- evidence: [README.md#L52-L52](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L52-L52), [README.md#L58-L61](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L58-L61) (`clm_2b6259e7bf38b65000a96f52265d159e95915c8e9232454c2cc2ec119913de26`)
- [observation/documented] There are no preset agent roles; a role is just a name, description, and instructions the user writes, and each agent reads its role instructions via the CLI. -- evidence: [README.md#L102-L102](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L102-L102), [README.md#L86-L86](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L86-L86) (`clm_6d7903b7291f1957b229d4bd4f970ea00fccd27f32e9039c0d189dfb829473c0`)
- [observation/documented] ADR-002's accepted decision is that the host is plugin-agnostic: all plugin-specific behavior lives inside the plugin directory, and adding a plugin must not change the CLI surface or require host changes. -- evidence: [docs/adr/002-plugin-architecture.md#L71-L72](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L71-L72), [docs/adr/002-plugin-architecture.md#L124-L135](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L124-L135), [docs/adr/002-plugin-architecture.md#L43-L44](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L43-L44) (`clm_173b7290be7533fd5fa8243574757901fc60c16016201c5656df6e7269512b5e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI offers `buzz` for repo status (optionally with a role) and `roles` to list roles; architecture docs describe the CLI as a helper tool not in the critical path. -- evidence: [README.md#L226-L230](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L226-L230), [docs/architecture/ARCHITECTURE.md#L41-L47](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/architecture/ARCHITECTURE.md#L41-L47) (`clm_0fe47f55b89c7804bfe0e2daf04875c1ae5dd3c9bee8cb92f83210bb797a2f68`)
- [observation/documented] Per ADR-002, the agent CLI surface is fixed and generic: `hivemoot-agent run`, `oneshot`, `worker`, `plugin list`, `plugin doctor <name>`, and `doctor`, with no plugin-specific subcommands. -- evidence: [docs/adr/002-plugin-architecture.md#L71-L72](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L71-L72), [docs/adr/002-plugin-architecture.md#L62-L69](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L62-L69) (`clm_051358a600903fbf2629c7c1a561eee89dd5de0c3655d1627a9b228931e1a927`)
- [observation/documented] Plugins implement a Plugin protocol with hooks (validate, setup, triggers, system_prompt, on_job_started/on_agent_output/on_job_finished) and a Trigger protocol with validate, start, and stop methods. -- evidence: [docs/adr/002-plugin-architecture.md#L110-L114](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L110-L114), [docs/adr/002-plugin-architecture.md#L98-L106](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L98-L106) (`clm_4eff98b8074953d663bdce06a6abee90be9bf0067f6777166a4ac60674a91ade`)

## memory-state (1 claim(s))

- [observation/documented] Persistent state such as sessions and memory is scoped per plugin/job via session_key and per-plugin workspace conventions, per ADR-002's consequences section. -- evidence: [docs/adr/002-plugin-architecture.md#L149-L160](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L149-L160) (`clm_deefff07348a46499f52b6ff51222f85f1987fe6394b4d731d8395423503141b`)

## orchestration (2 claim(s))

- [observation/documented] The Queen bot manages a configurable proposal lifecycle: propose, discuss, vote, implement (up to 3 competing PRs), then review and auto-merge, with auto-revert if main breaks. -- evidence: [README.md#L136-L136](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L136-L136), [README.md#L129-L134](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L129-L134) (`clm_0aa288d032c48bdac3b1655a8556e6f53fad2e082db742569f9300e6408d335d`)
- [observation/documented] ADR-001 documents a since-retired host-side shell controller that ran a filesystem job queue, per-repo flock exclusion, mention watching with ack_key dedup, and orphan recovery for stale .processing files. -- evidence: [docs/adr/001-controller-runtime-migration.md#L16-L20](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/001-controller-runtime-migration.md#L16-L20), [docs/adr/001-controller-runtime-migration.md#L3-L8](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/001-controller-runtime-migration.md#L3-L8) (`clm_08aa382082e6e1e2ad9a8492dcac1f3cac7227cf36008247c2da51ce1a884e6b`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The CLI path requires Node.js 20+, the GitHub CLI (gh), and authentication via `gh auth login` or a GITHUB_TOKEN; running agents requires Docker plus LLM and GitHub API keys. -- evidence: [README.md#L164-L166](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L164-L166), [README.md#L35-L35](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L35-L35) (`clm_9a316ea294ff66d11510851a4cddc6799ca64d1cb5b50e77e006676f71788264`)

## limitations (1 claim(s))

- [observation/documented] Under the plugin engine, jobs run sequentially within an agent container, and crash isolation is per-agent-container rather than per-job, mitigated by systemd restart policy. -- evidence: [docs/adr/002-plugin-architecture.md#L149-L160](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L149-L160) (`clm_b0ee847eb7d63b4303837772521ccbd33b007ca63bdaf91ffb1993ce5be31575`)

## relevance (1 claim(s))

- [observation/documented] The agent runtime delegates coding to pluggable coding tools including Claude Code, Codex CLI, Gemini CLI, Kilo Code, and OpenCode, and works with any AI agent that can interact with GitHub. -- evidence: [README.md#L232-L232](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L232-L232), [docs/architecture/ARCHITECTURE.md#L41-L47](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/architecture/ARCHITECTURE.md#L41-L47), [docs/architecture/ARCHITECTURE.md#L29-L29](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/architecture/ARCHITECTURE.md#L29-L29) (`clm_7178427a362ccb00baf48353d2cc6d5efd991bfd8d5335ae143c9014a9c30b69`)

