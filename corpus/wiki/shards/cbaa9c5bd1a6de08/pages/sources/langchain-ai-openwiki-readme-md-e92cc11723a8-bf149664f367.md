---
access: public
aliases: []
claim_ids:
- clm_148cfc859248fea87666537a7e52ff3d943e379730ff796e1e91d4e2d0ca04af
- clm_23d70d663bfdbfde2118e42a646d7cf5074e77fae68ab7ba849e2986f108f797
- clm_297282fa7f053d3a0a473513e571555c644e12b07fdcee8445db50113c17dd37
- clm_2b778e362b789acf06c003e9b25f5e597765d6c63ab65aca0828a993832ae22f
- clm_4192d1f20a41790de62927a8bf4e23e50a578911d424b6b5c161ae53da67143e
- clm_458eb8c35b488e7bbd5daeb0ea605e97f9f53dbdf6a981e784eea8dd052280f2
- clm_528cc5c643665c905dd3e157be0e367b6ab38dfc352531c99cbc5402e53ff779
- clm_9433e3f7348319bb6dce728194df4e95348727219e5bf8067ffa98bf1cdf21cc
- clm_a27e5781554a893e3a776cb10305633de0a19df1691c8c5eebb56741792b23e2
- clm_c50df9377a7b1a93d01457c261ada7523e340feb6608910be5495eeb8bc5e78f
- clm_c64f28cea96f70a75e0a55daecc1e11a85f6bdf279b23ab30c563ec0e12c7450
- clm_edfaf9164c195d4dd57e3b71427056ea3c327f61c72787fe02e9b8f40534fa48
maturity: draft
page_id: pg_5de9ca7f201854a78bcbbf149664f367
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3bd011bc315c56aaaa558de8bd0d9c1b
title: langchain-ai/openwiki/README.md @ e92cc11723a8
updated_at: '2026-09-14T04:04:40Z'
---

# langchain-ai/openwiki/README.md @ e92cc11723a8

<!-- rcw:begin owner=source:src_3bd011bc315c56aaaa558de8bd0d9c1b block=evidence -->
- Thirteen model providers are supported out of the box, including OpenAI (default, gpt-5.6-terra), Anthropic, Gemini, Bedrock, Copilot, OpenRouter, and any OpenAI-compatible endpoint via base URL and key. [@claim:clm_148cfc859248fea87666537a7e52ff3d943e379730ff796e1e91d4e2d0ca04af]
- Coding-agent integrations expose an MCP page-job lifecycle via tools named openwiki_begin, openwiki_submit_plan, openwiki_next_page, openwiki_inspect_page_claims, openwiki_submit_page, and openwiki_finish for Codex, Claude Code, OpenCode, and Cursor. [@claim:clm_23d70d663bfdbfde2118e42a646d7cf5074e77fae68ab7ba849e2986f108f797]
- Personal mode supports nine connectors (Custom MCP, Notion, Slack, Gmail, X, Web Search, Hacker News, LangSmith, local git); connector secrets are referenced by env var in ~/.openwiki/.env and never stored in config files. [@claim:clm_297282fa7f053d3a0a473513e571555c644e12b07fdcee8445db50113c17dd37]
- OpenWiki is a CLI that writes and maintains a wiki for a codebase or personal knowledge, generating linked Markdown intended as agent memory, with an interactive visualizer for humans. [@claim:clm_2b778e362b789acf06c003e9b25f5e597765d6c63ab65aca0828a993832ae22f]
- The tool offers two modes: a default 'code' wiki for the current repository written to openwiki/, and a 'personal' wiki for connected sources written to ~/.openwiki/wiki. [@claim:clm_4192d1f20a41790de62927a8bf4e23e50a578911d424b6b5c161ae53da67143e]
- Local state (credentials, personal wiki, connector data, history, skills) lives under ~/.openwiki by default, relocatable via OPENWIKI_CONFIG_DIR; the override does not move or delete the existing directory. [@claim:clm_458eb8c35b488e7bbd5daeb0ea605e97f9f53dbdf6a981e784eea8dd052280f2]
- Repository development practice: contributors adding another coding-agent integration are directed to follow the 'Adding a coding-agent integration' section of CONTRIBUTING.md. [@claim:clm_528cc5c643665c905dd3e157be0e367b6ab38dfc352531c99cbc5402e53ff779]
- Grounded Claims track material propositions in code wikis back to versioned repository evidence (e.g. repo:// paths with line ranges), stored as sidecars under openwiki/.claims/ rather than in the Markdown. [@claim:clm_9433e3f7348319bb6dce728194df4e95348727219e5bf8067ffa98bf1cdf21cc]
- Repository generation follows a resumable page-job lifecycle (begin, submit_plan, next_page, submit_page, finish) with a durable ordered queue checkpointed in openwiki/.run.json; each page becomes durable before advancing. [@claim:clm_a27e5781554a893e3a776cb10305633de0a19df1691c8c5eebb56741792b23e2]
- Per the README, host-driven coding-agent runs support only repository code wikis (not personal brains), use only repository source and tests (no connector context including LangSmith), and Grounded Claims apply only to repository evidence. [@claim:clm_c50df9377a7b1a93d01457c261ada7523e340feb6608910be5495eeb8bc5e78f]
- Output follows Open Knowledge Format (OKF) v0.2 with YAML front matter, generated/verified provenance stamps, validated optional trust and lifecycle fields, and reserved index.md and log.md documents. [@claim:clm_c64f28cea96f70a75e0a55daecc1e11a85f6bdf279b23ab30c563ec0e12c7450]
- The CLI requires Node.js 22 or newer, installs via npm, and depends on the better-sqlite3 native module, which on Windows may need Visual Studio Build Tools if installed with bun. [@claim:clm_edfaf9164c195d4dd57e3b71427056ea3c327f61c72787fe02e9b8f40534fa48]
<!-- rcw:end owner=source:src_3bd011bc315c56aaaa558de8bd0d9c1b block=evidence -->

## Researcher notes

