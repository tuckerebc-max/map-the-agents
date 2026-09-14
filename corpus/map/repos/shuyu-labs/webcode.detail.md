# shuyu-labs/webcode -- full detail

[Back to orientation](webcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shuyu-labs/webcode/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/786ea9384cdb639c.json](../../../wiki/dossiers/shuyu-labs/webcode/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/786ea9384cdb639c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] WebCode is described as an AI CLI work platform built on Blazor Server and .NET 10, wrapping local or server-side AI CLIs into a manageable, deployable, remotely accessible system. -- evidence: [README.md#L55-L55](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L55-L55) (`clm_700428ab788e6f856ff36ab31ac2ca29fe46177ed4c78e6c48dbd64de47c982d`)
- [observation/documented] The repo includes a Superpowers workflow layer that wraps user input into structured workflow prompts (e.g. plan, ralph, deep-interview, team) with capability detection, implemented via services like SuperpowersPromptBuilder. -- evidence: [README.md#L173-L173](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L173-L173), [README.md#L182-L186](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L182-L186), [README.md#L190-L197](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L190-L197) (`clm_0395366de02770c39169eb74859e467fe217a940b1054365bb34cfb6cb5cc78e`)

## design-choices (3 claim(s))

- [observation/documented] cc-switch is the single provider authority: WebCode does not allow manual provider editing or profile switching for the three managed CLIs and only reads cc-switch's current state and live config files. -- evidence: [README.md#L213-L216](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L213-L216), [README.md#L220-L222](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L220-L222) (`clm_1cf0022a1fe7a663ea83cedbb568526ef64dcc88ba82a24dcfcace132cfd3851`)
- [observation/documented] Sessions follow terminal-window semantics: a new session snapshots the active provider's live config at first run, and existing sessions only change provider when the user explicitly clicks sync. -- evidence: [README.md#L228-L230](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L228-L230), [README.md#L226-L226](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L226-L226) (`clm_079cb7ef35806ea4877af0212f7a6f83f52a95b13324e4b28c4649f5894af313`)
- [observation/documented] If a session's provider snapshot is lost or corrupted, WebCode blocks further execution and prompts for explicit sync rather than silently falling back to the machine's current live config. -- evidence: [README.md#L238-L238](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L238-L238) (`clm_73cefbef1d55fe0bc02692decf8791ba0edbefb9f66afa84cece459c86875ca3`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md imposes hard constraints for autonomous coding agents—never commit credential material, keep /.codex/ state untracked, and record implementation findings in dated files under /docs/agent-notes/. -- evidence: [AGENTS.md#L3-L3](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L3-L3), [AGENTS.md#L7-L11](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L7-L11), [AGENTS.md#L20-L23](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L20-L23), [AGENTS.md#L15-L16](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/AGENTS.md#L15-L16) (`clm_6a52dbf0a2d829197ba59cbe4dfbaa5ef1a105bdc3c42eb225d3a3bcace3201e`)
- [observation/documented] Repository development practice: CLAUDE.md documents build/run commands (dotnet restore/build/run, docker compose up), Tailwind CSS build via npm, and conventions such as Chinese comments and [ServiceDescription]-attribute service registration. -- evidence: [CLAUDE.md#L79-L83](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L79-L83), [CLAUDE.md#L52-L52](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L52-L52), [CLAUDE.md#L55-L55](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L55-L55), [CLAUDE.md#L58-L58](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L58-L58), [CLAUDE.md#L129-L132](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/CLAUDE.md#L129-L132) (`clm_d3ff3cf2870a378ba04553513a0e6b6807b196cfe45eac0686becc608fecce5e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product supports three entry points—desktop web, mobile, and Feishu cards—for creating, switching, closing, and importing AI CLI sessions, with desktop web described as the most complete console. -- evidence: [README.md#L100-L110](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L100-L110), [README.md#L114-L116](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L114-L116) (`clm_8cf1f9c4321769a70c4b9b046d77558d8d2d47ef3d52784b72d06a9851b0342b`)
- [observation/documented] Feishu integration covers session binding, card-based session management, streaming card updates, attachment staging cards for image/file messages, and auto-generated cloud reply documents with links sent back to chat. -- evidence: [README.md#L122-L131](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L122-L131), [README.md#L15-L22](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L15-L22), [README.md#L13-L13](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L13-L13) (`clm_4710fe1d0596b173578c935a03d7867439521d3ae186d3535a64a48bda229267`)
- [observation/documented] Deployment options include Docker Compose (default port 5000), Windows installer/portable win-x64 self-contained releases (default port 6021), and local dotnet run development. -- evidence: [README.md#L254-L258](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L254-L258), [README.md#L319-L319](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L319-L319), [README.md#L310-L315](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L310-L315), [README.md#L262-L262](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L262-L262), [README.md#L286-L286](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L286-L286), [README.md#L288-L288](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L288-L288) (`clm_6dc6b0ae5dbe84ff03c223cc4ff36da463906df8bb79b8737a29575e465e0783`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Per-user controls include enable/disable, restrictions on which CLI tools a user may use, directory whitelist policies, per-user Feishu bot configuration, and shared defaults with per-user overrides. -- evidence: [README.md#L141-L145](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L141-L145) (`clm_79808ac9b58f69c744d43738108ab4ba402f4e31a585d37d46510d4497c3311e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The stack includes Blazor Server, .NET 10, Monaco Editor, SqlSugar ORM, SQLite default database, YARP reverse proxy, and Markdig for Markdown. -- evidence: [README.md#L373-L373](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L373-L373), [README.md#L438-L447](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L438-L447) (`clm_36d2b27dd35d221bf4edfd340f969b772e97aa6ac489ff7fb1c2f4763347b69a`)
- [observation/documented] Codex /goal support requires Codex CLI version at least 0.128.0; WebCode probes the CLI version and goals feature, injecting goals=true into session-level .codex/config.toml only when the feature is available. -- evidence: [README.md#L160-L163](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L160-L163), [README.md#L167-L169](https://github.com/shuyu-labs/WebCode/blob/65c1b5708dea4083a8a3ba1f67d4ebf0a4b72213/README.md#L167-L169) (`clm_96111b2856e100e3854ea7f0cb10ba083a7c985454518c60575bd732c02e8742`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

