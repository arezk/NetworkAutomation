#!/usr/bin/python

device_string =  '  1.1.1.1, username  , password   '
info_list = [ device.strip() for device in device_string.split(',') ]
print info_list
