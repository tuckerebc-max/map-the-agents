# zhixiangluo/10xproductivity

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9a7da40bc798 @ cfc92ae293e2d435

## Summary (orientation draft, not independently verified)

The README describes 10xProductivity as a local-first stack that turns existing coding agents (Cursor, Claude Code, Codex) into personal work assistants via tool connections, triggers, a thin local runtime, workflows, and packaged agent skills. Evidence is mostly documentation; the repo layout, CLI entry points, private-state directory, and contributor rules are documented but not code-inspected. Evidence coverage: 141 of 376 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is organized into tool_connections/, triggers/, runtime/, workflows/, tests/, .cursor/skills/, .claude/skills/, and staging/, plus setup guides such as setup.md, add-new-tool.md, and setup-python.md. -- evidence: [README.md#L147-L159](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L147-L159)
- design-choices (2 claim(s)):
  - [observation/documented] The project is positioned as a local-first personal AI assistant stack that reuses the user's existing coding agent, browser sessions, desktop apps, and permissions, explicitly avoiding new company-wide platforms, Slack apps, webhooks, or IT approval. -- evidence: [README.md#L5-L5](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L5-L5), [README.md#L29-L34](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L29-L34), [README.md#L3-L3](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L3-L3)
  - [observation/documented] The connection philosophy prioritizes zero-friction auth: supported API tokens first, then Agent Browser over existing sessions; OAuth requiring the user to create their own app or register credentials is explicitly rejected. -- evidence: [add-new-tool.md#L113-L113](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L113-L113), [add-new-tool.md#L82-L82](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L82-L82), [add-new-tool.md#L87-L94](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L87-L94)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions follow a 'run before you write' rule — every snippet must be executed and seen to succeed — and new tool work starts in TENX_PRIVATE_DIR/personal/, never directly in tool_connections/, with promotion to the public repo only via staging/ and a PR after verification and scrubbing. -- evidence: [README.md#L341-L341](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L341-L341), [add-new-tool.md#L44-L51](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/add-new-tool.md#L44-L51)
- skills-patterns (1 claim(s)):
  - [observation/documented] Packaged Cursor and Claude Code skills cover tool setup, enterprise search, workflow creation, UI surface discovery, colleague distillation, and an assistant inbox/orchestrator skill. -- evidence: [README.md#L197-L197](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L197-L197)
- interfaces (2 claim(s)):
  - [observation/documented] The runtime exposes a CLI entry point 10x-host that takes --trigger, --workflow, and --engine arguments, e.g. running a slack-polling trigger with the assistant workflow and the cursor engine. -- evidence: [README.md#L281-L283](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L281-L283), [README.md#L238-L240](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L238-L240)
  - [observation/documented] A second CLI, 10x-standup-prep, supports a --meeting-context flag and a --dry-run mode; posting to Slack requires reviewing output first and setting TENX_STANDUP_PREP_SLACK_CHANNEL before using --post. -- evidence: [README.md#L289-L291](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L289-L291), [README.md#L293-L293](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L293-L293)
- memory-state (1 claim(s)):
  - [observation/documented] Private runtime state lives outside the repo by default under ~/.10xProductivity/ (.env tokens, personal/ recipes, verified_connections.md, tmp/ for trigger and scheduler state), overridable via the TENX_PRIVATE_DIR environment variable. -- evidence: [README.md#L163-L169](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L163-L169), [README.md#L171-L171](https://github.com/ZhixiangLuo/10xProductivity/blob/9a7da40bc798e4e3fe91b10770cf0fcc13cf0886/README.md#L171-L171)
- orchestration (1 claim(s)):
More evidence: [full detail](10xproductivity.detail.md)

Metadata and full claim list: [full detail](10xproductivity.detail.md)
Human notes ([notes](10xproductivity.notes.md), never overwritten by build)

[Back to map index](../../index.md)
