# jnmetacode/agency-agents-zh

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e00aed9f77ad @ ecf1c56b663d74e6

## Summary (orientation draft, not independently verified)

The library advertises 277 AI expert agents spanning 20 departments, of which 213 are translations of the English upstream and 64 are original China-market additions. Each agent is defined as a persona with an identity, key rules, workflow, and deliverables, activated by natural language after installation into an AI coding tool. Evidence coverage: 146 of 367 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The library advertises 277 AI expert agents spanning 20 departments, of which 213 are translations of the English upstream and 64 are original China-market additions. -- evidence: [README.md#L5-L5](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L5-L5), [README.md#L21-L23](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L21-L23)
  - [observation/documented] Each agent is defined as a persona with an identity, key rules, workflow, and deliverables, activated by natural language after installation into an AI coding tool. -- evidence: [README.md#L198-L198](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L198-L198)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README documents a usage workflow of converting formats (convert.sh), installing to a tool (install.sh), and linting agent files (lint-agents.sh), with OpenClaw requiring a gateway restart after install. -- evidence: [README.md#L718-L720](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L718-L720), [README.md#L700-L701](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L700-L701), [README.md#L696-L697](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L696-L697), [README.md#L692-L693](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L692-L693)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The repo ships shell scripts for format conversion and one-click installation: install.sh (with --tool flags for 20 named tools), convert.sh, and lint-agents.sh for checking agent file format. -- evidence: [README.md#L700-L701](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L700-L701), [README.md#L212-L212](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L212-L212), [README.md#L696-L697](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L696-L697), [README.md#L215-L235](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L215-L235), [README.md#L692-L693](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L692-L693), [README.md#L661-L661](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L661-L661)
  - [observation/documented] Claude Code and GitHub Copilot agents can be copied directly without conversion; other tools require running convert.sh first to transform the format. -- evidence: [README.md#L740-L740](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L740-L740), [README.md#L237-L237](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L237-L237), [README.md#L725-L725](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L725-L725)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A companion tool, Agency Orchestrator (npm install -g agency-orchestrator), composes multiple expert agents into teams with a 'ao compose ... --run' command, advertising DAG parallel execution and resume-from-checkpoint. -- evidence: [README.md#L172-L175](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L172-L175), [README.md#L179-L179](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L179-L179)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project is a Chinese community fork of msitarzewski/agency-agents, published as the npm package agency-agents-zh under an MIT license. -- evidence: [README.md#L7-L7](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L7-L7), [README.md#L3-L3](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L3-L3), [README.md#L11-L16](https://github.com/jnMetaCode/agency-agents-zh/blob/e00aed9f77ad66156af20e1acfdd69a51596b4da/README.md#L11-L16)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](agency-agents-zh.detail.md)

Metadata and full claim list: [full detail](agency-agents-zh.detail.md)
Human notes ([notes](agency-agents-zh.notes.md), never overwritten by build)

[Back to map index](../../index.md)
