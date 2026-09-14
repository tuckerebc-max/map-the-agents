# harnessworks/harness-starter-kit -- full detail

[Back to orientation](harness-starter-kit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/harnessworks/harness-starter-kit/62437bec264b2deed83353e8209660d645e86828/08418ac572a3a2e1.json](../../../wiki/dossiers/harnessworks/harness-starter-kit/62437bec264b2deed83353e8209660d645e86828/08418ac572a3a2e1.json)

## specifications (1 claim(s))

- [observation/documented] Harness Starter Kit is described as a prompt-first starter kit that converts repeated coding-agent mistakes into durable repository instructions, checks, memory, and evaluation. -- evidence: [README.md#L43-L44](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L43-L44) (`clm_a5bf0d2bcb8d190c2c4d8b5ce42425431c315f7b3b338d59ef4f0e5b4f17164f`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Adoption is agent-driven rather than an automatic installer: the agent inspects the target repo first and applies only the smallest useful set of harness artifacts, following documented workflow and prompt files. -- evidence: [README.md#L267-L272](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L267-L272) (`clm_3ccc75abee1b4f0e36a22b25efafaa3b9dccb963b40f9ca03c317709a8e2e136`)

## workflows (2 claim(s))

- [observation/documented] The adoption prompt instructs the agent to treat the working directory as the target repo, treat the cloned kit as read-only reference, inspect before editing, preserve existing architecture and conventions, and add only minimal harness pieces. -- evidence: [README.md#L80-L111](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L80-L111) (`clm_5f3de0cc38e94546acbfed22f1fb44951901ab905808f8c53a90d4d1dbd2a4d3`)
- [observation/documented] The expected adoption outcome includes a project-specific AGENTS.md, a knowledge store if none exists, lightweight drift checks from the repo's real rules, local verification commands, and an adoption report covering changes, checks, assumptions, failure memory, and gate placement. -- evidence: [README.md#L113-L122](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L113-L122) (`clm_801686245ff566ef93f961a193ebc759f8c7e25be9e4a3a9417941926e7a01c6`)

## skills-patterns (1 claim(s))

- [observation/documented] Besides prompt-first workflows, the same workflows are published as runtime-native skills for Codex and Claude Code, with the source package in agent-skills/ and packaging details in docs/agent-skills-package.md. -- evidence: [README.md#L258-L260](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L258-L260), [README.md#L193-L194](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L193-L194) (`clm_23d93f19f5ecee94534d13459a6bf5290ff95d3e5741b6a78fb5d88242a367a5`)

## interfaces (2 claim(s))

- [observation/documented] The /harness command names are prompt conventions typed into the coding agent chat by default, not built-in editor commands; they appear in editor command palettes only if matching custom slash commands are added separately. -- evidence: [README.md#L160-L163](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L160-L163) (`clm_38997cc2cbfdf3af116309a974924e2ed062adc0dd571e4d2788ef07a5326843`)
- [observation/documented] The kit exposes five stage-based commands: doctor (inspect without modifying), adopt (apply minimal harness pieces), review (challenge the diff pre-commit/PR), update (bring in a newer kit reference), and refresh (clean stale or duplicated guidance). -- evidence: [README.md#L178-L182](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L178-L182), [README.md#L167-L174](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L167-L174) (`clm_1ccc18ddd8e68cae3e4fd2ee444bd05a08319444c6afe30d6dfb3c14dc1ab9ce`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The /harness review sub-agent request is treated as explicit permission to use a read-only reviewer subagent when the active runtime and tool instructions permit it; if unavailable, blocked, or failed, the fallback reason must be reported. -- evidence: [README.md#L80-L111](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L80-L111) (`clm_cd85e72fd579803ed8b1f0f2ac90932cb7b9f8edbe8cf3b886f3a7dfd6ac431e`)

## evaluation (1 claim(s))

- [observation/documented] The kit ships evaluation materials (docs/evaluation.md, an effectiveness-report template, and a task-outcome.yaml template) for measuring comparable tasks, wrong-file edits, first-pass verification, and human rework. -- evidence: [README.md#L294-L302](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L294-L302) (`clm_756a693a35619ad8f58aa2e7c0f823f7a0c150d473794119b3fc5ff0d37131e6`)

## dependencies (2 claim(s))

- [observation/documented] Codex installation uses the harnessworks/harness-agent-skills-marketplace plugin marketplace pinned at ref v0.1.16, followed by installing harness-agent-skills from the Harnessworks marketplace. -- evidence: [README.md#L202-L203](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L202-L203), [README.md#L198-L200](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L198-L200) (`clm_c4c409dcea5aa28520bf1df18e337500d0b2ddf7349cc920cbbdb7ea65dbd8b1`)
- [observation/documented] Claude Code installation adds the harness-agent-skills-marketplace at v0.1.16 and installs harness-agent-skills@harnessworks, invoked via /harness-agent-skills:harness router commands. -- evidence: [README.md#L230-L233](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L230-L233), [README.md#L237-L241](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L237-L241) (`clm_2a3fbe1163656d653457f9ec061f6c77f3c4581ffbf630e1e922f0de094f116f`)

## limitations (2 claim(s))

- [observation/documented] The README states Harness Doctor can scan for durable repository evidence but cannot prove agents make fewer mistakes; harness health and agent effectiveness must be measured separately via task outcomes and effectiveness reports. -- evidence: [README.md#L148-L152](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L148-L152) (`clm_5ed7bc6629a7e07827f2433dbf8087b5df48136011956343c8b0ce94dba3c559`)
- [observation/documented] The included dogfood reports (TodayBus for a Next.js target and Harness ERP for a Spring/Maven backend) are harnessed-only benchmarks and, per the README, do not prove effectiveness improvement. -- evidence: [README.md#L304-L309](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L304-L309) (`clm_fd507364b8f1e4ee88f7ed4f8140b78a5483457ef39af2ab55cb21ddaba326ec`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

