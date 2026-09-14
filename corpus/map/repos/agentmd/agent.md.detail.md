# agentmd/agent.md -- full detail

[Back to orientation](agent.md.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agentmd/agent.md/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/d9bd0b2eecce1b16.json](../../../wiki/dossiers/agentmd/agent.md/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/d9bd0b2eecce1b16.json)

## specifications (4 claim(s))

- [observation/documented] The spec requires AGENT.md to be placed in a project's root directory and written in Markdown, and recommends sections covering structure, commands, style, architecture, testing, and security. -- evidence: [README.md#L57-L57](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L57-L57), [README.md#L59-L64](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L59-L64) (`clm_423251bc317b53136f55d112db08729a36f745110abf8aea6171908ed2184644`)
- [observation/documented] Implementations should support a hierarchy of AGENT.md files: root-level for general guidance, subdirectory files for subsystems, and a user-global file at ~/.config/AGENT.md. -- evidence: [README.md#L70-L70](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L70-L70), [README.md#L72-L74](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L72-L74) (`clm_ef50337cb48de0fa54c2697b5b03cfcee4379b43ddfbd01899da3cb3a22d9485`)
- [observation/documented] When multiple AGENT.md files exist, tools should merge configurations with more specific files taking precedence over general ones. -- evidence: [README.md#L76-L76](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L76-L76) (`clm_5067f6b6eff20813a3338de177d6a9ae52bf24db706f45a20419e9b55659ca3c`)
- [observation/documented] The document is marked informational, dated July 2025, authored by Geoffrey Huntley of Sourcegraph, Inc. -- evidence: [README.md#L9-L9](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L9-L9), [README.md#L3-L3](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L3-L3), [README.md#L5-L5](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L5-L5), [README.md#L7-L7](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L7-L7) (`clm_11f1baab413b54833982a3490f15d423cfb1c5253bb0325da1194dac9efb00cd`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The format is intended to be human-readable while remaining parseable by agentic coding tools, positioning one file as a universal voice for any AI coding tool. -- evidence: [README.md#L51-L51](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L51-L51), [README.md#L66-L66](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L66-L66) (`clm_17f9fe8bdbaf8fabdd791d99a2f0240b16778a36032e105d64a449388136ebc8`)
- [observation/documented] Tool implementers are advised to parse AGENT.md at project initialization, extract tool-relevant configuration, provide fallback behavior when absent, and respect legacy tool-specific config files. -- evidence: [README.md#L86-L89](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L86-L89), [README.md#L84-L84](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L84-L84) (`clm_1924536071abe2efc241a84fdbeae26ec73a8d8ef959a20e066a76289af39d0b`)

## workflows (1 claim(s))

- [observation/documented] The document provides migration commands that move legacy configs (e.g., .clinerules, CLAUDE.md, .cursorrules) to AGENT.md and symlink the old paths back, preserving backward compatibility. -- evidence: [README.md#L125-L125](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L125-L125), [README.md#L101-L101](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L101-L101), [README.md#L107-L107](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L107-L107), [README.md#L104-L104](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L104-L104) (`clm_6e090ee06d52cdccbb0096471a21af46bbbe750fba2d94e022dfa520883dc975`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] AGENT.md files may reference other files via @-mentions (e.g., @filename.md) to pull in additional context or documentation. -- evidence: [README.md#L80-L80](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L80-L80) (`clm_74a173f76984863b9d0c2aca7068b073b3c3502d17ce70bee66b2ea25c5a90c3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The document lists RFC 2119 and Gruber's Markdown as normative references, and states no IANA actions are required since the .md extension is already registered. -- evidence: [README.md#L254-L254](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L254-L254), [README.md#L252-L252](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L252-L252), [README.md#L246-L246](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L246-L246), [README.md#L250-L250](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L250-L250) (`clm_8b9804bd91c890d36dbe7ac7779b0205184f8bbf616716657b002b079e49ec12`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (2 claim(s))

- [observation/documented] The document motivates AGENT.md by the proliferation of per-tool config files such as .cursorrules, .windsurfrules, and .clauderules that consumers must maintain separately. -- evidence: [README.md#L49-L49](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L49-L49) (`clm_31369dfed15a1f082b118101b7fbc2e0c3ce440fadacc95e397947707d506799`)
- [observation/documented] Per the document, Amp has native AGENT.md support since 2025-05-07 (multiple files since 2025-07-07), while several other tools support it via symbolic linking. -- evidence: [README.md#L234-L242](https://github.com/agentmd/agent.md/blob/e86e5c8b57d5dc8838b78ad965536686ee8eaa64/README.md#L234-L242) (`clm_a5836d27c6d1e242e5693c04f61d18bc8ed54935d1e638b3af684a1d2404531b`)

