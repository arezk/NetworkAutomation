#!/usr/bin/python

from pprint import pprint
from collections import namedtuple

devices=[]

#opening the file

newfile= open('list.csv', 'r')

for line in newfile:
    device_info = tuple(line.strip().split(','))
    print 'Devices info: ', device_info
    devices.append(device_info)

pprint(devices)

newfile.close()

