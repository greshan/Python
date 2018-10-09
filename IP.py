import sys

args=sys.argv[1]
count = 0;
with open("IP.txt") as f:
	for line in f:
		if args in line:
			count = count+1;
print("IP present: ",args)
print("No of times the ip repeats: ",count)
sys.exit()
