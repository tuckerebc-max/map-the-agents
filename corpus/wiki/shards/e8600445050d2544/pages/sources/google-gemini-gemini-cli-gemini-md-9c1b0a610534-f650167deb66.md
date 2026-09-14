---
access: public
aliases: []
claim_ids:
- clm_24a467f8475aec0c19157464f21de1fe4a271062760bc935db5b687281bd899c
- clm_24f52035b123cf9b108c200bbb4cd59727796633d821cccc53de7b149ccad2ad
- clm_2c93bcd2fda4a0dafab6a5dfa2ae0e423f2567dc9709c01aab7e54135fee4ebb
- clm_a92d62d09cdca7dcdda48591d72342e5f5200b848c49ebc12c1fd107742cec60
maturity: draft
page_id: pg_2c8ad6e5579f53e2b92ff650167deb66
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d41cbdc5e7065844912accafccc1fc17
title: google-gemini/gemini-cli/GEMINI.md @ 9c1b0a610534
updated_at: '2026-09-14T02:01:21Z'
---

# google-gemini/gemini-cli/GEMINI.md @ 9c1b0a610534

<!-- rcw:begin owner=source:src_d41cbdc5e7065844912accafccc1fc17 block=evidence -->
- Repository development practice: PRs should be small and issue-linked, commits follow Conventional Commits, and new source files need Apache-2.0 license headers enforced by ESLint. [@claim:clm_24a467f8475aec0c19157464f21de1fe4a271062760bc935db5b687281bd899c]
- The project uses Node.js (>=20), TypeScript, React with Ink for CLI rendering, Vitest, esbuild, ESLint, and Prettier, in an npm-workspaces monorepo. [@claim:clm_24f52035b123cf9b108c200bbb4cd59727796633d821cccc53de7b149ccad2ad]
- Repository development practice: tests depending on environment variables should use vi.stubEnv in beforeEach and vi.unstubAllEnvs in afterEach rather than mutating process.env directly. [@claim:clm_2c93bcd2fda4a0dafab6a5dfa2ae0e423f2567dc9709c01aab7e54135fee4ebb]
- Repository development practice: contributors run npm run test for unit tests, test:e2e for integration, and preflight (clean, install, build, lint, type check, tests) before submitting PRs. [@claim:clm_a92d62d09cdca7dcdda48591d72342e5f5200b848c49ebc12c1fd107742cec60]
<!-- rcw:end owner=source:src_d41cbdc5e7065844912accafccc1fc17 block=evidence -->

## Researcher notes

