"""Regenerate JSON Schemas from the runtime's Pydantic contracts."""

import argparse
import json
from pathlib import Path

from rcw_core import models


def export_schemas(check=False):
    root = Path(__file__).resolve().parents[1] / "schemas/v1"
    schemas = {
        "corpus": models.CorpusConfig,
        "source-metadata": models.Metadata,
        "ingest-proposal": models.IngestProposal,
        "analysis-proposal": models.AnalysisProposal,
        "answer-proposal": models.AnswerProposal,
        **models.TABLES,
    }
    differences = []
    for name, model in schemas.items():
        path = root / (name + ".schema.json")
        text = json.dumps(model.model_json_schema(), ensure_ascii=False, indent=2) + "\n"
        if check:
            if not path.exists() or path.read_text() != text:
                differences.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    return {"ok": not differences, "schemas": len(schemas), "differences": differences}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    result = export_schemas(parser.parse_args().check)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ok"] else 1)
