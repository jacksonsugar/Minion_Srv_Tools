import os
import time

cwd = os.getcwd()

usrHome = str(os.path.expanduser("~"))

os.system('sudo apt-get -y install net-tools openssh-server openssh-client build-essential gcc avrdude arduino gparted')

alias_lscp = 'alias lscp="sudo python {}/lscp.py"'.format(cwd)

print(alias_lscp)

alias_mssh = 'alias mssh="sudo python {}/mssh.py"'.format(cwd)

print(alias_mssh)

os.system("echo '{}\n' >> {}/.bashrc".format(alias_lscp, usrHome))
os.system("echo '{}\n' >> {}/.bashrc".format(alias_mssh, usrHome))
