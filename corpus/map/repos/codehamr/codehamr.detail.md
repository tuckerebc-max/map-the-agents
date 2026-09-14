# codehamr/codehamr -- full detail

[Back to orientation](codehamr.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codehamr/codehamr/8ad8eae6cc57c2cd9941886334fcb960a370417d/3adff9ea9eb023a4.json](../../../wiki/dossiers/codehamr/codehamr/8ad8eae6cc57c2cd9941886334fcb960a370417d/3adff9ea9eb023a4.json)

## specifications (1 claim(s))

- [observation/documented] codehamr is described as a minimal coding agent for the terminal, built for local LLMs and also able to run against OpenAI-compatible endpoints. -- evidence: [README.md#L3-L4](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L3-L4) (`clm_06731ae1bf9be4a80775b4297bb526d6fb1627e95041a92d7607ce640c091bd7`)

## components (1 claim(s))

- [observation/documented] The agent works with four tools — bash, read_file, write_file, and edit_file — investigating the project directly rather than guessing. -- evidence: [README.md#L18-L23](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L18-L23) (`clm_b4d3375c1a8ab72fe4dc67d439b4a846c9c88e7a60c546a2603234128347dc3e`)

## design-choices (2 claim(s))

- [observation/documented] The design deliberately favors simplicity: three slash commands, one embedded system prompt, and no router, sub-agents, skill system, or MCP. -- evidence: [README.md#L15-L16](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L15-L16) (`clm_f44b5b0405ec7c5b12c29e4b696279af46c3380db6d592b93f5372b7d7f49a5c`)
- [observation/documented] Self-verification (running tests, compiling, loading the page) is instilled by the system prompt as a habit rather than a blocking gate; when a check cannot run, the agent reports 'unverified:' instead of pretending success. -- evidence: [README.md#L95-L95](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L95-L95), [README.md#L18-L23](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L18-L23) (`clm_4b7b754c0f0e3292dda630170bf04de8fa048a7ad9ce165ac5a154bc8a52908c`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The /models command lists configured model profiles, and /models <name> switches the active profile. -- evidence: [README.md#L81-L81](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L81-L81) (`clm_2175083c3dcb190b435d97a079ae4d1c8d53512ea22eeb5b7e106169d2c8cc18`)
- [observation/documented] On first run codehamr seeds .codehamr/config.yaml with a local profile (Ollama, vLLM, LM-Studio) and a hamrpass profile; the system prompt is embedded in the binary, not stored on disk. -- evidence: [README.md#L49-L52](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L49-L52) (`clm_859bdae9fd107b26ea877b737486d593b395bcf705a276877fdb214df15d0010`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The agent runs a single plain loop: it calls tools until the work is done, then replies, rather than using a more elaborate orchestration scheme. -- evidence: [README.md#L18-L23](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L18-L23) (`clm_975914a3a92def0d0398365969d5760cb849511bb6ab981071432ed73fa3c5ba`)

## tools-permissions (1 claim(s))

- [observation/documented] The README warns that the agent runs model-generated shell commands with full filesystem access and recommends running it inside sandboxes such as devcontainers or isolated VMs. -- evidence: [README.md#L43-L43](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L43-L43) (`clm_684300096fdef39891470e9b9b7cbcd1718f7cd06b8b0b6f8716605eda7c3eb8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Configuration supports OpenAI-compatible endpoints; the example config defines local, openai, and hamrpass profiles with llm and url fields, and the local and openai profiles also carry key and context_size fields. -- evidence: [README.md#L54-L55](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L54-L55), [README.md#L63-L79](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L63-L79) (`clm_cbf01476c59872491735309e1c80dc42314bd89480d130ddac832fea7d976d21`)
- [observation/documented] The project is MIT licensed and open source; HamrPass, a hosted endpoint with tuned model defaults, is optional and will only be built if waitlist demand appears. -- evidence: [README.md#L108-L111](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L108-L111), [README.md#L119-L119](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L119-L119), [README.md#L113-L117](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L113-L117), [README.md#L123-L123](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L123-L123) (`clm_e76eaafdbf6155822d2ddf78e24f24e3c3e3fad2ccae972dc11d971717dc6055`)

## limitations (2 claim(s))

- [observation/documented] On Windows the bash tool requires a POSIX shell (/bin/sh), so the agent should be run inside WSL2 or a devcontainer rather than from a bare cmd/PowerShell host. -- evidence: [README.md#L39-L39](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L39-L39) (`clm_6d65741c07a4ebb1b146c5b58bde38272e132c77810c32373f05e176f6784b9f`)
- [observation/documented] Because Ollama's /v1 endpoint reports no context-window header, codehamr packs to the configured context_size; if the server honors less, it silently front-truncates and the agent can lose its system prompt and earlier tool results mid-task with no error. -- evidence: [README.md#L87-L87](https://github.com/codehamr/codehamr/blob/8ad8eae6cc57c2cd9941886334fcb960a370417d/README.md#L87-L87) (`clm_1ac704a82a26b8e0a4489f382f603a83766291ab2e253241b2d269c3a8642a83`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

