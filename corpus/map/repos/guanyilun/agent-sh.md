# guanyilun/agent-sh

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8038ae7730eb @ a723232a0e326851

## Summary (orientation draft, not independently verified)

agent-sh is an npm-distributed composable agent runtime pairing a PTY shell frontend with swappable agent backends (default `ash`) over a shared extension bus; evidence is documentation-only, covering architecture, tools, context management, and platform limits. Evidence coverage: 140 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] agent-sh is published as an npm package (`agent-sh`) with a license badge, installable globally via `npm install -g agent-sh`. -- evidence: [README.md#L32-L34](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L32-L34), [README.md#L3-L4](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L3-L4)
  - [observation/documented] The runtime requires Node.js 18+ and supports bash, zsh, and fish as host shells; other shells such as nushell are not yet wired up. -- evidence: [README.md#L48-L48](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L48-L48)
- components (2 claim(s)):
  - [observation/documented] The architecture is a pure kernel (`createCore()`) providing EventBus, HandlerRegistry, Compositor, multi-backend coordination, and a default cwd handler, with agent, shell, TUI, and providers all loaded as extensions. -- evidence: [docs/architecture.md#L9-L43](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/architecture.md#L9-L43), [docs/architecture.md#L7-L7](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/architecture.md#L7-L7)
  - [observation/documented] The default backend `ash` resolves providers, configures an LlmClient, calls any OpenAI-compatible API directly, and executes tools in a loop until the LLM finishes; it only activates once an apiKey and model are resolved. -- evidence: [docs/agent.md#L5-L5](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L5-L5)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills follow the Agent Skills standard: directories with a SKILL.md containing YAML frontmatter (required name and description); only metadata enters the system prompt, and the agent loads full content via read_file when needed. -- evidence: [docs/agent.md#L104-L104](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L104-L104), [docs/agent.md#L122-L124](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L122-L124), [docs/agent.md#L120-L120](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L120-L120), [docs/agent.md#L82-L82](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L82-L82)
- interfaces (2 claim(s)):
  - [observation/documented] Tools implement a `ToolDefinition` interface with name, description, JSON Schema input_schema, an execute function with optional streaming onChunk callback, and flags like modifiesFiles, readOnly, and showOutput. -- evidence: [docs/agent.md#L280-L285](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L280-L285), [docs/agent.md#L287-L290](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L287-L290), [docs/agent.md#L292-L294](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L292-L294)
  - [observation/documented] Core tools include bash, read_file, write_file, edit_file, grep (via ripgrep), glob, ls, and list_skills; conversation_recall is registered by the rolling-history extension rather than being a core tool. -- evidence: [docs/agent.md#L177-L187](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L177-L187), [docs/agent.md#L189-L189](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L189-L189)
- memory-state (1 claim(s)):
  - [observation/documented] Conversation state is an OpenAI-compatible messages array; ash auto-compacts when estimated prompt tokens cross autoCompactThreshold (default 0.5) of the model's context window, and older turns are evicted to a persistent rolling-history store browsable via conversation_recall. -- evidence: [docs/agent.md#L356-L356](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L356-L356), [docs/agent.md#L37-L38](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L37-L38), [docs/agent.md#L350-L350](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L350-L350), [docs/agent.md#L341-L341](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L341-L341)
- orchestration (1 claim(s)):
More evidence: [full detail](agent-sh.detail.md)

Metadata and full claim list: [full detail](agent-sh.detail.md)
Human notes ([notes](agent-sh.notes.md), never overwritten by build)

[Back to map index](../../index.md)
