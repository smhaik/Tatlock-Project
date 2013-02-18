#!/usr/bin/env python
import json
import shutil

f = open("/home/knoxdw/hdw/tatlock-exhibit/expanded/html/expanded.json")
jset = json.load(f)
itemlist = jset['items']

f.close()

n = 1
results = []
for j in itemlist:
    r = json.loads("{}")
    r['model'] = 'bookexhibit.book'
    r['pk'] = n
    if j.has_key('has_backmatter'):
        if j['has_backmatter']=='Y' or j['has_backmatter']=='y':
            j['has_backmatter']='True'
        if j['has_backmatter']=='N' or j['has_backmatter']=='n':
            j['has_backmatter']='False'
    if j.has_key('has_illustrations'):
        if j['has_illustrations']=='Y' or j['has_illustrations']=='y':
            j['has_illustrations']='True'
        if j['has_illustrations']=='N' or j['has_illustrations']=='n':
            j['has_illustrations']='False'
    if j.has_key('has_frontispiece'):
        if j['has_frontispiece']=='Y' or j['has_frontispiece']=='y':
            j['has_frontispiece']='True'
        if j['has_frontispiece']=='N' or j['has_frontispiece']=='n':
            j['has_frontispiece']='False'
    r['fields'] = j
    n += 1
    results.append(r)
f = open("books.json.new", 'w')
json.dump(results,f)
