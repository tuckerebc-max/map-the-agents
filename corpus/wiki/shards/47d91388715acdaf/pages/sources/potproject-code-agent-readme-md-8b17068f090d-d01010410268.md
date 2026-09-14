---
access: public
aliases: []
claim_ids:
- clm_064e9f75cff07110587e514b5ec13ca8d95d905fff135f81c873498350853852
- clm_0c92274d6401d9ffb7b11c520453a78adea193cb8553307ba6a631f86183049f
- clm_1e0d72ca8f38b04f44b8d0792fd678d6ccacbb8a5fd4dfdb9f7fc5919819ce6d
- clm_7c4132ddb371e882f0ac42b6727153d36920cdbdc675520783c88e7f9177115f
- clm_b6c22cb8d58a465c4f994f555d9443d76c4ee20eb58e1e62737d783ab8b2e4c4
- clm_c5fabc880ff7d347032c3e48fb91e460b324442dfd7dddb72a20ea7ca86d5469
- clm_cc250a920487ba5b685476dcf17cc710188bd70d678dc6a3c012ef443cf41c56
- clm_d2136fc581bc324dda620c8b510e5629c3fa3771ec054cc5e38910c98dce0720
- clm_e6663f7732baa53bb3594160ba5376605db4d9123bd1d97cb0f2f9a508101880
- clm_e96fa3bdee1afca238fa91d99038f9300fc372641f7c76399b3df3ab2ca8901d
- clm_f2e158264533e9a18167909d159f61362cf7956e965129364841300a48304de9
- clm_ffc1dd6a7b4929c1e00fe3c61c4dbe643f46311de456cdbfe0758e5328389d4d
maturity: draft
page_id: pg_e392702a05d456e381e4d01010410268
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9824adad08f25e3c9e8393f64b39ebe4
title: potproject/code-agent/README.md @ 8b17068f090d
updated_at: '2026-09-14T02:32:22Z'
---

# potproject/code-agent/README.md @ 8b17068f090d

<!-- rcw:begin owner=source:src_9824adad08f25e3c9e8393f64b39ebe4 block=evidence -->
- The action exposes inputs including github-token (required), event-path, and a timeout for AI processing defaulting to 600 seconds. [@claim:clm_064e9f75cff07110587e514b5ec13ca8d95d905fff135f81c873498350853852]
- Claude Code mode requires an anthropic-api-key input, while Codex mode requires an openai-api-key input, typically supplied from repository secrets. [@claim:clm_0c92274d6401d9ffb7b11c520453a78adea193cb8553307ba6a631f86183049f]
- Before running core logic, the action checks that the triggering user has write or admin permission on the repository. [@claim:clm_1e0d72ca8f38b04f44b8d0792fd678d6ccacbb8a5fd4dfdb9f7fc5919819ce6d]
- Secrets such as the GitHub token, API keys, and AWS credentials are masked as *** in any output the action posts to GitHub. [@claim:clm_7c4132ddb371e882f0ac42b6727153d36920cdbdc675520783c88e7f9177115f]
- The action is triggered by /claude or /codex commands posted in GitHub Issues or Pull Request comments, which start Claude Code or Codex respectively. [@claim:clm_b6c22cb8d58a465c4f994f555d9443d76c4ee20eb58e1e62737d783ab8b2e4c4]
- Codex mode supports an optional openai-base-url input to override the OpenAI API base URL. [@claim:clm_c5fabc880ff7d347032c3e48fb91e460b324442dfd7dddb72a20ea7ca86d5469]
- The product depends on external AI CLIs, Claude Code by Anthropic and Codex by OpenAI, which it invokes on behalf of the user. [@claim:clm_cc250a920487ba5b685476dcf17cc710188bd70d678dc6a3c012ef443cf41c56]
- When the AI modifies code, the action automatically creates a Pull Request or commits the changes; if no changes result, it posts the AI output as a comment instead. [@claim:clm_d2136fc581bc324dda620c8b510e5629c3fa3771ec054cc5e38910c98dce0720]
- Optional Claude Code inputs cover base URL, model selection, a small fast model for tasks like commit message generation, AWS Bedrock usage with AWS credentials, and disabling prompt caching. [@claim:clm_e6663f7732baa53bb3594160ba5376605db4d9123bd1d97cb0f2f9a508101880]
- Setup requires repository workflow permissions for read/write access and allowing GitHub Actions to create and approve pull requests. [@claim:clm_e96fa3bdee1afca238fa91d99038f9300fc372641f7c76399b3df3ab2ca8901d]
- The recommended workflow listens on issue opened, issue_comment created, and pull_request_review_comment created events, and skips runs triggered by bot senders. [@claim:clm_f2e158264533e9a18167909d159f61362cf7956e965129364841300a48304de9]
- The tool appears aimed at automating code changes directly from GitHub conversations, with an example repository linked for issues and pull requests. [@claim:clm_ffc1dd6a7b4929c1e00fe3c61c4dbe643f46311de456cdbfe0758e5328389d4d]
<!-- rcw:end owner=source:src_9824adad08f25e3c9e8393f64b39ebe4 block=evidence -->

## Researcher notes

