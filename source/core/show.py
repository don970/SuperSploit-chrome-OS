from .database import DatabaseManagment
from .ToStdOut import ToStdout
from .exploithandler import exploitDetails


class Show:

    @staticmethod
    def shells(ars):
        with open('/etc/shells') as file:
            ToStdout.write(file.read())
            file.close()

    @staticmethod
    def show(data):
        if len(data.split(" ")) < 2:
            for k, v in DatabaseManagment.get().items():
                ToStdout.write(f"{k}: {v}")
            return
        elif "details" in data.split(" ")[1]:
            exploitDetails()
            return
        elif len(data.split(' ')) > 1:
            for x in data.split(" "):
                if data.split(" ").index(x) > 0:
                    for k, v in DatabaseManagment.get().items():
                        if data.split(' ')[data.split(" ").index(x)] == k:
                            ToStdout.write(f"{k}: {v}")
            return
        else:
            return
