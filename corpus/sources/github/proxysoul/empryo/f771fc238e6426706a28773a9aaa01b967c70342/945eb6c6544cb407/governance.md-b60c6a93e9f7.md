# Governance

SoulForge is a single-maintainer open-source project. This document explains how decisions get made.

## Maintainer

@proxysoul owns:

- Product direction and roadmap
- Architecture decisions (agent design, intelligence layer, prompts, context strategy)
- Release cadence and version numbers
- Final say on every merged PR
- License interpretation and commercial license issuance

## Decision-making

| Type of change | How it lands |
|---|---|
| Bug fix | Open a PR; maintainer reviews and merges |
| Provider adapter | Open a PR; maintainer reviews and merges |
| UI / theme / docs | Open a PR; maintainer reviews and merges |
| Tool improvement (no architecture change) | Open a PR; maintainer reviews and merges |
| New feature touching only "open" paths | Open an issue first to align; PR after |
| Architecture change | Open an issue **first**. Maintainer responds yes / no / "let's discuss". Skip this and the PR gets closed. |
| Public API / SDK change | Open an issue first; semver-stable contracts are not changed casually |
| Build / publish pipeline | Open an issue first; sensitive to source-map and identifier leaks |

The "open an issue first" rule exists to save your time. The maintainer would rather say "no, here's why" in 5 minutes than have you spend a weekend on a PR that won't land.

## Why strict architectural governance

SoulForge's value is in how the pieces fit together — agent loop, intelligence, context, prompts, memory. The maintainer needs to keep that vision coherent across many releases. Open-source contributions to architecture would fragment that vision and slow the project down.

This is the same model used by SQLite, Postgres, FreeBSD subsystems, the Linux kernel, aider, and most successful single-maintainer open-source projects.

CODEOWNERS enforces this on GitHub: PRs touching IP-sensitive paths require maintainer review and cannot self-merge.

## What "open source" means here

- **Visibility:** every line of source is on GitHub. You can read, audit, and learn from it.
- **Forkability:** you can fork the repo and patch it for yourself. BUSL-1.1 limits commercial redistribution for 4 years; converts to Apache 2.0 on March 15, 2030.
- **Contribution:** PRs welcome in the areas listed in [CONTRIBUTING.md](CONTRIBUTING.md). Architecture is single-maintainer.
- **Privacy:** SoulForge runs entirely on your machine. Your code is sent only to the LLM providers you choose. There is no SoulForge backend. See [PRIVACY.md](PRIVACY.md).

## License gates

| License | Use case |
|---|---|
| BUSL-1.1 (default) | Personal use, internal company use, non-redistribution. Free forever. |
| [Commercial license](COMMERCIAL_LICENSE.md) | Repackaging or reselling SoulForge as a commercial product or service during the BUSL period. Email proxysoul to inquire. |
| Apache 2.0 (auto-conversion) | All uses, after March 15, 2030. |

## Communication

- **Bug reports / feature requests:** [GitHub issues](https://github.com/proxysoul/soulforge/issues)
- **Security disclosures:** see [SECURITY.md](SECURITY.md)
- **Commercial license inquiries:** open a GitHub issue or contact via the email listed in COMMERCIAL_LICENSE.md
- **Discussion:** [GitHub Discussions](https://github.com/proxysoul/soulforge/discussions) (when enabled)

## Forking

You're free to fork. If your fork ships under a different name and respects BUSL-1.1, that's fine. If you want to maintain a permanent fork, that's also fine — but understand that upstream changes won't merge automatically and you take on the maintenance burden yourself.

If you're forking because a PR was rejected: this governance model means architecture rejections are intentional, not arbitrary. A fork that re-applies rejected architecture changes is welcome to exist; it's just not what SoulForge is.

## Future

This is a single-maintainer project today. If at some point a sustainable funding model materializes (sponsorships, commercial licenses, acquisition), governance may evolve — additional maintainers, a steering committee, or a non-profit foundation. Any such change will be announced clearly in advance.
