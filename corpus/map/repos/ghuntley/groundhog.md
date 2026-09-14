# ghuntley/groundhog

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3844519a70ed @ 4ec6c9cbe0f7bf93

## Summary (orientation draft, not independently verified)

Groundhog is an early-stage, Rust-based AI coding assistant CLI intended primarily as a teaching tool for understanding how coding agents work; its only implemented command is `explain`, which currently prints "hello world".

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Specifications are organized in a specs/ directory covering architecture, CLI interface, logging and telemetry, and individual commands. -- evidence: [SPECS.md#L7-L12](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L7-L12), [README.md#L64-L67](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L64-L67), [README.md#L62-L62](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L62-L62)
  - [observation/documented] The specs overview describes Groundhog as an AI-powered coding assistant built in Rust with modern logging, metrics, and telemetry practices. -- evidence: [SPECS.md#L16-L16](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L16-L16)
- components (2 claim(s)):
  - [observation/documented] The README lists features including code explanation, an implementation in Rust, built-in logging and telemetry, and a command-line interface. -- evidence: [README.md#L13-L16](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L13-L16)
  - [observation/documented] The first implemented command, `explain`, currently prints "hello world" as a basic implementation. -- evidence: [SPECS.md#L20-L20](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L20-L20), [SPECS.md#L26-L26](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L26-L26), [SPECS.md#L22-L24](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/SPECS.md#L22-L24)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source involves cloning the repository and running `cargo build`, and tests are run with `cargo test`; a Rust toolchain is listed as a prerequisite. -- evidence: [README.md#L48-L52](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L48-L52), [README.md#L56-L58](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L56-L58), [README.md#L43-L44](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L43-L44)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a CLI with the command structure `Groundhog <command> [options]`. -- evidence: [README.md#L26-L28](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L26-L28), [README.md#L24-L24](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L24-L24)
  - [observation/documented] The `explain` command provides explanations for code snippets or files and is invoked as `Groundhog explain`. -- evidence: [README.md#L32-L35](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L32-L35)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (3 claim(s)):
  - [observation/documented] The project describes itself as a teaching tool first and points users wanting a full-featured product to alternatives such as Goose, Roo/Cline, Aider, or AllHands. -- evidence: [README.md#L7-L7](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L7-L7)
  - [observation/documented] The README notes more commands will be added in future releases, and installation instructions, contribution guidelines, and license information are placeholders yet to be added. -- evidence: [README.md#L75-L75](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L75-L75), [README.md#L37-L37](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L37-L37), [README.md#L20-L20](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L20-L20), [README.md#L71-L71](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L71-L71)
- relevance (1 claim(s)):
  - [observation/documented] Groundhog's stated primary purpose is educational: teaching people how coding agents like Cursor work under the hood, built incrementally as part of a public series. -- evidence: [README.md#L3-L3](https://github.com/ghuntley/groundhog/blob/3844519a70ed03738d460567f7c67553402f21d7/README.md#L3-L3)

(1 additional claim(s) omitted for length; see [full detail](groundhog.detail.md) for every claim.)

Metadata and full claim list: [full detail](groundhog.detail.md)
Human notes ([notes](groundhog.notes.md), never overwritten by build)

[Back to map index](../../index.md)
