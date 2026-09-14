---
access: public
aliases: []
claim_ids:
- clm_0888bae78aa741eea48ad5ad94ea31dee9c41bd65c144ae803c415ba77e3c4bc
- clm_297fd424c4293b697b0488edd0dca0424eaa5bffa13bd248c7c67019f34c194b
- clm_51d6a420e0e1b20f861d93815e1c47247f735f39c311017e98d2b33a372e21ea
- clm_81ab657395e3d17ea77cc70b626d3f31cb3f7cc0dd0f3d3cf794bd25c5757a21
- clm_88f3d1edd2f0866f9424168848e72441ec09cc8163dd78f3a524dc2b4f5c8a7f
- clm_a2e502f09d390980e5d99721c1a5422a20b9cfce317980ab5257ae70908d0861
- clm_b21dc011cfc98509d5aa89a666bfb09f6923767b89f9e024f76cfb0bf53114bc
- clm_d6120aa7f01b74f2cb442a2b65f943e8d1c635691cf1f7aad770998e07db945b
- clm_db69156ca29eb549d34b91ea8aa2de0194f8bef28be4113c8d61f52485c8721f
- clm_e981837b2faee44f44077fa93abe9351b9b65066b03a127ca824682c976ab758
maturity: draft
page_id: pg_38ba26881c805838b8be6f3298110b05
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7fd982292abb53c8b52683c857ddee14
title: rustykuntz/clideck/README.md @ 2c381835565b
updated_at: '2026-09-14T02:37:44Z'
---

# rustykuntz/clideck/README.md @ 2c381835565b

<!-- rcw:begin owner=source:src_7fd982292abb53c8b52683c857ddee14 block=evidence -->
- Autopilot was removed because agents already have sub-agents, and mobile control was removed because harnesses provide their own remote access. [@claim:clm_0888bae78aa741eea48ad5ad94ea31dee9c41bd65c144ae803c415ba77e3c4bc]
- Built-in plugins include Git Changes, Supertonic Voice, Emoji, and Smart Dictation, and additional plugins can be built with a plugin SDK. [@claim:clm_297fd424c4293b697b0488edd0dca0424eaa5bffa13bd248c7c67019f34c194b]
- The CLI supports --port, --data-dir, and --help flags; CLIDECK_PORT or PORT also sets the port, and data is stored in ~/.clideck-next by default. [@claim:clm_51d6a420e0e1b20f861d93815e1c47247f735f39c311017e98d2b33a372e21ea]
- CliDeck runs Claude Code, Codex, Gemini CLI, OpenCode, Pi, and shell sessions in one browser window, grouped into projects, where each session is the agent's actual terminal with its own tools, configuration, and account. [@claim:clm_81ab657395e3d17ea77cc70b626d3f31cb3f7cc0dd0f3d3cf794bd25c5757a21]
- Sessions can be reopened and earlier conversations read, stopped sessions show last-used times, and session backups can be exported for recovery. [@claim:clm_88f3d1edd2f0866f9424168848e72441ec09cc8163dd78f3a524dc2b4f5c8a7f]
- CliDeck binds to localhost, and agent CLIs use their own network connections rather than going through CliDeck. [@claim:clm_a2e502f09d390980e5d99721c1a5422a20b9cfce317980ab5257ae70908d0861]
- After starting, the web UI is opened at http://127.0.0.1:4000; the tool can also be run via npx. [@claim:clm_b21dc011cfc98509d5aa89a666bfb09f6923767b89f9e024f76cfb0bf53114bc]
- CliDeck Ask lets agents send requests to other sessions and receive replies, including across providers; users type '@@' to find sessions, and agents discover teammates with 'clideck agents' and contact them with 'clideck ask'. [@claim:clm_d6120aa7f01b74f2cb442a2b65f943e8d1c635691cf1f7aad770998e07db945b]
- The product requires Node.js 22.12 or newer and an installed agent CLI, and is installed globally via npm as clideck@2. [@claim:clm_db69156ca29eb549d34b91ea8aa2de0194f8bef28be4113c8d61f52485c8721f]
- Agents open artifacts in preview tabs beside the terminal via 'clideck show', supporting Markdown, text, logs, JSON, HTML, PDFs, images, video, Mermaid diagrams, diffs, charts, and test results; users can also drop files onto the tab strip. [@claim:clm_e981837b2faee44f44077fa93abe9351b9b65066b03a127ca824682c976ab758]
<!-- rcw:end owner=source:src_7fd982292abb53c8b52683c857ddee14 block=evidence -->

## Researcher notes

