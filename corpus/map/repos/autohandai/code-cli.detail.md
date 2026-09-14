# autohandai/code-cli -- full detail

[Back to orientation](code-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/autohandai/code-cli/f4775fdebd930b7e1a624aebab7dc98fed04ca50/39ddcfcd21c53f63.json](../../../wiki/dossiers/autohandai/code-cli/f4775fdebd930b7e1a624aebab7dc98fed04ca50/39ddcfcd21c53f63.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Browser automation is built in via /browser or --browser flags, with tools for tabs, tab groups, network and console inspection, extension bridge calls, and JavaScript execution. -- evidence: [docs/announcing-0.9.md#L53-L53](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/announcing-0.9.md#L53-L53) (`clm_0c0b453a31272f313e11b5501d6d1ad4b7f8cb9444e63a047788c0d3c6a2c9e7`)

## design-choices (1 claim(s))

- [observation/documented] Every installer scans writable PATH directories and silently replaces any existing `agent` command so `agent` resolves to Autohand, which can break other tools' `agent` commands. -- evidence: [README.md#L52-L60](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L52-L60) (`clm_1773e6c7cba31627581866f68555329783eeded32baf77f8ec715f0c2d6b353a`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (3 claim(s))

- [observation/documented] Skills are SKILL.md packages with YAML frontmatter (name, description, optional allowed-tools, license, compatibility, metadata) plus markdown instructions injected into agent context when activated. -- evidence: [docs/agent-skills.md#L28-L28](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L28-L28), [docs/agent-skills.md#L21-L21](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L21-L21), [docs/agent-skills.md#L149-L149](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L149-L149), [docs/agent-skills.md#L170-L177](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L170-L177), [docs/agent-skills.md#L151-L161](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L151-L161) (`clm_0fe27beccf53825a779c8fe54ab85a48e0fbe14a5beab2eae40fbce7e008d9a9`)
- [observation/documented] Skills are discovered from many locations with later sources taking precedence, including built-in dist skills, Codex, Claude, shared agent directories, Autohand user/project dirs, and extension contributions. -- evidence: [docs/agent-skills.md#L107-L107](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L107-L107), [docs/agent-skills.md#L109-L123](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L109-L123) (`clm_04c47572c18fd0d86abcaa123f311b92e1c62c0ec1997f9dd8c144a8fff1abb0`)
- [observation/documented] Skills found in Codex or Claude locations are auto-copied to the corresponding Autohand locations, and existing Autohand skills are never overwritten. -- evidence: [docs/agent-skills.md#L131-L132](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L131-L132), [docs/agent-skills.md#L129-L129](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L129-L129), [docs/agent-skills.md#L134-L135](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L134-L135) (`clm_96322a6ba78b65463d9e38171f3bf42b9501c816ac86f0a30e983412f045db00`)

## interfaces (4 claim(s))

- [observation/documented] The product runs as a terminal REPL with file mentions, slash commands, keyboard shortcuts, provider switching, and session history available from one prompt. -- evidence: [README.md#L14-L14](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L14-L14), [README.md#L22-L28](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L22-L28) (`clm_5b2b35906618dad123d4e97d2ea9a54b4b77757a9fb0ae984c4d2cfeb82ded6c`)
- [observation/documented] Slash commands include /skills (list, use, deactivate, info, new) and /deep-research with a /deep-search alias for research runs. -- evidence: [docs/agent-skills.md#L693-L699](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L693-L699), [docs/agent-skills.md#L78-L78](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L78-L78), [docs/agent-skills.md#L38-L39](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L38-L39), [docs/agent-skills.md#L74-L76](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L74-L76) (`clm_c7d75e94edbeda87c007a68415cb256ae8d1493b7c07015a787e9a062e517227`)
- [observation/documented] The CLI is exposed as `autohand`, `autohand-code`, and `agent`, with `autohand` as the canonical name. -- evidence: [README.md#L52-L60](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L52-L60) (`clm_17d5f5fbbf5a76998b7885f28c2127c135da79dc9550891055d7fff88ce8f2ea`)
- [observation/documented] Version 0.9.0 makes the Ink TUI the default interactive experience and adds a TextBuffer composer with word navigation, multiline input, Shift+Enter, and $skill autocomplete. -- evidence: [docs/announcing-0.9.md#L9-L9](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/announcing-0.9.md#L9-L9), [docs/announcing-0.9.md#L28-L28](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/announcing-0.9.md#L28-L28), [docs/announcing-0.9.md#L17-L17](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/announcing-0.9.md#L17-L17) (`clm_119e4a8c669c368a0fb352bc72b9e464c2db2cc71c4cfcbbbf6f23e4a29ba6ad`)

## memory-state (2 claim(s))

- [observation/documented] Memory tools include save_memory, recall_memory (ranked by content, tags, recency), inspect_memory, and delete_memory which retains a canonical deletion event. -- evidence: [docs/agent-skills.md#L288-L293](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L288-L293) (`clm_7976533c20c6ab2bd70007c6148e0b32abdf754f3fd6c0a5b900f6f324b33559`)
- [observation/documented] Delegated workers read up to five recent project lessons (each truncated to 1,000 chars) from the workspace's .autohand/memory; bare mode disables this, and agent.autoMemory:false disables automatic lesson saving. -- evidence: [docs/agent-skills.md#L300-L305](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L300-L305), [docs/agent-skills.md#L295-L298](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L295-L298) (`clm_6026759256d34afe67334115c65547ad00ed4365841d993485992fde236b68f4`)

## orchestration (1 claim(s))

- [observation/documented] The bundled deep-research skill runs multi-task research with persisted status (task progress, tool, evidence/failure counts, tokens), and a run is marked complete only after tasks finish, the report passes a source audit, and project checks pass. -- evidence: [docs/agent-skills.md#L78-L78](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L78-L78), [docs/agent-skills.md#L80-L80](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L80-L80) (`clm_d8fd1ecb52e61e022bfee0494a507fe87a913345c2cd9848b872ae7f44b1a96f`)

## tools-permissions (1 claim(s))

- [observation/documented] Skills declare a space-delimited allowed-tools list restricting which tools they may use, and the agent prompts before risky operations unless a different permission mode is chosen. -- evidence: [README.md#L32-L36](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L32-L36), [docs/agent-skills.md#L227-L227](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L227-L227), [docs/agent-skills.md#L23-L26](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L23-L26), [docs/agent-skills.md#L170-L177](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L170-L177) (`clm_6d7ed083768bb9f67c429da0c57011804668192a6954874c040aa51f48683123`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The agent supports multiple LLM providers including OpenRouter, OpenAI, AWS Bedrock, DeepSeek, Azure, Z.ai, Vertex AI, Ollama, llama.cpp, MLX, and local models. -- evidence: [docs/announcing-0.9.md#L34-L34](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/announcing-0.9.md#L34-L34), [README.md#L22-L28](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L22-L28) (`clm_8d3b97bc088f8bc8dad41fe45c88178a80412c6a417098be9c6be33a3969a323`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

