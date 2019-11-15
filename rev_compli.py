import sys
def rev_complement_dna(s):
	r = s[::-1]
	c = list(r)
	for x in range(0, len(c), 1):
		if c[x] == 'A':
			c[x] = 'T'
		elif c[x] == 'T':
			c[x] = 'A'
		elif c[x] == 'C':
			c[x] = 'G'
		elif c[x] == 'G':
			c[x] = 'C'

	return ''.join(c)

def main():
	string = sys.argv[1]
	print "The rc"
	print rev_complement_dna(string)

if "__name__" == main():
	main()