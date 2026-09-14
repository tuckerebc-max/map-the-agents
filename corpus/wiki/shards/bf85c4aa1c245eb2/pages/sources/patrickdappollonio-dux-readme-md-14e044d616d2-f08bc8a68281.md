---
access: public
aliases: []
claim_ids:
- clm_336b6f28a274f3688e71bd905515ed23c7d92fbde45a6b450024141b4e88f535
- clm_47c97e0b1ae495ff5fae8d6fddbe51100710e2bb64f6f148d2c16c25253a876b
- clm_6af25d1b0d573d5832195e4efa762443efcd4a1ab5def7154d4b4ce7cb011643
- clm_7375a5afe5e3c460771b3fd74b0e571b033b13bcffc2a523fb5097cd4ac5d9db
- clm_8903dc642be7c1c55d384f35fbb379ec12ab08b4c5a489043a6c6d57eac34944
- clm_a22d9d059994befb9bce672d8aab79cd9c3d58b8102df4511c9842432f8d5b94
- clm_b4f5c8f8286acf5097cd8a57f0be616fb4772c5b20bdd7f7fcac386485332d4b
- clm_df90e48dec2785e69ad94e41d095d61cdc775973453854792fae20c2fd5d66ec
- clm_f90c6ce639f60c5dd3541de2e4ee89d90a6a0a0ee12c1c17ab004db824b8c024
- clm_fa614dff30db6eb0c77c1e534ebd5c1ff3e47f09dfcf21dccfbcbe2f8f1fd41e
- clm_ff104f5610089b2d526b76c26b365dd298cdceffa6c8e9027d34ce441cfb190d
maturity: draft
page_id: pg_5a2f9b6ad3115f389055f08bc8a68281
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1a20a257cf9e59208174d271dbe9b397
title: patrickdappollonio/dux/README.md @ 14e044d616d2
updated_at: '2026-09-14T02:30:06Z'
---

# patrickdappollonio/dux/README.md @ 14e044d616d2

<!-- rcw:begin owner=source:src_1a20a257cf9e59208174d271dbe9b397 block=evidence -->
- Each agent gets companion terminal shells in the same worktree, and multiple companion terminals per agent are supported. [@claim:clm_336b6f28a274f3688e71bd905515ed23c7d92fbde45a6b450024141b4e88f535]
- Projects support a startup command run in the new worktree before the provider launches, with env expansion, DUX_* environment variables, and log/rerun palette commands; failure does not block agent creation. [@claim:clm_47c97e0b1ae495ff5fae8d6fddbe51100710e2bb64f6f148d2c16c25253a876b]
- The right pane provides git staging: stage/unstage files, view syntax-highlighted diffs, write commit messages, push, and pull; AI commit-message drafting uses the provider in oneshot mode with a customizable prompt. [@claim:clm_6af25d1b0d573d5832195e4efa762443efcd4a1ab5def7154d4b4ce7cb011643]
- Session state persists in sessions.sqlite3 alongside the config, and logs go to dux.log in the config directory with a configurable level and path. [@claim:clm_7375a5afe5e3c460771b3fd74b0e571b033b13bcffc2a523fb5097cd4ac5d9db]
- Palette commands include change-agent-provider, change-default-provider, and change-project-default-provider for switching providers per worktree, globally, or per project, with resume_args reused when available. [@claim:clm_8903dc642be7c1c55d384f35fbb379ec12ab08b4c5a489043a6c6d57eac34944]
- Any terminal command can be a provider via a TOML config entry with command, args, and optional resume_args; built-in defaults include Claude, Codex, and OpenCode, and adding a provider is config-only. [@claim:clm_a22d9d059994befb9bce672d8aab79cd9c3d58b8102df4511c9842432f8d5b94]
- Themes use the Opaline TOML format; custom themes live next to the config file, resolution prefers user themes then bundled dux_dark then built-in Opaline themes, falling back to dux_dark with a logged warning. [@claim:clm_b4f5c8f8286acf5097cd8a57f0be616fb4772c5b20bdd7f7fcac386485332d4b]
- dux is a terminal UI that runs multiple AI coding agents side by side, each in its own git worktree, with companion terminals, macros, commit generation, and a command palette. [@claim:clm_df90e48dec2785e69ad94e41d095d61cdc775973453854792fae20c2fd5d66ec]
- Agents run through a PTY like a normal shell, so CLIs such as Claude, Codex, or OpenCode behave as they would in a regular terminal, including MCP servers, hooks, and permission dialogs. [@claim:clm_f90c6ce639f60c5dd3541de2e4ee89d90a6a0a0ee12c1c17ab004db824b8c024]
- git is required on PATH; the gh CLI is optional and enables PR status tracking shown as status pills in the interface. [@claim:clm_fa614dff30db6eb0c77c1e534ebd5c1ff3e47f09dfcf21dccfbcbe2f8f1fd41e]
- The interface has three panes: projects and agent sessions on the left, the agent's live terminal output or diff in the center, and changed files, staging, and diffs on the right. [@claim:clm_ff104f5610089b2d526b76c26b365dd298cdceffa6c8e9027d34ce441cfb190d]
<!-- rcw:end owner=source:src_1a20a257cf9e59208174d271dbe9b397 block=evidence -->

## Researcher notes

