import sys

def comp_gc(lst):
	gCount = float(lst.count("G"))
	cCount = float(lst.count("C"))
	length = float(len(lst))
	gFreq = (gCount/length)*100.0
	cFreq = (cCount/length)*100.0
	return gFreq+cFreq

def main():
	ipf = sys.argv[1]
	f = open(ipf, "r")
	fLst = []
	dnaLst = []
	freqLst = []
	flat = ''
	gcLst = []
	count = 0
	for lines in f:
		lst = list(lines)

		if lst[0] == '>':
			if count > 0:
				string = flat.replace('\n', '')
				dnaLst.append(string)
				flat = ''

			fastaName = ''.join(lst[1:])
			fLst.append(fastaName.replace('\n', ''))

		else:
			flat += lines

		count+=1

	dnaLst.append(flat.replace('\n', ''))

	for x in range(0, len(fLst), 1):
		gcLst.append(comp_gc(list(dnaLst[x])))

	print fLst[gcLst.index(max(gcLst))]
	print "%.6f"%max(gcLst)

if '__name__' == main():
	main()