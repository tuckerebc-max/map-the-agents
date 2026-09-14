# failproofai/failproofai -- full detail

[Back to orientation](failproofai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/failproofai/failproofai/86f80fc59ee1a18211780ef2fe964d80858deeb2/cca0cfe74a52d5e3.json](../../../wiki/dossiers/failproofai/failproofai/86f80fc59ee1a18211780ef2fe964d80858deeb2/cca0cfe74a52d5e3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] 39 built-in policies ship with the tool and activate immediately on install; examples include blocking .env reads, sudo, rm -rf, force pushes, destructive SQL, and unreviewed terraform/kubectl changes. -- evidence: [README.md#L149-L158](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L149-L158), [README.md#L143-L143](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L143-L143) (`clm_82581b1582d7667b196012cb16fa81d864344db38de083cb8979b582a32eb87b`)
- [observation/documented] A hosted observability product offers fleet-wide runs, execution graphs with parallel sub-agent lanes, latency percentiles, per-model cost tracking, SQL over traces, scheduled audits, and Slack/email/webhook alerts; self-hosting is Enterprise-only. -- evidence: [README.md#L213-L220](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L213-L220) (`clm_3fc58f555374c73ba3593a36b58c429093665a06e18105fa687d178ea654f010`)

## design-choices (1 claim(s))

- [observation/documented] The tool is licensed under MIT plus the Commons Clause: free for internal and personal use, but commercial resale of failproofai itself requires a separate agreement. -- evidence: [README.md#L258-L258](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L258-L258) (`clm_9c2e691b4bd5850923f0c27528ee0e6aa4d0b68ee9419075ca225fba2a3dfcbf`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors must run 'bun install && bun run build' before starting, because the repo runs failproofai's own hooks on itself and they resolve the import against the compiled dist/ bundle. -- evidence: [README.md#L266-L270](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L266-L270) (`clm_1acd9739e57a064b485bd19f156b5419178846af13464452495d41b9c85f9c08`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The product hooks into 12 agent harnesses in two classes: ten coding CLIs (e.g. Claude Code, Codex) and two chat/assistant gateways (Hermes, OpenClaw), with the same events and policies across them. -- evidence: [README.md#L17-L21](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L17-L21), [README.md#L33-L35](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L33-L35) (`clm_a3ba2c513f47868d14f2b6b4eff747d2036179598cf9abee9c673560a6068fa8`)
- [observation/documented] Agents outside supported harnesses can report via a Python SDK providing tracing, sessions and audits; enforcement there requires a hook in the user's own runtime. -- evidence: [README.md#L37-L39](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L37-L39) (`clm_3cb98631c03fcb2b1556c1b93a2bedd6f431f8d5d2155750a63a3c55fd15c637`)
- [observation/documented] Custom policies are JS files dropped into .failproofai/policies/ that load automatically without flags, and can be committed so the whole team receives them on pull. -- evidence: [README.md#L169-L170](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L169-L170) (`clm_1c0982328557c797273d1738618266d07074dd42a3e37ed058b3b50e31e6d8fd`)
- [observation/documented] Custom policies are registered via a customPolicies.add() API from the failproofai package, matching events such as PreToolUse and receiving a context with tool input. -- evidence: [README.md#L175-L184](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L175-L184), [README.md#L172-L173](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L172-L173) (`clm_f9e3d7d8905aedd84a24c98a4568e3545b84f73a5ec20252c1965974e3aeb891`)
- [observation/documented] Running failproofai with no arguments serves a local dashboard on localhost:8020 reading existing run history with no account or data leaving the machine; an audit command scans history for risky patterns and suggests policies. -- evidence: [README.md#L202-L207](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L202-L207) (`clm_a9cf62070de819442d116355e30a898ccbb653a3c9347fc4334913a7de2f37b0`)
- [observation/documented] A CLI 'fp' supports commands like 'fp list tools' and 'fp events --event-type tool_use,tool_result --env production --since 24h', with JSON output options for full session events. -- evidence: [docs/sessions/tools.mdx#L16-L25](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/docs/sessions/tools.mdx#L16-L25) (`clm_56923caf6f1aab338303927ede002b6badf18d71960544c6652e03a2f6e6bd91`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Policies return one of three decisions: allow() permits the operation, deny(message) blocks it and returns the message to the agent, and instruct(message) lets it pass while adding context to the agent's next prompt. -- evidence: [README.md#L188-L192](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L188-L192) (`clm_b4e41cdc9b7c5ad3fc9cd74329ca984b9a373e5a4e8289930c5c3be5ef864de0`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is distributed via npm as failproofai and installed globally with npm install -g; the project is written in TypeScript per its Trendshift badge. -- evidence: [README.md#L5-L5](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L5-L5), [README.md#L137-L141](https://github.com/FailproofAI/failproofai/blob/86f80fc59ee1a18211780ef2fe964d80858deeb2/README.md#L137-L141) (`clm_7c06879da3b4891c713f59e5490bae36fe4aab8287854faf5f9d42bf25c35d9e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

