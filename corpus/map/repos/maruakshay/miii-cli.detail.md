# maruakshay/miii-cli -- full detail

[Back to orientation](miii-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/maruakshay/miii-cli/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/5960cfd3fa980381.json](../../../wiki/dossiers/maruakshay/miii-cli/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/5960cfd3fa980381.json)

## specifications (1 claim(s))

- [observation/documented] miii is a local terminal AI coding agent that runs against Ollama with no API keys or cloud, positioned as an offline alternative to cloud coding assistants. -- evidence: [README.md#L3-L7](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L3-L7), [README.md#L1-L1](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L1-L1) (`clm_d864208656c219dba9bf6098875b0b273af5369e56538de528e888b4d34ff782`)

## components (1 claim(s))

- [observation/documented] Built-in agent tools include read_file, write_file, edit_file, glob, grep, run_bash, and write_todos for tracking multi-step work. -- evidence: [README.md#L74-L82](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L74-L82) (`clm_f27c42c8ce85e6ab374d2c3e35cb02b98de5e69d2a04290925a6703d95af998a`)

## design-choices (2 claim(s))

- [observation/documented] Tool output over ~10K bytes is spilled to ~/.miii/output/<id>.txt with a head/tail preview inline; the model pages through the file with ranged reads and spill files are garbage-collected after 24 hours. -- evidence: [README.md#L209-L209](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L209-L209), [README.md#L217-L218](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L217-L218) (`clm_8788b4ff918329fb1db305305d5e066e956a8b27f70667dc5de361a421a333ca`)
- [observation/documented] The agent repairs malformed tool calls from small models and sizes its prompt to the model's context window, and a MIII.md file in the repo is read every turn to teach project conventions. -- evidence: [README.md#L58-L65](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L58-L65) (`clm_0d46e7893c507521421fae6db105bdf2cb65ba526029dfe820d8e16d8d61f972`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm install && npm run dev, and use npm run build, npm run typecheck, npm test, and npm run eval (a regression gate powering miii doctor); npm run build && npm link runs the working tree as the global miii. -- evidence: [README.md#L236-L239](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L236-L239), [README.md#L248-L249](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L248-L249), [README.md#L241-L246](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L241-L246) (`clm_c42c0120ad210182b0a99d55f402b56119ddd26b3132858890aa43b95a634c2b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes slash commands (/plan, /permissions, /models, /sessions, /compact, /copy, /clear, /exit), a command palette on '/', and keyboard shortcuts such as Shift+Tab for permission modes and Ctrl+V for image paste. -- evidence: [README.md#L152-L164](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L152-L164), [README.md#L134-L150](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L134-L150) (`clm_cc53973488d3af3a7d5ef5139cd7fa5f1176027f60bcd24e79fc937dd8d0fdcd`)
- [observation/documented] Custom slash commands are Markdown files in .miii/commands/ (project scope) or ~/.miii/commands/ (personal), supporting $ARGUMENTS and $1-$9 substitution, with project commands shadowing personal ones but never built-ins. -- evidence: [README.md#L126-L126](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L126-L126), [README.md#L117-L117](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L117-L117), [README.md#L128-L129](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L128-L129) (`clm_f44125e1bc73a93e9e2034bd71bdcb86376fe7b3ccc3b5ccf612c2ab1f5f3f82`)

## memory-state (1 claim(s))

- [observation/documented] Saved approval rules live in .miii/permissions.json per project (with an optional global ~/.miii/permissions.json), and sessions can be saved and resumed via /new and /sessions. -- evidence: [README.md#L152-L164](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L152-L164), [README.md#L94-L94](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L94-L94) (`clm_5bb8339a525f232b1789181de9300440f42109a223e51726b4ac71a3ab0c1c0b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] File tools reject ../ traversal and absolute paths outside the workspace, while run_bash is not path-confined and is bounded only by the permission prompt. -- evidence: [README.md#L84-L85](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L84-L85) (`clm_47e0a3693cdf4b5803d63499e9b3b036fdc0155079da584746be22a3bae2f439`)
- [observation/documented] Four permission modes cycle via shift+tab: normal, plan (read-only), auto-accept edits, and bypass; 'always' approvals save exact commands plus globs that never span command boundaries or match destructive programs. -- evidence: [README.md#L104-L109](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L104-L109), [README.md#L92-L92](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L92-L92), [README.md#L90-L90](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L90-L90) (`clm_8507b87c0fbe5a1bea32b5da0b1b64a9e902ea5fc29da90240584449cc439107`)

## evaluation (1 claim(s))

- [observation/documented] The product includes `miii doctor`, which grades the user's installed local models on real engineering tasks to check whether they can drive an agent. -- evidence: [README.md#L58-L65](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L58-L65), [README.md#L263-L263](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L263-L263) (`clm_71db020bbd3913059e2e39478ff3b91b20476bf96f50e9f47f41f691d3345d68`)

## dependencies (2 claim(s))

- [observation/documented] The tool requires Node 18 or newer and Ollama, and is distributed as the npm package miii-agent. -- evidence: [README.md#L9-L14](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L9-L14), [README.md#L34-L34](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L34-L34) (`clm_015d9311a3c7d0f494195148097418c2e38216355fd50d2d9df6823d17301dd4`)
- [observation/documented] Besides Ollama, miii can talk to any OpenAI-compatible local server such as llama.cpp, LM Studio, or vLLM, selected via config providers or --provider at launch. -- evidence: [README.md#L195-L195](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L195-L195), [README.md#L183-L183](https://github.com/maruakshay/miii-cli/blob/0a712d9f2d68236ddeb53ee1ce10471ae59193bc/README.md#L183-L183) (`clm_eaaa84747daa921a19272b09fbbaf34be6318692c9dbbee2d887a8b860f04ebc`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

