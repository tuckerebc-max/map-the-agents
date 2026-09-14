# gptme/gptme

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7c8570587edc @ 5a6e65dab4305226

## Summary (orientation draft, not independently verified)

Selected evidence records: gptme is a chat-CLI for LLMs; prompts can be passed as arguments and chained with a '-' separator, and the interface exposes user commands like /undo, /log, /model, /tools, and /export. CLI options include --model, --workspace, --resume, --no-confirm (-y), --non-interactive (-n), --output-format text|json, --system, and a --tools flag restricting tools to a comma-separated allowlist.

## Source coverage

Source coverage (partial): 6 of 200 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Built-in tools documented include shell, ipython, read, save/append, patch/morph, browser (Playwright), vision, screenshot, rag, gh, tmux, computer, subagent, and chats. -- evidence: [README.md#L275-L290](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L275-L290)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README says contributions are welcome and points contributors to the contributing guide at gptme.org/docs/contributing.html; it also notes the codebase is checked and formatted with mypy, ruff, and pyupgrade. -- evidence: [README.md#L422-L433](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L422-L433), [README.md#L657-L657](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L657-L657)
- skills-patterns (1 claim(s)):
  - [observation/documented] Extensibility layers include Python-package plugins configured in gptme.toml, Anthropic-format skills that auto-load when named, keyword/pattern-matched lessons injected into conversations, and lifecycle hooks. -- evidence: [README.md#L302-L305](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L302-L305), [README.md#L311-L311](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L311-L311), [README.md#L307-L307](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L307-L307), [README.md#L298-L298](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L298-L298), [README.md#L309-L309](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L309-L309)
- interfaces (5 claim(s)):
  - [observation/documented] gptme is a chat-CLI for LLMs; prompts can be passed as arguments and chained with a '-' separator, and the interface exposes user commands like /undo, /log, /model, /tools, and /export. -- evidence: [README.md#L547-L549](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L547-L549), [README.md#L554-L555](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L554-L555), [README.md#L560-L580](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L560-L580), [README.md#L551-L552](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L551-L552)
  - [observation/documented] CLI options include --model, --workspace, --resume, --no-confirm (-y), --non-interactive (-n), --output-format text|json, --system, and a --tools flag restricting tools to a comma-separated allowlist. -- evidence: [README.md#L588-L615](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L588-L615)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] gptme service init scaffolds a self-contained headless agent: a systemd service unit, optional timer (hourly/daily/weekly/on-demand), a startup script running one non-interactive session per trigger, prompt.md, and config skeletons. -- evidence: [README.md#L391-L391](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L391-L391), [README.md#L384-L389](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L384-L389), [README.md#L374-L374](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L374-L374)
  - [observation/documented] The gptme-agent-template supports persistent autonomous agents with a git-tracked workspace, run loops, task queues, multi-agent coordination via file leases and a message bus, and external integrations like GitHub and Discord. -- evidence: [README.md#L352-L352](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L352-L352), [README.md#L354-L359](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L354-L359)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README advertises an evaluation suite for testing capabilities of different models, with advanced frontier-capability evals listed as in progress. -- evidence: [README.md#L437-L441](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L437-L441), [README.md#L422-L433](https://github.com/gptme/gptme/blob/7c8570587edca8a819777ba660f67ef2f3878cb5/README.md#L422-L433)
- dependencies (2 claim(s)):
More evidence: [full detail](gptme.detail.md)

Metadata and full claim list: [full detail](gptme.detail.md)
Human notes ([notes](gptme.notes.md), never overwritten by build)

[Back to map index](../../index.md)
