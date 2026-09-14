# Nerq Trust Score Analysis & Improvement Plan

> **Current Score**: 75.8/100 (B) — "Recommended for use"
> **Date**: 2026-03-23
> **Goal**: Reach 85+ (A rating)

---

## Score Breakdown

| Dimension | Score | Verdict |
|-----------|-------|---------|
| **Security** | 1/100 | Poor |
| **Maintenance** | 1/100 | Potentially abandoned |
| **Documentation** | 1/100 | Insufficient |
| **Compliance** | 79/100 | Broadly compliant |
| **Popularity** | 1/100 | Limited adoption |

The overall 75.8 is carried almost entirely by the Compliance score (79/100). The other four dimensions are scored at 1/100 each, which means the scoring system found **zero signals** to credit in those categories. This is a metadata/discoverability problem more than a quality problem.

---

## Is This Rating Accurate?

**Partially. The 1/100 scores reflect missing _signals_, not missing quality.**

CodeBuddy has real CI/CD, real tests, real security practices (env var sanitization, shell escaping, secret storage), a detailed README, and active development. But the automated scanners can't see what isn't surfaced through standard conventions.

### What Nerq Likely Checks

Nerq aggregates data from: npm/VS Code Marketplace registries, GitHub API, NVD, OSV.dev, and OpenSSF Scorecard. Each 1/100 score means the scrapers found almost nothing in the expected locations.

---

## Dimension-by-Dimension Audit

### 1. Security (1/100)

**What's missing (Nerq can't find):**

| Signal | Status | Impact |
|--------|--------|--------|
| `SECURITY.md` at repo root | MISSING | Nerq checks for responsible disclosure policy |
| Dependabot `.github/dependabot.yml` | MISSING | Automated vulnerability scanning |
| `npm audit` in CI pipeline | MISSING | No audit step in `workflow.yml` |
| OpenSSF Scorecard badge/workflow | MISSING | Industry-standard security benchmark |
| Code signing for VSIX | MISSING | Package integrity verification |
| Snyk/Socket integration | MISSING | External vulnerability DB |

**What exists but isn't visible to scanners:**

- Datadog static analysis config (`static-analysis.datadog.yml`) — **not wired into CI**
- ESLint with TypeScript rules — present but not a security-specific signal
- Shell injection prevention (`shell-escape.ts`) — internal, not discoverable
- Env var sanitization blocklist — internal, not discoverable
- Secret storage via VS Code `secretStorage` API — internal

**Verdict**: The Security score is unfairly low. The codebase has real security practices, but none of the standard _metadata_ signals exist for scanners to find.

---

### 2. Maintenance (1/100)

**What's missing:**

| Signal | Status | Impact |
|--------|--------|--------|
| CHANGELOG.md history | Only shows v2.0.0; package.json is at v4.2.1 | Scanners see no release history |
| GitHub Releases | Not checked — likely absent or sparse | Primary signal for release cadence |
| Issue/PR templates | `.github/ISSUE_TEMPLATE/` missing | Signals active project governance |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` missing | Signals structured contribution process |
| Version bump automation | No release scripts | Scanners look for release tooling |
| `bugs` field in package.json | MISSING | Links issue tracker for ecosystem tools |

**What exists but isn't credited:**

- Active commits (multiple per day based on this session alone)
- CI/CD on every PR (multi-OS: Ubuntu, macOS, Windows)
- Automated deploy on version tags
- 62 dependencies actively maintained

**Verdict**: The repo looks abandoned to scanners because there are no GitHub Releases and the CHANGELOG is stale. The actual development velocity is high — it just isn't surfaced through standard channels.

---

### 3. Documentation (1/100)

**What's missing:**

| Signal | Status | Impact |
|--------|--------|--------|
| CODE_OF_CONDUCT.md | MISSING | Standard open-source signal |
| API/reference docs site | MISSING | No generated docs (TypeDoc, etc.) |
| JSDoc/TSDoc coverage | Minimal (3 blocks in extension.ts) | Automated doc coverage tools find nothing |
| package.json `description` | Set to `"%description%"` (i18n placeholder) | Scanners see a literal string, not English |
| Badges in README | Only Nerq badge | No CI status, coverage, license, or version badges |

**What exists but isn't credited:**

- 851-line README with architecture, settings reference, troubleshooting
- CONTRIBUTING.md with fork/PR workflow
- 7-language i18n support (l10n bundles)
- Internal docs directory (4 architecture docs)
- 16 skill files with structured YAML frontmatter

**Verdict**: The README is genuinely comprehensive, but the description field is a placeholder string, there are no standard badges, no CODE_OF_CONDUCT, and no generated API docs. Scanners score what they can parse, and the i18n placeholder breaks the description signal.

---

### 4. Popularity (1/100)

| Signal | Current | Notes |
|--------|---------|-------|
| GitHub stars | 108 | Low compared to alternatives (LangChain: 100k+) |
| Forks | Not checked | Likely low |
| VS Code Marketplace installs | Unknown | May be the stronger signal |
| npm downloads | N/A (VS Code extension, not npm package) | |
| Ecosystem integrations | None detected | No "awesome" lists, no integrations page |

**Verdict**: This is the hardest dimension to improve short-term. 108 stars is real but low. Growth requires marketing, content, and community building — not code changes.

---

## Action Plan

### Tier 1: Quick Wins (1 day, biggest score impact)

These are metadata-only changes that directly address what scanners look for:

**1. Create `SECURITY.md`** at repo root
```markdown
# Security Policy

## Supported Versions
| Version | Supported |
|---------|-----------|
| 4.x     | Yes       |
| < 4.0   | No        |

## Reporting a Vulnerability
Please report security vulnerabilities via [GitHub Security Advisories](https://github.com/olasunkanmi-SE/codebuddy/security/advisories/new).
Do NOT open public issues for security vulnerabilities.

## Security Practices
- All secrets stored via VS Code secretStorage (encrypted)
- Shell command injection prevention via argument escaping
- Environment variable sanitization (blocklist for LD_PRELOAD, PATH, etc.)
- Dependency scanning via Dependabot (automated)
- Static analysis via Datadog SAST
```

**2. Add `.github/dependabot.yml`**
```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "npm"
    directory: "/webviewUi"
    schedule:
      interval: "weekly"
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
```

**3. Add `npm audit` step to CI workflow** (`workflow.yml`)
```yaml
- name: Security audit
  run: npm audit --audit-level=moderate
```

**4. Fix package.json `description` field** — replace the i18n placeholder with real English:
```json
"description": "An Autonomous AI Software Engineer for Visual Studio Code"
```

**5. Add `bugs` field to package.json**:
```json
"bugs": {
  "url": "https://github.com/olasunkanmi-SE/codebuddy/issues"
}
```

**6. Create `CODE_OF_CONDUCT.md`** — use the Contributor Covenant template

**7. Add standard badges to README.md** (CI status, license, version, marketplace):
```markdown
[![CI](https://github.com/olasunkanmi-SE/codebuddy/actions/workflows/workflow.yml/badge.svg)](https://github.com/olasunkanmi-SE/codebuddy/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/YourPublisher.codebuddy)](https://marketplace.visualstudio.com/items?itemName=YourPublisher.codebuddy)
```

---

### Tier 2: Medium Effort (1 week)

**8. Backfill CHANGELOG.md** — add entries for v2.0 through v4.2.1 with dates and highlights

**9. Create GitHub Releases** — tag and publish releases for recent versions with release notes

**10. Add issue and PR templates**:
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`

**11. Wire Datadog static analysis into CI** — add the SAST step to `workflow.yml`

**12. Add OpenSSF Scorecard GitHub Action**:
```yaml
- name: OpenSSF Scorecard
  uses: ossf/scorecard-action@v2
  with:
    results_file: results.sarif
    publish_results: true
```

**13. Increase JSDoc coverage** — add doc comments to public APIs in:
- `src/extension.ts` (activate, deactivate)
- `src/orchestrator.ts` (main orchestration methods)
- `src/services/skill/skill.service.ts` (public methods)

---

### Tier 3: Ongoing (improves Popularity)

**14. Publish to "awesome" lists** — submit to awesome-vscode, awesome-ai-tools

**15. Write blog posts / tutorials** — "Building an AI Code Assistant with LangGraph"

**16. Add VS Code Marketplace rich metadata** — gallery banner, Q&A enabled, categories

**17. Community engagement** — respond to issues promptly (Nerq tracks response times)

**18. GitHub Sponsors / FUNDING.yml** — signals active maintenance to scanners

---

## Expected Score Impact

| Action | Dimensions Affected | Estimated Lift |
|--------|---------------------|----------------|
| SECURITY.md + dependabot | Security | +20-30 |
| npm audit in CI | Security | +10-15 |
| Fix description + bugs field | Documentation, Maintenance | +5-10 |
| CODE_OF_CONDUCT + badges | Documentation | +10-15 |
| CHANGELOG + GitHub Releases | Maintenance | +20-30 |
| Issue/PR templates | Maintenance | +5-10 |
| OpenSSF Scorecard | Security | +10-20 |

**Projected score after Tier 1 + Tier 2**: ~85-90/100 (A rating)

The Compliance dimension is already at 79 and doesn't need attention. Popularity (108 stars) will grow organically as the other signals improve discoverability.

---

## Comparison with Alternatives

| Tool | Score | Why Higher |
|------|-------|------------|
| LangChain | 86.4/A | 100k+ stars, dedicated docs site, active releases, OpenSSF |
| OpenCode | 87.9/A | Full security policy, frequent releases, strong community |
| AutoGPT | 74.7/B | Similar gaps — proves stars alone don't fix this |
| Ollama | 73.8/B | Lower than CodeBuddy's potential post-fix |

AutoGPT has 160k+ stars but scores 74.7 — confirming that Nerq weights metadata signals heavily over raw popularity. CodeBuddy can surpass it with the metadata fixes alone.
