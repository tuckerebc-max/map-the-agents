---
access: public
aliases: []
claim_ids:
- clm_153325461bb62d021ecd8a77fd97a35a9b52bc804b9a18f5cec38278dc925401
- clm_529234d990062020be64def16835409e5d829ad569dd8ee771382299a6e723f0
- clm_5785201efd8539f70fe48600e9e8f3dff986a9014e74ac69809ee8c218468a3d
- clm_62dce7dfff3177787ad448570e35762d3b22f9c76c604db895f755ba7391da11
- clm_67c2ed8ff3517f3c4fdee60e6bdb006650564127c3694cef2fd0d831c735af05
- clm_79825c62fecec760633c4d26384762288fa6ef3c597802546aa30105cb1a08ba
- clm_f0aca8c7b32d4066f88e3b8c6610d3756fdc5f13276575bea1a15c118b506671
- clm_fefee780816f926b476085e17fa277a2af0c9216d060bdfe441ccccd1056c91c
maturity: draft
page_id: pg_49b2bee119be5288bb6c08648eaaac73
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_63b96278c62f5541a3347b04a7e43e36
title: coze-dev/coze-studio/README.md @ fefb05ff27be
updated_at: '2026-09-14T03:42:58Z'
---

# coze-dev/coze-studio/README.md @ fefb05ff27be

<!-- rcw:begin owner=source:src_63b96278c62f5541a3347b04a7e43e36 block=evidence -->
- Coze Studio is described as an all-in-one AI agent development tool offering models, tools, and development modes from development through deployment. [@claim:clm_153325461bb62d021ecd8a77fd97a35a9b52bc804b9a18f5cec38278dc925401]
- The README warns that public-network deployment carries risks including account registration, Python execution in workflow code nodes, SSRF, and API privilege-escalation issues, recommending protective measures. [@claim:clm_529234d990062020be64def16835409e5d829ad569dd8ee771382299a6e723f0]
- Repository development practice: security bugs must not be disclosed in public issues; reporters should contact the team by email instead. [@claim:clm_5785201efd8539f70fe48600e9e8f3dff986a9014e74ac69809ee8c218468a3d]
- The project credits the Eino framework for agent/workflow runtime and knowledge retrieval, FlowGram for the workflow canvas editor, and Hertz as the Go HTTP framework. [@claim:clm_62dce7dfff3177787ad448570e35762d3b22f9c76c604db895f755ba7391da11]
- Some features, such as tone customization, are limited to the commercial version and not available in the open-source edition. [@claim:clm_67c2ed8ff3517f3c4fdee60e6bdb006650564127c3694cef2fd0d831c735af05]
- The Community Edition API and Chat SDK authenticate via Personal Access Token and provide conversation and workflow APIs; agents or apps can be embedded via Chat SDK. [@claim:clm_79825c62fecec760633c4d26384762288fa6ef3c597802546aa30105cb1a08ba]
- The backend is written in Golang, the frontend in React + TypeScript, with a microservices architecture following domain-driven design principles. [@claim:clm_f0aca8c7b32d4066f88e3b8c6610d3756fdc5f13276575bea1a15c118b506671]
- Feature modules include model service management, agent building, app building, workflow building, resource development (plugins, knowledge bases, databases, prompts), and API/SDK integration. [@claim:clm_fefee780816f926b476085e17fa277a2af0c9216d060bdfe441ccccd1056c91c]
<!-- rcw:end owner=source:src_63b96278c62f5541a3347b04a7e43e36 block=evidence -->

## Researcher notes

