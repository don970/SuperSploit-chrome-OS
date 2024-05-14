import os
import subprocess
import sys
import threading

from .ToStdOut import ToStdout
true = True
false = False
print = ToStdout.write

class Input_fixes:
    def __init__(self, dataList: list):
        self.list = dataList
        ListOfFixes = [self.cd, self.clear, self.exit, self.cat]
        fixes = ["cd", "clear", "exit", "cat"]
        ListOfFixes[fixes.index(dataList[0])]()
        return

    @classmethod
    def continues(cls, data):
        def procone(data):
            subprocess.run(data.split(" "))
            return 0

        for x in data.split(" && "):
            str = x
            proc = threading.Thread(target=procone, args=((str, )))
            proc.start()
            proc.join()


    def cat(self):
        if len(self.list) < 1:
            return False
        try:
            if self.list[1] == "":
                return False
        except:
            return False
        with open(self.list[1], "r") as file:
            print(file.read())
            file.close()
        return

    @staticmethod
    def exit():
        sys.exit()

    def cd(self) -> int:
        os.chdir(self.list[1])
        return 0

    @staticmethod
    def clear():
        print("\033[H\033[J")

