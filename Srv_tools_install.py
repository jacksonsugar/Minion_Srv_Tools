import os
import platform
import time

cwd = os.getcwd()

usrHome = str(os.path.expanduser("~"))

system = platform.system()

def mkbash_safe(path):
    if os.path.isfile(path) == True:
        print("\n .bashrc already exists!")

    elif os.path.isfile(path) == False:
        os.system("touch {}".format(path))

    else:
        print("Mistakes were made here")
        exit(0)

    fullpath = "{}".format(path)
    return fullpath

if system == 'Darwin':
	print('Detected MacOS, Creating .bashrc file in home directory {}'.format(usrHome))
	fullpath = mkbash_safe('{}/.bashrc'.format(usrHome))
else:
	os.system('sudo apt-get -y install net-tools openssh-server openssh-client build-essential gcc avrdude arduino gparted')

alias_lscp = 'alias lscp="sudo python {}/source/lscp.py"'.format(cwd)

print(alias_lscp)

alias_mssh = 'alias mssh="sudo python {}/source/mssh.py"'.format(cwd)

print(alias_mssh)

os.system("echo '{}\n' >> {}/.bashrc".format(alias_lscp, usrHome))
os.system("echo '{}\n' >> {}/.bashrc".format(alias_mssh, usrHome))

