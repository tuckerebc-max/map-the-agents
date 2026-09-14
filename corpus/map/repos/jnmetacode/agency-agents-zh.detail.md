# jnmetacode/agency-agents-zh -- full detail

[Back to orientation](agency-agents-zh.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jnmetacode/agency-agents-zh/e00aed9f77ad66156af20e1acfdd69a51596b4da/ecf1c56b663d74e6.json](../../../wiki/dossiers/jnmetacode/agency-agents-zh/e00aed9f77ad66156af20e1acfdd69a51596b4da/ecf1c56b663d74e6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The library advertises 277 AI expert agents spanning 20 departments, of which 213 are translations of the English upstream and 64 are original China-market additions. -- evidence: [README.md#L5-L5](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L5-L5), [README.md#L21-L23](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L21-L23) (`clm_4d14819594770e366ba9ceb2ebee5e76edf180d7aadf90c7d4218eeed74dd00b`)
- [observation/documented] Each agent is defined as a persona with an identity, key rules, workflow, and deliverables, activated by natural language after installation into an AI coding tool. -- evidence: [README.md#L198-L198](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L198-L198) (`clm_7a6fc5cf9dff19f165a155191f2fa5d6d24609c01523bcbcf8324adbb967ddee`)
- [observation/documented] Original China-market agents cover platforms and verticals such as Xiaohongshu, Douyin, WeChat, Bilibili, Feishu/DingTalk operations, cross-border e-commerce, government ToG, medical compliance, Qt industrial host software, and mechanical design. -- evidence: [README.md#L7-L7](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L7-L7) (`clm_6ab1265b6d672ee3ca4bdf1d714974f2d5952c0cf48f7ebe3475956bd896e154`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README documents a usage workflow of converting formats (convert.sh), installing to a tool (install.sh), and linting agent files (lint-agents.sh), with OpenClaw requiring a gateway restart after install. -- evidence: [README.md#L718-L720](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L718-L720), [README.md#L700-L701](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L700-L701), [README.md#L696-L697](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L696-L697), [README.md#L692-L693](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L692-L693) (`clm_2479f15a3e5f3e6965af299b4c81781d0d95ce44994224f8c75f9a44ebbdf190`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The repo ships shell scripts for format conversion and one-click installation: install.sh (with --tool flags for 20 named tools), convert.sh, and lint-agents.sh for checking agent file format. -- evidence: [README.md#L700-L701](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L700-L701), [README.md#L212-L212](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L212-L212), [README.md#L696-L697](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L696-L697), [README.md#L215-L235](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L215-L235), [README.md#L692-L693](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L692-L693), [README.md#L661-L661](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L661-L661) (`clm_6deee4ba7d5408dc6ce513239a852fc55083404a2f299579a48805c9b0b3e4a1`)
- [observation/documented] Claude Code and GitHub Copilot agents can be copied directly without conversion; other tools require running convert.sh first to transform the format. -- evidence: [README.md#L740-L740](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L740-L740), [README.md#L237-L237](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L237-L237), [README.md#L725-L725](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L725-L725) (`clm_2b9869990c85a5a6b7fcb0f722bf21a673a984c192899d3b35ff06fe37009f52`)
- [observation/documented] For OpenClaw, each agent is split into three files — SOUL.md (identity/persona), AGENTS.md (capabilities and workflow), and IDENTITY.md (name and intro) — installed under ~/.openclaw/agency-agents/. -- evidence: [README.md#L241-L241](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L241-L241), [README.md#L708-L711](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L708-L711), [README.md#L665-L686](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L665-L686) (`clm_8a354c62f1fdb66bca7c5ebbc3c247034a7068c64858e56beac62b106473d221`)
- [observation/documented] A per-tool install-location table maps each of the 20 tools to target paths, e.g. ~/.claude/agents/ for Claude Code, .cursor/rules/ for Cursor, and ~/.gemini/extensions/agency-agents/ for Gemini CLI. -- evidence: [README.md#L665-L686](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L665-L686) (`clm_14bb3e1857ffec42bfcf844ec466bebe395f206e4ecaa20934df028c45417c1f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A companion tool, Agency Orchestrator (npm install -g agency-orchestrator), composes multiple expert agents into teams with a 'ao compose ... --run' command, advertising DAG parallel execution and resume-from-checkpoint. -- evidence: [README.md#L172-L175](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L172-L175), [README.md#L179-L179](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L179-L179) (`clm_1e2410e7fe1861549402f5ae860ff494140969ca0dae080ccaf8f8a3b0ee2295`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is a Chinese community fork of msitarzewski/agency-agents, published as the npm package agency-agents-zh under an MIT license. -- evidence: [README.md#L7-L7](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L7-L7), [README.md#L3-L3](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L3-L3), [README.md#L11-L16](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L11-L16) (`clm_6d498467d9e307e7d8ed024a0ac4cb60fa20d989951646fa6c43ea34b39d2cc0`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The collection targets users of AI coding assistants who want role-specialized prompts rather than generic templates; agents are also usable by copying/adapting the prompt text directly. -- evidence: [README.md#L262-L262](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L262-L262), [README.md#L5-L5](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L5-L5) (`clm_67696439575e9d300774ec8c37395d0110d2a6a80a5c27d1fbe49051d4ec997b`)

