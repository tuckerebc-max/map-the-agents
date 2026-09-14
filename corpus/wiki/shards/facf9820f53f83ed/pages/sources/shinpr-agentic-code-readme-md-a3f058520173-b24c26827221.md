---
access: public
aliases: []
claim_ids:
- clm_02f5fd2c253e825e0a8aa44d8a1b96febc49c05efaae643680fe09485b17989e
- clm_0b825dc8e3ed9bbf076d2fe22a1588f596b5baaf8223e691b1c703c0684f5a4e
- clm_1940a2f98617d0f6b71bd0a0ae9310b26ebb10fedeac57b20bdb6e9f35c5a7be
- clm_828fce4a09620854a69b2f42493983cf37b2e73f7cb02c9a1a142caab89be8df
- clm_940dff58a86bc5f6ae54f44aa4fe75d95ee06bd0a8ab380df4e5ee377f8452c5
- clm_a51b632c4c0307e4d78e93045120506aa215ebda0ac0a805e32ed4107a8792ce
- clm_b33a47b64c8836d7cfcedd04334edf1e0709f31a18c91aa990b6a9da9bb1dfa2
- clm_cf72b2dbd166de8a4b2adec7a290147922ff4675f9b97dd1991126d7e1a83d26
- clm_d325936df5b0a2204e2f97f3534c69b2d7ed42415d4d04f8db8c6a703cccfc20
- clm_d7273e45d6be4e3b40fa1d09d146ea6cee2a296c5d7239522b38575eff827689
- clm_da31861f806aa9555077f0478e224a7048ad3050780a9c5f08fa20b942433fac
- clm_ee74d541f0ff2c4eb3ed33185826a9450349a6549f9bcf7b77eac6bbd78662eb
maturity: draft
page_id: pg_035a61a4afe159a18e90b24c26827221
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cc7ad8ffcefc5c52a494a009f2725925
title: shinpr/agentic-code/README.md @ a3f058520173
updated_at: '2026-09-14T04:20:37Z'
---

# shinpr/agentic-code/README.md @ a3f058520173

<!-- rcw:begin owner=source:src_cc7ad8ffcefc5c52a494a009f2725925 block=evidence -->
- Work routing is based on decision burden rather than file count: Small work runs directly, Medium requires design and a work plan, Large requires a PRD with separate design decisions. [@claim:clm_02f5fd2c253e825e0a8aa44d8a1b96febc49c05efaae643680fe09485b17989e]
- Skills hold reusable judgment for coding, testing, documentation, implementation strategy, and metacognition, and are loaded only when a selected task needs them rather than at startup. [@claim:clm_0b825dc8e3ed9bbf076d2fe22a1588f596b5baaf8223e691b1c703c0684f5a4e]
- The workflow is strict about requirements, user authority, irreversible actions, accepted durable decisions, and completion evidence, while letting the agent resolve reversible repository-local choices itself. [@claim:clm_1940a2f98617d0f6b71bd0a0ae9310b26ebb10fedeac57b20bdb6e9f35c5a7be]
- The workflow targets tools that read repository-level AGENTS.md instructions, with Cursor, Codex CLI, and Gemini CLI cited as common examples, and exact discovery behavior depends on tool version. [@claim:clm_828fce4a09620854a69b2f42493983cf37b2e73f7cb02c9a1a142caab89be8df]
- The core is language-agnostic but TypeScript-specific references are included; other languages rely on repository-native commands until language-specific guidance is added. [@claim:clm_940dff58a86bc5f6ae54f44aa4fe75d95ee06bd0a8ab380df4e5ee377f8452c5]
- The framework adds process and context overhead, so direct agent execution is usually cheaper for well-scoped fixes, disposable experiments, or one-shot scripts with clear safe boundaries. [@claim:clm_a51b632c4c0307e4d78e93045120506aa215ebda0ac0a805e32ed4107a8792ce]
- The package ships an AGENTS.md entry point plus .agents directories for tasks, workflows, skills, and context-maps mapping tasks to skills. [@claim:clm_b33a47b64c8836d7cfcedd04334edf1e0709f31a18c91aa990b6a9da9bb1dfa2]
- Defined tasks include task-analysis, prd-creation, technical-design, acceptance-test-generation, work-planning, implementation, quality-assurance, code-review, technical-document-review, and integration-test-review, each owning one kind of result. [@claim:clm_cf72b2dbd166de8a4b2adec7a290147922ff4675f9b97dd1991126d7e1a83d26]
- A workflow file, .agents/workflows/agentic-coding.md, coordinates Medium/Large work across requirements, design, planning, implementation, QA, and review while preserving the approved outcome. [@claim:clm_d325936df5b0a2204e2f97f3534c69b2d7ed42415d4d04f8db8c6a703cccfc20]
- The tool requires Node.js 22 or later, per the Quick Start section. [@claim:clm_d7273e45d6be4e3b40fa1d09d146ea6cee2a296c5d7239522b38575eff827689]
- The skills subcommand installs only .agents/skills/ and does not install the full AGENTS.md workflow. [@claim:clm_da31861f806aa9555077f0478e224a7048ad3050780a9c5f08fa20b942433fac]
- The CLI is invoked as npx agentic-code with a project name to scaffold a repository, and a skills subcommand supporting --codex, --cursor, --project, and --path options. [@claim:clm_ee74d541f0ff2c4eb3ed33185826a9450349a6549f9bcf7b77eac6bbd78662eb]
<!-- rcw:end owner=source:src_cc7ad8ffcefc5c52a494a009f2725925 block=evidence -->

## Researcher notes

