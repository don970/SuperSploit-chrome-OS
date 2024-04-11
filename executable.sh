#!/bin/bash
echo "Making supersploit executable"
printf '#include <stdio.h>\nint main(){\nsystem("bash $HOME/.SuperSploit/start.sh");}' > supersploit.c
echo "Compiling executable"
gcc supersploit.c -o supersploit
echo "Moving  supersploit to /bin folder"
sudo mv supersploit /bin/supersploit
echo "Making desktop file and app drawer icon"
printf "[Desktop Entry]\nName=supersploit\nComment=Exploit Management framework\nExec=/bin/supersploit\nIcon=logo1.png\nTerminal=true\nType=Application\nCategories=Utility" > supersploit.desktop
sudo cp supersploit.desktop /usr/share/applications/
echo "Moving icon"
sudo cp logo1.png /usr/share/icons/locolor/16x16/apps/
echo "Changing permissions for executable file"
sudo chmod +x /bin/supersploit
sudo rm supersploit.desktop