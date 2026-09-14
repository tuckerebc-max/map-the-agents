# wendy7756/vibe-coding-guide

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 96368d319e86 @ a50fdf4d5e48b5a6

## Summary (orientation draft, not independently verified)

The repository is a bilingual (Chinese/English) documentation-only guide to 'Vibe Coding' — AI-assisted natural-language programming — containing definitions, workflows, tool listings, best practices, references, a contribution guide, and an Apache 2.0 license notice. No product runtime or code is evidenced. Evidence coverage: 160 of 166 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] The guide defines Vibe Coding as collaborative programming where developers describe requirements in natural language and an LLM generates complete runnable code, refined through iterative feedback. -- evidence: [README_EN.md#L36-L36](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L36-L36), [README.md#L36-L36](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L36-L36)
  - [observation/documented] It attributes the Vibe Coding concept to Andrej Karpathy, described as an OpenAI co-founder, introducing it in early 2025. -- evidence: [README_EN.md#L40-L43](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L40-L43), [README.md#L40-L43](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L40-L43)
- components (1 claim(s)):
  - [observation/documented] It catalogs AI programming tools across categories including mainstream assistants (GitHub Copilot, Cursor, Claude Code), extensions (Cline, Roo Code, Tabnine), no-code builders (Lovable, Bolt.new, v0.dev), and cloud IDEs (Replit, CodeSandbox, Gitpod). -- evidence: [README.md#L161-L164](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L161-L164), [README.md#L153-L156](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L153-L156), [README_EN.md#L169-L171](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L169-L171), [README_EN.md#L149-L151](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L149-L151), [README.md#L167-L169](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L167-L169), [README_EN.md#L163-L166](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L163-L166), [README_EN.md#L155-L158](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L155-L158), [README.md#L148-L150](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L148-L150)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] The guide describes a five-step iterative core workflow: natural-language input, AI code generation, execution and observation, feedback and refinement, and an iteration loop. -- evidence: [README.md#L59-L62](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L59-L62), [README.md#L98-L101](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L98-L101), [README.md#L55-L55](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L55-L55), [README_EN.md#L55-L55](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L55-L55), [README.md#L86-L89](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L86-L89), [README.md#L79-L82](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L79-L82), [README.md#L72-L75](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L72-L75)
  - [observation/documented] Repository development practice: the contribution guide instructs contributors to fork the repo, create a feature branch, commit, push, and open a pull request. -- evidence: [README.md#L463-L467](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L463-L467), [README.md#L461-L461](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L461-L461)
- skills-patterns (1 claim(s)):
  - [observation/documented] Best-practice sections advise writing specific prompts that state the tech stack, constraints, and expected results, and developing iteratively in small steps while referencing earlier code for context. -- evidence: [README_EN.md#L296-L300](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L296-L300), [README.md#L312-L314](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L312-L314), [README.md#L295-L299](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L295-L299), [README_EN.md#L313-L315](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L313-L315)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The guide lists underlying LLMs it considers foundational to Vibe Coding, including GPT-4/GPT-4o, Claude Sonnet, and Gemini Pro. -- evidence: [README_EN.md#L108-L111](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L108-L111), [README.md#L108-L111](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L108-L111)
- limitations (1 claim(s)):
  - [observation/documented] A troubleshooting section lists common problems with AI-generated code: poor code quality, loss of conversational context, and over-reliance on AI, each with suggested mitigations. -- evidence: [README_EN.md#L334-L338](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L334-L338), [README_EN.md#L320-L324](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L320-L324), [README.md#L327-L331](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L327-L331), [README.md#L320-L324](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L320-L324), [README.md#L334-L338](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README.md#L334-L338), [README_EN.md#L327-L331](https://github.com/wendy7756/vibe-coding-guide/blob/96368d319e867fa69cbfcae5fcdde287c9202618/README_EN.md#L327-L331)
- relevance (2 claim(s)):
More evidence: [full detail](vibe-coding-guide.detail.md)

Metadata and full claim list: [full detail](vibe-coding-guide.detail.md)
Human notes ([notes](vibe-coding-guide.notes.md), never overwritten by build)

[Back to map index](../../index.md)
