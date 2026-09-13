"""Run a synthetic mixed corpus through ingestion, synthesis, audit, and both views."""

import argparse
import json
import shutil
from pathlib import Path

from rcw_core import api


def run_demo(output):
    output = Path(output).resolve()
    if output.exists() and any(output.iterdir()):
        raise ValueError("Demo output must be empty")
    output.mkdir(parents=True, exist_ok=True)
    fixture = Path(__file__).resolve().parents[1] / "assets/demo"
    shutil.copytree(fixture / "sources", output / "sources")
    expected = json.loads((fixture / "claims.json").read_text())
    root = output / "wiki"
    api.init_corpus(root, output / "sources", profile="mixed")
    first = None
    for item in api.sync_plan(root)["pending"]:
        packet = api.ingest_prepare(root, item["key"])
        claim = expected[item["path"]]
        proposal = {
            "schema_version": "1.0",
            "operation_id": packet["operation_id"],
            "claims": [
                {
                    "key": "main",
                    "text": claim["text"],
                    "slice_ids": [packet["slices"][-1]["id"]],
                    "evidence_type": claim["evidence_type"],
                    "scope": claim.get("scope", {}),
                }
            ],
            "entities": [],
            "relationships": [],
        }
        api.ingest_apply(root, packet["operation_id"], proposal)
        if first is None:
            first = item["key"], proposal
    packet = api.ingest_prepare(root, first[0])
    repeat = {**first[1], "operation_id": packet["operation_id"]}
    repeat_result = api.ingest_apply(root, packet["operation_id"], repeat)
    packet = api.analyze_prepare(root, scope="full", access="public")
    originals = [c for c in packet["claims"] if c["lineage_status"] == "original_available"]
    assertions = [{"text": c["text"], "claim_ids": [c["id"]]} for c in originals]
    synthesis = {
        "schema_version": "1.0",
        "operation_id": packet["operation_id"],
        "pages": [
            {"key": "demo-map", "title": "Evidence map", "page_type": "theme", "assertions": assertions}
        ],
        "relationships": [],
        "gaps": [],
    }
    api.analyze_apply(root, packet["operation_id"], synthesis)
    report = api.audit(root, "pr")
    public = api.render(root, output / "public", access="public")
    internal = api.render(root, output / "internal", access="restricted")
    quartz = api.render(root, output / "quartz", adapter="quartz", access="public")
    (output / "citations.json").write_text(
        json.dumps(api.export_citations(root, "csl-json", "public"), indent=2) + "\n"
    )
    result = {
        "synthetic": True,
        "audit": report,
        "repeat_ingest_changed": repeat_result["changed"],
        "public_pages": public["pages"],
        "internal_pages": internal["pages"],
        "quartz_content": quartz["output"],
        "root": str(root),
    }
    (output / "demo-result.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    print(json.dumps(run_demo(parser.parse_args().output), indent=2))
