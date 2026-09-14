# aeonfun/aeon

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 95142d19705c @ 76226e8365f601b0

## Summary (orientation draft, not independently verified)

The snapshot documents the Aeon Developer Kit (ADK): a GitHub-App-based integration pattern for building products on top of Aeon instances (which are GitHub repos plus Actions), a skill/capability taxonomy with a runtime read-only enforcement tier, and a changelog describing skills, harnesses, and notification plumbing. Evidence coverage: 123 of 390 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 12 of 39 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The ./notify tool writes a structured JSON payload to a queue, and a post-run scripts/notify-deliver.sh is the only place channel tokens are consumed, rendering per channel (Telegram, Discord, Slack, Buzz) with per-send audit lines. -- evidence: [CHANGELOG.md#L104-L346](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/CHANGELOG.md#L104-L346)
  - [observation/documented] Aeon dispatches to ten coding-agent CLIs via a run-harness contract, including Cursor, Hermes, GLM, and Vercel's fx, with credentials surfaced as dashboard Access Keys rows. -- evidence: [CHANGELOG.md#L66-L102](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/CHANGELOG.md#L66-L102)
- design-choices (2 claim(s)):
  - [observation/documented] The ADK recommends a GitHub App over personal access tokens: no credential custody, least-privilege fixed permissions, instant revocation on uninstall, and free multi-tenancy since GitHub tracks installations. -- evidence: [docs/ADK.md#L50-L53](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L50-L53)
  - [observation/documented] Tenant isolation requires re-verifying with the user's token on every request that they still have access to the stored installation/repo, because otherwise any authenticated user could drive someone else's agent. -- evidence: [docs/ADK.md#L135-L135](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L135-L135), [docs/ADK.md#L124-L124](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L124-L124)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: adding a new capability value requires one PR updating the taxonomy doc, the schema reference, and the install-skill-pack allow-list constant, enforced by a ci-capabilities-parity workflow that fails when the three disagree. -- evidence: [docs/CAPABILITIES.md#L121-L121](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L121-L121), [docs/CAPABILITIES.md#L117-L119](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/CAPABILITIES.md#L117-L119)
  - [observation/documented] Repository development practice: pack authors can pre-flight locally with scripts/validate-pack.sh from an Aeon checkout, and listing requires a PR adding a README Community Packs row plus a catalog/skill-packs.json entry. -- evidence: [docs/ADK.md#L320-L322](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L320-L322)
- skills-patterns (2 claim(s)):
  - [observation/documented] A skill is a single Markdown file with frontmatter (name, description, category, requires, var, mode) plus a prompt; there is no plugin API or compilation step. -- evidence: [docs/ADK.md#L262-L271](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L262-L271), [docs/ADK.md#L260-L260](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L260-L260)
  - [observation/documented] Skill packs are published in their own repo with a skills-pack.json manifest; the installer security-scans each SKILL.md, records provenance in skills.lock, and registers skills disabled so the operator remains the trust boundary. -- evidence: [docs/ADK.md#L330-L330](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L330-L330), [docs/ADK.md#L288-L288](https://github.com/aeonfun/aeon/blob/95142d19705ca379815e7fc9493a497ee0504e8d/docs/ADK.md#L288-L288)
- interfaces (4 claim(s)):
More evidence: [full detail](aeon.detail.md)

Metadata and full claim list: [full detail](aeon.detail.md)
Human notes ([notes](aeon.notes.md), never overwritten by build)

[Back to map index](../../index.md)
