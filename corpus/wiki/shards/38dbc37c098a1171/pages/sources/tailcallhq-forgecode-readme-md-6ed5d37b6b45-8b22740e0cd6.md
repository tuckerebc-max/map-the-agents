---
access: public
aliases: []
claim_ids:
- clm_20b964b3e76d851fb1fcfd85f488979d80bbc95875c5100470954859e7f0b5c4
- clm_3861d5a22a6c88efa87845a0c544d50f002718a8d5ae5a3efc908de55bb17ec4
- clm_63c6684620c3edef5abc70c6d274ba1986b5399718bce932487eb6db38171d88
- clm_760767ae7361238213423d8c9fd3c539ed9b1a52e4fc3a22044246be1411e5ac
- clm_84ce517c7889f3d9cf0a500e21f71aecd229b6006c6fd5343e52e5447bc02871
- clm_afeb94b0df1aaac24101f533caf2bc09e5af06555cf2eb163958e01a2edd0beb
- clm_b80e64f38b5b5ecf24bc6dba76d973d572993c34900d0492430db8fd6338bc78
- clm_c074c1b4f134270e88d652bcfae3a779a97701e4cb973ec36939ba7c6f604e9a
- clm_e459e4540b6c1b7673d9cd35c10a7007344344a46d64b9128540fb56b4cde3cd
- clm_f0140789189621e9dab2dfccadbf5d4a1209ebe1553fe60507177cab63b2c6ac
- clm_f51e814cd487576af7026d87efe3a88626c600c4f1e7c25d2b9731539f82e14a
- clm_fc0973587d6198a66c2aeda157be7951f1ee1152bc0e23260669bccfc289624d
maturity: draft
page_id: pg_e1b1b49c931c59039e888b22740e0cd6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f03d08a8698757a7bbc313c18ce01953
title: tailcallhq/forgecode/README.md @ 6ed5d37b6b45
updated_at: '2026-09-14T03:17:48Z'
---

# tailcallhq/forgecode/README.md @ 6ed5d37b6b45

<!-- rcw:begin owner=source:src_f03d08a8698757a7bbc313c18ce01953 block=evidence -->
- Semantic search indexes the codebase via `:sync`/`forge workspace sync`, sending file content to a workspace server defaulting to https://api.forgecode.dev, overridable with FORGE_WORKSPACE_SERVER_URL. [@claim:clm_20b964b3e76d851fb1fcfd85f488979d80bbc95875c5100470954859e7f0b5c4]
- The README describes a restricted shell mode that limits file system access and prevents unintended changes as part of Forge's security design. [@claim:clm_3861d5a22a6c88efa87845a0c544d50f002718a8d5ae5a3efc908de55bb17ec4]
- Forge ships three built-in agents: `forge` (implementation, modifies files), `sage` (read-only research), and `muse` (planning, writes plans to `plans/`). [@claim:clm_63c6684620c3edef5abc70c6d274ba1986b5399718bce932487eb6db38171d88]
- An AGENTS.md file in the project root or `~/forge/AGENTS.md` gives agents persistent instructions, and Forge reads it automatically at the start of every conversation. [@claim:clm_760767ae7361238213423d8c9fd3c539ed9b1a52e4fc3a22044246be1411e5ac]
- Custom skills are SKILL.md files with YAML front-matter, resolved with precedence: project-local `.forge/skills/` over global `~/forge/skills/` over built-in skills embedded in the binary. [@claim:clm_84ce517c7889f3d9cf0a500e21f71aecd229b6006c6fd5343e52e5447bc02871]
- CLI options include `-p` for direct prompts, `--agent` to pick an agent, `-C` to change directory, `--sandbox` to create an isolated git worktree plus branch, and `--conversation-id` to resume a conversation. [@claim:clm_afeb94b0df1aaac24101f533caf2bc09e5af06555cf2eb163958e01a2edd0beb]
- Using `.env` files for provider configuration is deprecated and slated for removal; environment-variable credentials are still supported for backward compatibility and are auto-migrated to file-based storage on first run. [@claim:clm_b80e64f38b5b5ecf24bc6dba76d973d572993c34900d0492430db8fd6338bc78]
- Forge saves every conversation and provides commands to list, resume, clone, rename, delete, dump as JSON/HTML, compact, and retry conversations, including toggling to the previous one. [@claim:clm_c074c1b4f134270e88d652bcfae3a779a97701e4cb973ec36939ba7c6f604e9a]
- Three built-in skills ship with Forge: create-skill, execute-plan, and github-pr-description; skills are reusable workflows the AI can invoke as tools. [@claim:clm_e459e4540b6c1b7673d9cd35c10a7007344344a46d64b9128540fb56b4cde3cd]
- Forge offers three usage modes: an interactive terminal UI launched by running `forge` with no arguments, a one-shot CLI mode via `-p`/`--prompt`, and a ZSH plugin mode using `:` prefix commands. [@claim:clm_f0140789189621e9dab2dfccadbf5d4a1209ebe1553fe60507177cab63b2c6ac]
- Repository development practice: the README badges indicate a CI workflow (ci.yml), GitHub releases, a Discord community, and CLA assistant for contributions. [@claim:clm_f51e814cd487576af7026d87efe3a88626c600c4f1e7c25d2b9731539f82e14a]
- Forge supports MCP servers with subcommands to list, import, show, remove, and reload configured servers. [@claim:clm_fc0973587d6198a66c2aeda157be7951f1ee1152bc0e23260669bccfc289624d]
<!-- rcw:end owner=source:src_f03d08a8698757a7bbc313c18ce01953 block=evidence -->

## Researcher notes

