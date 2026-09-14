# thixpin/agentic-coding-basic -- full detail

[Back to orientation](agentic-coding-basic.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/thixpin/agentic-coding-basic/e295e241a981e932c4551d8835ff4665bc4bcdcc/2df949f3ce3ec51c.json](../../../wiki/dossiers/thixpin/agentic-coding-basic/e295e241a981e932c4551d8835ff4665bc4bcdcc/2df949f3ce3ec51c.json)

## specifications (2 claim(s))

- [observation/documented] The repository is a Burmese-language tutorial book on agentic coding with Claude Code, aimed at junior/noob developers, using a mini ecommerce project as its running example. -- evidence: [README.md#L18-L18](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L18-L18), [README.md#L22-L22](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L22-L22) (`clm_70fd6c687dbf13f388a44c2d20160d58218c653d6112e6a15190bcc184941e13`)
- [observation/documented] The tutorial project 'Mya Ri Store' is a buyer flow: product list, cart, checkout form (name/phone/address), order summary, then sending a screenshot to the seller via Viber. -- evidence: [README.md#L28-L31](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L28-L31) (`clm_2928fab7759433a4cf13333b8314528515f69ccc28bf9ba07db36fda082db478`)

## components (1 claim(s))

- [observation/documented] The book has nine chapters in markdown files under chapters/, covering topics from what agentic coding is, to Claude Code setup, instructing agents, skills, and context/token economy. -- evidence: [README.md#L37-L47](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L37-L47) (`clm_448a0f949b88114c5c148a342bbae10c5976fcaf6c01c6b0c4ca647435318908`)

## design-choices (1 claim(s))

- [observation/documented] The tutorial project is built with React, Vite, and Tailwind CSS, and is designed to run without a backend or rented server. -- evidence: [README.md#L33-L33](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L33-L33), [README.md#L26-L26](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L26-L26) (`clm_2f18a496d3eb97a131a2c0662c6f7592ce4ad692b3c807ad97e401c98573c2c3`)

## workflows (2 claim(s))

- [observation/documented] A build.sh script at the repo root produces EPUB and PDF outputs (both, or either alone) into dist/, with named files agentic-coding-basic-mm.epub and .pdf. -- evidence: [README.md#L66-L70](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L66-L70), [README.md#L72-L72](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L72-L72), [README.md#L74-L77](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L74-L77) (`clm_ee1b3433bfd2e77a5ceae912a79c1e6153fd320c9fc3336abd6c5c90b24175f3`)
- [observation/documented] On first run, build.sh creates a Python venv at build/venv, installs markdown and fonttools, embeds the Noto Sans Myanmar font, and assembles chapters into EPUB/PDF. -- evidence: [README.md#L79-L79](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L79-L79) (`clm_5292c039a5207c5dcf1fdb723ce95fd3be4b5c0f15b1f89605a30fca2d005d08`)

## skills-patterns (1 claim(s))

- [observation/documented] Chapter 7 covers building reusable Skills, including SKILL.md structure and three ways to reuse them. -- evidence: [README.md#L37-L47](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L37-L47) (`clm_d5d7beab0b47387ca94e676d5741acf677f94281b5194d07964cd9a227923065`)

## interfaces (1 claim(s))

- [observation/documented] Chapter 3 teaches instructing agents via CLAUDE.md, Plan Mode, and prompt-writing style. -- evidence: [README.md#L37-L47](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L37-L47) (`clm_a6f9f818e3822c35cd4bc35d4e5f19dfc582fdb69aa3f6ce65364a21a0f0cfa8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] Building the book requires python3 and a Chromium-based browser for PDF generation, with an optional CHROME environment variable pointing to the browser path. -- evidence: [README.md#L83-L85](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L83-L85) (`clm_44f896373e747c4873f6fe377b2be43a8334bd89a0ac492dab2c1a458bc0efc1`)
- [observation/documented] Readers need a computer (macOS/Windows/Linux), Claude Code with a Pro/Max/Team/Enterprise plan or Console account, Node.js v18 or later, and basic Git knowledge. -- evidence: [README.md#L57-L60](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L57-L60) (`clm_3c73358b899a5e1ea0f25aa8e8224da5d5a60523008c216eaa4196b1d5a05cf2`)
- [observation/documented] The repository is MIT licensed (Copyright 2026 Soe Thura), while the embedded Noto Sans Myanmar font is under the SIL Open Font License. -- evidence: [README.md#L93-L93](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L93-L93), [README.md#L95-L95](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L95-L95) (`clm_af090a3be29dd645e65694cb1f780a5ad10ed32e494ac51d519106edee0221cb`)

## limitations (1 claim(s))

- [observation/documented] The build script targets macOS by default because it uses the system-installed Noto Sans Myanmar font; on other OSes the regular and bold TTF files must be placed manually in build/. -- evidence: [README.md#L83-L85](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L83-L85) (`clm_6a6ca2e2bb999fc5f0ed52acb8a07b427c43f753c5e3441aa6e4b21c5266987e`)

## relevance (1 claim(s))

- [observation/documented] The book is positioned as a lightweight bootstrap for beginners, not a path to full mastery, and points to the author's PitWay project for deeper engineering-workflow topics. -- evidence: [README.md#L89-L89](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L89-L89), [README.md#L22-L22](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L22-L22) (`clm_6b2fd738bc4fe0a75f7db723938903c93e8fd3f1120e34204594f1db4993f167`)

