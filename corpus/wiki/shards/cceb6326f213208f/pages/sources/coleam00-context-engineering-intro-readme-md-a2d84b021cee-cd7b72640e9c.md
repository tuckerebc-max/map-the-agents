---
access: public
aliases: []
claim_ids:
- clm_01cde71315c5786f9cc38c2179754e84a7f3050de3f0084236847c83267d4d2e
- clm_1028e4fd45bf9a6aef86cff52d0800b238449ee229e3e5e84d5d2a57fe291069
- clm_284aba45a62cf86086eaeb918fba55850f15690162052996d11916f8b7fbe600
- clm_345b3e681017ff9985bcc4bc40c489b3ff055ccd5867781f818e3ebd159dec47
- clm_81386967363afd72d458ae2f37681a1fd019adc10495df94f1265e749eb58272
- clm_bd9658e039571d2d7b5a9c353750502d92b1aba4b9e2924ef6e729c6838cd010
- clm_c42238bc3d90497cb4016cca0da178b5da8fe909c1a62a25a974a50fbbd151dd
- clm_d688749afa8c5aa51f96ab47ca90b5b6f12daa18d776b94b04f361e9f443f7e4
- clm_eb7cfcf7207a26b6543a2a305f2c9d854edb4c918cc8f1ca3b56e93ad8046b39
maturity: draft
page_id: pg_0e5fd779685e53a9bc4bcd7b72640e9c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_677ae73c9785588a80fc13ccdedc7b37
title: coleam00/context-engineering-intro/README.md @ a2d84b021cee
updated_at: '2026-09-14T03:41:48Z'
---

# coleam00/context-engineering-intro/README.md @ a2d84b021cee

<!-- rcw:begin owner=source:src_677ae73c9785588a80fc13ccdedc7b37 block=evidence -->
- The template ships .claude/commands files (generate-prp.md, execute-prp.md), a PRPs folder with a base template and an example PRP, an examples/ folder, CLAUDE.md, INITIAL.md, and INITIAL_EXAMPLE.md. [@claim:clm_01cde71315c5786f9cc38c2179754e84a7f3050de3f0084236847c83267d4d2e]
- The slash commands use a $ARGUMENTS variable that receives whatever the user passes after the command name, such as INITIAL.md or a PRP path. [@claim:clm_1028e4fd45bf9a6aef86cff52d0800b238449ee229e3e5e84d5d2a57fe291069]
- The examples/ folder is treated as critical to the method's success, with the README advising users to include code-structure, testing, integration, and CLI patterns for the AI to mimic. [@claim:clm_284aba45a62cf86086eaeb918fba55850f15690162052996d11916f8b7fbe600]
- The template deliberately excludes RAG and tooling aspects of context engineering, which the author says are planned for future work. [@claim:clm_345b3e681017ff9985bcc4bc40c489b3ff055ccd5867781f818e3ebd159dec47]
- Two custom Claude Code slash commands are exposed: /generate-prp, which takes a feature-request file, and /execute-prp, which takes a generated PRP file path. [@claim:clm_81386967363afd72d458ae2f37681a1fd019adc10495df94f1265e749eb58272]
- Repository development practice: the generate-prp command is documented to research codebase patterns, gather documentation, create a blueprint with validation gates, and score its own confidence from 1 to 10. [@claim:clm_bd9658e039571d2d7b5a9c353750502d92b1aba4b9e2924ef6e729c6838cd010]
- Repository development practice: the execute-prp flow is documented as loading the PRP, planning tasks with TodoWrite, implementing components, running tests and linting, and iterating on failures. [@claim:clm_c42238bc3d90497cb4016cca0da178b5da8fe909c1a62a25a974a50fbbd151dd]
- The evidence consists only of README, CLAUDE.md, and INITIAL template files; no implementation code for the slash commands' behavior appears in the provided slices, so their described steps appear to be documentation rather than inspected code. [@claim:clm_d688749afa8c5aa51f96ab47ca90b5b6f12daa18d776b94b04f361e9f443f7e4]
- The approach centers on PRPs (Product Requirements Prompts), described as comprehensive implementation blueprints with context, validation steps, error-handling patterns, and test requirements, tailored for AI coding assistants. [@claim:clm_eb7cfcf7207a26b6543a2a305f2c9d854edb4c918cc8f1ca3b56e93ad8046b39]
<!-- rcw:end owner=source:src_677ae73c9785588a80fc13ccdedc7b37 block=evidence -->

## Researcher notes

