---
access: public
aliases: []
claim_ids:
- clm_3b005c62cdff2c918ddb4511f25ce9ebd1038d455eb7d1debd2b97ee0a29a45f
- clm_f5a1d32eae9a403a5524b02fee998ded80d910cb262dc89ce7aefec68a927ce2
maturity: draft
page_id: pg_8aa804deadc45eca84ed83e66472314e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3e1e634a91485184b21ba92ea00a1390
title: aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/README-Amplify-WebSocket-Workflow.md
  @ 092b5d81c5dc
updated_at: '2026-09-14T03:37:27Z'
---

# aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws/README-Amplify-WebSocket-Workflow.md @ 092b5d81c5dc

<!-- rcw:begin owner=source:src_3e1e634a91485184b21ba92ea00a1390 block=evidence -->
- The GraphQL schema defines Chat and Session models with owner-based auth rules, plus a custom sendChat mutation restricted to Cognito user pools. [@claim:clm_3b005c62cdff2c918ddb4511f25ce9ebd1038d455eb7d1debd2b97ee0a29a45f]
- Frontend-backend communication uses AWS AppSync GraphQL subscriptions; chat is sent via a sendChat mutation and responses arrive as onUpdateChat subscription messages with assistant text and trace data. [@claim:clm_f5a1d32eae9a403a5524b02fee998ded80d910cb262dc89ce7aefec68a927ce2]
<!-- rcw:end owner=source:src_3e1e634a91485184b21ba92ea00a1390 block=evidence -->

## Researcher notes

