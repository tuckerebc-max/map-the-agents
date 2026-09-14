# dicklesworthstone/coding_agent_account_manager

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ef01b6411acc @ 111e1c3e595f5ddc

## Summary (orientation draft, not independently verified)

caam is a CLI that manages OAuth credential files for AI coding CLIs (Claude Code, Codex, Gemini, Antigravity, Grok), offering vault/isolated/shallow profile modes, instant account switching, rotation and rate-limit tooling, and JSON output for agent use. All prior product claims were verified against README slices; the implementation language is not stated in the cited evidence. Evidence coverage: 140 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Profiles live in a vault under ~/.local/share/caam/vault/ organized per provider and account name, mirroring auth files from locations like ~/.claude.json and ~/.codex/auth.json. -- evidence: [README.md#L68-L74](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L68-L74), [README.md#L76-L80](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L76-L80)
  - [observation/documented] The tool uses embedded SQLite, requires no daemon, and an optional background service is available. -- evidence: [README.md#L90-L90](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L90-L90)
- design-choices (7 claim(s)):
  - [observation/documented] caam status detects the active profile by SHA-256 hashing current auth files and matching against vault profiles, avoiding hidden state files that could desync. -- evidence: [README.md#L98-L98](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L98-L98), [README.md#L104-L107](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L104-L107), [README.md#L100-L102](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L100-L102)
  - [observation/documented] The tool works by backing up and restoring the plain OAuth token files each AI CLI stores, so switching is effectively file copying with no browser or OAuth flow. -- evidence: [README.md#L56-L56](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L56-L56), [README.md#L62-L62](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L62-L62), [README.md#L90-L90](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L90-L90)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI offers commands including backup, activate, status, ls, delete, paths, clear, alias, rename, and uninstall for managing saved auth profiles. -- evidence: [README.md#L430-L441](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L430-L441)
  - [observation/documented] A --json flag is provided for agent contexts, with stdout carrying data, stderr diagnostics, and exit code 0 signaling success. -- evidence: [README.md#L28-L28](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L28-L28)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] caam pick uses fzf when installed and falls back to a numbered prompt otherwise, so fzf is an optional dependency. -- evidence: [README.md#L476-L476](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L476-L476), [README.md#L449-L452](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L449-L452)
- limitations (2 claim(s)):
  - [observation/documented] CAAM cannot refresh Claude or Grok tokens; users must re-login via /login or grok login when tokens expire, and Grok tokens expire after 7 days. -- evidence: [README.md#L339-L342](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L339-L342), [README.md#L378-L378](https://github.com/Dicklesworthstone/coding_agent_account_manager/blob/ef01b6411acc870ee455270b2c27baf7fe562561/README.md#L378-L378)
More evidence: [full detail](coding_agent_account_manager.detail.md)

Metadata and full claim list: [full detail](coding_agent_account_manager.detail.md)
Human notes ([notes](coding_agent_account_manager.notes.md), never overwritten by build)

[Back to map index](../../index.md)
