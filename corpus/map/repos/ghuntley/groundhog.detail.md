# ghuntley/groundhog -- full detail

[Back to orientation](groundhog.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ghuntley/groundhog/3844519a70ed03738d460567f7c67553402f21d7/4ec6c9cbe0f7bf93.json](../../../wiki/dossiers/ghuntley/groundhog/3844519a70ed03738d460567f7c67553402f21d7/4ec6c9cbe0f7bf93.json)

## specifications (2 claim(s))

- [observation/documented] Specifications are organized in a specs/ directory covering architecture, CLI interface, logging and telemetry, and individual commands. -- evidence: [SPECS.md#L7-L12](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L7-L12), [README.md#L64-L67](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L64-L67), [README.md#L62-L62](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L62-L62) (`clm_4ca7204c8ce262381edb4bb1c0d9c78b90d5d71ced2e34e1deee8e4801a69b89`)
- [observation/documented] The specs overview describes Groundhog as an AI-powered coding assistant built in Rust with modern logging, metrics, and telemetry practices. -- evidence: [SPECS.md#L16-L16](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L16-L16) (`clm_821c09db4a2f87dcfbcbea1e65cdcc03a44996a09a28766f7489c7f7cc93349a`)

## components (2 claim(s))

- [observation/documented] The README lists features including code explanation, an implementation in Rust, built-in logging and telemetry, and a command-line interface. -- evidence: [README.md#L13-L16](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L13-L16) (`clm_22bb32d5e4add30366d429a108cefd1a23f0956e9ef7541bb190e67a61e1ec18`)
- [observation/documented] The first implemented command, `explain`, currently prints "hello world" as a basic implementation. -- evidence: [SPECS.md#L20-L20](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L20-L20), [SPECS.md#L26-L26](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L26-L26), [SPECS.md#L22-L24](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L22-L24) (`clm_7dc71efc00616048fb860191e6b7f7444a4be1ddbc13d350f653a4e7ad168af9`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source involves cloning the repository and running `cargo build`, and tests are run with `cargo test`; a Rust toolchain is listed as a prerequisite. -- evidence: [README.md#L48-L52](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L48-L52), [README.md#L56-L58](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L56-L58), [README.md#L43-L44](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L43-L44) (`clm_491260cab9932bceaad81625ad2103ff0c1d111cb1c4522f2a08554fd638b030`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a CLI with the command structure `Groundhog <command> [options]`. -- evidence: [README.md#L26-L28](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L26-L28), [README.md#L24-L24](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L24-L24) (`clm_a3e852e2b6e0795803a3ad42a512b352937cacbcaba2720eb600dbeffbe74e7f`)
- [observation/documented] The `explain` command provides explanations for code snippets or files and is invoked as `Groundhog explain`. -- evidence: [README.md#L32-L35](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L32-L35) (`clm_35d3a07131ee7589139a22872daed931d6d5c0b6e51d51b7bccb169aadad7285`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (3 claim(s))

- [observation/documented] The project describes itself as a teaching tool first and points users wanting a full-featured product to alternatives such as Goose, Roo/Cline, Aider, or AllHands. -- evidence: [README.md#L7-L7](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L7-L7) (`clm_afe600e671cc452b3fa310c144d19714b96e4ce5267e183251976cadbfd7b441`)
- [observation/documented] The README notes more commands will be added in future releases, and installation instructions, contribution guidelines, and license information are placeholders yet to be added. -- evidence: [README.md#L75-L75](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L75-L75), [README.md#L37-L37](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L37-L37), [README.md#L20-L20](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L20-L20), [README.md#L71-L71](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L71-L71) (`clm_bb5ee36d8fd3dbd4460b0e1ede2e81db88a308215b0e95874598d90e030c04fa`)
- [observation/documented] The maintainer asks that GitHub issues not be raised about things not working, since the community/support model has not yet been decided. -- evidence: [README.md#L5-L5](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L5-L5) (`clm_79499fe270d95e324bfa788eb8039624ff04c7247ac0f6da8df2316e4a5eed5f`)

## relevance (1 claim(s))

- [observation/documented] Groundhog's stated primary purpose is educational: teaching people how coding agents like Cursor work under the hood, built incrementally as part of a public series. -- evidence: [README.md#L3-L3](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L3-L3) (`clm_af918c81a89c9b434f5be93dfe3bc716b30b11592fccf363088cf0b4d8348e14`)

