"""Integration checks for collection gates using synthetic, disposable artwork."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image, ImageDraw
import collection_qa as qa
from process_icons import process_icon
from manifest import write_manifest


class CollectionChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Keep temporary fixtures inside the writable workspace on Windows.
        cls.temp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        cls.root = Path(cls.temp.name)
        (cls.root / 'Test.vi').write_bytes(b'synthetic source')
        cls.folder = cls.root / 'icons' / 'Test.vi'
        cls.folder.mkdir(parents=True)
        cls.options, accepted, run_candidates = [], [], []
        ids = [f'candidate-{i:02}' for i in range(1, 6)]
        for i, cid in enumerate(ids, 1):
            source = cls.root / f'reviewed-{i}.png'
            img = Image.new('RGB', (128, 128), 'white')
            ImageDraw.Draw(img).rectangle((25, 25, 95, 95), fill=(i * 30, 0, 100))
            img.save(source)
            meta = process_icon(source, 'Fixture', i, salt=f'{i:010d}', output_dir=cls.folder, staging_root=cls.root)
            review_hash = qa.digest(source)
            meta.update(candidate_id=cid, concept_id=f'concept-{i}', visual_qa={
                'source_sha256': review_hash,
                'checks': {field: {'result': 'PASS', 'evidence': f'Synthetic fixture {cid} {field}'} for field in qa.QA_FIELDS},
                'distinctness': {'result': 'PASS', 'candidate_ids': ids, 'evidence': 'Synthetic fixture only.'}})
            cls.options.append(meta)
            signature = {key: f'fixture {cid} {key}' for key in ('metaphor','objects','cue','composition','orientation')}
            accepted.append({'candidate_id': cid, 'concept_id': f'concept-{i}', 'run_id': 'fixture', 'reviewed_source_file': str(source),
                'reviewed_source_sha256': review_hash, 'master_sha256': qa.digest(cls.folder / meta['source_file']),
                'signature': signature})
            run_candidates.append({'id': cid, 'concept_id': f'concept-{i}', 'signature': signature,
                'source_sha256': review_hash, 'reviewed_sha256': review_hash, 'qa': meta['visual_qa']['checks']})
        write_manifest(cls.folder / 'manifest.json', 'fixture', 'fixture', 'Fixture', cls.options, cls.folder)
        cls.ledger = {'sources': {'Test.vi': {'source_sha256': qa.digest(cls.root / 'Test.vi'),
            'output_dir': 'Test.vi', 'state': 'collection_validated', 'source_evidence': 'Synthetic source.', 'source_evidence_status': 'verified',
            'accepted': accepted, 'manifest': 'manifest.json', 'manifest_sha256': qa.digest(cls.folder / 'manifest.json'),
            'runs': [{'run_id': 'fixture', 'published': True, 'candidates': run_candidates,
                'preflight': {'result': 'PASS', 'evidence': 'Synthetic preflight only.',
                              'candidate_ids': [f'concept-{i}' for i in range(1, 6)]}}]}}}
        cls.ledger['collection_review'] = {'result': 'PASS', 'evidence': 'Synthetic review only.',
            'fingerprint': qa.collection_fingerprint(cls.ledger['sources']),
            'members': qa.collection_members(cls.ledger['sources'])}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_valid_package(self):
        self.assertEqual([], qa.validate(self.root, self.ledger))

    def test_missing_asset(self):
        path = self.folder / self.options[0]['ico_file']
        data = path.read_bytes()
        try:
            path.unlink()
            self.assertTrue(qa.validate(self.root, self.ledger))
        finally:
            path.write_bytes(data)

    def test_wrong_dimensions_and_ico_frame(self):
        for path, replacement in [(self.folder / self.options[0]['derived_png_files'][0]['file'], 'PNG'),
                                  (self.folder / self.options[0]['ico_file'], 'ICO')]:
            data = path.read_bytes()
            try:
                image = Image.new('RGB', (12, 12), 'white')
                image.save(path, format=replacement)
                self.assertTrue(qa.validate(self.root, self.ledger))
            finally:
                path.write_bytes(data)

    def test_reviewed_source_changed(self):
        path = Path(self.ledger['sources']['Test.vi']['accepted'][0]['reviewed_source_file'])
        data = path.read_bytes()
        try:
            path.write_bytes(data + b'changed')
            self.assertTrue(any('reviewed source' in x for x in qa.validate(self.root, self.ledger)))
        finally:
            path.write_bytes(data)

    def test_failed_or_missing_review(self):
        path = self.folder / 'manifest.json'
        original = path.read_text(encoding='utf-8')
        try:
            doc = json.loads(original)
            doc['options'][0]['visual_qa']['checks']['30x18']['result'] = 'FAIL'
            path.write_text(json.dumps(doc), encoding='utf-8')
            self.assertTrue(any('failed 30x18' in x for x in qa.validate(self.root, self.ledger)))
            del doc['options'][0]['visual_qa']['checks']['source']
            path.write_text(json.dumps(doc), encoding='utf-8')
            self.assertTrue(any('failed source' in x for x in qa.validate(self.root, self.ledger)))
        finally:
            path.write_text(original, encoding='utf-8')

    def test_duplicate_mapping_and_stale_collection(self):
        ledger = copy.deepcopy(self.ledger)
        (self.root / 'Other.vi').write_bytes(b'other')
        try:
            ledger['sources']['Other.vi'] = copy.deepcopy(ledger['sources']['Test.vi'])
            ledger['sources']['Other.vi']['source_sha256'] = qa.digest(self.root / 'Other.vi')
            errors = qa.validate(self.root, ledger)
            self.assertTrue(any('duplicates' in x for x in errors))
            self.assertTrue(any('collection-wide' in x for x in errors))
        finally:
            (self.root / 'Other.vi').unlink()

    def test_collection_coverage_and_signature(self):
        ledger = copy.deepcopy(self.ledger)
        ledger['collection_review']['members'].pop()
        ledger['sources']['Test.vi']['accepted'][0]['signature'].pop('cue')
        errors = qa.validate(self.root, ledger)
        self.assertTrue(any('does not cover' in x for x in errors))
        self.assertTrue(any('signature incomplete' in x for x in errors))
        self.assertTrue(any('missing, failed, or stale' in x for x in errors))

    def test_unverified_source_evidence(self):
        ledger = copy.deepcopy(self.ledger)
        ledger['sources']['Test.vi']['source_evidence_status'] = 'partial'
        self.assertTrue(any('not fully verified' in x for x in qa.validate(self.root, ledger)))

    def test_manifest_candidates_and_concepts_must_match_accepted(self):
        path = self.folder / 'manifest.json'
        original = path.read_text(encoding='utf-8')
        try:
            doc = json.loads(original)
            doc['options'][1]['candidate_id'] = doc['options'][0]['candidate_id']
            path.write_text(json.dumps(doc), encoding='utf-8')
            self.assertTrue(any('manifest candidates do not match' in x for x in qa.validate(self.root, self.ledger)))
            doc = json.loads(original)
            doc['options'][0]['concept_id'] = 'wrong-concept'
            path.write_text(json.dumps(doc), encoding='utf-8')
            self.assertTrue(any('manifest concept does not match' in x for x in qa.validate(self.root, self.ledger)))
        finally:
            path.write_text(original, encoding='utf-8')

    def test_identical_source_and_failed_preflight(self):
        ledger = copy.deepcopy(self.ledger)
        entry = ledger['sources']['Test.vi']
        entry['accepted'][1]['reviewed_source_sha256'] = entry['accepted'][0]['reviewed_source_sha256']
        entry['runs'][0]['preflight']['result'] = 'FAIL'
        errors = qa.validate(self.root, ledger)
        self.assertTrue(any('identical reviewed source' in x for x in errors))
        self.assertTrue(any('failed, or superseded concept preflight' in x for x in errors))

    def test_recorded_visual_conflict_follows_artwork_hashes(self):
        ledger = copy.deepcopy(self.ledger)
        entry = ledger['sources']['Test.vi']
        accepted = entry['accepted']
        comparison = self.root / 'icons' / 'comparison.json'
        members = [{'source': 'Test.vi', 'candidate_id': a['candidate_id'],
                    'reviewed_source_sha256': a['reviewed_source_sha256']} for a in accepted[:2]]
        qa.atomic_json(comparison, {'members': members, 'observations': [{'result': 'FAIL',
            'candidates': ['Test.vi/candidate-01', 'Test.vi/candidate-02']}]})
        entry['provisional_comparisons'] = ['icons/comparison.json']
        try:
            self.assertTrue(any('unresolved visual conflict' in x for x in qa.validate(self.root, ledger)))
            # Renaming does not alter which artwork was reviewed.
            accepted[0]['candidate_id'] = 'renamed'
            self.assertTrue(any('unresolved visual conflict' in x for x in qa.validate(self.root, ledger)))
            accepted[0]['reviewed_source_sha256'] = '0' * 64
            self.assertFalse(any('unresolved visual conflict' in x for x in qa.validate(self.root, ledger)))
        finally:
            comparison.unlink()

    def test_sync_preserves_annotations_and_refreshes_preflight(self):
        work = self.root / 'icons' / 'work' / 'labview-icons-fixture'
        work.mkdir(parents=True, exist_ok=True)
        run = {'output_dir': str(self.folder), 'run_id': 'fixture-run', 'candidates': [], 'published': False}
        qa.atomic_json(work / 'run.json', run)
        qa.atomic_json(work / 'preflight.json', {'result': 'FAIL', 'evidence': 'Fixture preflight.'})
        ledger = copy.deepcopy(self.ledger)
        ledger['sources']['Test.vi']['runs'] = [{'run_id': 'fixture-run', 'superseded_by': 'later-run'}]
        qa.atomic_json(self.root / 'icons' / 'collection-ledger.json', ledger)
        first = qa.sync(self.root, work.parent)['sources']['Test.vi']['runs'][0]
        self.assertEqual('later-run', first['superseded_by'])
        self.assertEqual('FAIL', first['preflight']['result'])
        (work / 'preflight.json').unlink()
        second = qa.sync(self.root, work.parent)['sources']['Test.vi']['runs'][0]
        self.assertNotIn('preflight', second)


if __name__ == '__main__':
    unittest.main()
