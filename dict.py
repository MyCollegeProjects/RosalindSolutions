import sys
s = sys.argv[1]
data = s.split(' ')
count = 0
for x in range(0, len(data), 1):
	if data[x]!='#':
		print data[x]+" ",
		count = data.count(data[x])
		t = data[x]
		for y in range(x+1, len(data), 1):
			if t == data[y]:
				data[y] = '#'
				data[x] = '#'
		print str(count)