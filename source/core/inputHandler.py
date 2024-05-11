import json
import os
import traceback
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import subprocess
from subprocess import PIPE
from .errors import Error
from .ToStdOut import ToStdout
from .help import Help
from .show import Show
from .set import SetV
from .exploithandler import ExploitHandler
from .use import use
from .search import Search
from .banners import banners
from .database import DatabaseManagment
from .inputfixes import Input_fixes
from .clean import clean

installation = f'{os.getenv("HOME")}/.SuperSploit'
history = FileHistory(f'{installation}/.data/.history/history')
with open(".data/Aliases.json") as file:
    aliases = json.load(file)
    file.close()

env = os.environ


class Input:
    @classmethod
    def sys_call_Linux(cls, data):
        shells = DatabaseManagment.findShells()
        if data in shells:
            subprocess.run([f"/usr/bin/{data}"])
        dataList = data.split(' ')
        with open(f"{installation}/.data/Aliases.json") as file:
            Aliases = json.load(file)
            file.close()
        for k, v in Aliases.items():
            if k in dataList:
                dataList[dataList.index(k)] = v
        try:
            subprocess.run(dataList)
            return True
        except Exception:
            Error(traceback.format_exc())
            return False

    @classmethod
    def sys_call_other(cls, data):
        try:
            cmd = subprocess.Popen(data.split(" "), stdout=PIPE, stdin=PIPE, stderr=PIPE)
            output = cmd.communicate()[0], cmd.communicate()[2]
            for x in output:
                if len(x) > 0:
                    ToStdout.write(x.decode())
                return True
        except Exception:
            Error(traceback.format_exc())
            return False

    def __init__(self):
        """This handles all the input"""
        pass

    @classmethod
    def check(cls, data):
        dataList = data.split(" ")
        for k, v in aliases.items():
            if k in data.split(" "):
                dataList = data.split(' ')[0:len(data.split(" ")) -1]
                dataList.append(v)
        inputFixList = ["cd", "clear", "exit"]
        try:
            if dataList[0] in inputFixList:
                Input_fixes(dataList)
                return
            if data.endswith(" "):
                data = data.lstrip(" ")
            functions = [clean, Show.shells, Recon, Help.help, Show.show, SetV.SetV, ExploitHandler, use, Search.search,
                         banners, DatabaseManagment.addVariableToDatabase]
            inputs = ["clean", "shells", "recon", "help", "show", "set", "exploit", "use", "search", "banner", "add"]
            try:
                if data.split(" ")[0] in inputs:
                    functions[inputs.index(data.split(" ")[0])](data)
                    return
                if "Linux" in os.uname():
                    cls.sys_call_Linux(data)
                    return
                cls.sys_call_other(data)
            except Exception:
                Error(traceback.format_exc())
        except Exception:
            Error(traceback.format_exc())

    @classmethod
    def get(cls):
        banners()
        while True:
            try:
                data = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
                inp = data.prompt(f"[SuperSploit]: ")
                cls().check(inp)
            except Exception:
                Error(traceback.format_exc())
                continue
