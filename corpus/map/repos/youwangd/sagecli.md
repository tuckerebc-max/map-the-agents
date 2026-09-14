# youwangd/sagecli

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c167712ddb69 @ 03c45df43acaed22

## Summary (orientation draft, not independently verified)

Sage is a single-file bash control plane (~8,500 lines, MIT) that orchestrates multiple agent CLIs via tmux-based runners, file-based inboxes under ~/.sage/, and 8 runtimes plus any ACP agent, with 53 commands and a bench harness. Evidence is documentation-based; no source code slices were provided. Evidence coverage: 155 of 174 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Sage is a vendor-neutral, Unix-native control plane for agent CLIs implemented as one bash script (~8,500 lines) under an MIT license. -- evidence: [README.md#L21-L22](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L21-L22), [README.md#L50-L52](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L50-L52), [README.md#L24-L28](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L24-L28), [README.md#L249-L249](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L249-L249), [README.md#L56-L63](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L56-L63)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Design emphasizes vendor neutrality: 8 runtimes plus any ACP agent behind one command surface, backends swappable with a flag, and a --fallback chain that auto-routes to healthy runtimes after a pre-flight health check. -- evidence: [README.md#L122-L125](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L122-L125), [README.md#L50-L52](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L50-L52), [README.md#L130-L130](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L130-L130), [README.md#L116-L116](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L116-L116)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes 53 commands across 12 domains (e.g. create, send, call, tasks, bench, mcp, skill, memory, trace, dashboard, doctor), with inline help via sage help and per-command --help. -- evidence: [README.md#L211-L211](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L211-L211), [README.md#L209-L209](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L209-L209), [CAPABILITIES.md#L4-L56](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/CAPABILITIES.md#L4-L56)
  - [observation/documented] The acp runtime speaks JSON-RPC 2.0 over stdio and maintains persistent sessions across tasks, unlike one-shot runtimes such as cline/claude-code which spawn a fresh process per task. -- evidence: [README.md#L179-L179](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L179-L179), [DEVELOPMENT.md#L167-L167](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L167-L167), [DEVELOPMENT.md#L187-L193](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L187-L193)
- memory-state (2 claim(s)):
  - [observation/documented] All state lives under ~/.sage/ as files: per-agent inbox/replies/results/workspace/state, runtime.json, instructions.md, steer.md, plus shared runtimes/, tools/, tasks/, plans/, and trace.jsonl. -- evidence: [DEVELOPMENT.md#L22-L60](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L22-L60), [README.md#L203-L203](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L203-L203)
  - [observation/documented] Sage provides per-agent persistent memory (memory set/get/ls/rm/clear with auto-injection into prompts) and a shared context store (context set/get/ls/rm/clear with auto-inject). -- evidence: [CAPABILITIES.md#L69-L180](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/CAPABILITIES.md#L69-L180)
- orchestration (2 claim(s)):
  - [observation/documented] Each agent runs a runner.sh process in a tmux window that polls its inbox directory every 300ms, sources the runtime script, and calls runtime_inject() per message. -- evidence: [README.md#L189-L201](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L189-L201), [DEVELOPMENT.md#L5-L18](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L5-L18)
  - [observation/documented] sage send is asynchronous (writes JSON to the inbox, returns a task ID immediately, auto-starts the agent), while sage call is synchronous, polling a reply directory up to a specified timeout. -- evidence: [DEVELOPMENT.md#L244-L255](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L244-L255), [DEVELOPMENT.md#L258-L268](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L258-L268)
- tools-permissions (1 claim(s)):
More evidence: [full detail](sagecli.detail.md)

Metadata and full claim list: [full detail](sagecli.detail.md)
Human notes ([notes](sagecli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
