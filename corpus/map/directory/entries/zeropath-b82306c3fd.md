# ZeroPath (`zeropath`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ZeroPath
- License: unknown
- Language: unknown
- Interface: install=SaaS - connect GitHub, GitLab, Bitbucket, or Azure DevOps; zero-config repository scanning with no build scripts; cloud, hybrid, or on-prem deployment
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): AI-native scanning + verified security patches; RSAC 2026 Innovation Sandbox

(captured site page body (agents/zeropath.md), not a verified repo-code finding)
ZeroPath targets the failure mode of traditional SAST: a finding is reported, but producing an actual fix remains a human project. The platform scans repository fleets without requiring build configuration, using AI-driven analysis to catch business-logic flaws and auth bypasses that rule-based scanners miss. Its distinguishing step is agentic patching — for confirmed vulnerabilities an agent drafts a change that must compile, pass tests, and merge cleanly before it is proposed, turning scanner output into mergeable pull requests. Around that core sit complementary scanners: dependency analysis weighted by reachability, secrets detection across 40+ file types with validation, infrastructure-as-code scanning for Terraform and Kubernetes, container scanning, DAST with exploit proof, and continuous security review of pull requests. A versioned policy engine lets teams codify security requirements as testable rules, findings sync to Jira, Linear, or ServiceNow, and an AI inventory discovers models, agents, and MCP servers in customer codebases for AI-BOM compliance. A separate assistant agent, Zero, runs AppSec program tasks such as bug-bounty triage. Sold demo-first with cloud, hybrid, or on-prem deployment, it targets security engineering teams; the company was an RSAC 2026 Innovation Sandbox finalist and reports 300,000+ monthly scans.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zeropath.md)
