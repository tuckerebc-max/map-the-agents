---
access: public
aliases: []
claim_ids:
- clm_145836d0beb30ca5569c3981c915713a2a8ca1fb00a7baf035bc00654046f8b2
- clm_213984ff31c39f425659fcedf28a2d87a39721b2a5c175a981d972d28dc8ae7f
- clm_24dcbcbee0c12da42c957262f707352c027c7396f5b97dbcf240ae48b137acf6
- clm_34ae20392277f257008de74af2b8f58f37eee3067997cb9be87d382573626574
- clm_45e5d22019fdd444a92e0dcb68aa9ea0fd2a14026c039ecd8364160c0fd97fc2
- clm_510c3efe689bfbecbc6cd41ec8fe39e9ed787ec21b8edb9b5f880657259966cc
- clm_6fbb0121b7a8f435cf25d02d7b43de1b6b6e060cc973ba6f9bec9ddc7db98863
- clm_92d93707395d57482d26ea74abe6e78e22599b50543652e6292255078a21521e
- clm_f043110ee059a9ebdfcf68b8ee6300de8d7f94706f72ed48205b039949353c3b
maturity: draft
page_id: pg_0d7d2f7fe3e25a35a33528c82c27c5f2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8a967b80278f5a32a343355a1195f94f
title: CommandCodeAI/command-code/readme.md @ 5c8f1b48c9d6
updated_at: '2026-09-14T01:44:05Z'
---

# CommandCodeAI/command-code/readme.md @ 5c8f1b48c9d6

<!-- rcw:begin owner=source:src_8a967b80278f5a32a343355a1195f94f block=evidence -->
- The taste system is designed to treat every accept, reject, and edit as a signal that shapes a per-user taste profile. [@claim:clm_145836d0beb30ca5569c3981c915713a2a8ca1fb00a7baf035bc00654046f8b2]
- Taste rules are designed to be shareable across a team via `npx taste push/pull`, with the README stating that rules decay while taste compounds. [@claim:clm_213984ff31c39f425659fcedf28a2d87a39721b2a5c175a981d972d28dc8ae7f]
- The README describes a model called `taste-1` as the core of the product's taste architecture, which it says learns from the user and grows with them. [@claim:clm_24dcbcbee0c12da42c957262f707352c027c7396f5b97dbcf240ae48b137acf6]
- A `/feedback` slash command is documented for reporting issues from within the tool, alongside GitHub issues as an alternative channel. [@claim:clm_34ae20392277f257008de74af2b8f58f37eee3067997cb9be87d382573626574]
- The tool is distributed as the npm package `command-code`, installed with `npm i -g command-code`. [@claim:clm_45e5d22019fdd444a92e0dcb68aa9ea0fd2a14026c039ecd8364160c0fd97fc2]
- The docs site advertises workflow recipes pairing concrete scenarios with prompts and expected outcomes, suggesting a curated usage-pattern library, though only the link is in evidence. [@claim:clm_510c3efe689bfbecbc6cd41ec8fe39e9ed787ec21b8edb9b5f880657259966cc]
- The project is a coding agent positioned as building full-stack projects, fixing bugs, writing tests, and refactoring while adapting to the user's coding style. [@claim:clm_6fbb0121b7a8f435cf25d02d7b43de1b6b6e060cc973ba6f9bec9ddc7db98863]
- The product runs as a CLI: it is installed globally via npm and started inside a project with the `cmd` command. [@claim:clm_92d93707395d57482d26ea74abe6e78e22599b50543652e6292255078a21521e]
- Interactive sessions support typed prefixes: `/` opens a command menu, `!` enters Bash mode, and `@` triggers file-path mention autocomplete. [@claim:clm_f043110ee059a9ebdfcf68b8ee6300de8d7f94706f72ed48205b039949353c3b]
<!-- rcw:end owner=source:src_8a967b80278f5a32a343355a1195f94f block=evidence -->

## Researcher notes

