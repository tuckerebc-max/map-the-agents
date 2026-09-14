---
access: public
aliases: []
claim_ids:
- clm_099082f07bdb315eecdcc3d50ba5b12d3152c565a801e35af738e4a9eeecd762
- clm_5df5b5b5ef74aa6507e9d1454cb137621463f568fe1c2b0cba365791ebfefc09
- clm_7d6ea39a5c50e14ed3924750d8deebb4fa199c2fb9501999c0678a699c5134b1
- clm_96c4a780c56b7a32c8b44d7eb2e6282fb754ae1f7bf75823c3e4c8682c47b842
- clm_b0a665ddba84b0d87fd379142b2c9445a3515344894df309edf700d15d0b589f
- clm_be5789e3606addf335ee91c9b73aaf65aea9939b23dddae369299f712a9f7ce7
- clm_d73d855348374f9995046065c626215ceb29a5ebe9ec48af5c192c80170bd73e
- clm_d974dcbb7c4d1b2c1c703779076e7e9df599cf6ac3ee34675ca6fbbd68b01d13
- clm_e6060cdccd54b12977c700a83f48032e1152b9a1074ed494e3507f84d5e57dcf
maturity: draft
page_id: pg_985c1f7296445d368ae4e1a269e7c122
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_567d07ebac005a49b46373de9f30afed
title: narenmanoharan/gpt-code-assistant/README.md @ 2bd455a16993
updated_at: '2026-09-14T04:11:39Z'
---

# narenmanoharan/gpt-code-assistant/README.md @ 2bd455a16993

<!-- rcw:begin owner=source:src_567d07ebac005a49b46373de9f30afed block=evidence -->
- The package is installable via pip as gpt-code-assistant. [@claim:clm_099082f07bdb315eecdcc3d50ba5b12d3152c565a801e35af738e4a9eeecd762]
- The tool is designed to work directly on any local codebase and claims language-agnostic support for multiple programming languages. [@claim:clm_5df5b5b5ef74aa6507e9d1454cb137621463f568fe1c2b0cba365791ebfefc09]
- The tool uses OpenAI's API; it prompts the user to configure OPENAI_API_KEY if not already set, and defaults to the gpt-3.5-turbo-16k model. [@claim:clm_7d6ea39a5c50e14ed3924750d8deebb4fa199c2fb9501999c0678a699c5134b1]
- Per the roadmap, support for additional models (Claude, Bedrock), local models (Llama2, Starcoder), code generation saved to files, and multi-codebase search are planned but not yet implemented. [@claim:clm_96c4a780c56b7a32c8b44d7eb2e6282fb754ae1f7bf75823c3e4c8682c47b842]
- The selected model is persisted in $HOME/.gpt-code-assistant/config.toml. [@claim:clm_b0a665ddba84b0d87fd379142b2c9445a3515344894df309edf700d15d0b589f]
- The tool is described as privacy-centric: code snippets are only sent when a question is asked and the LLM requests relevant code, though snippets are shared with OpenAI. [@claim:clm_be5789e3606addf335ee91c9b73aaf65aea9939b23dddae369299f712a9f7ce7]
- Documentation advises that mentioning a specific file name or keywords in a query improves search accuracy. [@claim:clm_d73d855348374f9995046065c626215ceb29a5ebe9ec48af5c192c80170bd73e]
- The product is a terminal CLI named gpt-code-assistant with subcommands including create-project, query, list-projects, refresh-project, delete-project, and select-model. [@claim:clm_d974dcbb7c4d1b2c1c703779076e7e9df599cf6ac3ee34675ca6fbbd68b01d13]
- Creating a project indexes all files by generating embeddings for each file and storing them in a local database. [@claim:clm_e6060cdccd54b12977c700a83f48032e1152b9a1074ed494e3507f84d5e57dcf]
<!-- rcw:end owner=source:src_567d07ebac005a49b46373de9f30afed block=evidence -->

## Researcher notes

