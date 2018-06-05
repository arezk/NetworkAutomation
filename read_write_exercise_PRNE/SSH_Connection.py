
# Importing Paramiko Library

import paramiko


ip_address = '10.30.30.1'
username = 'cisco'
password = 'cisco'

print '\n------------------------------------------------------'
print '--- Attempting paramiko connection to: ', ip_address

# Create paramiko session
ssh_client = paramiko.SSHClient()

# Must set missing host key policy since we don't have the SSH key
# stored in the 'known_hosts' file
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Make the connection to our host.
ssh_client.connect(hostname=ip_address,
                   username=username,
                   password=password)

# If there is an issue, paramiko will throw an exception,
# so the SSH request must have succeeded.

print '--- Success! connecting to: ', ip_address
print '---               Username: ', username
print '---               Password: ', password
print '------------------------------------------------------\n'

print '------------------------------------------------------\n'
print '-----Changing the hostname of router r1 to R1  -------\n'

stdin, stdout, stderr = ssh_client.exec_command('configure t')
stdin, stdout, stderr = ssh_client.exec_command('hostname R1')
stdin, stdout, stderr = ssh_client.exec_command('exit')

ssh_client.close()


