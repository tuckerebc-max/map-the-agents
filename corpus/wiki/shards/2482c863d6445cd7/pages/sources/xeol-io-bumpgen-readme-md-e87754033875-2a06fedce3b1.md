---
access: public
aliases: []
claim_ids:
- clm_0671b268d93ea651a0a351e525bc4695b9a04cc12412b557fc0d66af3e12757a
- clm_067cbf8536c1bb049b1ef5affd32f37cc54f39af436b1cf3d3dab38b70fff627
- clm_24adb78441e4d943d442e45b9ee6d41cfd161b2e80cc65dbf5325f1b679411cc
- clm_500ceac0eecbdb80ead5f18294a98f8e11d857a8a07d5858732f03a2c22f8cfc
- clm_7b28559f3a71e2ab0fee914ae754d3ca73f2453c56933e9b029a720f1c82631a
- clm_801a07e51f0af58a4857e24a99b6f6372bd7cad91779bc1304c0e6ce2b78ff50
- clm_85cdd73eaaa0530f55fc31a2eb585b3ee0300af95e1d7666da8bcbd777284885
- clm_a10ec0d61ea6394c831623a41ed8424b1491431675edc570712caae38325f4a0
- clm_bdb5b21184d1a2b4e1c5ffe4819fd0ea82a70716ed3144b885d8470837a864ec
- clm_ccd43d9f1943141113d18c83d92287cad6bb0477e372f2d419de896beb673ec3
- clm_d93adaef855c9fe4ac22f3e91846228d9666f035ec05f1c1bc0040f410905235
- clm_dcdd4b5e64d3c0f445f526367a3ebde2bb42740cbd6965f90c16eddfd3ee6eba
maturity: draft
page_id: pg_5fe2eba3b1815bb5b59f2a06fedce3b1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9df2608b0b37581a8723947d9355ae4e
title: xeol-io/bumpgen/README.md @ e87754033875
updated_at: '2026-09-14T03:24:52Z'
---

# xeol-io/bumpgen/README.md @ e87754033875

<!-- rcw:begin owner=source:src_9df2608b0b37581a8723947d9355ae4e block=evidence -->
- Repository development practice: contributions are welcome and setup for development is documented in .github/development.md. [@claim:clm_0671b268d93ea651a0a351e525bc4695b9a04cc12412b557fc0d66af3e12757a]
- The tool builds the project to detect what broke after a dependency bump, then uses ts-morph to build an AST of the code and obtain type definitions for external methods. [@claim:clm_067cbf8536c1bb049b1ef5affd32f37cc54f39af436b1cf3d3dab38b70fff627]
- bumpgen relies on build errors, so behavioral changes that don't produce build errors go undetected. [@claim:clm_24adb78441e4d943d442e45b9ee6d41cfd161b2e80cc65dbf5325f1b679411cc]
- The plan graph, the error, and the file containing the breaking change are passed to the LLM as context to maximize its ability to fix the issue. [@claim:clm_500ceac0eecbdb80ead5f18294a98f8e11d857a8a07d5858732f03a2c22f8cfc]
- bumpgen requires an OpenAI API key and only supports the gpt-4-turbo-preview model at this time. [@claim:clm_7b28559f3a71e2ab0fee914ae754d3ca73f2453c56933e9b029a720f1c82631a]
- bumpgen creates a plan-graph DAG, based on Microsoft's codeplan paper, to execute changes in order and propagate fixes for second-order breakages across the codebase. [@claim:clm_801a07e51f0af58a4857e24a99b6f6372bd7cad91779bc1304c0e6ce2b78ff50]
- bumpgen upgrades TypeScript/TSX dependencies and makes code changes automatically when the upgrade breaks things. [@claim:clm_85cdd73eaaa0530f55fc31a2eb585b3ee0300af95e1d7666da8bcbd777284885]
- The CLI accepts a package name and target version (e.g. bumpgen @tanstack/react-query 5.28.14), can be run without arguments to pick a package from a menu, and offers --help for options. [@claim:clm_a10ec0d61ea6394c831623a41ed8424b1491431675edc570712caae38325f4a0]
- bumpgen cannot handle multiple packages at once, failing on upgrades needing simultaneous peer-dependency updates, and struggles with very large framework upgrades like vue 2 to 3. [@claim:clm_bdb5b21184d1a2b4e1c5ffe4819fd0ea82a70716ed3144b885d8470837a864ec]
- The example GitHub workflow grants pull-requests:read and contents:write permissions and passes path, llm_key, and github_token inputs to the bumpgen action. [@claim:clm_ccd43d9f1943141113d18c83d92287cad6bb0477e372f2d419de896beb673ec3]
- A GitHub action runs bumpgen, intended to trigger on dependabot or renovatebot PRs, committing fixes to the PR branch when breaking changes are detected. [@claim:clm_d93adaef855c9fe4ac22f3e91846228d9666f035ec05f1c1bc0040f410905235]
- bumpgen with GPT-4 Turbo scored 45% (67 tasks) on a benchmark suite of version bumps with breaking changes (swe-bump-bench), with evals published in that repo. [@claim:clm_dcdd4b5e64d3c0f445f526367a3ebde2bb42740cbd6965f90c16eddfd3ee6eba]
<!-- rcw:end owner=source:src_9df2608b0b37581a8723947d9355ae4e block=evidence -->

## Researcher notes

