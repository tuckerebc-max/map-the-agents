# aaif-goose/goose -- full detail

[Back to orientation](goose.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aaif-goose/goose/50666ae0b9a51e260b52b7efbab2e4e020346e94/869b8f6fee4b256e.json](../../../wiki/dossiers/aaif-goose/goose/50666ae0b9a51e260b52b7efbab2e4e020346e94/869b8f6fee4b256e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The architecture diagram shows user interfaces (CLI, Electron desktop, custom UIs) above a 'goose serve' ACP HTTP/WebSocket server, above a core goose crate containing providers, MCP extensions, and config/recipes. -- evidence: [CUSTOM_DISTROS.md#L18-L41](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L18-L41) (`clm_d92175391619bafe7f38c4633892ad507f2b7ff19e9319c54169ad9419cad65b`)
- [observation/documented] The Docker image is a multi-stage Debian Bookworm Slim build of about 340MB containing a 32MB goose binary at /usr/local/bin/goose, optimized with LTO, stripping, and size optimization. -- evidence: [BUILDING_DOCKER.md#L47-L50](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L47-L50), [BUILDING_DOCKER.md#L212-L215](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L212-L215) (`clm_151f0ba04ec45bbfd9aaa4d4fcf3aee489ea7326f329d757729311ef827a3d6a`)

## design-choices (4 claim(s))

- [observation/documented] The project is built in Rust, which the README cites for performance and portability. -- evidence: [README.md#L25-L25](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L25-L25) (`clm_1272a5154c94de24c28edaa07fccd41d1dcdb0ec32db30a12ac5bb10f2c32726`)
- [observation/documented] The Docker image runs as a non-root 'goose' user (UID 1000) by default and includes git, curl, ca-certificates, and basic shell utilities. -- evidence: [BUILDING_DOCKER.md#L155-L155](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L155-L155), [BUILDING_DOCKER.md#L225-L229](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L225-L229), [BUILDING_DOCKER.md#L219-L221](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L219-L221) (`clm_15490f3078da6e183c015211675e10a52eaafd70862b8b3efc917a6c4e2d3298`)
- [observation/documented] Configuration precedence is documented as environment variables, then config.yaml, then defaults. -- evidence: [CUSTOM_DISTROS.md#L134-L136](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L134-L136) (`clm_44a2fcf77239b74a2f11e3ded86372429bb38a3d8196604332da2f10bdba3608`)
- [observation/documented] Telemetry via PostHog is optional and can be disabled by setting GOOSE_DISABLE_TELEMETRY=1, or redirected to a custom PostHog instance by modifying posthog.rs. -- evidence: [CUSTOM_DISTROS.md#L92-L94](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L92-L94) (`clm_55667549ff19c7a0476eb1387484a9f91aa9273427d87e6ac1bf61fef7ade92b`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: building the Linux desktop app requires Rust, Node.js 22.9.0+, pnpm 10+, and 'just'; the CLI is built with 'cargo build --release -p goose-cli --bin goose' and packaged via Electron Forge (ZIP recommended, plus DEB and Flatpak). -- evidence: [BUILDING_LINUX.md#L53-L56](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L53-L56), [BUILDING_LINUX.md#L171-L172](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L171-L172), [BUILDING_LINUX.md#L94-L97](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L94-L97), [BUILDING_LINUX.md#L70-L72](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L70-L72), [BUILDING_LINUX.md#L102-L105](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L102-L105) (`clm_5f82b335d9ae867b65a424b52e048569e3e278dfd7a60edd0785cfd823ad4ed2`)
- [observation/documented] Repository development practice: BUILDING_LINUX.md asks contributors to Linux build changes to test on multiple distributions, update documentation, and consider CI/CD implications. -- evidence: [BUILDING_LINUX.md#L213-L213](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L213-L213), [BUILDING_LINUX.md#L215-L218](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L215-L218) (`clm_dbddcc38b05e8a4bfafc9d6d60a0c60d47b6799e4246a7cc512151f50251663f`)
- [observation/documented] Repository development practice: BUILDING_DOCKER.md asks contributors to Docker changes to test builds on amd64 and arm64, keep image size reasonable, update docs, and test with various LLM providers. -- evidence: [BUILDING_DOCKER.md#L312-L316](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L312-L316), [BUILDING_DOCKER.md#L310-L310](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L310-L310) (`clm_2c3e989bc28ce205ed545b9052e385e3a34da21cc423d6fa21e05995bbb9ffe8`)

## skills-patterns (1 claim(s))

- [observation/documented] Recipes are YAML-based task definitions that can bundle extensions and, with sub-recipes and subagents, express multi-step workflows; an example recipe declares extensions with stdio type, command, and args. -- evidence: [CUSTOM_DISTROS.md#L45-L54](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L45-L54), [CUSTOM_DISTROS.md#L218-L228](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L218-L228) (`clm_90a58d313ca8dbf01d77aefe432f3a49763619610c7fa359392d60ef7295e5a3`)

## interfaces (3 claim(s))

- [observation/documented] goose ships as a native desktop app for macOS, Linux, and Windows, a full CLI, and an API for embedding it elsewhere. -- evidence: [README.md#L5-L5](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L5-L5), [README.md#L25-L25](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L25-L25) (`clm_8a4145ef059b19ee79bc1c92cba481d8b6bb6239009d12ab07e59ae746e2d13d`)
- [observation/documented] Docker usage is configured via environment variables such as GOOSE_PROVIDER, GOOSE_MODEL, and provider API keys, with CLI commands like 'goose run -t'. -- evidence: [BUILDING_DOCKER.md#L19-L24](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L19-L24), [BUILDING_DOCKER.md#L74-L79](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L74-L79), [BUILDING_DOCKER.md#L140-L142](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_DOCKER.md#L140-L142) (`clm_a89211a7d43fa48df74a4fe55671a463eca887a2b9bbe563c8949f09fbf518e3`)
- [observation/documented] Custom clients can integrate over ACP using 'goose serve', an HTTP/WebSocket server started with a GOOSE_SERVER__SECRET_KEY environment variable. -- evidence: [CUSTOM_DISTROS.md#L311-L311](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L311-L311), [CUSTOM_DISTROS.md#L315-L315](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L315-L315), [CUSTOM_DISTROS.md#L18-L41](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L18-L41) (`clm_4eaff013ceb7098aa8ce1901e121ba4af682b7fbedc9ef142f3ed788185ea054`)

## memory-state (1 claim(s))

- [observation/documented] Secrets are stored via a SecretStorage mechanism that uses the system keyring by default with a file-based fallback available, and configuration lives at ~/.config/goose/config.yaml. -- evidence: [CUSTOM_DISTROS.md#L166-L168](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/CUSTOM_DISTROS.md#L166-L168) (`clm_5b839e6628490757b93b6a2352615f2e97932532f3ce9dd0286566deeb78ebd1`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The README states goose works with 15+ LLM providers (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more) and connects to 70+ extensions via the Model Context Protocol. -- evidence: [README.md#L27-L27](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L27-L27) (`clm_65c502908ece83f62016ad90af3aaf8f19a08de6ed3a62e7d7802efebe77b8ab`)
- [observation/documented] BUILDING_LINUX.md gives separate package commands for Debian/Ubuntu, Fedora, openSUSE, and Arch/Manjaro. The Debian command includes protobuf-compiler and libxcb1-dev; Fedora includes libxcb-devel. Its Arch command uses shaderc, while Debian, Fedora, and openSUSE list glslc. -- evidence: [BUILDING_LINUX.md#L20-L23](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L20-L23), [BUILDING_LINUX.md#L9-L13](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L9-L13), [BUILDING_LINUX.md#L25-L28](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L25-L28), [BUILDING_LINUX.md#L15-L18](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L15-L18) (`clm_eae365bc1e2cc59600e948b8b4b2b2e3c80ecde0f81b14017aa760033b516687`)

## limitations (1 claim(s))

- [observation/documented] The musl/portable Linux build disables local-inference (V8) and system-keyring (D-Bus SecretService) because neither is available on Android, and Snap packaging is not currently supported. -- evidence: [BUILDING_LINUX.md#L46-L47](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L46-L47), [BUILDING_LINUX.md#L177-L177](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/BUILDING_LINUX.md#L177-L177) (`clm_a1c47154b93baa5cc2a617ab589cd5938ceafbb4fd59216e03d5dcc312c749e4`)

## relevance (1 claim(s))

- [observation/documented] goose is a general-purpose AI agent that runs locally, intended not just for code but also research, writing, automation, and data analysis; it is part of the Agentic AI Foundation at the Linux Foundation and Apache-2.0 licensed. -- evidence: [README.md#L23-L23](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L23-L23), [README.md#L7-L16](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L7-L16), [README.md#L29-L29](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/README.md#L29-L29) (`clm_d42dd68b7e82dc402a9e019bf601d1d1dedd3afe2874cd8889545d6903ea5d2a`)

Superseded claim IDs (kept as history): clm_6aca70ea501e8838794eca00c3323edfba8a0c58e4ec1e89fd5137932db5eaa9, clm_8cae85cc8fc38cb9f8343095f8344e7624137f84ebe9177b48f35eed61162cb8, clm_bc74ff3d8dfffbca044e8f01b6b2c3b9122f513aa9de23291ef74d2289830c7b

