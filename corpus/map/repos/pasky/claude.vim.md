# pasky/claude.vim

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 06baac1ed450 @ ab4d248724fbd4e3

## Summary (orientation draft, not independently verified)

README-only evidence for pasky/claude.vim, a Vim/Neovim plugin integrating Claude as a pair-programming chat/implementation assistant with tool use, vimdiff review, and configurable API providers. Evidence covers product description, usage modes, configuration, and cost/alpha caveats; no code or development-practice files are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The plugin is explicitly not code completion like Copilot; it provides a chat/instruction-centric interface optimized for human collaboration, with chat history access and vimdiff review as key features. -- evidence: [README.md#L12-L19](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L12-L19)
  - [observation/documented] Because Sonnet 3.5 is not deemed capable of fully autonomous complex tasks, the design keeps the human in control: users chat, review, and can reject changes and tool execution attempts. -- evidence: [README.md#L58-L60](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L58-L60)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The plugin offers two main interaction modes: a simple implementation assistant (ClaudeImplement) and a chat interface (ClaudeChat). -- evidence: [README.md#L133-L134](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L133-L134), [README.md#L131-L131](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L131-L131)
  - [observation/documented] ClaudeImplement works on a visual-mode selection: the selected block is all Claude sees, with no additional context, and proposed changes are reviewed in diff mode. -- evidence: [README.md#L141-L147](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L141-L147), [README.md#L138-L139](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L138-L139)
- memory-state (1 claim(s)):
  - [observation/documented] Chat history is sent to Claude with each request; previous interactions are folded in the buffer and users can edit or delete the history to redact it. -- evidence: [README.md#L174-L177](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L174-L177)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The plugin can open files and execute vim commands via a Claude Tools interface, and can evaluate Python expressions only with the user's case-by-case consent. -- evidence: [README.md#L39-L40](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L39-L40), [README.md#L35-L35](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L35-L35)
  - [observation/documented] The current version can also execute shell scripts, and the plugin can search the web when it lacks knowledge, with web access requiring elinks or felinks installed. -- evidence: [README.md#L52-L52](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L52-L52), [README.md#L90-L93](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L90-L93), [README.md#L48-L48](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L48-L48)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Web access depends on installing elinks or felinks; Google search additionally requires a one-time manual cookie-consent step in elinks. -- evidence: [README.md#L90-L93](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L90-L93)
  - [observation/documented] The plugin uses the Anthropic Claude API by default (API key set via g:claude_api_key), with AWS Bedrock available as an alternative provider via g:claude_use_bedrock. -- evidence: [README.md#L107-L109](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L107-L109), [README.md#L97-L99](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L97-L99), [README.md#L111-L111](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L111-L111)
- limitations (2 claim(s)):
More evidence: [full detail](claude.vim.detail.md)

Metadata and full claim list: [full detail](claude.vim.detail.md)
Human notes ([notes](claude.vim.notes.md), never overwritten by build)

[Back to map index](../../index.md)
