---
access: public
aliases: []
claim_ids:
- clm_090d7ba6aace523cc012b625ea653f96f6fdefb3e480064748b7f260ba8a6bf4
- clm_237bb214a120db62f18f37f0ce3d8441c4cc38d3d4e8f5ee302771f8ef008b9f
- clm_2ed9ba23f17ddc20849fc9047515cdcffbdec3b18bc9ce8f93ff7a408afade1b
- clm_4b0dd74d164e45d121a5fc9927ef055d5f5eb5c77446f71deab2b378e39722fc
- clm_8317142fd9228a982dcdfe7b990c2471db09c8c05f0be94eb28f83076f04b871
- clm_84bbdb21091952122b79b586d18a485f7c850aaeda3a11a5605ebbb28fef2d89
- clm_8524fb1b262679e3fac671019cd367fd0d69680faf901154f15bf6ce77e7f856
- clm_873544ab4ac9bced1a9d81bc9e86088baf051f80e0ec65b1cd1d6f5f59c9bfd2
- clm_9a8da15adaa4c4cf4254aec05b68ff86678c6f4557b33f58641dd211e3af2c14
- clm_dca220d4e9a1e4aa481d33e90b5d416ee54dcf72048b5889e9c26f6ff669613a
- clm_ebab8a19ea9bb1f24897b6cc00b85303329a790a21b4e4e24c1d0ee80829faf3
- clm_f5eea402cf66e85fe3a35855ce71c966c67f9fdaa4800195c1a8b7b05e6607d5
maturity: draft
page_id: pg_499c1f89e3785e5e9cbceed8619d1463
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_19bc9bacb4c45f59996178d8d573d3cf
title: aeonfun/aeon/docs/ADK.md @ 95142d19705c
updated_at: '2026-09-14T01:29:55Z'
---

# aeonfun/aeon/docs/ADK.md @ 95142d19705c

<!-- rcw:begin owner=source:src_19bc9bacb4c45f59996178d8d573d3cf block=evidence -->
- workflow_dispatch returns 204 with no run id, so integrators must either poll the runs list by dispatch time or subscribe to the workflow_run webhook for exact correlation. [@claim:clm_090d7ba6aace523cc012b625ea653f96f6fdefb3e480064748b7f260ba8a6bf4]
- The ADK auth pattern uses three credentials: a user OAuth token (no scope param, since permissions come from the App definition), an App JWT used only to mint installation tokens, and a ~1h installation token scoped to one installation's repos. [@claim:clm_237bb214a120db62f18f37f0ce3d8441c4cc38d3d4e8f5ee302771f8ef008b9f]
- On-demand skill runs go through a single aeon.yml workflow accepting workflow_dispatch inputs: skill (required, regex-checked), var, model (must match a choice option or GitHub returns 422), and harness (claude default or grok). [@claim:clm_2ed9ba23f17ddc20849fc9047515cdcffbdec3b18bc9ce8f93ff7a408afade1b]
- catalog/skills.json is the machine-readable skill catalog; each entry carries a slug, description, category, a single universal var input, required env keys, and needed MCP servers. [@claim:clm_4b0dd74d164e45d121a5fc9927ef055d5f5eb5c77446f71deab2b378e39722fc]
- The ADK recommends a GitHub App over personal access tokens: no credential custody, least-privilege fixed permissions, instant revocation on uninstall, and free multi-tenancy since GitHub tracks installations. [@claim:clm_8317142fd9228a982dcdfe7b990c2471db09c8c05f0be94eb28f83076f04b871]
- Repository development practice: pack authors can pre-flight locally with scripts/validate-pack.sh from an Aeon checkout, and listing requires a PR adding a README Community Packs row plus a catalog/skill-packs.json entry. [@claim:clm_84bbdb21091952122b79b586d18a485f7c850aaeda3a11a5605ebbb28fef2d89]
- A skill is a single Markdown file with frontmatter (name, description, category, requires, var, mode) plus a prompt; there is no plugin API or compilation step. [@claim:clm_8524fb1b262679e3fac671019cd367fd0d69680faf901154f15bf6ce77e7f856]
- Tenant isolation requires re-verifying with the user's token on every request that they still have access to the stored installation/repo, because otherwise any authenticated user could drive someone else's agent. [@claim:clm_873544ab4ac9bced1a9d81bc9e86088baf051f80e0ec65b1cd1d6f5f59c9bfd2]
- The instance needs at least one model credential (CLAUDE_CODE_OAUTH_TOKEN, ANTHROPIC_API_KEY, or an LLM gateway key), resolved by prefix with auto-cascading. [@claim:clm_9a8da15adaa4c4cf4254aec05b68ff86678c6f4557b33f58641dd211e3af2c14]
- An Aeon instance is a GitHub repo plus GitHub Actions with no Aeon server or API; integrators read/write files and dispatch workflows via GitHub APIs such as Contents, Actions Secrets, and workflow_dispatch. [@claim:clm_dca220d4e9a1e4aa481d33e90b5d416ee54dcf72048b5889e9c26f6ff669613a]
- GitHub delivers only about 10% of 5-minute schedule ticks; the scheduler also accepts repository_dispatch type cron-tick so a backend can act as an uptime pinger, with a debt model preventing double-firing. [@claim:clm_ebab8a19ea9bb1f24897b6cc00b85303329a790a21b4e4e24c1d0ee80829faf3]
- Skill packs are published in their own repo with a skills-pack.json manifest; the installer security-scans each SKILL.md, records provenance in skills.lock, and registers skills disabled so the operator remains the trust boundary. [@claim:clm_f5eea402cf66e85fe3a35855ce71c966c67f9fdaa4800195c1a8b7b05e6607d5]
<!-- rcw:end owner=source:src_19bc9bacb4c45f59996178d8d573d3cf block=evidence -->

## Researcher notes

