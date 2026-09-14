# morganlinton/albatross

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6f20178d81c6 @ efa5ca6ad18bbc10

## Summary (orientation draft, not independently verified)

Albatross is a terminal-first coding agent (v2.4.0, Rust) supporting local and cloud model providers, approval-gated tools, MCP/extensions/skills/packages, routed planning, an iterate/auto evaluation loop, and a local quality-PR scorecard. Evidence is README documentation only; no runtime code slices are present. Evidence coverage: 128 of 368 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The agent talks to one provider at a time, but providers can be switched mid-session with /provider while tools, commands, and the session log stay unchanged; Ollama is the default provider. -- evidence: [README.md#L213-L213](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L213-L213), [README.md#L135-L135](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L135-L135), [README.md#L222-L223](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L222-L223)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README shows a GitHub Actions CI badge for the repository's ci.yml workflow, indicating automated CI runs on the project. -- evidence: [README.md#L19-L27](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L19-L27)
- skills-patterns (1 claim(s)):
  - [observation/documented] Albatross supports the open Agent Skills directory/frontmatter standard, discovering skills from project and user roots plus installed packages; only names and descriptions enter the initial prompt, with full instructions loaded on demand. -- evidence: [README.md#L832-L837](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L832-L837)
- interfaces (2 claim(s)):
  - [observation/documented] Albatross is a terminal TUI coding agent launched via the `albatross` binary, with slash commands including /provider, /model, /plan, /ship, /undo, /auto, and `--continue` to resume the most recent session in the cwd. -- evidence: [README.md#L41-L45](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L41-L45), [README.md#L419-L453](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L419-L453), [README.md#L259-L278](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L259-L278), [README.md#L125-L127](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L125-L127)
  - [observation/documented] The tool surface includes read tools (file_read, grep, list_dir, glob, repo_search), approval-gated mutation tools (file_write, file_edit, apply_patch, batch_edit, shell), workflow tools such as run_tests and web_fetch, and MCP tools surfaced as mcp__<server>__<tool>. -- evidence: [README.md#L346-L351](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L346-L351)
- memory-state (1 claim(s)):
  - [observation/documented] Session memory features include /index and /map for project memory, /remember and /forget for durable notes, /compact for in-place summarization, and /reset which writes a handoff artifact to .albatross/continue.md and starts a fresh session seeded only with it. -- evidence: [README.md#L690-L697](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L690-L697), [README.md#L455-L470](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L455-L470)
- orchestration (1 claim(s)):
  - [observation/documented] /plan route builds a low/medium/high task graph in .albatross/plan.json using a configurable planner model, and /plan execute runs ready tasks sequentially, switching backend/model per task, with --yolo for unattended auto-approval. -- evidence: [README.md#L636-L641](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L636-L641), [README.md#L649-L651](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L649-L651)
- tools-permissions (2 claim(s)):
More evidence: [full detail](albatross.detail.md)

Metadata and full claim list: [full detail](albatross.detail.md)
Human notes ([notes](albatross.notes.md), never overwritten by build)

[Back to map index](../../index.md)
