---
access: public
aliases: []
claim_ids:
- clm_1ccc18ddd8e68cae3e4fd2ee444bd05a08319444c6afe30d6dfb3c14dc1ab9ce
- clm_23d93f19f5ecee94534d13459a6bf5290ff95d3e5741b6a78fb5d88242a367a5
- clm_2a3fbe1163656d653457f9ec061f6c77f3c4581ffbf630e1e922f0de094f116f
- clm_38997cc2cbfdf3af116309a974924e2ed062adc0dd571e4d2788ef07a5326843
- clm_3ccc75abee1b4f0e36a22b25efafaa3b9dccb963b40f9ca03c317709a8e2e136
- clm_5ed7bc6629a7e07827f2433dbf8087b5df48136011956343c8b0ce94dba3c559
- clm_5f3de0cc38e94546acbfed22f1fb44951901ab905808f8c53a90d4d1dbd2a4d3
- clm_756a693a35619ad8f58aa2e7c0f823f7a0c150d473794119b3fc5ff0d37131e6
- clm_801686245ff566ef93f961a193ebc759f8c7e25be9e4a3a9417941926e7a01c6
- clm_a5bf0d2bcb8d190c2c4d8b5ce42425431c315f7b3b338d59ef4f0e5b4f17164f
- clm_c4c409dcea5aa28520bf1df18e337500d0b2ddf7349cc920cbbdb7ea65dbd8b1
- clm_cd85e72fd579803ed8b1f0f2ac90932cb7b9f8edbe8cf3b886f3a7dfd6ac431e
- clm_fd507364b8f1e4ee88f7ed4f8140b78a5483457ef39af2ab55cb21ddaba326ec
maturity: draft
page_id: pg_95e81da1f45a552c9468c77b2bd2e4b4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cae2eac77aff596698f4668cb7179d45
title: harnessworks/harness-starter-kit/README.md @ 62437bec264b
updated_at: '2026-09-14T03:56:29Z'
---

# harnessworks/harness-starter-kit/README.md @ 62437bec264b

<!-- rcw:begin owner=source:src_cae2eac77aff596698f4668cb7179d45 block=evidence -->
- The kit exposes five stage-based commands: doctor (inspect without modifying), adopt (apply minimal harness pieces), review (challenge the diff pre-commit/PR), update (bring in a newer kit reference), and refresh (clean stale or duplicated guidance). [@claim:clm_1ccc18ddd8e68cae3e4fd2ee444bd05a08319444c6afe30d6dfb3c14dc1ab9ce]
- Besides prompt-first workflows, the same workflows are published as runtime-native skills for Codex and Claude Code, with the source package in agent-skills/ and packaging details in docs/agent-skills-package.md. [@claim:clm_23d93f19f5ecee94534d13459a6bf5290ff95d3e5741b6a78fb5d88242a367a5]
- Claude Code installation adds the harness-agent-skills-marketplace at v0.1.16 and installs harness-agent-skills@harnessworks, invoked via /harness-agent-skills:harness router commands. [@claim:clm_2a3fbe1163656d653457f9ec061f6c77f3c4581ffbf630e1e922f0de094f116f]
- The /harness command names are prompt conventions typed into the coding agent chat by default, not built-in editor commands; they appear in editor command palettes only if matching custom slash commands are added separately. [@claim:clm_38997cc2cbfdf3af116309a974924e2ed062adc0dd571e4d2788ef07a5326843]
- Adoption is agent-driven rather than an automatic installer: the agent inspects the target repo first and applies only the smallest useful set of harness artifacts, following documented workflow and prompt files. [@claim:clm_3ccc75abee1b4f0e36a22b25efafaa3b9dccb963b40f9ca03c317709a8e2e136]
- The README states Harness Doctor can scan for durable repository evidence but cannot prove agents make fewer mistakes; harness health and agent effectiveness must be measured separately via task outcomes and effectiveness reports. [@claim:clm_5ed7bc6629a7e07827f2433dbf8087b5df48136011956343c8b0ce94dba3c559]
- The adoption prompt instructs the agent to treat the working directory as the target repo, treat the cloned kit as read-only reference, inspect before editing, preserve existing architecture and conventions, and add only minimal harness pieces. [@claim:clm_5f3de0cc38e94546acbfed22f1fb44951901ab905808f8c53a90d4d1dbd2a4d3]
- The kit ships evaluation materials (docs/evaluation.md, an effectiveness-report template, and a task-outcome.yaml template) for measuring comparable tasks, wrong-file edits, first-pass verification, and human rework. [@claim:clm_756a693a35619ad8f58aa2e7c0f823f7a0c150d473794119b3fc5ff0d37131e6]
- The expected adoption outcome includes a project-specific AGENTS.md, a knowledge store if none exists, lightweight drift checks from the repo's real rules, local verification commands, and an adoption report covering changes, checks, assumptions, failure memory, and gate placement. [@claim:clm_801686245ff566ef93f961a193ebc759f8c7e25be9e4a3a9417941926e7a01c6]
- Harness Starter Kit is described as a prompt-first starter kit that converts repeated coding-agent mistakes into durable repository instructions, checks, memory, and evaluation. [@claim:clm_a5bf0d2bcb8d190c2c4d8b5ce42425431c315f7b3b338d59ef4f0e5b4f17164f]
- Codex installation uses the harnessworks/harness-agent-skills-marketplace plugin marketplace pinned at ref v0.1.16, followed by installing harness-agent-skills from the Harnessworks marketplace. [@claim:clm_c4c409dcea5aa28520bf1df18e337500d0b2ddf7349cc920cbbdb7ea65dbd8b1]
- The /harness review sub-agent request is treated as explicit permission to use a read-only reviewer subagent when the active runtime and tool instructions permit it; if unavailable, blocked, or failed, the fallback reason must be reported. [@claim:clm_cd85e72fd579803ed8b1f0f2ac90932cb7b9f8edbe8cf3b886f3a7dfd6ac431e]
- The included dogfood reports (TodayBus for a Next.js target and Harness ERP for a Spring/Maven backend) are harnessed-only benchmarks and, per the README, do not prove effectiveness improvement. [@claim:clm_fd507364b8f1e4ee88f7ed4f8140b78a5483457ef39af2ab55cb21ddaba326ec]
<!-- rcw:end owner=source:src_cae2eac77aff596698f4668cb7179d45 block=evidence -->

## Researcher notes

