import sys


class ToStdout:
    @staticmethod
    def write(data):
        """Writes to /dev/stdout"""
        if "str" not in str(type(data)):
            try:
                data = data.decode()
                pass
            except Exception:
                data = f"{str(data)}"
                pass
        if not data.endswith("\n"):
            data = f"{data}\n"
        try:
            sys.stdout.write(data)
        except Exception as e:
            with open("/dev/stdout", "w") as stdout:
                stdout.write(str(e))
                stdout.close()
            with open("/dev/stdout", "w") as stdout:
                stdout.write(data)
                stdout.close()
            return
