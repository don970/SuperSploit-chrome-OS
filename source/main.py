import sys
from core.inputHandler import Input


class Main:
    def __init__(self):
        try:
            """calls the main input handler"""
            Input.get()
        except KeyboardInterrupt:
            print(f"Good bye. );")
            sys.exit()


Main()