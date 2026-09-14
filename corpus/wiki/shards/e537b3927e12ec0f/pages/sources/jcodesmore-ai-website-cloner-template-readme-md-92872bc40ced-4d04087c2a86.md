---
access: public
aliases: []
claim_ids:
- clm_0a32e741f42fa393f8ee16b7c0e80be316102b78fcb1b07d9e552302a2887f94
- clm_2f9bcac516bed6ffbb4c6aca94e675ff63fe7aa921ca25898c2a16be956caa7a
- clm_546cb1170bc17b24351ba8bd52a70aad077cc8b1814c020cc3ec909903d228a9
- clm_5ccf2c19cdbe8db5522c36985f55b0114a5d9e62cf22940674ba50f54392f894
- clm_7713799186334ef82c44617c7cc8c305a93dce9fdbad4e101d9bb8c001d9209c
- clm_79ef548ad5a9fdd5b006f3fada7ff3124eb36286ba116ffe0b7b15ddbf94410f
- clm_bf5528087e0968b4b4128db77023e9ef928106830b2a712126fd204ab690189a
- clm_cc5140e0b7097647a709261cee312af234132f18ada63181e6a0cd041829198d
- clm_ff33e314ee2f04f198b39a38cd20eedeaef7e109616e9f488193793f2905eaa2
maturity: draft
page_id: pg_d64b9ae37c845d878e4d4d04087c2a86
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0e69bacd42b955efa1ea7e508154f3a6
title: JCodesMore/ai-website-cloner-template/README.md @ 92872bc40ced
updated_at: '2026-09-14T04:00:21Z'
---

# JCodesMore/ai-website-cloner-template/README.md @ 92872bc40ced

<!-- rcw:begin owner=source:src_0e69bacd42b955efa1ea7e508154f3a6 block=evidence -->
- Each builder agent receives the full component specification inline, including exact getComputedStyle() values, interaction models, multi-state content, breakpoints, and asset paths. [@claim:clm_0a32e741f42fa393f8ee16b7c0e80be316102b78fcb1b07d9e552302a2887f94]
- The template provides a /clone-website skill that runs a multi-phase pipeline: reconnaissance, foundation, component specs, parallel build, and assembly with QA. [@claim:clm_2f9bcac516bed6ffbb4c6aca94e675ff63fe7aa921ca25898c2a16be956caa7a]
- The skill is invoked as /clone-website <target-url1> [<target-url2> ...]; clients that activate skills via natural language accept a phrasing like 'Clone <target-url> using the clone-website workflow'. [@claim:clm_546cb1170bc17b24351ba8bd52a70aad077cc8b1814c020cc3ec909903d228a9]
- The project explicitly states it must not be used for phishing, impersonation, passing off others' designs, or violating sites' terms of service regarding scraping or reproduction. [@claim:clm_5ccf2c19cdbe8db5522c36985f55b0114a5d9e62cf22940674ba50f54392f894]
- Repository development practice: contributors run npm run dev/build/lint/typecheck/check, and Docker users can run the app or dev mode on port 3001 via docker compose. [@claim:clm_7713799186334ef82c44617c7cc8c305a93dce9fdbad4e101d9bb8c001d9209c]
- Stated use cases are migrating sites from WordPress/Webflow/Squarespace to Next.js, recovering lost source for live sites, and learning how production sites implement layouts and animations. [@claim:clm_79ef548ad5a9fdd5b006f3fada7ff3124eb36286ba116ffe0b7b15ddbf94410f]
- During the parallel-build phase, builder agents are dispatched in git worktrees, one per section or component, and later merged during assembly. [@claim:clm_bf5528087e0968b4b4128db77023e9ef928106830b2a712126fd204ab690189a]
- Repository development practice: AGENTS.md is the single source of truth for agent instructions; scripts/sync-agent-rules.sh and scripts/sync-skills.mjs regenerate platform-specific copies, and CLAUDE.md/GEMINI.md import AGENTS.md. [@claim:clm_cc5140e0b7097647a709261cee312af234132f18ada63181e6a0cd041829198d]
- The scaffolded stack is Next.js 16 (App Router, React 19, TypeScript strict), shadcn/ui with Radix primitives, Tailwind CSS v4 with oklch tokens, and Lucide React icons; Node.js 24+ is a prerequisite. [@claim:clm_ff33e314ee2f04f198b39a38cd20eedeaef7e109616e9f488193793f2905eaa2]
<!-- rcw:end owner=source:src_0e69bacd42b955efa1ea7e508154f3a6 block=evidence -->

## Researcher notes

