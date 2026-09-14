---
access: public
aliases: []
claim_ids:
- clm_0dc8a7d58adfd1cf75c43ef90d9e8bc504bd4636458b46ec6b9d6382f7dac32e
- clm_5d406044367d6c19cb86b873658dd2e216bd63b562b32c60e313314d73ffe5f3
- clm_5f5a727a0edc02ee8dd327e9fdc33d10a18072ecf0a1e13b4612a0899ec3bcd8
- clm_6467f8619faa626f12ac47a1ca6cc73b1d69700690db57388608ff51478c1e00
- clm_7844742e6069f28b5fa0671464002eedddfd69a83d1ae9d19a375976dee88a6b
- clm_af25437e6a02daac2584ba004d36a0d260936925024e9299ed1296e77036e8a0
- clm_db651db9419c97cc6c9acd6e4d6044d802f9a1c736593cf8b6cd53bf11252dbf
- clm_ef60fa0b7dc535adeaeadb07cc5e3a9f6934d0466c8d381216fc178e0735f5de
- clm_ff68c6a251949b027b4655a0ce016e1eb70fb9f8df12c525f4a302f0992b75dc
maturity: draft
page_id: pg_9ace87d7b7925590929e28561271dfeb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cab459e02f765d4a8d7a7f2fabdc17a8
title: synthetic-lab/octofriend/CHANGELOG.md @ 6b2159fc9829
updated_at: '2026-09-14T03:18:07Z'
---

# synthetic-lab/octofriend/CHANGELOG.md @ 6b2159fc9829

<!-- rcw:begin owner=source:src_cab459e02f765d4a8d7a7f2fabdc17a8 block=evidence -->
- New grep and glob tools search files without permission prompts, while in Collaboration Mode the fetch tool requires explicit permission to prevent prompt-injection exfiltration; tools can be whitelisted to skip prompting. [@claim:clm_0dc8a7d58adfd1cf75c43ef90d9e8bc504bd4636458b46ec6b9d6382f7dac32e]
- Octo is installed globally via npm as 'octofriend' and launched with either the 'octofriend' command or the short 'octo' alias. [@claim:clm_5d406044367d6c19cb86b873658dd2e216bd63b562b32c60e313314d73ffe5f3]
- MCP servers are declared in the config with a command and args (e.g. npx mcp-remote for Linear), and are shut down automatically when Octo exits. [@claim:clm_5f5a727a0edc02ee8dd327e9fdc33d10a18072ecf0a1e13b4612a0899ec3bcd8]
- Octo supports the Agent Skills spec (tagged Markdown with optional scripts), auto-detecting skills in ~/.config/agents/skills and per-repo .agents/skills, with extra paths configurable in the json5 config. [@claim:clm_6467f8619faa626f12ac47a1ca6cc73b1d69700690db57388608ff51478c1e00]
- The changelog notes a Rust-based rendering backend called Paintcannon used for the terminal UI. [@claim:clm_7844742e6069f28b5fa0671464002eedddfd69a83d1ae9d19a375976dee88a6b]
- Repository development practice: the repo ships a CONTRIBUTING.md describing contribution guidelines, and canary.sh/canary.fish scripts that contributors source to build and run 'main' as 'canary-octo'. [@claim:clm_af25437e6a02daac2584ba004d36a0d260936925024e9299ed1296e77036e8a0]
- An 'octo bench tps' subcommand benchmarks tokens-per-second from the configured API provider, with optional --model, --concurrency, custom prompt, and time-to-first-token/inter-token latency metrics. [@claim:clm_db651db9419c97cc6c9acd6e4d6044d802f9a1c736593cf8b6cd53bf11252dbf]
- Conversations are automatically saved per-directory, and Octo replaced rolling history windows with autocompaction for long-context tasks to improve prompt cache hit rates. [@claim:clm_ef60fa0b7dc535adeaeadb07cc5e3a9f6934d0466c8d381216fc178e0735f5de]
- Docker subcommands exist: 'octo docker connect <container>' attaches to a running container, and 'octo docker run -- <args>' launches a container that shuts down when Octo quits. [@claim:clm_ff68c6a251949b027b4655a0ce016e1eb70fb9f8df12c525f4a302f0992b75dc]
<!-- rcw:end owner=source:src_cab459e02f765d4a8d7a7f2fabdc17a8 block=evidence -->

## Researcher notes

