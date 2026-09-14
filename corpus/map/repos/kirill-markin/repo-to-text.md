# kirill-markin/repo-to-text

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9a397eb6ee6d @ 4b12a9b7f413642a

## Summary (orientation draft, not independently verified)

The evidence documents repo-to-text, a pip-installable CLI that converts a directory's tree and file contents into a single XML-tagged text file for sharing with LLMs, with options, YAML settings, and Docker usage described in the README.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Behavior is customizable via a .repo-to-text-settings.yaml file; the tool works without it by default, and --create-settings refuses to overwrite an existing settings file. -- evidence: [README.md#L103-L103](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L103-L103), [README.md#L171-L171](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L171-L171)
  - [observation/documented] Settings support gitignore-import-and-ignore, ignore-tree-and-content, ignore-content, wildcard patterns with ! negation, and an optional maximum_word_count_per_file that splits output into numbered part files. -- evidence: [README.md#L226-L230](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L226-L230), [README.md#L220-L222](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L220-L222), [README.md#L207-L214](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L207-L214), [README.md#L203-L205](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L203-L205)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: local development setup is via cloning the repo and running pip install -e ".[dev]"; tests run with pytest, and dev dependencies include pytest, black, mypy, isort, build, twine, and pylint. -- evidence: [README.md#L242-L242](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L242-L242), [README.md#L282-L284](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L282-L284), [README.md#L270-L276](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L270-L276), [README.md#L253-L255](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L253-L255)
  - [observation/documented] Repository development practice: a Docker workflow is documented using docker compose build and docker compose run --rm repo-to-text, with the container mounting the home directory at /home/user. -- evidence: [README.md#L143-L145](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L143-L145), [README.md#L137-L139](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L137-L139), [README.md#L167-L167](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L167-L167)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product provides a terminal command, repo-to-text (also runnable as `flatten`), that converts a directory's structure and contents into one text file. -- evidence: [README.md#L67-L69](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L67-L69), [README.md#L3-L3](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L3-L3), [README.md#L73-L75](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L73-L75)
  - [observation/documented] Generated output uses XML tags, including a directory_structure section and per-file content blocks tagged with the file's full path. -- evidence: [README.md#L30-L30](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L30-L30), [README.md#L21-L28](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L21-L28), [README.md#L35-L37](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L35-L37), [README.md#L15-L15](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L15-L15)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The package requires Python >= 3.10 and core dependencies setuptools, pathspec, argparse, and PyYAML at specified minimum versions. -- evidence: [README.md#L259-L264](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L259-L264)
  - [observation/documented] The project is distributed via pip (installable and upgradable with pip install/upgrade repo-to-text) and is MIT licensed. -- evidence: [README.md#L53-L55](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L53-L55), [README.md#L59-L61](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L59-L61), [README.md#L300-L300](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L300-L300)
- limitations (1 claim(s)):
  - [inference/documented] The tool appears intended for sharing code with LLMs for development and debugging, per the README's stated purpose. -- evidence: [README.md#L3-L3](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](repo-to-text.detail.md) for every claim.)

Metadata and full claim list: [full detail](repo-to-text.detail.md)
Human notes ([notes](repo-to-text.notes.md), never overwritten by build)

[Back to map index](../../index.md)
