import json
import math
import sys

import pytest

from map_agents import __main__ as cli, collect, core, intake, workers
from test_collect import FakeTransport
from test_workers import clone, corpus, routes


@pytest.mark.parametrize('field,value', [('max_seconds', math.inf), ('worker_seconds', math.nan), ('max_files', -1), ('max_proposal_bytes', -2)])
def test_nonfinite_or_negative_limits_are_rejected(field, value):
    with pytest.raises(core.WorkbenchError):
        workers.Limits(**{field: value})


def test_zero_wall_budget_does_not_start_catalog(tmp_path):
    transport = FakeTransport(routes())
    result = workers.maintain(tmp_path, workers.Limits(max_seconds=0), transport=transport)
    assert result['catalog'] is None
    assert result['snapshots'] == []
    assert result['stopped'] == 'time-budget'


def test_failure_attempts_respect_repository_limit(tmp_path, monkeypatch):
    intake.ingest(tmp_path, '\n'.join(f'https://github.com/org/item{i}' for i in range(5)), 'manual', 'test')
    attempted = []
    def failing(root, repo, *_args, **_kwargs):
        attempted.append(repo)
        raise collect.FetchFailed('http-404')
    monkeypatch.setattr(collect, 'snapshot', failing)
    result = workers.maintain(tmp_path, workers.Limits(catalog_entries=0, max_repos=2))
    assert len(attempted) == 2
    assert len(result['failures']) == 2
    assert result['status'] == 'degraded'


def test_attempt_cursor_survives_interrupted_run(tmp_path, monkeypatch):
    intake.ingest(tmp_path, 'https://github.com/org/alpha https://github.com/org/beta', 'manual', 'test')
    class Interrupted(BaseException):
        pass
    attempted = []
    def interrupted(_root, repo, *_args, **_kwargs):
        attempted.append(repo)
        raise Interrupted()
    monkeypatch.setattr(collect, 'snapshot', interrupted)
    for _ in range(2):
        with pytest.raises(Interrupted):
            workers.maintain(tmp_path, workers.Limits(catalog_entries=0, max_repos=1))
    assert attempted == ['org/alpha', 'org/beta']


def test_cli_preserves_delimiters_inside_configured_command(tmp_path, monkeypatch, capsys):
    commands = []
    def worker(_root, argv, *_args, **_kwargs):
        commands.append(argv)
        return {'outcome': 'manual'}
    monkeypatch.setattr(workers, 'run_worker', worker)
    assert cli.main(['--root', str(tmp_path), 'worker', '--', 'adapter', '--', 'argument']) == 0
    assert commands == [['adapter', '--', 'argument']]


def test_missing_executable_is_receipted_without_argv(clone):
    marker = 'private-argument-MARKER'
    with pytest.raises(workers.WorkerFailed):
        workers.run_worker(clone, ['nonexistent-workbench-executable', marker], workers.Limits(build=False), repo='org-a/alpha')
    receipt = json.loads((clone / workers.QUEUE_FILE).read_text(encoding='utf-8'))
    assert receipt['runs'][-1]['outcome'] == 'failed'
    assert marker not in json.dumps(receipt)


def test_rejected_model_payload_is_not_copied_to_receipts(clone):
    marker = 'PRIVATE-MARKER-IN-MODEL-OUTPUT'
    script = 'import json; print(json.dumps({' + repr(marker) + ': 1}))'
    with pytest.raises(workers.WorkerFailed):
        workers.run_worker(clone, [sys.executable, '-c', script], workers.Limits(build=False), repo='org-a/alpha')
    assert marker not in (clone / workers.QUEUE_FILE).read_text(encoding='utf-8')
