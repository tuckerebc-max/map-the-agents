# Real World Rails

This repository contains 200+ production open source Rails applications and engines as git submodules.

- `apps/` — Full source code of Rails applications (Discourse, Mastodon, GitLab, Gumroad, Chatwoot, Spree, Solidus, Canvas LMS, and many more)
- `engines/` — Rails engines (Blazer, PgHero, Ahoy, Chartkick, Thredded, etc.)
- `repos.md` — Full list with descriptions
- `analyses/` — Git-ignored directory for local research (not committed)

## How to use this repo

Search across all apps to find how production codebases implement patterns. For example:

- Grep for gem usage: search `Gemfile.lock` files across `apps/`
- Find model patterns: search `app/models/` across all apps
- Compare approaches: look at how multiple apps solve the same problem
- Study migrations, concerns, service objects, jobs, mailers, etc.

## Key details

- Submodules point to specific commits; run `bin/update` to get the latest
- Some apps are very large (GitLab, Canvas LMS, Discourse) — searches may take time
- The `analyses/` directory is git-ignored for storing local research
