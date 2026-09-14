---
access: public
aliases: []
claim_ids:
- clm_2d2d59fb0475fa54ddb37bb8f5b9e541d496bd4d9e4df2e6e0bd1dc286f65cb8
- clm_36a5ed3e9704f37086540a816ed55e0329a139ae6e9737707a9d9d62337cea1e
- clm_40265e8b48798c44c2b45abeacc674801c5123972da001ddc7ac25cd5296bf3a
- clm_419a3697db872a8869898d6cddd00bdd375b2d274cad958368eeabbb18405fc5
- clm_46e49be9d825259b1591b490c741d3715144d372c16113f09f4a95aced7ebdc4
- clm_55bd1bc05381f812b30e069bd7cb7ec3e6ff14fc2dc51aef5e4ec9e5ba5ed17d
- clm_5bffbef36bddd7ccec7e38fd71b90de5c837480322111bb294db7db1e7807a51
- clm_61d72132e9db821aeb2ad9a4607c632f210829caef14e600dea2c2754f29f920
- clm_76e8d1d77ee2480b6ea8e62bc21fd29625cef0fbd18e8a7b9417b4aeaf9d3ee2
- clm_7c8a3061de48993dddec3b8e4735c075a5b725e2f382559ad971298aa6887485
- clm_7faf76c22bc358d18ee77a36b2866f1b06130b193034f70f82eab13ee36d878b
- clm_9c5306f8e2e213ac77bbd900ee5711472b79916d3cd2ec8e580846f7234383e8
- clm_ac33731ef52c294bbaba79ce222752af1f4a484837060476a3b3757c5fa8b618
- clm_b244679893d138bc8d73196c10eebdc30132bd9cd3ca117a59ef1f04900b7271
- clm_b4c70b8f8b0359a74d4ed917282201ccca6b1dc909fa83e4436c007d0b6f5a8c
- clm_cdd398e29d07e53aee9580ba9f53e68bb99a28b650e3c59a53487547f59ad5b4
- clm_ea8ab22dcd4a1bd93c5030626e54fd9b7190d0fad010b1ab597e0eeab3a6c177
- clm_ebf1b53ae4de74f7cde872003771c4c717d35ac4938a685cb0cd6823c317e0b9
maturity: draft
page_id: pg_eb4220e7bf6956d098f0a07cf588a444
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6252bacc1d7f5756a69aa2a83603051d
title: Dicklesworthstone/coding_agent_account_manager/README.md @ ef01b6411acc
updated_at: '2026-09-14T03:46:54Z'
---

# Dicklesworthstone/coding_agent_account_manager/README.md @ ef01b6411acc

<!-- rcw:begin owner=source:src_6252bacc1d7f5756a69aa2a83603051d block=evidence -->
- After switching codex auth, caam detects a running codex app-server daemon and warns; --reload-daemon SIGTERMs it so it respawns with the new auth. [@claim:clm_2d2d59fb0475fa54ddb37bb8f5b9e541d496bd4d9e4df2e6e0bd1dc286f65cb8]
- Shallow-profile subcommands include shallow-profile create/list/delete/sync-config and shallow-spawn with flags like --create, --print-env, --allow-agent-view, --no-sync-config, and --effort. [@claim:clm_36a5ed3e9704f37086540a816ed55e0329a139ae6e9737707a9d9d62337cea1e]
- The tool works by backing up and restoring the plain OAuth token files each AI CLI stores, so switching is effectively file copying with no browser or OAuth flow. [@claim:clm_40265e8b48798c44c2b45abeacc674801c5123972da001ddc7ac25cd5296bf3a]
- In isolated profiles, dev tooling like ~/.ssh and ~/.gitconfig is symlinked to the real home while provider auth directories are real and isolated, and ~/.local/share/caam is never passed through. [@claim:clm_419a3697db872a8869898d6cddd00bdd375b2d274cad958368eeabbb18405fc5]
- caam limits supports --cached to read Claude's on-disk usage snapshot without network or token presentation, --rank earliest-reset-headroom for seat selection, and --profile/--source to read vault, isolated, or shallow credential namespaces. [@claim:clm_46e49be9d825259b1591b490c741d3715144d372c16113f09f4a95aced7ebdc4]
- The tool targets users of fixed-cost AI coding subscriptions (Claude Max, GPT Pro, Gemini Ultra) who hit rate limits and want sub-100ms account switching instead of a 30-60 second browser OAuth flow. [@claim:clm_55bd1bc05381f812b30e069bd7cb7ec3e6ff14fc2dc51aef5e4ec9e5ba5ed17d]
- Profiles live in a vault under ~/.local/share/caam/vault/ organized per provider and account name, mirroring auth files from locations like ~/.claude.json and ~/.codex/auth.json. [@claim:clm_5bffbef36bddd7ccec7e38fd71b90de5c837480322111bb294db7db1e7807a51]
- Three profile modes are offered: vault profiles for sequential switching, isolated profiles with full directory isolation for parallel sessions, and shallow profiles that isolate only auth-bearing files. [@claim:clm_61d72132e9db821aeb2ad9a4607c632f210829caef14e600dea2c2754f29f920]
- Unknown shallow-spawn names are errors rather than implicit profile creation, with --create required to provision a new empty identity, preventing mistyped names from spawning wrong-account logins. [@claim:clm_76e8d1d77ee2480b6ea8e62bc21fd29625cef0fbd18e8a7b9417b4aeaf9d3ee2]
- A --json flag is provided for agent contexts, with stdout carrying data, stderr diagnostics, and exit code 0 signaling success. [@claim:clm_7c8a3061de48993dddec3b8e4735c075a5b725e2f382559ad971298aa6887485]
- The tool uses embedded SQLite, requires no daemon, and an optional background service is available. [@claim:clm_7faf76c22bc358d18ee77a36b2866f1b06130b193034f70f82eab13ee36d878b]
- Claude's auth format does not expose email or account ID, so profile names default to timestamp-based auto-names unless a name is given at backup time. [@claim:clm_9c5306f8e2e213ac77bbd900ee5711472b79916d3cd2ec8e580846f7234383e8]
- caam pick uses fzf when installed and falls back to a numbered prompt otherwise, so fzf is an optional dependency. [@claim:clm_ac33731ef52c294bbaba79ce222752af1f4a484837060476a3b3757c5fa8b618]
- The CLI offers commands including backup, activate, status, ls, delete, paths, clear, alias, rename, and uninstall for managing saved auth profiles. [@claim:clm_b244679893d138bc8d73196c10eebdc30132bd9cd3ca117a59ef1f04900b7271]
- On macOS, caam treats the login keychain as authoritative for Claude's OAuth blob, with the credentials file as a 0600 mirror; CAAM_KEYCHAIN=0 disables the bridge. [@claim:clm_b4c70b8f8b0359a74d4ed917282201ccca6b1dc909fa83e4436c007d0b6f5a8c]
- Shallow-spawn injects CLAUDE_CODE_DISABLE_AGENT_VIEW=1 by default to prevent Claude's background supervisor from bypassing per-identity auth isolation, with --allow-agent-view as an opt-out. [@claim:clm_cdd398e29d07e53aee9580ba9f53e68bb99a28b650e3c59a53487547f59ad5b4]
- CAAM cannot refresh Claude or Grok tokens; users must re-login via /login or grok login when tokens expire, and Grok tokens expire after 7 days. [@claim:clm_ea8ab22dcd4a1bd93c5030626e54fd9b7190d0fad010b1ab597e0eeab3a6c177]
- caam status detects the active profile by SHA-256 hashing current auth files and matching against vault profiles, avoiding hidden state files that could desync. [@claim:clm_ebf1b53ae4de74f7cde872003771c4c717d35ac4938a685cb0cd6823c317e0b9]
<!-- rcw:end owner=source:src_6252bacc1d7f5756a69aa2a83603051d block=evidence -->

## Researcher notes

