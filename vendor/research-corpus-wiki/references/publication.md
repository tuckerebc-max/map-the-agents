# Browsing and publication

## Immediate HTML view

```bash
rcw render /workbench/research-wiki /workbench/research-wiki/build/internal --adapter html --access internal
```

The result contains a responsive searchable index, typed pages, evidence cards, graph JSON, and a manifest of output hashes. It is static, needs no account or model API, and opens locally. A public view contains only public-authorized claims and their eligible pages. It excludes protected source names, paths, quotations, edges, and counts. Search operates on the visible index; use `ask prepare` for corpus-wide claim search.

The view regenerates from registered assertions. It deliberately retains handwritten research notes only in the canonical Markdown; move evidence-bearing notes through a validated proposal before publishing them. HTML text is escaped, and raw source scripts are not executable content.

A build directory is disposable. Repeat builds verify prior generated-file hashes before replacing them; edited files block replacement. Prefer a fresh output directory for each audience. Neither a static page nor a private URL is an access-control service. Publish through the workbench's authorized hosting system and preserve its access settings.

## Quartz adapter

```bash
rcw render /workbench/research-wiki /workbench/research-wiki/build/quartz-public --adapter quartz --access public
```

This creates `content/index.md`, typed Markdown pages, evidence cards, tags, wikilinks, `graph.json`, and `build-manifest.json`. It is ready as a Quartz content directory. The adapter does not install or run an unpinned renderer automatically. Use the companion `scripts/quartz_build.py` with a locally available, clean Quartz checkout and an exact commit pin; it validates that checkout and builds the generated content tree. See its `--help` for the concrete invocation. Quartz remains replaceable and never writes back to canonical records.

## Citations

```bash
rcw export /workbench/research-wiki /workbench/citations-public.json --format csl-json --access public
rcw export /workbench/research-wiki /workbench/citations-public.bib --format bibtex --access public
```

Exports use the same eligible evidence selection as views. CSL JSON is primary; BibTeX keeps legal types/status/jurisdiction in notes where necessary. Identifiers are preserved when supplied; no DOI is invented. Exports refuse to overwrite an existing path.

## Formal reports

CSL JSON, BibTeX, and generated Markdown can feed Quarto, Zettlr, Manubot, or other report workflows. v0.1 does not include a native Quarto, Wiki.js, or Jupyter Book adapter. Do not advertise an exported tree as a deployed site or a completed formal report.
