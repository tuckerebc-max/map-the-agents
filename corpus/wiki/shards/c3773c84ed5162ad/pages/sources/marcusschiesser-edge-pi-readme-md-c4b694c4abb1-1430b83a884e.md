---
access: public
aliases: []
claim_ids:
- clm_014ed5aa1174708bc93fcb7593ee46bb4fcafd84f05c3588dd31c34f9d6886bc
- clm_1ac1c5cf9b9d4c67b5cd3b6deaeeb5e25f2c5dde1ae1ab2abdb76107eb6ba8bf
- clm_633f2cbdd6d69285ebc9e8a15677228e1bae2ad5a90fc9e5498d7b09e26f8de8
- clm_be80024b9d295bc38041217eccdd4eae86261657a919461c580876ad7d6c955a
- clm_d4917f5b93f267eb7f12d19d69c5f015b87b5f82a279fe6d06a61aa9516e2da7
- clm_d874e68176a02760795f9054c986e252f513ceff1eb8f6955ed19524d1a8560e
maturity: draft
page_id: pg_d70589191d0d5d64a7931430b83a884e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2935ea53bbdb5469b681a0d0b3e804de
title: marcusschiesser/edge-pi/README.md @ c4b694c4abb1
updated_at: '2026-09-14T02:16:18Z'
---

# marcusschiesser/edge-pi/README.md @ c4b694c4abb1

<!-- rcw:begin owner=source:src_2935ea53bbdb5469b681a0d0b3e804de block=evidence -->
- Repository development practice: the README documents dev commands including npm install, build, check, ./test.sh (which skips LLM-dependent tests without API keys), and ./epi.sh from the repo root. [@claim:clm_014ed5aa1174708bc93fcb7593ee46bb4fcafd84f05c3588dd31c34f9d6886bc]
- The codebase is based on the pi coding agent by Mario Zechner, and the SDK is intentionally minimal with features that don't belong there directed to the CLI. [@claim:clm_1ac1c5cf9b9d4c67b5cd3b6deaeeb5e25f2c5dde1ae1ab2abdb76107eb6ba8bf]
- The `epi` CLI is a full-featured coding agent with multi-provider support and skills, described as a proof of concept for using the SDK. [@claim:clm_633f2cbdd6d69285ebc9e8a15677228e1bae2ad5a90fc9e5498d7b09e26f8de8]
- The project positions itself as an open replacement for Anthropic's proprietary Claude Agent SDK, working with any LLM provider via the Vercel AI SDK. [@claim:clm_be80024b9d295bc38041217eccdd4eae86261657a919461c580876ad7d6c955a]
- The CLI is installed globally via `npm install -g edge-pi-cli` and run with the `epi` command, with `epi --help` for more information. [@claim:clm_d4917f5b93f267eb7f12d19d69c5f015b87b5f82a279fe6d06a61aa9516e2da7]
- Edge-Pi is a lightweight coding agent library built on the Vercel AI SDK, providing primitives for tool support, session management, and context compaction. [@claim:clm_d874e68176a02760795f9054c986e252f513ceff1eb8f6955ed19524d1a8560e]
<!-- rcw:end owner=source:src_2935ea53bbdb5469b681a0d0b3e804de block=evidence -->

## Researcher notes

