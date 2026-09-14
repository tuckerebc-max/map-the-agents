# jcodesmore/ai-website-cloner-template

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 92872bc40ced @ 62fbb0920530124a

## Summary (orientation draft, not independently verified)

The template provides a /clone-website skill that runs a multi-phase pipeline: reconnaissance, foundation, component specs, parallel build, and assembly with QA. During the parallel-build phase, builder agents are dispatched in git worktrees, one per section or component, and later merged during assembly. Evidence coverage: 141 of 142 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md is the single source of truth for agent instructions; scripts/sync-agent-rules.sh and scripts/sync-skills.mjs regenerate platform-specific copies, and CLAUDE.md/GEMINI.md import AGENTS.md. -- evidence: [README.md#L196-L196](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L196-L196), [README.md#L203-L203](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L203-L203), [GEMINI.md#L1-L1](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/GEMINI.md#L1-L1), [README.md#L198-L201](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L198-L201), [README.md#L149-L175](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L149-L175)
  - [observation/documented] Repository development practice: contributors run npm run dev/build/lint/typecheck/check, and Docker users can run the app or dev mode on port 3001 via docker compose. -- evidence: [README.md#L189-L192](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L189-L192), [README.md#L179-L185](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L179-L185)
- skills-patterns (2 claim(s)):
  - [observation/documented] The template provides a /clone-website skill that runs a multi-phase pipeline: reconnaissance, foundation, component specs, parallel build, and assembly with QA. -- evidence: [README.md#L117-L117](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L117-L117), [README.md#L127-L131](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L127-L131), [README.md#L119-L125](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L119-L125)
  - [observation/documented] Each builder agent receives the full component specification inline, including exact getComputedStyle() values, interaction models, multi-state content, breakpoints, and asset paths. -- evidence: [README.md#L133-L133](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L133-L133)
- interfaces (1 claim(s)):
  - [observation/documented] The skill is invoked as /clone-website <target-url1> [<target-url2> ...]; clients that activate skills via natural language accept a phrasing like 'Clone <target-url> using the clone-website workflow'. -- evidence: [README.md#L83-L83](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L83-L83), [README.md#L69-L81](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L69-L81)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] During the parallel-build phase, builder agents are dispatched in git worktrees, one per section or component, and later merged during assembly. -- evidence: [README.md#L127-L131](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L127-L131)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The scaffolded stack is Next.js 16 (App Router, React 19, TypeScript strict), shadcn/ui with Radix primitives, Tailwind CSS v4 with oklch tokens, and Lucide React icons; Node.js 24+ is a prerequisite. -- evidence: [AGENTS.md#L17-L21](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/AGENTS.md#L17-L21), [README.md#L110-L113](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L110-L113), [README.md#L105-L106](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L105-L106)
- limitations (1 claim(s)):
  - [observation/documented] The project explicitly states it must not be used for phishing, impersonation, passing off others' designs, or violating sites' terms of service regarding scraping or reproduction. -- evidence: [README.md#L143-L145](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L143-L145)
- relevance (1 claim(s)):
More evidence: [full detail](ai-website-cloner-template.detail.md)

Metadata and full claim list: [full detail](ai-website-cloner-template.detail.md)
Human notes ([notes](ai-website-cloner-template.notes.md), never overwritten by build)

[Back to map index](../../index.md)
