import os

from .ToStdOut import ToStdout
write = ToStdout.write

installation = f'{os.getenv("HOME")}/.SuperSploit'

class Error:
    def __init__(self, data):
        """Error Handling Method prints to stdout and writes to 'installation_dictionary/.data/.errors/error.log'"""
        try:
            if "str" not in str(type(data)):
                try:
                    data = data.decode()
                    pass
                except Exception:
                    data = f"{str(data)}"
                    pass
            if not data.endswith("\n"):
                data = f"{data}\n"
            with open(f"{installation}/.data/.errors/error.log", "a") as stdout:
                stdout.write(data)
                stdout.close()
            write(data)
            return
        except Exception as e:
            write(e)
