# open-multi-agent/open-multi-agent -- full detail

[Back to orientation](open-multi-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/open-multi-agent/open-multi-agent/eaeb420c4364e8d63757a7bbdc412655ed6c9420/fccf7ae5c773ed7e.json](../../../wiki/dossiers/open-multi-agent/open-multi-agent/eaeb420c4364e8d63757a7bbdc412655ed6c9420/fccf7ae5c773ed7e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Consequential actions pause for durable approvals: a suspend request is stored beside the checkpoint, bound to a SHA-256 hash of what the reviewer saw, decisions are atomic and first-wins, and tampered requests fail closed. -- evidence: [README.md#L91-L91](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L91-L91) (`clm_6ee9ffd4d6d73ead1fc400701983c223c8b139a5b2358d68a627471c3ff5829d`)
- [observation/documented] The runtime records every model block, tool call, and context rewrite in a journal; verifyRun() checks offline that each block reproduces byte for byte, reporting evicted windows as inconclusive rather than failures. -- evidence: [README.md#L97-L97](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L97-L97) (`clm_5d4577bb8e47f59b43b6c9e29ce955b3c5f2dcd3ada059091118a36dc69dae12`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: issues and pull requests are welcome, with CONTRIBUTING.md covering workspace boundaries, validation, and submission guidance. -- evidence: [README.md#L204-L204](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L204-L204) (`clm_22d61fd874fb6916074dfc80070a3ba9bba39877dc3123c94ccef49116297ee9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The core package exposes three run modes: runAgent() for a single agent, runTasks() for an explicit pipeline, and runTeam() which plans from a goal. -- evidence: [README.md#L87-L87](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L87-L87) (`clm_ffe8d231e17839decbf44cf7b6d6a4d2a535b68f0dd2b8ead70800d65e63db5a`)
- [observation/documented] An OpenMultiAgent instance is constructed with a default provider/model and an onToolCall callback that can return 'suspend' for consequential tool calls or 'allow' otherwise. -- evidence: [README.md#L63-L69](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L63-L69), [README.md#L60-L61](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L60-L61) (`clm_0983bbf29b4045e2d726bd156f2c8ae292df3a38e4410c80b6029ca6347f58f7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (3 claim(s))

- [observation/documented] runTeam() uses one model call to turn a goal into a task graph with assignees and dependencies, a deterministic scheduler executes it, and a second call writes the final answer; the coordinator is not consulted mid-run. -- evidence: [README.md#L150-L150](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L150-L150) (`clm_9f8c09e23b31b6a7fb4aff90a02b34b539773ad5c9b8b2bd71b8c6301498ee75`)
- [observation/documented] Adaptive recovery is opt-in via recovery.mode 'repairable': a Replanner or onTaskOutcome callback proposes a PlanPatch, OMA validates it, an optional onPlanPatch gate approves it, and the patch is applied atomically before the triggering task completes. -- evidence: [docs/adaptive-recovery.md#L9-L18](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L9-L18), [docs/adaptive-recovery.md#L3-L5](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L3-L5) (`clm_85dc8b1c6fe8d4e2b05fbfb52921da3814ef25bba8c39ff4dedcc4101760d8b1`)
- [observation/documented] Patch operations are addTasks, retargetPending, and supersedePending; started or terminal tasks cannot be retargeted or superseded, and repairs are forward-only with no undo of external side effects. -- evidence: [docs/adaptive-recovery.md#L84-L90](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L84-L90), [docs/adaptive-recovery.md#L92-L95](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L92-L95), [docs/adaptive-recovery.md#L145-L153](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L145-L153) (`clm_21575bcd943e015a5692e0b3247855243cf04e1a986d2bda6ed4ea7103614b72`)

## tools-permissions (1 claim(s))

- [observation/documented] Egress policy supports 'offline' or 'allowlist' modes checked before a built-in adapter connects; child policies can only tighten parents, unenforceable transports fail closed, and process/ACP backends sit outside the policy. -- evidence: [README.md#L109-L111](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L109-L111) (`clm_4a6d50386ec2f86137b83748c2588be1b36378f8848e55907c76fa8ec401a4ba`)

## evaluation (1 claim(s))

- [observation/documented] With governanceIntent 'required', runs are judged on an execution receipt of roles, ordering, dependency edges, and independent review; the evaluator never sees agent output text, and a successful run can still report 'unsatisfied'. -- evidence: [README.md#L103-L103](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L103-L103) (`clm_5a194948e06165e8044e794a22cdcac4add585894c6760c4df609e0587f23b2a`)

## dependencies (2 claim(s))

- [observation/documented] The project requires Node.js 20 or newer; Node 20 is upstream-EOL, kept only as a migration window, and will be removed in the next major release no earlier than 2026-10-31. -- evidence: [README.md#L41-L44](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L41-L44) (`clm_af0fe9f9166a6e7b9c2f52fa9a919e46a1c8857e668601461f3ca209cc1af38c`)
- [observation/documented] Built-in provider adapters cover Anthropic, OpenAI, Azure OpenAI, Bedrock, Gemini, Grok, Copilot, several Chinese providers, plus Ollama, vLLM, and llama-server via baseURL and any OpenAI-compatible or Vercel AI SDK endpoint. -- evidence: [README.md#L109-L111](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L109-L111) (`clm_b6db8eaf021a8a578de9f07c29be4e9c4f173f63707086d01ea18bfd1aa0af2f`)

## limitations (2 claim(s))

- [observation/documented] Budgets are checked only at turn and task boundaries, so a run can overshoot its ceiling by up to one model turn; exhausting a budget is reported via a budget_exceeded event and result fields rather than thrown. -- evidence: [docs/budgets-and-limits.md#L12-L18](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/budgets-and-limits.md#L12-L18) (`clm_e9f03b5b2fbd135e331d6f0c3345c39ab4ec6124de05e87ad26caab4eed37c09`)
- [observation/documented] When maxTurns is reached the run stops before the next model call and is still reported successful with no distinguishing flag; the docs suggest comparing toolCalls or message counts, or setting a lower maxTurns and treating a long run as an alert. -- evidence: [docs/budgets-and-limits.md#L40-L46](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/budgets-and-limits.md#L40-L46) (`clm_138096f7ff345494150fc199d68913fe2f5b3035c23c5be92471c5b4854c1609`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

