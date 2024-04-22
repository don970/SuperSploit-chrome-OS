import json
import os
import pty
import socket
import traceback
from subprocess import run, Popen, PIPE
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from .netToolAttacks import nmap

history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt

closing_statements = ["exit", 'close', 'back']


def sys_call_Linux(data):
    dataList = data.split(' ')
    with open(".data/Aliases.json") as file:
        Aliases = json.load(file)
        file.close()
    for k, v in Aliases.items():
        if k in dataList:
            dataList[dataList.index(k)] = v
    if "cd" in dataList:
        print("[*] The cd command will spawn a shell in the folder you change to. This is\n"
                       "because the program release on the working dir to be the programs install\n"
                       "folder. I will update in future to be able to just use cd.")
        cwd = os.getcwd()
        os.chdir(dataList[1])
        pty.spawn(f"{os.getenv('SHELL')}")
        os.chdir(cwd)
    if "cat" in dataList:
        with open(dataList[1], 'r') as file:
            print(file.read())
            file.close()
            return
    try:
        if "ls" in data:
            cmd = run(dataList)
            return
        cmd = Popen(dataList, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        output = cmd.communicate()[0], cmd.communicate()[1]
        for x in output:
            if len(x) > 0:
                print(x.decode())
        return True
    except Exception as e:
        print(e)
# replace the print method


def print(data):
    if "str" not in str(type(data)):
        try:
            data = data.decode()
            pass
        except Exception:
            data = f"{str(data)}"
            pass
    if not data.endswith("\n"):
        data = f"{data}\n"
    with open("/dev/stdout", "w") as stdout:
        stdout.write(data)
        stdout.close()
    return


def get_network_info():
    host = socket.gethostname()
    data = run(["ip", "addr"], capture_output=True).stdout.decode().split("\n")
    for i in data:
        if "inet" and "brd" in i and ":" not in i:
            ip = i.split(" ")[5].split('/')[0]
            subnet = i.split(" ")[5].split('/')[1]
            return ip, subnet, host


class help:
    def __init__(self, master):
        self.a = master.split(' ')
    @classmethod
    def help(cls):
        data = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
        with open(f".data/.help/all", "r") as file:
            print("\033[H\033[J")
            print(file.read())
            file.close()


class WifiScan:

    def __init__(self, master: list):
        error = master
        ip, subnet, host = get_network_info()
        self.GetData([ip, subnet, host])

    def GetData(self, ip_subnet_and_host):
        n = nmap(ip_subnet_and_host)
        while True:
            funcs = [n.scan_whole_network, n.targetedScan, help.help, n.show_target_list, n.Import, n.customScan]
            inputs = ["get-targets", "scan-target", "help", "view-targets", "import-targets", "custom-scan"]
            data = input(f"{os.getcwd()}:[WiFi Menu]: ")
            for x in closing_statements:
                if x in data:
                    return "Exiting"
            if data in inputs:
                print(funcs[inputs.index(data)]())
                continue
            try:
                sys_call_Linux(data)
                continue
            except Exception as e:
                print(e)
