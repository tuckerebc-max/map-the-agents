---
access: public
aliases: []
claim_ids:
- clm_0fb80b7c5ffd4033f8b5bfa5ac966cdabae8348e74bc5b2e87b6ce11d579e87e
- clm_228b4a3194609922f2813dc53edb64053793c7088ecdfc7e1417a2609d2d6732
- clm_4093e63e6e0cd745ddf83a0bd786dbfe0f63a1ddd2b11fc6e28f74052ade1de6
- clm_5d406044367d6c19cb86b873658dd2e216bd63b562b32c60e313314d73ffe5f3
- clm_5f5a727a0edc02ee8dd327e9fdc33d10a18072ecf0a1e13b4612a0899ec3bcd8
- clm_6467f8619faa626f12ac47a1ca6cc73b1d69700690db57388608ff51478c1e00
- clm_6dcba29931165f0ee9fef12e7e9fe6b3bbc11b1358ffed8d9b0cb7a4a942d2bb
- clm_88e03ad132cd4d95f3effa2eb54227e836d78b101549893cceeafc8a1d4e5b49
- clm_af25437e6a02daac2584ba004d36a0d260936925024e9299ed1296e77036e8a0
- clm_c45cec12ed5223ca5a76bb581b62ad0822828b5fef2b3ad00738a21df0fa6500
- clm_ef60fa0b7dc535adeaeadb07cc5e3a9f6934d0466c8d381216fc178e0735f5de
- clm_f3ae85207f0a73be42641e008a5894607af24499110d8d84478ca1ab44938372
- clm_ff68c6a251949b027b4655a0ce016e1eb70fb9f8df12c525f4a302f0992b75dc
maturity: draft
page_id: pg_3a6db9eb8a735a1c893f97f917df59ad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb0dc7e39bd75445a7e8f2af49ccfeb8
title: synthetic-lab/octofriend/README.md @ 6b2159fc9829
updated_at: '2026-09-14T03:18:07Z'
---

# synthetic-lab/octofriend/README.md @ 6b2159fc9829

<!-- rcw:begin owner=source:src_eb0dc7e39bd75445a7e8f2af49ccfeb8 block=evidence -->
- Octo claims zero telemetry and works with any OpenAI-compatible API, Anthropic, or locally run LLMs. [@claim:clm_0fb80b7c5ffd4033f8b5bfa5ac966cdabae8348e74bc5b2e87b6ce11d579e87e]
- Behavior is configured through ~/.config/octofriend/octofriend.json5, covering search, model modalities, skills paths, MCP servers, LSP servers, and notifications. [@claim:clm_228b4a3194609922f2813dc53edb64053793c7088ecdfc7e1417a2609d2d6732]
- Octo optionally uses two custom open-sourced Hugging Face models (diff-apply and fix-json) to automatically handle tool-call and code-edit failures from the main coding LLM. [@claim:clm_4093e63e6e0cd745ddf83a0bd786dbfe0f63a1ddd2b11fc6e28f74052ade1de6]
- Octo is installed globally via npm as 'octofriend' and launched with either the 'octofriend' command or the short 'octo' alias. [@claim:clm_5d406044367d6c19cb86b873658dd2e216bd63b562b32c60e313314d73ffe5f3]
- MCP servers are declared in the config with a command and args (e.g. npx mcp-remote for Linear), and are shut down automatically when Octo exits. [@claim:clm_5f5a727a0edc02ee8dd327e9fdc33d10a18072ecf0a1e13b4612a0899ec3bcd8]
- Octo supports the Agent Skills spec (tagged Markdown with optional scripts), auto-detecting skills in ~/.config/agents/skills and per-repo .agents/skills, with extra paths configurable in the json5 config. [@claim:clm_6467f8619faa626f12ac47a1ca6cc73b1d69700690db57388608ff51478c1e00]
- Instruction files are discovered as OCTO.md, CLAUDE.md, or AGENTS.md; the first found wins, and rules from the current directory up through the home directory are merged, with a global file also possible in ~/.config/octofriend/OCTO.md. [@claim:clm_6dcba29931165f0ee9fef12e7e9fe6b3bbc11b1358ffed8d9b0cb7a4a942d2bb]
- Sessions can be resumed with 'octo --resume <session-id>', listed via 'octo session list', or switched in-app through a Ctrl+p 'Load previous session' menu; Docker sessions can be resumed with new docker run args. [@claim:clm_88e03ad132cd4d95f3effa2eb54227e836d78b101549893cceeafc8a1d4e5b49]
- Repository development practice: the repo ships a CONTRIBUTING.md describing contribution guidelines, and canary.sh/canary.fish scripts that contributors source to build and run 'main' as 'canary-octo'. [@claim:clm_af25437e6a02daac2584ba004d36a0d260936925024e9299ed1296e77036e8a0]
- When running inside Docker, shell commands and filesystem edits/reads happen in the container, but MCP servers and the built-in fetch tool still run and make HTTP requests from the host machine. [@claim:clm_c45cec12ed5223ca5a76bb581b62ad0822828b5fef2b3ad00738a21df0fa6500]
- Conversations are automatically saved per-directory, and Octo replaced rolling history windows with autocompaction for long-context tasks to improve prompt cache hit rates. [@claim:clm_ef60fa0b7dc535adeaeadb07cc5e3a9f6934d0466c8d381216fc178e0735f5de]
- Octo auto-detects installed language servers (e.g. typescript-language-server, gopls, rust-analyzer) and exposes IDE-grade navigation tools with no configuration; custom LSP entries override built-ins, and LSP can be disabled entirely or per-server. [@claim:clm_f3ae85207f0a73be42641e008a5894607af24499110d8d84478ca1ab44938372]
- Docker subcommands exist: 'octo docker connect <container>' attaches to a running container, and 'octo docker run -- <args>' launches a container that shuts down when Octo quits. [@claim:clm_ff68c6a251949b027b4655a0ce016e1eb70fb9f8df12c525f4a302f0992b75dc]
<!-- rcw:end owner=source:src_eb0dc7e39bd75445a7e8f2af49ccfeb8 block=evidence -->

## Researcher notes

