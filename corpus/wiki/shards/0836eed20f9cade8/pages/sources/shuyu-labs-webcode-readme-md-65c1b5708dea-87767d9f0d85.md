---
access: public
aliases: []
claim_ids:
- clm_0395366de02770c39169eb74859e467fe217a940b1054365bb34cfb6cb5cc78e
- clm_079cb7ef35806ea4877af0212f7a6f83f52a95b13324e4b28c4649f5894af313
- clm_1cf0022a1fe7a663ea83cedbb568526ef64dcc88ba82a24dcfcace132cfd3851
- clm_36d2b27dd35d221bf4edfd340f969b772e97aa6ac489ff7fb1c2f4763347b69a
- clm_4710fe1d0596b173578c935a03d7867439521d3ae186d3535a64a48bda229267
- clm_6dc6b0ae5dbe84ff03c223cc4ff36da463906df8bb79b8737a29575e465e0783
- clm_700428ab788e6f856ff36ab31ac2ca29fe46177ed4c78e6c48dbd64de47c982d
- clm_73cefbef1d55fe0bc02692decf8791ba0edbefb9f66afa84cece459c86875ca3
- clm_79808ac9b58f69c744d43738108ab4ba402f4e31a585d37d46510d4497c3311e
- clm_8cf1f9c4321769a70c4b9b046d77558d8d2d47ef3d52784b72d06a9851b0342b
- clm_96111b2856e100e3854ea7f0cb10ba083a7c985454518c60575bd732c02e8742
maturity: draft
page_id: pg_0d31d9dc6d6f5cf0a1de87767d9f0d85
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a4fe55533ad55b078ef27fc530c5ddd0
title: shuyu-labs/WebCode/README.md @ 65c1b5708dea
updated_at: '2026-09-14T02:39:55Z'
---

# shuyu-labs/WebCode/README.md @ 65c1b5708dea

<!-- rcw:begin owner=source:src_a4fe55533ad55b078ef27fc530c5ddd0 block=evidence -->
- The repo includes a Superpowers workflow layer that wraps user input into structured workflow prompts (e.g. plan, ralph, deep-interview, team) with capability detection, implemented via services like SuperpowersPromptBuilder. [@claim:clm_0395366de02770c39169eb74859e467fe217a940b1054365bb34cfb6cb5cc78e]
- Sessions follow terminal-window semantics: a new session snapshots the active provider's live config at first run, and existing sessions only change provider when the user explicitly clicks sync. [@claim:clm_079cb7ef35806ea4877af0212f7a6f83f52a95b13324e4b28c4649f5894af313]
- cc-switch is the single provider authority: WebCode does not allow manual provider editing or profile switching for the three managed CLIs and only reads cc-switch's current state and live config files. [@claim:clm_1cf0022a1fe7a663ea83cedbb568526ef64dcc88ba82a24dcfcace132cfd3851]
- The stack includes Blazor Server, .NET 10, Monaco Editor, SqlSugar ORM, SQLite default database, YARP reverse proxy, and Markdig for Markdown. [@claim:clm_36d2b27dd35d221bf4edfd340f969b772e97aa6ac489ff7fb1c2f4763347b69a]
- Feishu integration covers session binding, card-based session management, streaming card updates, attachment staging cards for image/file messages, and auto-generated cloud reply documents with links sent back to chat. [@claim:clm_4710fe1d0596b173578c935a03d7867439521d3ae186d3535a64a48bda229267]
- Deployment options include Docker Compose (default port 5000), Windows installer/portable win-x64 self-contained releases (default port 6021), and local dotnet run development. [@claim:clm_6dc6b0ae5dbe84ff03c223cc4ff36da463906df8bb79b8737a29575e465e0783]
- WebCode is described as an AI CLI work platform built on Blazor Server and .NET 10, wrapping local or server-side AI CLIs into a manageable, deployable, remotely accessible system. [@claim:clm_700428ab788e6f856ff36ab31ac2ca29fe46177ed4c78e6c48dbd64de47c982d]
- If a session's provider snapshot is lost or corrupted, WebCode blocks further execution and prompts for explicit sync rather than silently falling back to the machine's current live config. [@claim:clm_73cefbef1d55fe0bc02692decf8791ba0edbefb9f66afa84cece459c86875ca3]
- Per-user controls include enable/disable, restrictions on which CLI tools a user may use, directory whitelist policies, per-user Feishu bot configuration, and shared defaults with per-user overrides. [@claim:clm_79808ac9b58f69c744d43738108ab4ba402f4e31a585d37d46510d4497c3311e]
- The product supports three entry points—desktop web, mobile, and Feishu cards—for creating, switching, closing, and importing AI CLI sessions, with desktop web described as the most complete console. [@claim:clm_8cf1f9c4321769a70c4b9b046d77558d8d2d47ef3d52784b72d06a9851b0342b]
- Codex /goal support requires Codex CLI version at least 0.128.0; WebCode probes the CLI version and goals feature, injecting goals=true into session-level .codex/config.toml only when the feature is available. [@claim:clm_96111b2856e100e3854ea7f0cb10ba083a7c985454518c60575bd732c02e8742]
<!-- rcw:end owner=source:src_a4fe55533ad55b078ef27fc530c5ddd0 block=evidence -->

## Researcher notes

