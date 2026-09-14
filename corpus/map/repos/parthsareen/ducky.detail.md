# parthsareen/ducky -- full detail

[Back to orientation](ducky.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/parthsareen/ducky/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/9266a62f93a6416b.json](../../../wiki/dossiers/parthsareen/ducky/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/9266a62f93a6416b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The tool is built around Ollama, supporting both local models (localhost:11434) and cloud models (ollama.com), with the last used model saved automatically. -- evidence: [README.md#L75-L78](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L75-L78), [README.md#L34-L35](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L34-L35), [README.md#L73-L73](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L73-L73) (`clm_3f76fe42a1c917d31c20a69a7b7727bb2d78b9aea9814cc0b01a22cebd9ebcd6`)
- [observation/documented] Piped input is supported, e.g. 'cat error.log | ducky "what's wrong here?"' or piping git diff for summarization. -- evidence: [README.md#L145-L145](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L145-L145), [README.md#L41-L47](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L41-L47), [README.md#L147-L150](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L147-L150) (`clm_886deaa6b53c3b442ee5e9d446e3695a4fd1ace4f3e1d66f19124f59239c37d6`)
- [inference/documented] The --yolo flag appears to bypass the default confirmation step before executing suggested shell commands, implying execution normally requires user confirmation. -- evidence: [README.md#L154-L154](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L154-L154), [README.md#L156-L158](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L156-L158), [README.md#L205-L211](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L205-L211) (`clm_a09c321a14672285262a98713673d0cad73040553bf2d253502d67c45d2ee233`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run 'uv sync', run via 'uv run ducky', and lint with 'uv run ruff check .'. -- evidence: [README.md#L285-L287](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L285-L287), [README.md#L294-L295](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L294-L295), [README.md#L290-L291](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L290-L291) (`clm_3df3886481fe64f9878b5ef505ad508c5a51754de4024dcd9c0ae58b8b30ff65`)

## skills-patterns (1 claim(s))

- [observation/documented] Crumbs are saved command shortcuts supporting ${VAR} and $var placeholder styles, invoked by name with positional arguments that substitute into the stored command. -- evidence: [README.md#L107-L107](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L107-L107), [README.md#L185-L185](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L185-L185), [README.md#L86-L86](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L86-L86), [README.md#L182-L183](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L182-L183), [README.md#L175-L175](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L175-L175) (`clm_0a8ae43598eac69ec4f997567eab67660fa4328fe24ad096bed18e6d65393e13`)

## interfaces (5 claim(s))

- [observation/documented] The CLI offers an interactive REPL launched with 'ducky' and a single-shot mode where a positional prompt yields one command suggestion that is copied to the clipboard. -- evidence: [README.md#L19-L19](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L19-L19), [README.md#L137-L137](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L137-L137), [README.md#L16-L16](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L16-L16), [README.md#L205-L211](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L205-L211), [README.md#L133-L135](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L133-L135), [README.md#L131-L131](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L131-L131) (`clm_7f6a331eee4623bfec49b52f8dc55ca34479a37432efede0bc7530139617b7c0`)
- [observation/documented] CLI flags include --directory/-d to preload code, --model/-m, --local/-l (qwen3 default), and --yolo/-y to auto-run commands without confirmation. -- evidence: [README.md#L22-L24](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L22-L24), [README.md#L80-L82](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L80-L82), [README.md#L205-L211](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L205-L211) (`clm_0f6dd66f7537ff7f924fbc69b45973a4855cf42db441883889f29400015a88c4`)
- [observation/documented] The REPL supports inline commands such as /help, /clear, /reset, /model, /local, /cloud, /run, /expand, plus crumb commands like /crumbs and /crumb add/del. -- evidence: [README.md#L193-L201](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L193-L201), [README.md#L164-L171](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L164-L171) (`clm_e5a318fd102bf19bd852ae1d0d00303f05093a5373842aebfa2a5809183842d4`)
- [observation/documented] Keyboard controls include Enter to submit, Ctrl+J for newline, empty Enter to rerun or explain output, Ctrl+R to rerun the last suggestion, Ctrl+S to copy, and !<cmd> to run shell commands directly. -- evidence: [README.md#L238-L246](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L238-L246), [README.md#L61-L69](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L61-L69) (`clm_06d78fafc485e15b09969c0f1ddd00baa1c543a6b4a22a9928b6b930ef473857`)
- [observation/documented] Both 'ducky' and 'rubber-ducky' executables work identically; global install via 'uv tool install rubber-ducky' is recommended, and uvx usage requires a '--' separator. -- evidence: [README.md#L30-L30](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L30-L30), [README.md#L27-L28](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L27-L28), [README.md#L13-L13](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L13-L13) (`clm_5dbd97c4b02e028e4ff70c324ef61ef5039dfd7a4fb4142eb4bc908d7325b7d0`)

## memory-state (1 claim(s))

- [observation/documented] Data is stored under ~/.ducky/ in files for prompt history, a JSON conversation log, user preferences including last model, and saved crumbs (crumbs.json). -- evidence: [README.md#L268-L268](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L268-L268), [README.md#L270-L275](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L270-L275) (`clm_087046fd7bb0daa0f796c75b7cc17188e7b757f677a6927a8fe4add502d332f2`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Ollama (local or cloud) and Python 3.10+; the requirements.txt lists 'ollama'. -- evidence: [README.md#L34-L35](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L34-L35), [requirements.txt#L1-L1](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/requirements.txt#L1-L1) (`clm_1cd9510270100dcc2dedfa54d80739f28ec2160a0bb65deaf9dc2704a1031522`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

