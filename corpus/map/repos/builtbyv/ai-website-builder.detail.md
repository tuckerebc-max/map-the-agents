# builtbyv/ai-website-builder -- full detail

[Back to orientation](ai-website-builder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/builtbyv/ai-website-builder/4bf3931a9651a5d0ba6ff60851bd402f24aec762/1e18c90010473fad.json](../../../wiki/dossiers/builtbyv/ai-website-builder/4bf3931a9651a5d0ba6ff60851bd402f24aec762/1e18c90010473fad.json)

## specifications (1 claim(s))

- [observation/documented] The project is a website template intended to be built and updated through conversation with AI assistants, with users describing changes in their own language and no coding required. -- evidence: [README.md#L7-L7](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L7-L7), [README.md#L3-L3](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L3-L3) (`clm_5ecfda66643788cbca83a8d26a166050c88dd06ffbcf9fbcf256644776920b00`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs the assistant to never start background processes, only check whether port 5173 is listening, and ask the user to run npm run dev themselves. -- evidence: [AGENTS.md#L17-L22](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L17-L22) (`clm_5b1c143f43d920eeda45cd8d5b016ae16762d06c5cf5c7d2ac219fb52ea4e395`)
- [observation/documented] Repository development practice: AGENTS.md forbids publishing without explicit confirmation and requires blocking publication if placeholders or broken essentials exist. -- evidence: [AGENTS.md#L7-L11](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L7-L11) (`clm_3a2d6838d3491b8bd35d87c5483a12a391c4eef8ad4442fa58b16c9e532f4339`)
- [observation/documented] Repository development practice: AGENTS.md restricts edits to index.html, additional HTML files, and /public assets, and prohibits editing setup-guide.html, AGENTS.md, CLAUDE.md, GEMINI.md, README.md, setup.sh, and QUICK_REFERENCE.txt. -- evidence: [AGENTS.md#L17-L22](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L17-L22) (`clm_d56f3a67301370c0d867233833018f4fab62dc0064ff952de86cc17d01ea264e`)
- [observation/documented] Repository development practice: AGENTS.md requires a pre-publish audit scanning all HTML except setup-guide.html for bracket placeholders, yourwebsite.com, placehold.co, and lorem ipsum, blocking publish until it passes. -- evidence: [AGENTS.md#L126-L128](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L126-L128), [AGENTS.md#L132-L134](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L132-L134), [AGENTS.md#L122-L122](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L122-L122), [AGENTS.md#L156-L156](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L156-L156) (`clm_5addb9e553c1a95ab5aba0ddbe50e40c35509498ba5e440e10ebe51a4f89d46a`)

## skills-patterns (3 claim(s))

- [observation/documented] A one-line curl|bash installer places the skill in ~/.claude/skills/ai-website-builder/ and also into ~/.agents/skills/ai-website-builder/ if that directory already exists. -- evidence: [README.md#L39-L39](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L39-L39), [README.md#L41-L43](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L41-L43) (`clm_7bc75820bf56c480a254d440b8da07007a327dd17f5f7da6c91f8765f0ab69a6`)
- [observation/documented] The skill is described as fully self-contained, bundling the starter template, publish scripts, style guides, and the instructions the AI needs to build websites. -- evidence: [README.md#L59-L59](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L59-L59) (`clm_1d293b1617c05ecf8e73fa7d445f9f7aa48324fa9654717751431ca838212628`)
- [observation/documented] For other tools, users can create tool-specific skills directories (e.g. ~/.agents/skills or ~/.gemini/skills, or project-local .claude/.agents/.cursor skills), or upload a skill ZIP via Claude.ai's Customize > Skills. -- evidence: [README.md#L47-L51](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L47-L51), [README.md#L55-L57](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L55-L57) (`clm_db74edd13bdbd15b1c1b48141c9a5eaa990782568286b2e97917471bca1abf7f`)

## interfaces (1 claim(s))

- [observation/documented] The documented workflow uses two terminals: one runs 'npm run dev' serving a preview at http://localhost:5173, the other starts the AI assistant via npx claude, npx codex, or npx gemini. -- evidence: [README.md#L319-L319](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L319-L319), [README.md#L313-L317](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L313-L317), [README.md#L304-L304](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L304-L304), [README.md#L297-L300](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L297-L300) (`clm_7ea59ec9e8d9c4a586ce5a70a054ab8db3434428028ce943a6ef2c5e98eeeb2a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] A setup.sh script checks the machine, installs the chosen AI CLI(s), completes setup, and provides a quick reference guide; launcher scripts for Windows (.bat), Mac (.app zip), and Linux (.sh) automate the flow including downloading the project and starting the assistant. -- evidence: [README.md#L84-L90](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L84-L90), [README.md#L68-L70](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L68-L70), [README.md#L162-L166](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L162-L166), [README.md#L73-L76](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L73-L76), [README.md#L79-L82](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L79-L82) (`clm_8af309636e175abeca663ec767e671e775b114cb831886013aa8c90f18f85801`)
- [observation/documented] Publishing is triggered by telling the AI to publish; AGENTS.md maps platforms to npm scripts (publish:github, publish:cloudflare, publish:netlify, publish:vercel) with npm run deploy as an interactive menu fallback. -- evidence: [README.md#L343-L347](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L343-L347), [AGENTS.md#L193-L198](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L193-L198), [README.md#L323-L326](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L323-L326) (`clm_b0ba9349ae106363fe9c38da878f1c62600cd98738cf090bc083a9d8913a6b64`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The README lists Node.js and Git as requirements, notes a free hosting account is created only when ready to publish, and says launcher scripts can check for and guide installation of anything missing. -- evidence: [README.md#L101-L105](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L101-L105), [README.md#L107-L107](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L107-L107) (`clm_7814f9b76ea956666913fe24b81ba0ee02d6313d716f9c00484939aa17042547`)
- [observation/documented] Supported AI assistants are Claude Code, OpenAI Codex CLI, and Google Gemini CLI; Gemini has a free tier, while Claude Code requires a Pro subscription or API key and Codex requires ChatGPT Plus or higher. -- evidence: [README.md#L10-L12](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L10-L12), [README.md#L411-L415](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L411-L415) (`clm_96b96ee1e5f785aee4017c8b8ebb6ce1b05d0237620946228bab77ef512378b0`)

## limitations (1 claim(s))

- [inference/documented] The template appears to target static sites built with Vite and Tailwind, with publishing oriented toward free static hosts (GitHub Pages, Cloudflare Pages, Netlify, Vercel). -- evidence: [README.md#L338-L341](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/README.md#L338-L341), [AGENTS.md#L1-L1](https://github.com/builtbyV/ai-website-builder/blob/4bf3931a9651a5d0ba6ff60851bd402f24aec762/AGENTS.md#L1-L1) (`clm_b53a319ff95b8321980a828c1da93001de410b46492f6d0ada9723d13bf3b75b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

