import sys
fileName = sys.argv[1];
f = open(fileName, "r")
count = 1
for lines in f:
	if count%2 == 0:
		print lines,
	count+=1