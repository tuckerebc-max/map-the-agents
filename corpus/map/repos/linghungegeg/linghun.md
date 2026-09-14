# linghungegeg/linghun

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 05d8457bd04a @ 64bad13006da78ed

## Summary (orientation draft, not independently verified)

Evidence from the README and an internal execution-plan document describes Linghun as a local-first, evidence-first AI coding CLI with provider runtime, permission boundaries, verification-aware delivery, workflow orchestration, and Windows/Chinese-first focus; the execution plan documents repository development practice. No cited slice shows a LINGHUN.md file present in the snapshot, so that item is dropped. Evidence coverage: 188 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Linghun is described as a local-first, evidence-first AI coding terminal that connects large models to real projects, tools, permissions, verification, and context. -- evidence: [README.md#L5-L5](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L5-L5), [README.md#L7-L7](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L7-L7), [README.md#L27-L27](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L27-L27)
- components (2 claim(s)):
  - [observation/documented] Built-in tool paths include Read, Write, Edit, MultiEdit, Grep, Glob, Bash, Todo, Diff, and Git, with file writes and commands passing through permission, path, security, and result-summary boundaries. -- evidence: [README.md#L338-L338](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L338-L338)
  - [observation/documented] The CLI package bundles a codebase-memory-mcp binary for Windows x64, Linux x64, and macOS on both Apple Silicon and Intel. -- evidence: [README.md#L364-L367](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L364-L367), [README.md#L362-L362](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L362-L362)
- design-choices (2 claim(s)):
  - [observation/documented] The design philosophy places key constraints at the system layer rather than in prompts: tool execution, permissions, evidence, verification, Git, indexing, caching, and failure learning form one main chain. -- evidence: [README.md#L133-L133](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L133-L133), [README.md#L135-L135](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L135-L135)
  - [observation/documented] Verification-aware delivery distinguishes PASS, PARTIAL, FAIL, TIMEOUT, STALE, and CANCELLED outcomes, and separates focused verification, mock verification, real smoke tests, and unverified conclusions. -- evidence: [README.md#L352-L352](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L352-L352)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: an internal execution-plan document mandates strict phase ordering (phases 0-7), per-phase minimal verification, independent re-checks, recorded completed/blocked items, and forbids skipping phases or substituting hidden text fixes for underlying event fixes. -- evidence: [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L15-L19](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L15-L19), [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L9-L11](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L9-L11), [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L21-L21](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L21-L21)
  - [observation/documented] Repository development practice: the execution plan requires establishing a fact baseline of Linghun and CCB call chains without modifying business code, with deliverables including call-chain comparison tables, output-source inventories, and minimal reproducible examples. -- evidence: [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L155-L159](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L155-L159), [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L137-L137](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L137-L137)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product is distributed as the npm package @linghun/cli, installed globally and launched with the `linghun` command; a capitalized `Linghun` entry is also supported on Windows. -- evidence: [README.md#L189-L191](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L189-L191), [README.md#L195-L197](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L195-L197), [README.md#L193-L193](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L193-L193), [README.md#L183-L185](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L183-L185), [README.md#L20-L23](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L20-L23)
  - [observation/documented] Model configuration is done via a `/model setup` wizard asking for API base URL, API key, model name, and reasoning level; `/model doctor` checks provider configuration. -- evidence: [README.md#L215-L218](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L215-L218), [README.md#L209-L211](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L209-L211), [README.md#L224-L226](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L224-L226)
More evidence: [full detail](linghun.detail.md)

Metadata and full claim list: [full detail](linghun.detail.md)
Human notes ([notes](linghun.notes.md), never overwritten by build)

[Back to map index](../../index.md)
