---
access: public
aliases: []
claim_ids:
- clm_146399fc3688144856f263090d46a1f4d441553e884e95a7e95c7691bdc00609
- clm_1a94fe3c6379fc50ce50cc773aeede7472b8d2014ea577f5bc77649368b86f5b
- clm_2f67450b07cfa481c5c338f38141624a9e7d664ae5da3985fe5c912178eb319e
- clm_3e3a392edf6c35cdc48c5a4741c7c389ab410a4bd7f06c5a404f0cc6beeded04
- clm_4eb8156ad1fb9b441936e0edb5bc8f4a04dc11a25816e5092df8ad961d4da664
- clm_577d2811c621c3738641c66f8d2dc8ee879762bc786a10149675b20c36b90242
- clm_d7181f461def0da71713d81915062f8316dd29b3a557134c9598553c9ded3d68
- clm_dc3fd546d942ee9a6ac9881b9a1d280f59f5449b3f80534e90bb3db8cc0b256c
- clm_e0f7d93b06e0bd1e2093e92901cf070f0f9364ad3bd55382a7584d49535d17b0
- clm_e8724ed61f697fd8372577f308ad9f97abc4cff152566620d4b7d2c181619dc7
maturity: draft
page_id: pg_e858c536398058d39618560fc4a24516
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_89cee47acd5155e19a117e43fa4da1bc
title: haasonsaas/ocode/README.md @ b1877260448f
updated_at: '2026-09-14T02:01:28Z'
---

# haasonsaas/ocode/README.md @ b1877260448f

<!-- rcw:begin owner=source:src_89cee47acd5155e19a117e43fa4da1bc block=evidence -->
- OCode is described as a terminal-native AI coding assistant built to work with local Ollama models, offering codebase intelligence and autonomous task execution. [@claim:clm_146399fc3688144856f263090d46a1f4d441553e884e95a7e95c7691bdc00609]
- Runtime permissions are configurable via settings, including allow_file_read/write, allow_shell_exec, allow_git_ops, allowed_paths, blocked_paths, and blocked_commands such as rm and sudo. [@claim:clm_1a94fe3c6379fc50ce50cc773aeede7472b8d2014ea577f5bc77649368b86f5b]
- Required prerequisites are Python 3.8+ and pip; Ollama (a local LLM server) and Git are listed as needed for full functionality. [@claim:clm_2f67450b07cfa481c5c338f38141624a9e7d664ae5da3985fe5c912178eb319e]
- The README claims enhanced accuracy of over 97% for query categorization, though this is a documentation assertion not backed by visible benchmark code. [@claim:clm_3e3a392edf6c35cdc48c5a4741c7c389ab410a4bd7f06c5a404f0cc6beeded04]
- The product is invoked via a Python CLI (python -m ocode_python.core.cli) supporting interactive mode, single-prompt mode with -p, model selection with -m, and JSON/stream-json output formats. [@claim:clm_4eb8156ad1fb9b441936e0edb5bc8f4a04dc11a25816e5092df8ad961d4da664]
- The README describes multi-action query detection that maps compound prompts to multiple tools, plus context strategies (none/minimal/targeted/full) based on query complexity. [@claim:clm_577d2811c621c3738641c66f8d2dc8ee879762bc786a10149675b20c36b90242]
- An agent tool is included to delegate complex tasks to specialized agents, with the README noting agent delegation recommendations for multi-step workflows. [@claim:clm_d7181f461def0da71713d81915062f8316dd29b3a557134c9598553c9ded3d68]
- The toolset includes memory_tools for managing context and session memory. [@claim:clm_dc3fd546d942ee9a6ac9881b9a1d280f59f5449b3f80534e90bb3db8cc0b256c]
- MCP (Model Context Protocol) is described as an extensible plugin layer for third-party integrations, exposed via an mcp tool. [@claim:clm_e0f7d93b06e0bd1e2093e92901cf070f0f9364ad3bd55382a7584d49535d17b0]
- Behavior is configurable through environment variables including OCODE_MODEL, OLLAMA_HOST, OCODE_VERBOSE, OCODE_TEMPERATURE, and OCODE_TIMEOUT. [@claim:clm_e8724ed61f697fd8372577f308ad9f97abc4cff152566620d4b7d2c181619dc7]
<!-- rcw:end owner=source:src_89cee47acd5155e19a117e43fa4da1bc block=evidence -->

## Researcher notes

