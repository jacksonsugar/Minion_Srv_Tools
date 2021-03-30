import os
import sys
import time

cwd = os.getcwd()

usrHome = str(os.path.expanduser("~"))

def yes_no(answer):
    yes = set(['yes','y', 'ye', 'yeet', ''])
    no = set(['no','n'])

    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond with 'yes' or 'no'\n")

def mkdir_safe(path):
	if os.path.isdir(path) == True:
		print("\nDirectory: [{}] already exists. \n\nProcess stopped to protect files.".format(path))
		exit(0)

	elif os.path.isdir(path) == False:
		os.system("mkdir {}".format(path))

	else:
		print("Mistakes were made here")
		exit(0)


# to simplify the {scp remote_username@10.10.0.2:/remote/file.txt /local/directory}
try:
    numMinion = sys.argv[1]

except:
    numMinion = ''

try:
    dataType = str(sys.argv[2])

except:
    dataType = ''

if numMinion == '':
    print(numMinion)
    print('No file specified in argument. Please use form: mtest [Minion Number] [Test_Type]')
    exit(0)

if numMinion == '-h':

    print('This script is designed to be used remotely from the MINION')
    print('Execute this local script to retrieve test data from a remote host\n')
    print('Use the form: mtest [Minion Number] [Test_Type]\n\n')
    print('[Test Types: pics, data, both]')
    print('[data] test type yields sensor data informed by the config file\n')
    exit(0)

numMinion = int(numMinion)

hostMinion = 'pi@192.168.0.{}'.format(numMinion)

HOST_UP  = True if os.system("ping -c 1 -W 1 192.168.0.{}".format(numMinion)) is 0 else False

if HOST_UP == False:
    print('Minion [{}] not connected to WIFI'.format(numMinion))
    exit(0)

Destination = yes_no('Do you wish to save files to {}/Desktop/? [Y/N] : '.format(usrHome))

if Destination == False:
    Destination = raw_input("Please specify local file destination: {}/".format(usrHome))
    Destination = Destination.strip("/")
    Destination = "{}/{}/Minion_{}".format(usrHome, Destination, numMinion)
    mkdir_safe(Destination)

else:
    Destination = '{}/Desktop/Minion_{}'.format(usrHome,numMinion)
    mkdir_safe(Destination)

if dataType == 'pics':
    

elif dataType == 'data':
    

elif dataType == '' or 'both':
    
    
else:
    print('Please specify either [pics] or [data]')