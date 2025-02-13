#!/bin/bash
cd $HOME
echo "updating system and apt"
sudo apt-get update && sudo apt-get full-upgrade -y
sudo apt-get install nmap gcc g++ zsh nano adb fastboot python3-prompt-toolkit python3-requests git tilix curl heindall-flash -y

echo "installing gh cli clent!"
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

sudo apt install gh -y
gh auth login

echo "Downloading pycharm-community"
wget https://download.jetbrains.com/python/pycharm-community-2024.3.2.tar.gz

echo "Extracting pycharm"
tar -xf pycharm-community-2024.3.2.tar.gz
mv pycharm-community-2024.3.2 $HOME/.pycharm

echo "Making executable for pycharm"
printf '#include <stdio.h>\nint main(){\nsystem("bash $HOME/.pycharm/bin/pycharm.sh");}' > pycharm.c


echo "Compiling executable"
gcc pycharm.c -o pycharm

echo "Making desktop file and app drawer icon"
printf "[Desktop Entry]\nName=Pycharm\nComment=JetBrains Python IDE\nExec=/bin/pycharm\nIcon=/usr/share/icons/locolor/16x16/apps/pycharm.png\nTerminal=true\nType=Application\nCategories=Utility" > pycharm.desktop

echo "Moving icon"
sudo cp $HOME/.pycharm/bin/pycharm.png /usr/share/icons/locolor/16x16/apps/

rm pycharm.c

echo "Moving pycharm to /bin folder"
sudo mv pycharm /bin/pycharm

echo "Changing permissions"
sudo chmod +x /bin/pycharm

echo "Downloading SuperSploit"
gh repo clone don970/SuperSploit-chrome-OS

echo "Installing SuperSploit to home"
mv SuperSploit-chrome-OS .SuperSploit

echo "setting up supersploit"
sudo apt-get install python3-prompt-toolkit python3-requests -y
sudo bash $HOME/.SuperSploit/executable.sh

echo "installing oh my zsh"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo "Installing zsh plugins"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
echo "Copy this to .zshrc plugins: zsh-autosuggestions"
echo "All Finished."
