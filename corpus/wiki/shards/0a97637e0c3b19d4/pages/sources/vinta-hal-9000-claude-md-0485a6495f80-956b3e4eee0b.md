---
access: public
aliases: []
claim_ids:
- clm_0ef88ebf0d44464fb33be14314bcc850f864d5707c636241c40f4ef3f10a6116
- clm_943e46197059f388004f40a59903f617d0d84710857ddb792e0a432ec093ec05
maturity: draft
page_id: pg_8cfbcdb2f86a541696c9956b3e4eee0b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0baafc4bd7b25d7a99fd8922a4ba9907
title: vinta/hal-9000/CLAUDE.md @ 0485a6495f80
updated_at: '2026-09-14T04:30:04Z'
---

# vinta/hal-9000/CLAUDE.md @ 0485a6495f80

<!-- rcw:begin owner=source:src_0baafc4bd7b25d7a99fd8922a4ba9907 block=evidence -->
- Repository development practice: managed home-directory files must be edited under dotfiles/ (mapped via hal_dotfiles.json), and skills/plugins edits only go live after publishing with a version bump since Claude Code loads them from the GitHub marketplace. [@claim:clm_0ef88ebf0d44464fb33be14314bcc850f864d5707c636241c40f4ef3f10a6116]
- Repository development practice: contributors should use `make help` to find targets and prefer Makefile targets over running underlying tools directly; `make test` runs tests and `make hal-completion` regenerates zsh completion after editing bin/hal.py. [@claim:clm_943e46197059f388004f40a59903f617d0d84710857ddb792e0a432ec093ec05]
<!-- rcw:end owner=source:src_0baafc4bd7b25d7a99fd8922a4ba9907 block=evidence -->

## Researcher notes

