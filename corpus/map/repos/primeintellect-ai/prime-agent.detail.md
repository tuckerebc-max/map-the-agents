# primeintellect-ai/prime-agent -- full detail

[Back to orientation](prime-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/primeintellect-ai/prime-agent/1fc1adb6e8062bf871a9b59705c1d15468e589f0/500e7d550bac7429.json](../../../wiki/dossiers/primeintellect-ai/prime-agent/1fc1adb6e8062bf871a9b59705c1d15468e589f0/500e7d550bac7429.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A persistent Python REPL is the built-in model tool; file operations, shell commands, tool use, subagents, and context management all happen through code in that environment. -- evidence: [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52) (`clm_b04524e197dab269ff66e0c843216a1797ccd61b8bf14b515393a8dfa89c6410`)

## design-choices (1 claim(s))

- [observation/documented] Prime Agent is built around two abstractions: a Recursive Language Model that treats context as variables and subagents as function calls in a persistent REPL, and a Continual Harness storing prompts, memories, skills, and subagent specs as durable state. -- evidence: [README.md#L41-L42](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L41-L42), [README.md#L39-L39](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L39-L39) (`clm_e1b89d0f1bd9fb8c0bf46d8ca9695479f2bd9250246977494ab184f583b2cd33`)

## workflows (7 claim(s))

- [observation/documented] Repository development practice: AGENTS.md requires running 'npm run check' after code changes, forbids npm run dev/build/test, and mandates running any created or modified test file until it passes, using the faux provider harness for coding-agent suite tests. -- evidence: [AGENTS.md#L25-L33](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L25-L33) (`clm_eda536769e487f7f55ad542d0a4bdf6ef1f8dcfe1c9d0c0033febbfcb2069107`)
- [observation/documented] Repository development practice: dependency updates are subject to a 7-day minimum release age enforced via .npmrc min-release-age=7 and a matching Dependabot cooldown, with an explicit override flag for urgent security patches. -- evidence: [AGENTS.md#L46-L48](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L46-L48) (`clm_70b43fb7575e858260bd5ffdfb710010c9ddc07fff55009392bf4f487892f316`)
- [observation/documented] Repository development practice: changelog entries are added as fragment files under packages/<pkg>/.changes/ rather than editing CHANGELOG.md directly, and PRs touching package src without a fragment fail CI unless labeled no-changelog. -- evidence: [AGENTS.md#L111-L111](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L111-L111), [CONTRIBUTING.md#L45-L50](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/CONTRIBUTING.md#L45-L50) (`clm_3a103463d5a6d4767b5c300625bdee71a25cc1fd7237eff4073f91752785ac62`)
- [observation/documented] Repository development practice: parallel agents in one worktree must stage only their own files (never git add -A), and destructive operations like git reset --hard, git clean -fd, and commit --no-verify are forbidden. -- evidence: [AGENTS.md#L210-L216](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L210-L216), [AGENTS.md#L222-L227](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L222-L227) (`clm_a6c11274fc4d88ec8234e80fcb71a122220c0dd8ca6197b8fabcafdaa0ec57a8`)
- [observation/documented] Repository development practice: public contributions start in GitHub Discussions; unsolicited pull requests are not reviewed, and PRs are limited to maintainers and explicitly vouched trusted contributors, with unvouched PRs automatically closed. -- evidence: [CONTRIBUTING.md#L27-L27](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/CONTRIBUTING.md#L27-L27), [CONTRIBUTING.md#L3-L3](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/CONTRIBUTING.md#L3-L3), [CONTRIBUTING.md#L5-L5](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/CONTRIBUTING.md#L5-L5), [CONTRIBUTING.md#L29-L29](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/CONTRIBUTING.md#L29-L29) (`clm_3c33ddd33cb35a484a2cb9490e2faec4c8cf4d0dee9eac6761b193656bed4dd8`)
- [observation/documented] Repository development practice: daemon protocol changes must be classified as backward-compatible, capability-gated, or incompatible; incompatible changes require bumping DAEMON_PROTOCOL_VERSION and updating schema revision and compatibility tests. -- evidence: [AGENTS.md#L37-L42](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/AGENTS.md#L37-L42) (`clm_10f22556452cb5352867155618ce28444e071b1faad62052e54f69164c3d7ce5`)
- [observation/documented] Repository development practice: security vulnerabilities must be reported privately to security@primeintellect.ai, never through public Issues, Discussions, or pull requests. -- evidence: [SECURITY.md#L7-L7](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/SECURITY.md#L7-L7), [SECURITY.md#L5-L5](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/SECURITY.md#L5-L5) (`clm_7f85d34bce0cd37760c01d05c9775f0848bbbaf83ccaf0ef70027028aa512740`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are importable Python packages, and a built-in skill creator can turn recurring workflows into project or personal skills. -- evidence: [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52) (`clm_4b0d22519987c8435f5ce90f15786149e6ebaf8d09b5b56fbd843ed2eae7da76`)

## interfaces (2 claim(s))

- [observation/documented] The CLI includes commands such as prime-agent agents, attach, --resume, status, doctor, update, and shutdown for browsing sessions, managing background services, and stopping all agents and workers. -- evidence: [README.md#L78-L86](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L78-L86) (`clm_bbffd5adecbe54708ec900cf447a5058d406c69f88287aad12f40877bb20cd0f`)
- [observation/documented] Documentation references JSON mode and RPC mode for headless automation and integrations, alongside a TUI for interactive use. -- evidence: [README.md#L100-L108](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L100-L108), [README.md#L89-L89](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L89-L89) (`clm_bf49f10a0168185ef7656dc83c2ddee53ca330ce482b4786c2c72acae16608c0`)

## memory-state (1 claim(s))

- [observation/documented] The /refine command reviews the current trajectory and can apply small, evidence-backed updates to supplemental harness state (prompts, memories, skill descriptions, subagent specs), never rewriting the immutable base system prompt, with snapshots supporting rollback. -- evidence: [README.md#L91-L96](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L91-L96), [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52) (`clm_b5b07ce0d0748a7343ff6dbb7bd2aa2090b114eca059631e075abcbf3cd6eee0`)

## orchestration (2 claim(s))

- [observation/documented] rlm.spawn(...) creates real child agents for parallel or background work and returns their results programmatically; running agents can also discover and message each other directly without routing through the user. -- evidence: [README.md#L91-L96](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L91-L96), [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52) (`clm_87edfd5b81ea0ea137590a463c845eaa3fa78c95cd2c38e6406e34f9baed78e5`)
- [observation/documented] Daemon-backed agents keep running when the terminal disconnects and can be reattached; heartbeats, schedules, persistent goals, automatic compaction, and bounded autonomous mode preserve progress across turns. -- evidence: [README.md#L91-L96](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L91-L96), [README.md#L46-L52](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L46-L52) (`clm_0843c43cea0f7f996fc3b06433579df628af2ddbe539b6c955859f959f4df2d7`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The installer requires HTTPS for release downloads and verifies the archive against the release origin's SHA-256 inventory; the README notes HTTPS itself is the authenticity boundary since inventory and archive share an origin. -- evidence: [README.md#L62-L62](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L62-L62) (`clm_0b941c6f97c66cb7d9beb6a957b1a2ff36f5da1485463d1811a7381500b2ef3a`)
- [observation/documented] The agent and TUI are built on top of the open-source 'pi' project, which the README acknowledges. -- evidence: [README.md#L118-L118](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L118-L118) (`clm_c3b729945ed711ee85cd235743e325bd06bb55af181f7279ab969c0fb5c7c5b9`)

## limitations (1 claim(s))

- [observation/documented] The README warns that Prime Agent executes model-generated Python and project commands with the user's permissions; worker and kernel processes improve lifecycle isolation but are not a security sandbox. -- evidence: [README.md#L73-L74](https://github.com/PrimeIntellect-ai/prime-agent/blob/1fc1adb6e8062bf871a9b59705c1d15468e589f0/README.md#L73-L74) (`clm_5d063fda099910beb7928a5bcaa44ea620041349f2e50eb321101157d5ffc111`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

