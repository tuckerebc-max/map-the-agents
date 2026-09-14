# potproject/code-agent -- full detail

[Back to orientation](code-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/potproject/code-agent/8b17068f090ddc32ccb05956e08f9ca9f740fdab/c663c1a26b3610b0.json](../../../wiki/dossiers/potproject/code-agent/8b17068f090ddc32ccb05956e08f9ca9f740fdab/c663c1a26b3610b0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] When the AI modifies code, the action automatically creates a Pull Request or commits the changes; if no changes result, it posts the AI output as a comment instead. -- evidence: [README.md#L7-L10](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L7-L10) (`clm_d2136fc581bc324dda620c8b510e5629c3fa3771ec054cc5e38910c98dce0720`)

## design-choices (2 claim(s))

- [observation/documented] The recommended workflow listens on issue opened, issue_comment created, and pull_request_review_comment created events, and skips runs triggered by bot senders. -- evidence: [README.md#L39-L45](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L39-L45), [README.md#L47-L54](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L47-L54) (`clm_f2e158264533e9a18167909d159f61362cf7956e965129364841300a48304de9`)
- [observation/documented] Setup requires repository workflow permissions for read/write access and allowing GitHub Actions to create and approve pull requests. -- evidence: [README.md#L18-L19](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L18-L19) (`clm_e96fa3bdee1afca238fa91d99038f9300fc372641f7c76399b3df3ab2ca8901d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The action is triggered by /claude or /codex commands posted in GitHub Issues or Pull Request comments, which start Claude Code or Codex respectively. -- evidence: [README.md#L3-L3](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L3-L3), [README.md#L7-L10](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L7-L10) (`clm_b6c22cb8d58a465c4f994f555d9443d76c4ee20eb58e1e62737d783ab8b2e4c4`)
- [observation/documented] The action exposes inputs including github-token (required), event-path, and a timeout for AI processing defaulting to 600 seconds. -- evidence: [README.md#L113-L117](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L113-L117) (`clm_064e9f75cff07110587e514b5ec13ca8d95d905fff135f81c873498350853852`)
- [observation/documented] Claude Code mode requires an anthropic-api-key input, while Codex mode requires an openai-api-key input, typically supplied from repository secrets. -- evidence: [README.md#L141-L143](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L141-L143), [README.md#L25-L25](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L25-L25), [README.md#L121-L123](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L121-L123) (`clm_0c92274d6401d9ffb7b11c520453a78adea193cb8553307ba6a631f86183049f`)
- [observation/documented] Optional Claude Code inputs cover base URL, model selection, a small fast model for tasks like commit message generation, AWS Bedrock usage with AWS credentials, and disabling prompt caching. -- evidence: [README.md#L127-L137](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L127-L137), [README.md#L59-L68](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L59-L68) (`clm_e6663f7732baa53bb3594160ba5376605db4d9123bd1d97cb0f2f9a508101880`)
- [observation/documented] Codex mode supports an optional openai-base-url input to override the OpenAI API base URL. -- evidence: [README.md#L73-L75](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L73-L75), [README.md#L148-L150](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L148-L150) (`clm_c5fabc880ff7d347032c3e48fb91e460b324442dfd7dddb72a20ea7ca86d5469`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Before running core logic, the action checks that the triggering user has write or admin permission on the repository. -- evidence: [README.md#L154-L155](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L154-L155) (`clm_1e0d72ca8f38b04f44b8d0792fd678d6ccacbb8a5fd4dfdb9f7fc5919819ce6d`)
- [observation/documented] Secrets such as the GitHub token, API keys, and AWS credentials are masked as *** in any output the action posts to GitHub. -- evidence: [README.md#L154-L155](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L154-L155) (`clm_7c4132ddb371e882f0ac42b6727153d36920cdbdc675520783c88e7f9177115f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product depends on external AI CLIs, Claude Code by Anthropic and Codex by OpenAI, which it invokes on behalf of the user. -- evidence: [README.md#L3-L3](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L3-L3) (`clm_cc250a920487ba5b685476dcf17cc710188bd70d678dc6a3c012ef443cf41c56`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [inference/documented] The tool appears aimed at automating code changes directly from GitHub conversations, with an example repository linked for issues and pull requests. -- evidence: [README.md#L3-L3](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L3-L3), [README.md#L79-L79](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L79-L79) (`clm_ffc1dd6a7b4929c1e00fe3c61c4dbe643f46311de456cdbfe0758e5328389d4d`)

