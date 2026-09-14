"""Selected maintenance audits never masquerade as a release-wide audit."""
import json
import pytest
from map_agents import core, wiki
from test_partitioned_wiki import snap, sha_for, good_proposal, write

def test_selected_partition_and_empty_selection_are_explicit_while_full_detects_other_damage(tmp_path):
    keys=['scope/one','scope/two'];wiki.enable_partitioned(tmp_path)
    for i,key in enumerate(keys):
        snap(tmp_path,key,sha_for(i+1));prepared=wiki.prepare(tmp_path,key)
        packet=json.loads((tmp_path/prepared['packet']).read_bytes())
        wiki.apply(tmp_path,tmp_path/prepared['packet'],write(tmp_path/f'p{i}.json',good_proposal(packet)))
    other=wiki._kernel_root(tmp_path,keys[1])/'data/claims.jsonl'
    other.write_bytes(b'')
    selected=wiki.audit(tmp_path,repos=[keys[0]])
    assert selected['ok'] is True and set(selected['repos'])=={keys[0]}
    assert selected['scope']=={'kind':'selected','repositories':[keys[0]]}
    empty=wiki.audit(tmp_path,repos=[])
    assert empty['ok'] and empty['scope']['kind']=='selected' and not empty['partitions']
    assert wiki.audit(tmp_path)['ok'] is False

def test_unknown_selected_key_is_not_silently_audited_as_empty(tmp_path):
    core.init(tmp_path);wiki.enable_partitioned(tmp_path)
    with pytest.raises(wiki.WikiError,match='known repository keys'):
        wiki.audit(tmp_path,repos=['missing/repo'])

def test_shared_layout_audit_stays_full_when_selection_is_supplied(tmp_path):
    snap(tmp_path,'scope/one',sha_for(1))
    result=wiki.audit(tmp_path,repos=[])
    assert result['scope']['kind']=='full'
