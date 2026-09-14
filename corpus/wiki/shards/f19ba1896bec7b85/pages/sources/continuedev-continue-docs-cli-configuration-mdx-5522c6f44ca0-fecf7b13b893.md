---
access: public
aliases: []
claim_ids:
- clm_41906ac0ec4c107b0537188a2ee3562a0c21a39a665fb5bf1dfd99a2dd56cc6b
- clm_674a2ff212bbf8940bc4e473505cab6f4e14bb849447d9e59682a44bf99ef4c9
- clm_eb9bd6021c717d81109cfea7204c6bdbf9dd32bfc05f15c807a07c72a106d138
- clm_f9793019a66b0a2c3af655f952dc21515f4050463a82f67fa81f4793e5939c12
maturity: draft
page_id: pg_c9560508360b548dafd6fecf7b13b893
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4c1e20ba052d5b38ba487a6fc6e80a95
title: continuedev/continue/docs/cli/configuration.mdx @ 5522c6f44ca0
updated_at: '2026-09-14T01:44:07Z'
---

# continuedev/continue/docs/cli/configuration.mdx @ 5522c6f44ca0

<!-- rcw:begin owner=source:src_4c1e20ba052d5b38ba487a6fc6e80a95 block=evidence -->
- Inside a CLI TUI session, the `/config` command lists available local configurations and the selection persists to the next session. [@claim:clm_41906ac0ec4c107b0537188a2ee3562a0c21a39a665fb5bf1dfd99a2dd56cc6b]
- The CLI supports repeatable launch flags such as `--rule` (file path or inline string) and `--agent` (e.g. `my-org/pr-reviewer`) to inject configuration without editing files. [@claim:clm_674a2ff212bbf8940bc4e473505cab6f4e14bb849447d9e59682a44bf99ef4c9]
- Sensitive values in config are referenced as environment variables using the `${{ secrets.MY_API_KEY }}` syntax. [@claim:clm_eb9bd6021c717d81109cfea7204c6bdbf9dd32bfc05f15c807a07c72a106d138]
- The CLI (`cn`) resolves configuration in order: a `--config` file path flag, the last-used saved config, then the default `~/.continue/config.yaml`. [@claim:clm_f9793019a66b0a2c3af655f952dc21515f4050463a82f67fa81f4793e5939c12]
<!-- rcw:end owner=source:src_4c1e20ba052d5b38ba487a6fc6e80a95 block=evidence -->

## Researcher notes

