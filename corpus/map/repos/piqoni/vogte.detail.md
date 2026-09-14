# piqoni/vogte -- full detail

[Back to orientation](vogte.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/piqoni/vogte/37e9ab501aa7f803799b298ec1da00a0f257819f/40c3abfc06915167.json](../../../wiki/dossiers/piqoni/vogte/37e9ab501aa7f803799b298ec1da00a0f257819f/40c3abfc06915167.json)

## specifications (1 claim(s))

- [observation/documented] Vogte is described as an agentic terminal tool aimed at existing Go codebases, helping developers build and maintain Go projects with LLMs. -- evidence: [README.md#L1-L9](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L1-L9), [README.md#L15-L19](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L15-L19) (`clm_7e5d6ac3be06728a0e2d444a78812ac28fa9f123381d51eb26d69a8eec4358bd`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Because the language is assumed to be Go, the tool parses repositories with Abstract Syntax Trees to extract compressed, relevant context for LLM prompts, aiming for near-zero configuration. -- evidence: [README.md#L15-L19](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L15-L19) (`clm_ab954c665c09aeacbdda48e27808afc9fdaa6d9a022fbc1237eb1c0ce56af530`)

## workflows (1 claim(s))

- [observation/documented] Installation is via 'go install github.com/piqoni/vogte@latest'; the TUI exits via Ctrl+C or typing q, quite, or exit. -- evidence: [README.md#L49-L49](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L49-L49), [README.md#L41-L43](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L41-L43) (`clm_8f989390f23016d3adbf3de8a2799ba83d9138a9c74cdf28d00c413c83a841b0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The tool offers a TUI with ask/agent modes and CLI flags including -review, -generate-context, -agent, -config, -dir, and -model. -- evidence: [README.md#L51-L61](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L51-L61), [README.md#L29-L31](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L29-L31), [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27), [README.md#L63-L69](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L63-L69) (`clm_0fefc8983a25da6b8a888303adff7fa5910a0ab91bf6fd36670a728a0a79050b`)
- [observation/documented] Running 'vogte -generate-context' writes a vogte-context.txt file in the current directory, and -dir lets users analyze a project in another directory. -- evidence: [README.md#L78-L79](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L78-L79), [README.md#L81-L81](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L81-L81), [README.md#L63-L69](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L63-L69), [README.md#L74-L76](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L74-L76) (`clm_27ec768133466b800cbb7e200de2985e57d61ccea8d9be4c505d5c466a0bb13b`)
- [inference/documented] The -review flag appears to perform a local LLM review of uncommitted changes against a base branch (default main), optionally accepting a change description message. -- evidence: [README.md#L29-L31](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L29-L31), [README.md#L63-L69](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L63-L69) (`clm_4b17e5d9ba469efa89c3e27ce21ed9e50d8c3a4d6305961ad18a846e27f87c93`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] It uses a two-step flow: first it extracts structs/interfaces/methods signatures and asks the LLM which files are needed, then supplies those files in full so the LLM can produce a solution. -- evidence: [README.md#L38-L38](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L38-L38) (`clm_f3718b27617026f67795f182acf1b56d516be18b29935004a2fbcdd672b7eec9`)

## tools-permissions (1 claim(s))

- [observation/documented] In agent mode (via -agent or the AGENT toggle) the tool edits files without user approval, and users are advised to rely on version control to avoid losing work. -- evidence: [README.md#L71-L71](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L71-L71) (`clm_b15b3a0acc12cfb42cd406210c022500552442ab28ae63bb377666e6e94740a1`)

## evaluation (1 claim(s))

- [observation/documented] After applying patches, the tool runs a 'Sanity Check' (currently 'go vet ./...') and shows a project-health indicator for instant feedback. -- evidence: [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27) (`clm_b92079fc233fee9e64deafadc83644f693358bd05878d83d92bda697ca0c43ee`)

## dependencies (1 claim(s))

- [observation/documented] It works with OpenAI-compatible APIs (tested with GPT-4 and Claude Sonnet), supports AWS Bedrock for Anthropic models, and uses OPENAI_API_KEY or ANTHROPIC_API_KEY environment variables. -- evidence: [README.md#L46-L47](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L46-L47), [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27) (`clm_df6d86b6ac9992c779e04358c3d92ade1a62c15f15f0c80684f9a29a0250e8ef`)

## limitations (2 claim(s))

- [observation/documented] Each message is treated as a new, unrelated chat, and there is no agentic retry loop on failure, at least for now. -- evidence: [README.md#L34-L35](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L34-L35) (`clm_c8105f4f84e272cd463128a7920be5169e0abf5915b10566cfdb252b4ddde941`)
- [observation/documented] Patch application is currently line-based; an AST-based patching approach is still being explored, and agent-mode patching is described as rough around the edges. -- evidence: [README.md#L22-L27](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L22-L27), [README.md#L15-L19](https://github.com/piqoni/vogte/blob/37e9ab501aa7f803799b298ec1da00a0f257819f/README.md#L15-L19) (`clm_1ab4ecd604cbb29ae58e316da0b3611ce9d184f0fffd0e7667ea46eb1b04b79e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

