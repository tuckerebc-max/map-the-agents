---
access: public
aliases: []
claim_ids:
- clm_2a9135daa42faaabff26b6345911c271f80076227e99f077ba2a9e82a00b9d81
- clm_4348b5123ea401290c710a80f51e7d6b06bb45c3345199beee56b6b78f0057d1
- clm_6f22fb0f11157f905be50b3df9ff6449a8d73c7ef75bb46bc621769809939584
- clm_8e996eb882cdcbb69283f001b229899e4d1b9dd11b08c3b582e0de9bc469dac4
- clm_94ebef614fd57a05ec4a6ff738831e92cd2025e640256d2939802c0bd2c94c93
- clm_e3f2c55c99d0a243f1fe0055c2bbbd4dc5be1d23577d4dce445f2ada20d6d1ae
- clm_ec2cbb269dc71847f570650847e739c08db75d46f4b5f8f0e932147dc9524bcf
- clm_fba3c0a30902b3aea9a62fafb23f54ab0a592adcbcb707d46c95504998de3a97
maturity: draft
page_id: pg_0516707bce035d3faf6da55972893bea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a804f686c51757aaa6e5ba09b42b3c2f
title: vercel-labs/fx/README.md @ e3ad6d8d645d
updated_at: '2026-09-14T04:40:43Z'
---

# vercel-labs/fx/README.md @ e3ad6d8d645d

<!-- rcw:begin owner=source:src_a804f686c51757aaa6e5ba09b42b3c2f block=evidence -->
- Repository development practice: building from source requires Zig 0.16.0+, tests run with `zig build test`, and AGENTS.md requires contributors to run the built binary end to end and pass full CI before declaring work ready. [@claim:clm_2a9135daa42faaabff26b6345911c271f80076227e99f077ba2a9e82a00b9d81]
- The interface is designed to stay closer to a Unix shell than an IDE in the terminal. [@claim:clm_4348b5123ea401290c710a80f51e7d6b06bb45c3345199beee56b6b78f0057d1]
- Extensibility comprises skills (reusable instructions loaded on invocation), MCP for connecting external tools and servers, and subagents for delegating independent work. [@claim:clm_6f22fb0f11157f905be50b3df9ff6449a8d73c7ef75bb46bc621769809939584]
- Users sign in via `fx login` (Vercel AI Gateway), `fx login codex` (ChatGPT/Codex OAuth), `fx login grok` (xAI OAuth), or `fx setup` with an AI Gateway API key. [@claim:clm_8e996eb882cdcbb69283f001b229899e4d1b9dd11b08c3b582e0de9bc469dac4]
- Embedding surfaces include `fx acp` for Agent Client Protocol clients, `createFxAgent()` for a JavaScript host via fx-core.wasm, and `createFxTerminal()` via fx-term.wasm; the WebAssembly SDK is described as experimental. [@claim:clm_94ebef614fd57a05ec4a6ff738831e92cd2025e640256d2939802c0bd2c94c93]
- The README marks fx's status as experimental and tells users to use it at their own risk. [@claim:clm_e3f2c55c99d0a243f1fe0055c2bbbd4dc5be1d23577d4dce445f2ada20d6d1ae]
- The CLI supports an interactive shell launched by running `fx` in a project, one-shot requests via `fx ask`, and `/help` inside the shell to browse interactive commands. [@claim:clm_ec2cbb269dc71847f570650847e739c08db75d46f4b5f8f0e932147dc9524bcf]
- fx is a coding agent CLI written in Zig, distributed as a roughly 6.17 MiB native binary under the Apache-2.0 license, described as model-agnostic and embeddable. [@claim:clm_fba3c0a30902b3aea9a62fafb23f54ab0a592adcbcb707d46c95504998de3a97]
<!-- rcw:end owner=source:src_a804f686c51757aaa6e5ba09b42b3c2f block=evidence -->

## Researcher notes

