# dicklesworthstone/coding_agent_account_manager -- full detail

[Back to orientation](coding_agent_account_manager.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/91a858f0/dafe21fe/ef01b6411acc870ee455270b2c27baf7fe562561/111e1c3e595f5ddc.json](../../../wiki/dossiers/91a858f0/dafe21fe/ef01b6411acc870ee455270b2c27baf7fe562561/111e1c3e595f5ddc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Profiles live in a vault under ~/.local/share/caam/vault/ organized per provider and account name, mirroring auth files from locations like ~/.claude.json and ~/.codex/auth.json. -- evidence: [README.md#L68-L74](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L68-L74), [README.md#L76-L80](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L76-L80) (`clm_5bffbef36bddd7ccec7e38fd71b90de5c837480322111bb294db7db1e7807a51`)
- [observation/documented] The tool uses embedded SQLite, requires no daemon, and an optional background service is available. -- evidence: [README.md#L90-L90](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L90-L90) (`clm_7faf76c22bc358d18ee77a36b2866f1b06130b193034f70f82eab13ee36d878b`)

## design-choices (7 claim(s))

- [observation/documented] caam status detects the active profile by SHA-256 hashing current auth files and matching against vault profiles, avoiding hidden state files that could desync. -- evidence: [README.md#L98-L98](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L98-L98), [README.md#L104-L107](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L104-L107), [README.md#L100-L102](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L100-L102) (`clm_ebf1b53ae4de74f7cde872003771c4c717d35ac4938a685cb0cd6823c317e0b9`)
- [observation/documented] The tool works by backing up and restoring the plain OAuth token files each AI CLI stores, so switching is effectively file copying with no browser or OAuth flow. -- evidence: [README.md#L56-L56](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L56-L56), [README.md#L62-L62](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L62-L62), [README.md#L90-L90](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L90-L90) (`clm_40265e8b48798c44c2b45abeacc674801c5123972da001ddc7ac25cd5296bf3a`)
- [observation/documented] Three profile modes are offered: vault profiles for sequential switching, isolated profiles with full directory isolation for parallel sessions, and shallow profiles that isolate only auth-bearing files. -- evidence: [README.md#L115-L115](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L115-L115), [README.md#L126-L126](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L126-L126), [README.md#L154-L154](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L154-L154) (`clm_61d72132e9db821aeb2ad9a4607c632f210829caef14e600dea2c2754f29f920`)
- [observation/documented] In isolated profiles, dev tooling like ~/.ssh and ~/.gitconfig is symlinked to the real home while provider auth directories are real and isolated, and ~/.local/share/caam is never passed through. -- evidence: [README.md#L139-L146](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L139-L146) (`clm_419a3697db872a8869898d6cddd00bdd375b2d274cad958368eeabbb18405fc5`)
- [observation/documented] On macOS, caam treats the login keychain as authoritative for Claude's OAuth blob, with the credentials file as a 0600 mirror; CAAM_KEYCHAIN=0 disables the bridge. -- evidence: [README.md#L333-L333](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L333-L333) (`clm_b4c70b8f8b0359a74d4ed917282201ccca6b1dc909fa83e4436c007d0b6f5a8c`)
- [observation/documented] Shallow-spawn injects CLAUDE_CODE_DISABLE_AGENT_VIEW=1 by default to prevent Claude's background supervisor from bypassing per-identity auth isolation, with --allow-agent-view as an opt-out. -- evidence: [README.md#L300-L306](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L300-L306) (`clm_cdd398e29d07e53aee9580ba9f53e68bb99a28b650e3c59a53487547f59ad5b4`)
- [observation/documented] Unknown shallow-spawn names are errors rather than implicit profile creation, with --create required to provision a new empty identity, preventing mistyped names from spawning wrong-account logins. -- evidence: [README.md#L246-L250](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L246-L250), [README.md#L258-L265](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L258-L265) (`clm_76e8d1d77ee2480b6ea8e62bc21fd29625cef0fbd18e8a7b9417b4aeaf9d3ee2`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The CLI offers commands including backup, activate, status, ls, delete, paths, clear, alias, rename, and uninstall for managing saved auth profiles. -- evidence: [README.md#L430-L441](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L430-L441) (`clm_b244679893d138bc8d73196c10eebdc30132bd9cd3ca117a59ef1f04900b7271`)
- [observation/documented] A --json flag is provided for agent contexts, with stdout carrying data, stderr diagnostics, and exit code 0 signaling success. -- evidence: [README.md#L28-L28](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L28-L28) (`clm_7c8a3061de48993dddec3b8e4735c075a5b725e2f382559ad971298aa6887485`)
- [observation/documented] Shallow-profile subcommands include shallow-profile create/list/delete/sync-config and shallow-spawn with flags like --create, --print-env, --allow-agent-view, --no-sync-config, and --effort. -- evidence: [README.md#L202-L216](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L202-L216) (`clm_36a5ed3e9704f37086540a816ed55e0329a139ae6e9737707a9d9d62337cea1e`)
- [observation/documented] caam limits supports --cached to read Claude's on-disk usage snapshot without network or token presentation, --rank earliest-reset-headroom for seat selection, and --profile/--source to read vault, isolated, or shallow credential namespaces. -- evidence: [README.md#L499-L514](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L499-L514), [README.md#L646-L650](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L646-L650), [README.md#L518-L521](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L518-L521) (`clm_46e49be9d825259b1591b490c741d3715144d372c16113f09f4a95aced7ebdc4`)
- [observation/documented] After switching codex auth, caam detects a running codex app-server daemon and warns; --reload-daemon SIGTERMs it so it respawns with the new auth. -- evidence: [README.md#L355-L355](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L355-L355) (`clm_2d2d59fb0475fa54ddb37bb8f5b9e541d496bd4d9e4df2e6e0bd1dc286f65cb8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] caam pick uses fzf when installed and falls back to a numbered prompt otherwise, so fzf is an optional dependency. -- evidence: [README.md#L476-L476](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L476-L476), [README.md#L449-L452](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L449-L452) (`clm_ac33731ef52c294bbaba79ce222752af1f4a484837060476a3b3757c5fa8b618`)

## limitations (2 claim(s))

- [observation/documented] CAAM cannot refresh Claude or Grok tokens; users must re-login via /login or grok login when tokens expire, and Grok tokens expire after 7 days. -- evidence: [README.md#L339-L342](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L339-L342), [README.md#L378-L378](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L378-L378) (`clm_ea8ab22dcd4a1bd93c5030626e54fd9b7190d0fad010b1ab597e0eeab3a6c177`)
- [observation/documented] Claude's auth format does not expose email or account ID, so profile names default to timestamp-based auto-names unless a name is given at backup time. -- evidence: [README.md#L339-L342](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L339-L342) (`clm_9c5306f8e2e213ac77bbd900ee5711472b79916d3cd2ec8e580846f7234383e8`)

## relevance (1 claim(s))

- [observation/documented] The tool targets users of fixed-cost AI coding subscriptions (Claude Max, GPT Pro, Gemini Ultra) who hit rate limits and want sub-100ms account switching instead of a 30-60 second browser OAuth flow. -- evidence: [README.md#L52-L52](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L52-L52), [README.md#L11-L11](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L11-L11), [README.md#L45-L45](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L45-L45) (`clm_55bd1bc05381f812b30e069bd7cb7ec3e6ff14fc2dc51aef5e4ec9e5ba5ed17d`)

