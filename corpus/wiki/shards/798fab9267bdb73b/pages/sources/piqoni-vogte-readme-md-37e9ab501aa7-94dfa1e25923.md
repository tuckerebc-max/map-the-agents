---
access: public
aliases: []
claim_ids:
- clm_0fefc8983a25da6b8a888303adff7fa5910a0ab91bf6fd36670a728a0a79050b
- clm_1ab4ecd604cbb29ae58e316da0b3611ce9d184f0fffd0e7667ea46eb1b04b79e
- clm_27ec768133466b800cbb7e200de2985e57d61ccea8d9be4c505d5c466a0bb13b
- clm_4b17e5d9ba469efa89c3e27ce21ed9e50d8c3a4d6305961ad18a846e27f87c93
- clm_7e5d6ac3be06728a0e2d444a78812ac28fa9f123381d51eb26d69a8eec4358bd
- clm_8f989390f23016d3adbf3de8a2799ba83d9138a9c74cdf28d00c413c83a841b0
- clm_ab954c665c09aeacbdda48e27808afc9fdaa6d9a022fbc1237eb1c0ce56af530
- clm_b15b3a0acc12cfb42cd406210c022500552442ab28ae63bb377666e6e94740a1
- clm_b92079fc233fee9e64deafadc83644f693358bd05878d83d92bda697ca0c43ee
- clm_c8105f4f84e272cd463128a7920be5169e0abf5915b10566cfdb252b4ddde941
- clm_df6d86b6ac9992c779e04358c3d92ade1a62c15f15f0c80684f9a29a0250e8ef
- clm_f3718b27617026f67795f182acf1b56d516be18b29935004a2fbcdd672b7eec9
maturity: draft
page_id: pg_19359ea980515b6aac7094dfa1e25923
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eef05b8e4d5851b887c4bc5c5748b2fb
title: piqoni/vogte/README.md @ 37e9ab501aa7
updated_at: '2026-09-14T02:31:10Z'
---

# piqoni/vogte/README.md @ 37e9ab501aa7

<!-- rcw:begin owner=source:src_eef05b8e4d5851b887c4bc5c5748b2fb block=evidence -->
- The tool offers a TUI with ask/agent modes and CLI flags including -review, -generate-context, -agent, -config, -dir, and -model. [@claim:clm_0fefc8983a25da6b8a888303adff7fa5910a0ab91bf6fd36670a728a0a79050b]
- Patch application is currently line-based; an AST-based patching approach is still being explored, and agent-mode patching is described as rough around the edges. [@claim:clm_1ab4ecd604cbb29ae58e316da0b3611ce9d184f0fffd0e7667ea46eb1b04b79e]
- Running 'vogte -generate-context' writes a vogte-context.txt file in the current directory, and -dir lets users analyze a project in another directory. [@claim:clm_27ec768133466b800cbb7e200de2985e57d61ccea8d9be4c505d5c466a0bb13b]
- The -review flag appears to perform a local LLM review of uncommitted changes against a base branch (default main), optionally accepting a change description message. [@claim:clm_4b17e5d9ba469efa89c3e27ce21ed9e50d8c3a4d6305961ad18a846e27f87c93]
- Vogte is described as an agentic terminal tool aimed at existing Go codebases, helping developers build and maintain Go projects with LLMs. [@claim:clm_7e5d6ac3be06728a0e2d444a78812ac28fa9f123381d51eb26d69a8eec4358bd]
- Installation is via 'go install github.com/piqoni/vogte@latest'; the TUI exits via Ctrl+C or typing q, quite, or exit. [@claim:clm_8f989390f23016d3adbf3de8a2799ba83d9138a9c74cdf28d00c413c83a841b0]
- Because the language is assumed to be Go, the tool parses repositories with Abstract Syntax Trees to extract compressed, relevant context for LLM prompts, aiming for near-zero configuration. [@claim:clm_ab954c665c09aeacbdda48e27808afc9fdaa6d9a022fbc1237eb1c0ce56af530]
- In agent mode (via -agent or the AGENT toggle) the tool edits files without user approval, and users are advised to rely on version control to avoid losing work. [@claim:clm_b15b3a0acc12cfb42cd406210c022500552442ab28ae63bb377666e6e94740a1]
- After applying patches, the tool runs a 'Sanity Check' (currently 'go vet ./...') and shows a project-health indicator for instant feedback. [@claim:clm_b92079fc233fee9e64deafadc83644f693358bd05878d83d92bda697ca0c43ee]
- Each message is treated as a new, unrelated chat, and there is no agentic retry loop on failure, at least for now. [@claim:clm_c8105f4f84e272cd463128a7920be5169e0abf5915b10566cfdb252b4ddde941]
- It works with OpenAI-compatible APIs (tested with GPT-4 and Claude Sonnet), supports AWS Bedrock for Anthropic models, and uses OPENAI_API_KEY or ANTHROPIC_API_KEY environment variables. [@claim:clm_df6d86b6ac9992c779e04358c3d92ade1a62c15f15f0c80684f9a29a0250e8ef]
- It uses a two-step flow: first it extracts structs/interfaces/methods signatures and asks the LLM which files are needed, then supplies those files in full so the LLM can produce a solution. [@claim:clm_f3718b27617026f67795f182acf1b56d516be18b29935004a2fbcdd672b7eec9]
<!-- rcw:end owner=source:src_eef05b8e4d5851b887c4bc5c5748b2fb block=evidence -->

## Researcher notes

