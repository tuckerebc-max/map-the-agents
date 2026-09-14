# proxysoul/empryo

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f771fc238e64 @ 945eb6c6544cb407

## Summary (orientation draft, not independently verified)

The repository is the public home for Empryo (formerly SoulForge), a local-first AI coding agent with a tree-sitter code graph, symbol-level AST editing, a multi-model task router, and desktop/terminal/CLI surfaces. Evidence is documentation-only (README, GETTING_STARTED, governance and license docs); no runtime source code is included in the snapshot. Evidence coverage: 171 of 199 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product offers 65+ symbol-level AST editing operations with atomic all-or-nothing rollback and structural edits across 30+ languages, with a typecheck as the gate. -- evidence: [README.md#L53-L56](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L53-L56), [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69)
- design-choices (1 claim(s)):
  - [observation/documented] Empryo builds codebase understanding before mutating code: on launch, tree-sitter parses the repo into a live graph of symbols, imports, and call sites ranked by PageRank and git co-change. -- evidence: [README.md#L53-L56](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L53-L56), [README.md#L51-L51](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L51-L51)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: governance is single-maintainer; architecture changes and public API/SDK changes require opening an issue first, and CODEOWNERS prevents self-merging of PRs touching IP-sensitive paths. -- evidence: [GOVERNANCE.md#L17-L26](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L17-L26), [GOVERNANCE.md#L3-L3](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L3-L3), [GOVERNANCE.md#L36-L36](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L36-L36), [GOVERNANCE.md#L40-L43](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L40-L43)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Three surfaces share one code graph: a native desktop app, a full terminal UI, and a headless CLI for scripts and CI. -- evidence: [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69)
  - [observation/documented] The terminal UI embeds a real Neovim instance (Ctrl+E toggles focus), with config modes selectable via /nvim-config (auto, user, default, none). -- evidence: [GETTING_STARTED.md#L132-L134](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L132-L134), [GETTING_STARTED.md#L25-L25](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L25-L25), [GETTING_STARTED.md#L142-L142](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L142-L142), [GETTING_STARTED.md#L128-L128](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L128-L128), [GETTING_STARTED.md#L144-L149](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L144-L149)
- memory-state (2 claim(s)):
  - [observation/documented] A SQLite-backed memory system stores decisions, patterns, and preferences across conversations, with write scope configurable to session, project, or global and memories injected into the system prompt. -- evidence: [GETTING_STARTED.md#L270-L271](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L270-L271), [GETTING_STARTED.md#L268-L268](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L268-L268)
  - [observation/documented] Every prompt creates a git checkpoint ('time machine'), letting users rewind code and conversation together to any turn. -- evidence: [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69)
- orchestration (1 claim(s)):
  - [observation/documented] A task router assigns models to ten routable roles (e.g. spark for read-only scouting, ember for code edits, verify for review), configurable per tab, per project, or globally, with custom agents definable. -- evidence: [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69), [README.md#L77-L77](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L77-L77), [GETTING_STARTED.md#L159-L168](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L159-L168), [README.md#L81-L85](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L81-L85), [README.md#L73-L73](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L73-L73)
- tools-permissions (1 claim(s)):
  - [observation/documented] A privacy feature lets users block file patterns (e.g. .env, secrets/**) via /privacy add; the agent then refuses to read, display, or access matching files even through shell commands. -- evidence: [GETTING_STARTED.md#L292-L292](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L292-L292), [GETTING_STARTED.md#L285-L285](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L285-L285), [GETTING_STARTED.md#L287-L290](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L287-L290)
More evidence: [full detail](empryo.detail.md)

Metadata and full claim list: [full detail](empryo.detail.md)
Human notes ([notes](empryo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
