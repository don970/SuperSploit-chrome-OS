import os
import sys

from core.inputHandler import Input


class Main:
    def __init__(self):
        try:
            """calls the main input handler"""
            Input.get()
        except KeyboardInterrupt:
            sys.stdout.write(f"Good by {os.getlogin()}")
            sys.exit()


Main()