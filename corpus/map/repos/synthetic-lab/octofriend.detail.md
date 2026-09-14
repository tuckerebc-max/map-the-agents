# synthetic-lab/octofriend -- full detail

[Back to orientation](octofriend.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/synthetic-lab/octofriend/6b2159fc9829edac98484803a55720318987319f/00d502e0d3cc130a.json](../../../wiki/dossiers/synthetic-lab/octofriend/6b2159fc9829edac98484803a55720318987319f/00d502e0d3cc130a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Octo optionally uses two custom open-sourced Hugging Face models (diff-apply and fix-json) to automatically handle tool-call and code-edit failures from the main coding LLM. -- evidence: [README.md#L22-L31](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L22-L31) (`clm_4093e63e6e0cd745ddf83a0bd786dbfe0f63a1ddd2b11fc6e28f74052ade1de6`)
- [observation/documented] Octo auto-detects installed language servers (e.g. typescript-language-server, gopls, rust-analyzer) and exposes IDE-grade navigation tools with no configuration; custom LSP entries override built-ins, and LSP can be disabled entirely or per-server. -- evidence: [README.md#L321-L323](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L321-L323), [README.md#L316-L317](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L316-L317), [README.md#L292-L296](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L292-L296), [README.md#L298-L300](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L298-L300), [README.md#L325-L329](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L325-L329), [README.md#L286-L290](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L286-L290) (`clm_f3ae85207f0a73be42641e008a5894607af24499110d8d84478ca1ab44938372`)

## design-choices (2 claim(s))

- [observation/documented] Octo claims zero telemetry and works with any OpenAI-compatible API, Anthropic, or locally run LLMs. -- evidence: [README.md#L1-L2](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L1-L2), [README.md#L33-L36](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L33-L36), [README.md#L22-L31](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L22-L31) (`clm_0fb80b7c5ffd4033f8b5bfa5ac966cdabae8348e74bc5b2e87b6ce11d579e87e`)
- [observation/documented] Instruction files are discovered as OCTO.md, CLAUDE.md, or AGENTS.md; the first found wins, and rules from the current directory up through the home directory are merged, with a global file also possible in ~/.config/octofriend/OCTO.md. -- evidence: [README.md#L175-L177](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L175-L177), [README.md#L185-L186](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L185-L186), [README.md#L179-L183](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L179-L183), [README.md#L169-L169](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L169-L169), [README.md#L171-L173](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L171-L173) (`clm_6dcba29931165f0ee9fef12e7e9fe6b3bbc11b1358ffed8d9b0cb7a4a942d2bb`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the repo ships a CONTRIBUTING.md describing contribution guidelines, and canary.sh/canary.fish scripts that contributors source to build and run 'main' as 'canary-octo'. -- evidence: [README.md#L409-L410](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L409-L410), [CHANGELOG.md#L89-L89](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L89-L89), [CHANGELOG.md#L85-L87](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L85-L87) (`clm_af25437e6a02daac2584ba004d36a0d260936925024e9299ed1296e77036e8a0`)

## skills-patterns (1 claim(s))

- [observation/documented] Octo supports the Agent Skills spec (tagged Markdown with optional scripts), auto-detecting skills in ~/.config/agents/skills and per-repo .agents/skills, with extra paths configurable in the json5 config. -- evidence: [README.md#L242-L248](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L242-L248), [README.md#L239-L240](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L239-L240), [CHANGELOG.md#L135-L136](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L135-L136), [README.md#L233-L237](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L233-L237), [README.md#L190-L196](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L190-L196), [README.md#L231-L231](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L231-L231) (`clm_6467f8619faa626f12ac47a1ca6cc73b1d69700690db57388608ff51478c1e00`)

## interfaces (4 claim(s))

- [observation/documented] Octo is installed globally via npm as 'octofriend' and launched with either the 'octofriend' command or the short 'octo' alias. -- evidence: [README.md#L6-L8](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L6-L8), [README.md#L15-L16](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L15-L16), [CHANGELOG.md#L418-L418](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L418-L418), [README.md#L12-L13](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L12-L13) (`clm_5d406044367d6c19cb86b873658dd2e216bd63b562b32c60e313314d73ffe5f3`)
- [observation/documented] Sessions can be resumed with 'octo --resume <session-id>', listed via 'octo session list', or switched in-app through a Ctrl+p 'Load previous session' menu; Docker sessions can be resumed with new docker run args. -- evidence: [README.md#L76-L78](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L76-L78), [README.md#L91-L95](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L91-L95), [README.md#L80-L82](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L80-L82), [README.md#L101-L103](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L101-L103), [README.md#L87-L89](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L87-L89) (`clm_88e03ad132cd4d95f3effa2eb54227e836d78b101549893cceeafc8a1d4e5b49`)
- [observation/documented] Docker subcommands exist: 'octo docker connect <container>' attaches to a running container, and 'octo docker run -- <args>' launches a container that shuts down when Octo quits. -- evidence: [README.md#L150-L151](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L150-L151), [README.md#L145-L146](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L145-L146), [CHANGELOG.md#L363-L366](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L363-L366), [README.md#L139-L143](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L139-L143) (`clm_ff68c6a251949b027b4655a0ce016e1eb70fb9f8df12c525f4a302f0992b75dc`)
- [observation/documented] Behavior is configured through ~/.config/octofriend/octofriend.json5, covering search, model modalities, skills paths, MCP servers, LSP servers, and notifications. -- evidence: [README.md#L298-L300](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L298-L300), [README.md#L368-L370](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L368-L370), [README.md#L239-L240](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L239-L240), [README.md#L46-L48](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L46-L48), [README.md#L252-L258](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L252-L258), [README.md#L114-L115](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L114-L115) (`clm_228b4a3194609922f2813dc53edb64053793c7088ecdfc7e1417a2609d2d6732`)

## memory-state (1 claim(s))

- [observation/documented] Conversations are automatically saved per-directory, and Octo replaced rolling history windows with autocompaction for long-context tasks to improve prompt cache hit rates. -- evidence: [README.md#L76-L78](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L76-L78), [CHANGELOG.md#L23-L25](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L23-L25), [CHANGELOG.md#L150-L152](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L150-L152) (`clm_ef60fa0b7dc535adeaeadb07cc5e3a9f6934d0466c8d381216fc178e0735f5de`)

## orchestration (2 claim(s))

- [observation/documented] When running inside Docker, shell commands and filesystem edits/reads happen in the container, but MCP servers and the built-in fetch tool still run and make HTTP requests from the host machine. -- evidence: [README.md#L159-L165](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L159-L165) (`clm_c45cec12ed5223ca5a76bb581b62ad0822828b5fef2b3ad00738a21df0fa6500`)
- [observation/documented] MCP servers are declared in the config with a command and args (e.g. npx mcp-remote for Linear), and are shut down automatically when Octo exits. -- evidence: [README.md#L275-L282](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L275-L282), [README.md#L252-L258](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L252-L258), [README.md#L260-L271](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/README.md#L260-L271), [CHANGELOG.md#L229-L229](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L229-L229) (`clm_5f5a727a0edc02ee8dd327e9fdc33d10a18072ecf0a1e13b4612a0899ec3bcd8`)

## tools-permissions (1 claim(s))

- [observation/documented] New grep and glob tools search files without permission prompts, while in Collaboration Mode the fetch tool requires explicit permission to prevent prompt-injection exfiltration; tools can be whitelisted to skip prompting. -- evidence: [CHANGELOG.md#L35-L36](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L35-L36), [CHANGELOG.md#L64-L65](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L64-L65), [CHANGELOG.md#L111-L112](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L111-L112) (`clm_0dc8a7d58adfd1cf75c43ef90d9e8bc504bd4636458b46ec6b9d6382f7dac32e`)

## evaluation (1 claim(s))

- [observation/documented] An 'octo bench tps' subcommand benchmarks tokens-per-second from the configured API provider, with optional --model, --concurrency, custom prompt, and time-to-first-token/inter-token latency metrics. -- evidence: [CHANGELOG.md#L302-L302](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L302-L302), [CHANGELOG.md#L241-L242](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L241-L242), [CHANGELOG.md#L82-L83](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L82-L83), [CHANGELOG.md#L323-L326](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L323-L326) (`clm_db651db9419c97cc6c9acd6e4d6044d802f9a1c736593cf8b6cd53bf11252dbf`)

## dependencies (1 claim(s))

- [observation/documented] The changelog notes a Rust-based rendering backend called Paintcannon used for the terminal UI. -- evidence: [CHANGELOG.md#L45-L47](https://github.com/synthetic-lab/octofriend/blob/6b2159fc9829edac98484803a55720318987319f/CHANGELOG.md#L45-L47) (`clm_7844742e6069f28b5fa0671464002eedddfd69a83d1ae9d19a375976dee88a6b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

