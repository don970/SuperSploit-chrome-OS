import subprocess as sub
import time

from ppadb.client import Client as AdbClient


# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()


# Get device ip address by running ifconfig wlan0 via a adb test
def ip():
    for device in devices:
        devicesInfo = str(device.shell('ifconfig wlan0')).split('\n')
        ipp = str(devicesInfo[1].split(' ')[11]).split(':')[1]
        return ipp


# Connect to discovered device
def adb_connect():
    ipp = ip()
    sub.run(['adb', 'disconnect'])
    sub.run(['adb', 'tcpip', '5555'])
    time.sleep(2)
    sub.run([f'adb', 'connect', f'{ipp}:5555'])


adb_connect()
