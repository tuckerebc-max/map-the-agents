# antigmalabs/ante

Status: distilled - Freshness: stale
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ae2438217d8a @ 0b6b7c4fff05d43c

## Summary (orientation draft, not independently verified)

The snapshot is README and license/terms documentation for Ante, a Rust-based terminal coding agent distributed as a prebuilt binary, with protocol/SDK crates and an eval pipeline in the repo. Claims below rest on documented statements only.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Ante is described as a self-contained terminal coding agent shipped as a single Rust executable with zero runtime dependencies, about 15MB compressed. -- evidence: [README.md#L21-L21](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L21-L21), [README.md#L112-L112](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L112-L112)
- components (2 claim(s)):
  - [observation/documented] The curated `pi` profile reduces Ante to four tools (Read, Write, Edit, Bash) plus a short replacement system prompt, with file search via `rg`, subagents via `ante -p`, and web access via `curl`. -- evidence: [README.md#L169-L169](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L169-L169)
  - [observation/documented] The repo contains `ante-harbor/`, a Harbor agent adapter behind the Terminal-Bench results, intended for reproducing published runs. -- evidence: [README.md#L221-L223](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L221-L223)
- design-choices (1 claim(s)):
  - [observation/documented] A settings profile can define the whole agent, including a replacement system prompt, tool set, skills, and memory; `--profile <name>` swaps profiles per run, and a built-in `bare` profile strips skills, MCP, session saving, and auto-memory. -- evidence: [README.md#L32-L32](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L32-L32), [README.md#L167-L167](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L167-L167), [README.md#L176-L176](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L176-L176)
- workflows (1 claim(s)):
  - [observation/documented] Repository source (including SDK and protocol crates) is Apache 2.0 licensed, while the prebuilt binary is governed by separate Binary Preview Terms permitting free commercial use during the preview. -- evidence: [BINARY-TERMS.md#L3-L6](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/BINARY-TERMS.md#L3-L6), [README.md#L319-L323](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L319-L323), [README.md#L316-L317](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L316-L317), [BINARY-TERMS.md#L8-L10](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/BINARY-TERMS.md#L8-L10)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Ante offers four run modes: interactive TUI (`ante`), headless one-shot (`ante -p`), server daemon (`ante serve`) over a JSONL protocol, and gateway mode for Slack/Discord bots. -- evidence: [README.md#L126-L131](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L126-L131), [README.md#L307-L308](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L307-L308)
  - [observation/documented] The `crates/protocol-shape` crate defines the schema and wire messages spoken by `ante serve`, and `crates/ante-sdk` is a Rust SDK/client for building against agent runtimes. -- evidence: [README.md#L221-L223](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L221-L223)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The documented architecture is client-daemon: TUI, headless, and serve clients connect to a daemon organized as Session, Turn, Step, with tools, permissions, and skills/agents, above a provider layer. -- evidence: [README.md#L231-L258](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L231-L258), [README.md#L229-L229](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L229-L229)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Ante is evaluated continuously on Terminal-Bench 2.1 under official leaderboard constraints (89 tasks, 5 trials each); the latest reported full run scored 82.7% with DeepSeek V4 Flash 0731, with raw Harbor runs linked for audit. -- evidence: [README.md#L36-L36](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L36-L36)
- dependencies (3 claim(s)):
More evidence: [full detail](ante.detail.md)

Metadata and full claim list: [full detail](ante.detail.md)
Human notes ([notes](ante.notes.md), never overwritten by build)

[Back to map index](../../index.md)
