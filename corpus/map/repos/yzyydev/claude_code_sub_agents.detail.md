# yzyydev/claude_code_sub_agents -- full detail

[Back to orientation](claude_code_sub_agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yzyydev/claude_code_sub_agents/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/e2fcdd7a779f6e0a.json](../../../wiki/dossiers/yzyydev/claude_code_sub_agents/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/e2fcdd7a779f6e0a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The system is organized around three command modules in .claude/commands/: start.md (iterative loop orchestrator), solve.md (parallel case processor), and prime.md (context management utilities). -- evidence: [README.md#L13-L13](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L13-L13), [README.md#L229-L247](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L229-L247), [README.md#L17-L22](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L17-L22) (`clm_48ba97847fc9570ecccf2e99e6a1e68313a59f13059ef244e300720d8c59c8b3`)

## design-choices (1 claim(s))

- [observation/documented] The design uses wave-based agent deployment to manage context limits, fresh agent instances per wave, progressive summarization of completed iterations, and lightweight state tracking in the main orchestrator. -- evidence: [README.md#L108-L111](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L108-L111), [README.md#L180-L184](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L180-L184), [README.md#L26-L29](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L26-L29) (`clm_0ee5aab3308f4b7c541935a0e0bd551e1c83eaec4f64943a411fdc3adcb069b8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The /start command takes a spec file, an output directory, and a count that may be a number or the literal 'infinite', e.g. /start specs/content_spec.md output/ 5. -- evidence: [README.md#L84-L85](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L84-L85), [README.md#L36-L39](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L36-L39), [README.md#L41-L44](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L41-L44) (`clm_d7f7ac577f2025c35d3806958bf28488b6ba0e54e1f87af8ff17db63965ac328`)
- [observation/documented] The /solve command takes a legal analysis spec, an input directory of scenario files, and an output directory, e.g. /solve specs/law_example.md example_input/ example_output/. -- evidence: [README.md#L60-L63](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L60-L63), [README.md#L96-L97](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L96-L97), [README.md#L55-L58](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L55-L58) (`clm_347e818d022ca924c2e4f460408d60de8993eea6e1198e30412e127efa54bd0f`)
- [observation/documented] The /prime command lists project files for context awareness, pre-loads documentation, and manages memory efficiency across agent waves. -- evidence: [README.md#L72-L72](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L72-L72), [README.md#L74-L77](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L74-L77) (`clm_d316800e0d3027abc6413e5fdb6a8da8f4b3e4186e68182b4898be9322f2330c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Sub-agents receive structured task prompts specifying the iteration number, full spec analysis, a summary of existing outputs, and an assigned creative direction, with requirements to ensure uniqueness and follow the spec format. -- evidence: [README.md#L171-L178](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L171-L178), [README.md#L165-L169](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L165-L169), [README.md#L163-L163](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L163-L163), [README.md#L159-L161](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L159-L161) (`clm_4025e2ff96479edc96fdbf8634a50bb5078542b248b3f25a7a9cc622bf4450d0`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README self-reports tested scenarios including 10 parallel legal analyses, infinite-mode generation with maintained quality, and cross-agent deduplication; these are author claims, not an independent benchmark harness. -- evidence: [README.md#L126-L129](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L126-L129), [README.md#L103-L106](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L103-L106), [README.md#L120-L124](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L120-L124) (`clm_ff2be5fd26603e1cbd8f7316ec1fdf0221493770a7b830700609c66c977d3610`)

## dependencies (1 claim(s))

- [observation/documented] The project depends on Claude Code's command system and sub-agent infrastructure, and includes a .claude/settings.local.json configuration file. -- evidence: [README.md#L229-L247](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L229-L247), [README.md#L7-L7](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L7-L7) (`clm_72bab8cb2be86b2d6bc9436e12a7d76c88549c9135d96232501c2a910715a907`)

## limitations (1 claim(s))

- [observation/documented] The README acknowledges context-capacity boundaries, noting wave-based deployment, progressive sophistication strategies, and graceful conclusion planning are used when approaching context limits. -- evidence: [README.md#L126-L129](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L126-L129) (`clm_85e7512abb6858f0001a716b6591d767f9be01d4c7a2979ac6f8d8dfe7ae5f69`)

## relevance (1 claim(s))

- [observation/documented] A bundled legal education example provides 10 civilian-law scenario files, a law_example.md specification, student instructions, and 10 generated IRAC-format analyses. -- evidence: [README.md#L136-L138](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L136-L138), [README.md#L133-L133](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L133-L133), [README.md#L229-L247](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L229-L247), [README.md#L141-L144](https://github.com/yzyydev/claude_code_sub_agents/blob/7597ed864ce2c6d19ee558aeb8f7cca0d7d64c9c/README.md#L141-L144) (`clm_8e3dd30f22df69a287584913406984bdf0602f86fc77d9c87ba80dff20d3fa95`)

