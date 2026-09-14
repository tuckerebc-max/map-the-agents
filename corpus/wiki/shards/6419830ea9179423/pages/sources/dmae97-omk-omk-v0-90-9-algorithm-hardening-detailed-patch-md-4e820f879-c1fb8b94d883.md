---
access: public
aliases: []
claim_ids:
- clm_0859292a9d1605c39511857d95d3e84ee43438bb849c24af04821f1d9fef28e1
- clm_1245a5771a276023deebf5ef97c078085c65053a470525938ff3b1eb7389d57a
- clm_1d3485a52a1a6a798a06d10845894129936f1c6d6504ff4f1deda02f12ad1a36
- clm_5f183e0a5e4b487d902413a3601a9eda8dba391d25c7923010f80c6651ecaa1c
- clm_8fd7762e9bc932b52183b1c2ad7baaf23ca0ee47ee359d68f34345ccb25e6075
- clm_e31c9aafda0fb46551d24a8d21983711be7e1552d47ae7c28f3bdb56dbe6771a
- clm_e44b4c5230ddfcefd4167b2ad36e7fef8185b04a73154162cb52543bab3f12ca
- clm_eba337909e5e4762ce0026e3cb90511d36907a4b4c1fd358e16c2c3ce48f61e0
- clm_f13b6d368aeefd54a0fb803d4300ae3e8a280efeb9a3bf48e958ad5cde6cab31
- clm_f87fb44387e59c1e78a89c5e22cb753b06881fd468a0f786bbe48949e94cc514
maturity: draft
page_id: pg_a57fb15b48e15f42811ec1fb8b94d883
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_afa0fa5d99065b0890b8f65785bb6c86
title: dmae97/omk/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md @ 4e820f879503
updated_at: '2026-09-14T03:48:13Z'
---

# dmae97/omk/OMK_v0.90.9_ALGORITHM_HARDENING_DETAILED_PATCH.md @ 4e820f879503

<!-- rcw:begin owner=source:src_afa0fa5d99065b0890b8f65785bb6c86 block=evidence -->
- The v0.90.9 hardening document is an implementation-ready plan kept as a plan, not evidence that code was applied; the package version was 0.90.8 when written and 0.91.0 in the later snapshot. [@claim:clm_0859292a9d1605c39511857d95d3e84ee43438bb849c24af04821f1d9fef28e1]
- The contiguous wave scheduler is safe but causes head-of-line blocking: one earlier conflict delays later independent calls, and path comparison does not detect symlink, hardlink, realpath, or Windows drive/UNC identity aliases. [@claim:clm_1245a5771a276023deebf5ef97c078085c65053a470525938ff3b1eb7389d57a]
- ALG-003 is reported complete (15/15) as of 2026-07-23, including a Git workspace fingerprint (head plus dirty-diff digest), post-receipt latest-mutation evidence invalidation, and command-string secret redaction with a secure command hash. [@claim:clm_1d3485a52a1a6a798a06d10845894129936f1c6d6504ff4f1deda02f12ad1a36]
- The current continuation guard only checks whether the last message is an assistant message containing tool calls, so a transcript ending in a toolResult can pass while earlier calls remain unresolved. [@claim:clm_5f183e0a5e4b487d902413a3601a9eda8dba391d25c7923010f80c6651ecaa1c]
- Only the CI callsite is wired to the receipt executor: ci.yml invokes dist/verify-ci.js, which runs release-consistency commands via executeVerifiedLocalBash with executor 'ci-runner'; CLI, interactive, RPC, and AgentSession bash paths remain unconnected. [@claim:clm_8fd7762e9bc932b52183b1c2ad7baaf23ca0ee47ee359d68f34345ccb25e6075]
- Repository development practice: the 2026-07-23 snapshot's verification evidence is limited to focused tests (112/112) and 'npm run check' exit 0; it explicitly does not claim full builds, ./test.sh, ./omk-test.sh, npm pack, or platform smoke results. [@claim:clm_e31c9aafda0fb46551d24a8d21983711be7e1552d47ae7c28f3bdb56dbe6771a]
- The evidence gate currently verifies metadata presence (status, hash, verification command) rather than proving a command actually ran, its exit code, the workspace revision, or that artifacts stayed unchanged after execution. [@claim:clm_e44b4c5230ddfcefd4167b2ad36e7fef8185b04a73154162cb52543bab3f12ca]
- Per the patch analysis, aborting during sequential or wave tool execution can leave later tool calls in the transcript without matching tool results, since the loop breaks and returns only completed results. [@claim:clm_eba337909e5e4762ce0026e3cb90511d36907a4b4c1fd358e16c2c3ce48f61e0]
- The planned ALG-001 invariant requires every assistant tool call to have exactly one terminal result with a disposition of completed, failed, blocked, aborted, timeout, or skipped, with synthetic results for never-started calls. [@claim:clm_f13b6d368aeefd54a0fb803d4300ae3e8a280efeb9a3bf48e958ad5cde6cab31]
- OMK runs with the invoking user's process privileges, so its scheduler and evidence gate are explicitly not security boundaries; strong isolation is delegated to containers, micro-VMs, or sandboxes. [@claim:clm_f87fb44387e59c1e78a89c5e22cb753b06881fd468a0f786bbe48949e94cc514]
<!-- rcw:end owner=source:src_afa0fa5d99065b0890b8f65785bb6c86 block=evidence -->

## Researcher notes

