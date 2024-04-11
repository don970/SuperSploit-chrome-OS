from math import fabs
from ppadb.client import Client as AdbClient
from subprocess import run

adb = AdbClient()
devices = adb.devices()

def uid_to_0():
    if len(devices) > 1:
        return False
    try:
        a = run(['adb', 'root'], capture_output=True)
        if a.stdout.decode() == 'adbd is already running as root':
            return True
        return True
    except:
        return False

class adb():

    def __init__(self) -> None:
        while uid_to_0():
            if not self.sendCommand(input('Enter command to send via adb_root use # to exit: ')):
                break 

    def sendCommand(self, command):
        if str(command).startswith('#'):
            return False
        for x in devices:
            a = x.shell(command)
            print(a)
        return True

adb()