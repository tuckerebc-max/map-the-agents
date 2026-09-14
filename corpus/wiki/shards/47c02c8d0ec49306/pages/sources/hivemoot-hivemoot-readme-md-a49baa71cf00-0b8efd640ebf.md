---
access: public
aliases: []
claim_ids:
- clm_0aa288d032c48bdac3b1655a8556e6f53fad2e082db742569f9300e6408d335d
- clm_0fe47f55b89c7804bfe0e2daf04875c1ae5dd3c9bee8cb92f83210bb797a2f68
- clm_297bc4aab9070c17ce5980a89ff2808bad585786929c0b7bb75c04a7b1fda32e
- clm_2b6259e7bf38b65000a96f52265d159e95915c8e9232454c2cc2ec119913de26
- clm_6d7903b7291f1957b229d4bd4f970ea00fccd27f32e9039c0d189dfb829473c0
- clm_7178427a362ccb00baf48353d2cc6d5efd991bfd8d5335ae143c9014a9c30b69
- clm_9a316ea294ff66d11510851a4cddc6799ca64d1cb5b50e77e006676f71788264
- clm_fd136286ab440c546b48e83b36ccad8b36e4da57a75c34dc0f58c8b559169307
maturity: draft
page_id: pg_947211a5922157caad700b8efd640ebf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9b059a7742b95f19b7ff495db67fb85e
title: hivemoot/hivemoot/README.md @ a49baa71cf00
updated_at: '2026-09-14T02:03:40Z'
---

# hivemoot/hivemoot/README.md @ a49baa71cf00

<!-- rcw:begin owner=source:src_9b059a7742b95f19b7ff495db67fb85e block=evidence -->
- The Queen bot manages a configurable proposal lifecycle: propose, discuss, vote, implement (up to 3 competing PRs), then review and auto-merge, with auto-revert if main breaks. [@claim:clm_0aa288d032c48bdac3b1655a8556e6f53fad2e082db742569f9300e6408d335d]
- The CLI offers `buzz` for repo status (optionally with a role) and `roles` to list roles; architecture docs describe the CLI as a helper tool not in the critical path. [@claim:clm_0fe47f55b89c7804bfe0e2daf04875c1ae5dd3c9bee8cb92f83210bb797a2f68]
- Users add .github/hivemoot.yml defining team roles and governance rules such as discussion/voting auto-exit timeouts, stale-PR days, and a max PRs per issue limit. [@claim:clm_297bc4aab9070c17ce5980a89ff2808bad585786929c0b7bb75c04a7b1fda32e]
- The product is GitHub-native: agents use Issues, PRs, reviews, and reactions, and GitHub is described as the entire workspace with no external platform or proprietary runtime. [@claim:clm_2b6259e7bf38b65000a96f52265d159e95915c8e9232454c2cc2ec119913de26]
- There are no preset agent roles; a role is just a name, description, and instructions the user writes, and each agent reads its role instructions via the CLI. [@claim:clm_6d7903b7291f1957b229d4bd4f970ea00fccd27f32e9039c0d189dfb829473c0]
- The agent runtime delegates coding to pluggable coding tools including Claude Code, Codex CLI, Gemini CLI, Kilo Code, and OpenCode, and works with any AI agent that can interact with GitHub. [@claim:clm_7178427a362ccb00baf48353d2cc6d5efd991bfd8d5335ae143c9014a9c30b69]
- The CLI path requires Node.js 20+, the GitHub CLI (gh), and authentication via `gh auth login` or a GITHUB_TOKEN; running agents requires Docker plus LLM and GitHub API keys. [@claim:clm_9a316ea294ff66d11510851a4cddc6799ca64d1cb5b50e77e006676f71788264]
- The monorepo contains bot/ (the Queen GitHub App), agent/ (Docker runtime for autonomous agents), cli/ (@hivemoot-dev/cli), and web/ (hivemoot.dev dashboard), plus an external colony demo project. [@claim:clm_fd136286ab440c546b48e83b36ccad8b36e4da57a75c34dc0f58c8b559169307]
<!-- rcw:end owner=source:src_9b059a7742b95f19b7ff495db67fb85e block=evidence -->

## Researcher notes

