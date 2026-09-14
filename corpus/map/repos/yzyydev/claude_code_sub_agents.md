# yzyydev/claude_code_sub_agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7597ed864ce2 @ e2fcdd7a779f6e0a

## Summary (orientation draft, not independently verified)

A README-only snapshot describing a Claude Code multi-agent orchestration project built from three slash commands (/start, /solve, /prime) that spawn parallel sub-agents for iterative content generation and legal case analysis, with a bundled 10-case legal demo. All evidence is documentation, not code inspection.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The system is organized around three command modules in .claude/commands/: start.md (iterative loop orchestrator), solve.md (parallel case processor), and prime.md (context management utilities). -- evidence: [README.md#L13-L13](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L13-L13), [README.md#L229-L247](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L229-L247), [README.md#L17-L22](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L17-L22)
- design-choices (1 claim(s)):
  - [observation/documented] The design uses wave-based agent deployment to manage context limits, fresh agent instances per wave, progressive summarization of completed iterations, and lightweight state tracking in the main orchestrator. -- evidence: [README.md#L108-L111](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L108-L111), [README.md#L180-L184](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L180-L184), [README.md#L26-L29](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L26-L29)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The /start command takes a spec file, an output directory, and a count that may be a number or the literal 'infinite', e.g. /start specs/content_spec.md output/ 5. -- evidence: [README.md#L84-L85](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L84-L85), [README.md#L36-L39](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L36-L39), [README.md#L41-L44](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L41-L44)
  - [observation/documented] The /solve command takes a legal analysis spec, an input directory of scenario files, and an output directory, e.g. /solve specs/law_example.md example_input/ example_output/. -- evidence: [README.md#L60-L63](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L60-L63), [README.md#L96-L97](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L96-L97), [README.md#L55-L58](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L55-L58)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Sub-agents receive structured task prompts specifying the iteration number, full spec analysis, a summary of existing outputs, and an assigned creative direction, with requirements to ensure uniqueness and follow the spec format. -- evidence: [README.md#L171-L178](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L171-L178), [README.md#L165-L169](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L165-L169), [README.md#L163-L163](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L163-L163), [README.md#L159-L161](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L159-L161)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README self-reports tested scenarios including 10 parallel legal analyses, infinite-mode generation with maintained quality, and cross-agent deduplication; these are author claims, not an independent benchmark harness. -- evidence: [README.md#L126-L129](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L126-L129), [README.md#L103-L106](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L103-L106), [README.md#L120-L124](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L120-L124)
- dependencies (1 claim(s)):
  - [observation/documented] The project depends on Claude Code's command system and sub-agent infrastructure, and includes a .claude/settings.local.json configuration file. -- evidence: [README.md#L229-L247](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L229-L247), [README.md#L7-L7](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L7-L7)
- limitations (1 claim(s)):
  - [observation/documented] The README acknowledges context-capacity boundaries, noting wave-based deployment, progressive sophistication strategies, and graceful conclusion planning are used when approaching context limits. -- evidence: [README.md#L126-L129](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L126-L129)
- relevance (1 claim(s)):
  - [observation/documented] A bundled legal education example provides 10 civilian-law scenario files, a law_example.md specification, student instructions, and 10 generated IRAC-format analyses. -- evidence: [README.md#L136-L138](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L136-L138), [README.md#L133-L133](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L133-L133), [README.md#L229-L247](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L229-L247), [README.md#L141-L144](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L141-L144)
More evidence: [full detail](claude_code_sub_agents.detail.md)

Metadata and full claim list: [full detail](claude_code_sub_agents.detail.md)
Human notes ([notes](claude_code_sub_agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
