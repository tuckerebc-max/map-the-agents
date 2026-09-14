# shuyu-labs/webcode

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 65c1b5708dea @ 786ea9384cdb639c

## Summary (orientation draft, not independently verified)

WebCode is a Blazor Server (.NET 10) platform that wraps local AI CLIs (Claude Code, Codex, OpenCode) into a manageable multi-user web/mobile/Feishu console, with cc-switch as the sole provider authority. Evidence is README documentation plus contributor-instruction files; no code inspection is available.

## Source coverage

Source coverage (partial): 3 of 155 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] WebCode is described as an AI CLI work platform built on Blazor Server and .NET 10, wrapping local or server-side AI CLIs into a manageable, deployable, remotely accessible system. -- evidence: [README.md#L55-L55](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L55-L55)
  - [observation/documented] The repo includes a Superpowers workflow layer that wraps user input into structured workflow prompts (e.g. plan, ralph, deep-interview, team) with capability detection, implemented via services like SuperpowersPromptBuilder. -- evidence: [README.md#L173-L173](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L173-L173), [README.md#L182-L186](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L182-L186), [README.md#L190-L197](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L190-L197)
- design-choices (3 claim(s)):
  - [observation/documented] cc-switch is the single provider authority: WebCode does not allow manual provider editing or profile switching for the three managed CLIs and only reads cc-switch's current state and live config files. -- evidence: [README.md#L213-L216](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L213-L216), [README.md#L220-L222](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L220-L222)
  - [observation/documented] Sessions follow terminal-window semantics: a new session snapshots the active provider's live config at first run, and existing sessions only change provider when the user explicitly clicks sync. -- evidence: [README.md#L228-L230](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L228-L230), [README.md#L226-L226](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L226-L226)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md imposes hard constraints for autonomous coding agents—never commit credential material, keep /.codex/ state untracked, and record implementation findings in dated files under /docs/agent-notes/. -- evidence: [AGENTS.md#L3-L3](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L3-L3), [AGENTS.md#L7-L11](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L7-L11), [AGENTS.md#L20-L23](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L20-L23), [AGENTS.md#L15-L16](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L15-L16)
  - [observation/documented] Repository development practice: CLAUDE.md documents build/run commands (dotnet restore/build/run, docker compose up), Tailwind CSS build via npm, and conventions such as Chinese comments and [ServiceDescription]-attribute service registration. -- evidence: [CLAUDE.md#L79-L83](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L79-L83), [CLAUDE.md#L52-L52](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L52-L52), [CLAUDE.md#L55-L55](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L55-L55), [CLAUDE.md#L58-L58](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L58-L58), [CLAUDE.md#L129-L132](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L129-L132)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product supports three entry points—desktop web, mobile, and Feishu cards—for creating, switching, closing, and importing AI CLI sessions, with desktop web described as the most complete console. -- evidence: [README.md#L100-L110](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L100-L110), [README.md#L114-L116](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L114-L116)
  - [observation/documented] Feishu integration covers session binding, card-based session management, streaming card updates, attachment staging cards for image/file messages, and auto-generated cloud reply documents with links sent back to chat. -- evidence: [README.md#L122-L131](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L122-L131), [README.md#L15-L22](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L15-L22), [README.md#L13-L13](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L13-L13)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](webcode.detail.md)

Metadata and full claim list: [full detail](webcode.detail.md)
Human notes ([notes](webcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
