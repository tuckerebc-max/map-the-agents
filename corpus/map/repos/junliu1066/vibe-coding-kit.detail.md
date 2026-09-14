# junliu1066/vibe-coding-kit -- full detail

[Back to orientation](vibe-coding-kit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/junliu1066/vibe-coding-kit/cb387af342e6a001b33ee514456ce2a54a92f72c/7819d75fd9da7233.json](../../../wiki/dossiers/junliu1066/vibe-coding-kit/cb387af342e6a001b33ee514456ce2a54a92f72c/7819d75fd9da7233.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] A three-layer governance system is described: CLAUDE.md as auto-loaded constitution, a harness skill for post-hoc artifact validation, and per-SKILL.md pre-delivery checklists, all derived from a root harness.json config. -- evidence: [README.md#L66-L66](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L66-L66), [README.md#L68-L72](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L68-L72), [README.md#L74-L74](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L74-L74) (`clm_3591358bdd82f847a58fcbcb18935f6e0dfc606d4025bbe0407d44f8369a719f`)
- [observation/documented] A worked example project (FileMaster, a Flutter desktop file organizer) demonstrates the kit's outputs: project spec, tech-stack decision table, directory tree, security checklist, deployment steps, and acceptance checklist. -- evidence: [docs/项目说明书.md#L7-L10](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L7-L10), [docs/项目说明书.md#L88-L93](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L88-L93), [docs/项目说明书.md#L96-L104](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L96-L104), [docs/项目说明书.md#L4-L4](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L4-L4), [docs/项目说明书.md#L27-L66](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L27-L66), [docs/项目说明书.md#L17-L24](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L17-L24), [docs/项目说明书.md#L76-L85](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E%E4%B9%A6.md#L76-L85) (`clm_b3f1daf8e6bbd68b753bcb277efaa48d6a1469b1112ff866b8803c2dab76ac2a`)

## design-choices (2 claim(s))

- [observation/documented] harness.json is the single source of truth from which CLAUDE.md, the harness skill, and SKILL.md checklists are derived, so editing one place keeps the three layers in sync. -- evidence: [docs/Harness-v2-重设计方案.md#L214-L219](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L214-L219), [docs/Harness-v2-重设计方案.md#L221-L221](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L221-L221), [README.md#L74-L74](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L74-L74) (`clm_56c8f3ce8999e7883dab8ceb9e6cc47b05d3486727e7bf5f41ef6ac6d7db479e`)
- [observation/documented] A triage step (S1.1) classifies needs as light or heavy: light/demo mode merges gate confirmations into groups and skips optional steps with a ledger note, while exit gates always apply; heavy mode confirms each step individually. -- evidence: [docs/Harness-v2-重设计方案.md#L246-L246](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L246-L246), [docs/Harness-v2-重设计方案.md#L257-L257](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L257-L257), [docs/Harness-v2-重设计方案.md#L248-L255](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L248-L255) (`clm_bff7687b8f21c5b6d86497a1b103a393cbf564ec2d77c8e137df75b1b1b8ebde`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions via Issue and PR are welcomed, with requested style of plain language, stating costs, and avoiding complexity. -- evidence: [README.md#L169-L169](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L169-L169) (`clm_1974d039e9b1fa7f25478ecb9c7428fa87fd60cd0137cde7f00f42830bae539d`)

## skills-patterns (1 claim(s))

- [observation/documented] The kit ships six skills (prd, requirements, architecture, production, survival, harness), each a folder with a SKILL.md in a generic skill format, intended to trigger automatically when needed. -- evidence: [README.md#L53-L60](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L53-L60), [README.md#L51-L51](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L51-L51), [README.md#L102-L102](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L102-L102) (`clm_618651a901534b876b287f0590086076e9c334194843dcda2a816ab195c31007`)

## interfaces (1 claim(s))

- [observation/documented] Usage paths documented: paste a SKILL.md into any chat (Claude/ChatGPT/Codex), upload a skill folder to claude.ai settings, or copy folders into ~/.claude/skills/ for Claude Code auto-triggering. -- evidence: [README.md#L136-L136](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L136-L136), [README.md#L118-L121](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L118-L121), [README.md#L132-L132](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L132-L132), [README.md#L108-L110](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L108-L110) (`clm_1612c38b10873705cd879a8d57110042cfa21f9ec639491cb166db177fb2278f`)

## memory-state (1 claim(s))

- [observation/documented] Process state lives in docs/进度账本.md, which the AI must read at the start of each turn and update after each gate; a .dsu/progress/ card system (index, module, task files) handles development-context recovery. -- evidence: [README.md#L78-L78](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L78-L78), [docs/进度账本.md#L3-L3](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/%E8%BF%9B%E5%BA%A6%E8%B4%A6%E6%9C%AC.md#L3-L3), [README.md#L76-L76](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L76-L76), [docs/Harness-v2-重设计方案.md#L35-L35](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L35-L35), [docs/Harness-v2-重设计方案.md#L39-L41](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L39-L41) (`clm_4e9b57bb63a41f3280ffc01130e169fa6e7ad874d294302a7aee516981a218ec`)

## orchestration (1 claim(s))

- [observation/documented] The harness.json workflow block defines an ordered S1 requirements → S2 architecture → S3 launch pipeline with entry/exit gates, per-step exit conditions, and rules that skipped steps must be recorded in the ledger. -- evidence: [docs/Harness-v2-重设计方案.md#L84-L84](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L84-L84), [README.md#L76-L76](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L76-L76), [docs/Harness-v2-重设计方案.md#L86-L153](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L86-L153) (`clm_abb45277b201e88ee5e1fff573d7d7a2f49dc961d576effac7bc9396e83ce8ae`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The v2 redesign doc records that only batches 1-2 are done (workflow block, ledger template, prd skill pilot); extending to the other four skills, harness process audit, and end-to-end validation remain unchecked. -- evidence: [docs/Harness-v2-重设计方案.md#L263-L267](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/docs/Harness-v2-%E9%87%8D%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88.md#L263-L267) (`clm_cba5d1cb47488cb1f9d11d498dfaab322b6fd6a3e4783ff57c08040333bbf20b`)

## relevance (1 claim(s))

- [observation/documented] The kit targets non-coders or beginners (PMs, founders, indie developers) who build products via AI, aiming to teach requirements clarity and discipline rather than coding. -- evidence: [README.md#L163-L165](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L163-L165), [README.md#L22-L22](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L22-L22), [README.md#L9-L9](https://github.com/Junliu1066/vibe-coding-kit/blob/cb387af342e6a001b33ee514456ce2a54a92f72c/README.md#L9-L9) (`clm_174893598bfa0d8a6ac24e3d857bdd22542c7782ba5bc625f13d635a63afccac`)

