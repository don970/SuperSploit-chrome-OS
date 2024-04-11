# This is a wrapper for nmap
import os
from subprocess import run
# redefine input method
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt

# replace the print method
def print(data):
    if "str" not in str(type(data)):
        data = f"{str(data)}"
    if not data.endswith("\n"):
        data = f"{data}\n"
    with open("/dev/stdout", "w") as stdout:
        stdout.write(data)
        stdout.close()
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
        with open(".data/.targets") as file:
            print("[*] Repopulating targets list via target file. ")
            for x in file.read().split("\n"):
                self.targetlist.append(x)
            file.close()

        return "[*] Targets saved."
    def show_target_list(self):
        for x in self.targetlist:
            print(x)
        return "[*] Showing all saved targets"

    def  scan_whole_network(self) -> list or False:
        custr = f"{self.ip}/{self.subnet}"
        if not input(f"would you like to perform a scan with a subnet of ({self.ip}/{self.subnet}): ").startswith("y"):
            custr = input("[*] Enter the address and subnet [ip/sub]: ")
            print("[*] IP and subnet updated.")

        print("[*] Scanning...")
        a = run(["nmap", "-sn", custr], capture_output=True)
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
        with open(".data/.targets", "w") as file:
            for x in li:
                if li.index(x) < len(li) - 1:
                    file.write(f"{x}\n")
                else:
                    file.write(f"{x}")
            file.close()
        print("[*] Dumping targets to a global list.")
        self.targetlist = li
        return "[*] Targets added."

    def targetedScan(self) -> str or False:
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
        with open(".data/.targeted_scan", "w") as file:
            file.write(output.stdout.decode())
            file.close()
        return "[*] Full scan logged to .data/.targeted_scan"

    def customScan(self):
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
        with open(".data/.custom_scan", "w") as file:
            file.write(output.stdout.decode())
            file.close()
        return "[*] Full scan logged to .data/.custom_scan"

