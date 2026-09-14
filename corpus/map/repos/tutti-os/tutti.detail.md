# tutti-os/tutti -- full detail

[Back to orientation](tutti.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tutti-os/tutti/8821cf4788f6a8fe5886942b2ab2890900c14997/e2307a61fc57c0b8.json](../../../wiki/dossiers/tutti-os/tutti/8821cf4788f6a8fe5886942b2ab2890900c14997/e2307a61fc57c0b8.json)

## specifications (3 claim(s))

- [observation/documented] Tutti is described as a real-time shared workspace where multiple agents share context, files, running tasks, and apps, positioned as a layer around existing coding agents rather than a replacement for them. -- evidence: [README.md#L260-L260](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L260-L260), [README.md#L92-L92](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L92-L92), [README.md#L102-L102](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L102-L102), [README.md#L11-L11](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L11-L11) (`clm_34b660108d585b2c6f344ae01d6a5458d7bd66db70a7464d939eb4fa8ae9c97b`)
- [observation/documented] The project ships two versions: an open-source Tutti for one person with multiple agents, and Tutti · VM (Early Access) adding group chat, multi-user collaboration, and work with others' agents. -- evidence: [README.md#L26-L40](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L26-L40), [README.md#L48-L48](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L48-L48), [README.md#L189-L194](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L189-L194) (`clm_e0e42b10ce78f690bd0abe55cd20c3a9a189a936236fada96c83b8494d5fbfe6`)
- [observation/documented] A goals-to-tasks feature lets users describe a goal, after which Tutti breaks it into sub-tasks that the user reviews and assigns to suitable agents. -- evidence: [README.md#L198-L201](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L198-L201), [README.md#L163-L163](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L163-L163) (`clm_3d90a7e15eaf45b8fade2e805002dc60438a83c32b5b28b1be8ca47a8dc346a8`)

## components (1 claim(s))

- [observation/documented] Tutti includes an app center shared across the workspace with apps such as image generation (AI Canvas), prototype/UI-UX design, docs, and AI PPT, usable by both humans and agents, with app outputs remaining referenceable in the workspace. -- evidence: [README.md#L80-L80](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L80-L80), [README.md#L146-L149](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L146-L149), [README.md#L138-L138](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L138-L138), [README.md#L155-L155](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L155-L155) (`clm_1f061d957120e1a8474a2bd8e1e1b52a519f732afad71bc7caa338910fa98a51`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to read the nearest area AGENTS.md before editing, route agent lifecycle work to packages/agent/host, treat Windows as part of the default compatibility contract, and use a pnpm/Oxlint/tsgo toolchain with Husky pre-commit and pre-push hooks. -- evidence: [AGENTS.md#L135-L141](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L135-L141), [AGENTS.md#L162-L162](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L162-L162), [AGENTS.md#L43-L55](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L43-L55), [AGENTS.md#L18-L18](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L18-L18), [AGENTS.md#L164-L165](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L164-L165), [AGENTS.md#L30-L34](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENTS.md#L30-L34) (`clm_74f0db7e0129956f366133374d7557e49d834dcf59b44d26fc3373e8c029b448`)
- [observation/documented] Repository development practice: a refactor handoff doc records an 800-line file limit for agent business files, a provider descriptor/strategy seam so GUI code has no per-provider identity branches, and completion gated on `pnpm check:full` passing with locked baselines. -- evidence: [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L67-L69](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L67-L69), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L17-L21](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L17-L21), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L51-L54](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L51-L54), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L92-L95](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L92-L95), [AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L87-L88](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/AGENT_GUI_CONTROLLER_REFACTOR_HANDOFF.md#L87-L88) (`clm_8fcd12858bf7021174cefa134132993019251ce2483f79f13674bac18487f97c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] In the agent chat box, users can @ past conversations, files, app invocations, and tasks — including those of other agents and, in VM, teammates — and use "+" to reference local files or app outputs. -- evidence: [README.md#L108-L110](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L108-L110), [README.md#L26-L40](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L26-L40), [README.md#L120-L120](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L120-L120), [README.md#L132-L132](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L132-L132) (`clm_e0761c52348509524aa45a8e76efefa19c116797856c295bbd13128cf82b644e`)
- [observation/documented] The product is fully GUI-based with no command line, and offers a Control Center view surfacing agent conversations, pending approvals, and running tasks in one place. -- evidence: [README.md#L179-L179](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L179-L179), [README.md#L171-L171](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L171-L171), [README.md#L224-L224](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L224-L224) (`clm_7e74dc362c4c07b22444cbcf9e1f21ae6e14bcf4c026a04fac55f1bee2b6929d`)

## memory-state (1 claim(s))

- [observation/documented] In open-source Tutti, agents run locally and working state stays local; in Tutti · VM, agents still run locally on the owner's machine inside a managed local VM while working state lives in a cloud Room. -- evidence: [README.md#L232-L232](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L232-L232), [README.md#L234-L234](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L234-L234), [README.md#L189-L194](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L189-L194) (`clm_2db40593235f5a7dd7d81467d490644352a2fd9bade4a45e57f0afb460d61c55`)

## orchestration (1 claim(s))

- [observation/documented] Agents from different providers share visibility into each other's work so they can avoid or resolve conflicts and decide whether work runs in parallel or in sequence. -- evidence: [README.md#L128-L128](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L128-L128) (`clm_457615a89e0549a9295ad06d4a9be53f7a52aa4dc3db29a6a1684ee8f4fb6205`)

## tools-permissions (1 claim(s))

- [observation/documented] In Tutti · VM, sharing is scoped to the Room: only content created inside the same room is shared with invitees, and everything else remains private; creating a Room requires an invite code while joining does not. -- evidence: [README.md#L256-L256](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L256-L256), [README.md#L60-L60](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L60-L60), [README.md#L213-L213](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L213-L213) (`clm_7422bb9f3e0d8d6283a0345d9b4dfb4250c39ecd8581759b7a063bc18242cdf5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Tutti runs agents and apps on users' existing agent subscriptions rather than reselling model access; currently supported are Claude Code, Codex, and Hermes, with OpenClaw noted as in development, and a built-in free Tutti Agent during Early Access. -- evidence: [README.md#L183-L183](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L183-L183), [README.md#L244-L244](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L244-L244), [README.md#L248-L248](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L248-L248), [README.md#L157-L157](https://github.com/tutti-os/tutti/blob/8821cf4788f6a8fe5886942b2ab2890900c14997/README.md#L157-L157) (`clm_ad8cc2e4923bbea755d8f62ad51badc2d31d2994a62d7bad16f51dbdc00840b7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_13c82ecfc17ce94c0635ebe5ba5b56e6e3f700cf92938914ba7b4f01aa9443dd

