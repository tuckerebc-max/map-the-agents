---
access: public
aliases: []
claim_ids:
- clm_3a2d6838d3491b8bd35d87c5483a12a391c4eef8ad4442fa58b16c9e532f4339
- clm_5addb9e553c1a95ab5aba0ddbe50e40c35509498ba5e440e10ebe51a4f89d46a
- clm_5b1c143f43d920eeda45cd8d5b016ae16762d06c5cf5c7d2ac219fb52ea4e395
- clm_b0ba9349ae106363fe9c38da878f1c62600cd98738cf090bc083a9d8913a6b64
- clm_b53a319ff95b8321980a828c1da93001de410b46492f6d0ada9723d13bf3b75b
- clm_d56f3a67301370c0d867233833018f4fab62dc0064ff952de86cc17d01ea264e
maturity: draft
page_id: pg_e9623b3b5e2553eb8ce76ea12882e8b3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d73b53017bcc530fb0cfd97497a40a52
title: builtbyV/ai-website-builder/AGENTS.md @ 4bf3931a9651
updated_at: '2026-09-14T03:39:55Z'
---

# builtbyV/ai-website-builder/AGENTS.md @ 4bf3931a9651

<!-- rcw:begin owner=source:src_d73b53017bcc530fb0cfd97497a40a52 block=evidence -->
- Repository development practice: AGENTS.md forbids publishing without explicit confirmation and requires blocking publication if placeholders or broken essentials exist. [@claim:clm_3a2d6838d3491b8bd35d87c5483a12a391c4eef8ad4442fa58b16c9e532f4339]
- Repository development practice: AGENTS.md requires a pre-publish audit scanning all HTML except setup-guide.html for bracket placeholders, yourwebsite.com, placehold.co, and lorem ipsum, blocking publish until it passes. [@claim:clm_5addb9e553c1a95ab5aba0ddbe50e40c35509498ba5e440e10ebe51a4f89d46a]
- Repository development practice: AGENTS.md instructs the assistant to never start background processes, only check whether port 5173 is listening, and ask the user to run npm run dev themselves. [@claim:clm_5b1c143f43d920eeda45cd8d5b016ae16762d06c5cf5c7d2ac219fb52ea4e395]
- Publishing is triggered by telling the AI to publish; AGENTS.md maps platforms to npm scripts (publish:github, publish:cloudflare, publish:netlify, publish:vercel) with npm run deploy as an interactive menu fallback. [@claim:clm_b0ba9349ae106363fe9c38da878f1c62600cd98738cf090bc083a9d8913a6b64]
- The template appears to target static sites built with Vite and Tailwind, with publishing oriented toward free static hosts (GitHub Pages, Cloudflare Pages, Netlify, Vercel). [@claim:clm_b53a319ff95b8321980a828c1da93001de410b46492f6d0ada9723d13bf3b75b]
- Repository development practice: AGENTS.md restricts edits to index.html, additional HTML files, and /public assets, and prohibits editing setup-guide.html, AGENTS.md, CLAUDE.md, GEMINI.md, README.md, setup.sh, and QUICK_REFERENCE.txt. [@claim:clm_d56f3a67301370c0d867233833018f4fab62dc0064ff952de86cc17d01ea264e]
<!-- rcw:end owner=source:src_d73b53017bcc530fb0cfd97497a40a52 block=evidence -->

## Researcher notes

