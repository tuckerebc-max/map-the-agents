from conftest import proposal, rows, source


def ingest_entity(api, root, sources, name, access="public", external=None):
    path = source(sources, name=name, access=access, identifiers={})
    packet = api.ingest_prepare(root, path.name)
    proposed = proposal(packet)
    proposed["entities"] = [
        {
            "key": "person",
            "name": "Alex Smith",
            "entity_type": "person",
            "claim_keys": ["result"],
            "external_ids": external or {},
        }
    ]
    api.ingest_apply(root, packet["operation_id"], proposed)


def test_same_name_in_different_sources_does_not_merge_identity(api, corpus):
    root, sources = corpus
    ingest_entity(api, root, sources, "first.md")
    ingest_entity(api, root, sources, "second.md")
    assert len(rows(root, "entities")) == 2


def test_shared_external_identity_retains_evidence_and_strictest_access(api, corpus):
    root, sources = corpus
    external = {"orcid": "synthetic-person-001"}
    ingest_entity(api, root, sources, "first.md", "confidential", external)
    ingest_entity(api, root, sources, "second.md", "public", external)
    entity = rows(root, "entities")[0]
    assert len(rows(root, "entities")) == 1
    assert len(entity["claim_ids"]) == 2
    assert entity["access"] == "confidential"


def test_relationship_inherits_endpoint_access_and_audit_detects_tampering(api, corpus):
    from rcw_core.audit import audit_tables
    from rcw_core.ingest import relationships
    from rcw_core.storage import load_tables

    root, sources = corpus
    ingest_entity(api, root, sources, "private.md", "confidential")
    ingest_entity(api, root, sources, "public.md", "public")
    tables = load_tables(root)
    private = next(e for e in tables["entities"].values() if e["access"] == "confidential")
    public = next(e for e in tables["entities"].values() if e["access"] == "public")
    claim = public["claim_ids"][0]
    relationships(
        tables,
        [
            {
                "subject": private["id"],
                "object": public["id"],
                "predicate": "related_to",
                "claim_ids": [claim],
                "rationale": "Synthetic identity comparison.",
            }
        ],
        "op_test",
        {private["id"], public["id"], claim},
    )
    relation = next(iter(tables["relationships"].values()))
    assert relation["access"] == "confidential"
    relation["access"] = "public"
    assert any(e["code"] == "RCW_ACCESS_LEAK" for e in audit_tables(root, tables)["errors"])


def test_analyzed_unverified_claim_does_not_starve_next_delta_batch(api, corpus):
    root, sources = corpus
    path = source(sources, source_type="synthesis_report")
    packet = api.ingest_prepare(root, path.name)
    api.ingest_apply(root, packet["operation_id"], proposal(packet))
    packet = api.analyze_prepare(root, limit=1)
    cid = packet["claims"][0]["id"]
    api.analyze_apply(
        root,
        packet["operation_id"],
        {
            "operation_id": packet["operation_id"],
            "pages": [
                {
                    "key": "reading",
                    "title": "Reading evidence",
                    "page_type": "finding",
                    "assertions": [
                        {
                            "text": "The report's claimed reading gain awaits original-source verification.",
                            "claim_ids": [cid],
                        }
                    ],
                }
            ],
            "relationships": [],
            "gaps": [],
        },
    )
    assert api.analyze_prepare(root, limit=1)["claims"] == []
