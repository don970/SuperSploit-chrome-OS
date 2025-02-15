# This is a wrapper for nmap
import os
import sys
from subprocess import run
# redefine input method
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt
installation = f'{os.getenv("HOME")}/.SuperSploit'

# replace the print method
def print(data):
    if "str" not in str(type(data)):
        data = f"{str(data)}"
    if not data.endswith("\n"):
        data = f"{data}\n"

    sys.stdout.write(data)
    return



class nmap:
    def __init__(self, ip):
        """This is a wrapper to use the tool nmap to
        scan for live host identification and more"""
        self.ip = ip[0]
        self.subnet = ip[1]
        self.targetlist = []
        return

    def Import(self):
        with open(f"{installation}/.data/.targets") as file:
            print("[*] Repopulating targets list via target file. ")
            for x in file.read().split("\n"):
                self.targetlist.append(x)
            file.close()
        return "[*] Targets saved."

    def show_target_list(self):
        if len(self.targetlist) == 0:
            return "[!] Target list is not populated"
        for x in self.targetlist:
            print(x)
        return "[*] Showing all saved targets"

    def scan_whole_network(self) -> list or False:
        try:
            ip = self.ip.split(".")[0:3]
            ip.append("0")
            st = ""
            for x in ip:
                if ip.index(x) < len(ip) - 1:
                    st += x + "."
                else:
                    st += x
            ip = st
            if not input(f"would you like to perform a scan with a subnet of ({ip}/{self.subnet}): ").startswith("y"):
                ip = input("[*] Enter the address and subnet [ip/sub]: ")
                print("[*] IP and subnet updated.")
            print("[*] Scanning...")
            a = run(["nmap", "-sn", ip], capture_output=True)
            li = []
            print("[*] Formatting output.")
            result = a.stdout.decode().split('\n')
            self.results = result
            for x in result:
                # 31 is the length of "scan report for xxx.xxx.xxx.xxx"
                if len(x) > 31 and "http" not in x and "add" not in x:
                    # split output and take the 4 index of the output and add to a list
                    li.append(x.split(" ")[4])
            print("[*] Populating targets file.")
            with open(f"{installation}/.data/.targets", "w") as file:
                for x in li:
                    if li.index(x) < len(li) - 1:
                        file.write(f"{x}\n")
                    else:
                        file.write(f"{x}")
                file.close()
            print("[*] Dumping targets to a global list.")
            self.targetlist = li
            return "[*] Targets added."
        except KeyboardInterrupt:
            return "[!] Exiting scan mode"

    def targetedScan(self) -> str or False:
        try:
            if len(self.targetlist) < 1:
                return "[!] No targets available."
            for x in self.targetlist:
                print(f"{self.targetlist.index(x)}: {x}")
            data = input("Enter the index of the target: ")
            try:
                data = int(data)
                pass
            except Exception:
                return "[!] Invaild Input"
            print("[*] Scanning... ")
            output = run(["nmap", "-A", self.targetlist[data]], capture_output=True)
            print("[*] Populating targeted scan file")
            with open(f"{installation}/.data/.targeted_scan", "w") as file:
                file.write(output.stdout.decode())
                file.close()
            return "[*] Full scan logged to .data/.targeted_scan"
        except KeyboardInterrupt:
            return "[!] Exiting scan mode"

    def customScan(self):
        try:
            if len(self.targetlist) < 1:
                return "[!] No targets available."
            for x in self.targetlist:
                print(f"{self.targetlist.index(x)}: {x}")
            data = input("Enter the index of the target: ")
            try:
                data = int(data)
                pass
            except Exception:
                return "[!] Invalid Input"
            data1 = input("Now enter the arguments to use: ")
            print("[*] Scanning... ")
            output = run(["nmap", data1, self.targetlist[data]], capture_output=True)
            print("[*] Populating custom scan file")
            with open(f"{installation}/.data/.custom_scan", "w") as file:
                file.write(output.stdout.decode())
                file.close()
            return "[*] Full scan logged to .data/.custom_scan"
        except KeyboardInterrupt:
            return "[!] Exiting scan mode"

    def traceroute(self):
        run(["traceroute", "google.com"])
        return

