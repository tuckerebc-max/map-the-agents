---
access: public
aliases: []
claim_ids:
- clm_0a8f2ed8d91143e3862b012d60017f63e61219e7ce9a59100337d38f64372551
- clm_0ee0b3505e206d9e8594b6ff74894fe1608d6bd77fb57d42aef12c08d36042c2
- clm_0ef5444d3de449ce87a39657254757fd527bfaa1ed0706c5f57dcf72625475af
- clm_18c28a839b5b8ccec163d0d2bed44c0c11e38a7b2225a494755ad193793bb01b
- clm_1aa3064b6c5a8d0ab28891fff901ba6d203e7b79cc787d8a1951a54a3653f1c6
- clm_1faa8ee252ea242c6df1ca7778b4198e7e68eb812926eba3571d137153babe38
- clm_2d901df74540148a0e3fc66e1f77a465a38d55f28e23e4ace3d0e8877ba662a6
- clm_5be491f29429e4b078e517657dcb78565eb9b4b8a4d515f7fcde9a65579d91e8
- clm_64597b60f8efe53f351ca63ab3613b5e86b38a194392d4fa05e18cbf35b423fd
- clm_69221903dc71a12bf3242c8a1a0bdb1344446579c4006795d559871c70772896
- clm_74000dd14bfee9a144ffe8030077dfacbd4376a9e048db9817b172fc2431031c
- clm_95ca6ddd9542e680f564169bbca1ee0fdb45ec3e4931b540210793a5ba2fc396
- clm_96765caec6bd0b77b087ca5ff83348a3b05312b251ae5912458580cc8bf52175
- clm_cf1df6c63239e22ced3a71c067ea8eff848867adb141fedca4998616869dabff
- clm_e493b12851c8cfa896f657a81bf1edf8fee99d43aa80d73b53adaa087982b1af
maturity: draft
page_id: pg_f4ddd62ab0005909957bd226c45ced41
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fbb6be333bfb593d9b07b2e1862f473f
title: Legorobotdude/PrivateCode/README.md @ b7d665774224
updated_at: '2026-09-14T02:12:35Z'
---

# Legorobotdude/PrivateCode/README.md @ b7d665774224

<!-- rcw:begin owner=source:src_fbb6be333bfb593d9b07b2e1862f473f block=evidence -->
- The model: prefix switches the active Ollama model at runtime, and timeout:N adjusts the LLM operation timeout. [@claim:clm_0a8f2ed8d91143e3862b012d60017f63e61219e7ce9a59100337d38f64372551]
- The product is a terminal coding assistant using local LLMs via Ollama for coding help, web search, file editing, and command execution with user confirmation. [@claim:clm_0ee0b3505e206d9e8594b6ff74894fe1608d6bd77fb57d42aef12c08d36042c2]
- The create: prefix makes new empty files with confirmation, supports multiple files at once, auto-creates missing directories, and prompts before overwriting existing files. [@claim:clm_0ef5444d3de449ce87a39657254757fd527bfaa1ed0706c5f57dcf72625475af]
- File edits always require user confirmation, and a .bak backup is created before modifying any file. [@claim:clm_18c28a839b5b8ccec163d0d2bed44c0c11e38a7b2225a494755ad193793bb01b]
- Thinking blocks let the model include reasoning in responses, hidden by default, with thinking:on/off and thinking:length N commands controlling display and length. [@claim:clm_1aa3064b6c5a8d0ab28891fff901ba6d203e7b79cc787d8a1951a54a3653f1c6]
- Queries prefixed with search: perform web searches, and URLs in square brackets are fetched for reference content; search can be combined with file context. [@claim:clm_1faa8ee252ea242c6df1ca7778b4198e7e68eb812926eba3571d137153babe38]
- The plan:/vibecode: feature has the LLM break a request into JSON-formatted executable steps (file creation, code writing, edits, commands, output verification), each confirmed interactively and optionally saved to a JSON file. [@claim:clm_2d901df74540148a0e3fc66e1f77a465a38d55f28e23e4ace3d0e8877ba662a6]
- Defaults are configurable in code_assistant.py, including DEFAULT_MODEL, MAX_SEARCH_RESULTS (5), MAX_URL_CONTENT_LENGTH (10000), SHOW_THINKING (False), and DEFAULT_TIMEOUT (500 seconds). [@claim:clm_5be491f29429e4b078e517657dcb78565eb9b4b8a4d515f7fcde9a65579d91e8]
- Editing a nonexistent file prompts to create it, allowing file creation and editing in a single step. [@claim:clm_64597b60f8efe53f351ca63ab3613b5e86b38a194392d4fa05e18cbf35b423fd]
- Partial file reading supports line-range syntax [file:start-end], [file:start-], [file:-end], and [file:line], with 1-indexed line numbers. [@claim:clm_69221903dc71a12bf3242c8a1a0bdb1344446579c4006795d559871c70772896]
- Users include file context by placing file paths in square brackets in queries, and multiple files can be included in one question. [@claim:clm_74000dd14bfee9a144ffe8030077dfacbd4376a9e048db9817b172fc2431031c]
- The edit: prefix requests file edits; the assistant shows a diff of proposed changes and asks for confirmation before saving. [@claim:clm_95ca6ddd9542e680f564169bbca1ee0fdb45ec3e4931b540210793a5ba2fc396]
- Conversation history is maintained for context during a session but is not saved between sessions. [@claim:clm_96765caec6bd0b77b087ca5ff83348a3b05312b251ae5912458580cc8bf52175]
- Commands are checked against a list of safe prefixes, dangerous commands trigger extra warnings, and every command requires explicit user confirmation before execution. [@claim:clm_cf1df6c63239e22ced3a71c067ea8eff848867adb141fedca4998616869dabff]
- The project requires Python 3.6+, a locally running Ollama instance with a pulled code LLM (e.g., codellama, llama2, mixtral), and optionally an internet connection for web search. [@claim:clm_e493b12851c8cfa896f657a81bf1edf8fee99d43aa80d73b53adaa087982b1af]
<!-- rcw:end owner=source:src_fbb6be333bfb593d9b07b2e1862f473f block=evidence -->

## Researcher notes

