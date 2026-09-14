# jcodesmore/ai-website-cloner-template -- full detail

[Back to orientation](ai-website-cloner-template.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jcodesmore/ai-website-cloner-template/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/62fbb0920530124a.json](../../../wiki/dossiers/jcodesmore/ai-website-cloner-template/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/62fbb0920530124a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md is the single source of truth for agent instructions; scripts/sync-agent-rules.sh and scripts/sync-skills.mjs regenerate platform-specific copies, and CLAUDE.md/GEMINI.md import AGENTS.md. -- evidence: [README.md#L196-L196](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L196-L196), [README.md#L203-L203](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L203-L203), [GEMINI.md#L1-L1](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/GEMINI.md#L1-L1), [README.md#L198-L201](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L198-L201), [README.md#L149-L175](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L149-L175) (`clm_cc5140e0b7097647a709261cee312af234132f18ada63181e6a0cd041829198d`)
- [observation/documented] Repository development practice: contributors run npm run dev/build/lint/typecheck/check, and Docker users can run the app or dev mode on port 3001 via docker compose. -- evidence: [README.md#L189-L192](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L189-L192), [README.md#L179-L185](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L179-L185) (`clm_7713799186334ef82c44617c7cc8c305a93dce9fdbad4e101d9bb8c001d9209c`)
- [observation/documented] Repository development practice: AGENTS.md instructs agents that this Next.js version has breaking changes and to read bundled docs in node_modules/next/dist/docs/ before writing code; the block is re-added by next dev. -- evidence: [AGENTS.md#L5-L5](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/AGENTS.md#L5-L5), [AGENTS.md#L7-L7](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/AGENTS.md#L7-L7) (`clm_f3d87e2b9002e1a8ddce800c4c44f532b2ee04a293bcdde7dc49b558e401f9a7`)
- [observation/documented] Repository development practice: code style rules include TypeScript strict with no any, named exports, Tailwind utility classes without inline styles, 2-space indentation, and mobile-first responsive design. -- evidence: [AGENTS.md#L31-L35](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/AGENTS.md#L31-L35) (`clm_9fea65200e655fec4a48fc9ec744f63253b3794aad7c70d19cf5b428759944d7`)

## skills-patterns (2 claim(s))

- [observation/documented] The template provides a /clone-website skill that runs a multi-phase pipeline: reconnaissance, foundation, component specs, parallel build, and assembly with QA. -- evidence: [README.md#L117-L117](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L117-L117), [README.md#L127-L131](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L127-L131), [README.md#L119-L125](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L119-L125) (`clm_2f9bcac516bed6ffbb4c6aca94e675ff63fe7aa921ca25898c2a16be956caa7a`)
- [observation/documented] Each builder agent receives the full component specification inline, including exact getComputedStyle() values, interaction models, multi-state content, breakpoints, and asset paths. -- evidence: [README.md#L133-L133](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L133-L133) (`clm_0a32e741f42fa393f8ee16b7c0e80be316102b78fcb1b07d9e552302a2887f94`)

## interfaces (1 claim(s))

- [observation/documented] The skill is invoked as /clone-website <target-url1> [<target-url2> ...]; clients that activate skills via natural language accept a phrasing like 'Clone <target-url> using the clone-website workflow'. -- evidence: [README.md#L83-L83](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L83-L83), [README.md#L69-L81](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L69-L81) (`clm_546cb1170bc17b24351ba8bd52a70aad077cc8b1814c020cc3ec909903d228a9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] During the parallel-build phase, builder agents are dispatched in git worktrees, one per section or component, and later merged during assembly. -- evidence: [README.md#L127-L131](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L127-L131) (`clm_bf5528087e0968b4b4128db77023e9ef928106830b2a712126fd204ab690189a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The scaffolded stack is Next.js 16 (App Router, React 19, TypeScript strict), shadcn/ui with Radix primitives, Tailwind CSS v4 with oklch tokens, and Lucide React icons; Node.js 24+ is a prerequisite. -- evidence: [AGENTS.md#L17-L21](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/AGENTS.md#L17-L21), [README.md#L110-L113](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L110-L113), [README.md#L105-L106](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L105-L106) (`clm_ff33e314ee2f04f198b39a38cd20eedeaef7e109616e9f488193793f2905eaa2`)

## limitations (1 claim(s))

- [observation/documented] The project explicitly states it must not be used for phishing, impersonation, passing off others' designs, or violating sites' terms of service regarding scraping or reproduction. -- evidence: [README.md#L143-L145](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L143-L145) (`clm_5ccf2c19cdbe8db5522c36985f55b0114a5d9e62cf22940674ba50f54392f894`)

## relevance (1 claim(s))

- [observation/documented] Stated use cases are migrating sites from WordPress/Webflow/Squarespace to Next.js, recovering lost source for live sites, and learning how production sites implement layouts and animations. -- evidence: [README.md#L137-L139](https://github.com/JCodesMore/ai-website-cloner-template/blob/92872bc40ced2c5edb4d5dc9fd3970d40c77f4ca/README.md#L137-L139) (`clm_79ef548ad5a9fdd5b006f3fada7ff3124eb36286ba116ffe0b7b15ddbf94410f`)

