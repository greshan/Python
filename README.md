# Python

import sys

args=sys.argv[1]

with open("IP.txt") as f:
	for line in f:
		if args in line:
			print("IP present: ",args)

sys.exit() 
