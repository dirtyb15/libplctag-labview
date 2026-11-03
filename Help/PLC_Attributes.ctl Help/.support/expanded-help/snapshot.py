from html.parser import HTMLParser
from pathlib import Path
import json,hashlib,sys
b=Path('Help/PLC_Attributes.ctl Help/.support/expanded-help');p=Path(sys.argv[1]) if len(sys.argv)>1 else b/'PLC_Attributes.ctl.html'
class Extract(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.block=None;self.parts=[];self.sections=[];self.unit=0
 def handle_starttag(self,t,a):
  if t in ('h2','p','tr','li','pre') and self.block is None:self.block=t;self.parts=[]
  elif t in ('th','td') and self.block=='tr' and self.parts:self.parts.append(' | ')
 def handle_data(self,t):
  if self.block:self.parts.append(t)
 def handle_endtag(self,t):
  if t==self.block:
   v=''.join(self.parts).strip();self.block=None
   if t=='h2':self.sections.append({'id':f'section-{len(self.sections)+1}','title':v,'level':2,'units':[]})
   elif self.sections:
    self.unit+=1;self.sections[-1]['units'].append({'id':f'unit-{self.unit}','kind':{'p':'paragraph','tr':'table-row','li':'list-item','pre':'code'}[t],'text':v})
x=Extract();x.feed(p.read_text(encoding='utf8'))
s={'artifact':str(p.resolve()),'artifact_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'profile':{'audience':'LabVIEW developer who is new to PLCs and industrial networks','prerequisites':'Basic LabVIEW controls, wires and error clusters; PLC terms introduced in the text'},'sections':x.sections}
q=b/'review';q.mkdir(exist_ok=True);(q/'snapshot.json').write_text(json.dumps(s,indent=2)+'\n',encoding='utf8')
print(len(x.sections),'sections',x.unit,'text units')
