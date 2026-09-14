# langchain-ai/openwiki

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e92cc11723a8 @ 33a575400f233391

## Summary (orientation draft, not independently verified)

OpenWiki is a CLI that writes and maintains a wiki for a codebase or personal knowledge, generating linked Markdown intended as agent memory, with an interactive visualizer for humans. The tool offers two modes: a default 'code' wiki for the current repository written to openwiki/, and a 'personal' wiki for connected sources written to ~/.openwiki/wiki. Evidence coverage: 139 of 319 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] OpenWiki is a CLI that writes and maintains a wiki for a codebase or personal knowledge, generating linked Markdown intended as agent memory, with an interactive visualizer for humans. -- evidence: [README.md#L19-L19](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L19-L19)
- components (2 claim(s)):
  - [observation/documented] Grounded Claims track material propositions in code wikis back to versioned repository evidence (e.g. repo:// paths with line ranges), stored as sidecars under openwiki/.claims/ rather than in the Markdown. -- evidence: [README.md#L141-L141](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L141-L141), [README.md#L256-L260](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L256-L260), [README.md#L147-L147](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L147-L147)
  - [observation/documented] Personal mode supports nine connectors (Custom MCP, Notion, Slack, Gmail, X, Web Search, Hacker News, LangSmith, local git); connector secrets are referenced by env var in ~/.openwiki/.env and never stored in config files. -- evidence: [README.md#L205-L205](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L205-L205), [README.md#L231-L231](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L231-L231), [README.md#L23-L31](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L23-L31), [README.md#L220-L227](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L220-L227)
- design-choices (2 claim(s)):
  - [observation/documented] The tool offers two modes: a default 'code' wiki for the current repository written to openwiki/, and a 'personal' wiki for connected sources written to ~/.openwiki/wiki. -- evidence: [README.md#L155-L155](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L155-L155), [README.md#L23-L31](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L23-L31), [README.md#L157-L160](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L157-L160)
  - [observation/documented] Output follows Open Knowledge Format (OKF) v0.2 with YAML front matter, generated/verified provenance stamps, validated optional trust and lifecycle fields, and reserved index.md and log.md documents. -- evidence: [README.md#L266-L273](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L266-L273), [README.md#L264-L264](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L264-L264)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors adding another coding-agent integration are directed to follow the 'Adding a coding-agent integration' section of CONTRIBUTING.md. -- evidence: [README.md#L136-L137](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L136-L137)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Coding-agent integrations expose an MCP page-job lifecycle via tools named openwiki_begin, openwiki_submit_plan, openwiki_next_page, openwiki_inspect_page_claims, openwiki_submit_page, and openwiki_finish for Codex, Claude Code, OpenCode, and Cursor. -- evidence: [README.md#L132-L132](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L132-L132), [README.md#L101-L101](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L101-L101)
- memory-state (1 claim(s)):
  - [observation/documented] Local state (credentials, personal wiki, connector data, history, skills) lives under ~/.openwiki by default, relocatable via OPENWIKI_CONFIG_DIR; the override does not move or delete the existing directory. -- evidence: [README.md#L166-L166](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L166-L166), [README.md#L172-L172](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L172-L172), [README.md#L168-L170](https://github.com/langchain-ai/openwiki/blob/e92cc11723a852b05b7983ab1a61feab96d75ba9/README.md#L168-L170)
- orchestration (1 claim(s)):
More evidence: [full detail](openwiki.detail.md)

Metadata and full claim list: [full detail](openwiki.detail.md)
Human notes ([notes](openwiki.notes.md), never overwritten by build)

[Back to map index](../../index.md)
