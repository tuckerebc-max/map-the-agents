---
access: public
aliases: []
claim_ids:
- clm_39b5fcfaada4b64bf4ec4387e637a506b658bf8c101eb77f0ce2a024f6c9c6b8
- clm_458ab9d8876580755cdb588d524874b34cde4d4ed3ab7ad9e47808a620c1d784
- clm_540ff36e8eb299c92a09c4cedce5d63d92111d817d2a752fb66ba5951c3cbefd
- clm_b933783ad3c597cb134ee41a179cfa720cc3690c750888bfab7e21fb8c8e416c
- clm_e0c8641dd010089b5af8923fe8461fa10212ace4fa4856fd322141dc66a96399
maturity: draft
page_id: pg_94d0dda12b2756d4ae66844ccb0bb8cd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d236a3c7f2595a1d848e6a85478f5cd0
title: rawwerks/recursive-coding-agents/DEVELOPING.md @ 0c71127a731c
updated_at: '2026-09-14T04:18:23Z'
---

# rawwerks/recursive-coding-agents/DEVELOPING.md @ 0c71127a731c

<!-- rcw:begin owner=source:src_d236a3c7f2595a1d848e6a85478f5cd0 block=evidence -->
- Repository development practice: slide content is authored as mdsvex files in web/src/slides/ with ordering controlled by order.ts, and slides support metadata props like label, variant, alt, align, and background. [@claim:clm_39b5fcfaada4b64bf4ec4387e637a506b658bf8c101eb77f0ce2a024f6c9c6b8]
- Repository development practice: production deploys go through a checked scripts/deploy-web.sh wrapper or wrangler, require maintainer Cloudflare authentication, and tokens must never be passed on command lines. [@claim:clm_458ab9d8876580755cdb588d524874b34cde4d4ed3ab7ad9e47808a620c1d784]
- Repository development practice: pre-commit hooks run gitleaks on staged changes, and pre-push hooks only remind maintainers that deploys are explicit; hooks are activated via core.hooksPath. [@claim:clm_540ff36e8eb299c92a09c4cedce5d63d92111d817d2a752fb66ba5951c3cbefd]
- Repository development practice: contributors run bun-based checks from web/ including svelte-check, design, social-metadata, and theme tests, plus a production build. [@claim:clm_b933783ad3c597cb134ee41a179cfa720cc3690c750888bfab7e21fb8c8e416c]
- The web project appears to depend on SvelteKit with mdsvex slides and the @sveltejs/adapter-cloudflare adapter, built with the bun toolchain. [@claim:clm_e0c8641dd010089b5af8923fe8461fa10212ace4fa4856fd322141dc66a96399]
<!-- rcw:end owner=source:src_d236a3c7f2595a1d848e6a85478f5cd0 block=evidence -->

## Researcher notes

