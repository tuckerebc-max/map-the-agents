"""Large repository trees must not prevent bounded root-document evidence capture."""
import json
import pytest
from map_agents import collect
from test_collect import API, SHA1, FakeTransport, js, repo_routes

def oversized_tree_routes():
    routes=repo_routes('org/large',SHA1,{'README.md':b'# Large repository\nA runtime with pluggable tools.\n'})
    recursive=f'{API}/repos/org/large/git/trees/{SHA1}?recursive=1'
    shallow=recursive.split('?')[0]
    routes[shallow]=routes[recursive]
    routes[recursive]=collect.Response(200,b' '+b'x'*collect.MAX_API_BYTES)
    return routes,recursive,shallow

def test_large_tree_still_captures_verified_readme_with_partial_coverage(tmp_path):
    routes,recursive,shallow=oversized_tree_routes(); transport=FakeTransport(routes)
    result=collect.snapshot(tmp_path,'org/large',max_files=2,max_bytes=1000,transport=transport)
    manifest=json.loads((tmp_path/result['dir']/'snapshot.json').read_bytes())
    assert [f['path'] for f in manifest['files']]==['README.md']
    assert manifest['repository']['complete'] is False
    assert manifest['repository']['tree_truncated'] is True
    assert recursive in transport.urls('api.github.com') and shallow in transport.urls('api.github.com')

def test_large_tree_does_not_silently_drop_requested_nested_code(tmp_path):
    routes,_,_=oversized_tree_routes()
    with pytest.raises(collect.InvalidPath,match='path not in tree'):
        collect.snapshot(tmp_path,'org/large',max_files=2,max_bytes=1000,paths=['src/agent.py'],transport=FakeTransport(routes))

def test_rate_limit_does_not_trigger_alternative_tree_requests(tmp_path):
    routes,recursive,shallow=oversized_tree_routes();routes[recursive]=js({},429)
    transport=FakeTransport(routes)
    with pytest.raises(collect.FetchFailed,match='http-429'):
        collect.snapshot(tmp_path,'org/large',max_files=2,max_bytes=1000,transport=transport)
    assert shallow not in transport.urls('api.github.com')
