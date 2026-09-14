---
access: public
aliases: []
claim_ids:
- clm_06d78fafc485e15b09969c0f1ddd00baa1c543a6b4a22a9928b6b930ef473857
- clm_087046fd7bb0daa0f796c75b7cc17188e7b757f677a6927a8fe4add502d332f2
- clm_0a8ae43598eac69ec4f997567eab67660fa4328fe24ad096bed18e6d65393e13
- clm_0f6dd66f7537ff7f924fbc69b45973a4855cf42db441883889f29400015a88c4
- clm_1cd9510270100dcc2dedfa54d80739f28ec2160a0bb65deaf9dc2704a1031522
- clm_3df3886481fe64f9878b5ef505ad508c5a51754de4024dcd9c0ae58b8b30ff65
- clm_3f76fe42a1c917d31c20a69a7b7727bb2d78b9aea9814cc0b01a22cebd9ebcd6
- clm_5dbd97c4b02e028e4ff70c324ef61ef5039dfd7a4fb4142eb4bc908d7325b7d0
- clm_7f6a331eee4623bfec49b52f8dc55ca34479a37432efede0bc7530139617b7c0
- clm_886deaa6b53c3b442ee5e9d446e3695a4fd1ace4f3e1d66f19124f59239c37d6
- clm_a09c321a14672285262a98713673d0cad73040553bf2d253502d67c45d2ee233
- clm_e5a318fd102bf19bd852ae1d0d00303f05093a5373842aebfa2a5809183842d4
maturity: draft
page_id: pg_350fb79dc5115591ab5e4d6b5d17d6b9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e5704ef5c25a527785206d5ac1d694ac
title: ParthSareen/ducky/README.md @ e9c8f5f98bf4
updated_at: '2026-09-14T04:15:21Z'
---

# ParthSareen/ducky/README.md @ e9c8f5f98bf4

<!-- rcw:begin owner=source:src_e5704ef5c25a527785206d5ac1d694ac block=evidence -->
- Keyboard controls include Enter to submit, Ctrl+J for newline, empty Enter to rerun or explain output, Ctrl+R to rerun the last suggestion, Ctrl+S to copy, and !<cmd> to run shell commands directly. [@claim:clm_06d78fafc485e15b09969c0f1ddd00baa1c543a6b4a22a9928b6b930ef473857]
- Data is stored under ~/.ducky/ in files for prompt history, a JSON conversation log, user preferences including last model, and saved crumbs (crumbs.json). [@claim:clm_087046fd7bb0daa0f796c75b7cc17188e7b757f677a6927a8fe4add502d332f2]
- Crumbs are saved command shortcuts supporting ${VAR} and $var placeholder styles, invoked by name with positional arguments that substitute into the stored command. [@claim:clm_0a8ae43598eac69ec4f997567eab67660fa4328fe24ad096bed18e6d65393e13]
- CLI flags include --directory/-d to preload code, --model/-m, --local/-l (qwen3 default), and --yolo/-y to auto-run commands without confirmation. [@claim:clm_0f6dd66f7537ff7f924fbc69b45973a4855cf42db441883889f29400015a88c4]
- Requirements are Ollama (local or cloud) and Python 3.10+; the requirements.txt lists 'ollama'. [@claim:clm_1cd9510270100dcc2dedfa54d80739f28ec2160a0bb65deaf9dc2704a1031522]
- Repository development practice: contributors clone the repo, run 'uv sync', run via 'uv run ducky', and lint with 'uv run ruff check .'. [@claim:clm_3df3886481fe64f9878b5ef505ad508c5a51754de4024dcd9c0ae58b8b30ff65]
- The tool is built around Ollama, supporting both local models (localhost:11434) and cloud models (ollama.com), with the last used model saved automatically. [@claim:clm_3f76fe42a1c917d31c20a69a7b7727bb2d78b9aea9814cc0b01a22cebd9ebcd6]
- Both 'ducky' and 'rubber-ducky' executables work identically; global install via 'uv tool install rubber-ducky' is recommended, and uvx usage requires a '--' separator. [@claim:clm_5dbd97c4b02e028e4ff70c324ef61ef5039dfd7a4fb4142eb4bc908d7325b7d0]
- The CLI offers an interactive REPL launched with 'ducky' and a single-shot mode where a positional prompt yields one command suggestion that is copied to the clipboard. [@claim:clm_7f6a331eee4623bfec49b52f8dc55ca34479a37432efede0bc7530139617b7c0]
- Piped input is supported, e.g. 'cat error.log | ducky "what's wrong here?"' or piping git diff for summarization. [@claim:clm_886deaa6b53c3b442ee5e9d446e3695a4fd1ace4f3e1d66f19124f59239c37d6]
- The --yolo flag appears to bypass the default confirmation step before executing suggested shell commands, implying execution normally requires user confirmation. [@claim:clm_a09c321a14672285262a98713673d0cad73040553bf2d253502d67c45d2ee233]
- The REPL supports inline commands such as /help, /clear, /reset, /model, /local, /cloud, /run, /expand, plus crumb commands like /crumbs and /crumb add/del. [@claim:clm_e5a318fd102bf19bd852ae1d0d00303f05093a5373842aebfa2a5809183842d4]
<!-- rcw:end owner=source:src_e5704ef5c25a527785206d5ac1d694ac block=evidence -->

## Researcher notes

