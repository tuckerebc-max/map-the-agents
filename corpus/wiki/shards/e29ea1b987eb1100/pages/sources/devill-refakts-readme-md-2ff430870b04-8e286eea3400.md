---
access: public
aliases: []
claim_ids:
- clm_02bc5fbfa7cb44aebd774540a3a09d3cfc0c43b5c3c0c0e83116eddb303ccf35
- clm_229e6ca4f6bf0ead48ea971b912c24650e8dc180037be8af1d379ddbe3a366b4
- clm_49a7ab7047c752bac63c825d7803ef6bc010854518a7bcfce9b6b84016f99058
- clm_6b671edf2be68ad3614e9601412c80870975d15e5bf08ce19fe5ea092aa9cb0f
- clm_7598f12684d23327c3b60a57022f96186e6869909dad63ff3c4a7d9604ebc57e
- clm_77150e6643c5ad48dfd7f28de9c8253a05afb12c10d43af4fd51fc5b3b6769d5
- clm_8068648ab0810c879b3438f28542e2ecdcefa7424968b2168637ddbc8365af05
- clm_8ec2b73f4db1b63018039ccf43c79e1df2d8294dcd9f5eb2c73d82d04aecfe19
- clm_ca1c355f024b7f3e90d3806a36c822765b5dbf32cb8c117af4b2ab0957c274ed
- clm_d9e58cfff72b4e4ead069fbc96b63d0d73132f2665c3c68a931efe744cc64bd4
- clm_e4ddb0d3756605404e91b2eb8237ffdaf35b0076762831a19d275b1d807f8609
- clm_ed1f2771b29ebfa83dc3074d4d40dd5e0040e9839bfeabd2d3bea266bbdb2ca0
maturity: draft
page_id: pg_a0d6aefdb6e958f083a58e286eea3400
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e607df5f05fa5b09b066c4070d7755a1
title: devill/refakts/README.md @ 2ff430870b04
updated_at: '2026-09-14T03:47:03Z'
---

# devill/refakts/README.md @ 2ff430870b04

<!-- rcw:begin owner=source:src_e607df5f05fa5b09b066c4070d7755a1 block=evidence -->
- Licensing is PolyForm Noncommercial 1.0.0: free for non-commercial use while businesses require a license, with fees distributed among contributors at project leads' discretion. [@claim:clm_02bc5fbfa7cb44aebd774540a3a09d3cfc0c43b5c3c0c0e83116eddb303ccf35]
- move-file updates import references across the codebase, and find-usages locates symbol usages across files. [@claim:clm_229e6ca4f6bf0ead48ea971b912c24650e8dc180037be8af1d379ddbe3a366b4]
- The design goal is surgical edits: instead of regenerating whole files, operations change only the targeted code and its references, saving tokens and preserving agent cognitive capacity. [@claim:clm_49a7ab7047c752bac63c825d7803ef6bc010854518a7bcfce9b6b84016f99058]
- Repository development practice: the repo is optimized for Claude Code; contributors are told to have Claude set up pre/post commit hooks, pick a 'good first issue', assign it to themselves, and can direct work by issue number. [@claim:clm_6b671edf2be68ad3614e9601412c80870975d15e5bf08ce19fe5ea092aa9cb0f]
- The tool uses ts-morph for AST manipulation and @phenomnomnominal/tsquery for node selection, and is built with TypeScript. [@claim:clm_7598f12684d23327c3b60a57022f96186e6869909dad63ff3c4a7d9604ebc57e]
- The package is installed globally via npm as 'refakts'. [@claim:clm_77150e6643c5ad48dfd7f28de9c8253a05afb12c10d43af4fd51fc5b3b6769d5]
- Repository development practice: tests are fixture-based under tests/fixtures with .input.ts, .expected.ts, and .expected.txt files per command, and npm run test:coverage checks for uncovered use cases. [@claim:clm_8068648ab0810c879b3438f28542e2ecdcefa7424968b2168637ddbc8365af05]
- The select command supports regex, range, structural, and boundary modes, e.g. --range with start/end regexes and --boundaries "function". [@claim:clm_8ec2b73f4db1b63018039ccf43c79e1df2d8294dcd9f5eb2c73d82d04aecfe19]
- RefakTS is a command-line tool exposing commands including extract-variable, inline-variable, rename, select, sort-methods, find-usages, and move-file. [@claim:clm_ca1c355f024b7f3e90d3806a36c822765b5dbf32cb8c117af4b2ab0957c274ed]
- Repository development practice: post-commit hooks scan for quality issues (oversized functions, unused methods, comments, duplication, large changes) and automatically prompt the AI agent with corrective guidance. [@claim:clm_d9e58cfff72b4e4ead069fbc96b63d0d73132f2665c3c68a931efe744cc64bd4]
- The project targets AI agents making multi-location code changes (renames, extractions) and is positioned as built by AI agents for AI agents, with a roadmap managed by Claude instances. [@claim:clm_e4ddb0d3756605404e91b2eb8237ffdaf35b0076762831a19d275b1d807f8609]
- The project is explicitly labeled a proof of concept demonstrating the core concept with basic refactoring operations, with more commands in development. [@claim:clm_ed1f2771b29ebfa83dc3074d4d40dd5e0040e9839bfeabd2d3bea266bbdb2ca0]
<!-- rcw:end owner=source:src_e607df5f05fa5b09b066c4070d7755a1 block=evidence -->

## Researcher notes

