# langchain-ai/openwiki -- full detail

[Back to orientation](openwiki.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/langchain-ai/openwiki/e92cc11723a852b05b7983ab1a61feab96d75ba9/33a575400f233391.json](../../../wiki/dossiers/langchain-ai/openwiki/e92cc11723a852b05b7983ab1a61feab96d75ba9/33a575400f233391.json)

## specifications (1 claim(s))

- [observation/documented] OpenWiki is a CLI that writes and maintains a wiki for a codebase or personal knowledge, generating linked Markdown intended as agent memory, with an interactive visualizer for humans. -- evidence: [README.md#L19-L19](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L19-L19) (`clm_2b778e362b789acf06c003e9b25f5e597765d6c63ab65aca0828a993832ae22f`)

## components (2 claim(s))

- [observation/documented] Grounded Claims track material propositions in code wikis back to versioned repository evidence (e.g. repo:// paths with line ranges), stored as sidecars under openwiki/.claims/ rather than in the Markdown. -- evidence: [README.md#L141-L141](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L141-L141), [README.md#L256-L260](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L256-L260), [README.md#L147-L147](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L147-L147) (`clm_9433e3f7348319bb6dce728194df4e95348727219e5bf8067ffa98bf1cdf21cc`)
- [observation/documented] Personal mode supports nine connectors (Custom MCP, Notion, Slack, Gmail, X, Web Search, Hacker News, LangSmith, local git); connector secrets are referenced by env var in ~/.openwiki/.env and never stored in config files. -- evidence: [README.md#L205-L205](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L205-L205), [README.md#L231-L231](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L231-L231), [README.md#L23-L31](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L23-L31), [README.md#L220-L227](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L220-L227) (`clm_297282fa7f053d3a0a473513e571555c644e12b07fdcee8445db50113c17dd37`)

## design-choices (2 claim(s))

- [observation/documented] The tool offers two modes: a default 'code' wiki for the current repository written to openwiki/, and a 'personal' wiki for connected sources written to ~/.openwiki/wiki. -- evidence: [README.md#L155-L155](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L155-L155), [README.md#L23-L31](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L23-L31), [README.md#L157-L160](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L157-L160) (`clm_4192d1f20a41790de62927a8bf4e23e50a578911d424b6b5c161ae53da67143e`)
- [observation/documented] Output follows Open Knowledge Format (OKF) v0.2 with YAML front matter, generated/verified provenance stamps, validated optional trust and lifecycle fields, and reserved index.md and log.md documents. -- evidence: [README.md#L266-L273](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L266-L273), [README.md#L264-L264](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L264-L264) (`clm_c64f28cea96f70a75e0a55daecc1e11a85f6bdf279b23ab30c563ec0e12c7450`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors adding another coding-agent integration are directed to follow the 'Adding a coding-agent integration' section of CONTRIBUTING.md. -- evidence: [README.md#L136-L137](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L136-L137) (`clm_528cc5c643665c905dd3e157be0e367b6ab38dfc352531c99cbc5402e53ff779`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Coding-agent integrations expose an MCP page-job lifecycle via tools named openwiki_begin, openwiki_submit_plan, openwiki_next_page, openwiki_inspect_page_claims, openwiki_submit_page, and openwiki_finish for Codex, Claude Code, OpenCode, and Cursor. -- evidence: [README.md#L132-L132](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L132-L132), [README.md#L101-L101](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L101-L101) (`clm_23d70d663bfdbfde2118e42a646d7cf5074e77fae68ab7ba849e2986f108f797`)

## memory-state (1 claim(s))

- [observation/documented] Local state (credentials, personal wiki, connector data, history, skills) lives under ~/.openwiki by default, relocatable via OPENWIKI_CONFIG_DIR; the override does not move or delete the existing directory. -- evidence: [README.md#L166-L166](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L166-L166), [README.md#L172-L172](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L172-L172), [README.md#L168-L170](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L168-L170) (`clm_458eb8c35b488e7bbd5daeb0ea605e97f9f53dbdf6a981e784eea8dd052280f2`)

## orchestration (1 claim(s))

- [observation/documented] Repository generation follows a resumable page-job lifecycle (begin, submit_plan, next_page, submit_page, finish) with a durable ordered queue checkpointed in openwiki/.run.json; each page becomes durable before advancing. -- evidence: [README.md#L93-L93](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L93-L93), [README.md#L35-L39](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L35-L39) (`clm_a27e5781554a893e3a776cb10305633de0a19df1691c8c5eebb56741792b23e2`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The CLI requires Node.js 22 or newer, installs via npm, and depends on the better-sqlite3 native module, which on Windows may need Visual Studio Build Tools if installed with bun. -- evidence: [README.md#L88-L89](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L88-L89), [README.md#L45-L47](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L45-L47), [README.md#L43-L43](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L43-L43) (`clm_edfaf9164c195d4dd57e3b71427056ea3c327f61c72787fe02e9b8f40534fa48`)
- [observation/documented] Thirteen model providers are supported out of the box, including OpenAI (default, gpt-5.6-terra), Anthropic, Gemini, Bedrock, Copilot, OpenRouter, and any OpenAI-compatible endpoint via base URL and key. -- evidence: [README.md#L23-L31](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L23-L31), [README.md#L290-L290](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L290-L290), [README.md#L292-L303](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L292-L303) (`clm_148cfc859248fea87666537a7e52ff3d943e379730ff796e1e91d4e2d0ca04af`)

## limitations (1 claim(s))

- [observation/documented] Per the README, host-driven coding-agent runs support only repository code wikis (not personal brains), use only repository source and tests (no connector context including LangSmith), and Grounded Claims apply only to repository evidence. -- evidence: [README.md#L128-L128](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L128-L128), [README.md#L130-L130](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L130-L130), [README.md#L151-L151](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L151-L151) (`clm_c50df9377a7b1a93d01457c261ada7523e340feb6608910be5495eeb8bc5e78f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

