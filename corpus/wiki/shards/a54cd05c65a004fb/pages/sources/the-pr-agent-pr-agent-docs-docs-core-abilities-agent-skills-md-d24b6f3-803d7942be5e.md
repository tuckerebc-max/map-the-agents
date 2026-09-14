---
access: public
aliases: []
claim_ids:
- clm_0c0562a4b7ea69a1b4fb73240a06fe56a04021739851f9883684dc7b67566a64
- clm_1f642a8b20b4c16442496d356e6c8b9a98f08ce6e6b1c36742583cec868cf31b
- clm_56a80641befb4b89feccbff5575c0bacc1720455b2a25aefdeb61daffc65d8ca
- clm_5d2a7d1e95113ebcbe914a5e8a694f4624d007c914b54c5939dc2ebe42da071c
maturity: draft
page_id: pg_e241a735f30d528da7dd803d7942be5e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_37f82d16035951cfb0aa4b38872f0ef3
title: The-PR-Agent/pr-agent/docs/docs/core-abilities/agent_skills.md @ d24b6f36e787
updated_at: '2026-09-14T04:25:33Z'
---

# The-PR-Agent/pr-agent/docs/docs/core-abilities/agent_skills.md @ d24b6f36e787

<!-- rcw:begin owner=source:src_37f82d16035951cfb0aa4b38872f0ef3 block=evidence -->
- When enabled, PR-Agent discovers SKILL.md files under configured paths and injects each skill's name, description, and body into the /review, /improve, /describe, and top-level /ask prompts alongside extra_instructions. [@claim:clm_0c0562a4b7ea69a1b4fb73240a06fe56a04021739851f9883684dc7b67566a64]
- skills.paths is host-level only: it cannot be set from a repository's .pr_agent.toml, and repo-supplied values are ignored with a warning, to prevent malicious repos from pointing the scan at sensitive host files. [@claim:clm_1f642a8b20b4c16442496d356e6c8b9a98f08ce6e6b1c36742583cec868cf31b]
- Agent Skills use a SKILL.md format: a directory with a markdown file whose YAML frontmatter carries name and description, followed by a markdown body of review guidance. [@claim:clm_56a80641befb4b89feccbff5575c0bacc1720455b2a25aefdeb61daffc65d8ca]
- Because PR-Agent makes single-shot model calls with no tool-use loop, the agent-skills progressive-disclosure model is not implementable; all enabled skill text is loaded into every prompt (bounded by max_skills_tokens), and skills needing script execution or binary assets will not work. [@claim:clm_5d2a7d1e95113ebcbe914a5e8a694f4624d007c914b54c5939dc2ebe42da071c]
<!-- rcw:end owner=source:src_37f82d16035951cfb0aa4b38872f0ef3 block=evidence -->

## Researcher notes

