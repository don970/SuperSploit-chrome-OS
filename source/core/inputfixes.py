import os
import subprocess
import sys

from .ToStdOut import ToStdout


class Input_fixes:
    def __init__(self, dataList: list):
        self.list = dataList
        ListOfFixes = [self.cd, self.clear, self.exit, self.cat]
        fixes = ["cd", "clear", "exit", "cat"]
        ListOfFixes[fixes.index(dataList[0])]()
        return

    def cat(self):
        if len(self.list) < 1:
            return False
        return

    @staticmethod
    def exit():
        sys.exit()

    def cd(self) -> int:
        os.chdir(self.list[1])
        return 0

    @staticmethod
    def clear():
        ToStdout.write("\033[H\033[J")

