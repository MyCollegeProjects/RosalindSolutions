import sys

def k_split(s, length):
	lst = []
	for x in range(0, len(s), length):
		lst.append(s[x:x+length])
	return lst

def main():
	fn = sys.argv[1]
	fs = open(fn, "r")
	lst = []
	table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I',
				'GUA': 'V','UUG': 'L','CUG': 'L','AUG': 'M','GUG': 'V','UCU': 'S','CCU': 'P','ACU': 'T','GCU': 'A','UCC': 'S','CCC': 'P',
				'ACC': 'T','GCC': 'A','UCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A','UCG': 'S','CCG': 'P','ACG': 'T','GCG': 'A','UAU': 'Y',
				'CAU': 'H','AAU': 'N','GAU': 'D','UAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D','UAA': 'Stop','CAA': 'Q','AAA': 'K',
				'GAA': 'E','UAG': 'Stop','CAG': 'Q','AAG': 'K','GAG': 'E','UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G','UGC': 'C',
				'CGC': 'R','AGC': 'S','GGC': 'G','UGA': 'Stop','CGA': 'R','AGA': 'R','GGA': 'G','UGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G'}

	for line in fs:
		lst = k_split(line, 3)

	op = ''
	for x in range(0, len(lst), 1):
		if table[lst[x]] != 'Stop':
			op+=table[lst[x]]

	print op

if '__name__' == main():
	main()