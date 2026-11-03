import json
from pathlib import Path
import collection_qa as q
root = Path(__file__).resolve().parent.parent
ledger = q.read_json(root/'icons/collection-ledger.json')
count=0
for rel, entry in ledger['sources'].items():
    folder=root/'icons'/entry['output_dir']
    path=folder/'manifest.json'
    if not path.is_file() or q.inventory(root).get(rel)!=entry['source_sha256']:
        continue
    manifest=q.read_json(path)
    runs=[r for r in entry['runs'] if r.get('run_id')==manifest.get('run_id') and r.get('published')]
    if len(runs)!=1 or len(manifest.get('options',[]))!=5: continue
    run=runs[0]; items=[]
    for opt in manifest['options']:
        candidates=[c for c in run['candidates'] if c['id']==opt['candidate_id']]
        if len(candidates)!=1: break
        c=candidates[0]
        items.append({'candidate_id':c['id'],'concept_id':c['concept_id'],'run_id':run['run_id'],
            'signature':c['signature'],'reviewed_source_file':c['source_file'],
            'reviewed_source_sha256':c['reviewed_sha256'],
            'master_sha256':opt['sha256'][opt['source_file']]})
    if len(items)!=5: continue
    entry.update({'accepted':items,'manifest':path.name,'manifest_sha256':q.digest(path),'state':'set_validated'})
    count+=1
ledger['collection_review']={'result':'WAIVED','evidence':'User instructed that cross-file similarity checks be skipped to save time and LLM usage.'}
q.atomic_json(root/'icons/collection-ledger.json',ledger)
print(f'Reconciled {count} published packages; cross-file similarity review explicitly waived.')
