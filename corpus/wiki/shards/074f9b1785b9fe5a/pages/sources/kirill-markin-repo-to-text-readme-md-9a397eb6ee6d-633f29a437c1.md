---
access: public
aliases: []
claim_ids:
- clm_62db8d6197f35b25c8b2471fb7f5851457f66aded77d7d2b516406698176485f
- clm_65942994cee6d218e971d11c0927054cdfd076252ee9533c24a531e7cb51ccad
- clm_7d18e587e9c8a46425967aae566b4e35d7bc9cb34174b56954f0139fb4858d2b
- clm_80ca77b5a90ec682fec8b1b4e0b9588ed5be47daa515702375ee93d1053af2e4
- clm_87f33baa606bd0debedd24f599f19e4c58f8affd606dfd13ca97c72875059dab
- clm_ca571949ca8177636d559e8bc28fcc1eef7be7e82956827d053f0770aed4012a
- clm_cf1cd7f78ba30b1f4449eb0b74d9d629e0cd6145202f36e1bb5ef886df39b7f2
- clm_e48bd10a8df600a3d0cfce5fa201ab0691f9ebfeafd6adb58ddcfa75357bf98b
- clm_ec92182ab957a24278a3e697f58644a8a98e998ee9b5557141415352c759aa2b
- clm_f5dbce7a689cf5d19795a56837a06c992598f10eb6493e8ac151f42f7a1ca6ec
- clm_fd73e001e55583ab9685ab2ca1a08c928bcc3586a6852e0d86e07bdfd90ef94e
maturity: draft
page_id: pg_839a4ddd0c555b829de6633f29a437c1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_423feb6043235e5fb84ccdf17a8ed475
title: kirill-markin/repo-to-text/README.md @ 9a397eb6ee6d
updated_at: '2026-09-14T04:03:30Z'
---

# kirill-markin/repo-to-text/README.md @ 9a397eb6ee6d

<!-- rcw:begin owner=source:src_423feb6043235e5fb84ccdf17a8ed475 block=evidence -->
- Repository development practice: a Docker workflow is documented using docker compose build and docker compose run --rm repo-to-text, with the container mounting the home directory at /home/user. [@claim:clm_62db8d6197f35b25c8b2471fb7f5851457f66aded77d7d2b516406698176485f]
- The product provides a terminal command, repo-to-text (also runnable as `flatten`), that converts a directory's structure and contents into one text file. [@claim:clm_65942994cee6d218e971d11c0927054cdfd076252ee9533c24a531e7cb51ccad]
- The package requires Python >= 3.10 and core dependencies setuptools, pathspec, argparse, and PyYAML at specified minimum versions. [@claim:clm_7d18e587e9c8a46425967aae566b4e35d7bc9cb34174b56954f0139fb4858d2b]
- Repository development practice: local development setup is via cloning the repo and running pip install -e ".[dev]"; tests run with pytest, and dev dependencies include pytest, black, mypy, isort, build, twine, and pylint. [@claim:clm_80ca77b5a90ec682fec8b1b4e0b9588ed5be47daa515702375ee93d1053af2e4]
- Settings support gitignore-import-and-ignore, ignore-tree-and-content, ignore-content, wildcard patterns with ! negation, and an optional maximum_word_count_per_file that splits output into numbered part files. [@claim:clm_87f33baa606bd0debedd24f599f19e4c58f8affd606dfd13ca97c72875059dab]
- The tool appears intended for sharing code with LLMs for development and debugging, per the README's stated purpose. [@claim:clm_ca571949ca8177636d559e8bc28fcc1eef7be7e82956827d053f0770aed4012a]
- By default the tool writes a timestamped file named repo-to-text_YYYY-MM-DD-HH-MM-SS-UTC.txt in the current directory and also copies the result to the clipboard. [@claim:clm_cf1cd7f78ba30b1f4449eb0b74d9d629e0cd6145202f36e1bb5ef886df39b7f2]
- Generated output uses XML tags, including a directory_structure section and per-file content blocks tagged with the file's full path. [@claim:clm_e48bd10a8df600a3d0cfce5fa201ab0691f9ebfeafd6adb58ddcfa75357bf98b]
- CLI options include --output-dir, --create-settings/--init, --debug, --stdout, and an optional positional input directory argument. [@claim:clm_ec92182ab957a24278a3e697f58644a8a98e998ee9b5557141415352c759aa2b]
- Behavior is customizable via a .repo-to-text-settings.yaml file; the tool works without it by default, and --create-settings refuses to overwrite an existing settings file. [@claim:clm_f5dbce7a689cf5d19795a56837a06c992598f10eb6493e8ac151f42f7a1ca6ec]
- The project is distributed via pip (installable and upgradable with pip install/upgrade repo-to-text) and is MIT licensed. [@claim:clm_fd73e001e55583ab9685ab2ca1a08c928bcc3586a6852e0d86e07bdfd90ef94e]
<!-- rcw:end owner=source:src_423feb6043235e5fb84ccdf17a8ed475 block=evidence -->

## Researcher notes

