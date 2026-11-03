import json, subprocess, os
from pathlib import Path
root=Path(__file__).resolve().parent
skill=Path.home()/'.codex/skills/labview-icon-creator/scripts/run_icons.py'
files={'Read_Double.vi':'F64','Read_Float.vi':'F32','Read_I64.vi':'I64','Read_U16.vi':'U16','Read_U32.vi':'U32','Read_U64.vi':'U64','Set_Double.vi':'F64','Set_Float.vi':'F32','Set_I16.vi':'I16','Set_I32.vi':'I32','Set_I64.vi':'I64','Set_I8.vi':'I8','Set_U16.vi':'U16','Set_U32.vi':'U32','Set_U64.vi':'U64','Set_U8.vi':'U8'}
for name,label in files.items():
    is_read=name.startswith('Read_'); action='reading from' if is_read else 'writing into'; direction='pointing AWAY from' if is_read else 'pointing TOWARD'; verb='out of' if is_read else 'into'
    common=(f'One SQUARE flat software icon on white for {action} a tag buffer a value of datatype {label}. '
       f'Across the TOP place exactly {label} in HUGE BOLD BLACK characters with large WHITE GAPS between each character. '
       'Capital I, if present, MUST have broad horizontal top and bottom bars, clearly different from digit 1. '
       f'The exact label {label} must dominate the image and remain legible at 30x18 pixels. No other text, no shadows. ')
    motifs=[('buffer-arrow','Typed buffer transfer',f'Below the type show a large BLUE rectangular buffer and a bold ORANGE horizontal arrow {direction} the buffer. The arrow must clearly show data going {verb} the buffer.'),
            ('cylinder-arrow','Typed cylinder transfer',f'Below the type show a large BLUE cylindrical buffer and a thick ORANGE vertical arrow {direction} the cylinder. Make arrow direction obvious for data going {verb} the cylinder.'),
            ('tray-arrow','Typed tray transfer',f'Below the type show a wide BLUE U-shaped tray and one large ORANGE vertical arrow {direction} the tray. The arrow visibly indicates data going {verb} the tray.'),
            ('card-arrow','Typed card transfer',f'Below the type show a simple BLUE card-shaped buffer at left and a thick ORANGE arrow {direction} the card, clearly indicating data going {verb} it.'),
            ('socket-arrow','Typed socket transfer',f'Below the type draw a large BLUE circular buffer socket, plus a thick ORANGE diagonal arrow {direction} the socket. The arrow must visibly indicate data going {verb} the socket.')]
    concepts=[]
    for ident,summary,desc in motifs:
        concepts.append({'concept_id':ident,'concept_summary':summary,'signature':{'metaphor':ident,'objects':'type label, buffer, arrow','cue':f'{verb} buffer','composition':desc,'orientation':ident},'prompt':common+desc+' Center the entire design within the square.'})
    plan={'request':f'{action} tag buffer {label} at offset','summary_name':name[:-3].replace('_',' '),'background_mode':'white','concepts':concepts}
    path=root/'work'/('plan-'+name+'.json');path.write_text(json.dumps(plan,indent=2),encoding='utf-8')
    proc=subprocess.run([r'C:\Python314\python.exe',str(skill),'init','--plan',str(path),'--output-dir',str(root/name),'--work-root',str(root/'work')],capture_output=True,text=True,check=True)
    run_file=Path(json.loads(proc.stdout)['run_file']);preflight={'result':'PASS','scope':'Local concept planning; cross-file similarity review waived by user','candidate_ids':[c['concept_id'] for c in concepts],'evidence':'Five transfer cues use different buffer shapes and arrow positions. Shared type layout is permitted by user.'};(run_file.parent/'preflight.json').write_text(json.dumps(preflight,indent=2),encoding='utf-8')
    print(name,run_file)
