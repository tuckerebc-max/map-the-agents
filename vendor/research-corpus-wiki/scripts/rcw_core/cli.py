"""Command line for local evidence operations. No remote writes are implicit."""

import json
from pathlib import Path
from typing import Annotated

import typer

from . import api
from .storage import RCWError

app = typer.Typer(help="Build and maintain a source-grounded research corpus wiki.", no_args_is_help=True)
ingest_app = typer.Typer(help="Prepare evidence packets and apply validated extraction proposals.")
analyze_app = typer.Typer(help="Prepare and apply source-grounded synthesis.")
ask_app = typer.Typer(help="Retrieve original slices and validate a corpus answer.")
app.add_typer(ingest_app, name="ingest")
app.add_typer(analyze_app, name="analyze")
app.add_typer(ask_app, name="ask")


def emit(value):
    typer.echo(json.dumps(value, ensure_ascii=False, indent=2))


def read_proposal(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


@app.command("init")
def initialize(
    root: Path,
    sources: Annotated[Path, typer.Option("--sources")],
    profile: str = "mixed",
    access: str = "internal",
    title: str = "Research corpus",
):
    emit(api.init_corpus(root, sources, profile, access, title))


@app.command()
def inventory(root: Path):
    emit(api.inventory(root))


@app.command()
def status(root: Path):
    emit(api.status(root))


@app.command()
def sync(root: Path):
    """Plan resumable ingestion of new and changed packages."""
    emit(api.sync_plan(root))


@ingest_app.command("prepare")
def ingest_prepare(root: Path, package: str):
    emit(api.ingest_prepare(root, package))


@ingest_app.command("apply")
def ingest_apply(root: Path, operation: str, proposal: Path):
    emit(api.ingest_apply(root, operation, read_proposal(proposal)))


@analyze_app.command("prepare")
def analyze_prepare(root: Path, scope: str = "changed", access: str = "restricted", limit: int = 200):
    emit(api.analyze_prepare(root, scope, access, limit))


@analyze_app.command("apply")
def analyze_apply(root: Path, operation: str, proposal: Path):
    emit(api.analyze_apply(root, operation, read_proposal(proposal)))


@ask_app.command("prepare")
def ask_prepare(root: Path, question: str, access: str = "internal", limit: int = 40):
    emit(api.ask_prepare(root, question, access, limit))


@ask_app.command("complete")
def ask_complete(root: Path, operation: str, proposal: Path, file_answer: bool = False):
    emit(api.ask_complete(root, operation, read_proposal(proposal), file_answer))


@app.command()
def audit(root: Path, level: str = "working"):
    result = api.audit(root, level)
    emit(result)
    if not result["ok"]:
        raise typer.Exit(3)


@app.command()
def render(root: Path, output: Path, adapter: str = "html", access: str = "internal"):
    emit(api.render(root, output, adapter, access))


@app.command("export")
def export(root: Path, output: Path, format: str = "csl-json", access: str = "internal"):
    result = api.export_citations(root, format, access)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n" if isinstance(result, list) else result
    if output.exists():
        raise RCWError("RCW_OUTPUT_EXISTS", "Choose a new export path")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    emit({"output": str(output)})


@app.command("review-packet")
def review_packet(root: Path):
    emit(api.review_packet(root))


@app.command("recover")
def recover(root: Path):
    emit(api.recover(root))


@app.command("reindex")
def reindex(root: Path):
    emit(api.reindex(root))


def main():
    try:
        app()
    except (RCWError, OSError, ValueError) as error:
        code = getattr(error, "code", "RCW_INPUT_ERROR")
        typer.echo(json.dumps({"error": code, "message": str(error)}), err=True)
        raise SystemExit(3) from None


@app.command("metadata")
def metadata(root: Path, key: str, file: Path):
    """Register source metadata in the wiki without editing original sources."""
    emit(api.register_metadata(root, key, read_proposal(file)))
