#!/usr/bin/python

#Openning the devices file
input_file = open('devices', 'rt')

#Reading the file line by line

Router_name = input_file.readline().strip()
IP_Address = input_file.readline().strip()
IOS_image = input_file.readline().strip()
Username = input_file.readline().strip()
Password = input_file.readline().strip()

input_file.close()
#Printing the output nicely
print '--- Device info nicely presented ------------------------------------------------------------'
print 'Name                IP Address       OS Image      Username       Password'
print '-----------         ---------------  -----------   ----------     ----------'
print '{0:19} {1:17} {2:12} {3:14} {4:15}'.format(Router_name,IP_Address,IOS_image,Username,Password)
print '---------------------------------------------------------------------------------------------'



#writing into a file with comma seperated value (creating CSV)
device_info_comma=Router_name
device_info_comma=device_info_comma + ',' + IP_Address
device_info_comma=device_info_comma + ',' + IOS_image
device_info_comma=device_info_comma + ',' + Username
device_info_comma=device_info_comma + ',' + Password

#Writing them into  a csv file

print '---- Writing Devices information into a file ---- \n'

out_file = open('csv_dev_info_out','w')
out_file.write(device_info_comma)
out_file.write('\n')
out_file.close()

# now we will read this CSV file here

print '--- Reading out the CSV File ---'

csv_read = open('csv_dev_info_out','r')
devices_info = csv_read.readline().strip()
csv_read.close()

print ''
print '----- Reading the file ----'
print 'Device Info: ', devices_info
print '---------------------------'
print ''





