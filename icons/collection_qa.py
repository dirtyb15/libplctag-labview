#!/usr/bin/env python3
"""Inventory and validate the LabVIEW icon collection; never approve artwork.

Run with the Pillow-enabled Python: collection_qa.py sync|validate [--root PATH].
sync only adds inventory entries and reconciles existing owned runs; it never
silently updates a changed source hash or accepts an image.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SKILL_SCRIPTS = Path.home() / '.codex/skills/labview-icon-creator/scripts'
sys.path.insert(0, str(SKILL_SCRIPTS))
from validate_icon_assets import validate_package, has_failures  # noqa: E402

QA_FIELDS = ('source', '29x29', '30x23', '30x18', '16x16')
COMPLETE = {'set_validated', 'collection_validated'}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def inventory(root):
    excluded = {'icons', 'icon sets', '.git', '.codex', '.agents'}
    result = {}
    for parent, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d.casefold() not in excluded]
        for name in files:
            path = Path(parent) / name
            if path.suffix.casefold() in ('.vi', '.ctl'):
                result[path.relative_to(root).as_posix()] = digest(path)
    return dict(sorted(result.items(), key=lambda pair: pair[0].casefold()))


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.ledger-', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(value, f, indent=2, ensure_ascii=False)
            f.write('\n')
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def safe_child(base, name):
    path = (base / name).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError(f'path escapes output folder: {name}')
    return path


def sync(root, runs_root=None):
    out = root / 'icons'
    ledger_path = out / 'collection-ledger.json'
    ledger = read_json(ledger_path) if ledger_path.exists() else {'schema_version': 1, 'sources': {}, 'collection_review': None}
    found = inventory(root)
    for rel, sha in found.items():
        # Mirror the source parent for nested files; the complete filename is retained.
        folder = Path(rel).as_posix()
        entry = ledger['sources'].setdefault(rel, {'source_sha256': sha, 'output_dir': folder,
            'state': 'not_started', 'runs': [], 'accepted': [], 'manifest': None, 'source_evidence': None})
        if sha != entry['source_sha256']:
            entry['source_changed'] = True
            entry['source_evidence_status'] = 'stale'
        if (out / folder / 'drafts').is_dir() and entry['state'] == 'not_started':
            entry['state'] = 'review_required'
    if runs_root and runs_root.exists():
        for path in runs_root.glob('labview-icons-*/run.json'):
            try:
                run = read_json(path)
                target = Path(run['output_dir']).resolve()
                for rel, entry in ledger['sources'].items():
                    if target == (out / entry['output_dir']).resolve():
                        rec = {'run_file': str(path), 'run_id': run['run_id'],
                               'published': bool(run.get('published')),
                               'candidates': [{'id': c['candidate_id'], 'concept_id': c['concept_id'],
                                   'concept_summary': c.get('concept_summary'), 'signature': c.get('signature'),
                                   'attempt_number': c.get('attempt_number'),
                                   'source_file': c['source_file'], 'exists': Path(c['source_file']).is_file(),
                                   'source_sha256': digest(Path(c['source_file'])) if Path(c['source_file']).is_file() else None,
                                   'reviewed_sha256': c.get('reviewed_sha256'),
                                   'qa': c.get('qa', {})} for c in run['candidates']]}
                        preflight = path.parent / 'preflight.json'
                        if preflight.is_file():
                            rec['preflight_file'] = str(preflight)
                            rec['preflight'] = read_json(preflight)
                        previous = next((r for r in entry['runs'] if r.get('run_id') == rec['run_id']), {})
                        # Preserve workflow annotations but refresh all observed run data.
                        rec = {**{k: previous[k] for k in ('superseded_by', 'notes') if k in previous}, **rec}
                        entry['runs'] = [r for r in entry['runs'] if r.get('run_id') != rec['run_id']] + [rec]
                        if entry['state'] == 'not_started':
                            entry['state'] = 'review_required' if any(c['exists'] for c in rec['candidates']) else 'planned'
            except (OSError, ValueError, KeyError, TypeError):
                continue
    atomic_json(ledger_path, ledger)
    return ledger


def collection_fingerprint(sources):
    data = []
    for rel, entry in sorted(sources.items()):
        accepted = [{'candidate_id': a.get('candidate_id', ''), 'concept_id': a.get('concept_id', ''),
                     'run_id': a.get('run_id', ''), 'master_sha256': a.get('master_sha256', ''),
                     'reviewed_source_sha256': a.get('reviewed_source_sha256', ''),
                     'signature': a.get('signature')} for a in entry.get('accepted', [])]
        used_runs = {a['run_id'] for a in accepted}
        preflights = sorted(({'run_id': r.get('run_id'), 'preflight': r.get('preflight'),
                              'superseded_by': r.get('superseded_by')}
                             for r in entry.get('runs', []) if r.get('run_id') in used_runs),
                            key=lambda r: r['run_id'] or '')
        data.append({'source': rel, 'source_sha256': entry['source_sha256'],
                     'source_evidence': entry.get('source_evidence'),
                     'source_evidence_status': entry.get('source_evidence_status'),
                     'manifest_sha256': entry.get('manifest_sha256', ''),
                     'accepted': sorted(accepted, key=lambda a: a['candidate_id']), 'preflights': preflights})
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def collection_members(sources):
    """Stable identities and master hashes that the collection review must cover."""
    return sorted((rel, a.get('candidate_id', ''), a.get('master_sha256', ''))
                  for rel, entry in sources.items() for a in entry.get('accepted', []))


def provisional_conflicts(root, sources):
    """Report recorded failed comparisons that still involve accepted artwork.

    Matching the reviewed hashes, rather than just candidate labels, allows a
    replacement to be assessed afresh and prevents renaming unchanged artwork
    from hiding a conflict. These records do not grant visual acceptance.
    """
    errors = []
    refs = {ref for entry in sources.values() for ref in entry.get('provisional_comparisons', [])}
    for ref in sorted(refs):
        try:
            path = safe_child(root, ref)
            if not path.is_relative_to((root / 'icons').resolve()):
                raise ValueError('comparison record is outside icons')
            review = read_json(path)
            members = {f"{m['source']}/{m['candidate_id']}": m for m in review['members']}
            for observation in review['observations']:
                if observation.get('result') != 'FAIL':
                    continue
                ids = observation['candidates']
                if not ids or any(identifier not in members for identifier in ids):
                    raise ValueError('failed comparison has missing members')
                def retained(identifier):
                    member = members[identifier]
                    accepted = sources.get(member['source'], {}).get('accepted', [])
                    return any(a.get('reviewed_source_sha256') == member['reviewed_source_sha256']
                               for a in accepted)
                if all(retained(identifier) for identifier in ids):
                    errors.append('unresolved visual conflict: ' + ' vs '.join(ids))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f'invalid provisional comparison {ref}: {exc}')
    return errors


def validate(root, ledger):
    errors = []
    found = inventory(root)
    sources = ledger.get('sources', {})
    for rel in sorted(found.keys() - sources.keys()): errors.append(f'{rel}: missing ledger entry')
    for rel in sorted(sources.keys() - found.keys()): errors.append(f'{rel}: source removed or renamed')
    mapped = {}
    reviewed_hashes = {}
    master_hashes = {}
    out = root / 'icons'
    for rel, entry in sources.items():
        def fail(msg): errors.append(f'{rel}: {msg}')
        if found.get(rel) != entry.get('source_sha256'): fail('source hash changed or source missing')
        try:
            folder = safe_child(out, entry['output_dir'])
            key = str(folder).casefold()
            if key in mapped: fail(f'output folder duplicates {mapped[key]}')
            mapped[key] = rel
        except (ValueError, KeyError, TypeError) as exc:
            fail(f'invalid output folder: {exc}'); continue
        if entry.get('state') not in COMPLETE: fail(f"unfinished state: {entry.get('state')}")
        if not str(entry.get('source_evidence') or '').strip(): fail('source behavior evidence missing')
        if entry.get('source_evidence_status') != 'verified': fail('source behavior evidence is not fully verified')
        accepted = entry.get('accepted', [])
        if len(accepted) != 5 or len({a.get('candidate_id') for a in accepted}) != 5:
            fail('requires five uniquely identified accepted options')
        for a in accepted:
            signature = a.get('signature') or {}
            if not all(str(signature.get(k) or '').strip() for k in ('metaphor', 'objects', 'cue', 'composition', 'orientation')):
                fail(f"{a.get('candidate_id', '?')}: visual signature incomplete")
            cid = a.get('candidate_id', '?')
            for label, value, seen in (('reviewed source', a.get('reviewed_source_sha256'), reviewed_hashes),
                                       ('packaged master', a.get('master_sha256'), master_hashes)):
                if not isinstance(value, str) or len(value) != 64:
                    fail(f'{cid}: {label} hash missing or invalid')
                elif value in seen:
                    fail(f'{cid}: identical {label} already used by {seen[value]}')
                else:
                    seen[value] = f'{rel}/{cid}'
            matching_runs = [r for r in entry.get('runs', []) if r.get('run_id') == a.get('run_id')]
            if len(matching_runs) != 1:
                fail(f'{cid}: missing or ambiguous source run')
                continue
            run = matching_runs[0]
            candidates = [c for c in run.get('candidates', []) if c.get('id') == cid]
            preflight = run.get('preflight') or {}
            if (run.get('superseded_by') or not run.get('published') or preflight.get('result') != 'PASS'
                    or not str(preflight.get('evidence', '')).strip()
                    or a.get('concept_id') not in preflight.get('candidate_ids', [])):
                fail(f'{cid}: missing, failed, or superseded concept preflight')
            if (len(candidates) != 1 or candidates[0].get('concept_id') != a.get('concept_id')
                    or candidates[0].get('signature') != signature
                    or candidates[0].get('source_sha256') != a.get('reviewed_source_sha256')
                    or candidates[0].get('reviewed_sha256') != a.get('reviewed_source_sha256')):
                fail(f'{cid}: source run, signature, or reviewed hash mismatch')
        manifest_name = entry.get('manifest')
        if not manifest_name:
            fail('manifest missing'); continue
        try:
            manifest_path = safe_child(folder, manifest_name)
            if entry.get('manifest_sha256') != digest(manifest_path):
                fail('manifest hash missing or changed')
            manifest = read_json(manifest_path)
            options = manifest['options']
            if any(a.get('run_id') != manifest.get('run_id') for a in accepted):
                fail('accepted source run does not match manifest run')
            if len(options) != 5 or {o['option_number'] for o in options} != set(range(1, 6)):
                fail('manifest must contain options 1 through 5')
            by_id = {a['candidate_id']: a for a in accepted}
            option_ids = [o.get('candidate_id') for o in options]
            if len(option_ids) != len(set(option_ids)) or set(option_ids) != set(by_id):
                fail('manifest candidates do not match the five accepted candidates')
            for opt in options:
                files = [opt['source_file'], opt['ico_file']] + [d['file'] for d in opt['derived_png_files']]
                for name in files:
                    file = safe_child(folder, name)
                    if not file.is_file() or opt.get('sha256', {}).get(name) != digest(file):
                        fail(f'missing asset or hash mismatch: {name}')
                cid = opt['candidate_id']
                qa = opt['visual_qa']
                master_hash = opt.get('sha256', {}).get(opt['source_file'])
                accepted_item = by_id.get(cid, {})
                if opt.get('concept_id') != accepted_item.get('concept_id'):
                    fail(f'{cid}: manifest concept does not match accepted concept')
                source_runs = [r for r in entry.get('runs', []) if r.get('run_id') == accepted_item.get('run_id')]
                source_candidates = [c for r in source_runs for c in r.get('candidates', []) if c.get('id') == cid]
                if len(source_candidates) != 1 or source_candidates[0].get('qa') != qa.get('checks'):
                    fail(f'{cid}: run review does not match manifest review')
                reviewed = accepted_item.get('reviewed_source_sha256')
                reviewed_path = Path(accepted_item.get('reviewed_source_file', ''))
                if (accepted_item.get('master_sha256') != master_hash or not reviewed
                        or qa.get('source_sha256') != reviewed or not reviewed_path.is_file()
                        or digest(reviewed_path) != reviewed):
                    fail(f'{cid}: reviewed source or packaged master hash mismatch')
                for field in QA_FIELDS:
                    check = qa.get('checks', {}).get(field, {})
                    if check.get('result') not in ('PASS', 'WARN') or not str(check.get('evidence', '')).strip():
                        fail(f'{cid}: missing or failed {field} review')
                distinct = qa.get('distinctness', {})
                if distinct.get('result') != 'PASS' or not str(distinct.get('evidence', '')).strip() or set(distinct.get('candidate_ids', [])) != {o['candidate_id'] for o in options}:
                    fail(f'{cid}: within-set review missing or stale')
            checks = validate_package(options, folder)
            if has_failures(checks):
                fail('skill package checks failed: ' + ', '.join(sorted({c['rule_id'] for c in checks if c['result'] == 'FAIL'})))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            fail(f'manifest or package invalid: {exc}')
    errors.extend(provisional_conflicts(root, sources))
    review = ledger.get('collection_review') or {}
    if review.get('result') != 'PASS' or not str(review.get('evidence', '')).strip() or review.get('fingerprint') != collection_fingerprint(sources):
        errors.append('collection-wide visual review missing, failed, or stale')
    try:
        covered = sorted(tuple(member) for member in review.get('members', []))
        if covered != collection_members(sources):
            errors.append('collection-wide visual review does not cover exactly the accepted candidates')
    except (TypeError, ValueError):
        errors.append('collection-wide visual review coverage is invalid')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('sync', 'validate'))
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--runs-root', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == 'sync':
        ledger = sync(root, args.runs_root)
        print(f"Inventoried {len(ledger['sources'])} sources; ledger updated without accepting drafts.")
        return 0
    try:
        ledger = read_json(root / 'icons/collection-ledger.json')
        errors = validate(root, ledger)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'FAIL: cannot validate ledger: {exc}')
        return 1
    print(f"{'FAIL' if errors else 'PASS'}: {len(ledger['sources'])} ledger entries, {len(errors)} issues. Visual review records are evidence, not automated judgments.")
    for error in errors[:30]: print(' - ' + error)
    if len(errors) > 30: print(f' - ... {len(errors) - 30} further issues')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
