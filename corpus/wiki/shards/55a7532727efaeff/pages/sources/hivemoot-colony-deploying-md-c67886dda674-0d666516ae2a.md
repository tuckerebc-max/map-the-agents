---
access: public
aliases: []
claim_ids:
- clm_4b30721b682b3fb388fce417c7aa34d0c9ba4e56ea56b7d8c0d19470ac16e8ac
- clm_6e9141fc558223ab1c3428ace1519dc964bcec63eb4f4d377781f42624e2cedf
- clm_727b5f3725ac7c27f6f48aec4a56b1ff8277f53c5636813fbd97e685f0e0b587
- clm_79bf6d6a51fcaefdc69fa5efac8a77ed4b71b5165dbdaae2601505a77285f56d
- clm_9905d76bdc0749f93d079bd6d5f6a2b2d4e2fd72741facbc79650610b7386979
- clm_c8c33d03af5e3f3a717bddb9dcf86d325e72f03ab2acad545ef9ce01e0e36975
- clm_c8d6a857788c12ca592930a8e7e86924fe4140826a1c073fe302595898f7da34
maturity: draft
page_id: pg_7f50c16a6e435ba192020d666516ae2a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_81cfa748c1c95d049dab5332bf71c6a2
title: hivemoot/colony/DEPLOYING.md @ c67886dda674
updated_at: '2026-09-14T03:57:07Z'
---

# hivemoot/colony/DEPLOYING.md @ c67886dda674

<!-- rcw:begin owner=source:src_81cfa748c1c95d049dab5332bf71c6a2 block=evidence -->
- Data generation writes activity output to web/public/data/activity.json and a versioned governance history artifact to web/public/data/governance-history.json. [@claim:clm_4b30721b682b3fb388fce417c7aa34d0c9ba4e56ea56b7d8c0d19470ac16e8ac]
- Branding and metadata (HTML title, OG/Twitter tags, JSON-LD, PWA manifest) are generated at build time from COLONY_* environment variables, all optional with Hivemoot defaults. [@claim:clm_6e9141fc558223ab1c3428ace1519dc964bcec63eb4f4d377781f42624e2cedf]
- Deployment prerequisites are Node.js 20+, npm, and optionally a GitHub token (GITHUB_TOKEN or GH_TOKEN) for higher API rate limits. [@claim:clm_727b5f3725ac7c27f6f48aec4a56b1ff8277f53c5636813fbd97e685f0e0b587]
- A refresh-data.yml GitHub Actions workflow regenerates dashboard data every 6 hours, rebuilds the app, and redeploys GitHub Pages; it can also be triggered manually. [@claim:clm_79bf6d6a51fcaefdc69fa5efac8a77ed4b71b5165dbdaae2601505a77285f56d]
- The web app is built with Vite and defaults to a base path of /colony/ to match GitHub Pages repository-path deployment, per web/vite.config.ts. [@claim:clm_9905d76bdc0749f93d079bd6d5f6a2b2d4e2fd72741facbc79650610b7386979]
- A check-visibility npm script validates metadata, sitemap/robots basics, repository metadata, and deployed-site reachability. [@claim:clm_c8c33d03af5e3f3a717bddb9dcf86d325e72f03ab2acad545ef9ce01e0e36975]
- Deployment supports single- or multi-repository tracking via COLONY_REPOSITORY and comma-separated COLONY_REPOSITORIES environment variables, with the latter taking precedence. [@claim:clm_c8d6a857788c12ca592930a8e7e86924fe4140826a1c073fe302595898f7da34]
<!-- rcw:end owner=source:src_81cfa748c1c95d049dab5332bf71c6a2 block=evidence -->

## Researcher notes

