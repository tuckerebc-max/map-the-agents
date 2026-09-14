---
access: public
aliases: []
claim_ids:
- clm_0b3a056311e989daf947b7caa3cd1ae1682fc22615e5ce23a6e55cd99b3fe7ff
- clm_2a38d9559b3b741bdaa06e734f7b3221b43cd041c00fc473e36c192379427a0a
- clm_3c7c4ad2b5103bf40b8561d79c921f82bb03942894df8d4eaf13a14f5c6e6b32
- clm_4ed23ddcbc03f3f6c674e8e600f5b5dd2f593266340e9f57e257c7bfd3a5c3be
- clm_77d6678623dd8b141f1382865910a300ba1b915fa8ed1189178c45413c446bed
- clm_9d921746b939c8d1966037af9b50f7e5cefe63e1c2bd32cbfee085b678aa89f8
- clm_a10df509f6f6fcb6df4aee8bb732524ce867ff7cfb08f75ab02f5a64fec1493c
- clm_aac25ea095e6a57f610dc7d102acaf65b600ee144660cf12e1d1ed226bc57422
- clm_abc8b65115441dd9d047a6433a1e36944cbf6cbe32ade01160de710671af6703
- clm_c9d11cfdbd4a4b0abbd50ab2e04c973f977c85a9bca96ebb8d0ef573ee24adc0
- clm_cb7e292e59de524ca91d765fdb90dcd08d4d004e75dc95cff20ced5ce7c01352
- clm_ce97dfe7885cb2c9f63e4f0a44f317884a99bc12761d61973c35326daf48b9f8
maturity: draft
page_id: pg_18f09296dd52529bae9ae2dc83abf22d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d591ee9fe69c573d86bb647d2e13f54e
title: AGI-is-going-to-arrive/ahadiff/README.md @ 36da35e9fd40
updated_at: '2026-09-14T03:31:49Z'
---

# AGI-is-going-to-arrive/ahadiff/README.md @ 36da35e9fd40

<!-- rcw:begin owner=source:src_d591ee9fe69c573d86bb647d2e13f54e block=evidence -->
- Snapshots store a sanitized copy of an earlier file for later comparison without modifying originals, and are learning references rather than full backups. [@claim:clm_0b3a056311e989daf947b7caa3cd1ae1682fc22615e5ce23a6e55cd99b3fe7ff]
- Learning history and review records are stored under .ahadiff/ in each working folder; API keys go into a scope-specific .env with an environment-variable reference in config.toml. [@claim:clm_2a38d9559b3b741bdaa06e734f7b3221b43cd041c00fc473e36c192379427a0a]
- Provider classes include openai, openai_responses, gemini, anthropic, azure, newapi, openai_compat, lmstudio, and ollama, covering local and remote LLM endpoints. [@claim:clm_3c7c4ad2b5103bf40b8561d79c921f82bb03942894df8d4eaf13a14f5c6e6b32]
- ahadiff serve creates local state and opens a WebUI at http://127.0.0.1:8765, with a --no-browser option; ordinary folders work while init and doctor target Git repositories. [@claim:clm_4ed23ddcbc03f3f6c674e8e600f5b5dd2f593266340e9f57e257c7bfd3a5c3be]
- The WebUI supports five learning sources: Git changes, two files, a pasted diff, a saved snapshot, or a single Markdown document, with local preview before a generation request. [@claim:clm_77d6678623dd8b141f1382865910a300ba1b915fa8ed1189178c45413c446bed]
- Repository development practice: building from source requires cloning the repo, running 'uv sync --locked --dev', and building the viewer with pnpm before an editable uv tool install. [@claim:clm_9d921746b939c8d1966037af9b50f7e5cefe63e1c2bd32cbfee085b678aa89f8]
- The tool does not execute exercise or notebook code; practice statistics reflect recorded attempts and self-assessments, not measured learning gain. [@claim:clm_a10df509f6f6fcb6df4aee8bb732524ce867ff7cfb08f75ab02f5a64fec1493c]
- Default privacy mode is strict_local; redacted_remote or explicit_remote must be chosen before remote providers, and the tool checks for secrets and suspicious instructions while advising user inspection. [@claim:clm_aac25ea095e6a57f610dc7d102acaf65b600ee144660cf12e1d1ed226bc57422]
- Documented limits: no PDF ingestion or web-page capture; directory comparison and Git hooks require macOS/Linux; browser-selected files capped at 256 KiB each (512 KiB per pair) and pasted diffs at 64 KiB. [@claim:clm_abc8b65115441dd9d047a6433a1e36944cbf6cbe32ade01160de710671af6703]
- Deterministic scoring covers eight dimensions with required evidence and safety checks; an optional LLM judge gives feedback but cannot override the final verdict. [@claim:clm_c9d11cfdbd4a4b0abbd50ab2e04c973f977c85a9bca96ebb8d0ef573ee24adc0]
- A read-only MCP server can be registered with tools like Claude or Codex via 'ahadiff mcp-server --repo-root /path/to/workspace'. [@claim:clm_cb7e292e59de524ca91d765fdb90dcd08d4d004e75dc95cff20ced5ce7c01352]
- Installable via pipx or uv tool; an optional 'optimizer' extra adds torch for FSRS parameter optimization, which base review and scheduling do not need. [@claim:clm_ce97dfe7885cb2c9f63e4f0a44f317884a99bc12761d61973c35326daf48b9f8]
<!-- rcw:end owner=source:src_d591ee9fe69c573d86bb647d2e13f54e block=evidence -->

## Researcher notes

