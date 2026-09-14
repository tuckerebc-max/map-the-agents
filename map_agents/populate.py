"""One resumable group of <=8 repositories through prepare -> model -> source-review -> apply.

Requires the same trusted worker/wiki contract as `workers.run_worker`; only public frozen
evidence reaches the trusted adapter. Completed proposals are persisted before apply; uncertain
provider or reviewer calls are never retried automatically. This is a bounded campaign driver,
not an automatic scheduler: it does not enable partitioning on an already-initialized shared
corpus, and it holds (never silently re-runs) a job left in a completed-failure stage -- use
`map_agents.proposal_recovery --repair` or `--retain` explicitly for those.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from . import core, wiki, workers
from .source_review import review_proposal


def save(path: Path, value: object) -> None:
    core.atomic_write_bytes(path, core.dump_json(value))


def safe_failure(exc: Exception) -> dict:
    return {'type': type(exc).__name__, 'error': str(exc)[:500] if isinstance(exc, core.WorkbenchError) else 'detail withheld'}


def launch_before(deadline: float, argv: list[str], payload: bytes, timeout: float, max_stdout: int, max_stderr: int) -> dict:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise workers.WorkerFailed('group deadline reached before model launch')
    return workers.run_process(argv, payload, min(timeout, remaining), max_stdout, max_stderr)


def batch(root: Path, keys: list[str], receipts: Path, concurrency: int = 4, seconds: float = 1200,
          quarantine_invalid_claims: bool = False) -> dict:
    if not 1 <= len(keys) <= 8 or len(set(keys)) != len(keys):
        raise ValueError('a group requires 1..8 unique repositories')
    if not 1 <= concurrency <= 4 or not 1 <= seconds <= 1800:
        raise ValueError('finite group limits required')
    if wiki.load_layout(root)['layout'] != 'partitioned':
        raise ValueError('independent authoring requires partitioned kernels')
    receipts.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    results, ready = [], []
    limits = workers.Limits(max_seconds=seconds, worker_seconds=270, build=False)
    with workers.Lease(root, 'population-batch'):
        repos = core.load_repos(root)
        for key in keys:
            if key not in repos:
                raise ValueError('group contains an unknown repository')
            slug = key.replace('/', '--')
            receipt = receipts / (slug + '.json')
            old = json.loads(receipt.read_bytes()) if receipt.exists() else None
            rec = repos[key]
            if rec.get('status') == 'distilled' and rec.get('indexed_snapshot_id') == rec.get('latest_snapshot_id'):
                dossier = wiki.load_dossier(root, key)
                results.append({'repo': key, 'outcome': 'existing', 'claims': len(dossier['claims'])})
                continue
            if not rec.get('latest_snapshot'):
                result = {'repo': key, 'outcome': 'unavailable' if rec.get('last_error') else 'not-started',
                          'collection_error': rec.get('last_error')}
                if rec.get('last_error'):
                    save(receipt, result)
                results.append(result)
                continue
            if old:
                if old.get('stage') in {'proposal-ready', 'proposal-reviewed', 'applying'}:
                    op = old.get('operation_id')
                    if (not isinstance(op, str) or not re.fullmatch(r'op_[a-f0-9]+', op)
                            or old.get('repo') != key or old.get('packet') != f'packets/{op}.json'
                            or old.get('proposal') != f'proposals/{op}.json'):
                        raise ValueError('saved operation has invalid identity or paths')
                    packet_path = root / old['packet']
                    proposal_path = root / old['proposal']
                    packet = wiki.load_packet(root, packet_path)
                    if packet['repo'] != key:
                        raise ValueError('saved operation belongs to another repository')
                    ready.append((key, receipt, old, packet))
                    continue
                raise RuntimeError(f'{key}: saved {old.get("stage", old.get("outcome"))} requires reconciliation; no automatic retry')
            if time.monotonic() - start >= seconds:
                results.append({'repo': key, 'outcome': 'not-started', 'reason': 'group deadline'})
                continue
            try:
                prepared = wiki.prepare(root, key)
                packet = wiki.load_packet(root, root / prepared['packet'])
                envelope = core.dump_json(workers.envelope(root, packet))
                if len(envelope) > limits.max_envelope_bytes:
                    raise workers.WorkerFailed('envelope exceeds worker byte ceiling')
                envelope_rel = f"packets/{packet['operation_id']}.envelope.json"
                core.atomic_write_bytes(root / envelope_rel, envelope)
                job = {'repo': key, 'stage': 'prepared', 'packet': prepared['packet'], 'envelope': envelope_rel,
                       'operation_id': packet['operation_id'], 'snapshot_id': packet['snapshot_id']}
                save(receipt, job)
                ready.append((key, receipt, job, packet))
            except (core.WorkbenchError, OSError) as exc:
                result = {'repo': key, 'outcome': 'failed', 'stage': 'prepare', **safe_failure(exc)}
                save(receipt, result)
                results.append(result)

        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            futures = {}
            for key, receipt, job, packet in ready:
                if job['stage'] in {'proposal-ready', 'proposal-reviewed', 'applying'}:
                    continue
                remaining = seconds - (time.monotonic() - start)
                if remaining <= 0:
                    results.append({'repo': key, 'outcome': 'not-started', 'reason': 'group deadline'})
                    continue
                argv = [sys.executable, '-m', 'map_agents.lunaroute', '--timeout-seconds', '120',
                        '--max-output-tokens', '5000', '--usage-file', str(receipts / (key.replace('/', '--') + '.usage.json'))]
                if quarantine_invalid_claims:
                    argv.append('--quarantine-invalid-claims')
                job['stage'] = 'model-running'
                save(receipt, job)
                f = pool.submit(launch_before, start + seconds, argv, (root / job['envelope']).read_bytes(),
                                min(270, remaining), limits.max_proposal_bytes, limits.max_stderr_bytes)
                futures[f] = (key, receipt, job, packet)
            for future in as_completed(futures):
                key, receipt, job, packet = futures[future]
                try:
                    proc = future.result()
                    job['model'] = {k: proc[k] for k in ('returncode', 'timed_out', 'seconds', 'stdout_over', 'stderr_over', 'drain_complete')}
                    if proc['returncode'] != 0 or proc['timed_out'] or proc['stdout_over'] or not proc['drain_complete']:
                        raise workers.WorkerFailed('model process did not return a complete bounded proposal; inspect sanitized usage receipt')
                    proposal = json.loads(proc['stdout'].decode('utf-8'))
                    wiki.validate_proposal(proposal, packet)
                    proposal_rel = f"proposals/{packet['operation_id']}.json"
                    save(root / proposal_rel, proposal)
                    job.update({'stage': 'proposal-ready', 'proposal': proposal_rel})
                    save(receipt, job)
                except Exception as exc:
                    job.update({'stage': 'model-failed', 'outcome': 'failed', **safe_failure(exc)})
                    save(receipt, job)
                    results.append(dict(job))

        # A separate fresh reviewer sees the actual cited text before any claim is
        # committed. Failed or uncertain assessments remain proposals only.
        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            reviews = {}
            for key, receipt, job, packet in ready:
                if job['stage'] != 'proposal-ready':
                    continue
                if time.monotonic() - start >= seconds:
                    results.append({'repo': key, 'outcome': 'deferred', 'stage': job['stage']})
                    continue
                proposal = json.loads((root / job['proposal']).read_bytes())
                job['stage'] = 'review-running'
                save(receipt, job)
                review_path = receipts / (key.replace('/', '--') + '.review.json')
                reviews[pool.submit(review_proposal, packet, proposal, review_path)] = (key, receipt, job)
            for future in as_completed(reviews):
                key, receipt, job = reviews[future]
                try:
                    review = future.result()
                    job['source_review'] = {'status': review['status'], 'verdict': review.get('verdict', 'unavailable'),
                                            'input_sha256': review['input_sha256'], 'proposal_sha256': review['dossier_seal']}
                    if review['status'] != 'reviewed' or review.get('verdict') != 'pass':
                        raise workers.WorkerFailed('source review did not pass; proposal retained without canonical apply')
                    job['stage'] = 'proposal-reviewed'
                    save(receipt, job)
                except Exception as exc:
                    job.update({'stage': 'review-failed', 'outcome': 'failed', **safe_failure(exc)})
                    save(receipt, job)
                    results.append(dict(job))

        # Only this controller mutates the canonical kernel and catalog. Each proposal
        # remains bound to one partition, source snapshot and exact operation/base.
        for key, receipt, job, packet in ready:
            if job['stage'] not in {'proposal-reviewed', 'applying'}:
                continue
            if time.monotonic() - start >= seconds:
                results.append({'repo': key, 'outcome': 'deferred', 'stage': job['stage']})
                continue
            try:
                proposal = json.loads((root / job['proposal']).read_bytes())
                import hashlib
                current_sha = hashlib.sha256(core.dump_json(proposal)).hexdigest()
                if job.get('source_review', {}).get('verdict') != 'pass' or job['source_review'].get('proposal_sha256') != current_sha:
                    raise workers.WorkerFailed('saved source review is absent or bound to another proposal')
                job['stage'] = 'applying'
                save(receipt, job)
                applied = wiki.apply(root, root / job['packet'], root / job['proposal'])
                dossier = wiki.load_dossier(root, key)
                job.update({'stage': 'applied', 'outcome': 'applied', 'claims': len(dossier['claims']), 'apply': applied})
                save(receipt, job)
                results.append({'repo': key, 'outcome': 'applied', 'claims': len(dossier['claims'])})
            except Exception as exc:
                # Keep 'applying' + the exact proposal so recovery can reconcile a kernel
                # commit that may have completed before an auxiliary write failed.
                job.update({'outcome': 'apply-failed', **safe_failure(exc)})
                save(receipt, job)
                results.append({'repo': key, 'outcome': 'apply-failed', **safe_failure(exc)})
    return {'results': results, 'elapsed_seconds': round(time.monotonic() - start, 3),
            'concurrency': concurrency, 'group_seconds': seconds,
            'ok': all(r['outcome'] in {'applied', 'existing', 'unavailable'} for r in results) and len(results) == len(keys)}


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog='python -m map_agents.populate',
                                description='Bounded population run for <=8 repositories: prepare, model, source-review, apply.')
    p.add_argument('--root', type=Path, required=True)
    p.add_argument('--group', type=Path, required=True, help='JSON file: a list of 1..8 repository keys, never executable configuration')
    p.add_argument('--receipts', type=Path, required=True)
    p.add_argument('--concurrency', type=int, default=4)
    p.add_argument('--quarantine-invalid-claims', action='store_true', default=False,
                    help='opt-in, default off: forward the trusted --quarantine-invalid-claims flag to the '
                         'lunaroute adapter subprocess for every model call this batch launches')
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    keys = json.loads(args.group.read_bytes())
    if not isinstance(keys, list) or not all(isinstance(k, str) for k in keys):
        raise SystemExit('--group must be a JSON list of repository key strings')
    result = batch(args.root, keys, args.receipts, args.concurrency,
                    quarantine_invalid_claims=args.quarantine_invalid_claims)
    save(args.receipts / 'batch.json', result)
    print(json.dumps(result), flush=True)
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
