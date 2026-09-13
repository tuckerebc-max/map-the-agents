# Sources and dependency attribution

The catalog source is [All the Agents](https://alltheagents.org/), with its public
[published index](https://alltheagents.org/agents.json) and the
[backing repository](https://github.com/prime-radiant-inc/alltheagents.org).
The collector pins `_data/agents.json` to a commit. Published and backing counts can differ;
they are separate observations, not interchangeable completeness claims. Each retained catalog
entry keeps its original locator and identity. The optional `catalog --published` command records
the published index digest/count separately.

The existing [Research Corpus Wiki](https://github.com/tuckerebc-max/research-corpus-wiki)
skill and kernel are vendored at commit `9307cae7b0d37e6ae9fa166e9dddeadf648aae87`, unmodified,
under [Apache-2.0](vendor/research-corpus-wiki/LICENSE). Preserve its
[third-party notices](vendor/research-corpus-wiki/THIRD_PARTY_NOTICES.md) and the per-file
[vendor pin](vendor-pin.json). An upstream change is outside this workbench's publication scope.

Collected repository text remains attributable to its original repository, commit, path and
line range. Source licenses are recorded when supplied by GitHub; unknown licenses remain
unknown. Inclusion in the map does not relicense source material or establish endorsement.

Automation behavior follows GitHub's [event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
and [workflow trigger documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).
