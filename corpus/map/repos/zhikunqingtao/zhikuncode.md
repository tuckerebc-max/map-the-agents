# zhikunqingtao/zhikuncode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 931a9beebf21 @ c7992362e1b91e4b

## Summary (orientation draft, not independently verified)

ZhikunCode is documented as a browser-controlled, self-hostable AI coding assistant with a Java/React/Python three-tier architecture, a unified Tool Gateway authorization pipeline, MCP tools gated by a three-layer whitelist/toggle/credential check, and direct connections to several Chinese LLM providers. The README reports an official-harness SWE-bench Lite result with open-sourced evaluation artifacts. Evidence: only 6 of 920 candidate files stored (README.md and five smaller docs/case-study files); selection incomplete, so most of the codebase and documentation is unexamined.

## Source coverage

Source coverage (partial): 6 of 920 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes ZhikunCode as an open-source AI programming assistant deployed once and controllable entirely from a browser, with multi-agent collaboration, Docker self-hosting, direct connections to domestic Chinese LLM providers, and what it calls a deep security architecture. -- evidence: [README.md#L3-L7](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L3-L7)
- components (1 claim(s)):
  - [observation/documented] Documentation describes a three-tier architecture: a Java 21/Spring Boot backend handling core orchestration, LLM routing, and the authorization gateway; a React/TypeScript frontend for the interactive UI; and an optional Python/FastAPI service for code analysis and MCP bridging. -- evidence: [README.md#L534-L538](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L534-L538), [README.md#L514-L514](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L514-L514)
- design-choices (1 claim(s)):
  - [observation/documented] Documentation states that on a 402 quota-exceeded or 404 model-unavailable response, the system automatically cools that key down for 15 minutes and switches to the next configured API key. -- evidence: [README.md#L356-L357](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L356-L357)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state (1 claim(s)):
  - [observation/documented] The README describes a six-level context-compression cascade (Snip, MicroCompact, ContextCollapse, AutoCompact, CollapseDrain, ReactiveCompact) intended to keep sessions within the context window, with a documented two-stage CollapseDrain/ReactiveCompact recovery path for large sessions. -- evidence: [README.md#L453-L456](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L453-L456)
- orchestration (1 claim(s)):
  - [observation/documented] The README lists three multi-agent collaboration modes: Team for fixed role division, Swarm for dynamic negotiation, and SubAgent for master/subordinate delegation. -- evidence: [README.md#L120-L141](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L120-L141)
- tools-permissions (3 claim(s)):
  - [observation/documented] Documentation describes a unified authorization pipeline where core tools pass through a Tool Gateway: input normalization, an Operation Analyzer risk/resource check, a system-invariant check, a RUN/SESSION/WORKSPACE grant match or persistent-permission prompt, a pre-execution recheck, and a structured audit of results; high-risk operations are limited to single-use authorization. -- evidence: [README.md#L120-L141](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L120-L141)
More evidence: [full detail](zhikuncode.detail.md)

Metadata and full claim list: [full detail](zhikuncode.detail.md)
Human notes ([notes](zhikuncode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
