
#Importing the PEXPECT Library
import pexpect
#Spawn an exec Command within the PEXPECT
ping_devices=pexpect.spawn('ping -c 5 localhost')
#What to expect with the PEXPECT Command
results=ping_devices.expect([pexpect.EOF, pexpect.TIMEOUT])
print ping_devices.before
