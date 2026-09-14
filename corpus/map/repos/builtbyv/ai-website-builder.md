# builtbyv/ai-website-builder

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4bf3931a9651 @ 1e18c90010473fad

## Summary (orientation draft, not independently verified)

The repository is a website template designed to be built and updated by conversing with AI coding assistants (Claude Code, Codex CLI, Gemini CLI), with a skill installer, launcher/setup scripts, a two-terminal preview workflow, and publish scripts for free hosting platforms. AGENTS.md contains agent-facing guardrails treated here as repository development practice. Evidence coverage: 178 of 204 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is a website template intended to be built and updated through conversation with AI assistants, with users describing changes in their own language and no coding required. -- evidence: [README.md#L7-L7](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L7-L7), [README.md#L3-L3](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs the assistant to never start background processes, only check whether port 5173 is listening, and ask the user to run npm run dev themselves. -- evidence: [AGENTS.md#L17-L22](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L17-L22)
  - [observation/documented] Repository development practice: AGENTS.md forbids publishing without explicit confirmation and requires blocking publication if placeholders or broken essentials exist. -- evidence: [AGENTS.md#L7-L11](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L7-L11)
- skills-patterns (3 claim(s)):
  - [observation/documented] A one-line curl|bash installer places the skill in ~/.claude/skills/ai-website-builder/ and also into ~/.agents/skills/ai-website-builder/ if that directory already exists. -- evidence: [README.md#L39-L39](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L39-L39), [README.md#L41-L43](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L41-L43)
  - [observation/documented] The skill is described as fully self-contained, bundling the starter template, publish scripts, style guides, and the instructions the AI needs to build websites. -- evidence: [README.md#L59-L59](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L59-L59)
- interfaces (1 claim(s)):
  - [observation/documented] The documented workflow uses two terminals: one runs 'npm run dev' serving a preview at http://localhost:5173, the other starts the AI assistant via npx claude, npx codex, or npx gemini. -- evidence: [README.md#L319-L319](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L319-L319), [README.md#L313-L317](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L313-L317), [README.md#L304-L304](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L304-L304), [README.md#L297-L300](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L297-L300)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] A setup.sh script checks the machine, installs the chosen AI CLI(s), completes setup, and provides a quick reference guide; launcher scripts for Windows (.bat), Mac (.app zip), and Linux (.sh) automate the flow including downloading the project and starting the assistant. -- evidence: [README.md#L84-L90](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L84-L90), [README.md#L68-L70](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L68-L70), [README.md#L162-L166](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L162-L166), [README.md#L73-L76](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L73-L76), [README.md#L79-L82](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L79-L82)
  - [observation/documented] Publishing is triggered by telling the AI to publish; AGENTS.md maps platforms to npm scripts (publish:github, publish:cloudflare, publish:netlify, publish:vercel) with npm run deploy as an interactive menu fallback. -- evidence: [README.md#L343-L347](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L343-L347), [AGENTS.md#L193-L198](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L193-L198), [README.md#L323-L326](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L323-L326)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](ai-website-builder.detail.md)

Metadata and full claim list: [full detail](ai-website-builder.detail.md)
Human notes ([notes](ai-website-builder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
