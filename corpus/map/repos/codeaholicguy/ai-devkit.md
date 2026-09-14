# codeaholicguy/ai-devkit

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1a3a0024eb3b @ fadc9f2153ecec7e

## Summary (orientation draft, not independently verified)

AI DevKit is a local-first control plane for AI coding agents: one .ai-devkit.json config, an agent console/send CLI, local SQLite memory via MCP and CLI, and nine built-in engineering skills. Claims are drawn from README and CHANGELOG slices; one prior claim was narrowed (agent kill is documented as a console command, not a standalone CLI subcommand). Evidence coverage: 111 of 175 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 454 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project comprises packages including cli, agent-manager, channel-connector, and memory, which were migrated from CommonJS to ES Modules with Vitest replacing Jest. -- evidence: [CHANGELOG.md#L292-L293](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L292-L293)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install and npm run build, and contributing guidance lives in CONTRIBUTING.md. -- evidence: [README.md#L240-L243](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L240-L243), [README.md#L236-L238](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L236-L238)
- skills-patterns (2 claim(s)):
  - [observation/documented] Nine built-in skills are documented, anchored by dev-lifecycle, plus verify, tdd, structured-debug, memory, dev-commit, document-code, simplify-implementation, and technical-writer. -- evidence: [README.md#L176-L186](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L176-L186), [README.md#L174-L174](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L174-L174)
  - [observation/documented] The verify skill blocks completion claims without fresh test or build evidence, and dev-commit checks diffs, stages explicit paths, validates, and reports the SHA/status. -- evidence: [README.md#L128-L132](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L128-L132), [README.md#L176-L186](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L176-L186)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI exposes agent subcommands including agent list, agent detail, agent console, agent send, agent start, and agent rename; agent kill is documented as a console command with confirmation and tmux cleanup. -- evidence: [README.md#L86-L86](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L86-L86), [README.md#L92-L92](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L92-L92), [CHANGELOG.md#L271-L272](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L271-L272), [CHANGELOG.md#L264-L265](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L264-L265), [README.md#L21-L27](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L21-L27), [README.md#L89-L89](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L89-L89)
  - [observation/documented] agent send supports --stdin for piped input, --wait to block until a response, --timeout in milliseconds, --json structured output, and --group for sending to saved agent groups. -- evidence: [README.md#L98-L98](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L98-L98), [CHANGELOG.md#L335-L335](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L335-L335), [CHANGELOG.md#L322-L325](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L322-L325), [README.md#L95-L95](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L95-L95)
- memory-state (1 claim(s)):
  - [observation/documented] Memory stores project decisions, conventions, and fixes in a local SQLite file, exposed through MCP and CLI, with store and search commands and opt-in hybrid semantic search. -- evidence: [README.md#L108-L108](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L108-L108), [CHANGELOG.md#L41-L41](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L41-L41), [README.md#L112-L116](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L112-L116), [README.md#L11-L15](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L11-L15), [README.md#L119-L120](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L119-L120)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] A changelog entry reports retrieval-quality metrics for hybrid semantic memory search tuning: judged irrelevant top-3 results fell from 4.7% to 2.5% while hit@3 stayed at 97%. -- evidence: [CHANGELOG.md#L30-L30](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L30-L30)
- dependencies (2 claim(s)):
More evidence: [full detail](ai-devkit.detail.md)

Metadata and full claim list: [full detail](ai-devkit.detail.md)
Human notes ([notes](ai-devkit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
