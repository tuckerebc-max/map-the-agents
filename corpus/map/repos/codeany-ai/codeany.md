# codeany-ai/codeany

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7e614dc436ef @ c133a7afd77dd2c7

## Summary (orientation draft, not independently verified)

README and CODEANY.md describe Codeany, an open-source Go terminal AI agent built on Bubble Tea and the open-agent-sdk-go, with slash commands, skills, plugins, MCP, sessions, and permission modes. Much of CODEANY.md is contributor guidance, so build/test instructions are reported only as repository development practice.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The internal package layout includes modules for config, permissions, memory, pipe mode, plugins, sessions, skills, slash command registry, team/mailbox, theme, TUI model/input/render, version, and git worktree isolation. -- evidence: [CODEANY.md#L16-L37](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L16-L37)
- design-choices (2 claim(s)):
  - [observation/documented] Configuration lives in ~/.codeany/ with settings.json (model, permissions, MCP, hooks), an alternative config.yaml, persisted permissions.json, and directories for memory, sessions, skills, plugins, teams, and worktrees. -- evidence: [CODEANY.md#L41-L51](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L41-L51), [README.md#L112-L126](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L112-L126), [README.md#L110-L110](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L110-L110)
  - [inference/documented] The project appears positioned as a feature-parity, fully open-source alternative to Claude Code, and even instructs contributors to compare against the original TypeScript codebase when adding features. -- evidence: [CODEANY.md#L5-L5](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L5-L5), [CODEANY.md#L78-L80](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L78-L80)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors build with `make build` or `go build -o codeany ./cmd/codeany/`, run `make vet`, cross-compile six platforms with `make dist`, and test pipe mode via `go run ./cmd/codeany -p -y`. -- evidence: [CODEANY.md#L57-L60](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L57-L60), [CODEANY.md#L63-L65](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L63-L65)
  - [observation/documented] Repository development practice: slash commands must be registered in both AllCommands() for autocomplete and Handle() for routing, and go.work links the SDK locally while go.mod uses the published version for CI. -- evidence: [CODEANY.md#L69-L74](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L69-L74)
- skills-patterns (1 claim(s)):
  - [observation/documented] Custom skills are markdown files at .codeany/skills/<name>/SKILL.md with YAML frontmatter (name, description, argumentHint) whose body can reference $ARGUMENTS and be invoked as a slash command like /deploy staging. -- evidence: [README.md#L173-L178](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L173-L178), [README.md#L184-L184](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L184-L184), [README.md#L180-L182](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L180-L182), [README.md#L171-L171](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L171-L171)
- interfaces (4 claim(s)):
  - [observation/documented] The product is a terminal TUI agent written in Go using Bubble Tea, invoked as the `codeany` binary with interactive, initial-prompt, pipe (-p), and print (--print) modes. -- evidence: [README.md#L39-L39](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L39-L39), [README.md#L48-L48](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L48-L48), [README.md#L45-L45](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L45-L45), [README.md#L42-L42](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L42-L42), [README.md#L7-L7](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L7-L7)
  - [observation/documented] The CLI supports flags including -p for pipe mode, -y to skip permission prompts, -m to select a model, and --output-format json for JSON output. -- evidence: [README.md#L57-L58](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L57-L58), [README.md#L48-L48](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L48-L48), [README.md#L45-L45](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L45-L45), [README.md#L51-L51](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L51-L51), [README.md#L54-L54](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L54-L54)
- memory-state (1 claim(s)):
  - [observation/documented] The agent maintains memory files under ~/.codeany/memory/ (MEMORY.md plus files per the architecture doc), session history with save/restore/resume, and per-session context such as files accessed. -- evidence: [CODEANY.md#L16-L37](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L16-L37), [README.md#L112-L126](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L112-L126), [README.md#L62-L90](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L62-L90)
- orchestration (1 claim(s)):
More evidence: [full detail](codeany.detail.md)

Metadata and full claim list: [full detail](codeany.detail.md)
Human notes ([notes](codeany.notes.md), never overwritten by build)

[Back to map index](../../index.md)
