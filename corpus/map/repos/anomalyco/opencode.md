# anomalyco/opencode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit df23b7f9488a @ 62fba2c78cec8b3e

## Summary (orientation draft, not independently verified)

OpenCode is an open-source AI coding agent with built-in build/plan/general agents, a permission-based agent runtime, installable via many channels including a desktop app documented as BETA, and a documented session context architecture. Evidence coverage: 123 of 195 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 8 of 29 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 9 documented, 6 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The README documents two built-in agents switchable with the Tab key: build (default, full access) and plan (read-only, denies file edits by default and asks before running bash commands), plus a general subagent invoked via @general. -- evidence: [README.md#L104-L108](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L104-L108), [README.md#L102-L102](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L102-L102), [README.md#L110-L111](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L110-L111)
  - [observation/code-inspected] The plan agent's permission config denies all edit tools except plan markdown files under .opencode/plans and the global plans data directory, and denies the general task subagent. -- evidence: [packages/opencode/src/agent/agent.ts#L140-L265](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L140-L265)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to read CONTRIBUTING.md before submitting pull requests, and derivative projects using 'opencode' in their name must state they are unaffiliated with the OpenCode team. -- evidence: [README.md#L125-L125](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L125-L125), [README.md#L121-L121](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L121-L121)
- skills-patterns (1 claim(s)):
  - [observation/code-inspected] Users can define custom agents in config; entries can disable built-ins or add new agents whose properties (model, prompt, permissions, mode, etc.) are merged over defaults. -- evidence: [packages/opencode/src/agent/agent.ts#L267-L294](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L267-L294)
- interfaces (4 claim(s)):
  - [observation/code-inspected] Agent configuration is a schema with name, description, mode (subagent/primary/all), permission ruleset, optional model, prompt, temperature, topP, steps, variant, color, and hidden fields. -- evidence: [packages/opencode/src/agent/agent.ts#L35-L56](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L35-L56)
  - [observation/documented] The install script resolves its target directory by priority: OPENCODE_INSTALL_DIR, XDG_BIN_DIR, $HOME/bin, then $HOME/.opencode/bin as fallback. -- evidence: [README.md#L89-L92](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L89-L92), [README.md#L87-L87](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/README.md#L87-L87)
- memory-state (2 claim(s)):
  - [observation/documented] CONTEXT.md defines a session runtime where sessions preserve durable conversation history and assemble a System Context from typed Context Sources, with changes admitted as Mid-Conversation System Messages at safe provider-turn boundaries. -- evidence: [CONTEXT.md#L22-L24](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L22-L24), [CONTEXT.md#L39-L40](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L39-L40), [CONTEXT.md#L3-L3](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L3-L3), [CONTEXT.md#L15-L17](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L15-L17)
  - [observation/documented] Tool outputs exceeding history limits are projected into bounded Model Tool Output, with full oversized output retained in a managed temporary file under a shared tool-output directory. -- evidence: [CONTEXT.md#L54-L55](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L54-L55), [CONTEXT.md#L57-L58](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/CONTEXT.md#L57-L58)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/code-inspected] The agent module defines default permission rules: wildcard allow, ask for doom_loop and external directories, deny for question and plan transitions, and ask for reading .env files while allowing .env.example. -- evidence: [packages/opencode/src/agent/agent.ts#L119-L136](https://github.com/anomalyco/opencode/blob/df23b7f9488a38e6f8064a0739d4f8cde86d7cfb/packages/opencode/src/agent/agent.ts#L119-L136)
More evidence: [full detail](opencode.detail.md)

Metadata and full claim list: [full detail](opencode.detail.md)
Human notes ([notes](opencode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
