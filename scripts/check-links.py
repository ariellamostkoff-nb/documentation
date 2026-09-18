#!/usr/bin/env python3
"""Check a list of docs.northbeam.io URLs against this repo's pages + redirects.

Usage:  python3 scripts/check-links.py urls.txt        (one URL or path per line)
        pbpaste | python3 scripts/check-links.py -      (from clipboard)
Prints one line per URL: OK / REDIRECT -> dest / ANCHOR-JUMP -> dest / MISSING.
"""
import json, re, sys, os
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT/'docs.json'))
nav=set()
def walk(x):
    if isinstance(x,str) and (x.startswith('docs/') or x.startswith('reference/')): nav.add(x)
    elif isinstance(x,dict): [walk(v) for v in x.values()]
    elif isinstance(x,list): [walk(v) for v in x]
walk(d['navigation'])
exact={r['source'].rstrip('/'):r['destination'] for r in d['redirects'] if ':' not in r['source']}
wild=[(re.compile('^'+re.sub(r':(\w+)\*',r'(?P<\1>.*)',r['source'])+'$'),r['destination']) for r in d['redirects'] if ':' in r['source']]
js=(ROOT/'interactions.js').read_text()
m=re.search(r'var MAP = (\{.*?\});',js,re.S); amap=json.loads(m.group(1)) if m else {}
def page_exists(p):
    p=p.lstrip('/'); return p in nav or (ROOT/(p+'.mdx')).exists()
def resolve(url):
    path=re.sub(r'^https?://docs\.northbeam\.io','',url.strip()); path=re.sub(r'\.md(?=$|[#?])','',path)
    frag=''; 
    if '#' in path: path,frag=path.split('#',1)
    path=path.split('?')[0].rstrip('/').rstrip('\\') or '/'
    if page_exists(path): return 'OK', path+('#'+frag if frag else '')
    dest=exact.get(path)
    if not dest:
        for rx,dst in wild:
            mm=rx.match(path)
            if mm: dest=re.sub(r':(\w+)\*',lambda k: mm.group(k.group(1)),dst); break
    if dest:
        if not page_exists(dest) and dest in exact: return 'MISSING (chained redirect)', dest
        if frag and dest in amap and frag in amap[dest]: return 'ANCHOR-JUMP', amap[dest][frag]
        return 'REDIRECT', dest+('#'+frag if frag else '')
    return 'MISSING', ''
if __name__=='__main__':
    src=sys.stdin if (len(sys.argv)<2 or sys.argv[1]=='-') else open(sys.argv[1])
    counts={}
    for line in src:
        u=line.strip()
        if not u or u.startswith('#'): continue
        st,dest=resolve(u); counts[st.split()[0]]=counts.get(st.split()[0],0)+1
        print(f'{st:24s} {u}' + (f'  ->  {dest}' if dest and st!='OK' else ''))
    print('\nSUMMARY:', ', '.join(f'{k}={v}' for k,v in sorted(counts.items())), file=sys.stderr)
