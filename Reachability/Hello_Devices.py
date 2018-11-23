
#Importing the PEXPECT Library
import pexpect
#Spawn an exec Command within the PEXPECT
ping_yahoo=pexpect.spawn('ping -c 5 yahoo.com')
#What to expect with the PEXPECT Command
results=ping_yahoo.expect([pexpect.EOF, pexpect.TIMEOUT])
print ping_yahoo.before
