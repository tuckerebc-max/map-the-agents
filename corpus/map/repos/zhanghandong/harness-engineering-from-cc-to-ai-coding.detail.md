# zhanghandong/harness-engineering-from-cc-to-ai-coding -- full detail

[Back to orientation](harness-engineering-from-cc-to-ai-coding.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/f8a65556/d6452df1/e40e0feec02b90e308ccbfc7a8911d64118ccca0/62d8f458f85dc19c.json](../../../wiki/dossiers/f8a65556/d6452df1/e40e0feec02b90e308ccbfc7a8911d64118ccca0/62d8f458f85dc19c.json)

## specifications (4 claim(s))

- [observation/documented] The book is organized into seven main parts (architecture, prompt engineering, context management, prompt caching, security/permissions, advanced subsystems, lessons) plus four appendices. -- evidence: [README.md#L29-L29](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L29-L29), [README.md#L31-L37](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L31-L37) (`clm_dda0cc07a59f086ea92dae5bfcdba2ef43f33c0d1b81c3aa61e2b974b7711a21`)
- [observation/documented] The analysis is stated to be based on reverse-engineering 1,902 TypeScript source files of Claude Code v2.1.88. -- evidence: [docs/book-outline.md#L5-L5](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/book-outline.md#L5-L5) (`clm_48a928c702d8014b9b2d50e4885e749d886e6f4f04e44c00bc4acc0a92c4da21`)
- [observation/documented] Per the guide, v2.1.88 shipped a 57MB source map restoring 4,756 source files, while v2.1.89+ removed source-map distribution, forcing minified-bundle analysis. -- evidence: [docs/reverse-engineering-guide.md#L93-L93](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L93-L93), [docs/reverse-engineering-guide.md#L41-L44](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L41-L44) (`clm_02aecaeb9271b034db13d867fa67d5299431b856111694d93bf48d73dc68a73d`)
- [observation/documented] A comparison table reports v2.1.88 to v2.1.91 changes: cli.js grew ~115KB, tengu events went 827 to 860, environment variables 178 to 183, GrowthBook configs 17 to 18. -- evidence: [docs/reverse-engineering-guide.md#L237-L243](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L237-L243) (`clm_044d21217cc331a245272705b16a521986f4a86e87935dd140b675a111ce9c85`)

## components (1 claim(s))

- [observation/documented] The reverse-engineering guide documents helper scripts: scripts/extract-signals.sh for string-constant mining and scripts/cc-version-diff.sh for structured version-to-version diff reports. -- evidence: [docs/reverse-engineering-guide.md#L178-L185](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L178-L185), [docs/reverse-engineering-guide.md#L169-L169](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L169-L169), [docs/reverse-engineering-guide.md#L101-L101](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L101-L101), [docs/reverse-engineering-guide.md#L165-L165](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L165-L165), [docs/reverse-engineering-guide.md#L97-L97](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L97-L97) (`clm_98aca8401f700c9c2c2ba1cfabce9005f7a3833bcdb96c46e7e39e42506ae62a`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Local preview is done with 'mdbook build book' and 'mdbook serve book', serving by default at http://localhost:3000. -- evidence: [README.en.md#L35-L38](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L35-L38), [README.md#L54-L54](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L54-L54), [README.en.md#L42-L42](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L42-L42), [README.md#L47-L50](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L47-L50) (`clm_fed995223ea96b889c9e91ffb9df1ff3e2f56c990417d4965eb88759f5c39f9f`)
- [observation/documented] The repository intentionally tracks only files needed to publish the book to GitHub Pages; the English edition is a scaffolded preview while the Chinese edition is canonical. -- evidence: [README.md#L58-L61](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L58-L61), [README.en.md#L46-L48](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L46-L48), [README.en.md#L11-L11](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L11-L11) (`clm_6605f5458a680287f86491998a219d1f0474d1deccfba36fb67f1095c8d65b99`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] A dedicated chapter documents Claude Code's shortcomings as analyzed by the book, including cache fragility, compaction information loss, text-only Grep limits, silent truncation, and flag complexity. -- evidence: [docs/book-outline.md#L280-L285](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/book-outline.md#L280-L285) (`clm_7c5c23748563c3cb6a05adca042fcc1cb3bcab17fd6cd0d9041c937a2fba43db`)
- [inference/documented] The book explicitly disclaims official status: it is reverse-engineering-based research and does not represent Anthropic's official documentation or positions. -- evidence: [README.md#L58-L61](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L58-L61), [README.en.md#L46-L48](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L46-L48) (`clm_087e28555c753195be5df8bd27fe3875f05dcd4debaa7e20d3f4ee1bc8c774d6`)

## relevance (2 claim(s))

- [observation/documented] The repository publishes a Chinese technical book on Harness Engineering, analyzed from the publicly released Claude Code v2.1.88 package and its source-map reconstruction rather than official docs. -- evidence: [README.en.md#L9-L9](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L9-L9), [README.md#L11-L11](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L11-L11) (`clm_f7cca01e0c1bcb56006b8d6dc17cf8cf6d15811de0d5424c6c5680f10d414ba9`)
- [observation/documented] The book targets engineers building AI coding products, agent frameworks, and tool-calling platforms who want to understand Claude Code's implementation details. -- evidence: [README.md#L41-L43](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L41-L43), [README.en.md#L29-L31](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L29-L31) (`clm_cd71afbcb3deec8c95e4e59d0dabd8d819818183e0194c3bcfc008fa032cf803`)

