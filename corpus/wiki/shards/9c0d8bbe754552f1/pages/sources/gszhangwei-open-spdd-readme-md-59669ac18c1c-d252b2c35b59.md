---
access: public
aliases: []
claim_ids:
- clm_2403e05eb1cd79ad1144e1ba98887f4d940741d142920e26c49898d8fb42d697
- clm_25d241e423f3b63ba40541ead00be523410d682c2b5c115cdd2352028b9c3f3e
- clm_26d340e4a7e8a083ae281fa2dff787df5615b1e54c08d11430dcb41fa6fa3dee
- clm_350faa9514b4a1dee56052eb15efa092fbe539cd5b85bb8f5d3c1ea13c918caf
- clm_555964487ad8ec88bd7062d648c2a9ba3ccd90b821ce1700b27bfc8b77570758
- clm_9f20e03f6131c60c6754ed4ad5fa7c154cf294cbd5744b7463ef52ac821f0601
- clm_cd3f4e9d6e9e1327e6093b81d24c929a2a4ae408cb03ab52303263caace958ac
- clm_d47d422b246e25bd9cb9122ccffcdc1e04aef697f6039254b7ee83c6b8fae3f3
- clm_e9bf170ad00901d1aa623bf9829e79978d02481c55518939be917b03ba767ad3
- clm_ecd7c5f79fef260c23ef913f74b0c30ef6cf0c20b7f75f8a4f49ea47f7ac0031
maturity: draft
page_id: pg_3a6d0a2292015a91ab0cd252b2c35b59
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ff434ac5c8505e7791fcd5e68a7c580b
title: gszhangwei/open-spdd/README.md @ 59669ac18c1c
updated_at: '2026-09-14T03:55:08Z'
---

# gszhangwei/open-spdd/README.md @ 59669ac18c1c

<!-- rcw:begin owner=source:src_ff434ac5c8505e7791fcd5e68a7c580b block=evidence -->
- The uninstall command detects the install method (Homebrew or go install), prints a plan, requires confirmation by default, and refuses to act on unclassifiable installs such as manually copied binaries. [@claim:clm_2403e05eb1cd79ad1144e1ba98887f4d940741d142920e26c49898d8fb42d697]
- The tool auto-detects the user's AI coding environment and writes command templates into tool-specific directories, e.g. .cursor/commands/, .claude/commands/, .github/copilot-prompts/, and .agents/skills/ for Codex. [@claim:clm_25d241e423f3b63ba40541ead00be523410d682c2b5c115cdd2352028b9c3f3e]
- Generated OpenCode command files intentionally omit frontmatter name fields to avoid command alias conflicts in OpenCode. [@claim:clm_26d340e4a7e8a083ae281fa2dff787df5615b1e54c08d11430dcb41fa6fa3dee]
- Repository development practice: contributors run tests with go test ./tests/..., with verbose and per-module variants like ./tests/detector/... and ./tests/templates/..., and can build from source with go build ./cmd/openspdd. [@claim:clm_350faa9514b4a1dee56052eb15efa092fbe539cd5b85bb8f5d3c1ea13c918caf]
- The methodology centers on a 7-dimension REASONS Canvas (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards) treating prompts as executable design contracts rather than task lists. [@claim:clm_555964487ad8ec88bd7062d648c2a9ba3ccd90b821ce1700b27bfc8b77570758]
- For Codex, skills are generated as project-scoped SKILL.md bundles under .agents/skills/ with implicit invocation disabled by default, opt-in via --allow-implicit. [@claim:clm_9f20e03f6131c60c6754ed4ad5fa7c154cf294cbd5744b7463ef52ac821f0601]
- The tool is written in Go and installable via Homebrew (gszhangwei/tools/openspdd), go install from cmd/openspdd, a scripts/install.sh script, or prebuilt GitHub Releases binaries. [@claim:clm_cd3f4e9d6e9e1327e6093b81d24c929a2a4ae408cb03ab52303263caace958ac]
- On some Codex versions, skills from untrusted projects are silently ignored; users must mark the project trusted in ~/.codex/config.toml or restart Codex if skills do not appear. [@claim:clm_d47d422b246e25bd9cb9122ccffcdc1e04aef697f6039254b7ee83c6b8fae3f3]
- All templates are embedded in a single Go binary via Go's embed directive, and the tool provides an interactive terminal UI for command selection. [@claim:clm_e9bf170ad00901d1aa623bf9829e79978d02481c55518939be917b03ba767ad3]
- The project targets AI-assisted business development where design-intent drift causes rework, recommending itself for enterprise features, team collaboration, and complex refactoring, but not for one-off scripts. [@claim:clm_ecd7c5f79fef260c23ef913f74b0c30ef6cf0c20b7f75f8a4f49ea47f7ac0031]
<!-- rcw:end owner=source:src_ff434ac5c8505e7791fcd5e68a7c580b block=evidence -->

## Researcher notes

