#!/usr/bin/env bash
sudo apt-get install python3-prompt-toolkit -y
sudo apt-get install python3-pyfiglet -y
sudo apt-get install netcat-traditional adb fastboot pip -y

echo "Checking for terminal"

if [ -f "/bin/tilix" ]; then
  sleep
else
  sudo apt-get install tilix
fi


pip install --break-system-packages pure-python-adb pwn pybluez
bash <( curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install )
sudo mv ./phoneinfoga /usr/local/bin/phoneinfoga
cwd=pwd
cd $HOME/.SuperSploit/source/core/reconCore/external_tools/ && git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng && pip install --break-system-packages -r REQUIREMENTS
cd $CWD
bash executable.sh
