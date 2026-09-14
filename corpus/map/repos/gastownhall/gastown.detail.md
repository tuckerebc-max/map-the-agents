# gastownhall/gastown -- full detail

[Back to orientation](gastown.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/gastownhall/gastown/649b832b7672bc7a2dbef26f5983aba6198b819b/46e632c92880ab13.json](../../../wiki/dossiers/gastownhall/gastown/649b832b7672bc7a2dbef26f5983aba6198b819b/46e632c92880ab13.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture includes a Mayor AI coordinator, a Town workspace directory (e.g. ~/gt/), per-project Rigs wrapping git repositories, and Polecats (worker agents with persistent identity but ephemeral sessions). -- evidence: [README.md#L58-L58](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L58-L58), [README.md#L66-L66](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L66-L66), [README.md#L54-L54](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L54-L54), [README.md#L50-L50](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L50-L50) (`clm_59af9cd3cecf2693aff698db0088b64986e4c6b9f26915b68ac863c0cf0e2463`)

## design-choices (2 claim(s))

- [observation/documented] A stated key design principle is loose coupling: Gas Town orchestrates agents through tmux and environment variables, without importing or linking agent libraries — integration is configuration, not compilation. -- evidence: [docs/agent-provider-integration.md#L23-L26](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L23-L26) (`clm_66a13df9cd4a483f69646b172d92ae151b9cac8398b47c67c273da04d44e7669`)
- [observation/documented] Agent provider integration is tiered: Tier 0 is zero-change tmux orchestration via send-keys and capture-pane, Tier 1 is a JSON preset in agents.json, Tier 2 adds hooks, and Tier 3 is deep native API integration. -- evidence: [docs/agent-provider-integration.md#L49-L52](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L49-L52), [docs/agent-provider-integration.md#L30-L35](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L30-L35), [docs/agent-provider-integration.md#L46-L47](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L46-L47) (`clm_6a7ee3f54121c1a2f058a35b05b3d797fe691568dc74221b65388832be43bf0a`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Bead/issue IDs use a prefix plus 5-character alphanumeric format (e.g. gt-abc12), where the prefix indicates the item's origin or rig; commands like gt sling and gt convoy accept these IDs. -- evidence: [README.md#L80-L80](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L80-L80) (`clm_2676378cc7e03582cdae0c5f020d09cf4c83a85a3be246d134217e3bca93b898`)
- [observation/documented] Runtime configuration is per-rig via settings/config.json with provider, command, args, and prompt_mode fields; built-in agent presets include claude, gemini, codex, kiro, cursor, auggie, amp, opencode, copilot, pi, and omp. -- evidence: [README.md#L507-L507](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L507-L507), [README.md#L458-L467](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L458-L467), [README.md#L456-L456](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L456-L456) (`clm_7d899e87a142e781f732b7f26b82c1906cf2104826e33347f74edc2bf452d1ca`)

## memory-state (1 claim(s))

- [observation/documented] Agent work state persists in git worktree-based 'Hooks' storage that survives crashes and restarts, and work items are stored in the Beads ledger, a git-backed issue tracking system. -- evidence: [README.md#L7-L7](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L7-L7), [README.md#L70-L70](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L70-L70), [README.md#L78-L78](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L78-L78) (`clm_1a6749db0581f421d4787ce29ab192635df42fcb68d2d0d582f2274f0075072a`)

## orchestration (2 claim(s))

- [observation/documented] A three-tier watchdog system keeps agents healthy: per-rig Witnesses monitor polecats and trigger recovery, the Deacon runs continuous patrol cycles across rigs, and Dogs are dispatched for maintenance tasks like triage. -- evidence: [README.md#L88-L88](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L88-L88), [README.md#L633-L633](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L633-L633), [README.md#L90-L92](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L90-L92), [README.md#L637-L637](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L637-L637) (`clm_7b80926cc27e77495d454099cf1d7d29ea782c9feb2c5952542f0cc9d9213ffa`)
- [observation/documented] The Refinery is a per-rig Bors-style merge queue: polecats run 'gt done' to create MR beads, the Refinery batches them, runs verification gates, and bisects failing batches; polecats never push directly to main. -- evidence: [README.md#L96-L96](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L96-L96), [README.md#L661-L661](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L661-L661), [README.md#L655-L659](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L655-L659) (`clm_40c914724c4bf780f0fcd63e00b4e037ff5f33902350ea7a31aeb8f05dd137d2`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Native installs require Git 2.20+, Go 1.26.2+ (per go.mod), Beads (bd) 0.57.0+, sqlite3, ICU4C dev headers for source builds, tmux 3.0+ for tmux-backed roles, and a Claude Code CLI as the default runtime; Docker installs only need Docker Compose. -- evidence: [README.md#L127-L127](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L127-L127), [README.md#L129-L137](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L129-L137) (`clm_212bd080fbc62bc3b785f35d5e97905a6f69ddd6a4a7653cc55e219cfae559de`)
- [observation/documented] The Wasteland federated coordination network links Gas Towns through DoltHub, and Dolt is a prerequisite on the Linux and Windows install paths. -- evidence: [README.md#L117-L117](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L117-L117), [README.md#L690-L690](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L690-L690), [README.md#L164-L164](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L164-L164), [README.md#L180-L180](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L180-L180) (`clm_ef23240f603528346092a158f01701f68925cd9728ad36cbe889cb804e3c7bbd`)

## limitations (1 claim(s))

- [observation/documented] The Tier 0 tmux shim layer is described as timing-sensitive with no delivery confirmation, lacking session resume, automatic context injection, and process-name detection compared to higher integration tiers. -- evidence: [docs/agent-provider-integration.md#L57-L61](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L57-L61), [docs/agent-provider-integration.md#L54-L55](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L54-L55) (`clm_950caac5142aeebb46830f211e4cb125520b8c743b587497c4e2ecb340a01b83`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

