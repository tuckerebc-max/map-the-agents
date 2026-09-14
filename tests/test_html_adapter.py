"""The trusted worker adapter must accept the same real HTML evidence as the wiki gate."""
import io
import json
import pytest
from map_agents import core,lunaroute,wiki,workers
from test_html_locators import _snap,SHA1

@pytest.mark.parametrize('path',['index.html','page.htm'])
def test_real_html_packet_through_adapter_and_kernel(tmp_path,monkeypatch,capsys,path):
    root=tmp_path/'corpus';key='org-a/adapter';_snap(root,key,SHA1,path)
    prepared=wiki.prepare(root,key);packet=wiki.load_packet(root,root/prepared['packet'])
    selected,_=lunaroute._select_slices(packet['slices'],lunaroute.MAX_PROMPT_CHARS)
    idx=next(i for i,s in enumerate(selected,1) if 'DISTINCTIVE_CODE_FACT' in s['text'])
    reply={'summary':'An HTML page with an inline JavaScript function.', 'claims':[{
        'facet':'components','kind':'observation','basis':'code-inspected',
        'text':'The inline script defines computeAnswer, returning the number 42.', 'slices':[idx]}]}
    def fake_transport(request,timeout):
        return 200,json.dumps({'choices':[{'message':{'content':json.dumps(reply)},'finish_reason':'stop'}]}).encode()
    monkeypatch.setenv('LUNAROUTE_API_KEY','offline-fixture-only')
    monkeypatch.setattr(lunaroute,'_transport',fake_transport)
    rc=lunaroute.main(['--quarantine-invalid-claims'],stdin=io.BytesIO(core.dump_json(workers.envelope(root,packet))))
    captured=capsys.readouterr();assert rc==0,captured.err
    proposal=json.loads(captured.out);assert len(proposal['claims'])==1
    pp=root/'proposals'/'accepted.json';pp.write_bytes(core.dump_json(proposal))
    wiki.apply(root,root/prepared['packet'],pp)
    dossier=wiki.load_dossier(root,key)
    assert dossier['claims'][0]['basis']=='code-inspected'
    assert dossier['claims'][0]['locators'][0]['line_start']==17
