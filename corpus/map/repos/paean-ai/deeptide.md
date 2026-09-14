# paean-ai/deeptide

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b48688d56c3e @ b47b4daf011a3fc2

## Summary (orientation draft, not independently verified)

DeepTide is an agentic coding assistant shipped as a macOS native app, a Bun-based cross-platform CLI (a thin wrapper around @paean-ai/zero-cli), and a Rust CLI with an optional desktop GUI; the repo also hosts a local DeepSeek V4 Flash inference runtime (ds4/dsgo) and quantization docs describing local-mode constraints. Evidence coverage: 130 of 315 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] DeepTide is an agentic coding assistant in which the model plans, calls tools, observes results, and adapts; it ships as a macOS native app, a cross-platform Bun CLI, and a Rust CLI with an optional desktop GUI. -- evidence: [README.md#L23-L31](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L23-L31), [README.md#L204-L205](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L204-L205)
- components (2 claim(s)):
  - [observation/documented] The repo hosts two npm packages: `deeptide`, a thin redirect to @paean-ai/zero-cli, and `deeptide-rs`, which ships a native Rust binary via GitHub Releases postinstall; the Rust port lives under crates/. -- evidence: [README.md#L45-L48](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L45-L48), [README.md#L320-L326](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L320-L326), [README.md#L36-L39](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L36-L39)
  - [observation/documented] The repository also contains a native local inference runtime under native/: a hard-forked ds4 DeepSeek V4 Flash Metal engine and dsgo, an OpenAI/Anthropic-compatible local gateway, built via npm run build:native on macOS. -- evidence: [README.md#L279-L279](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L279-L279), [README.md#L50-L53](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L50-L53), [README.md#L287-L290](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L287-L290)
- design-choices (1 claim(s)):
  - [observation/documented] The local V4 Flash Q2 profile caps context at 64k, disables subagents, and forces serial tool execution, because Q2's attention quality degrades on long contexts and parallel tool calls compound state too quickly. -- evidence: [docs/deepseek-v4-flash-q2.md#L36-L36](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L36-L36), [docs/deepseek-v4-flash-q2.md#L38-L38](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L38-L38)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors build the Rust GUI from the crates/ workspace with cargo run/build -p deeptide-gui, build native components with npm run build:ds4 / build:dsgo, and report security vulnerabilities via private vulnerability reporting, redacting sensitive data from logs. -- evidence: [README.md#L310-L314](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L310-L314), [README.md#L190-L192](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L190-L192), [README.md#L287-L290](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L287-L290), [README.md#L302-L308](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L302-L308)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI installs `deeptide` and `tide` commands supporting an interactive REPL, one-shot mode via `-p`, `--base-url`/`--api-key` for BYOK providers, `tide auth login`, and `tide doctor` diagnostics. -- evidence: [README.md#L141-L141](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L141-L141), [README.md#L69-L74](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L69-L74), [README.md#L105-L110](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L105-L110)
  - [observation/documented] The Rust GUI shares the CLI's configuration (~/.config/tide/settings.json and project .deeptide/settings.json), on-disk session store resumable via `--resume`, and full tool set; it is launched with `deeptide-rs --gui` or the `deeptide-gui` binary. -- evidence: [README.md#L180-L180](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L180-L180), [README.md#L156-L159](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L156-L159), [README.md#L161-L168](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L161-L168), [README.md#L183-L184](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L183-L184)
- memory-state (1 claim(s)):
More evidence: [full detail](deeptide.detail.md)

Metadata and full claim list: [full detail](deeptide.detail.md)
Human notes ([notes](deeptide.notes.md), never overwritten by build)

[Back to map index](../../index.md)
