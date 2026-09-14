# thixpin/agentic-coding-basic

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e295e241a981 @ 2df949f3ce3ec51c

## Summary (orientation draft, not independently verified)

This repository is a Burmese-language tutorial book ('Agentic Coding Basic for Junior Developers') teaching agentic coding with Claude Code by building a mini ecommerce site, with a build script producing EPUB/PDF. Evidence is mostly README documentation; no product runtime code is shown.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The repository is a Burmese-language tutorial book on agentic coding with Claude Code, aimed at junior/noob developers, using a mini ecommerce project as its running example. -- evidence: [README.md#L18-L18](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L18-L18), [README.md#L22-L22](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L22-L22)
  - [observation/documented] The tutorial project 'Mya Ri Store' is a buyer flow: product list, cart, checkout form (name/phone/address), order summary, then sending a screenshot to the seller via Viber. -- evidence: [README.md#L28-L31](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L28-L31)
- components (1 claim(s)):
  - [observation/documented] The book has nine chapters in markdown files under chapters/, covering topics from what agentic coding is, to Claude Code setup, instructing agents, skills, and context/token economy. -- evidence: [README.md#L37-L47](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L37-L47)
- design-choices (1 claim(s)):
  - [observation/documented] The tutorial project is built with React, Vite, and Tailwind CSS, and is designed to run without a backend or rented server. -- evidence: [README.md#L33-L33](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L33-L33), [README.md#L26-L26](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L26-L26)
- workflows (2 claim(s)):
  - [observation/documented] A build.sh script at the repo root produces EPUB and PDF outputs (both, or either alone) into dist/, with named files agentic-coding-basic-mm.epub and .pdf. -- evidence: [README.md#L66-L70](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L66-L70), [README.md#L72-L72](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L72-L72), [README.md#L74-L77](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L74-L77)
  - [observation/documented] On first run, build.sh creates a Python venv at build/venv, installs markdown and fonttools, embeds the Noto Sans Myanmar font, and assembles chapters into EPUB/PDF. -- evidence: [README.md#L79-L79](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L79-L79)
- skills-patterns (1 claim(s)):
  - [observation/documented] Chapter 7 covers building reusable Skills, including SKILL.md structure and three ways to reuse them. -- evidence: [README.md#L37-L47](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L37-L47)
- interfaces (1 claim(s)):
  - [observation/documented] Chapter 3 teaches instructing agents via CLAUDE.md, Plan Mode, and prompt-writing style. -- evidence: [README.md#L37-L47](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L37-L47)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] Building the book requires python3 and a Chromium-based browser for PDF generation, with an optional CHROME environment variable pointing to the browser path. -- evidence: [README.md#L83-L85](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L83-L85)
  - [observation/documented] Readers need a computer (macOS/Windows/Linux), Claude Code with a Pro/Max/Team/Enterprise plan or Console account, Node.js v18 or later, and basic Git knowledge. -- evidence: [README.md#L57-L60](https://github.com/thixpin/agentic-coding-basic/blob/e295e241a981e932c4551d8835ff4665bc4bcdcc/README.md#L57-L60)
- limitations (1 claim(s)):
More evidence: [full detail](agentic-coding-basic.detail.md)

Metadata and full claim list: [full detail](agentic-coding-basic.detail.md)
Human notes ([notes](agentic-coding-basic.notes.md), never overwritten by build)

[Back to map index](../../index.md)
