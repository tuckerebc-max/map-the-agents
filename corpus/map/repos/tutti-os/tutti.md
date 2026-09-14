# tutti-os/tutti

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8821cf4788f6 @ e2307a61fc57c0b8

## Summary (orientation draft, not independently verified)

Evidence covers Tutti, an open-source real-time shared workspace for multiple AI agents, with a separate Early Access Tutti · VM product adding multi-user cloud rooms; contributor-facing AGENTS.md and a refactor handoff doc describe repository development practice. Evidence: 3 of 154 candidate documentation files stored (README.md, AGENTS.md, AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md); 151 omitted by file budget, including all architecture and ADR docs; selection incomplete.

## Source coverage

Source coverage (partial): 3 of 154 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] Tutti is described as a real-time shared workspace where multiple agents share context, files, running tasks, and apps, positioned as a layer around existing coding agents rather than a replacement for them. -- evidence: [README.md#L260-L260](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L260-L260), [README.md#L92-L92](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L92-L92), [README.md#L102-L102](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L102-L102), [README.md#L11-L11](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L11-L11)
  - [observation/documented] The project ships two versions: an open-source Tutti for one person with multiple agents, and Tutti · VM (Early Access) adding group chat, multi-user collaboration, and work with others' agents. -- evidence: [README.md#L26-L40](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L26-L40), [README.md#L48-L48](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L48-L48), [README.md#L189-L194](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L189-L194)
- components (1 claim(s)):
  - [observation/documented] Tutti includes an app center shared across the workspace with apps such as image generation (AI Canvas), prototype/UI-UX design, docs, and AI PPT, usable by both humans and agents, with app outputs remaining referenceable in the workspace. -- evidence: [README.md#L80-L80](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L80-L80), [README.md#L146-L149](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L146-L149), [README.md#L138-L138](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L138-L138), [README.md#L155-L155](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L155-L155)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to read the nearest area AGENTS.md before editing, route agent lifecycle work to packages/agent/host, treat Windows as part of the default compatibility contract, and use a pnpm/Oxlint/tsgo toolchain with Husky pre-commit and pre-push hooks. -- evidence: [AGENTS.md#L135-L141](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L135-L141), [AGENTS.md#L162-L162](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L162-L162), [AGENTS.md#L43-L55](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L43-L55), [AGENTS.md#L18-L18](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L18-L18), [AGENTS.md#L164-L165](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L164-L165), [AGENTS.md#L30-L34](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L30-L34)
  - [observation/documented] Repository development practice: a refactor handoff doc records an 800-line file limit for agent business files, a provider descriptor/strategy seam so GUI code has no per-provider identity branches, and completion gated on `pnpm check:full` passing with locked baselines. -- evidence: [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L67-L69](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L67-L69), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L17-L21](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L17-L21), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L51-L54](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L51-L54), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L92-L95](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L92-L95), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L87-L88](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L87-L88)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] In the agent chat box, users can @ past conversations, files, app invocations, and tasks — including those of other agents and, in VM, teammates — and use "+" to reference local files or app outputs. -- evidence: [README.md#L108-L110](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L108-L110), [README.md#L26-L40](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L26-L40), [README.md#L120-L120](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L120-L120), [README.md#L132-L132](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L132-L132)
  - [observation/documented] The product is fully GUI-based with no command line, and offers a Control Center view surfacing agent conversations, pending approvals, and running tasks in one place. -- evidence: [README.md#L179-L179](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L179-L179), [README.md#L171-L171](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L171-L171), [README.md#L224-L224](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L224-L224)
- memory-state (1 claim(s)):
More evidence: [full detail](tutti.detail.md)

Metadata and full claim list: [full detail](tutti.detail.md)
Human notes ([notes](tutti.notes.md), never overwritten by build)

[Back to map index](../../index.md)
