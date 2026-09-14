# aattaran/deepclaude

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 70518b6cdcf3 @ 5d655440a2eb307f

## Summary (orientation draft, not independently verified)

README-only evidence for deepclaude, a shell-script wrapper plus local proxy that routes Claude Code API calls to DeepSeek/OpenRouter/Fireworks/Anthropic backends, with CLI flags, slash-command switching, cost tracking, and documented limitations.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product consists of platform launcher scripts (deepclaude.ps1 for Windows, deepclaude.sh for macOS/Linux) plus a Node-based local proxy component. -- evidence: [README.md#L51-L55](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L51-L55), [README.md#L318-L320](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L318-L320), [README.md#L45-L45](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L45-L45), [README.md#L322-L322](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L322-L322)
- design-choices (3 claim(s)):
  - [observation/documented] The tool sets Claude Code environment variables (e.g. ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, model-tier variables) per session and restores original settings on exit rather than persisting them. -- evidence: [README.md#L74-L81](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L74-L81), [README.md#L72-L72](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L72-L72), [README.md#L83-L83](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L83-L83)
  - [observation/documented] Backend switching works mid-session without restart via slash commands, a CLI --switch flag, or VS Code tasks that POST to the proxy's mode endpoint. -- evidence: [README.md#L150-L150](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L150-L150), [README.md#L204-L207](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L204-L207), [README.md#L177-L177](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L177-L177), [README.md#L200-L200](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L200-L200), [README.md#L211-L232](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L211-L232)
- workflows (1 claim(s)):
  - [observation/documented] Setup involves obtaining a DeepSeek API key, setting DEEPSEEK_API_KEY via setx or shell profile, and installing the script on PATH by copy or symlink. -- evidence: [README.md#L51-L55](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L51-L55), [README.md#L45-L45](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L45-L45), [README.md#L25-L25](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L25-L25), [README.md#L29-L32](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L29-L32), [README.md#L34-L38](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L34-L38)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI supports flags including --status, --backend (ds/or/fw/anthropic), --cost, --benchmark, --switch, and --remote, per the usage examples. -- evidence: [README.md#L204-L207](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L204-L207), [README.md#L297-L301](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L297-L301), [README.md#L59-L68](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L59-L68)
  - [observation/documented] A local proxy on localhost:3200 exposes control endpoints: POST /_proxy/mode to switch backends, GET /_proxy/status, and GET /_proxy/cost, forwarding /v1/messages to the active backend. -- evidence: [README.md#L162-L162](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L162-L162), [README.md#L164-L173](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L164-L173)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Prerequisites are a logged-in Claude Code install, a claude.ai subscription (the remote bridge is Anthropic infrastructure), Node.js 18+ for the proxy, and backend API keys such as DEEPSEEK_API_KEY. -- evidence: [README.md#L318-L320](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L318-L320), [README.md#L96-L100](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L96-L100), [README.md#L108-L112](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L108-L112), [README.md#L102-L106](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L102-L106)
- limitations (2 claim(s)):
  - [observation/documented] Documented degraded features: no image/vision input through DeepSeek's endpoint, no MCP server tools via the compatibility layer, sequential tool calls by default, and Anthropic cache_control ignored. -- evidence: [README.md#L137-L142](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L137-L142)
  - [observation/documented] The README states Claude Opus is stronger on complex reasoning, recommending --backend anthropic for hard problems while DeepSeek is comparable on routine tasks. -- evidence: [README.md#L145-L146](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L145-L146)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](deepclaude.detail.md) for every claim.)

Metadata and full claim list: [full detail](deepclaude.detail.md)
Human notes ([notes](deepclaude.notes.md), never overwritten by build)

[Back to map index](../../index.md)
