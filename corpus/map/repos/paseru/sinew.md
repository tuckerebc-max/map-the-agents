# paseru/sinew

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 13b0a2187a07 @ 8eac9848b44c0207

## Summary (orientation draft, not independently verified)

README-only evidence describing Sinew, a Tauri 2 desktop AI coding harness with three agent modes, a toggleable/editable toolset, multi-provider OAuth/API-key connections, sub-agents, peer-to-peer agent teams, compaction, and rollback. No development-practice or evaluation evidence is present. Evidence coverage: 161 of 251 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Sinew is a desktop AI coding harness built on Tauri 2, React, Rust, Monaco, xterm, and MCP, where every tool is toggleable, descriptions are editable, and providers are pluggable. -- evidence: [README.md#L19-L21](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L19-L21), [README.md#L13-L17](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L13-L17)
- components (1 claim(s)):
  - [observation/documented] The codebase is organized as a React UI (src/), a Tauri 2 shell (src-tauri/), provider-agnostic core types (sinew-core), the agent loop and tools (sinew-app), and per-provider adapter crates. -- evidence: [README.md#L536-L540](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L536-L540)
- design-choices (3 claim(s)):
  - [observation/documented] read, glob, and grep each require a mandatory limit parameter, forcing the model to declare how much output it wants to preserve context. -- evidence: [README.md#L256-L256](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L256-L256), [README.md#L208-L208](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L208-L208), [README.md#L233-L233](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L233-L233)
  - [observation/documented] The clean_context tool lets the model replace its own current-turn tool results with short placeholders, keeping the placeholder visible and avoiding retroactive purges so provider prompt caching is preserved. -- evidence: [README.md#L169-L169](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L169-L169), [README.md#L178-L178](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L178-L178), [README.md#L175-L176](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L175-L176)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are directories with a SKILL.md, discovered from four prioritized locations (.agents/skills and .sinew/skills in workspace and home), with the .agents format aligned to the Claude Agent Skills convention. -- evidence: [README.md#L415-L415](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L415-L415), [README.md#L396-L402](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L396-L402), [README.md#L408-L411](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L408-L411), [README.md#L413-L413](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L413-L413)
- interfaces (3 claim(s)):
  - [observation/documented] The agent has three interaction modes: Act (single-turn loop), Goal (autonomous loop until the task finishes), and Plan (a question/answer session that only ends when the user clicks send-and-stop). -- evidence: [README.md#L68-L68](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L68-L68), [README.md#L72-L72](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L72-L72), [README.md#L76-L76](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L76-L76)
  - [observation/documented] The agent's toolset includes bash/bash_input, read, glob, grep, edit_file, write_file, web_search, web_fetch, create_image, question, todo_list, clean_context, load_mcp_tool, skill, subagent tools, and team tools. -- evidence: [README.md#L134-L155](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L134-L155)
- memory-state (1 claim(s)):
  - [observation/documented] The todo list's full state is re-injected into the system reminder every turn so the model always sees an up-to-date version, which the README says matters most in long Goal-mode runs. -- evidence: [README.md#L363-L363](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L363-L363)
- orchestration (2 claim(s)):
  - [observation/documented] The main agent can launch a peer-to-peer team of 2 to 8 agents with no lead; teammates coordinate through a shared task board with dependencies and messages delivered via system reminders. -- evidence: [README.md#L440-L440](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L440-L440), [README.md#L497-L501](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L497-L501), [README.md#L493-L493](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L493-L493), [README.md#L456-L457](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L456-L457)
More evidence: [full detail](sinew.detail.md)

Metadata and full claim list: [full detail](sinew.detail.md)
Human notes ([notes](sinew.notes.md), never overwritten by build)

[Back to map index](../../index.md)
