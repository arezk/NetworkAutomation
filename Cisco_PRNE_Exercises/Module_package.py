#!/usr/bin/env python

facts = {'platform': 'nexus', 'model': '9396', 'hostname': 'NX01', 'vendor': 'cisco', 'vlans': ['1', '5', '10']}
import json
import time
from os import getcwd
print json.dumps(facts,indent=4)

routers=['r1','r2','r3']

for router in routers:
    print 'My router name is ',router
    time.sleep(1)

print getcwd()
