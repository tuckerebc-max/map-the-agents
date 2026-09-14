---
access: public
aliases: []
claim_ids:
- clm_1de13b58669272bd4649e9379411f996a9fd33a9e646ac37cf4eec1f54402ec4
- clm_57b45cd9a6217209dfe2ce39625ddc8a5b19034e1ace0ffc1b015d4a9c2aa484
- clm_c42d55e89d7823ad82e8a520b89fc10ece52924e5c99f33138d2d74afe7cadc9
- clm_d9b249c073a96104d8ab56ccb5bf331eb06f0d958c13ef67240c5060498ad30a
- clm_e7746c93cde4593477bd3b969127e422c869351a8a81c0e267723c1c9878d026
- clm_ecb18d162b7f86cdc6bfb6f072b483b1e58a31297032a3f0a9eeac1d10baa743
- clm_ee06d390ad5670ba67ec9c13df0c7243a56fb20b7cd46603863b1177c763d672
maturity: draft
page_id: pg_dd96b98a44085aa9811fadab990b0c4a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_91908edf19ab5a6f80ba480c4a25457d
title: kirodotdev/Kiro/docs/STALE_ISSUE_CLOSING_EXPLAINED.md @ bfe7ff30d9b2
updated_at: '2026-09-14T02:09:24Z'
---

# kirodotdev/Kiro/docs/STALE_ISSUE_CLOSING_EXPLAINED.md @ bfe7ff30d9b2

<!-- rcw:begin owner=source:src_91908edf19ab5a6f80ba480c4a25457d block=evidence -->
- The stale-issue workflow requires GitHub permissions of issues:write (close issues, post comments) and contents:read (access scripts). [@claim:clm_1de13b58669272bd4649e9379411f996a9fd33a9e646ac37cf4eec1f54402ec4]
- The workflow targets open issues labeled 'pending-response', closes those inactive for 7 or more days, and posts a closing comment explaining the closure and how to reopen. [@claim:clm_57b45cd9a6217209dfe2ce39625ddc8a5b19034e1ace0ffc1b015d4a9c2aa484]
- Inactivity is measured from the more recent of the label-application date and the last activity date, where activity means new comments or any label change. [@claim:clm_c42d55e89d7823ad82e8a520b89fc10ece52924e5c99f33138d2d74afe7cadc9]
- The automation appears to be TypeScript scripts using the Octokit GitHub client, built with npm, based on code examples and build instructions in the docs. [@claim:clm_d9b249c073a96104d8ab56ccb5bf331eb06f0d958c13ef67240c5060498ad30a]
- GitHub API calls use retry with exponential backoff (up to 3 retries at 1s, 2s, 4s), and per-issue errors are logged without stopping processing of remaining issues. [@claim:clm_e7746c93cde4593477bd3b969127e422c869351a8a81c0e267723c1c9878d026]
- The stale-issue workflow runs daily at midnight UTC via cron and can also be triggered manually with gh workflow run close-stale.yml. [@claim:clm_ecb18d162b7f86cdc6bfb6f072b483b1e58a31297032a3f0a9eeac1d10baa743]
- Maintainers are advised to apply the pending-response label consistently, monitor workflow logs, and adjust the 7-day threshold if their community needs more time. [@claim:clm_ee06d390ad5670ba67ec9c13df0c7243a56fb20b7cd46603863b1177c763d672]
<!-- rcw:end owner=source:src_91908edf19ab5a6f80ba480c4a25457d block=evidence -->

## Researcher notes

