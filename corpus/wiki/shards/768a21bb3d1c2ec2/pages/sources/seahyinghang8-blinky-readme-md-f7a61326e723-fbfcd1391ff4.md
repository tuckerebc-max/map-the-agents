---
access: public
aliases: []
claim_ids:
- clm_15f43c903d653b129f56f4a02a9ee5952827e071ddd556b1cba005519723ebd7
- clm_328226f0af8ccfda90c12ccaeb893ce87a2776745045a97a973670284ea93a90
- clm_59ff641efd91253dcc379f47fc6f81d5fe1c4cdb64f57a276d2cbde14b011d72
- clm_5a7c12c7943199fb22a78cbdc84a60c4be2c6f1e93433af0b6795ea3c7c1bdb8
- clm_a11d6ee77adb30a487384e61082e83d0b9a7fe70455a7eb185dddcd4f7991ef1
- clm_a29924d99170325e657ef9af5318a11c3ec9511c269c47df4fdb26178b5d0901
- clm_aa1a420b81d9c99d83801da8151cc8bd845ab6828840275eb504061f4bb6f980
- clm_c03401602f3efe4b5aa47169866f5035af5ceaddf90de6b21d7e78c692774bdb
- clm_c2fe49222c3b6ed5e1a4707b0da0d2b100b9325ed80c67b4fcc4e8e57606f26e
- clm_cd6f3524cf536df7a18a2a209a6641189a90014a7245233c121ca8a8ae680647
- clm_d1dded2f06fbeabe0c4f01a6905c45a241f42f783043c2cf638cddcf0c116098
- clm_fdd4c468589c0f5e9eff42ce185abf525ac5033509b7bb3525336959c77e5bee
maturity: draft
page_id: pg_ae62d69374795ea5853dfbfcd1391ff4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c92c64d0ce785893ba7cdce2b3873d27
title: seahyinghang8/blinky/README.md @ f7a61326e723
updated_at: '2026-09-14T02:39:09Z'
---

# seahyinghang8/blinky/README.md @ f7a61326e723

<!-- rcw:begin owner=source:src_c92c64d0ce785893ba7cdce2b3873d27 block=evidence -->
- As of May 2024, per the README, SOTA LLMs struggle with large edits, motivating the match-and-replace editing approach; long builds are also cited as an unavoidable slowdown. [@claim:clm_15f43c903d653b129f56f4a02a9ee5952827e071ddd556b1cba005519723ebd7]
- Users can configure a custom 'Build Ready Text' pattern via Advanced Settings under Specify Repro Steps, used by the verifier to detect when a build step completes. [@claim:clm_328226f0af8ccfda90c12ccaeb893ce87a2776745045a97a973670284ea93a90]
- File editing uses a match-and-replace technique where the agent regenerates the original text with line numbers, which the README says helps catch hallucinations and bad indentation. [@claim:clm_59ff641efd91253dcc379f47fc6f81d5fe1c4cdb64f57a276d2cbde14b011d72]
- Users interact through a VSCode chat interface (ghost icon in the sidebar) where they describe the bug and optionally specify repro steps before starting the agent. [@claim:clm_5a7c12c7943199fb22a78cbdc84a60c4be2c6f1e93433af0b6795ea3c7c1bdb8]
- User feedback given while the agent runs is incorporated into its subsequent step, and after completion the user can accept or reject the proposed changes. [@claim:clm_a11d6ee77adb30a487384e61082e83d0b9a7fe70455a7eb185dddcd4f7991ef1]
- The agent's tool set includes LSP-based navigation tools GoToDefinition and GetAllReferences, plus GetFilesRelevantToEndpoint for navigating backend systems. [@claim:clm_a29924d99170325e657ef9af5318a11c3ec9511c269c47df4fdb26178b5d0901]
- The core agent loop was ported from SWE-agent, and the extension embeds it in VSCode so developers can give feedback mid-run. [@claim:clm_aa1a420b81d9c99d83801da8151cc8bd845ab6828840275eb504061f4bb6f980]
- Blinky is an open-source AI debugging agent for VSCode that uses LLMs to identify and fix backend code errors, inspired by SWE-agent. [@claim:clm_c03401602f3efe4b5aa47169866f5035af5ceaddf90de6b21d7e78c692774bdb]
- A Verify tool runs the user-specified repro steps; the agent iteratively debugs until the repro test passes and uses execution feedback from its print statements. [@claim:clm_c2fe49222c3b6ed5e1a4707b0da0d2b100b9325ed80c67b4fcc4e8e57606f26e]
- On first run the user is prompted for an OpenAI API key, which is stored locally in VSCode config for subsequent calls to OpenAI's server. [@claim:clm_cd6f3524cf536df7a18a2a209a6641189a90014a7245233c121ca8a8ae680647]
- Repository development practice: contributors can run `npm run install:all` and press F5 (Debug: Start Debugging) for local extension development, and prompts are edited in src/config/default.yaml before rebuilding. [@claim:clm_d1dded2f06fbeabe0c4f01a6905c45a241f42f783043c2cf638cddcf0c116098]
- The agent leverages the VSCode API, the Language Server Protocol, and print statement debugging to triangulate bugs in real-world backend systems. [@claim:clm_fdd4c468589c0f5e9eff42ce185abf525ac5033509b7bb3525336959c77e5bee]
<!-- rcw:end owner=source:src_c92c64d0ce785893ba7cdce2b3873d27 block=evidence -->

## Researcher notes

