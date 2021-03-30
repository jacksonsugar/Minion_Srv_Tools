import os
import sys

numMinion = ''

try:
    numMinion = sys.argv[1]
    int(numMinion)

except:
	if numMinion == '-h':
		print("\nUsed as: mssh (Minion_number)\n")
		exit(0)

	else:
		numMinion = raw_input('Which Minion (#) would you like to connect to? : ')

		try:
			int(numMinion)
		except:
			print('Host pi@192.168.0.{} does not exist'.format(numMinion))
			exit(0)

HOST_UP  = True if os.system("ping -c 1 -W 1 192.168.0.{}".format(numMinion)) is 0 else False

if HOST_UP == False:
    print('Minion [{}] not connected to WIFI'.format(numMinion))
    exit(0)

os.system('sudo ssh pi@192.168.0.{}'.format(numMinion))