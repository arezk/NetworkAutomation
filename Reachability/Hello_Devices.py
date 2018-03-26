import pexpect
ping_devices=pexpect.spawn('ping -c 5 localhost')
results=ping_devices.expect([pexpect.EOF, pexpect.TIMEOUT])
print ping_devices.before
