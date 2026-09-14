# Initial corpus release validation

Checked 2026-09-14T06:32:11.880169+00:00 against the locally collected corpus. The private workbench contains all **1,366 initial directory entries**, **990 repository profiles**, and **12,365 source-linked claims**. This is a documented feature map for design and coding research; source coverage remains explicit on every profile.

| Measure | Result |
|---|---:|
| All the Agents backing rows / published rows / captured entry pages | 1,347 / 828 / 1,366 |
| Distinct current repository identities / former-name aliases | 1,018 / 34 |
| Verified immutable source packages and current profiles | 990 |
| Current identities with an explicit collection failure | 28 |
| Documentation-derived / code-inspected claims | 12,319 / 46 |
| Complete / partial selections under the collector's file policy | 454 / 536 |
| Distinct cited original-source spans checked / mismatches | 24,196 / 0 |
| Generated Markdown files checked / broken local links | 6,155 / 0 |
| Largest directory orientation | 400 words |
| Offline release tests on Windows, Python 3.12 | 396 passed; 3 skipped; 523.98 seconds |

The original directory is frozen at [backing commit 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/tree/0709cccb49aff08a4b10beb95a214005a810a363). The three views have 105 discrepancies, retained in the map. Entry-to-repository links, current repository identities, and renamed identities have different denominators; the machine-readable [release summary](evidence/release-summary.json) keeps them separate.

## Evidence and limits

Every current claim appears in the generated map. Every current accepted proposal has a matching passing source-review receipt and matches its sealed dossier field-for-field. The [990 accepted proposals and source-review receipts](evidence/current-source-reviews.jsonl) preserve the exact proposal, snapshot, dossier seal, actual applied kernel operation and fresh GLM verdict. Summary-only kernel no-ops retain the earlier applied operation; the reviewed proposal's operation is preserved separately. These are model assessments, not proof that a product behaves as documented.

A separate commissioned Claude assessment covered a risk-oriented sample of 23 profiles, 283 claims and 23 summaries, plus the two selection guides and implementation changes. Corrections changed 16 sampled claims and 12 summaries; subsequent checks verified the actual applied artifacts. Initial findings, withdrawn false findings and later missed-citation corrections remain in the local execution record. This sample does not support a library-wide accuracy estimate.

Most claims come from repository documentation. Code-inspected means inspection of captured source, not execution or a benchmark. A complete *selection* means the collector exhausted its eligible file selection under its policy; it does not establish complete feature discovery. One profile, `entropy-research/slate-plan-mode`, contains only a one-line README title and zero feature claims. Unknown facets remain unknown. Collection failures report the observed error; HTTP 404 does not establish whether a repository was removed or made private.

The full `pr` audit covered every initialized wiki partition, searched for orphan partitions, and checked current dossier/kernel correspondence. All structural checks passed. **The raw credential-pattern scan returns exit 3:** two file flags cover four literal PEM markers in documentation templates/instructions, with `MIIE...` or `...` placeholder bodies and no actual key material in the matched spans. A separate source assessor reviewed these exact spans; the parent rechecked the source and kernel-file hashes and complete match set. The [raw audit](evidence/raw-corpus-audit.json) remains unchanged, and the [narrow adjudication](evidence/credential-placeholder-adjudication.json) binds these four examples to exact bytes. Any changed bytes, new match, additional file or other error requires fresh review; no scanner rule or source was changed. This is a reviewed false positive, not a claim that the raw scanner passed. All 72 vendored wiki files match pinned commit `9307cae7b0d37e6ae9fa166e9dddeadf648aae87`. The synthetic two-class demonstration passed through the real kernel with no live network or models. Three HTML captures were refreshed at their original commits using source-preserving text storage; their older captures remain immutable. A whole-current-library span check found zero mismatches.

## Reproduce and maintain

```sh
uv run --python 3.12 --extra dev python -m pytest tests -q
uv run --python 3.12 python scripts/verify_vendor.py
uv run --python 3.12 python -m map_agents --root corpus audit --level pr
uv run --python 3.12 python -m map_agents --root corpus query "memory orchestration" --limit 5 --max-chars 2500
```

The memory, orchestration and evaluation queries scanned the complete generated search surface, returned current results, and stayed within their 2,500-character excerpt budgets. Lookup freshness compares the dossier with the latest **locally collected** snapshot; lookup does not contact GitHub HEAD. Hosted Windows/Linux CI checks the published commit; its result is available in [Actions](https://github.com/tuckerebc-max/map-the-agents/actions).

Daily hosted maintenance handles bounded directory, public-link intake, metadata, source collection and map refresh. Feature distillation uses the separately configured local population pipeline. No model credential is installed in GitHub, and live WhatsApp or account-wide research hooks are not connected. Producers must submit links through the documented intake/dispatch paths; supplied private exports remain local. See [operations](operations.md) and [population](population.md).
