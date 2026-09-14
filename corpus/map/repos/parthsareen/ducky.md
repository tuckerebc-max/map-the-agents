# parthsareen/ducky

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e9c8f5f98bf4 @ 9266a62f93a6416b

## Summary (orientation draft, not independently verified)

Rubber Ducky is a terminal tool that turns natural-language prompts into shell commands via Ollama (local or cloud), with an interactive REPL, single-shot mode, piped input, saved 'crumb' shortcuts, and state stored under ~/.ducky/. Evidence is README documentation plus a requirements.txt listing 'ollama'; development setup uses uv and ruff.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The tool is built around Ollama, supporting both local models (localhost:11434) and cloud models (ollama.com), with the last used model saved automatically. -- evidence: [README.md#L75-L78](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L75-L78), [README.md#L34-L35](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L34-L35), [README.md#L73-L73](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L73-L73)
  - [observation/documented] Piped input is supported, e.g. 'cat error.log | ducky "what's wrong here?"' or piping git diff for summarization. -- evidence: [README.md#L145-L145](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L145-L145), [README.md#L41-L47](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L41-L47), [README.md#L147-L150](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L147-L150)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run 'uv sync', run via 'uv run ducky', and lint with 'uv run ruff check .'. -- evidence: [README.md#L285-L287](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L285-L287), [README.md#L294-L295](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L294-L295), [README.md#L290-L291](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L290-L291)
- skills-patterns (1 claim(s)):
  - [observation/documented] Crumbs are saved command shortcuts supporting ${VAR} and $var placeholder styles, invoked by name with positional arguments that substitute into the stored command. -- evidence: [README.md#L107-L107](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L107-L107), [README.md#L185-L185](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L185-L185), [README.md#L86-L86](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L86-L86), [README.md#L182-L183](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L182-L183), [README.md#L175-L175](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L175-L175)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI offers an interactive REPL launched with 'ducky' and a single-shot mode where a positional prompt yields one command suggestion that is copied to the clipboard. -- evidence: [README.md#L19-L19](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L19-L19), [README.md#L137-L137](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L137-L137), [README.md#L16-L16](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L16-L16), [README.md#L205-L211](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L205-L211), [README.md#L133-L135](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L133-L135), [README.md#L131-L131](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L131-L131)
  - [observation/documented] CLI flags include --directory/-d to preload code, --model/-m, --local/-l (qwen3 default), and --yolo/-y to auto-run commands without confirmation. -- evidence: [README.md#L22-L24](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L22-L24), [README.md#L80-L82](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L80-L82), [README.md#L205-L211](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L205-L211)
- memory-state (1 claim(s)):
  - [observation/documented] Data is stored under ~/.ducky/ in files for prompt history, a JSON conversation log, user preferences including last model, and saved crumbs (crumbs.json). -- evidence: [README.md#L268-L268](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L268-L268), [README.md#L270-L275](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L270-L275)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requirements are Ollama (local or cloud) and Python 3.10+; the requirements.txt lists 'ollama'. -- evidence: [README.md#L34-L35](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/README.md#L34-L35), [requirements.txt#L1-L1](https://github.com/ParthSareen/ducky/blob/e9c8f5f98bf4c0da1c5271ad88f98a1b0ecf1ac1/requirements.txt#L1-L1)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](ducky.detail.md) for every claim.)

Metadata and full claim list: [full detail](ducky.detail.md)
Human notes ([notes](ducky.notes.md), never overwritten by build)

[Back to map index](../../index.md)
