# Introduce
It is feature detached from <a href="https://github.com/shuairuan/orsh">ORSH</a>. But we made a lot of changes and added more features.__The ORSH one is just a shrinked one...__**But anyways.**
We used suo.im's free api.
Made by python.
Before you use this program, please install python 3 and requests. You are install these using following command.
**If you want to unattended use, please see the manual.**

## Windows
Go to <a href="http://python.org/downloads"> http://python.org/downloads</a> to download the latest installer. Then install.

Then run following command.
```shell
pip install requests
```

## Linux
Most of Linux have been installed both python2 and python3 you may now need to install again. But if you didn't, you can install it.
```shell
sudo apt update
sudo apt install python3
```
Or if you are Arch Linux.
```shell
sudo pacman -Syyu
sudo pacman -S python3
```

Then run 
```shell
pip
```

If it reported error, you need to install it by following command.
```shell
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
```





Run this command to install required libraries.
```shell
pip3 install requests
```

If it errored, please run this command.
```shell
pip install requests
```

If it still don't working, please add 'sudo' at first.

# Files

main.py:Main program.

.gitignore:Clone ignore, you can delete it.

README.md:Manual.

history.txt: History.

usc.py: Unattend script creator.

unattend.py: Unattend run.
