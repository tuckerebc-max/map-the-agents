---
access: public
aliases: []
claim_ids:
- clm_152c56215d1894fa60d554233b33b3f5605e1b245e39c626728bc9b33efef897
- clm_34d8a3e68972ad2f117a1955c44f84c3e4e9c1e2d96966c3fac155180fda3e96
- clm_4aae6828c37d27a354b50839a7007d5bb59496d84f77a6e61761fca9ddadafd5
- clm_5c3cd18776cd5796e4fdb54569d63d6649f47f20ee0d62c524990666298c5bd4
- clm_6dbf7ae307f51ff96a04a4ab15fc23716bd76498e7f2b4d86cb0529bcf9a5c2c
- clm_c4a9a2c784200ab4ec69aa53ef9a45268b40f1068d2654879cabf7217cc30d22
- clm_cab1afe4ca8d4f20db94815ec135a8b5cfef355f339cf6ff5f5fb3f08cdf872b
- clm_d6bf4185bfa989a0f1cf31d1cb1e7943e9d48d808541e434d2d0acf6f889c5ae
- clm_f319fd9fe1d16f4159f59b6d15c09840f1ef57c7c5f4b0ab9ce4ba685988728e
maturity: draft
page_id: pg_6a60d883627356eea37e0a32b1a21564
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5a8788cbeeeb5b8a8cadf36ffcd7c1f7
title: bmdavis419/.better-coding-agents/README.md @ 9a1709fa3b7f
updated_at: '2026-09-14T03:38:28Z'
---

# bmdavis419/.better-coding-agents/README.md @ 9a1709fa3b7f

<!-- rcw:begin owner=source:src_5a8788cbeeeb5b8a8cadf36ffcd7c1f7 block=evidence -->
- The repository ships preconfigured setups for svelte & sveltekit, effect.ts, neverthrow, and opencode. [@claim:clm_152c56215d1894fa60d554233b33b3f5605e1b245e39c626728bc9b33efef897]
- The copy steps use cp -u so existing files are overwritten only when the source is newer, and parent directories are created if missing. [@claim:clm_34d8a3e68972ad2f117a1955c44f84c3e4e9c1e2d96966c3fac155180fda3e96]
- Cursor setup copies CURSOR_ASSETS/commands markdown files into ~/.cursor/commands, creating the directory if needed. [@claim:clm_4aae6828c37d27a354b50839a7007d5bb59496d84f77a6e61761fca9ddadafd5]
- The tooling targets OpenCode and Cursor as the consuming coding-agent environments, with the repo expected to be cloned to ~/.better-coding-agents. [@claim:clm_5c3cd18776cd5796e4fdb54569d63d6649f47f20ee0d62c524990666298c5bd4]
- After setup, users get slash commands for the covered libraries in OpenCode and Cursor, plus a special OpenCode agent that searches the codebase for answers. [@claim:clm_6dbf7ae307f51ff96a04a4ab15fc23716bd76498e7f2b4d86cb0529bcf9a5c2c]
- An init command configures the user's machine by upserting OpenCode commands and agents and Cursor commands, updating existing files or creating new ones. [@claim:clm_c4a9a2c784200ab4ec69aa53ef9a45268b40f1068d2654879cabf7217cc30d22]
- The approach is to clone a library's entire source repo as a git subtree so an agent can search the codebase to answer questions about that library. [@claim:clm_cab1afe4ca8d4f20db94815ec135a8b5cfef355f339cf6ff5f5fb3f08cdf872b]
- Setup involves copying OPENCODE_ASSETS agent, command, and theme files into ~/.config/opencode subdirectories (agent, command, themes) after creating them. [@claim:clm_d6bf4185bfa989a0f1cf31d1cb1e7943e9d48d808541e434d2d0acf6f889c5ae]
- The repository also includes a color theme ported to OpenCode as part of its assets. [@claim:clm_f319fd9fe1d16f4159f59b6d15c09840f1ef57c7c5f4b0ab9ce4ba685988728e]
<!-- rcw:end owner=source:src_5a8788cbeeeb5b8a8cadf36ffcd7c1f7 block=evidence -->

## Researcher notes

