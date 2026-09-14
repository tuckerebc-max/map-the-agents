"""Explicit recovery for jobs left in a completed-failure stage by `map_agents.populate`.

Two operations, each a bounded, one-round action on already-completed (never uncertain)
failures: `--repair` asks for one corrected proposal and a fresh source review; `--retain`
quarantines rejected clauses from an already-completed, exactly-bound source assessment,
rebuilds the summary from what remains, and requires a NEW source review before apply. Neither
operation retries an uncertain provider or reviewer call, and neither is a way to relabel a
rejected claim as supported. `map_agents.populate` never calls these automatically.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from . import core, lunaroute, wiki, workers
from .source_review import review_proposal


def _save(path: Path, body: object) -> None:
    core.atomic_write_bytes(path, core.dump_json(body))


def correct(root: Path, key: str, directory: Path) -> dict:
    """One-round correction of a completed model or review failure. Never retries an uncertain outcome."""
    slug = key.replace('/', '--')
    path = directory / (slug + '.json')
    job = json.loads(path.read_bytes())
    if job.get('stage') not in ('review-failed', 'model-failed'):
        raise ValueError('only explicitly completed failed proposals may be corrected')
    if job.get('correction_round'):
        raise ValueError('one-round correction ceiling reached')
    model = job.get('model', {})
    if model.get('timed_out') or not model.get('drain_complete'):
        raise ValueError('uncertain model outcome requires separate reconciliation')
    usage = json.loads((directory / (slug + '.usage.json')).read_bytes())
    if not usage.get('calls') or any(c.get('finish_reason') != 'stop' for c in usage['calls']):
        raise ValueError('provider did not confirm complete responses; no retry')
    packet = wiki.load_packet(root, root / job['packet'])
    selected, _ = lunaroute._select_slices(packet['slices'], lunaroute.MAX_PROMPT_CHARS)
    if job['stage'] == 'review-failed':
        review = json.loads((directory / (slug + '.review.json')).read_bytes())
        if review.get('status') != 'reviewed':
            raise ValueError('uncertain reviewer outcome requires reconciliation')
        prior = json.loads((root / job['proposal']).read_bytes())
        if review['dossier_seal'] != hashlib.sha256(core.dump_json(prior)).hexdigest():
            raise ValueError('review proposal binding mismatch')
        problems = [json.dumps({'prior_claims': prior['claims'], 'source_review': review['claims']})]
    else:
        problems = [usage.get('error', 'Completed response unusable')]
    saved_before = {**job, 'correction_round': 0}
    _save(directory / (slug + '.first.json'), saved_before)
    if job.get('proposal'):
        _save(directory / (slug + '.first-proposal.json'), json.loads((root / job['proposal']).read_bytes()))
    job.update(stage='correction-running', correction_round=1)
    _save(path, job)
    calls: list = []
    try:
        user = lunaroute._build_user_content(packet, selected, None, problems=problems)
        system = lunaroute.SYSTEM_PROMPT + ''' Correct the completed earlier extraction using the review feedback. Keep only warranted clauses and cite each clause's own evidence. Use conservative atomic claims. Omit contributor-instruction-only observations entirely for this correction; focus on product architecture, runtime code and product docs. Dropping an unsupported assertion is allowed; never invent facts to retain its facet. Do not borrow a version/platform/command from memory or another uncited slice. Return the normal reduced JSON schema.'''
        reduced, claims = lunaroute._one_pass('glm-5.3-flash', [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
                                              120, 5000, selected, calls, 'source-correction')
        proposal = {k: packet[k] for k in ('operation_id', 'repo', 'commit', 'snapshot_id', 'base_digest')}
        proposal.update(schema_version=wiki.DOSSIER_SCHEMA, summary=lunaroute._final_summary(reduced['summary'], len(selected), len(packet['slices'])), claims=claims)
        wiki.validate_proposal(proposal, packet)
        job['proposal'] = f"proposals/{packet['operation_id']}.json"
        _save(root / job['proposal'], proposal)
        job['stage'] = 'correction-review-running'
        _save(path, job)
        result = review_proposal(packet, proposal, directory / (slug + '.correction-review.json'))
        if result['status'] != 'reviewed' or result.get('verdict') != 'pass':
            raise ValueError('corrected source assessment did not pass')
        job.update(stage='proposal-reviewed',
                  source_review={'status': result['status'], 'verdict': result['verdict'], 'input_sha256': result['input_sha256'], 'proposal_sha256': result['dossier_seal']})
        for field in ('outcome', 'error', 'type'):
            job.pop(field, None)
    except Exception as exc:
        job.update(stage='correction-failed', outcome='failed', error_type=type(exc).__name__)
    _save(directory / (slug + '.correction-usage.json'), {'calls': calls, 'round': 1})
    _save(path, job)
    return {'repo': key, 'stage': job['stage']}


def retain(proposal: dict, assessment: dict) -> tuple[dict, dict]:
    """Quarantine rejected clauses from an exact, completed source assessment; rebuild the summary."""
    digest = hashlib.sha256(core.dump_json(proposal)).hexdigest()
    if (assessment.get('status') != 'reviewed' or assessment.get('finish_reason') != 'stop'
            or assessment.get('dossier_seal') != digest):
        raise ValueError('retention needs a completed assessment bound to this exact proposal')
    expected = {f'proposal-{i+1}' for i in range(len(proposal['claims']))} | {'summary'}
    rows = assessment.get('claims', [])
    ids = [r.get('claim_id') for r in rows]
    if len(ids) != len(set(ids)) or set(ids) != expected:
        raise ValueError('assessment must cover each claim and summary exactly once')
    byid = {r['claim_id']: r for r in rows}
    kept, rejected = [], []
    for i, claim in enumerate(proposal['claims']):
        verdict = byid[f'proposal-{i+1}']
        if verdict['verdict'] == 'supported':
            kept.append(claim)
        elif verdict['verdict'] in ('revise', 'unsupported'):
            rejected.append({'original_index': i + 1, 'claim': claim, 'reason': verdict['reason']})
        else:
            raise ValueError('invalid source assessment')
    if not kept:
        raise ValueError('no supported feature observations to retain')
    # Never carry the old free-form summary across removal of its underlying claims.
    summary = 'Selected evidence records: '
    for claim in kept[:2]:
        if len(summary) + len(claim['text']) + 1 <= 780:
            summary += claim['text'] + ' '
    candidate = {**proposal, 'claims': kept, 'summary': summary.strip()}
    return candidate, {'prior_proposal_sha256': digest, 'retained_claims': len(kept), 'rejected_claims': rejected,
                       'prior_summary': proposal['summary'], 'summary_rebuilt_from_retained_claims': True}


def prepare_retained(root: Path, key: str, directory: Path) -> dict:
    """Recovery step after a completed correction failure -- not a way to label a rejected claim supported."""
    slug = key.replace('/', '--')
    jobpath = directory / (slug + '.json')
    job = json.loads(jobpath.read_bytes())
    if job.get('stage') != 'correction-failed':
        raise ValueError('retention is only for reconciled completed correction failures')
    target = directory / (slug + '.retention.json')
    if target.exists():
        raise ValueError('retention already attempted; reconcile its existing receipt')
    choices = [(root / job.get('proposal', 'missing'), directory / (slug + '.correction-review.json')),
               (directory / (slug + '.first-proposal.json'), directory / (slug + '.review.json'))]
    packet = wiki.load_packet(root, root / job['packet'])
    candidate = None
    receipt = None
    for source, reviewpath in choices:
        if not source.is_file() or not reviewpath.is_file():
            continue
        proposal = json.loads(source.read_bytes())
        assessment = json.loads(reviewpath.read_bytes())
        if assessment.get('status') != 'reviewed' or assessment.get('finish_reason') != 'stop':
            continue
        if assessment.get('dossier_seal') != hashlib.sha256(core.dump_json(proposal)).hexdigest():
            continue
        wiki.validate_proposal(proposal, packet)
        candidate, receipt = retain(proposal, assessment)
        break
    if candidate is None:
        raise ValueError('no completed, bound source assessment is available; model/provider failures stay held')
    wiki.validate_proposal(candidate, packet)
    lunaroute._check_contributor_gate(candidate['claims'], packet['slices'])
    lunaroute._check_quote_limit(candidate['claims'], packet['slices'])
    proposal_path = directory / (slug + '.retained-proposal.json')
    core.atomic_write_bytes(proposal_path, core.dump_json(candidate))
    receipt.update(repo=key, status='review-running', operation_id=packet['operation_id'])
    core.atomic_write_bytes(target, core.dump_json(receipt))
    review = review_proposal(packet, candidate, directory / (slug + '.retention-review.json'))
    if review.get('status') != 'reviewed' or review.get('verdict') != 'pass':
        receipt.update(status='held', review_verdict=review.get('verdict'))
        core.atomic_write_bytes(target, core.dump_json(receipt))
        return {'repo': key, 'stage': 'held'}
    old = root / job['proposal']
    core.atomic_write_bytes(directory / (slug + '.before-retention-proposal.json'), old.read_bytes())
    core.atomic_write_bytes(old, core.dump_json(candidate))
    job.update(stage='proposal-reviewed',
              source_review={'status': 'reviewed', 'verdict': 'pass', 'input_sha256': review['input_sha256'], 'proposal_sha256': review['dossier_seal']},
              retention_receipt=target.name)
    for field in ('outcome', 'error', 'type'):
        job.pop(field, None)
    core.atomic_write_bytes(jobpath, core.dump_json(job))
    receipt['status'] = 'reviewed'
    core.atomic_write_bytes(target, core.dump_json(receipt))
    return {'repo': key, 'stage': 'proposal-reviewed', 'claims': len(candidate['claims'])}


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog='python -m map_agents.proposal_recovery',
                                description='Explicit --repair or --retain recovery for completed failed population jobs.')
    p.add_argument('--root', type=Path, required=True)
    p.add_argument('--group', type=Path, required=True, help='JSON file: a list of 1..8 repository keys')
    p.add_argument('--receipts', type=Path, required=True)
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--repair', action='store_true', help='one-round correction of a completed model/review failure')
    mode.add_argument('--retain', action='store_true', help='quarantine rejected clauses from a completed correction failure')
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    keys = json.loads(args.group.read_bytes())
    if not isinstance(keys, list) or not 1 <= len(keys) <= 8 or len(set(keys)) != len(keys):
        raise SystemExit('--group must contain 1..8 unique repository keys')
    op = correct if args.repair else prepare_retained
    lease_kind = 'completed-source-correction' if args.repair else 'supported-observation-retention'
    out = []
    with workers.Lease(args.root, lease_kind):
        with ThreadPoolExecutor(max_workers=4) as pool:
            jobs = {pool.submit(op, args.root, k, args.receipts): k for k in keys}
            for f in as_completed(jobs):
                try:
                    out.append(f.result())
                except Exception as exc:
                    out.append({'repo': jobs[f], 'stage': 'refused', 'error_type': type(exc).__name__})
    print(json.dumps(out), flush=True)
    return 0 if all(r.get('stage') not in ('refused', 'held', 'correction-failed') for r in out) else 1


if __name__ == '__main__':
    raise SystemExit(main())
