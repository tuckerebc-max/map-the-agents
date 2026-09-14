# CodeReview-AI-Agent (`codereview-ai-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: smirk-dev
- License: MIT
- Language: Python 3.9+
- Interface: install=git clone; create venv; pip install -r requirements.txt; set GOOGLE_AI_API_KEY (GitHub token optional)
- Model providers: Google Gemini
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [smirk-dev/codereview-ai-agent](../../repos/smirk-dev/codereview-ai-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent AI code review built on Google's ADK with three specialized agents (Code Analyzer, Security Checker, Quality Reviewer) running in sequence/parallel for ~2-3x speedup; analyzes 6 languages and outputs 4 report formats (HTML/MD/SARIF/JSON, SARIF for IDE integration); built-in GitHub PR integration for automated comments and inline reviews; Kaggle Agents Intensive Capstone 2025 (Enterprise Agents Track).

(captured site page body (agents/codereview-ai-agent.md), not a verified repo-code finding)
CodeReview-AI-Agent was built as a Kaggle Agents Intensive 2025 capstone on Google's Agent Development Kit, structuring review as three cooperating agents: a Code Analyzer, a Security Checker, and a Quality Reviewer, coordinated by an orchestrator with shared session state. Agents run sequentially or in parallel depending on configuration, with parallel execution cutting review latency substantially on multi-language changes. The pipeline covers Python, JavaScript, TypeScript, Java, Go, and Rust, combines LLM judgment with Python AST analysis, and produces reports in HTML, Markdown, SARIF, and JSON — SARIF enabling direct IDE and GitHub Security integration. A GitHub integration posts review comments and inline annotations on pull requests, and a GitHub Actions workflow runs reviews from CI. The repository is a capstone portfolio project with 24 commits, not an actively maintained production tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codereview-ai-agent.md)
