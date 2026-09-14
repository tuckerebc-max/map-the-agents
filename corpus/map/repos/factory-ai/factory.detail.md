# factory-ai/factory -- full detail

[Back to orientation](factory.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/factory-ai/factory/eb4c4e381fd708b704bdf072d8560e9addbf5d06/b15ed6fa8ebff7dd.json](../../../wiki/dossiers/factory-ai/factory/eb4c4e381fd708b704bdf072d8560e9addbf5d06/b15ed6fa8ebff7dd.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Separate TypeScript and Python SDK repositories for Droid are linked from the README. -- evidence: [README.md#L52-L53](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L52-L53) (`clm_e09e3161f2b5746dee163af3404f8ee17286668fb9477ee6959fa080ff0420e0`)
- [observation/documented] A Droid GitHub Action is referenced that runs AI-powered code reviews, security scans, and PR description generation on pull requests. -- evidence: [README.md#L57-L57](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L57-L57) (`clm_0a927fc68a1c362083ee38eb4f91bf3f433ba08488534f49d804c850cafa556b`)
- [observation/documented] The ecosystem links include a plugins marketplace and an ESLint plugin repository. -- evidence: [README.md#L61-L62](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L61-L62) (`clm_b887ad0315f8bd03dca455b8ac89f930a8ef3742caa604f1060f45436f6737f8`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: docs contributors install the Mintlify CLI globally and run `mintlify dev` at the docs root (where docs.json lives) to preview changes locally. -- evidence: [docs/README.md#L21-L23](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L21-L23), [docs/README.md#L15-L17](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L15-L17), [docs/README.md#L19-L19](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L19-L19), [docs/README.md#L13-L13](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L13-L13) (`clm_2ffbc8fae987e5d99cf8e5646d3ecc7e1e544522b673594d76bbed95afac5633`)
- [observation/documented] Repository development practice: troubleshooting guidance says to run `mintlify install` if the dev server fails, and that 404s usually mean the wrong folder (docs.json missing). -- evidence: [docs/README.md#L31-L32](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L31-L32) (`clm_024dc5d73fdae857c64de01746e55fbaf960b5f076ce97b014a363cd14e47393`)
- [observation/documented] Repository development practice: a GitHub App can auto-propagate repo changes to the docs deployment, with production deploys after pushes to the default branch. -- evidence: [docs/README.md#L27-L27](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/docs/README.md#L27-L27) (`clm_954c490e6202b73fa964e86255f391bb5cd2e8d460913573427096caad4a84be`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Factory is described as an agent-native development platform available across CLI, Web, Slack/Teams, Linear/Jira, and Mobile. -- evidence: [README.md#L3-L3](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L3-L3) (`clm_b915261df90e00e1095f729f77b75e67590977b9354564cdfba430fcf7dde2f6`)
- [observation/documented] The product's agent is named Droid and is distributed as a CLI; users start a session by running `droid` inside a project directory. -- evidence: [README.md#L31-L31](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L31-L31), [README.md#L33-L36](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L33-L36), [README.md#L5-L5](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L5-L5) (`clm_0de514154a023649a354c2035decb2781fe0f26da8ee88837b1461e59c776266`)
- [observation/documented] The README links a VS Code extension and notes ACP support for JetBrains IDEs and Zed. -- evidence: [README.md#L40-L42](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L40-L42) (`clm_73df4562039154cf9245765a234026d6da5be232b2b46198ce84e33db62a6b18`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README claims Droid is top performing in terminal benchmarks; this is a self-reported marketing statement, not an eval harness in the repo. -- evidence: [README.md#L5-L5](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L5-L5) (`clm_cc0302d865251d47c4ea2d5e95597a0cc28747fbc31dc794974ea6434324b6e8`)

## dependencies (1 claim(s))

- [observation/documented] Installation options include a curl shell script for macOS/Linux, a PowerShell command for Windows, and a global npm install of the `droid` package. -- evidence: [README.md#L15-L17](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L15-L17), [README.md#L27-L29](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L27-L29), [README.md#L21-L23](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L21-L23) (`clm_672eacd23d72fe270f89d6d688273a3c7c56f3e9d1d4d520255b67e0167b58f3`)

## limitations (1 claim(s))

- [inference/documented] The evidence consists only of README/docs marketing and setup text; no source code appears in the snapshot, so runtime internals of Droid cannot be verified from this evidence. -- evidence: [README.md#L71-L71](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L71-L71), [README.md#L3-L3](https://github.com/Factory-AI/factory/blob/eb4c4e381fd708b704bdf072d8560e9addbf5d06/README.md#L3-L3) (`clm_6ceed9ac2415c6f903d6b2b5cb54d0be7bd17a2c0513191578fb3ff0a1fd426e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

