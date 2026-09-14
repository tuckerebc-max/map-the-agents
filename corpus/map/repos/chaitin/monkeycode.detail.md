# chaitin/monkeycode -- full detail

[Back to orientation](monkeycode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/chaitin/monkeycode/a67aef068778d4be596ca1cf793f7be25c408a26/2727223fcc195893.json](../../../wiki/dossiers/chaitin/monkeycode/a67aef068778d4be596ca1cf793f7be25c408a26/2727223fcc195893.json)

## specifications (3 claim(s))

- [observation/documented] MonkeyCode is described as an open-source enterprise-grade AI development platform combining development environment management, AI model/task management, and project requirement management. -- evidence: [README.md#L23-L23](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L23-L23) (`clm_574db900ad1c95baab900c5ddf1bdb682715c08d5bc929ec8b50a6133c01cff6`)
- [observation/documented] The MonkeyAI admin console manages user identity, AI resources, session usage, credit billing, and admin audit within a single instance, explicitly without multi-tenancy. -- evidence: [CONTEXT.md#L3-L3](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L3-L3) (`clm_64995ba91e0cfddc951404233511f0b11cb53da4b5972692b22b337e8b30e6d6`)
- [observation/documented] MonkeyCode is licensed under the GNU Affero General Public License v3.0. -- evidence: [README.md#L133-L133](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L133-L133) (`clm_49697c7cb891b4b63b16615681881eaf974ac2bfd21baafd84239ebd9c7ae350`)

## components (2 claim(s))

- [observation/documented] Tasks run in server-side cloud development environments; build, test, and preview workflows are executed in the cloud rather than on local machines. -- evidence: [README.md#L61-L66](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L61-L66) (`clm_000e608dbcf5f6733e241207f06231e40a66814076f6af739dc71ea1db9bfa95`)
- [observation/documented] AI resources include models, skills, rules, MCP services, individually toggleable MCP tools, and Experts (system-level agent presets combining role prompts, MCP tools, rules, and skills). -- evidence: [CONTEXT.md#L71-L73](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L71-L73), [CONTEXT.md#L75-L77](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L75-L77), [CONTEXT.md#L79-L81](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L79-L81), [CONTEXT.md#L87-L89](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L87-L89), [CONTEXT.md#L83-L85](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L83-L85), [CONTEXT.md#L67-L69](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L67-L69) (`clm_95d91e9bdd23f93ed0d1357e3367f872766d741981e2f487a1c59fd5aee0df64`)

## design-choices (2 claim(s))

- [observation/documented] The product targets deployment inside enterprise networks shared with an R&D team, with an online hosted environment (managed dev environments, built-in LLMs, mobile support) as an alternative. -- evidence: [README.md#L25-L26](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L25-L26) (`clm_51a375d178a48a2c0674497c3190b18f7e85fc72b0bc0adbb1f5f8109a297734`)
- [observation/documented] Users are organized in a tree expanding from a unique root group; group authorization covers descendant groups, and quotas inherit from the nearest parent group when unset. -- evidence: [CONTEXT.md#L105-L107](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L105-L107), [CONTEXT.md#L15-L17](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L15-L17) (`clm_2c4f5657f926b0d8587c99ff25c11ef08b959c6e2af1641c2ab0b1cfe4849d42`)

## workflows (1 claim(s))

- [observation/documented] Self-hosted install is via a curl-fetched bash script, with recommended minimums of 2C/4GB/40GB for the console and 8C/16GB/100GB for development-environment hosts. -- evidence: [README.md#L80-L81](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L80-L81), [README.md#L85-L87](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L85-L87) (`clm_d0376602231b7ac1f2b44c49e737a237c4746a29a9cb94e742b776d435792f50`)

## skills-patterns (1 claim(s))

- [observation/documented] A design-workflow plan proposes extracting design patterns via Skills/Atoms (code-import, design-extract, token-map, rewrite-plan), saved as Design System Packages with revisions so re-extraction creates a new revision rather than overwriting. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L334-L334](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L334-L334), [docs/plans/monkeydesign-design-workflow.md#L325-L325](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L325-L325), [docs/plans/monkeydesign-design-workflow.md#L327-L332](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L327-L332), [docs/plans/monkeydesign-design-workflow.md#L396-L396](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L396-L396) (`clm_bab0f642bd4682e07151be6145be1d06974dfbd81a29c020aa8737539c19000e`)

## interfaces (2 claim(s))

- [observation/documented] Native iOS and Android support is claimed, keeping PC and mobile data in sync so agents can continue running tasks while the user is away. -- evidence: [README.md#L61-L66](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L61-L66) (`clm_ee1c7e3a469c40ab4b52dfe691caee5df7fb176dd2c62451cce7378de60c88ec`)
- [inference/documented] The plan proposes new agent-client protocol messages (design/start-choice, template/reference/pattern selection, redesign-level) because plain AskUserQuestion cannot carry images; these appear to be proposals, not shipped behavior. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L571-L571](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L571-L571), [docs/plans/monkeydesign-design-workflow.md#L575-L583](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L575-L583) (`clm_bb0c595ad37cead759be14608f5c310a64d9f8337ff3bd0a0b22ccef951e4cf2`)

## memory-state (2 claim(s))

- [observation/documented] Billing uses an internal credit unit with per-cycle quotas, credit accounts, and immutable ledger records for deductions, grants, refunds, resets, and manual adjustments. -- evidence: [CONTEXT.md#L113-L115](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L113-L115), [CONTEXT.md#L109-L111](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L109-L111), [CONTEXT.md#L101-L103](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L101-L103) (`clm_6d89d3aa8ebdbd1f4a057a1a098d05d3c6fd97d75d016fb584c80a29fb2989ac`)
- [inference/documented] A DesignFlowState state machine is proposed so the design flow persists explicit stage state rather than relying on model memory; it appears to be a design proposal, not verified shipped code. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L727-L740](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L727-L740), [docs/plans/monkeydesign-design-workflow.md#L725-L725](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L725-L725) (`clm_16217d9acbcbc15cb19c14496e29cddb8589dab2e0b9ebd5a2823bc10ea93135`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Resource sharing supports read-only and read-write levels; read-write excludes sharing, deletion, or ownership transfer, and system rules can be forced onto target users or groups. -- evidence: [CONTEXT.md#L49-L51](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L49-L51), [CONTEXT.md#L45-L47](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L45-L47), [CONTEXT.md#L57-L59](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L57-L59) (`clm_f77e93194bca2d26a0a0bb68a939caeb6084a33c3c6bc7c6d3c077a86bb95328`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The platform integrates multiple LLMs including GLM, Kimi, MiniMax, Qwen, and DeepSeek, switchable per task type or chosen manually. -- evidence: [README.md#L61-L66](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L61-L66) (`clm_ccf94eed339c67bc763a66aa2ab40dabaa36447202723e0d309b4e71f2619314`)
- [observation/documented] The plan notes the image generation provider is not yet integrated into the current MonkeyDesign runtime, and Open Design code/assets licensing needs confirmation. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L703-L710](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L703-L710) (`clm_9c3a5f1370a4fd338e36f3b39026d555ec610090021541e41fd60c25542c6532`)

## limitations (2 claim(s))

- [observation/documented] A comparison table marks MonkeyCode as lacking local IDE, local CLI, and code completion, while claiming cloud environments, automated PR/MR review, team collaboration, and private deployment. -- evidence: [README.md#L93-L105](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L93-L105) (`clm_db9e030816a1592753a254da052d257dbcd03a2e68f50a318caab0d71429e76e`)
- [observation/documented] The plan lists non-goals including Figma two-way sync, a public design-pattern marketplace, multi-user collaboration and org-level permissions, and automatic production deployment. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L714-L714](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L714-L714), [docs/plans/monkeydesign-design-workflow.md#L716-L721](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L716-L721) (`clm_2babaa4f99befd1e281460e2df19a1ad90982116b00736448176f48a9a48e494`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

