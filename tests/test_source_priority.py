"""A bounded snapshot should spend scarce slots on product architecture evidence."""
import json
from map_agents import collect, core
from test_collect import API, SHA1, FakeTransport, js, repo_routes


def test_runtime_docs_precede_contributor_rules_at_real_snapshot_boundary(tmp_path):
    files = {
        'README.md': b'# Agent\nA command line agent.\n',
        'AGENTS.md': b'# Contributor\nRun unit tests before submitting.\n',
        'CLAUDE.md': b'# Contribution\nUse format checks.\n',
        'docs/sandbox.md': b'# Runtime isolation\nTool execution runs in a sandbox.\n',
        'docs/architecture.md': b'# Architecture\nThe runtime dispatches tools.\n',
    }
    result = collect.snapshot(tmp_path, 'org/agent', 3, 10000, transport=FakeTransport(repo_routes('org/agent', SHA1, files)))
    manifest = json.loads((tmp_path / result['dir'] / 'snapshot.json').read_bytes())
    assert {f['path'] for f in manifest['files']} == {'README.md', 'docs/sandbox.md', 'docs/architecture.md'}
    assert {f['path'] for f in manifest['omitted']} == {'AGENTS.md', 'CLAUDE.md'}
    assert manifest['selection']['complete'] is False


def test_explicit_contributor_selection_is_still_respected(tmp_path):
    files = {'README.md': b'# Agent\n', 'AGENTS.md': b'# Developer policy\n', 'docs/architecture.md': b'# Runtime\n'}
    result = collect.snapshot(tmp_path, 'org/agent', 2, 10000, paths=['AGENTS.md'], strict_explicit=True,
                              transport=FakeTransport(repo_routes('org/agent', SHA1, files)))
    manifest = json.loads((tmp_path / result['dir'] / 'snapshot.json').read_bytes())
    assert {f['path'] for f in manifest['files']} == {'README.md', 'AGENTS.md'}


def test_runtime_mdx_is_captured_as_text_without_execution(tmp_path):
    docs = b'# Memory\n<Widget>persistent checkpoints</Widget>\n'
    files = {'README.md': b'# Agent\n', 'AGENTS.md': b'# Contributor\n', 'site/src/content/docs/memory.mdx': docs}
    result = collect.snapshot(tmp_path, 'org/agent', 2, 10000, transport=FakeTransport(repo_routes('org/agent', SHA1, files)))
    manifest = json.loads((tmp_path / result['dir'] / 'snapshot.json').read_bytes())
    runtime = next(f for f in manifest['files'] if f['path'].endswith('.mdx'))
    assert (tmp_path / result['dir'] / runtime['stored']).read_bytes() == docs
    assert [f['path'] for f in manifest['omitted']] == ['AGENTS.md']


def test_official_numeric_repository_identity_survives_snapshot_and_record(tmp_path):
    routes = repo_routes('org/agent', SHA1, {'README.md': b'# Agent\n'})
    meta = json.loads(routes[f'{API}/repos/org/agent'].body)
    meta['id'] = 983715534
    routes[f'{API}/repos/org/agent'] = js(meta)
    result = collect.snapshot(tmp_path, 'org/agent', 2, 10000, transport=FakeTransport(routes))
    manifest = json.loads((tmp_path / result['dir'] / 'snapshot.json').read_bytes())
    assert manifest['repository_id'] == 983715534
    assert core.load_repos(tmp_path)['org/agent']['repository_id'] == 983715534
