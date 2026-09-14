# vercel-labs/fx -- full detail

[Back to orientation](fx.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vercel-labs/fx/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/323053b52be3fa84.json](../../../wiki/dossiers/vercel-labs/fx/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/323053b52be3fa84.json)

## specifications (1 claim(s))

- [observation/documented] fx is a coding agent CLI written in Zig, distributed as a roughly 6.17 MiB native binary under the Apache-2.0 license, described as model-agnostic and embeddable. -- evidence: [README.md#L14-L14](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L14-L14), [README.md#L85-L85](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L85-L85) (`clm_fba3c0a30902b3aea9a62fafb23f54ab0a592adcbcb707d46c95504998de3a97`)

## components (1 claim(s))

- [observation/documented] Extensibility comprises skills (reusable instructions loaded on invocation), MCP for connecting external tools and servers, and subagents for delegating independent work. -- evidence: [README.md#L62-L64](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L62-L64) (`clm_6f22fb0f11157f905be50b3df9ff6449a8d73c7ef75bb46bc621769809939584`)

## design-choices (2 claim(s))

- [observation/documented] The interface is designed to stay closer to a Unix shell than an IDE in the terminal. -- evidence: [README.md#L14-L14](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L14-L14) (`clm_4348b5123ea401290c710a80f51e7d6b06bb45c3345199beee56b6b78f0057d1`)
- [observation/documented] Recent releases reduced the shell tool to three actions (down from twelve) and cut the subagent command surface to two commands, with Enter steering the active turn rather than queuing follow-ups. -- evidence: [CHANGELOG.md#L51-L58](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L51-L58) (`clm_0d7af5696e1878f6320d23b43e71ca65b68188f0133fc0c29a4fd814f376db1e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source requires Zig 0.16.0+, tests run with `zig build test`, and AGENTS.md requires contributors to run the built binary end to end and pass full CI before declaring work ready. -- evidence: [README.md#L81-L81](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L81-L81), [README.md#L74-L79](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L74-L79), [README.md#L72-L72](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L72-L72), [AGENTS.md#L11-L15](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/AGENTS.md#L11-L15), [AGENTS.md#L7-L7](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/AGENTS.md#L7-L7) (`clm_2a9135daa42faaabff26b6345911c271f80076227e99f077ba2a9e82a00b9d81`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Users sign in via `fx login` (Vercel AI Gateway), `fx login codex` (ChatGPT/Codex OAuth), `fx login grok` (xAI OAuth), or `fx setup` with an AI Gateway API key. -- evidence: [README.md#L26-L29](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L26-L29) (`clm_8e996eb882cdcbb69283f001b229899e4d1b9dd11b08c3b582e0de9bc469dac4`)
- [observation/documented] The CLI supports an interactive shell launched by running `fx` in a project, one-shot requests via `fx ask`, and `/help` inside the shell to browse interactive commands. -- evidence: [README.md#L44-L44](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L44-L44), [README.md#L31-L31](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L31-L31), [README.md#L33-L36](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L33-L36), [README.md#L40-L42](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L40-L42) (`clm_ec2cbb269dc71847f570650847e739c08db75d46f4b5f8f0e932147dc9524bcf`)
- [observation/documented] Embedding surfaces include `fx acp` for Agent Client Protocol clients, `createFxAgent()` for a JavaScript host via fx-core.wasm, and `createFxTerminal()` via fx-term.wasm; the WebAssembly SDK is described as experimental. -- evidence: [README.md#L56-L56](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L56-L56), [README.md#L50-L54](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L50-L54), [README.md#L48-L48](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L48-L48) (`clm_94ebef614fd57a05ec4a6ff738831e92cd2025e640256d2939802c0bd2c94c93`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Subagents can run with their own model and reasoning effort, keep running while the user steers, and accept mid-task feedback without interrupting their current tool. -- evidence: [CHANGELOG.md#L15-L20](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L15-L20), [CHANGELOG.md#L7-L7](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L7-L7) (`clm_ba98f3373e76dd23fe728d862baefb742ca82f9c1af9c30ed803aebd562fadee`)

## tools-permissions (1 claim(s))

- [observation/documented] The product has an auto mode that reviews each pending action, blocks cautioned or untrusted-output-derived actions, and supports full-access mode via `--full-access` or `/permissions full-access`. -- evidence: [CHANGELOG.md#L291-L298](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L291-L298), [CHANGELOG.md#L62-L74](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L62-L74), [CHANGELOG.md#L39-L41](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L39-L41) (`clm_84c5b043adbefafe74cbf15c3d4bbabbccdcf7a65fc3dd9b75a6bc288229f880`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The libfx npm package is stated to have no runtime dependencies, though host-supplied tools and MCP clients may bring their own. -- evidence: [CHANGELOG.md#L62-L74](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/CHANGELOG.md#L62-L74) (`clm_1dbd4240dc80b3a0a6aa6e904133b0e955db5c6089daa929c757e7dbd330a88d`)

## limitations (1 claim(s))

- [observation/documented] The README marks fx's status as experimental and tells users to use it at their own risk. -- evidence: [README.md#L1-L12](https://github.com/vercel-labs/fx/blob/e3ad6d8d645db2512cc9b2267fed2d4b9a5b3929/README.md#L1-L12) (`clm_e3f2c55c99d0a243f1fe0055c2bbbd4dc5be1d23577d4dce445f2ada20d6d1ae`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

