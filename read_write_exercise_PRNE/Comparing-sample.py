import re

print '' # Print heading
print 'Devices and their versions'
print '=================================='

# Set Variable for current version comparison used in Step 4

current_version = 'Version 5.3.1'
version_pattern = re.compile('version ([0-9][0-9]?\.[0-9]\.?[0-9]?)')
# Read all lines of device information from file
file = open('devices','r')
for line in file:

    device_info_list = line.strip().split(',') # Get device info into list
    device_info ={}
    device_info['name'] = device_info_list[0]
    #obtaining the version info by searching in each line of the pattern above
    version_info=version_pattern.search(line)
    device_info['version'] = version_info.group(1)

    #printing the result

    print 'Device:', device_info['name'],'      Version:', device_info['version']

print ''

file.close()




