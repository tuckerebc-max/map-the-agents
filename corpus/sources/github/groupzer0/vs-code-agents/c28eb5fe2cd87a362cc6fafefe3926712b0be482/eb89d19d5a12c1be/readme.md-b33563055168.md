# Flowbaby Agent Team

> A multi-agent workflow system for GitHub Copilot in VS Code that brings structure, quality gates, and long-term memory to AI-assisted development.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What This Is

The Flowbaby Agent Team is the **reference implementation** for Flowbaby’s persistent memory system.

These agents are intentionally designed to take advantage of long-term, workspace-scoped memory. They demonstrate what agent workflows look like when memory is treated as infrastructure rather than chat history.

## The Problem

AI coding assistants are powerful but chaotic:
- They forget context between sessions
- They try to do everything at once (plan, code, test, review)
- They skip quality gates and security reviews
- They lose track of decisions made earlier

## The Solution

This repository provides **specialized AI agents** that each own a specific part of your development workflow:

| Agent | Role |
|-------|------|
| **Roadmap** | Product vision and epics |
| **Planner** | Implementation-ready plans (WHAT, not HOW) |
| **Analyst** | Deep technical research |
| **Architect** | System design and patterns |
| **Critic** | Plan quality review |
| **Security** | Comprehensive security assessment |
| **Implementer** | Code and tests |
| **Code Reviewer** | Code quality gate before QA |
| **QA** | Test strategy and verification |
| **UAT** | Business value validation |
| **DevOps** | Packaging and releases |
| **Retrospective** | Lessons learned |
| **ProcessImprovement** | Workflow evolution |

Each agent has **clear constraints** (Planner can't write code, Implementer can't redesign) and produces **structured documents** that create an audit trail.

Use as many or as few as you need, in any order. They are designed to know their own role and work together with other agents in this repo. They are designed to work together to create a structured and auditable development process. They are also designed to challenge each other to ensure the best possible outcome.

## Quick Start

### 1. Get the Agents

```bash
git clone https://github.com/groupzer0/agents.git
```

### 2. Add to Your Project

Copy agents to your workspace (per-repo, recommended):
```text
your-project/
└── .github/
    └── agents/
        ├── planner.agent.md
        ├── implementer.agent.md
        └── ... (others you need)
```

Or install them at the **user level** so they are available across all VS Code workspaces. User-level agents are stored in your [VS Code profile folder](https://code.visualstudio.com/docs/configure/profiles):

- **Linux**: `~/.config/Code/User/`
- **macOS**: `~/Library/Application Support/Code/User/`
- **Windows**: `%APPDATA%\Code\User\`

> [!TIP]
> The easiest way to create a user-level agent is via the Command Palette: **Chat: New Custom Agent** → select **User profile**. VS Code will place it in the correct location automatically.


### 3. Use in Copilot Chat

In VS Code, select your agent from the **agents dropdown** at the top of the Chat panel, then type your prompt:

```text
Create a plan for adding user authentication
```

> [!NOTE]
> Unlike built-in participants (e.g., `@workspace`), custom agents are **not** invoked with the `@` symbol. You must select them from the dropdown or use the Command Palette.

### 4. Flowbaby Requirement

These agents require Flowbaby to function correctly.

Flowbaby provides the persistent memory layer that allows agents to remember decisions, constraints, and prior work across sessions. Without Flowbaby, the agents fall back to stateless behavior and lose most of their intended value.

Install [Flowbaby](https://marketplace.visualstudio.com/items?itemName=flowbaby.flowbaby) for cross-session memory:

1. VS Code Extensions → Search "Flowbaby" → Install
2. Command Palette → "Flowbaby: Initialize Workspace"
3. Command Palette → "Flowbaby: Set API Key"

Flowbaby governs memory usage and evaluation limits for these agents.

### 5. (Optional) Use with GitHub Copilot CLI

You can also use these agents with the GitHub Copilot CLI by placing your `.agent.md` files under `.github/agents/` in each repository where you run the CLI, then invoking them with commands like:

```bash
copilot --agent planner --prompt "Create a plan for adding user authentication"
```

**Known limitation (user-level agents):** The Copilot CLI currently has an upstream bug where user-level agents in `~/.copilot/agents/` are not loaded, even though they are documented ([github/copilot-cli#452](https://github.com/github/copilot-cli/issues/452)). This behavior and the recommended per-repository workaround were identified and documented by @rjmurillo. Until the bug is fixed, prefer `.github/agents/` in each repo.


## Documentation

| Document | Purpose |
|----------|---------|
| [USING-AGENTS.md](USING-AGENTS.md) | Quick start guide (5 min read) |
| [AGENTS-DEEP-DIVE.md](AGENTS-DEEP-DIVE.md) | Comprehensive documentation |
| [CHANGELOG.md](CHANGELOG.md) | Notable repository changes |
| [memory-contract-example.md](vs-code-agents/memory-contract-example.md) | Memory usage patterns |

---

### Typical Workflow

```text
Roadmap → Planner → Analyst/Architect/Security/Critic → Implementer → Code Reviewer → QA → UAT → DevOps
```

1. **Roadmap** defines what to build and why
2. **Planner** creates a structured plan at the feature level or smaller
3. **Analyst** researches unknowns
4. **Architect** ensures design fit. Enforces best practices.
5. **Security** audits for vulnerabilities. Recommends best practices.
6. **Critic** reviews plan quality
7. **Implementer** writes code
8. **Code Reviewer** verifies code quality
9. **QA** verifies tests. Ensures robust test coverage
10. **UAT** confirms business value was delivered
11. **DevOps** releases (with user approval)

---

## Key Features

### 🎯 Separation of Concerns
Each agent has one job. Planner plans. Implementer implements. No scope creep.

### 📝 Document-Driven
Agents produce Markdown documents in `agent-output/`. Every decision is recorded.

### 🔒 Quality Gates
Critic reviews plans. Security audits code. QA verifies tests. Nothing ships without checks.

### 🧠 Robust Memory
With [Flowbaby](https://github.com/groupzer0/flowbaby), agents remember decisions across sessions.

### 🔄 Handoffs
Agents hand off to each other with context. No lost information between phases.

---

## Flowbaby Memory Integration

[Flowbaby](https://github.com/groupzer0/flowbaby) is a VS Code extension that solves a specific problem: Copilot forgets what you've discussed. Across sessions, developers repeatedly re-explain context, architecture decisions, and constraints. Flowbaby captures, summarizes, and resurfaces relevant prior work automatically—bridging context between sessions and maintaining continuity within long-running conversations.

The persistent memory layer that powers the Flowbaby Agent Team.

### Links

- **GitHub**: https://github.com/groupzer0/flowbaby
- **VS Code Marketplace**: https://marketplace.visualstudio.com/items?itemName=flowbaby.flowbaby
- **Documentation**: See the GitHub README for full setup guide

---

## Repository Structure

```text
agents/
├── CHANGELOG.md                 # Notable changes
├── README.md                    # This file
├── USING-AGENTS.md              # Quick start guide
├── AGENTS-DEEP-DIVE.md          # Comprehensive documentation
├── LICENSE                      # MIT License
└── vs-code-agents/              # Agent definitions
    ├── analyst.agent.md
    ├── architect.agent.md
    ├── critic.agent.md
    ├── devops.agent.md
    ├── implementer.agent.md
    ├── pi.agent.md              # ProcessImprovement
    ├── planner.agent.md
    ├── qa.agent.md
    ├── code-reviewer.agent.md
    ├── retrospective.agent.md
    ├── roadmap.agent.md
    ├── security.agent.md
    ├── uat.agent.md
    └── reference/
        └── memory-contract-example.md
```

---

## Security Agent Highlight

The **Security Agent** has been enhanced to provide truly comprehensive security reviews:

### Five-Phase Framework
1. **Architectural Security**: Trust boundaries, STRIDE threat modeling, attack surface mapping
2. **Code Security**: OWASP Top 10, language-specific vulnerability patterns
3. **Dependency Security**: CVE scanning, supply chain risk assessment
4. **Infrastructure Security**: Headers, TLS, container security
5. **Compliance**: OWASP ASVS, NIST, industry standards

### Why This Matters

Most developers don't know how to conduct thorough security reviews. They miss:
- Architectural weaknesses (implicit trust, flat networks)
- Language-specific vulnerabilities (prototype pollution, pickle deserialization)
- Supply chain risks (abandoned packages, dependency confusion)
- Compliance gaps (missing security headers, weak TLS)

The Security Agent systematically checks all of these, producing actionable findings with severity ratings and remediation guidance.You can then hand this off to the Planner agent and the Implementer to address. 

See [security.agent.md](vs-code-agents/security.agent.md) for the full specification.

---

## Customization

### Modify Existing Agents

Edit `.agent.md` files to adjust:
- `description`: What shows in Copilot
- `tools`: Which VS Code tools the agent can use
- `handoffs`: Other agents it can hand off to
- Responsibilities and constraints

### Create New Agents

1. Create `your-agent.agent.md` following the existing format
2. Define purpose, responsibilities, constraints
3. Include the Memory Contract section
4. Add to `.github/agents/` in your workspace

---

## Recent Updates

Recent commits introduced significant improvements to agent workflow and capabilities:

### Uncertainty-Aware Issue Analysis (2026-01-15)

Agents now explicitly avoid forced root-cause narratives when evidence is missing.

- **Analyst**: Uses an objective hard pivot trigger (timebox/evidence gate) to switch from RCA attempts to system hardening + telemetry requirements.
- **Architect**: Treats insufficient observability as an architectural risk; defines normal vs debug logging guidance and a minimum viable incident telemetry baseline.
- **QA**: Validates diagnosability improvements; prefers asserting structured telemetry fields/events over brittle log string matching.
- **Template**: `vs-code-agents/reference/uncertainty-review-template.md` provides a repeatable output format.

### Skills System (2025-12-19)

Agents now use **Claude Skills**—modular, reusable instruction sets that load on-demand:

| Skill | Purpose |
|-------|---------|
| `memory-contract` | Unified Flowbaby memory retrieval/storage contract |
| `analysis-methodology` | Confidence levels, gap tracking, investigation techniques |
| `architecture-patterns` | ADR templates, patterns, anti-pattern detection |
| `code-review-checklist` | Pre/post-implementation review criteria |
| `code-review-standards` | Code review checklist, severity definitions, document templates |
| `cross-repo-contract` | Multi-repo API type safety and contract coordination |
| `document-lifecycle` | Unified numbering, automated closure, orphan detection |
| `engineering-standards` | SOLID, DRY, YAGNI, KISS with detection patterns |
| `release-procedures` | Two-stage release workflow, semver, platform constraints |
| `security-patterns` | OWASP Top 10, language-specific vulnerabilities |
| `testing-patterns` | TDD workflow, test pyramid, coverage strategies |

**Skill Placement:**
- **VS Code Stable (1.107.1)**: Place in `.claude/skills/`
- **VS Code Insiders**: Place in `.github/skills/`

> [!NOTE]
> These locations are changing with upcoming VS Code releases. The `.github/skills/` location is becoming the standard. See the [VS Code Agent Skills documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills) for the latest guidance.

### Key Agent Flow Improvements

- **TDD mandatory**: Implementer and QA now require Test-Driven Development for new feature code
- **Two-stage release**: DevOps commits locally first; pushes only on explicit release approval
- **Document status tracking**: All agents update Status fields in planning docs ("Draft", "In Progress", "Released")
- **Open Question Gate**: Implementer halts if plans have unresolved questions; requires explicit user acknowledgment to proceed
- **Memory as skill**: Memory contract moved from inline in each agent to a loadable `memory-contract` skill
- **Slimmed Security agent**: Reduced by 46% using skill references instead of inline content

### Cross-Repository Contract Skill (2025-12-26)

New `cross-repo-contract` skill for projects with runtime + backend repos that need to stay aligned:

- **Contract discovery**: Agents check `api-contract/` or `.contracts/` for type definitions
- **Type safety enforcement**: Implementer verifies contract definitions before coding API endpoints/clients
- **Breaking change coordination**: Plans must document contract changes and sync dependencies
- **Quality gate**: Critic verifies multi-repo plans address contract adherence

Integrated into Architect, Planner, Implementer, and Critic agents.

### Document Lifecycle System (2025-12-24)

New `document-lifecycle` skill implementing:

- **Unified numbering**: All documents in a work chain share the same ID (analysis 080 → plan 080 → qa 080 → uat 080)
- **Automated closure**: Documents move to `closed/` subfolders after commit
- **Orphan detection**: Agents self-check + Roadmap periodic sweep

This keeps active plans visible while archiving completed work for traceability.

### Previous Updates

- **Refined Flowbaby memory contract (2025-12-16)**: All core agents share a unified memory contract. Agents function without Flowbaby but greatly benefit from its use.
- **Aligned agent tool names with VS Code APIs (2025-12-16)**: Agent `tools` definitions now use official VS Code agent tool identifiers.
- **Added subagent usage patterns (2025-12-15)**: Planner, Implementer, QA, Analyst, and Security document how to invoke each other as scoped subagents.
- **Background Implementer mode (2025-12-15)**: Implementation can run as local chat or background agent in isolated Git worktree.

## Contributing

Contributions welcome! Areas of interest:

- **Agent refinements**: Better constraints, clearer responsibilities
- **New agents**: For specialized workflows (e.g., Documentation, Performance)
- **Memory patterns**: Better retrieval/storage strategies
- **Documentation**: Examples, tutorials, troubleshooting

This repository also runs an automatic **Markdown lint** check in GitHub Actions on pushes and pull requests that touch `.md` files. The workflow uses `markdownlint-cli2` with a shared configuration, and helps catch issues like missing fenced code block languages (MD040) early in review. This lint workflow was proposed based on feedback and review from @rjmurillo.

---

## Requirements

- VS Code with GitHub Copilot
- For memory: [Flowbaby extension](https://marketplace.visualstudio.com/items?itemName=flowbaby.flowbaby) + Python 3.10+

---

## License

MIT License - see [LICENSE](LICENSE)

---

## Related Resources

- [GitHub Copilot Agents Documentation](https://code.visualstudio.com/docs/copilot/copilot-agents)
- [Flowbaby Extension](https://github.com/groupzer0/flowbaby)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
