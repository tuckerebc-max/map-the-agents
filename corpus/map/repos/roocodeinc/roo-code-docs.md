# roocodeinc/roo-code-docs

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a676c4173ae6 @ 4f3c03b6e158e322

## Summary (orientation draft, not independently verified)

The repository is the Docusaurus documentation site for Roo Code (docs.roocode.com), documenting an AI coding suite offered as a VS Code Extension and Cloud Agents, with modes, tool approval, MCP, skills, providers, and codebase indexing; a sunset notice announces shutdown of all products on May 15, 2026. Evidence coverage: 158 of 171 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 529 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Roo Code is described as an AI-powered suite of coding products that uses large language models to understand user requests and translate them into actions. -- evidence: [docs/faq.md#L29-L29](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L29-L29), [docs/faq.md#L25-L25](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L25-L25)
- components (1 claim(s)):
  - [observation/documented] The product ships in two forms: a VS Code Extension working locally in the IDE, and Roo Code Cloud Agents described as an autonomous AI development team reachable via channels like Slack and GitHub. -- evidence: [docs/index.mdx#L24-L26](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/index.mdx#L24-L26)
- design-choices (1 claim(s)):
  - [observation/documented] Roo Code offers persona-based modes (Code, Architect, Ask, Debug) plus user-created Custom Modes, switchable via a dropdown or the '/' command. -- evidence: [docs/faq.md#L106-L106](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L106-L106), [docs/faq.md#L98-L102](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L98-L102), [docs/faq.md#L96-L96](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L96-L96)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the docs site is built with Docusaurus; contributors install dependencies with pnpm install and run a local dev server with pnpm start, which live-reloads changes without restart. -- evidence: [README.md#L17-L17](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L17-L17), [README.md#L3-L3](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L3-L3), [README.md#L7-L9](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L7-L9), [README.md#L13-L15](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L13-L15)
  - [observation/documented] Repository development practice: the README displays an Apache 2.0 license badge linking to the LICENSE file. -- evidence: [README.md#L21-L21](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L21-L21)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are SKILL.md files with required name/description frontmatter that Roo loads on demand via progressive disclosure: metadata is indexed at startup, full instructions load only when a request matches, and bundled resources are discovered on demand. -- evidence: [docs/features/skills.mdx#L60-L60](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L60-L60), [docs/features/skills.mdx#L58-L58](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L58-L58), [docs/features/skills.mdx#L104-L104](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L104-L104), [docs/features/skills.mdx#L14-L14](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L14-L14), [docs/features/skills.mdx#L62-L62](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L62-L62), [docs/features/skills.mdx#L230-L233](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L230-L233)
  - [observation/documented] Skills live in .roo/skills/ or .agents/skills/ directories (global or project), support mode-specific variants like skills-code/, and follow an eight-level override priority where project beats global and .roo beats .agents. -- evidence: [docs/features/skills.mdx#L219-L219](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L219-L219), [docs/features/skills.mdx#L208-L208](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L208-L208), [docs/features/skills.mdx#L183-L186](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L183-L186), [docs/features/skills.mdx#L75-L75](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L75-L75), [docs/features/skills.mdx#L210-L217](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L210-L217), [docs/features/skills.mdx#L88-L88](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L88-L88)
- interfaces (1 claim(s)):
  - [observation/documented] The Extension exposes a chat panel (Kangaroo icon) where tasks are typed, supports '@' context mentions for files, folders, and problems, and offers error diagnostics export with basic and detailed options. -- evidence: [docs/reporting-errors.md#L20-L20](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/reporting-errors.md#L20-L20), [docs/reporting-errors.md#L32-L35](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/reporting-errors.md#L32-L35), [docs/faq.md#L112-L112](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L112-L112), [docs/reporting-errors.md#L39-L43](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/reporting-errors.md#L39-L43), [docs/faq.md#L93-L93](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L93-L93)
- memory-state (1 claim(s)):
More evidence: [full detail](roo-code-docs.detail.md)

Metadata and full claim list: [full detail](roo-code-docs.detail.md)
Human notes ([notes](roo-code-docs.notes.md), never overwritten by build)

[Back to map index](../../index.md)
