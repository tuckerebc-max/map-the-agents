# kirill-markin/repo-to-text -- full detail

[Back to orientation](repo-to-text.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kirill-markin/repo-to-text/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/4b12a9b7f413642a.json](../../../wiki/dossiers/kirill-markin/repo-to-text/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/4b12a9b7f413642a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Behavior is customizable via a .repo-to-text-settings.yaml file; the tool works without it by default, and --create-settings refuses to overwrite an existing settings file. -- evidence: [README.md#L103-L103](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L103-L103), [README.md#L171-L171](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L171-L171) (`clm_f5dbce7a689cf5d19795a56837a06c992598f10eb6493e8ac151f42f7a1ca6ec`)
- [observation/documented] Settings support gitignore-import-and-ignore, ignore-tree-and-content, ignore-content, wildcard patterns with ! negation, and an optional maximum_word_count_per_file that splits output into numbered part files. -- evidence: [README.md#L226-L230](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L226-L230), [README.md#L220-L222](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L220-L222), [README.md#L207-L214](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L207-L214), [README.md#L203-L205](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L203-L205) (`clm_87f33baa606bd0debedd24f599f19e4c58f8affd606dfd13ca97c72875059dab`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: local development setup is via cloning the repo and running pip install -e ".[dev]"; tests run with pytest, and dev dependencies include pytest, black, mypy, isort, build, twine, and pylint. -- evidence: [README.md#L242-L242](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L242-L242), [README.md#L282-L284](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L282-L284), [README.md#L270-L276](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L270-L276), [README.md#L253-L255](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L253-L255) (`clm_80ca77b5a90ec682fec8b1b4e0b9588ed5be47daa515702375ee93d1053af2e4`)
- [observation/documented] Repository development practice: a Docker workflow is documented using docker compose build and docker compose run --rm repo-to-text, with the container mounting the home directory at /home/user. -- evidence: [README.md#L143-L145](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L143-L145), [README.md#L137-L139](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L137-L139), [README.md#L167-L167](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L167-L167) (`clm_62db8d6197f35b25c8b2471fb7f5851457f66aded77d7d2b516406698176485f`)
- [observation/documented] Repository development practice: AGENTS.md and CLAUDE.md each point to .cursor/rules/index.mdc for contributor instructions. -- evidence: [CLAUDE.md#L1-L1](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/CLAUDE.md#L1-L1), [AGENTS.md#L1-L1](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/AGENTS.md#L1-L1) (`clm_45cc63b92ebf2c06b05ab27b7fa071e4ae9f25ac06913bb13301198d2742640d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product provides a terminal command, repo-to-text (also runnable as `flatten`), that converts a directory's structure and contents into one text file. -- evidence: [README.md#L67-L69](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L67-L69), [README.md#L3-L3](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L3-L3), [README.md#L73-L75](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L73-L75) (`clm_65942994cee6d218e971d11c0927054cdfd076252ee9533c24a531e7cb51ccad`)
- [observation/documented] Generated output uses XML tags, including a directory_structure section and per-file content blocks tagged with the file's full path. -- evidence: [README.md#L30-L30](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L30-L30), [README.md#L21-L28](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L21-L28), [README.md#L35-L37](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L35-L37), [README.md#L15-L15](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L15-L15) (`clm_e48bd10a8df600a3d0cfce5fa201ab0691f9ebfeafd6adb58ddcfa75357bf98b`)
- [observation/documented] By default the tool writes a timestamped file named repo-to-text_YYYY-MM-DD-HH-MM-SS-UTC.txt in the current directory and also copies the result to the clipboard. -- evidence: [README.md#L77-L77](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L77-L77) (`clm_cf1cd7f78ba30b1f4449eb0b74d9d629e0cd6145202f36e1bb5ef886df39b7f2`)
- [observation/documented] CLI options include --output-dir, --create-settings/--init, --debug, --stdout, and an optional positional input directory argument. -- evidence: [README.md#L91-L91](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L91-L91), [README.md#L123-L123](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L123-L123), [README.md#L105-L105](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L105-L105), [README.md#L117-L117](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L117-L117), [README.md#L83-L83](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L83-L83) (`clm_ec92182ab957a24278a3e697f58644a8a98e998ee9b5557141415352c759aa2b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The package requires Python >= 3.10 and core dependencies setuptools, pathspec, argparse, and PyYAML at specified minimum versions. -- evidence: [README.md#L259-L264](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L259-L264) (`clm_7d18e587e9c8a46425967aae566b4e35d7bc9cb34174b56954f0139fb4858d2b`)
- [observation/documented] The project is distributed via pip (installable and upgradable with pip install/upgrade repo-to-text) and is MIT licensed. -- evidence: [README.md#L53-L55](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L53-L55), [README.md#L59-L61](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L59-L61), [README.md#L300-L300](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L300-L300) (`clm_fd73e001e55583ab9685ab2ca1a08c928bcc3586a6852e0d86e07bdfd90ef94e`)

## limitations (1 claim(s))

- [inference/documented] The tool appears intended for sharing code with LLMs for development and debugging, per the README's stated purpose. -- evidence: [README.md#L3-L3](https://github.com/kirill-markin/repo-to-text/blob/9a397eb6ee6d06f1e6647a542acc32a78c4b8fb7/README.md#L3-L3) (`clm_ca571949ca8177636d559e8bc28fcc1eef7be7e82956827d053f0770aed4012a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

