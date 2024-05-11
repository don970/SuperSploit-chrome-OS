import json
import os
import subprocess
import traceback
import socket
from .errors import Error
from .help import Help
from .inputfixes import Input_fixes
from .show import Show
from .set import SetV
from .exploithandler import ExploitHandler
from .use import use
from .search import Search
from .banners import banners
from .database import DatabaseManagment
from subprocess import Popen, run, PIPE
from .reconCore.networkRecon import WifiScan
from .reconCore.Bluetooth import bt
from .reconCore.external_tools.namesearch import NameSearch
from .reconCore.external_tools.phoneinfoga import Phone
from .reconCore.external_tools.bettercap import bettercap
from .reconCore.external_tools.wireshark import wireshark
# redefine input method
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
installation = f'{os.getenv("HOME")}/.SuperSploit'
history = FileHistory(f'{installation}/.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt


def recon_ng(data):
    run(["python3", f"{installation}/source/core/reconCore/external_tools/recon-ng/recon-ng"])
    return

def sys_call_Linux(data):
    shells = DatabaseManagment.findShells()
    dataList = data.split(" ")
    with open(f"{installation}/.data/Aliases.json") as file:
        Aliases = json.load(file)
        file.close()
    for k, v in Aliases.items():
        if k in data.split(" "):
            dataList = data.split(' ')[0:len(data.split(" ")) - 1]
            dataList.append(v)
    if data in shells:
        subprocess.run([f"/usr/bin/{data}"])
    inputFixList = ["cd", "clear", "exit"]
    try:
        if dataList[0] in inputFixList:
            Input_fixes(dataList)
            return
        subprocess.run(dataList)
        return True
    except Exception:
        Error(traceback.format_exc())
        return False

def get_network_info():
    host = socket.gethostname()
    data = run(["ip", "addr"], capture_output=True).stdout.decode().split("\n")
    for i in data:
        if "inet" and "brd" in i and ":" not in i:
            ip = i.split(" ")[5].split('/')[0]
            subnet = i.split(" ")[5].split('/')[1]
            return ip, subnet, host

class Recon:

    def __init__(self, args):
        self.database = DatabaseManagment.get()
        while True:
            try:
                functions = [NameSearch.main, wireshark, bettercap, recon_ng, Phone, WifiScan, bt, Help.help, Show.show, SetV.SetV, ExploitHandler, use, Search.search, banners, DatabaseManagment.addVariableToDatabase]
                inputs = ["name-search", "wireshark", "bettercap", "recon-ng", "phoneinfoga", "wifi", "bt", "help", "show", "set", "exploit", "use", "search", "banner", "add"]
                data = input("[Recon menu]: ")
                if data.split(" ")[0] in inputs:
                    functions[inputs.index(data.split(" ")[0])](data)
                    continue
                if "exit" in data:
                    break
                try:
                    sys_call_Linux(data)
                except Exception:
                    Error(traceback.format_exc())
            except Exception:
                Error(traceback.format_exc())
