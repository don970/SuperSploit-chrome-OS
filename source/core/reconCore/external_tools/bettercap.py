import subprocess


class bettercap:
    def __init__(self, ar):
        try:
            subprocess.run(["sudo", "bettercap"])
            return
        except OSError:
            return False
        pass