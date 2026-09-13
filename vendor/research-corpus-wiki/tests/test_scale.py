"""Inventory throughput fixtures; not a claim about full 5,000-source synthesis."""

import json
import time

import pytest


@pytest.mark.parametrize("count", [50, 500, 5000])
def test_inventory_scale(api, tmp_path, count):
    sources = tmp_path / "sources"
    sources.mkdir()
    metadata = {
        "title": "Synthetic scale fixture",
        "creator": "Fixture generator",
        "source_type": "report",
        "access": "public",
    }
    for i in range(count):
        path = sources / f"source-{i:05d}.md"
        path.write_text(f"# Synthetic source {i}\n\nFixture statement number {i}.\n")
        path.with_name(path.name + ".source.json").write_text(json.dumps(metadata))
    root = tmp_path / "wiki"
    api.init_corpus(root, sources)
    started = time.perf_counter()
    report = api.inventory(root)
    elapsed = time.perf_counter() - started
    assert len(report["items"]) == count
    assert all(item["status"] == "new" for item in report["items"])
    assert elapsed < 600, f"Inventory took {elapsed:.2f}s for {count} packages"
    print(f"inventory_packages={count} elapsed_seconds={elapsed:.3f}")
