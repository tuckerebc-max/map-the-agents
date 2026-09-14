---
access: public
aliases: []
claim_ids:
- clm_0105fcfcb789980bfd314e0a1e4a176dd9003de8ebea043a7fd7f76f0d53f9ca
- clm_16fa087c47745e91a803a9d6535e1fbaa7e70826303e4b12a999419ee1e28586
- clm_2348926268771b6b5835090c70c036e89764e800a95d7690d65ec6f7083676c3
- clm_333378e7c8a28c44c6a94f39c4bc55565bac508cf29fc7a1b0dbfcf190ef531d
- clm_72ba22218f6adefa5aa6e43927134351a579d4e6971a5150baaa9d92b36e2b40
- clm_7b5ccd553c40fc7bba18d94f85e3c4e845f37cb9482763baf41a1e42e800c593
- clm_7df8aa6129c53f1d4841613d15f3cf72d417f0c6262aeddfe4f18ca0b4db50d2
- clm_9f19a86280dc393eb4e4e237733611ab2d8b5a400bd855785a325acf8255da43
- clm_bb0d8b5375f0971e262fb58b4faf497d70d400793eb8d39f91e00b04244693bb
- clm_e8b6b692ae46bef69eb47814217476045a01a632b8ed057a4a791f9db254830b
maturity: draft
page_id: pg_4de467d49c015ee89baadc2e21850a70
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b7c4790bbc7f56018b74c94f6233188b
title: lnxpy/hey/README.md @ 9b1b2ab680a4
updated_at: '2026-09-14T04:06:54Z'
---

# lnxpy/hey/README.md @ 9b1b2ab680a4

<!-- rcw:begin owner=source:src_b7c4790bbc7f56018b74c94f6233188b block=evidence -->
- Configuration is managed via `hey config create` to generate a base config file and `hey config edit` to view and edit it. [@claim:clm_0105fcfcb789980bfd314e0a1e4a176dd9003de8ebea043a7fd7f76f0d53f9ca]
- A `hey auth` command sets the LLM service token after installation. [@claim:clm_16fa087c47745e91a803a9d6535e1fbaa7e70826303e4b12a999419ee1e28586]
- The README recommends free tokens from mdb.ai but notes users are not limited to it and can point Hey at any other LLM service. [@claim:clm_2348926268771b6b5835090c70c036e89764e800a95d7690d65ec6f7083676c3]
- Configuration parameters include service URL, model (default gpt-3.5-turbo), a system prompt, code-block theme, loading text and spinner, and a never_style option to disable output styling for copying. [@claim:clm_333378e7c8a28c44c6a94f39c4bc55565bac508cf29fc7a1b0dbfcf190ef531d]
- The loading spinner feature appears to rely on the Rich library, since the config comment points users to `python -m rich.spinner` for the full spinner list. [@claim:clm_72ba22218f6adefa5aa6e43927134351a579d4e6971a5150baaa9d92b36e2b40]
- The CLI provides an `ask` sub-command for quick questions, e.g. `hey ask "..."`, and `--help` to list commands and sub-commands. [@claim:clm_7b5ccd553c40fc7bba18d94f85e3c4e845f37cb9482763baf41a1e42e800c593]
- Hey is a CLI-based AI assistant powered by LLMs, and users can choose which LLM service it connects to. [@claim:clm_7df8aa6129c53f1d4841613d15f3cf72d417f0c6262aeddfe4f18ca0b4db50d2]
- The package is installable from PyPI as hey-mindsdb, or directly from the GitHub repository via pip. [@claim:clm_9f19a86280dc393eb4e4e237733611ab2d8b5a400bd855785a325acf8255da43]
- The tool requires pip and Python 3.8 or newer on the user's machine. [@claim:clm_bb0d8b5375f0971e262fb58b4faf497d70d400793eb8d39f91e00b04244693bb]
- Running bare `hey` opens the default $EDITOR for composing longer questions; if unset, it falls back to vim on Unix-like systems and notepad on Windows. [@claim:clm_e8b6b692ae46bef69eb47814217476045a01a632b8ed057a4a791f9db254830b]
<!-- rcw:end owner=source:src_b7c4790bbc7f56018b74c94f6233188b block=evidence -->

## Researcher notes

