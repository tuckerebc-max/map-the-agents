# coze-dev/coze-studio -- full detail

[Back to orientation](coze-studio.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coze-dev/coze-studio/fefb05ff27be1da939612fbf9faf5db62583b8ae/9ba9c01ea3d00373.json](../../../wiki/dossiers/coze-dev/coze-studio/fefb05ff27be1da939612fbf9faf5db62583b8ae/9ba9c01ea3d00373.json)

## specifications (1 claim(s))

- [observation/documented] Coze Studio is described as an all-in-one AI agent development tool offering models, tools, and development modes from development through deployment. -- evidence: [README.md#L20-L20](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L20-L20) (`clm_153325461bb62d021ecd8a77fd97a35a9b52bc804b9a18f5cec38278dc925401`)

## components (1 claim(s))

- [observation/documented] Feature modules include model service management, agent building, app building, workflow building, resource development (plugins, knowledge bases, databases, prompts), and API/SDK integration. -- evidence: [README.md#L29-L36](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L29-L36) (`clm_fefee780816f926b476085e17fa277a2af0c9216d060bdfe441ccccd1056c91c`)

## design-choices (1 claim(s))

- [observation/documented] The backend is written in Golang, the frontend in React + TypeScript, with a microservices architecture following domain-driven design principles. -- evidence: [README.md#L27-L27](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L27-L27) (`clm_f0aca8c7b32d4066f88e3b8c6610d3756fdc5f13276575bea1a15c118b506671`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: contributors use a Rush.js monorepo with 135+ frontend packages, run tests via rush test / go test, and follow coverage targets by package level (80% for level 1). -- evidence: [CLAUDE.md#L70-L71](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L70-L71), [CLAUDE.md#L56-L60](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L56-L60), [CLAUDE.md#L151-L153](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L151-L153), [CLAUDE.md#L7-L7](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L7-L7) (`clm_25810b429e727ab22fff0acff556f07cf65533ef5dbb93c768010d7f178fd5c2`)
- [observation/documented] Repository development practice: PRs should follow AngularJS commit message conventions, pass lint (gofmt, golangci-lint), and include test cases; git-flow branching is used. -- evidence: [CONTRIBUTING.md#L44-L47](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L44-L47), [CONTRIBUTING.md#L25-L41](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L25-L41), [CONTRIBUTING.md#L7-L7](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L7-L7) (`clm_c4bb3b9bd0c41152265c75e1d660c763f27e2833dffffac921e1de9c7a7d5f75`)
- [observation/documented] Repository development practice: model configuration requires copying a template in backend/conf/model/ and setting id, API key, and model; supported providers include OpenAI, Volcengine Ark, Claude, Gemini, Qwen, DeepSeek, and Ollama. -- evidence: [CLAUDE.md#L143-L146](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L143-L146) (`clm_45445fbdf514406b74e3437b967142d27a0b8de6e334151a763a369fbc6f7f1e`)
- [observation/documented] Repository development practice: security bugs must not be disclosed in public issues; reporters should contact the team by email instead. -- evidence: [CONTRIBUTING.md#L19-L19](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L19-L19), [README.md#L101-L102](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L101-L102) (`clm_5785201efd8539f70fe48600e9e8f3dff986a9014e74ac69809ee8c218468a3d`)
- [observation/documented] Repository development practice: the project adopts a Contributor Covenant 2.0 code of conduct with an enforcement ladder from private warning to permanent ban. -- evidence: [CODE_OF_CONDUCT.md#L100-L104](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CODE_OF_CONDUCT.md#L100-L104), [CODE_OF_CONDUCT.md#L112-L113](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CODE_OF_CONDUCT.md#L112-L113), [CODE_OF_CONDUCT.md#L117-L119](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CODE_OF_CONDUCT.md#L117-L119), [CODE_OF_CONDUCT.md#L88-L93](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CODE_OF_CONDUCT.md#L88-L93), [CODE_OF_CONDUCT.md#L76-L77](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CODE_OF_CONDUCT.md#L76-L77) (`clm_a3e1d86712948b5d8804ef75591619682f39f3c86b44231cbe161fbb2c610546`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The Community Edition API and Chat SDK authenticate via Personal Access Token and provide conversation and workflow APIs; agents or apps can be embedded via Chat SDK. -- evidence: [README.md#L89-L94](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L89-L94), [README.md#L75-L83](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L75-L83) (`clm_79825c62fecec760633c4d26384762288fa6ef3c597802546aa30105cb1a08ba`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project credits the Eino framework for agent/workflow runtime and knowledge retrieval, FlowGram for the workflow canvas editor, and Hertz as the Go HTTP framework. -- evidence: [README.md#L129-L132](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L129-L132) (`clm_62dce7dfff3177787ad448570e35762d3b22f9c76c604db895f755ba7391da11`)

## limitations (2 claim(s))

- [observation/documented] The README warns that public-network deployment carries risks including account registration, Python execution in workflow code nodes, SSRF, and API privilege-escalation issues, recommending protective measures. -- evidence: [README.md#L70-L71](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L70-L71) (`clm_529234d990062020be64def16835409e5d829ad569dd8ee771382299a6e723f0`)
- [observation/documented] Some features, such as tone customization, are limited to the commercial version and not available in the open-source edition. -- evidence: [README.md#L86-L86](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L86-L86) (`clm_67c2ed8ff3517f3c4fdee60e6bdb006650564127c3694cef2fd0d831c735af05`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

