---
access: public
aliases: []
claim_ids:
- clm_53723a697dc23761d725c70ca0df7d1d0ca0792c3199b81858f1ad9ba5baf68d
- clm_6ad6a1d30c438363a1775097394a4e3a9f2c0f9225b2a0b97f2d0786b3427def
- clm_c258088d05443334a23937994268570faa424df4a5934146c6d91c3f54599a90
- clm_d4dd2550a8b463c0ffc1ab7c2097f6e980390e3dc8f86789989ca8ead3f4ff9e
maturity: draft
page_id: pg_5c1ade349dd557a7be290c0e7d58c30d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4cdaae0fa5395e1fadcfa955e32399f2
title: kodu-ai/claude-coder/extension-state-summary.md @ 60c1a717992c
updated_at: '2026-09-14T02:09:50Z'
---

# kodu-ai/claude-coder/extension-state-summary.md @ 60c1a717992c

<!-- rcw:begin owner=source:src_4cdaae0fa5395e1fadcfa955e32399f2 block=evidence -->
- An ExtensionStateProvider sets up listeners for extension messages and supplies state to child components, while a useExtensionState hook exposes state and setters. [@claim:clm_53723a697dc23761d725c70ca0df7d1d0ca0792c3199b81858f1ad9ba5baf68d]
- The extension's UI appears to depend on React and the Jotai state library, based on the state-management summary's description. [@claim:clm_6ad6a1d30c438363a1775097394a4e3a9f2c0f9225b2a0b97f2d0786b3427def]
- The extension's webview state is managed with Jotai, where individual atoms are combined into a single derived extensionStateAtom. [@claim:clm_c258088d05443334a23937994268570faa424df4a5934146c6d91c3f54599a90]
- Extension state includes fields such as claudeMessages, taskHistory, currentTask, apiConfiguration, maxRequestsPerTask, customInstructions, and alwaysAllowReadOnly/WriteOnly flags. [@claim:clm_d4dd2550a8b463c0ffc1ab7c2097f6e980390e3dc8f86789989ca8ead3f4ff9e]
<!-- rcw:end owner=source:src_4cdaae0fa5395e1fadcfa955e32399f2 block=evidence -->

## Researcher notes

