if [ -d "$HOME/.SuperSploit" ]; then
  if [ $UID == 0 ]; then
    echo "Do not run as root"
    exit
  else
    sleep 0
  fi
  cd $HOME/.SuperSploit && python3 source/main.py
else
  if [ $UID == 0 ]; then
    echo "Do not run as root"
    exit
  else
    sleep 0
  fi
  cd /home/donald/.SuperSploit/ && python3 source/main.py
fi