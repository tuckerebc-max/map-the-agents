import json
from pathlib import Path
import re

from map_agents import core, intake, maps


def test_all_generated_navigation_is_small_and_tail_reachable(tmp_path):
    records = {}
    for i in range(450):
        key = f"org/item{i:04}"
        records[key] = intake.new_record(key, f"https://github.com/{key}")
    records['org/item0000']['projects'] = ['project with many words ' + str(i) for i in range(600)]
    core.init(tmp_path)
    core.save_repos(tmp_path, records)
    maps.build(tmp_path)
    pages = list((tmp_path / 'map').rglob('*.md'))
    assert all(len(p.read_text(encoding='utf-8').split()) <= 2000 for p in pages)
    seen, pending = set(), [tmp_path / 'AGENTS_CORPUS.md']
    while pending:
        path = pending.pop().resolve()
        if path in seen:
            continue
        seen.add(path)
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if '://' not in target and target.split('#')[0].endswith('.md'):
                dest = (path.parent / target.split('#')[0]).resolve()
                assert dest.is_file(), target
                pending.append(dest)
    assert (tmp_path / 'map/repos/org/item0449.md').resolve() in seen
    assert maps.query(tmp_path, 'item0449')['complete']


def test_query_detects_changed_build_and_does_not_search_obsolete_pages(tmp_path):
    intake.ingest(tmp_path, 'https://github.com/org/alpha', 'manual', 'first')
    maps.build(tmp_path)
    assert maps.query(tmp_path, 'alpha')['stale_view'] is False
    intake.ingest(tmp_path, 'https://github.com/org/alpha', 'manual', 'second')
    result = maps.query(tmp_path, 'alpha')
    assert result['stale_view'] is True
    assert all(r['stale_view'] for r in result['results'])
    obsolete = tmp_path / 'map/obsolete.md'
    obsolete.write_text('onlyobsoleteword', encoding='utf-8')
    assert not maps.query(tmp_path, 'onlyobsoleteword')['results']


def test_query_is_incomplete_if_any_read_is_truncated(tmp_path, monkeypatch):
    intake.ingest(tmp_path, 'https://github.com/org/alpha', 'manual', 'first')
    maps.build(tmp_path)
    monkeypatch.setattr(maps, 'MAX_QUERY_FILE_BYTES', 10)
    assert maps.query(tmp_path, 'absent')['complete'] is False


def test_orientation_limit_counts_maximum_claims_and_footer():
    record = intake.new_record('org/alpha', 'https://github.com/org/alpha')
    record.update(status='distilled', dossier='wiki/dossiers/alpha.json')
    claim = {'facet': 'components', 'kind': 'observation', 'basis': 'documented',
             'text': ('bounded text ' * 30).strip(), 'locators': [], 'claim_id': 'claim-1'}
    dossier = {'summary': 'summary ' * 90, 'claims': [dict(claim) for _ in range(40)], 'gaps': []}
    assert len(maps._render_repo_page('org/alpha', record, dossier).split()) <= 500
