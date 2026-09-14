# oleksandrchekhovskyi/hax

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7db349773eb7 @ bcb987170292241c

## Summary (orientation draft, not independently verified)

hax is a minimalist terminal-native coding agent written as a single C binary, supporting multiple LLM providers, XDG-based configuration and session state, presets, background tasks, and transcript/trace debugging. Evidence is documentation-only; no runtime code slices were supplied. Evidence coverage: 127 of 212 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] hax is described as a minimalist, terminal-native coding agent implemented as a single native C binary with a small dependency set and low memory use. -- evidence: [README.md#L14-L27](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L14-L27), [README.md#L5-L5](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L5-L5)
  - [observation/documented] The product runs on Linux, macOS, FreeBSD, and OpenBSD; on Windows it is used under WSL, and the BSDs are build-from-source only. -- evidence: [README.md#L42-L43](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L42-L43)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The project deliberately omits MCP marketplaces, a plugin runtime, IDE panels, and per-command permission prompts, composing instead via subprocesses and documenting each omission in docs/philosophy.md. -- evidence: [README.md#L31-L35](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L31-L35), [README.md#L14-L27](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L14-L27)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI supports an interactive REPL, one-shot `-p` prompts (including stdin input), `-c` to continue the latest session, and `--resume`/`--resume=ID` session selection. -- evidence: [README.md#L100-L107](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L100-L107)
  - [observation/documented] In the REPL, slash commands such as `/provider`, `/model`, `/effort`, `/preset`, `/config`, and `/preset-save` select providers and settings; Ctrl-T opens a transcript view in $PAGER and Ctrl-O shows the conversation as displayed. -- evidence: [docs/configuration.md#L202-L205](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L202-L205), [docs/debugging.md#L47-L48](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L47-L48), [README.md#L82-L83](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L82-L83), [docs/configuration.md#L152-L153](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L152-L153), [docs/configuration.md#L49-L50](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L49-L50), [docs/debugging.md#L50-L52](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L50-L52)
- memory-state (3 claim(s)):
  - [observation/documented] hax follows the XDG Base Directory specification: config at ~/.config/hax/config.json, remembered interactive selections and sessions under ~/.local/state/hax/, and a model-metadata cache at ~/.cache/hax/catalog.json. -- evidence: [docs/configuration.md#L8-L9](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L8-L9), [docs/configuration.md#L11-L16](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L11-L16)
  - [observation/documented] Settings resolve in order: current-process override, resumed conversation, environment, state.json, config.json, then default; the resumed tier covers provider, model, effort, and preset. -- evidence: [docs/configuration.md#L26-L28](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L26-L28), [docs/configuration.md#L30-L32](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L30-L32)
- orchestration (2 claim(s)):
  - [observation/documented] Presets can act as roles with description, system-prompt additions, and a tint; only presets with a description are advertised to the model as subagent delegation targets. -- evidence: [docs/configuration.md#L184-L192](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L184-L192), [docs/configuration.md#L146-L150](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L146-L150)
  - [observation/documented] The agent manages background tasks with configurable wait timeout and a concurrency cap (default 32, up to 64), and bash commands detach after a default 2-minute timeout with a SIGTERM-to-SIGKILL grace period. -- evidence: [docs/configuration.md#L304-L317](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L304-L317)
- tools-permissions (1 claim(s)):
More evidence: [full detail](hax.detail.md)

Metadata and full claim list: [full detail](hax.detail.md)
Human notes ([notes](hax.notes.md), never overwritten by build)

[Back to map index](../../index.md)
