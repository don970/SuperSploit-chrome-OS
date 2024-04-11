import traceback

import pyfiglet
from .ToStdOut import ToStdout
import os
import random
installation = f'{os.getenv("HOME")}/.SuperSploit'

class banners:
    def __init__(self, *args):
        os.system("clear")
        try:
            with open(f"{installation}/.data/.banners/{random.choice(os.listdir('.data/.banners/'))}") as file:
                data = file.read()
                file.close()
                data = data.split("#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!")
                choice = random.choice(data)
                ToStdout.write(pyfiglet.figlet_format("Supersploit"))
                ToStdout.write(choice)
                return
        except Exception:
            ToStdout.write(traceback.format_exc())

