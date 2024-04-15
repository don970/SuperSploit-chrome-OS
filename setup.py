#!/usr/bin/env python3
import json
import os
import subprocess
import traceback

from prompt_toolkit import prompt

try:
    # create an object to hold the aliases

    a = {
        "~": os.getenv("HOME"),
        "install_dir": f"{os.getenv('HOME')}/.SuperSploit"
    }

    # Creating a variable for the installation path also creates a pointer
    # allowing us to use the cd command while still knowing the full path to the
    # installation dictionary.

    installation = f'{os.getenv("HOME")}/.SuperSploit'
    with open(f"{installation}/.data/Aliases.json", "w") as file:
        file.write(json.dumps(a))
        file.close()
        
    
    commands = """sudo apt-get install python3-prompt-toolkit -y
sudo apt-get install python3-pyfiglet -y
sudo apt-get install netcat-traditional adb fastboot pip -y""".split("\n")

    command_one = """pip install --break-system-packages pure-python-adb
pip install --break-system-packages  pwn 
pip install --break-system-packages pybluez
bash <( curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install )
sudo mv ./phoneinfoga /usr/local/bin/phoneinfoga
cd $HOME/.SuperSploit/source/core/reconCore/external_tools/ && git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng && pip install --break-system-packages -r REQUIREMENTS
cd $CWD
bash executable.sh""".split('\n')

    with open(".data/.terminals") as file:
        terms = file.read().split("\n")
        file.close()
    programs = os.listdir("/bin")
    term = False
    prompt("[*] The following will attempt to install a terminal program if none are present in bin folder defaults to "
           "Tilix.\nPress enter to continue")

    for x in terms:
        if x in programs:
            term = True

    if not term:
        for x in terms:
            print(f"{terms.index(x)}: {x}")
        try:
            
            data = prompt("Enter the index of the terminal program to attempt to install")
            STR = f"sudo apt-get install {terms[int(data)]}"
            subprocess.run(STR.split(" "))
        except ValueError:
            STR = f"sudo apt-get install tilix"
            subprocess.run(STR.split(" "))

    for x in commands:
        if commands.index(x) < 3:
            subprocess.run(x.split(" "))

    for x in command_one:
        subprocess.run(x.split(" "))

except Exception as e:
    print(traceback.format_exc())
    print(f"[!] Error: [{e}]. Happened during setup script execution. program was not installed properly. Please "
              f"Rerun ./setup.py from install location")
