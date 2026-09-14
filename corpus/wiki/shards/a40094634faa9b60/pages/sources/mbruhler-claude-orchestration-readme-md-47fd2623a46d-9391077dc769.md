---
access: public
aliases: []
claim_ids:
- clm_079e3646521017641b39e66358a915001837ddc1ee35b9dde2621cf1fccad4bb
- clm_0d6d783dca5afa1710d2c51d669b192efdc51434fca625a1a8f191e31cbf81d1
- clm_2e1faf4ffc3e8345e474523dd32e541e026c337713bf604481962521b76334f5
- clm_3d7aa7afabe036838c49e94856a63101894330ded9547d917a9d19e3e38bc9fa
- clm_5dbbdc0ad07e4cfe30a4defce918d10226e220c92f47feb4bf2d67df9cb53319
- clm_7bf7c2b0cad253cef1eddb093b655d65cc11fd9ad3443f541ffda28bfc82fa55
- clm_be101a1b4d5a32b23b291fb6d0560fcd73fb56b79720ae60c8ba707afbfe690d
- clm_dc90ac4955f0ca3fe96421ac0597bb7f04bc4b7643ad458d06b01eb0241f3883
maturity: draft
page_id: pg_590d97c4374b5468bb0f9391077dc769
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f235b70a9dc0506b809f95ed9403356b
title: mbruhler/claude-orchestration/README.md @ 47fd2623a46d
updated_at: '2026-09-14T05:00:53Z'
---

# mbruhler/claude-orchestration/README.md @ 47fd2623a46d

<!-- rcw:begin owner=source:src_f235b70a9dc0506b809f95ed9403356b block=evidence -->
- Documentation states the plugin is installed by adding a marketplace to Claude Code and installing it from the plugin menu, then verified by checking for orchestration slash commands such as /orchestration:menu and /orchestration:init. [@claim:clm_079e3646521017641b39e66358a915001837ddc1ee35b9dde2621cf1fccad4bb]
- The README describes this as a Claude Code plugin for multi-agent workflow orchestration, comparing it to N8N in Claude Code, that chains AI agents to automate complex tasks using natural language or a declarative flow syntax. [@claim:clm_0d6d783dca5afa1710d2c51d669b192efdc51434fca625a1a8f191e31cbf81d1]
- Documentation describes the project's own layout: auto-activating skills for creating, executing, and debugging workflows, a permanent agents/ directory, an auto-cleaned temp-agents/ directory, generated temp-scripts/, and example .flow templates. [@claim:clm_2e1faf4ffc3e8345e474523dd32e541e026c337713bf604481962521b76334f5]
- Documentation describes a semantic routing step that sends a captured variable through an LLM-evaluated condition tree to select which branch of agents runs next, in place of fixed text-matching conditions. [@claim:clm_3d7aa7afabe036838c49e94856a63101894330ded9547d917a9d19e3e38bc9fa]
- Documentation states failed or interrupted workflows are recoverable: node and variable state is saved automatically to a state file, and resuming a workflow reloads that state, skips completed steps, and continues from the point of failure. [@claim:clm_5dbbdc0ad07e4cfe30a4defce918d10226e220c92f47feb4bf2d67df9cb53319]
- The README documents that workflows can run standalone and headless outside interactive Claude Code, invoked as a claude -p command against a flow file, with an option to request JSON-formatted output. [@claim:clm_7bf7c2b0cad253cef1eddb093b655d65cc11fd9ad3443f541ffda28bfc82fa55]
- The README documents a flow syntax with sequential (->), parallel (||), and conditional (~>) operators, checkpoint labels (@label), variable capture (:var) and interpolation ({var}), and temporary-agent declaration ($agent). [@claim:clm_be101a1b4d5a32b23b291fb6d0560fcd73fb56b79720ae60c8ba707afbfe690d]
- The README describes checkpoint directives such as @review that pause a workflow for human approval, with documented fallback behaviors - skip, or log to a file instead of blocking - for unattended, scheduled runs where no one can approve interactively. [@claim:clm_dc90ac4955f0ca3fe96421ac0597bb7f04bc4b7643ad458d06b01eb0241f3883]
<!-- rcw:end owner=source:src_f235b70a9dc0506b809f95ed9403356b block=evidence -->

## Researcher notes

