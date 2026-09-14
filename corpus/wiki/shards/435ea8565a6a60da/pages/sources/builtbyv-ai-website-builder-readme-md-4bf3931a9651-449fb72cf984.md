---
access: public
aliases: []
claim_ids:
- clm_1d293b1617c05ecf8e73fa7d445f9f7aa48324fa9654717751431ca838212628
- clm_5ecfda66643788cbca83a8d26a166050c88dd06ffbcf9fbcf256644776920b00
- clm_7814f9b76ea956666913fe24b81ba0ee02d6313d716f9c00484939aa17042547
- clm_7bc75820bf56c480a254d440b8da07007a327dd17f5f7da6c91f8765f0ab69a6
- clm_7ea59ec9e8d9c4a586ce5a70a054ab8db3434428028ce943a6ef2c5e98eeeb2a
- clm_8af309636e175abeca663ec767e671e775b114cb831886013aa8c90f18f85801
- clm_96b96ee1e5f785aee4017c8b8ebb6ce1b05d0237620946228bab77ef512378b0
- clm_b0ba9349ae106363fe9c38da878f1c62600cd98738cf090bc083a9d8913a6b64
- clm_b53a319ff95b8321980a828c1da93001de410b46492f6d0ada9723d13bf3b75b
- clm_db74edd13bdbd15b1c1b48141c9a5eaa990782568286b2e97917471bca1abf7f
maturity: draft
page_id: pg_17414ccb788b5f92a9c9449fb72cf984
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_07aa9ca346a552919566428262ed24de
title: builtbyV/ai-website-builder/README.md @ 4bf3931a9651
updated_at: '2026-09-14T03:39:55Z'
---

# builtbyV/ai-website-builder/README.md @ 4bf3931a9651

<!-- rcw:begin owner=source:src_07aa9ca346a552919566428262ed24de block=evidence -->
- The skill is described as fully self-contained, bundling the starter template, publish scripts, style guides, and the instructions the AI needs to build websites. [@claim:clm_1d293b1617c05ecf8e73fa7d445f9f7aa48324fa9654717751431ca838212628]
- The project is a website template intended to be built and updated through conversation with AI assistants, with users describing changes in their own language and no coding required. [@claim:clm_5ecfda66643788cbca83a8d26a166050c88dd06ffbcf9fbcf256644776920b00]
- The README lists Node.js and Git as requirements, notes a free hosting account is created only when ready to publish, and says launcher scripts can check for and guide installation of anything missing. [@claim:clm_7814f9b76ea956666913fe24b81ba0ee02d6313d716f9c00484939aa17042547]
- A one-line curl|bash installer places the skill in ~/.claude/skills/ai-website-builder/ and also into ~/.agents/skills/ai-website-builder/ if that directory already exists. [@claim:clm_7bc75820bf56c480a254d440b8da07007a327dd17f5f7da6c91f8765f0ab69a6]
- The documented workflow uses two terminals: one runs 'npm run dev' serving a preview at http://localhost:5173, the other starts the AI assistant via npx claude, npx codex, or npx gemini. [@claim:clm_7ea59ec9e8d9c4a586ce5a70a054ab8db3434428028ce943a6ef2c5e98eeeb2a]
- A setup.sh script checks the machine, installs the chosen AI CLI(s), completes setup, and provides a quick reference guide; launcher scripts for Windows (.bat), Mac (.app zip), and Linux (.sh) automate the flow including downloading the project and starting the assistant. [@claim:clm_8af309636e175abeca663ec767e671e775b114cb831886013aa8c90f18f85801]
- Supported AI assistants are Claude Code, OpenAI Codex CLI, and Google Gemini CLI; Gemini has a free tier, while Claude Code requires a Pro subscription or API key and Codex requires ChatGPT Plus or higher. [@claim:clm_96b96ee1e5f785aee4017c8b8ebb6ce1b05d0237620946228bab77ef512378b0]
- Publishing is triggered by telling the AI to publish; AGENTS.md maps platforms to npm scripts (publish:github, publish:cloudflare, publish:netlify, publish:vercel) with npm run deploy as an interactive menu fallback. [@claim:clm_b0ba9349ae106363fe9c38da878f1c62600cd98738cf090bc083a9d8913a6b64]
- The template appears to target static sites built with Vite and Tailwind, with publishing oriented toward free static hosts (GitHub Pages, Cloudflare Pages, Netlify, Vercel). [@claim:clm_b53a319ff95b8321980a828c1da93001de410b46492f6d0ada9723d13bf3b75b]
- For other tools, users can create tool-specific skills directories (e.g. ~/.agents/skills or ~/.gemini/skills, or project-local .claude/.agents/.cursor skills), or upload a skill ZIP via Claude.ai's Customize > Skills. [@claim:clm_db74edd13bdbd15b1c1b48141c9a5eaa990782568286b2e97917471bca1abf7f]
<!-- rcw:end owner=source:src_07aa9ca346a552919566428262ed24de block=evidence -->

## Researcher notes

