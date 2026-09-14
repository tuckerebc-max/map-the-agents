---
access: public
aliases: []
claim_ids:
- clm_72df9db2574fecf503da4c8eeecbeab13b4e8233897038f6e2ea0329da49cb43
- clm_7d851ecef6911863daab06c55a31ba9fc467ce58a588135d3f7d21ef4eeda081
- clm_c81a7a0a69b6b8ddbde60ad0b128bd2e0590a879c01e815ef77971ad99e0e72a
- clm_f84177d489d5765cb0a35b244fdd9d23c13b735374a3618f73318232da4bbabc
maturity: draft
page_id: pg_d15c68da8cef58819550d0c515c39d5f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4f1df9a7ef9952c3a549d6c509aeeb49
title: codeflash-ai/codeflash/docs/index.mdx @ a3a38efc9ec3
updated_at: '2026-09-14T01:41:44Z'
---

# codeflash-ai/codeflash/docs/index.mdx @ a3a38efc9ec3

<!-- rcw:begin owner=source:src_4f1df9a7ef9952c3a549d6c509aeeb49 block=evidence -->
- The optimizer aims to find better algorithms, remove wasteful compute, and use caching or more efficient library methods, but does not modify the system architecture of the code it optimizes. [@claim:clm_72df9db2574fecf503da4c8eeecbeab13b4e8233897038f6e2ea0329da49cb43]
- The CLI supports optimizing a whole codebase with `codeflash --all`, a single script with `codeflash optimize myscript.py`, and per docs a single function via `codeflash --file path --function name`. [@claim:clm_7d851ecef6911863daab06c55a31ba9fc467ce58a588135d3f7d21ef4eeda081]
- Per docs, Codeflash also supports JavaScript/TypeScript (installed via npm/yarn/pnpm/bun, configured in package.json or codeflash.config.js) and Java (via uv, with Maven/Gradle and JUnit/TestNG support). [@claim:clm_c81a7a0a69b6b8ddbde60ad0b128bd2e0590a879c01e815ef77971ad99e0e72a]
- The product verifies optimization correctness by generating and running new regression tests alongside existing tests, and reports percentage speed increases and proofs of correctness in PR explanations. [@claim:clm_f84177d489d5765cb0a35b244fdd9d23c13b735374a3618f73318232da4bbabc]
<!-- rcw:end owner=source:src_4f1df9a7ef9952c3a549d6c509aeeb49 block=evidence -->

## Researcher notes

