---
access: public
aliases: []
claim_ids:
- clm_11f1baab413b54833982a3490f15d423cfb1c5253bb0325da1194dac9efb00cd
- clm_17f9fe8bdbaf8fabdd791d99a2f0240b16778a36032e105d64a449388136ebc8
- clm_1924536071abe2efc241a84fdbeae26ec73a8d8ef959a20e066a76289af39d0b
- clm_31369dfed15a1f082b118101b7fbc2e0c3ce440fadacc95e397947707d506799
- clm_423251bc317b53136f55d112db08729a36f745110abf8aea6171908ed2184644
- clm_5067f6b6eff20813a3338de177d6a9ae52bf24db706f45a20419e9b55659ca3c
- clm_6e090ee06d52cdccbb0096471a21af46bbbe750fba2d94e022dfa520883dc975
- clm_74a173f76984863b9d0c2aca7068b073b3c3502d17ce70bee66b2ea25c5a90c3
- clm_8b9804bd91c890d36dbe7ac7779b0205184f8bbf616716657b002b079e49ec12
- clm_a5836d27c6d1e242e5693c04f61d18bc8ed54935d1e638b3af684a1d2404531b
- clm_ef50337cb48de0fa54c2697b5b03cfcee4379b43ddfbd01899da3cb3a22d9485
maturity: draft
page_id: pg_d71b674c263c55939a14fce4e2b61d5d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f322e22946775c708d663f0f3ce14dea
title: agentmd/agent.md/README.md @ e86e5c8b57d5
updated_at: '2026-09-14T03:32:04Z'
---

# agentmd/agent.md/README.md @ e86e5c8b57d5

<!-- rcw:begin owner=source:src_f322e22946775c708d663f0f3ce14dea block=evidence -->
- The document is marked informational, dated July 2025, authored by Geoffrey Huntley of Sourcegraph, Inc. [@claim:clm_11f1baab413b54833982a3490f15d423cfb1c5253bb0325da1194dac9efb00cd]
- The format is intended to be human-readable while remaining parseable by agentic coding tools, positioning one file as a universal voice for any AI coding tool. [@claim:clm_17f9fe8bdbaf8fabdd791d99a2f0240b16778a36032e105d64a449388136ebc8]
- Tool implementers are advised to parse AGENT.md at project initialization, extract tool-relevant configuration, provide fallback behavior when absent, and respect legacy tool-specific config files. [@claim:clm_1924536071abe2efc241a84fdbeae26ec73a8d8ef959a20e066a76289af39d0b]
- The document motivates AGENT.md by the proliferation of per-tool config files such as .cursorrules, .windsurfrules, and .clauderules that consumers must maintain separately. [@claim:clm_31369dfed15a1f082b118101b7fbc2e0c3ce440fadacc95e397947707d506799]
- The spec requires AGENT.md to be placed in a project's root directory and written in Markdown, and recommends sections covering structure, commands, style, architecture, testing, and security. [@claim:clm_423251bc317b53136f55d112db08729a36f745110abf8aea6171908ed2184644]
- When multiple AGENT.md files exist, tools should merge configurations with more specific files taking precedence over general ones. [@claim:clm_5067f6b6eff20813a3338de177d6a9ae52bf24db706f45a20419e9b55659ca3c]
- The document provides migration commands that move legacy configs (e.g., .clinerules, CLAUDE.md, .cursorrules) to AGENT.md and symlink the old paths back, preserving backward compatibility. [@claim:clm_6e090ee06d52cdccbb0096471a21af46bbbe750fba2d94e022dfa520883dc975]
- AGENT.md files may reference other files via @-mentions (e.g., @filename.md) to pull in additional context or documentation. [@claim:clm_74a173f76984863b9d0c2aca7068b073b3c3502d17ce70bee66b2ea25c5a90c3]
- The document lists RFC 2119 and Gruber's Markdown as normative references, and states no IANA actions are required since the .md extension is already registered. [@claim:clm_8b9804bd91c890d36dbe7ac7779b0205184f8bbf616716657b002b079e49ec12]
- Per the document, Amp has native AGENT.md support since 2025-05-07 (multiple files since 2025-07-07), while several other tools support it via symbolic linking. [@claim:clm_a5836d27c6d1e242e5693c04f61d18bc8ed54935d1e638b3af684a1d2404531b]
- Implementations should support a hierarchy of AGENT.md files: root-level for general guidance, subdirectory files for subsystems, and a user-global file at ~/.config/AGENT.md. [@claim:clm_ef50337cb48de0fa54c2697b5b03cfcee4379b43ddfbd01899da3cb3a22d9485]
<!-- rcw:end owner=source:src_f322e22946775c708d663f0f3ce14dea block=evidence -->

## Researcher notes

