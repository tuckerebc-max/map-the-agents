import errno
from pathlib import Path, PureWindowsPath

import pytest
from rcw_core.storage import RCWError, safe_path, transaction


def test_nested_portable_path_is_a_native_corpus_target(tmp_path):
    target = safe_path(tmp_path, "data/packages.jsonl")
    assert target == tmp_path / "data" / "packages.jsonl"
    assert not target.exists()
    target.parent.mkdir()
    target.write_text("corpus data", encoding="utf-8")
    assert safe_path(tmp_path, "data/packages.jsonl").read_text(encoding="utf-8") == "corpus data"


def test_transaction_writes_nested_portable_paths(tmp_path):
    changed = transaction(tmp_path, "op_test", {"data/packages.jsonl": "{}\n"})
    assert changed == ["data/packages.jsonl"]
    assert (tmp_path / "data" / "packages.jsonl").read_bytes() == b"{}\n"
    assert (tmp_path / "state" / "operations" / "op_test" / "journal.json").is_file()
    assert transaction(tmp_path, "op_repeat", {"data/packages.jsonl": "{}\n"}) == []


@pytest.mark.parametrize(
    "relative",
    [
        "../outside.md",
        "data/../../outside.md",
        "data/../packages.jsonl",
        r"..\outside.md",
        r"data\..\outside.md",
        r"data\packages.jsonl",
        r"data/nested\packages.jsonl",
        "/outside.md",
        "C:/outside.md",
        "C:outside.md",
        "C:",
        "c:outside.md",
        "D:/outside.md",
        r"\outside.md",
        r"\\server\share\outside.md",
        "//server/share/outside.md",
        r"\\?\C:\outside.md",
        "//?/C:/outside.md",
        r"\\.\C:\outside.md",
    ],
)
def test_nonportable_or_escaping_paths_are_rejected(tmp_path, relative):
    with pytest.raises(RCWError, match="RCW_PATH_ESCAPE"):
        safe_path(tmp_path, relative)


@pytest.mark.parametrize("form", ["drive_relative", "drive_absolute_inside"])
@pytest.mark.parametrize("prefix", ["./", "././", ".//"])
def test_dot_prefixes_do_not_hide_drive_syntax(tmp_path, prefix, form):
    if form == "drive_relative":
        relative = prefix + "C:inside.md"
    else:
        absolute = (
            (tmp_path / "page.md").as_posix()
            if tmp_path.drive
            else "C:/corpus/page.md"
        )
        relative = prefix + absolute
    with pytest.raises(RCWError, match="RCW_PATH_ESCAPE"):
        safe_path(tmp_path, relative)


def test_absolute_paths_inside_corpus_are_still_rejected(tmp_path):
    target = tmp_path / "page.md"
    # Include a drive-less rooted Windows path whose resolved target is inside the corpus.
    rooted = target.as_posix().removeprefix(PureWindowsPath(target).drive)
    for relative in (str(target), target.as_posix(), rooted):
        with pytest.raises(RCWError, match="RCW_PATH_ESCAPE"):
            safe_path(tmp_path, relative)


@pytest.mark.parametrize("directory", [False, True], ids=["file", "ancestor"])
@pytest.mark.parametrize("outside", [False, True], ids=["inside", "outside"])
@pytest.mark.parametrize("exists", [False, True], ids=["dangling", "existing"])
def test_symlink_corpus_targets_are_rejected(tmp_path, symlink, directory, outside, exists):
    root = tmp_path / "wiki"
    root.mkdir()
    target = (tmp_path if outside else root) / "target"
    if exists:
        if directory:
            target.mkdir()
        else:
            target.write_text("original", encoding="utf-8")
    link = root / "link"
    symlink(link, target, target_is_directory=directory)
    with pytest.raises(RCWError, match="RCW_PATH_ESCAPE"):
        safe_path(root, "link/page.md" if directory else "link")


def test_symlink_permission_errors_are_not_broadly_skipped(tmp_path, symlink, monkeypatch):
    def denied(*args, **kwargs):
        raise PermissionError(errno.EACCES, "simulated permission failure")

    monkeypatch.setattr(Path, "symlink_to", denied)
    with pytest.raises(PermissionError, match="simulated permission failure"):
        symlink(tmp_path / "link", tmp_path / "target")


def test_required_symlink_coverage_cannot_skip_missing_privilege(tmp_path, symlink, monkeypatch):
    error = OSError("simulated missing symlink privilege")
    error.winerror = 1314

    def denied(*args, **kwargs):
        raise error

    monkeypatch.setenv("RCW_REQUIRE_SYMLINKS", "1")
    monkeypatch.setattr(Path, "symlink_to", denied)
    with pytest.raises(OSError, match="simulated missing symlink privilege"):
        symlink(tmp_path / "link", tmp_path / "target")
