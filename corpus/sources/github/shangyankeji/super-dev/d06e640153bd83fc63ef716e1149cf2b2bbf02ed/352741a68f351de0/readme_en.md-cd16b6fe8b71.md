# Super Dev

<div align="center">

<img src="docs/assets/super-dev-logo.png" alt="Super Dev - AI PIPELINE ORCHESTRATOR" width="600">

### Host Coaching System for Commercial-Grade Delivery

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Type Checks](https://img.shields.io/badge/type%20checks-mypy-success)](https://mypy-lang.org/)
[![Lint](https://img.shields.io/badge/lint-ruff-success)](https://docs.astral.sh/ruff/)

[简体中文](README.md) | English

</div>

---

## Version

Current version: `2.4.0`

- Release notes: [v2.4.0](docs/releases/2.4.0.md)
- Website changelog: [superdev.goder.ai/changelog](https://superdev.goder.ai/changelog)

## Install

The homepage installation story is now intentionally uv-first:

```bash
uv tool install super-dev
```

Then run:

```bash
super-dev
```

Source installs and rollback/version-pinning flows remain in [docs/INSTALL_OPTIONS.md](docs/INSTALL_OPTIONS.md).

Cross-platform note:

- Windows, macOS, and Linux all use the same entry: install the package, then run `super-dev`.
- The repository `install.sh` is a macOS/Linux convenience script, not the only Windows path.

## What's New in 2.4.0

### Public Surface, Finally Host-First

- The terminal is now intentionally small:
  - `super-dev`
  - `super-dev update`
  - `super-dev uninstall`
- Real delivery work happens inside the host through:
  - `/super-dev`
  - `/super-dev-seeai`
  - `continue current flow`
  - `what is the next step now`
- `super-dev-core` has been removed from current code, templates, skills, and active contracts. The product name is consistently `super-dev`.

### Existing-Project Flow Is Now First-Class

- Existing-project work now follows a formal chain instead of pretending every job is greenfield:
  - `baseline -> baseline confirmation -> delta research -> docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery`
- `resume` is a first-class scenario, not an exception.
- `workflow_context`, `baseline_governance`, and `resume_gate` now drive detect / doctor / validate / proof-pack / release-readiness consistently.

### 26-Host Unified Matrix

- The current matrix is now unified as:
  - 12 CLI hosts
  - 9 IDE hosts
  - 5 desktop assistants
- `Droid CLI`, `Kimi Code`, `Qwen Code`, `Trae SOLO`, and `Trae SOLOCN` are first-class hosts in the current matrix.
- `OpenClaw` is no longer part of the current support surface.
- Host adaptation now includes:
  - project-first onboarding
  - optional user/global surfaces
  - official alignment
  - host start playbooks
  - resume guidance
  - repair playbooks
  - post-onboard self-checks
  - standard vs. SEEAI readiness

### Project-First Onboarding

- Super Dev no longer defaults to writing rules into system-level `AGENTS.md`.
- The default is now project-first:
  - write project surfaces first
  - only add user/global surfaces with explicit opt-in
- This keeps onboarding safer, cleaner, and closer to real team workflows.

### UI Design Upgrade: Less AI Slop, More Intentional Design

- The UI contract now freezes:
  - art-direction candidates
  - a visual philosophy / direction manifest
  - anti-AI-slop guardrails
  - a five-dimension critique rubric
  - tweak categories
- Frontend blueprints and UI review now consume those signals directly instead of treating design as a generic template problem.

### Release Gates Are Green Again

- `pytest -q`: `2576 passed, 2 skipped`
- `scripts/preflight.sh --allow-dirty`: passing
- Core release gates, knowledge gates, delivery smoke, host compatibility, build, and twine checks are green again

For the full breakdown, see [docs/releases/2.4.0.md](docs/releases/2.4.0.md).

---

## Demo Video

<video controls playsinline preload="metadata" src="https://shangyankeji.github.io/super-dev/demo.mp4" width="100%"></video>

- Stream online: [Watch the demo](https://shangyankeji.github.io/super-dev/demo.mp4)
- Repository file: [demo.mp4](super-dev-website/public/demo.mp4)

---

## What is Super Dev

`Super Dev` is not another layer of low-level commands or a scaffolding shell. It is a host coaching system that trains the model capabilities inside your host into a stable, transparent, auditable delivery flow for real commercial software work.

**Division of responsibility:**

- The host handles model inference, web research, code generation, terminal execution, and file modifications.
- `Super Dev` handles blueprints, workflow governance, design constraints, quality gates, audit artifacts, and delivery standards.

In practice:

- the host is the executor
- `Super Dev` is the product coach, architecture coach, design director, and QA gatekeeper

**Problems it solves:**

- Converts requirements into production artifacts: PRD, architecture, UI/UX spec, task plans, and delivery manifests.
- Organizes development into a standardized pipeline: traceable, resumable, auditable, and reviewable.
- Enforces quality at every stage: policy governance, red-team review, quality gates, and release rehearsals.
- Unifies collaboration across 12 CLI hosts, 9 IDE hosts, and 5 desktop assistants under one project-first delivery standard.
- Trains the host into a more reliable commercial-delivery team instead of leaving users to manually improvise process, design, and quality.

---

## 5-Minute Start

Regular users should remember 1 install command and 3 terminal commands:

```bash
uv tool install super-dev
```

```bash
# Enter the host onboarding flow
super-dev

# Upgrade to the latest version and migrate onboarded hosts
super-dev update

# Remove injected Super Dev surfaces from onboarded hosts
super-dev uninstall
```

### 5-minute path

1. Run `super-dev` inside the project directory.
2. Let the installer detect hosts and write project-level surfaces first; only add user/global surfaces when you explicitly want them.
3. Open `output/maintenance/host-onboard-smoke-*.md`.
4. Read the `standard-flow first prompt` or `competition-flow first prompt`.
5. Check `post-onboard self-check`, `Framework focus`, and `official workflow checks`.
6. Go back to the host and trigger the first prompt. The host should enter `research -> three core docs -> wait for confirmation`.

If those six steps hold, you did not just “install a tool.” You turned the current host into a coached delivery system for this repository.

### The terminal only does 3 things
- onboarding
- upgrade
- uninstall / cleanup preview

After onboarding, regular use moves back into the host. Regular users should only need to remember:

```text
/super-dev your requirement
super-dev: your requirement
/super-dev-seeai your competition brief
```

Do not try to memorize every host-specific trigger. Open the generated `host-onboard-smoke` guide and copy the `standard-flow first prompt` or `competition-flow first prompt`.

Correct mental model:

- The terminal is only for onboarding, upgrading, and uninstalling.
- The host is where baseline, research, the three core docs, approval gates, spec, implementation, quality gates, and delivery happen.
- Auto-judgement is allowed during onboarding and upgrade, not during normal development flow.
- `Integrated` and `runtime verified` are different states. Files existing does not prove the host actually follows the governed flow.
- Existing-project work must not jump directly into docs or coding. `evolve / variant / patch` always start with a baseline scan.
- Resume is the default scenario. Closing the host, shutting the laptop, or returning the next day should continue from `.super-dev/` and `output/` artifacts.

Work modes:

- `new`: greenfield 0-to-1 delivery
- `evolve`: additive work on the current product
- `variant`: 1-N+1 derivative based on the current product
- `patch`: bugfix / remediation on the current product
- `resume`: continue the interrupted workflow

Recommended first run:

1. Run `super-dev` in the terminal.
2. Let the installer detect hosts and write the required project-level surfaces by default; add `--with-user-surfaces` only when you explicitly want cross-project user/global protocol surfaces.
3. The installer is project-first: it writes project surfaces before optional user/global surfaces.
4. Open `output/maintenance/host-onboard-smoke-*.md` and validate the host using the generated smoke guide first, including any Framework focus when the project already has a frozen framework playbook.
5. Open the host and use `/super-dev` or `super-dev:`.
6. For existing projects, let the host finish baseline first, then generate delta research, PRD, Architecture, and UI/UX.
7. Only move to Spec and implementation after the docs are confirmed.

Main rule: once installation is done, the terminal should mostly step aside. Real project work moves back into the host. Copy the standard-flow or competition-flow first prompt first, then follow the smoke guide.

SEEAI competition fast mode:

- Entry: `/super-dev-seeai` or `super-dev-seeai:`
- It still keeps `research -> docs -> docs confirm -> spec`
- After Spec it goes straight into an integrated full-stack sprint, without a separate preview confirmation gate
- Best for 30-minute showcase builds such as a polished landing page, mini-game, or focused demo tool

Everything else (`detect / doctor / review / quality / release / spec / task`) remains available as maintenance surface only. Regular users should only need:

```bash
super-dev
super-dev update
super-dev uninstall
```

Maintainer additions:

- Post-onboard smoke guides are written to `output/maintenance/host-onboard-smoke-*.md`
- If the project already has a frozen framework playbook, the smoke guide also exposes Framework focus, validation surfaces, and delivery evidence.
- Uninstall previews and cleanup audits are written to `output/maintenance/host-cleanup-*.json/.md`
- Use `super-dev uninstall --dry-run` to preview removals before deleting anything
- After upgrade, reopen the terminal and run `super-dev --version`; if the host no longer enters `research -> three core docs -> wait for confirmation`, then return to the terminal and run `doctor`
- If the first UI pass still looks flat, empty, or template-like, do not defer polish to the end. A screenshot-level UI gate now keeps blocking that state across UI review, quality gate, proof-pack, and release readiness.
- `docs/PUBLISHING.md` and `docs/RELEASE_RUNBOOK.md` are maintainer-only release docs, not part of the normal end-user path.

---

## Core Features

### 1. 11-Expert Agent Architecture

Super Dev currently ships with eleven domain-expert agents. Each expert is injected into prompts at the corresponding pipeline stage so the host stays constrained to professional-grade output:

| Expert | Role | Injection Stages |
|--------|------|-----------------|
| PRODUCT | Product Lead | research, prd, quality, delivery |
| PM | Product Manager | research, prd |
| ARCHITECT | System Architect | architecture |
| UI | Interface Designer | uiux, frontend |
| UX | Interaction Designer | uiux, frontend |
| SECURITY | Security Engineer | architecture, backend, quality |
| CODE | Software Engineer | frontend, backend |
| DBA | Database Architect | architecture, backend |
| QA | Quality Assurance | quality |
| DEVOPS | DevOps Engineer | delivery |
| RCA | Root Cause Analyst | quality, delivery |

Each expert carries: objective definition, background story, thinking framework, and quality criteria. The generated AI prompts ensure every stage meets domain-specific professional baselines.

### 2. UI Design Intelligence System

A built-in design intelligence engine that directly constrains visual quality during frontend implementation:

- **119 color palettes**: 84 product palettes + 35 aesthetic palettes, all with automatic dark mode generation.
- **39 component libraries**: covering 11 frontend stacks (React 15 / Vue 9 / Angular 4 / Svelte 2 / others).
- **17 typography presets**: based on Google Fonts, categorized by product tone and personality.
- **Complete design token system**: color scales, shadows, motion, typography, and spacing.
- **12-item pre-delivery checklist**: A11y, responsive design, dark mode, loading states, empty states, error states, and more.
- **10 industry customizations**: education, healthcare, e-commerce, fintech, SaaS, social, content, enterprise, utilities, and gaming.

The UI system is no longer only advisory. It is frozen into actual artifacts:

- `output/*-uiux.md`
- `output/*-ui-contract.json`
- `output/frontend/design-tokens.css`
- `output/*-ui-contract-alignment.md`
- `output/*-ui-contract-alignment.json`

Host prompts, implementation constraints, UI review, frontend runtime, quality gate, proof-pack, and release readiness all consume that same UI contract.

Key governance evidence:

- UI review and UI contract alignment
- Frontend runtime evidence
- Proof-pack and release readiness summaries

### 3. Pipeline Orchestration Engine

- **9-stage standard pipeline**: research -> prd -> architecture -> uiux -> spec -> frontend -> backend -> quality -> delivery.
- **Checkpoint and resume**: interrupted pipelines resume from the last completed stage without losing progress.
- **Stage timeout protection**: each stage has a timeout mechanism to prevent indefinite stalling.
- **Confirmation gates**: mandatory user confirmation after core documents and after frontend preview.
- **Stage recovery**: natural-language recovery inside the host is the default path; explicit stage-jump controls remain maintenance-only.
- **UI revision loop**: when the frontend needs another pass, start the revision loop inside the host and update UIUX before redoing the frontend.
- **Dual-mode delivery**: works for both greenfield (0-1) and iterative (1-N+1) projects.
- **Continuation routing**: internal recovery and status commands share the same workflow state and action card semantics.
- **Session recovery card**: `.super-dev/SESSION_BRIEF.md` and `.super-dev/workflow-state.json` persist the current action, host first sentence, machine action, and continuity rules.
- **Recent operational timeline**: workflow snapshots, semantic workflow events, and hook events are merged into one timeline that now surfaces in `SESSION_BRIEF`, Workflow Harness, proof-pack, and release readiness.
- **Rework-first state handling**: docs confirmation, preview confirmation, UI redesign, architecture rework, and quality remediation all stay inside one governed state machine.

### 4. Document Generation Engine

Super Dev generates an initial document framework for each stage. The host LLM then enriches it with user requirements, web research, and expert knowledge:

| Document | Content |
|----------|---------|
| PRD | User personas, feature matrix, acceptance criteria, competitive benchmarking, business rules |
| Architecture | System architecture, data models, API contracts, security strategy, deployment plan |
| UIUX | Design tokens, page skeletons, component inventory, interaction states, responsive strategy |

The host expands documents based on actual project needs. Final document scope depends on project complexity. Supports 10 industry-specific customizations: education, healthcare, e-commerce, fintech, SaaS, social, content, enterprise, utilities, and gaming.

### 5. Quality Gate System

- A11y accessibility checks.
- Performance budget enforcement.
- Red-team review (security / performance / architecture).
- Fix command suggestions (detected issues produce actionable repair instructions).
- Policy governance (`default` / `balanced` / `enterprise` presets).
- Spec quality scoring and release-readiness panel.
- UI contract execution checks (`ui-contract.json`, `design-tokens.css`, frontend runtime, and UI alignment evidence must stay consistent).

### 6. Host Onboarding Governance

- A unified onboarding matrix grouped into CLI hosts, IDE hosts, and desktop assistants.
- Droid CLI joins the official host matrix via `AGENTS.md + .factory/rules + .factory/skills`, with `.factory/commands` kept as a compatibility enhancement.
- Auto-generates host rule files, slash command mappings, and Skill directories.
- Host capability boundary modeling: Certified / Compatible / Experimental three-tier certification.
- `detect` / `onboard` / `doctor` / `setup` / `install` / `start` form a closed onboarding loop.
- `--dry-run` preview mode and `--stable-only` stable-only mode.
- `doctor`, `detect`, and `start` now emit decision cards: recommended host, recommendation reason, first action, folded candidate list, and path-override hints.
- Decision cards, the installer, and runtime reports now surface the host's standard-flow first prompt, competition-flow first prompt, post-onboard self-check, official workflow checks, and repair playbook.
- Host readiness is no longer just "files exist"; it explicitly distinguishes "ready for standard flow" vs. "ready for SEEAI competition flow".
- Supports Windows registry hits, shim directories, common install paths, and `SUPER_DEV_HOST_PATH_<HOST>` explicit path overrides.
- If you explicitly choose a host, Super Dev centers guidance around that host instead of letting auto-detection override your intent.

### 7. Internal Analysis and Scope Governance

The runtime still keeps internal analysis capabilities such as scope coverage, blast-radius estimation, and regression planning. They remain part of the governance core, but they are no longer taught as standalone public commands for ordinary users.

### 8. Auditable Delivery

- `pipeline-metrics`: telemetry and metrics report.
- `pipeline-contract`: stage-level contract evidence.
- `resume-audit`: resume execution audit trail.
- `delivery manifest/report/archive`: delivery package.
- `proof-pack`: delivery evidence bundle with executive summary.
- `release readiness`, `Spec Quality`, and `Scope Coverage`: unified release scoring panel.
- UI Contract Alignment is part of proof-pack and release readiness, not just an internal UI review detail.
- Governance snapshots, frontend runtime, validation reports, and knowledge tracking now participate in delivery closure.

### 9. Knowledge Base

- Project-level `knowledge/` directory for domain knowledge files.
- Knowledge bundle caching at `output/knowledge-cache/*-knowledge-bundle.json`.
- Matched local standards, scenario packs, and checklists are treated as hard constraints.
- Hosts must read relevant knowledge files before drafting PRD, architecture, and UIUX documents.
- Knowledge hits are inherited into Spec and implementation stages.

### 10. Policy Governance (Policy DSL)

Parameterized workflow governance through a Policy DSL:

- **default**: standard preset, suitable for individuals and small teams.
- **balanced**: balanced preset, suitable for medium-sized teams.
- **enterprise**: enterprise preset, higher quality thresholds, host profiling requirements, and configurable required hosts per project.

Governance control dimensions:

- Mandatory red-team / quality gate toggle.
- Minimum quality threshold enforcement.
- CI/CD platform whitelist.
- Required hosts and ready+score hard validation (enabled per project).
- Automatic host profiling and scoring.
- `host-compatibility` report with history tracking.

Configurable via `super-dev.yaml` policy section.

---

## How It Works

1. User runs `super-dev` in the project directory.
2. The onboarding wizard connects Super Dev to the target host.
3. User triggers Super Dev using the host's supported entry, such as `/super-dev requirement`, `super-dev: requirement`, Codex App/Desktop selecting `super-dev` from the `/` list, or Codex CLI typing `$super-dev`.
4. The host enters the Super Dev pipeline; 11 expert agents are injected by stage.
5. The host handles web research, inference, coding, execution, and file modifications.
6. Super Dev handles workflow, documents, gates, audit, and delivery standards.

Standard flow for new work: `research -> docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery`

Existing-project flow: `baseline -> baseline confirmation -> delta docs -> docs_confirm -> spec -> frontend -> preview_confirm -> backend -> quality -> delivery`

New features follow the full pipeline. Bug fixes follow a lightweight patch path (symptoms, reproduction, blast radius, regression risk) without skipping documentation. Analysis stages automatically exclude `.venv`, `site-packages`, `node_modules`, and other non-source directories.

### How Hosts Understand Super Dev

- `Super Dev` is a local Python CLI tool plus host-side rule files / Skills / slash mappings.
- The host handles inference, research, coding, and execution. `Super Dev` handles pipeline flow, gates, and audit.
- When the user uses the host-supported Super Dev entry (`/super-dev`, `super-dev:`, Codex App/Desktop `/`-list skill entry, or Codex CLI `$super-dev`), the host switches to pipeline mode.
- If a `knowledge/` directory exists, the host reads relevant knowledge files before drafting documents.
- If `output/knowledge-cache/*-knowledge-bundle.json` exists, its knowledge hits are inherited into all later stages.

---

## Installation

### 1. uv (recommended)

```bash
uv tool install super-dev
```

Upgrade:

```bash
super-dev update
```

### 2. Pin a specific version

```bash
uv tool install super-dev==2.4.0
```

Upgrade:

```bash
uv tool upgrade super-dev
super-dev update
```

After installation, run `super-dev` to launch the interactive host onboarding wizard (`Up/Down` to navigate, `Space` to select, `Enter` to install, `A` for all, `C` for CLI only, `I` for IDE only, `R` to reset). The terminal prints the exact trigger command for each selected host.

To explicitly initialize the project contract before onboarding:

```bash
super-dev bootstrap --name my-project --platform web --frontend next --backend node
```

This generates `.super-dev/WORKFLOW.md` and `output/*-bootstrap.md` to lock down initialization spec, trigger method, and stage sequence.

### 3. Install from GitHub tag

```bash
uv tool install --from git+https://github.com/shangyankeji/super-dev.git@v2.4.0 super-dev
```

### 4. Source install for development

```bash
git clone https://github.com/shangyankeji/super-dev.git
cd super-dev
uv sync
uv run super-dev --version
```

### Dependency Notes

`uv` automatically installs Super Dev's own Python dependencies (`rich`, `pyyaml`, `ddgs`, `requests`, `beautifulsoup4`, `fastapi`, `uvicorn`, etc.).

It does **not** install:

- Host applications (Claude Code, Codex CLI, Gemini CLI, Cursor, Trae, Windsurf, and desktop assistants)
- System runtimes (Node.js, npm, pnpm, Docker, database services)
- Host authentication state, browsing permissions, or API keys
- Project-specific frontend/backend runtime dependencies

In short: `uv` installs **Super Dev's Python dependencies**. It does not install **host tools or system environments** on your behalf.

---

## Architecture Overview

### System Flow Architecture

Shows the relationship between users, host-side tools, the Super Dev orchestration engine, and final artifacts.

![System Overview](docs/assets/architecture/en/system-overview.png)

### Pipeline Stage Flow

Details the internal execution flow after each host-side trigger.

![Pipeline Stages](docs/assets/architecture/en/pipeline-12-phase.png)

### Core Module Topology

Shows the responsibility boundaries and call relationships of core source directories under `super_dev`.

![Module Topology](docs/assets/architecture/en/module-topology.png)

---

## Unified Host Matrix

Super Dev officially documents one unified onboarding matrix:

- **Certified**: fully aligned integration model; recommended for production use.
- **Compatible**: complete integration path; awaiting extended real-world validation.
- **Experimental**: functional integration; needs broader production testing.
- Project-first injection is the default: project surfaces are written first, then optional user/global surfaces.
- `Codex` and `Codex CLI` are distinct hosts, and `Claude` and `Claude Code` are distinct hosts.

### Unified CLI Hosts (12)

| Host | Trigger | Terminal Entry |
|------|---------|-----------------|
| Claude Code | `/super-dev your requirement` | `super-dev` |
| Codex CLI | `$super-dev`; fallback `super-dev: your requirement` | `super-dev` |
| OpenCode | `/super-dev your requirement` | `super-dev` |
| Droid CLI | `/super-dev your requirement`; competition mode `/super-dev-seeai`; fallback `super-dev: your requirement` | `super-dev` |
| Gemini CLI | `/super-dev your requirement` | `super-dev` |
| Kiro CLI | `/super-dev your requirement` | `super-dev` |
| Cursor CLI | `super-dev: your requirement` | `super-dev` |
| Copilot CLI | `super-dev: your requirement` | `super-dev` |
| Qoder CLI | `/super-dev your requirement` | `super-dev` |
| CodeBuddy CLI | `/super-dev your requirement` | `super-dev` |
| Kimi Code | `super-dev: your requirement`; explicit entry `/skill:super-dev your requirement` | `super-dev` |
| Qwen Code | `/super-dev your requirement` | `super-dev` |

### IDE Hosts (9)

| Host | Trigger | Terminal Entry |
|------|---------|-----------------|
| Antigravity | `/super-dev your requirement` | `super-dev` |
| Cursor | `/super-dev your requirement` | `super-dev` |
| Windsurf | `/super-dev your requirement` | `super-dev` |
| Kiro | `/super-dev your requirement` | `super-dev` |
| Trae IDE | `super-dev: your requirement` | `super-dev` |
| TraeCN | `super-dev: your requirement` | `super-dev` |
| CodeBuddy | `/super-dev your requirement` | `super-dev` |
| CodeBuddyCN | `/super-dev your requirement` | `super-dev` |
| Qoder | `/super-dev your requirement` | `super-dev` |

### Desktop Assistants (5)

| Host | Trigger | Terminal Entry |
|------|---------|-----------------|
| Claude | `super-dev: your requirement` | `super-dev` |
| Codex | App/Desktop: select `super-dev` from the `/` list | `super-dev` |
| WorkBuddy | `super-dev: your requirement` | `super-dev` |
| Trae SOLO | `/super-dev your requirement` | `super-dev` |
| Trae SOLOCN | `super-dev: your requirement` | `super-dev` |

### Public Terminal Entry

```bash
super-dev
super-dev update
```

Run `super-dev` to open the installer and choose the target host there. `onboard --host`, `doctor`, and other CLI commands remain available for maintenance, but they are no longer the normal end-user path.

### Per-Host Usage Details

#### CLI Hosts

**Claude Code**

```bash
super-dev
```

Trigger location: launch Claude Code in the project directory, then trigger within the same session.
Trigger command: `/super-dev your requirement`
Fallback: `super-dev: your requirement`
Restart required after onboarding: No.

Notes:
1. Recommended as the primary CLI host.
2. If a maintainer needs to verify the installed surfaces, run `super-dev doctor --host claude-code` to confirm project-root `CLAUDE.md`, project `.claude/CLAUDE.md`, optional `.claude/settings*.json`, and project/user skills plus agents are active together.
3. Claude Code is now aligned to the official `CLAUDE.md + settings + project/user skills + subagents` model; `.claude/commands/` remains compatibility-only rather than the primary contract.
4. Super Dev can also install `.claude-plugin/marketplace.json` plus `plugins/super-dev-claude/.claude-plugin/plugin.json` as an optional repo-local Claude plugin enhancement.

**Codex**

```bash
super-dev
```

Trigger location: after onboarding, restart `codex`, then trigger in the new session.
Trigger command:
`Codex App/Desktop: choose super-dev from the / list`
`Codex CLI: $super-dev`
`Fallback: super-dev: your requirement`
Restart required after onboarding: Yes.

Notes:
1. In Codex app/desktop, prefer selecting `super-dev` directly from the `/` list; that is the enabled Skill entry, not a project-level custom slash command.
2. In Codex CLI, prefer explicit `$super-dev`.
3. If you are already continuing inside natural-language context, you can still use `super-dev: your requirement` as the AGENTS-driven fallback.
4. The default base surfaces are project `AGENTS.md` plus project `.agents/skills/super-dev/SKILL.md`; the official user-level Skill at `~/.agents/skills/super-dev/SKILL.md` is still installed, while `CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) is now only written when `--with-user-surfaces` is explicitly requested.
5. Super Dev also installs an optional repo-local Codex plugin enhancement at `.agents/plugins/marketplace.json` + `plugins/super-dev-codex/.codex-plugin/plugin.json` so Codex App/Desktop can expose a richer local plugin surface alongside AGENTS + Skills.
6. Older installations are migrated forward to the unified `super-dev` naming during upgrade.
7. If a previous session did not load the new surfaces, restart `codex` and try again.

**Gemini CLI**

```bash
super-dev
```

Trigger location: launch Gemini CLI in the project directory.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: No.

Notes:
1. The official primary model is now `GEMINI.md + settings + custom commands`; inside the project, check `GEMINI.md`, optional `.gemini/settings.json`, and `.gemini/commands/*.toml` first.
2. `/super-dev` is the injected Super Dev custom command, not a Gemini-native built-in command; if the command list has not refreshed, reopen the Gemini CLI session first.
3. `~/.gemini/skills/` is kept only as a compatibility enhancement, not as the default primary protocol surface.
4. Complete the full pipeline within a single session: research -> three documents -> user confirmation -> Spec -> frontend verification -> backend / delivery.

**Cursor CLI**

```bash
super-dev
```

Trigger location: launch Cursor CLI in the project directory.
Trigger command: `super-dev: your requirement`
Restart required after onboarding: No.

Notes:
1. Suitable for continuous research, documentation, and coding within the terminal.
2. The official project context model is project-root `AGENTS.md` + `.cursor/rules/`; root `CLAUDE.md` remains compatibility context only.
3. If project context or rules have not refreshed, reopen the Cursor CLI session; when resuming an existing workflow, prefer Cursor CLI's native session continuity instead of starting a new thread.

**Kiro CLI**

```bash
super-dev
```

Trigger location: launch Kiro CLI in the project directory.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: Yes.

Notes:
1. Kiro CLI now prefers the currently exposed `/super-dev` host entry; if the session only accepts natural language, fall back to `super-dev: your requirement`.
2. The official integration surfaces are `AGENTS.md` + `.kiro/steering/super-dev.md` + `.kiro/skills/super-dev/SKILL.md`; global steering and skills stay as optional enhancement surfaces.
3. Relaunch Kiro CLI after onboarding so steering context and skills load in the new session.

**OpenCode**

```bash
super-dev
```

Trigger location: launch OpenCode in the project directory.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: No.

Notes:
1. Uses CLI slash mode.
2. If you use a global command directory, keep the project-level onboarding files as well.

**Qoder CLI**

```bash
super-dev
```

Trigger location: launch Qoder CLI in the project directory.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: No.

Notes:
1. Suitable for command-line pipeline development.
2. If slash is not active, confirm that `AGENTS.md` and `.qoder/commands/super-dev.md` exist and that the `.qoder/rules/` directory has been created.
3. The official surfaces now use `AGENTS.md` + `.qoder/rules/super-dev.md` + `.qoder/commands/super-dev.md` + `.qoder/skills/` / `~/.qoder/AGENTS.md` + `~/.qoder/commands/` + `~/.qoder/skills/`; `.qoder/agents/` stays as an enhancement layer only.

**CodeBuddy CLI**

```bash
super-dev
```

Trigger location: launch CodeBuddy CLI in the project directory.
Trigger command: `/super-dev your requirement`
Competition mode: `/super-dev-seeai your competition brief`
Restart required after onboarding: No.

Notes:
1. Type the command directly in the current CLI session.
2. The official primary surfaces are `CODEBUDDY.md` + `.codebuddy/rules/` + `.codebuddy/commands/` + `.codebuddy/skills/` + `.codebuddy/agents/`, plus `~/.codebuddy/CODEBUDDY.md`.
3. If the session was opened before onboarding, reload project rules before triggering.
4. For hackathon-style work, prefer `/super-dev-seeai` so the host stays on the 30-minute fast path.

#### IDE Hosts

**Antigravity**

```bash
super-dev
```

Trigger location: open the Agent Chat / Prompt panel in Antigravity with the project workspace active.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: Yes.

Notes:
1. Uses the `GEMINI.md + custom commands` integration model, with `.agent/workflows` kept as the recommended enhancement layer.
2. Onboarding writes project-level `GEMINI.md`, `.gemini/commands/super-dev.toml`, and `.agent/workflows/super-dev.md`.
3. By default it only writes project-level `GEMINI.md` and project command surfaces; user-level `~/.gemini/GEMINI.md` and `~/.gemini/commands/` are only written when `--with-user-surfaces` is explicitly requested, while `~/.gemini/skills/` remains a compatibility enhancement only.
4. After onboarding, reopen Antigravity or start a new Agent Chat before triggering.

**Cursor IDE**

```bash
super-dev
```

Trigger location: open Agent Chat in Cursor with the target project as the active workspace.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: No.

Notes:
1. Complete the full pipeline within a single Agent Chat session.
2. If project rules did not load, reopen the workspace or start a new chat.

**Windsurf**

```bash
super-dev
```

Trigger location: open Agent Chat or the Workflow entry in Windsurf within the project context.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: No.

Notes:
1. Uses the `AGENTS.md + rules + workflow + skills` integration model.
2. Best suited for completing research, documents, Spec, and coding within a single Workflow.
3. The official docs expose `AGENTS.md`, `.windsurf/workflows/`, and `.windsurf/skills/`; the repo keeps `.windsurf/rules/` as the project constraint layer.

**Kiro IDE**

```bash
super-dev
```

Trigger location: open the Agent Chat / AI panel in Kiro IDE within the project context.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: Yes.

Notes:
1. Uses the currently exposed `/super-dev` host entry first; if the current session only accepts natural language, fall back to `super-dev: your requirement`.
2. Onboarding writes project-level `.kiro/steering/super-dev.md` and `.kiro/skills/super-dev/SKILL.md`, plus global `~/.kiro/steering/super-dev.md` and `~/.kiro/skills/super-dev/SKILL.md`; legacy `~/.kiro/steering/AGENTS.md` remains as a compatibility surface.
3. If steering or skills are not loaded, reopen the project window or start a new Agent Chat.

**Qoder IDE**

```bash
super-dev
```

Trigger location: open Agent Chat in Qoder IDE within the current project.
Trigger command: `/super-dev your requirement`
Restart required after onboarding: No.

Notes:
1. Uses the official `AGENTS.md + commands + rules + skills` project model; type `/super-dev your requirement` directly in Agent Chat.
2. If the new command does not appear, confirm `AGENTS.md`, `.qoder/commands/super-dev.md`, and `.qoder/rules/super-dev.md` exist, then reopen the project or start a new Agent Chat.
3. The official surfaces now use `AGENTS.md` + `.qoder/rules/super-dev.md` + `.qoder/commands/super-dev.md` + `.qoder/skills/` / `~/.qoder/AGENTS.md` + `~/.qoder/commands/` + `~/.qoder/skills/`; `.qoder/agents/` stays as an enhancement layer only.

**Trae IDE**

```bash
super-dev
```

Trigger location: open Agent Chat in Trae IDE within the current project context.
Trigger command: `super-dev: your requirement`
Restart required after onboarding: No.

Notes:
1. Uses `super-dev: your requirement` as the primary trigger.
2. By default onboarding writes project-level `.trae/project_rules.md` and `.trae/rules.md`; user-level `~/.trae/user_rules.md` and `~/.trae/rules.md` are only written with explicit `--with-user-surfaces`; if a compatible skill directory is detected, it also installs `~/.trae/skills/super-dev/SKILL.md`.
3. After onboarding, reopen Trae or start a new Agent Chat to activate rules; if the compatible Skill was installed, it activates as well.
4. Proceed using `output/*` and `.super-dev/changes/*/tasks.md`.

**CodeBuddy**

```bash
super-dev
```

Trigger location: open Agent Chat in CodeBuddy within the project context.
Trigger command: `/super-dev your requirement`
Competition mode: `/super-dev-seeai your competition brief`
Restart required after onboarding: No.

Notes:
1. Use within a project-level Agent Chat; do not leave the project context.
2. Let the host complete research before proceeding to documents and coding.
3. Uses `CODEBUDDY.md` + `.codebuddy/rules/super-dev/RULE.mdc` + `.codebuddy/commands/` + `.codebuddy/agents/` + `.codebuddy/skills/` integration surfaces.
4. For competition sprints, keep the same Agent Chat alive and avoid unnecessary sub-session switching.

**Copilot (VS Code) / Roo Code / Kilo Code / Cline**

These IDE hosts and desktop assistants all use the same pattern: run `super-dev` in the terminal, choose the target host in the installer, then trigger with `super-dev: your requirement` inside the host chat or workspace. No restart is required after onboarding unless the host says so.

```bash
super-dev
```

#### Droid CLI

Droid CLI uses Factory's official host surfaces rather than a separate plugin package.

**Integration surfaces:**
- `AGENTS.md`
- `.factory/rules/super-dev.md`
- `.factory/skills/super-dev/SKILL.md`
- `.factory/skills/super-dev-seeai/SKILL.md`
- compatibility enhancement: `.factory/commands/super-dev.md`, `.factory/commands/super-dev-seeai.md`
- user-level `~/.factory/AGENTS.md`, `~/.factory/commands/`, `~/.factory/skills/` (not written by default; only when `--with-user-surfaces` is explicitly requested)

**Installation:**
```bash
super-dev
```

Choose `Droid CLI` in the installer, then go back to the active Droid project session.

**Trigger:**
```text
/super-dev your requirement
```

Fallback:
```text
super-dev: your requirement
```

Competition mode:
```text
/super-dev-seeai your competition brief
```

Headless resume:
```bash
droid exec --session-id <id> "continue with next steps"
```

**Notes:**
1. Keep Droid in the same project session so it reuses the current workflow context instead of restarting.
2. `/super-dev-seeai` is the preferred SEEAI competition entry; use `super-dev-seeai:` only as a fallback.
3. Droid's primary official model is `AGENTS.md + .factory/rules + .factory/skills`; `.factory/commands/` remains a compatibility enhancement alongside that core model.

---

## Internal / Maintenance Surface

Support, governance, and advanced maintenance commands still exist, but they are no longer the public end-user path.

The public surface stays at:

- `super-dev`
- `super-dev update`
- `super-dev uninstall`
- `/super-dev ...`
- `/super-dev-seeai ...`
- `continue current flow`
- `what is the next step now`

Everything else should be treated as maintenance-only:

- `doctor / detect / onboard / skill / integrate` for host injection and validation
- `review / quality / release` for governance evidence and gate synchronization
- `spec / task` for maintainer-side change management

For interrupted work, prefer host-side recovery first:

- `continue current flow`
- `baseline confirmed, continue current flow`
- `docs confirmed, continue current flow`

---

## Documentation

- [Documentation overview](docs/README.md)
- [Quick start](docs/QUICKSTART.md)
- [Installation options](docs/INSTALL_OPTIONS.md)
- [Host usage guide](docs/HOST_USAGE_GUIDE.md)
- [Host capability audit](docs/HOST_CAPABILITY_AUDIT.md)
- [Host runtime validation matrix](docs/HOST_RUNTIME_VALIDATION.md)
- [Host install surfaces](docs/HOST_INSTALL_SURFACES.md)
- [Workflow guide](docs/WORKFLOW_GUIDE_EN.md)
- [Integration guide](docs/INTEGRATION_GUIDE.md)
- [Product audit](docs/PRODUCT_AUDIT.md)

**Execution principles:**

- The host is responsible for "writing code."
- `Super Dev` is responsible for "making the development process correct, complete, and auditable."

---

## License

[MIT](LICENSE)
