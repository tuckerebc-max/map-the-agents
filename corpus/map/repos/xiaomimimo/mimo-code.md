# xiaomimimo/mimo-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6fbb1732232c @ d96a162cc3e28c0a

## Summary (orientation draft, not independently verified)

MiMoCode is a terminal-native AI coding assistant (an OpenCode fork) with persistent SQLite-backed memory, multi-agent orchestration, deterministic JS workflows, builtin skills, and a GPT-specific tool ABI; evidence is documentation-based from README and an architecture doc. Evidence coverage: 154 of 375 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 72 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] For GPT/Codex models, a smaller tool ABI (bash, apply_patch, view_image, exec) is exposed; exec composes host tools inside QuickJS while permissions and side effects remain under host control. -- evidence: [docs/architecture/codex-microkernel-runtime.en.md#L7-L7](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L7-L7), [docs/architecture/codex-microkernel-runtime.en.md#L13-L15](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L13-L15)
  - [observation/documented] The GPT profile is enabled when the model ID contains 'gpt-' (excluding 'oss' and 'gpt-4') and hides overlapping read/write/edit/grep/glob tools; prompt routing and tool profiles use separate string rules not yet unified. -- evidence: [docs/architecture/codex-microkernel-runtime.en.md#L35-L35](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L35-L35), [docs/architecture/codex-microkernel-runtime.en.md#L46-L46](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L46-L46), [docs/architecture/codex-microkernel-runtime.en.md#L44-L44](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L44-L44)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: development uses bun (bun ci for frozen-lockfile install, bun run dev, bun turbo typecheck). -- evidence: [README.md#L535-L539](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L535-L539)
- skills-patterns (2 claim(s)):
  - [observation/documented] Builtin skills are matched by exact name, localized alias, or BM25 relevance; high-confidence matches auto-load, and users can override builtins with same-name skills in project or personal skill directories. -- evidence: [README.md#L270-L270](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L270-L270), [README.md#L238-L238](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L238-L238)
  - [observation/documented] Environment variables can disable builtin skills entirely, disable only office/media skills, or hide skills from TUI autocomplete while keeping them available to agents. -- evidence: [README.md#L275-L279](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L275-L279), [README.md#L281-L281](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L281-L281)
- interfaces (3 claim(s)):
  - [observation/documented] MiMoCode is a terminal-native AI coding assistant that reads/writes code, runs commands, manages Git, and maintains persistent project memory across sessions. -- evidence: [README.md#L19-L19](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L19-L19)
  - [observation/documented] Install options include a curl one-liner for macOS/Linux, a PowerShell script for Windows, and npm install -g @mimo-ai/cli; the CLI is launched with the `mimo` command. -- evidence: [README.md#L45-L45](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L45-L45), [README.md#L51-L51](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L51-L51), [README.md#L48-L48](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L48-L48), [README.md#L54-L55](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L54-L55)
- memory-state (2 claim(s)):
  - [observation/documented] Cross-session memory uses SQLite FTS5 with files for project memory (MEMORY.md), session checkpoints, scratch notes, and per-task progress; memory is injected automatically on session resume. -- evidence: [README.md#L148-L151](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L148-L151), [README.md#L146-L146](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L146-L146), [README.md#L153-L153](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L153-L153)
  - [observation/documented] Context management includes automatic checkpoints, context reconstruction near the window limit, budgeted injection with importance ranking, and a per-model adjustable compaction point via /context-limit or compaction.max_context. -- evidence: [README.md#L157-L160](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L157-L160), [README.md#L165-L167](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L165-L167)
- orchestration (3 claim(s)):
More evidence: [full detail](mimo-code.detail.md)

Metadata and full claim list: [full detail](mimo-code.detail.md)
Human notes ([notes](mimo-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
